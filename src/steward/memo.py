"""The agent's recommendation: schema, deterministic checks, and the weekly report.

Checks (all must pass before a memo is accepted):
- every claim cites ledger ids that exist in this week's ledger;
- every metric number in the text (a number with a decimal point, or with %, bps, $ or pp)
  matches a value in the cited entries, or the difference of two of them, within rounding;
- improvement words ("better", "lower error", ...) agree with the sign of the cited change;
- a "switch" needs a passed `promote` for that same challenger, and cites it;
- length limits.
A memo that fails gets the list of errors back; after 3 failed submissions the week is escalated.
"""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from .run import Run
from .settings import SETTINGS
from .space import ModelConfig, save_config

MAX_SUBMISSIONS = 3


class Claim(BaseModel):
    model_config = ConfigDict(extra="forbid")
    claim: str = Field(max_length=300)
    ledger_ids: list[str] = Field(min_length=1)


class Recommendation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    decision: Literal["keep", "switch"]
    challenger: str | None = None  # saved config name or config key, required for "switch"
    diagnosis: str = Field(max_length=500)
    evidence: list[Claim] = Field(min_length=1, max_length=6)
    risks: str = Field(max_length=400)
    watch_next_week: str = Field(max_length=300)


# ---------------------------------------------------------------- number matching
NUM = re.compile(
    r"(?<![\w.])(?P<dollar>\$)?(?P<num>[+\-−]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)(?P<scale>[kM])?"
    r"(?:\s?(?P<unit>%|bps|bp|pp|basis points))?(?![\w])")
DATE = re.compile(r"\d{4}-\d{2}(?:-\d{2})?")


def metric_numbers(text: str) -> list[tuple[str, float, float]]:
    """(as written, value, tolerance) for every metric number in `text`."""
    text = DATE.sub(" ", text)
    out = []
    for m in NUM.finditer(text):
        raw = m.group("num").replace(",", "").replace("−", "-")
        has_unit = bool(m.group("unit") or m.group("dollar"))
        if "." not in raw and not has_unit:
            continue  # plain integers ("4 weeks", "30 trials") are not checked
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        scale = {"k": 1e3, "M": 1e6}.get(m.group("scale") or "", 1.0)
        value = abs(float(raw)) * scale
        tol = 0.5 * 10 ** -decimals * scale + 1e-9
        out.append((m.group(0).strip(), value, tol))
    return out


def _flatten(obj) -> list[float]:
    if isinstance(obj, bool):
        return []
    if isinstance(obj, (int, float)):
        return [float(obj)]
    if isinstance(obj, dict):
        return [x for v in obj.values() for x in _flatten(v)]
    if isinstance(obj, list):
        return [x for v in obj for x in _flatten(v)]
    return []


def allowed_values(entries: list[dict]) -> list[float]:
    vals = {abs(v) for e in entries for v in _flatten(e["result"])}
    vals |= {v * 100 for v in vals if v <= 1.5}  # rates written as percentages
    base = sorted(vals)
    vals |= {abs(a - b) for a, b in itertools.combinations(base, 2)} if len(base) < 400 else set()
    return sorted(vals)


IMPROVE = re.compile(r"\b(better|improv\w*|outperform\w*|beats?|lower error|reduc\w*|smaller error)\b", re.I)
WORSE = re.compile(r"\b(worse|deteriorat\w*|underperform\w*|higher error|larger error|degrad\w*)\b", re.I)
CHANGE_KEYS = ("mae_change_vs_champion_pct", "cv_change_pct", "change_last_26w_vs_prior_pct")


def _changes(entries: list[dict]) -> list[float]:
    return [e["result"][k] for e in entries for k in CHANGE_KEYS
            if isinstance(e["result"].get(k), (int, float))]


# ---------------------------------------------------------------- checks
def check(rec: Recommendation, run: Run) -> list[str]:
    ledger = {e["id"]: e for e in run.ledger() if e["command"] != "submit"}
    errors: list[str] = []
    for i, c in enumerate(rec.evidence, 1):
        missing = [x for x in c.ledger_ids if x not in ledger]
        if missing:
            errors.append(f"evidence {i}: ledger ids {missing} don't exist this week")
            continue
        cited = [ledger[x] for x in c.ledger_ids]
        allowed = allowed_values(cited)
        for written, value, tol in metric_numbers(c.claim):
            if not any(abs(value - a) <= tol for a in allowed):
                errors.append(f"evidence {i}: '{written}' doesn't match any value in {c.ledger_ids}")
        changes = _changes(cited)
        if changes and IMPROVE.search(c.claim) and not WORSE.search(c.claim) and all(x > 0 for x in changes):
            errors.append(f"evidence {i}: says better/improved, but the cited change is positive (worse)")
        if changes and WORSE.search(c.claim) and not IMPROVE.search(c.claim) and all(x < 0 for x in changes):
            errors.append(f"evidence {i}: says worse, but the cited change is negative (better)")
    for field in ("diagnosis", "risks", "watch_next_week"):
        if metric_numbers(getattr(rec, field)):
            errors.append(f"{field}: put numbers in evidence claims (with ledger ids), not here")

    promo = run.state.get("promotion")
    promo_ids = [e["id"] for e in ledger.values() if e["command"] == "promote"]
    cited_all = {x for c in rec.evidence for x in c.ledger_ids}
    if promo_ids and not set(promo_ids) & cited_all:
        errors.append(f"cite the promotion test result ({promo_ids[0]}) in the evidence")
    if rec.decision == "switch":
        if not promo:
            errors.append("decision 'switch' needs a `promote` call first")
        elif not promo["passed"]:
            errors.append("decision 'switch' is blocked: the challenger failed the promotion rule")
        else:
            key = ModelConfig.model_validate(promo["config"]).key()
            ok = rec.challenger in (key,) or (rec.challenger and run.config_path(rec.challenger).exists()
                                              and _key_of(run, rec.challenger) == key)
            if not ok:
                errors.append(f"'challenger' must name the promoted config (key {key})")
    return errors


def _key_of(run: Run, name: str) -> str:
    return ModelConfig.model_validate_json(run.config_path(name).read_text()).key()


# ---------------------------------------------------------------- submit and report
def submit(run: Run, source: str | Path | dict) -> dict:
    if run.state["status"] != "open":
        raise RuntimeError(f"this run is {run.state['status']}")
    try:
        if isinstance(source, dict):
            rec = Recommendation.model_validate(source)
        else:
            text = str(source)
            if not text.lstrip().startswith("{") and not Path(source).exists():
                raise FileNotFoundError(f"{source} not found: write the memo there first (not counted as a try)")
            text = text if text.lstrip().startswith("{") else Path(source).read_text()
            rec = Recommendation.model_validate_json(text)
        errors = check(rec, run)
        raw = rec.model_dump()
    except ValidationError as e:
        errors = [f"{'.'.join(map(str, x['loc']))}: {x['msg']}" for x in e.errors()]
        rec, raw = None, source if isinstance(source, dict) else None

    n = run.state["submissions"] + 1
    run.update(submissions=n)
    entry = run.log("submit", {"recommendation": raw}, {"accepted": not errors, "errors": errors, "attempt": n})
    if errors:
        if n >= MAX_SUBMISSIONS:
            run.update(status="escalated")
            path = write_report(run, None, escalated=errors)
            return {"accepted": False, "escalated": True, "errors": errors, "report": str(path)}
        return {"accepted": False, "errors": errors, "attempts_left": MAX_SUBMISSIONS - n,
                "ledger_id": entry["id"]}

    new_champion = run.champion
    if rec.decision == "switch":
        new_champion = ModelConfig.model_validate(run.state["promotion"]["config"])
    run.update(status="submitted", decision=rec.decision, first_try=(n == 1),
               new_champion=new_champion.model_dump(mode="json"))
    path = write_report(run, rec)
    if run.state["mode"] == "live" and rec.decision == "switch":
        save_config(new_champion, SETTINGS.champion_file)
    return {"accepted": True, "decision": rec.decision, "report": str(path),
            "champion": new_champion.label()}


def _ledger_line(e: dict) -> str:
    r = e["result"]
    c = e["command"]
    if c == "backtest":
        return f"{r['label']}: MAE {r['mae_bps']} bps ({r['mae_change_vs_champion_pct']:+}% vs champion)"
    if c == "tune":
        return f"{r['label']}: CV MAE {r['cv_mae_bps_start']} → {r['cv_mae_bps_best']} bps"
    if c == "promote":
        return (f"{r['challenger']}: {r['challenger_mae_bps']} vs {r['champion_mae_bps']} bps, "
                f"p = {r['dm_p_value']}, {'passed' if r['passed'] else 'failed'}")
    if c == "champion-report":
        m = r["mae_bps"]
        return f"champion MAE last 4w {m['last_4w']}, last 26w {m['last_26w']}, prior 26w {m['prior_26w']} bps"
    if c == "diagnose":
        return f"diagnosis of {r['config']}"
    if c == "data-summary":
        return f"market data through {r['data_through']}"
    if c == "submit":
        return "accepted" if r["accepted"] else f"rejected: {len(r['errors'])} error(s)"
    return ""


def _safe_line(e: dict) -> str:
    try:
        return _ledger_line(e)
    except (KeyError, TypeError):
        return ""


def write_report(run: Run, rec: Recommendation | None, escalated: list[str] | None = None) -> Path:
    s = run.state
    lines = [f"# Weekly model review: {s['cutoff']}", ""]
    if rec is None:
        lines += ["**Status: escalated.** The agent's memo failed the checks three times, so no "
                  "recommendation is made this week and the champion stays. Last errors:", ""]
        lines += [f"- {e}" for e in escalated or []]
    else:
        champ = run.champion
        new = ModelConfig.model_validate(s["new_champion"])
        verb = "Switch" if rec.decision == "switch" else "Keep"
        lines += [f"**Decision: {verb}.** Champion: `{new.label()}`"
                  + (f" (was `{champ.label()}`)" if rec.decision == "switch" else ""), "",
                  f"**What changed:** {rec.diagnosis}", "", "## Evidence", ""]
        lines += [f"- {c.claim} ({', '.join(c.ledger_ids)})" for c in rec.evidence]
        lines += ["", f"**Risks:** {rec.risks}", "", f"**Watch next week:** {rec.watch_next_week}"]
    used = s["used"]
    lines += ["", "## Ledger", "",
              f"Budget used: backtests {used.get('backtest', 0)}, tunes {used.get('tune', 0)}, "
              f"promotion tests {used.get('promote', 0)}. Memo submissions: {s['submissions']}.", "",
              "| Id | Command | Result |", "|---|---|---|"]
    lines += [f"| {e['id']} | {e['command']} | {_safe_line(e)} |" for e in run.ledger()]
    text = "\n".join(lines) + "\n"
    path = (SETTINGS.reports_dir / "weekly" / f"{s['cutoff']}.md") if s["mode"] == "live" else run.path / "report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    (run.path / "recommendation.json").write_text(json.dumps(rec.model_dump() if rec else None, indent=2) + "\n")
    return path

"""Replay: run a brain on past weeks, then score each decision on the 12 weeks that followed.

Every replayed week starts from the same initial champion (Project 3's tuned XGBoost setup),
so weeks are independent and all methods are compared on equal footing: same starting point,
same budget, same rule. Each week's run folder keeps its ledger, memo and score.
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import numpy as np
import pandas as pd

from .backtest import metrics, walk_forward
from .data import CORRIDORS, SERIES, dataset, last_date, load_all
from .run import Run
from .settings import ROOT, SETTINGS
from .space import HALFLIVES, ModelConfig, load_config

INITIAL_CHAMPION = ROOT / "configs" / "initial_champion.json"
REPLAY_DIR = SETTINGS.runs_dir / "replay"
FIRST_WEEK = "2024-01-05"


def replay_weeks(first: str = FIRST_WEEK) -> list[pd.Timestamp]:
    """Fridays from `first` whose 12 following weeks are fully in the data."""
    last = last_date() - pd.Timedelta(days=SETTINGS.future_days + 7)
    return list(pd.date_range(first, last, freq="W-FRI"))


def future_score(cfg: ModelConfig, cutoff: pd.Timestamp) -> dict:
    """The config deployed at the cutoff, refit on its own schedule, scored on the next 12 weeks."""
    cache = SETTINGS.cache_dir / "future" / f"{cfg.key()}_{cutoff:%Y-%m-%d}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    end = cutoff + pd.Timedelta(days=SETTINGS.future_days)
    m = metrics(walk_forward(cfg, cutoff, end, visible_until=end))
    out = {"mae_bps": m["mae_bps"], "mae_usd": m["mae_usd"], "breach_rate": m["breach_rate"]}
    cache.parent.mkdir(parents=True, exist_ok=True)
    tmp = cache.with_suffix(f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(out))
    tmp.replace(cache)
    return out


def run_week(method: str, cutoff: pd.Timestamp, brain=None) -> Path:
    """Run one brain on one week (skipped if already done), then score it."""
    path = REPLAY_DIR / method / f"{cutoff:%Y-%m-%d}"
    done = (path / "state.json").exists() and Run(path).state["status"] != "open"
    if brain is not None and not done:
        if path.exists():
            shutil.rmtree(path)
        run = Run.start(cutoff, load_config(INITIAL_CHAMPION), path=path, mode="replay")
        brain(run)
    if (path / "state.json").exists() and Run(path).state["status"] != "open":
        score_week(Run(path), method)
    return path


def score_week(run: Run, method: str) -> dict:
    s = run.state
    start = ModelConfig.model_validate(s["champion"])
    chosen = ModelConfig.model_validate(s.get("new_champion") or s["champion"])
    promo = s.get("promotion")
    proposed = ModelConfig.model_validate(promo["config"]) if promo else None
    fs, fc = future_score(start, run.cutoff), future_score(chosen, run.cutoff)
    fp = future_score(proposed, run.cutoff) if proposed else None
    row = {
        "method": method, "cutoff": s["cutoff"], "status": s["status"],
        "decision": s.get("decision", "keep"), "first_try": s.get("first_try", False),
        "submissions": s["submissions"], **{f"used_{k}": v for k, v in s["used"].items()},
        "proposed": proposed.label() if proposed else None,
        "rule_passed": promo["passed"] if promo else None,
        "chosen": chosen.label(),
        "start_future_mae_bps": fs["mae_bps"], "chosen_future_mae_bps": fc["mae_bps"],
        "proposed_future_mae_bps": fp["mae_bps"] if fp else None,
        "start_future_mae_usd": fs["mae_usd"], "chosen_future_mae_usd": fc["mae_usd"],
        "proposed_future_mae_usd": fp["mae_usd"] if fp else None,
        "chosen_future_breach_rate": fc["breach_rate"],
    }
    (run.path / "score.json").write_text(json.dumps(row, indent=1) + "\n")
    return row


def collect() -> pd.DataFrame:
    rows = [json.loads(p.read_text()) for p in sorted(REPLAY_DIR.glob("*/*/score.json"))]
    return pd.DataFrame(rows)


def summarize(weeks: pd.DataFrame, on_weeks: list[str] | None = None) -> pd.DataFrame:
    """One row per method: future error of the models it chose vs never retraining.

    `if_rule_ignored` is the error had every proposed challenger been accepted without the rule.
    """
    w = weeks if on_weeks is None else weeks[weeks["cutoff"].isin(on_weeks)]
    out = []
    for method, g in w.groupby("method"):
        alt = g["proposed_future_mae_bps"].fillna(g["start_future_mae_bps"])
        alt_usd = g["proposed_future_mae_usd"].fillna(g["start_future_mae_usd"])
        base, chosen = g["start_future_mae_bps"].mean(), g["chosen_future_mae_bps"].mean()
        out.append({
            "method": method, "weeks": len(g),
            "switches": int((g["decision"] == "switch").sum()),
            "promotion_tests": int(g["proposed"].notna().sum()),
            "future_MAE_bps": round(chosen, 3),
            "future_MAE_usd": round(g["chosen_future_mae_usd"].mean()),
            "change_vs_never_pct": round((chosen - base) / base * 100, 3),
            "if_rule_ignored_MAE_bps": round(alt.mean(), 3),
            "if_rule_ignored_MAE_usd": round(alt_usd.mean()),
            "weeks_better_than_never": int((g["chosen_future_mae_bps"] < g["start_future_mae_bps"]).sum()),
            "weeks_worse_than_never": int((g["chosen_future_mae_bps"] > g["start_future_mae_bps"]).sum()),
            "memo_first_try_pass_rate": round(g["first_try"].mean(), 3),
            "escalations": int((g["status"] == "escalated").sum()),
        })
    order = {"never": 0, "scripted": 1, "automation": 2, "agent": 3}
    return pd.DataFrame(out).sort_values("method", key=lambda s: s.map(order)).reset_index(drop=True)


def sample_weeks(n: int = 16, seed: int = SETTINGS.seed) -> list[str]:
    """A stratified sample of replay weeks for the AI agent: equal shares of calm, normal and
    volatile weeks, by the average 20-day FX volatility across corridors at the cutoff."""
    market, _ = load_all()
    trading = market[market["is_trading_day"]]
    vol = pd.concat([np.log(trading[s]).diff().rolling(20).std() for s in SERIES[:len(CORRIDORS)]], axis=1)
    pct = vol.rank(pct=True).mean(axis=1)
    weeks = replay_weeks()
    level = pd.Series([pct.loc[:w].iloc[-1] for w in weeks], index=weeks)
    tiers = pd.qcut(level.rank(method="first"), 3, labels=["calm", "normal", "volatile"])
    rng = np.random.default_rng(seed)
    picks = []
    for i, tier in enumerate(["calm", "normal", "volatile"]):
        pool = list(level.index[tiers == tier])
        k = n // 3 + (1 if i < n % 3 else 0)
        picks += list(rng.choice(pool, size=min(k, len(pool)), replace=False))
    return sorted(f"{pd.Timestamp(w):%Y-%m-%d}" for w in picks)


def warm_cache() -> None:
    for hl in HALFLIVES:
        dataset(hl)

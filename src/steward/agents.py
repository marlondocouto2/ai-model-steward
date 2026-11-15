"""Non-AI "brains" that use exactly the same tools and budget as the AI agent.

- `never`:      keep the champion; no tool calls (the never-retrain baseline).
- `scripted`:   a fixed playbook a careful analyst might follow (also the CI dry run).
- `automation`: Optuna searches the whole config space with the same budget, then tunes
                the winner. No judgement, just search.

Both `scripted` and `automation` promote their best development candidate whenever it beats
the champion there; the promotion rule then decides. Their memos are built from ledger values,
so they always pass the checks.
"""

from __future__ import annotations

import optuna

from . import memo, tools
from .run import BudgetExceeded, Run
from .space import ALL_GROUPS, ModelConfig


# ---------------------------------------------------------------- shared
def _best(run: Run) -> dict | None:
    rows = [e for e in run.ledger() if e["command"] == "backtest"]
    return min(rows, key=lambda e: e["result"]["mae_bps"]) if rows else None


def _finish(run: Run, report: dict, best: dict | None) -> dict:
    """Promote the best candidate if it beat the champion in development, then submit a memo."""
    promo = None
    if best and best["result"]["mae_change_vs_champion_pct"] < 0:
        promo = tools.promote(run, best["result"]["name"])
    r = report["result"]
    m = r["mae_bps"]
    trend = "up" if r["change_last_26w_vs_prior_pct"] > 0 else "down"
    evidence = [{"claim": (f"The champion's error over the last 26 weeks was {m['last_26w']} bps vs "
                           f"{m['prior_26w']} bps in the prior 26 weeks ({r['change_last_26w_vs_prior_pct']:+}%)."),
                 "ledger_ids": [report["id"]]}]
    if best:
        b = best["result"]
        evidence.append({"claim": (f"The best development candidate, {b['label']}, scored {b['mae_bps']} bps vs "
                                   f"the champion's {b['champion_mae_bps']} bps ({b['mae_change_vs_champion_pct']:+}%)."),
                         "ledger_ids": [best["id"]]})
    if promo:
        p = promo["result"]
        verdict = "passed the promotion rule" if p["passed"] else "failed the promotion rule"
        evidence.append({"claim": (f"On the hidden window it scored {p['challenger_mae_bps']} bps vs the champion's "
                                   f"{p['champion_mae_bps']} bps (p = {p['dm_p_value']}) and {verdict}."),
                         "ledger_ids": [promo["id"]]})
    switch = bool(promo and promo["result"]["passed"])
    rec = {
        "decision": "switch" if switch else "keep",
        "challenger": promo["result"]["config_key"] if switch else None,
        "diagnosis": f"The champion's development error is {trend} compared with the previous half-year.",
        "evidence": evidence,
        "risks": "Development results may not carry over to the next weeks if volatility changes.",
        "watch_next_week": "Whether the champion's recent error keeps moving in the same direction.",
    }
    return memo.submit(run, rec)


# ---------------------------------------------------------------- brains
def never(run: Run) -> dict:
    report = tools.champion_report(run)
    return _finish(run, report, None)


def scripted(run: Run) -> dict:
    """Coordinate search: family -> training window -> half-life -> refit -> tune -> backtest."""
    tools.data_summary(run)
    report = tools.champion_report(run)
    base = {"features": ALL_GROUPS, "train_window": "all", "refit_days": 30, "halflife": 10}
    results: dict[str, float] = {}

    def bt(cfg: dict, name: str) -> float:
        c = ModelConfig(**cfg)
        if c.key() not in results:
            results[c.key()] = tools.backtest(run, c, name)["result"]["mae_bps"]
        return results[c.key()]

    fams = {f: bt({**base, "family": f} if f != "ewma" else {"family": "ewma"}, f"{f}_all")
            for f in ("ewma", "ridge", "xgboost", "lightgbm")}
    fam = min((f for f in fams if f != "ewma"), key=fams.get)
    cur = {**base, "family": fam}
    for field, options in (("train_window", ("3y", "2y", "1y")), ("halflife", (5, 20)), ("refit_days", (7,))):
        best_val, best_mae = cur[field], bt(cur, "")
        for v in options:
            mae = bt({**cur, field: v}, f"{fam}_{field}_{v}")
            if mae < best_mae:
                best_val, best_mae = v, mae
        cur[field] = best_val
    tools.tune(run, ModelConfig(**cur), trials=20, name="best_tuned")
    tools.backtest(run, "best_tuned")
    return _finish(run, report, _best(run))


SEARCH_BACKTESTS = 13


def automation(run: Run) -> dict:
    """Optuna (TPE) over the whole config space, 13 backtests; then tune the winner and backtest it."""
    report = tools.champion_report(run)
    seen: dict[str, float] = {}

    def objective(t: optuna.Trial) -> float:
        fam = t.suggest_categorical("family", ["ewma", "ridge", "xgboost", "lightgbm"])
        groups = tuple(g for g in ALL_GROUPS if t.suggest_categorical(g, [True, False]))
        cfg = {"family": fam, "train_window": t.suggest_categorical("train_window", ["all", "3y", "2y", "1y"]),
               "refit_days": t.suggest_categorical("refit_days", [7, 30]),
               "halflife": t.suggest_categorical("halflife", [5, 10, 20])}
        if fam != "ewma":
            cfg["features"] = groups or ALL_GROUPS
        c = ModelConfig(**cfg)
        if c.key() not in seen:
            seen[c.key()] = tools.backtest(run, c, f"search_{len(seen) + 1:02d}")["result"]["mae_bps"]
        return seen[c.key()]

    study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler(seed=7))
    trials = 0
    while len(seen) < SEARCH_BACKTESTS and trials < 60:
        study.optimize(objective, n_trials=1)
        trials += 1
    best = _best(run)
    best_cfg = ModelConfig.model_validate_json(run.config_path(best["result"]["name"]).read_text())
    if best_cfg.family != "ewma":
        try:
            tools.tune(run, best_cfg, trials=20, name="best_tuned")
            tools.backtest(run, "best_tuned")
        except BudgetExceeded:
            pass
    return _finish(run, report, _best(run))


BRAINS = {"never": never, "scripted": scripted, "automation": automation}

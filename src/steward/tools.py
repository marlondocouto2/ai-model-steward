"""The agent's tools. Each returns a JSON-ready dict and records it in the run's ledger.

Visibility rules (enforced here, not by the agent):
- Market data is visible up to the cutoff W (it's past data at decision time).
- Model errors are visible only up to D = W - 8 weeks. The promotion window [D, W) is scored
  only inside `promote`, once per week.
"""

from __future__ import annotations

import numpy as np
import optuna
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from fx_margin.models import make_model

from . import rule
from .backtest import daily_loss, metrics, walk_forward
from .data import CORRIDORS, SERIES, dataset, load_all
from .run import Run
from .settings import BPS, SETTINGS
from .space import RANGES, ModelConfig, describe_space, save_config

optuna.logging.set_verbosity(optuna.logging.WARNING)


# ---------------------------------------------------------------- helpers
def _dev_preds(run: Run, cfg: ModelConfig) -> pd.DataFrame:
    """Development backtest: origins in the 26 weeks before D, nothing settled on/after D."""
    preds = run.load_preds(cfg)
    if preds is None:
        preds = walk_forward(cfg, run.dev_start, run.dev_end, visible_until=run.dev_end)
        run.save_preds(cfg, preds)
    return preds


def _backtested(run: Run) -> dict[str, dict]:
    """Configs backtested in this run: key -> {name, label, mae_bps, ledger id}."""
    out = {}
    for e in run.ledger():
        if e["command"] == "backtest":
            r = e["result"]
            out[r["config_key"]] = {"name": r["name"], "label": r["label"], "mae_bps": r["mae_bps"],
                                    "ledger_id": e["id"]}
    return out


def _resolve(run: Run, arg) -> tuple[ModelConfig, str]:
    """A config from a ModelConfig, a saved config name in this run, a file path, or inline JSON."""
    from .space import load_config
    if isinstance(arg, ModelConfig):
        return arg, arg.key()
    text = str(arg)
    if text == "champion":
        return run.champion, "champion"
    if not text.lstrip().startswith("{") and len(text) < 100:
        saved = run.config_path(text)
        if saved.exists():
            return load_config(saved), text
    cfg = load_config(text)
    return cfg, cfg.key()


def _pct(a: float, b: float) -> float:
    return round((a - b) / b * 100, 2)


# ---------------------------------------------------------------- tools
def status(run: Run) -> dict:
    s = run.state
    return {
        "cutoff": s["cutoff"], "mode": s["mode"], "status": s["status"],
        "development_window": {"from": f"{run.dev_start:%Y-%m-%d}", "to_before": s["dev_end"]},
        "promotion_window": {"from": s["dev_end"], "to": s["cutoff"],
                             "note": "hidden: only `promote` scores models here"},
        "champion": {"label": run.champion.label(), "config": s["champion"]},
        "budget_remaining": run.remaining(), "submissions": s["submissions"],
        "backtested": [{"key": k, **v} for k, v in _backtested(run).items()],
    }


def space(run: Run) -> dict:
    return describe_space()


def data_summary(run: Run) -> dict:
    """What the market did up to the cutoff, per corridor, vs its own history."""
    market, business = load_all()
    W = run.cutoff
    m = market.loc[:W]
    trading = m[m["is_trading_day"]]
    out = {"data_through": f"{trading.index.max():%Y-%m-%d}",
           "trading_days_last_7": int(m["is_trading_day"].loc[W - pd.Timedelta(days=6):W].sum()),
           "corridors": {}}
    for corridor, series in zip(CORRIDORS, SERIES):
        p = trading[series]
        ret = np.log(p).diff()
        vol20 = ret.rolling(20).std()
        hist = vol20.loc[W - pd.Timedelta(days=3 * 365):W].dropna()
        move_1w = float(np.log(p.iloc[-1] / p.iloc[-6]))
        sd60 = float(ret.iloc[-60:].std())
        b = business[(business["corridor"] == corridor) & (business["date"] <= W)].set_index("date")
        out["corridors"][corridor] = {
            "series": series, "last_rate": round(float(p.iloc[-1]), 4),
            "change_1w_pct": round((p.iloc[-1] / p.iloc[-6] - 1) * 100, 2),
            "change_4w_pct": round((p.iloc[-1] / p.iloc[-21] - 1) * 100, 2),
            "move_1w_z": round(move_1w / (sd60 * np.sqrt(5)), 2),
            "vol20_daily_bps": round(float(vol20.iloc[-1]) * BPS, 1),
            "vol20_percentile_3y": round(float((hist <= vol20.iloc[-1]).mean() * 100), 0),
            "markup_last_week_bps": round(float(b["markup"].iloc[-7:].mean()) * BPS, 1),
            "markup_prior_4w_bps": round(float(b["markup"].iloc[-35:-7].mean()) * BPS, 1),
        }
    dxy = trading[SERIES[-1]]
    out["dollar_index"] = {"last": round(float(dxy.iloc[-1]), 2),
                           "change_1w_pct": round((dxy.iloc[-1] / dxy.iloc[-6] - 1) * 100, 2),
                           "change_4w_pct": round((dxy.iloc[-1] / dxy.iloc[-21] - 1) * 100, 2)}
    return run.log("data-summary", {}, out)


def champion_report(run: Run) -> dict:
    """How the champion has done recently vs before, on the development window only."""
    champ = run.champion
    recent = _dev_preds(run, champ)
    prior = walk_forward(champ, run.dev_start - pd.Timedelta(days=SETTINGS.dev_eval_days), run.dev_start,
                         visible_until=run.dev_end)
    D = run.dev_end

    def since(days: int) -> pd.DataFrame:
        return recent[recent["origin"] >= D - pd.Timedelta(days=days)]

    m26, mprior = metrics(recent), metrics(prior)
    out = {
        "champion": champ.label(), "config_key": champ.key(),
        "mae_bps": {"last_4w": metrics(since(28))["mae_bps"], "last_13w": metrics(since(91))["mae_bps"],
                    "last_26w": m26["mae_bps"], "prior_26w": mprior["mae_bps"]},
        "change_last_26w_vs_prior_pct": _pct(m26["mae_bps"], mprior["mae_bps"]),
        "breach_rate_last_26w": m26["breach_rate"],
        "mae_usd_last_26w": m26["mae_usd"],
        "by_corridor": {c: {"mae_bps_last_4w": metrics(since(28)[since(28)["corridor"] == c])["mae_bps"],
                            "mae_bps_last_26w": m26["by_corridor"][c]["mae_bps"],
                            "mae_bps_prior_26w": mprior["by_corridor"][c]["mae_bps"],
                            "breach_rate_last_26w": m26["by_corridor"][c]["breach_rate"]}
                        for c in CORRIDORS},
    }
    return run.log("champion-report", {}, out)


def backtest(run: Run, config, name: str | None = None) -> dict:
    """Development backtest of one config, compared with the champion on the same days."""
    cfg, ref = _resolve(run, config)
    champ = run.champion
    if cfg.key() != champ.key():
        run.spend("backtest")
    name = name or (ref if not ref.startswith("{") else cfg.key())
    save_config(cfg, run.config_path(name))
    preds, champ_preds = _dev_preds(run, cfg), _dev_preds(run, champ)
    m, mc = metrics(preds), metrics(champ_preds)
    out = {
        "name": name, "config_key": cfg.key(), "label": cfg.label(),
        "mae_bps": m["mae_bps"], "rmse_bps": m["rmse_bps"], "mae_usd": m["mae_usd"],
        "breach_rate": m["breach_rate"],
        "champion_mae_bps": mc["mae_bps"],
        "mae_change_vs_champion_pct": _pct(m["mae_bps"], mc["mae_bps"]),
        "by_corridor": {c: {"mae_bps": m["by_corridor"][c]["mae_bps"],
                            "champion_mae_bps": mc["by_corridor"][c]["mae_bps"],
                            "breach_rate": m["by_corridor"][c]["breach_rate"]} for c in CORRIDORS},
        "window": {"from": m["from"], "to": m["to"], "days": m["days"]},
        "budget_remaining": run.remaining(),
    }
    return run.log("backtest", {"config": cfg.model_dump(mode="json"), "name": name}, out)


def diagnose(run: Run, config) -> dict:
    """Where a backtested config goes wrong: bias, weekday, volatility regime, month, worst days."""
    cfg, _ = _resolve(run, config)
    if cfg.key() != run.champion.key() and cfg.key() not in _backtested(run):
        raise ValueError("diagnose works on the champion or a config already backtested this week")
    preds = _dev_preds(run, cfg)
    feats = dataset(cfg.halflife)[["corridor", "origin", "vol_20"]]
    p = preds.merge(feats, on=["corridor", "origin"], how="left")
    p["err_bps"] = (p["margin_rate"] - p["forecast"]) * BPS
    p["abs_bps"] = p["err_bps"].abs()
    p["regime"] = p.groupby("corridor")["vol_20"].transform(
        lambda v: pd.qcut(v.rank(method="first"), 3, labels=["calm", "normal", "volatile"]))
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    r2 = lambda s: {str(k): round(float(v), 2) for k, v in s.items()}  # noqa: E731
    worst = p.nlargest(5, "abs_bps")
    out = {
        "config": cfg.label(), "config_key": cfg.key(),
        "bias_bps_by_corridor": r2(p.groupby("corridor")["err_bps"].mean()),
        "mae_bps_by_target_weekday": r2(p.groupby(p["target"].dt.dayofweek.map(dict(enumerate(days))))["abs_bps"].mean()
                                        .reindex(days).dropna()),
        "mae_bps_by_volatility_regime": r2(p.groupby("regime", observed=True)["abs_bps"].mean()),
        "mae_bps_by_month": r2(p.groupby(p["origin"].dt.strftime("%Y-%m"))["abs_bps"].mean()),
        "worst_days": [{"origin": f"{r.origin:%Y-%m-%d}", "corridor": r.corridor,
                        "error_bps": round(float(r.err_bps), 1)} for r in worst.itertuples()],
        "note": "error = realized - forecast; positive bias means the model forecasts too low",
    }
    return run.log("diagnose", {"config": cfg.model_dump(mode="json")}, out)


def tune(run: Run, config, trials: int = 20, name: str | None = None) -> dict:
    """Optuna search over the family's hyperparameters, with time-ordered CV on the 3 years
    before D. Saves the best config (to backtest next)."""
    cfg, ref = _resolve(run, config)
    if cfg.family == "ewma":
        raise ValueError("family 'ewma' has no hyperparameters to tune")
    trials = int(min(max(trials, 5), SETTINGS.tune_max_trials))
    run.spend("tune")
    D = run.dev_end
    data = dataset(cfg.halflife)
    pre = data[(data["settle_date"] < D) & (data["origin"] >= D - pd.Timedelta(days=3 * 365))]
    origins = np.sort(pre["origin"].unique())
    cols = cfg.columns()
    folds = list(TimeSeriesSplit(n_splits=SETTINGS.cv_splits).split(origins))

    def cv(params: dict) -> float:
        c = cfg.model_copy(update={"params": params})
        scores = []
        for _, val_idx in folds:
            cut = origins[val_idx[0]]
            tr = pre[pre["settle_date"] < cut]
            va = pre[pre["origin"].isin(origins[val_idx])]
            model = make_model(cfg.family, c.full_params()).fit(tr[cols], tr["resid"])
            scores.append(np.mean(np.abs(va["resid"] - model.predict(va[cols]))))
        return float(np.mean(scores)) * BPS

    def suggest(t: optuna.Trial) -> dict:
        out = {}
        for k, (lo, hi, typ, log) in RANGES[cfg.family].items():
            out[k] = (t.suggest_int(k, int(lo), int(hi), log=log) if typ is int
                      else t.suggest_float(k, lo, hi, log=log))
        return out

    study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler(seed=SETTINGS.seed))
    study.enqueue_trial(cfg.full_params()[cfg.family])
    study.optimize(lambda t: cv(suggest(t)), n_trials=trials)
    start_score = study.trials[0].value
    tuned = cfg.model_copy(update={"params": {k: (int(v) if RANGES[cfg.family][k][2] is int else round(float(v), 6))
                                              for k, v in study.best_params.items()}})
    tuned = ModelConfig.model_validate(tuned.model_dump())
    name = name or f"{(ref if not ref.startswith('{') else cfg.key())}_tuned"
    save_config(tuned, run.config_path(name))
    out = {"name": name, "config_key": tuned.key(), "label": tuned.label(), "trials": trials,
           "cv_mae_bps_start": round(start_score, 2), "cv_mae_bps_best": round(study.best_value, 2),
           "cv_change_pct": _pct(study.best_value, start_score), "params": tuned.params,
           "note": "CV error on the residual, 3 years before the development window end; "
                   "backtest the tuned config to compare it with the champion",
           "budget_remaining": run.remaining()}
    return run.log("tune", {"config": cfg.model_dump(mode="json"), "trials": trials}, out)


def promotion_scores(champ: ModelConfig, chall: ModelConfig, start: pd.Timestamp,
                     end: pd.Timestamp) -> tuple[dict, dict, float, float]:
    pc = walk_forward(champ, start, end, visible_until=end)
    pn = walk_forward(chall, start, end, visible_until=end)
    keys = ["corridor", "origin"]
    common = pc[keys].merge(pn[keys], on=keys)
    pc, pn = pc.merge(common, on=keys), pn.merge(common, on=keys)
    stat, p = rule.diebold_mariano(daily_loss(pc), daily_loss(pn))
    return metrics(pc), metrics(pn), stat, p


def promote(run: Run, challenger) -> dict:
    """Score champion and challenger on the hidden promotion window and apply the rule. Once a week."""
    cfg, ref = _resolve(run, challenger)
    if cfg.key() == run.champion.key():
        raise ValueError("the challenger is the champion")
    if cfg.key() not in _backtested(run):
        raise ValueError("backtest the challenger on the development window before promoting it")
    run.spend("promote")
    mc, mn, stat, p = promotion_scores(run.champion, cfg, run.dev_end, run.cutoff)
    verdict = rule.evaluate(mc["mae_bps"], mn["mae_bps"], p, mn["breach_rate"])
    out = {"challenger": cfg.label(), "config_key": cfg.key(), "name": ref,
           "window": {"from": mn["from"], "to": mn["to"], "days": mn["days"]},
           "champion_mae_bps": mc["mae_bps"], "challenger_mae_bps": mn["mae_bps"],
           "mae_change_vs_champion_pct": _pct(mn["mae_bps"], mc["mae_bps"]),
           "dm_statistic": round(stat, 2) if np.isfinite(stat) else None, "dm_p_value": round(p, 3),
           "challenger_breach_rate": mn["breach_rate"], "champion_breach_rate": mc["breach_rate"],
           **verdict}
    run.update(promotion={"config": cfg.model_dump(mode="json"), "passed": verdict["passed"]})
    return run.log("promote", {"config": cfg.model_dump(mode="json")}, out)

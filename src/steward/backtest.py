"""Walk-forward backtests inside a data window, and their metrics.

`visible_until` is the leakage guard: a backtest never trains on, or scores, a margin that
settled on or after it. Development backtests use visible_until = D (the start of the hidden
promotion window); `promote` uses W; replay scoring uses W + future_days.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .data import dataset
from .models import Candidate
from .settings import BPS, SETTINGS
from .space import WINDOW_DAYS, ModelConfig


def walk_forward(cfg: ModelConfig, start: pd.Timestamp, end: pd.Timestamp,
                 visible_until: pd.Timestamp, data: pd.DataFrame | None = None) -> pd.DataFrame:
    """Forecasts for origins in [start, end), refitting every `cfg.refit_days` days.

    Each refit at date c trains on rows whose margin settled before c (and within the config's
    training window); scored rows must have settled before `visible_until`.
    """
    data = dataset(cfg.halflife) if data is None else data
    end = min(end, visible_until)
    data = data[data["settle_date"] < visible_until]
    window = WINDOW_DAYS[cfg.train_window]
    cuts = pd.date_range(start, end, freq=f"{cfg.refit_days}D", inclusive="left")
    out = []
    for i, cut in enumerate(cuts):
        nxt = cuts[i + 1] if i + 1 < len(cuts) else end
        block = data[(data["origin"] >= cut) & (data["origin"] < nxt)]
        if block.empty:
            continue
        train = data[data["settle_date"] < cut]
        if window:
            train = train[train["origin"] >= cut - pd.Timedelta(days=window)]
        model = Candidate(cfg).fit(train)
        out.append(block[["corridor", "origin", "target", "margin_rate", "volume", "settle_date"]]
                   .join(model.predict(block)))
    if not out:
        raise ValueError("no rows to score in this window")
    return pd.concat(out).reset_index(drop=True)


def metrics(preds: pd.DataFrame) -> dict:
    """Margin-rate error (bps), the dollar metric, and the band's breach rate; overall and by corridor."""
    err = preds["margin_rate"] - preds["forecast"]
    below = preds["margin_rate"] < preds["band"]

    def block(e: pd.Series, b: pd.Series, v: pd.Series) -> dict:
        return {"mae_bps": round(float(np.mean(np.abs(e)) * BPS), 2),
                "rmse_bps": round(float(np.sqrt(np.mean(e**2)) * BPS), 2),
                "mae_usd": round(float(np.mean(np.abs(e * v)))),
                "breach_rate": round(float(b.mean()), 3)}

    out = {"days": int(preds["origin"].nunique()),
           "from": f"{preds['origin'].min():%Y-%m-%d}", "to": f"{preds['origin'].max():%Y-%m-%d}",
           **block(err, below, preds["volume"]), "by_corridor": {}}
    for c, g in preds.groupby("corridor"):
        out["by_corridor"][c] = block(err[g.index], below[g.index], g["volume"])
    return out


def daily_loss(preds: pd.DataFrame) -> pd.Series:
    """Absolute error per origin day, averaged over corridors (bps). Input for the DM test."""
    e = (preds["margin_rate"] - preds["forecast"]).abs() * BPS
    return e.groupby(preds["origin"]).mean()

"""Fit and apply one config: a point forecast and a 5% margin-at-risk band.

Point forecast = stage 1 EWMA + stage 2 correction (none for family 'ewma').
Band = point forecast's stage 1 + a LightGBM quantile model of the residual, shifted by a
conformal correction on the last `calibration_days` of training (as in Project 3). For family
'ewma' the band is the stage 1 forecast plus the empirical 5% quantile of recent residuals.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from fx_margin.models import DEFAULT_PARAMS, make_model

from .settings import SETTINGS
from .space import ModelConfig


class Candidate:
    def __init__(self, cfg: ModelConfig):
        self.cfg = cfg

    def fit(self, train: pd.DataFrame) -> "Candidate":
        cfg, q = self.cfg, SETTINGS.mar_quantile
        cut = train["settle_date"].max() - pd.Timedelta(days=SETTINGS.calibration_days)
        fit_part, cal = train[train["settle_date"] <= cut], train[train["settle_date"] > cut]
        if cfg.family == "ewma":
            self.model_ = None
            self.q_model_ = None
            self.band_offset_ = float(np.quantile(cal["resid"], q)) if len(cal) else float(np.quantile(train["resid"], q))
            return self
        cols = cfg.columns()
        self.model_ = make_model(cfg.family, cfg.full_params()).fit(train[cols], train["resid"])
        self.q_model_ = make_model("lightgbm", {"lightgbm": DEFAULT_PARAMS["lightgbm"]}, quantile=q).fit(
            fit_part[cols], fit_part["resid"])
        score = self.q_model_.predict(cal[cols]) - cal["resid"].to_numpy()  # > 0: realized fell below
        n = len(score)
        level = min(1.0, (1 - q) * (n + 1) / n)
        self.band_offset_ = -float(np.quantile(score, level))
        return self

    def predict(self, rows: pd.DataFrame) -> pd.DataFrame:
        s1 = rows["s1_ewma"].to_numpy()
        out = pd.DataFrame(index=rows.index)
        if self.model_ is None:
            out["forecast"] = s1
            out["band"] = s1 + self.band_offset_
        else:
            X = rows[self.cfg.columns()]
            out["forecast"] = s1 + self.model_.predict(X)
            out["band"] = s1 + self.q_model_.predict(X) + self.band_offset_
        return out

"""The config space: every model the agent may choose is a `ModelConfig`.

A config fixes the stage 2 model family, the feature groups it sees, how much history it trains
on, how often it is refit, the stage 1 EWMA half-life, and (optionally) tuned hyperparameters.
Anything outside this space is rejected, so the agent can't invent a model nobody can audit.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Literal

from fx_margin.models import DEFAULT_PARAMS
from pydantic import BaseModel, ConfigDict, field_validator, model_validator

Family = Literal["ewma", "ridge", "xgboost", "lightgbm"]
FeatureGroup = Literal["fx_returns", "volatility", "dollar_index", "markup", "calendar", "lagged_residuals"]
TrainWindow = Literal["all", "3y", "2y", "1y"]

FEATURE_GROUPS: dict[str, list[str]] = {
    "fx_returns": ["ret_1", "ret_2", "ret_5", "ret_10"],
    "volatility": ["vol_5", "vol_20", "vol_ratio"],
    "dollar_index": ["dxy_ret_1", "dxy_ret_5"],
    "markup": ["markup_now", "markup_gap"],
    "calendar": ["dow", "is_weekend", "is_month_end", "is_holiday"],
    "lagged_residuals": ["dev_lag_0", "dev_lag_1", "dev_lag_2", "dev_mean_7", "trend_slope"],
}
ALWAYS = ["corr_MX", "corr_IN", "corr_BR"]  # corridor indicators
ALL_GROUPS = tuple(FEATURE_GROUPS)
WINDOW_DAYS = {"all": None, "3y": 3 * 365, "2y": 2 * 365, "1y": 365}
HALFLIVES = (5, 10, 20)

# Hyperparameter ranges (the same as Project 3's Optuna search): name -> (low, high, type, log scale)
RANGES: dict[str, dict[str, tuple[float, float, type, bool]]] = {
    "ridge": {"alpha": (1e-3, 1e3, float, True)},
    "xgboost": {
        "n_estimators": (100, 800, int, False), "max_depth": (2, 6, int, False),
        "learning_rate": (0.01, 0.2, float, True), "subsample": (0.6, 1.0, float, False),
        "colsample_bytree": (0.6, 1.0, float, False), "min_child_weight": (1.0, 50.0, float, True),
        "reg_lambda": (0.1, 10.0, float, True),
    },
    "lightgbm": {
        "n_estimators": (100, 800, int, False), "num_leaves": (4, 48, int, False),
        "learning_rate": (0.01, 0.2, float, True), "min_child_samples": (20, 400, int, True),
        "subsample": (0.6, 1.0, float, False), "colsample_bytree": (0.6, 1.0, float, False),
        "reg_lambda": (0.1, 10.0, float, True),
    },
}


class ModelConfig(BaseModel):
    """One point in the config space."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    family: Family
    features: tuple[FeatureGroup, ...] = ()
    train_window: TrainWindow = "all"
    refit_days: Literal[7, 30] = 30
    halflife: Literal[5, 10, 20] = 10
    params: dict[str, float] = {}

    @field_validator("features")
    @classmethod
    def _sorted_unique(cls, v: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(g for g in ALL_GROUPS if g in set(v))

    @model_validator(mode="after")
    def _check(self) -> "ModelConfig":
        if self.family == "ewma":
            if self.features or self.params:
                raise ValueError("family 'ewma' is stage 1 only: it takes no features and no params")
            return self
        if not self.features:
            raise ValueError(f"family '{self.family}' needs at least one feature group")
        ranges = RANGES[self.family]
        for name, value in self.params.items():
            if name not in ranges:
                raise ValueError(f"unknown {self.family} parameter '{name}'; allowed: {sorted(ranges)}")
            lo, hi, typ, _ = ranges[name]
            if not lo <= value <= hi:
                raise ValueError(f"{name}={value} is outside the allowed range [{lo}, {hi}]")
            if typ is int and value != int(value):
                raise ValueError(f"{name} must be a whole number")
        return self

    # ---- helpers
    def columns(self) -> list[str]:
        return [c for g in self.features for c in FEATURE_GROUPS[g]] + ALWAYS

    def full_params(self) -> dict:
        """Hyperparameters for fx_margin.models.make_model: defaults overridden by `params`."""
        if self.family == "ewma":
            return {}
        p = dict(DEFAULT_PARAMS[self.family])
        for name, value in self.params.items():
            p[name] = int(value) if RANGES[self.family][name][2] is int else float(value)
        return {self.family: p}

    def key(self) -> str:
        """Short stable id, the same for equal configs."""
        blob = json.dumps(self.model_dump(mode="json"), sort_keys=True)
        return hashlib.sha1(blob.encode()).hexdigest()[:8]

    def label(self) -> str:
        if self.family == "ewma":
            core = "ewma"
        else:
            short = {"fx_returns": "fx", "volatility": "vol", "dollar_index": "dxy", "markup": "mk",
                     "calendar": "cal", "lagged_residuals": "lag"}
            tuned = " tuned" if self.params else ""
            core = f"{self.family}[{','.join(short[g] for g in self.features)}]{tuned}"
        return f"{core} {self.train_window} refit{self.refit_days} hl{self.halflife}"


def load_config(arg: str | Path) -> ModelConfig:
    """A config from a JSON file path or an inline JSON string."""
    text = str(arg)
    if not text.lstrip().startswith("{"):
        text = Path(arg).read_text()
    return ModelConfig.model_validate_json(text)


def save_config(cfg: ModelConfig, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cfg.model_dump(mode="json"), indent=2) + "\n")
    return path


def describe_space() -> dict:
    """The config space as plain data, for the agent's `space` command."""
    return {
        "family": ["ewma", "ridge", "xgboost", "lightgbm"],
        "features": {g: cols for g, cols in FEATURE_GROUPS.items()},
        "train_window": list(WINDOW_DAYS),
        "refit_days": [7, 30],
        "halflife": list(HALFLIVES),
        "params": {fam: {k: [lo, hi] for k, (lo, hi, _, _) in r.items()} for fam, r in RANGES.items()},
        "notes": "family 'ewma' = stage 1 only (no features, no params). Other families need >= 1 "
                 "feature group. Corridor indicators are always included. Set params only from "
                 "`tune` output or within the ranges shown.",
    }

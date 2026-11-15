"""All settings in one place: data windows, the weekly budget and the promotion rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    seed: int = 42

    # Data windows, relative to the weekly cutoff W (the last day of data).
    promotion_days: int = 56   # [W - 56 days, W): hidden from the agent, used only by `promote`
    dev_eval_days: int = 182   # development backtests score the 26 weeks before the promotion window
    future_days: int = 84      # replay only: decisions are scored on the 12 weeks after W

    # Weekly budget: calls the agent (or the automation baseline) may make per week.
    budget: tuple[tuple[str, int], ...] = (("backtest", 15), ("tune", 2), ("promote", 1))
    tune_max_trials: int = 30
    cv_splits: int = 3

    # Promotion rule: all three must hold on the promotion window.
    min_improvement: float = 0.01      # challenger MAE at least 1% lower than the champion's
    max_p_value: float = 0.10          # one-sided Diebold-Mariano test
    breach_bounds: tuple[float, float] = (0.02, 0.09)  # 5% margin-at-risk band breach rate

    # Margin at risk
    mar_quantile: float = 0.05
    calibration_days: int = 180

    fred_dir: Path = field(default=ROOT / "data" / "fred")
    cache_dir: Path = field(default=ROOT / "data" / "cache")
    runs_dir: Path = field(default=ROOT / "runs")
    reports_dir: Path = field(default=ROOT / "reports")
    champion_file: Path = field(default=ROOT / "champion.json")


SETTINGS = Settings()
BUDGET = dict(SETTINGS.budget)
BPS = 1e4

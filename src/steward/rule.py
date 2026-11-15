"""The promotion rule: a deterministic gate the agent can't argue with.

A challenger replaces the champion only if, on the hidden promotion window:
1. its MAE is at least `min_improvement` (1%) lower;
2. a one-sided Diebold-Mariano test says the improvement is unlikely to be luck (p < 0.10);
3. its 5% margin-at-risk band is breached on a sensible share of days (2-9%).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .settings import SETTINGS


def diebold_mariano(loss_champion: pd.Series, loss_challenger: pd.Series, h: int = 1) -> tuple[float, float]:
    """One-sided DM test that the challenger's loss is lower, with a Newey-West (HAC) variance
    and the Harvey-Leybourne-Newbold small-sample correction. Returns (statistic, p-value)."""
    d = (loss_champion - loss_challenger).dropna().to_numpy()  # > 0 when the challenger is better
    n = len(d)
    if n < 10:
        return float("nan"), 1.0
    lags = max(h - 1, int(np.floor(n ** (1 / 3))))
    dc = d - d.mean()
    var = dc @ dc / n
    for k in range(1, lags + 1):
        w = 1 - k / (lags + 1)
        var += 2 * w * (dc[k:] @ dc[:-k]) / n
    if var <= 0:
        return float("nan"), 1.0
    dm = d.mean() / np.sqrt(var / n)
    hln = np.sqrt((n + 1 - 2 * h + h * (h - 1) / n) / n)
    stat = float(dm * hln)
    return stat, float(1 - stats.t.cdf(stat, df=n - 1))


def evaluate(champion_mae: float, challenger_mae: float, dm_p: float, challenger_breach: float) -> dict:
    improvement = (champion_mae - challenger_mae) / champion_mae
    lo, hi = SETTINGS.breach_bounds
    checks = {
        "improvement": improvement >= SETTINGS.min_improvement,
        "significance": dm_p < SETTINGS.max_p_value,
        "band": lo <= challenger_breach <= hi,
    }
    reasons = []
    if not checks["improvement"]:
        reasons.append(f"MAE improvement {improvement:.1%} is below the required {SETTINGS.min_improvement:.0%}")
    if not checks["significance"]:
        reasons.append(f"Diebold-Mariano p-value {dm_p:.3f} is not below {SETTINGS.max_p_value}")
    if not checks["band"]:
        reasons.append(f"band breach rate {challenger_breach:.1%} is outside {lo:.0%}-{hi:.0%}")
    return {"passed": all(checks.values()), "checks": checks,
            "improvement_pct": round(improvement * 100, 2), "reasons": reasons}

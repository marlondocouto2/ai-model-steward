# Weekly model review: 2025-01-17

**Decision: Switch.** Champion: `lightgbm[mk,lag] tuned 1y refit7 hl5` (was `ewma all refit30 hl10`)

**What changed:** The champion degraded mainly in MX, where a high-volatility regime and a mid-year shock doubled errors, while BR worsened modestly and IN was stable. The feature-free EWMA trained on all history adapts slowly; a LightGBM on markup and lagged-residual features with a one-year window and weekly refits tracks the new regime better in every corridor.

## Evidence

- The champion's error over the last 26 weeks was 66.33 bps vs 46.41 bps before (+42.92%), driven by MX at 106.44 bps vs 56.52 bps. (L02)
- In development the tuned challenger scored 62.81 bps vs the champion's 66.33 bps (-5.31%), better in MX (103.27 bps vs 106.44 bps), IN (9.07 bps vs 13.13 bps) and BR (76.1 bps vs 79.42 bps). (L15)
- The gain is robust to halflife: the untuned one-year markup and lagged-residual model with halflife 10 also improved on the champion at -4.84%, while the 2y window version improved only -2.07% and was worse in BR. (L12, L08)
- On the hidden promotion window the challenger scored 64.53 bps vs the champion's 67.99 bps (-5.09%), with a Diebold-Mariano p-value of 0.01 and a breach rate of 0.068, passing all three checks. (L16)

**Risks:** The challenger still forecasts MX and BR too low on average, and the largest misses remain MX shock days that no candidate handles well. The shorter training window may overreact if the volatile regime fades, and tuned hyperparameters may carry some selection luck.

**Watch next week:** Watch MX error and bias under the new model, whether the BR markup rise persists, and whether the challenger's risk-band breach rate stays inside the allowed range.

## Ledger

Budget used: backtests 9, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-01-17 |
| L02 | champion-report | champion MAE last 4w 60.78, last 26w 66.33, prior 26w 46.41 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 69.46 bps (+4.72% vs champion) |
| L05 | backtest | ridge[vol,mk,cal,lag] 2y refit7 hl10: MAE 67.04 bps (+1.07% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 65.06 bps (-1.91% vs champion) |
| L07 | diagnose | diagnosis of lightgbm[vol,mk,cal,lag] 2y refit7 hl10 |
| L08 | backtest | lightgbm[mk,lag] 2y refit7 hl10: MAE 64.96 bps (-2.07% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 65.89 bps (-0.66% vs champion) |
| L10 | backtest | lightgbm[mk,lag] 1y refit7 hl5: MAE 63.49 bps (-4.28% vs champion) |
| L11 | backtest | lightgbm[vol,mk,cal,lag] 1y refit7 hl10: MAE 63.24 bps (-4.66% vs champion) |
| L12 | backtest | lightgbm[mk,lag] 1y refit7 hl10: MAE 63.12 bps (-4.84% vs champion) |
| L13 | diagnose | diagnosis of lightgbm[mk,lag] 1y refit7 hl5 |
| L14 | tune | lightgbm[mk,lag] tuned 1y refit7 hl5: CV MAE 60.3 → 58.71 bps |
| L15 | backtest | lightgbm[mk,lag] tuned 1y refit7 hl5: MAE 62.81 bps (-5.31% vs champion) |
| L16 | promote | lightgbm[mk,lag] tuned 1y refit7 hl5: 64.53 vs 67.99 bps, p = 0.01, passed |
| L17 | submit | accepted |

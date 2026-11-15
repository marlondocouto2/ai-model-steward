# Weekly model review: 2026-01-09

**Decision: Switch.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.67 bps vs 67.6 bps in the prior 26 weeks (-30.96%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5, scored 42.96 bps vs the champion's 46.67 bps (-7.95%). (L14)
- On the hidden window it scored 43.68 bps vs the champion's 46.71 bps (p = 0.029) and passed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-09 |
| L02 | champion-report | champion MAE last 4w 36.58, last 26w 46.67, prior 26w 67.6 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.67 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.4 bps (-4.86% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.7 bps (-6.36% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.04 bps (-5.64% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 43.67 bps (-6.43% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 45.19 bps (-3.17% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 45.88 bps (-1.69% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 43.12 bps (-7.61% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.2 bps (-7.44% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 43.13 bps (-7.59% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 54.97 → 53.74 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 42.96 bps (-7.95% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: 43.68 vs 46.71 bps, p = 0.029, passed |
| L16 | submit | accepted |

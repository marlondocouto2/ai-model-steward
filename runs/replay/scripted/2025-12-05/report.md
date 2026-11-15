# Weekly model review: 2025-12-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.73 bps vs 61.98 bps in the prior 26 weeks (-26.22%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl20, scored 44.83 bps vs the champion's 45.73 bps (-1.97%). (L12)
- On the hidden window it scored 35.49 bps vs the champion's 35.3 bps (p = 0.593) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-05 |
| L02 | champion-report | champion MAE last 4w 36.43, last 26w 45.73, prior 26w 61.98 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 48.76 bps (+6.63% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.72 bps (-0.02% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.11 bps (+0.83% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.56 bps (+1.82% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 44.95 bps (-1.71% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 46.93 bps (+2.62% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 48.41 bps (+5.86% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 44.95 bps (-1.71% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 44.94 bps (-1.73% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl20: MAE 44.83 bps (-1.97% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl20: CV MAE 57.96 → 55.04 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl20: MAE 45.11 bps (-1.36% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl20: 35.49 vs 35.3 bps, p = 0.593, failed |
| L16 | submit | accepted |

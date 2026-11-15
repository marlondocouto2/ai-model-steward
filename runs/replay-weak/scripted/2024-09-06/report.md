# Weekly model review: 2024-09-06

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.48 bps vs 57.27 bps in the prior 26 weeks (-3.13%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20, scored 49.23 bps vs the champion's 55.48 bps (-11.27%). (L11)
- On the hidden window it scored 77.03 bps vs the champion's 66.32 bps (p = 0.94) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-09-06 |
| L02 | champion-report | champion MAE last 4w 70.44, last 26w 55.48, prior 26w 57.27 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 55.48 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.46 bps (-9.05% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 49.67 bps (-10.47% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.11 bps (-9.68% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 49.94 bps (-9.99% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 49.61 bps (-10.58% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 49.72 bps (-10.38% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 49.57 bps (-10.65% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 49.23 bps (-11.27% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20: MAE 49.83 bps (-10.18% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: CV MAE 63.45 → 61.4 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: MAE 50.72 bps (-8.58% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: 77.03 vs 66.32 bps, p = 0.94, failed |
| L16 | submit | accepted |

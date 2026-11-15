# Weekly model review: 2024-07-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.09 bps vs 56.17 bps in the prior 26 weeks (-26.85%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20, scored 40.38 bps vs the champion's 41.09 bps (-1.73%). (L11)
- On the hidden window it scored 70.92 bps vs the champion's 68.82 bps (p = 0.83) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-07-12 |
| L02 | champion-report | champion MAE last 4w 50.23, last 26w 41.09, prior 26w 56.17 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 45.94 bps (+11.8% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.71 bps (+1.51% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 40.86 bps (-0.56% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.27 bps (+0.44% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.19 bps (+0.24% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 40.45 bps (-1.56% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 41.42 bps (+0.8% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 40.71 bps (-0.92% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 40.38 bps (-1.73% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20: MAE 40.42 bps (-1.63% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: CV MAE 63.98 → 62.48 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: MAE 41.53 bps (+1.07% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: 70.92 vs 68.82 bps, p = 0.83, failed |
| L16 | submit | accepted |

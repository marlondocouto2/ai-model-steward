# Weekly model review: 2024-07-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.59 bps vs 54.54 bps in the prior 26 weeks (-23.74%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20, scored 40.71 bps vs the champion's 41.59 bps (-2.12%). (L11)
- On the hidden window it scored 70.92 bps vs the champion's 70.95 bps (p = 0.494) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-07-19 |
| L02 | champion-report | champion MAE last 4w 45.0, last 26w 41.59, prior 26w 54.54 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.66 bps (+12.19% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.14 bps (+1.32% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.22 bps (-0.89% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.61 bps (+0.05% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.56 bps (-0.07% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 40.74 bps (-2.04% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 41.83 bps (+0.58% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 41.13 bps (-1.11% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 40.71 bps (-2.12% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20: MAE 40.79 bps (-1.92% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: CV MAE 63.94 → 62.38 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl20: MAE 42.05 bps (+1.11% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: 70.92 vs 70.95 bps, p = 0.494, failed |
| L16 | submit | accepted |

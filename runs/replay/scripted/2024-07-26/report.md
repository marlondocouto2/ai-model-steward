# Weekly model review: 2024-07-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.89 bps vs 52.5 bps in the prior 26 weeks (-20.21%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10, scored 41.29 bps vs the champion's 41.89 bps (-1.43%). (L08)
- On the hidden window it scored 69.05 bps vs the champion's 67.26 bps (p = 0.778) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-07-26 |
| L02 | champion-report | champion MAE last 4w 36.59, last 26w 41.89, prior 26w 52.5 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.72 bps (+11.53% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.48 bps (+1.41% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.69 bps (-0.48% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.34 bps (+1.07% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.47 bps (-1.0% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 41.29 bps (-1.43% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 41.94 bps (+0.12% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 41.52 bps (-0.88% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 41.48 bps (-0.98% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 41.29 bps (-1.43% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: CV MAE 62.81 → 61.52 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: MAE 41.56 bps (-0.79% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: 69.05 vs 67.26 bps, p = 0.778, failed |
| L16 | submit | accepted |

# Weekly model review: 2024-06-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.34 bps vs 54.64 bps in the prior 26 weeks (-24.34%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 41.0 bps vs the champion's 41.34 bps (-0.82%). (L10)
- On the hidden window it scored 61.64 bps vs the champion's 62.64 bps (p = 0.144) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-06-14 |
| L02 | champion-report | champion MAE last 4w 59.07, last 26w 41.34, prior 26w 54.64 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 44.78 bps (+8.32% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.53 bps (+0.46% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.13 bps (-0.51% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.58 bps (+0.58% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.82 bps (+1.16% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 41.89 bps (+1.33% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 42.63 bps (+3.12% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 41.0 bps (-0.82% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 41.08 bps (-0.63% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 41.06 bps (-0.68% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 63.96 → 62.95 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 41.06 bps (-0.68% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: 61.64 vs 62.64 bps, p = 0.144, failed |
| L16 | submit | accepted |

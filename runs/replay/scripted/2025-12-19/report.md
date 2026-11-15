# Weekly model review: 2025-12-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.09 bps vs 63.38 bps in the prior 26 weeks (-28.86%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5, scored 44.34 bps vs the champion's 45.09 bps (-1.66%). (L14)
- On the hidden window it scored 41.23 bps vs the champion's 40.68 bps (p = 0.805) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-19 |
| L02 | champion-report | champion MAE last 4w 38.05, last 26w 45.09, prior 26w 63.38 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 48.38 bps (+7.3% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.64 bps (+1.22% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.24 bps (+0.33% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.06 bps (+2.15% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 44.95 bps (-0.31% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 46.66 bps (+3.48% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 48.14 bps (+6.76% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 44.36 bps (-1.62% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 44.56 bps (-1.18% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 44.63 bps (-1.02% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 56.0 → 54.74 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 44.34 bps (-1.66% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: 41.23 vs 40.68 bps, p = 0.805, failed |
| L16 | submit | accepted |

# Weekly model review: 2026-04-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.59 bps vs 55.98 bps in the prior 26 weeks (-25.71%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5, scored 41.13 bps vs the champion's 41.59 bps (-1.11%). (L10)
- On the hidden window it scored 72.21 bps vs the champion's 71.31 bps (p = 0.805) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-04-24 |
| L02 | champion-report | champion MAE last 4w 36.2, last 26w 41.59, prior 26w 55.98 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 45.1 bps (+8.44% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.83 bps (+2.98% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.95 bps (+0.87% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.45 bps (+2.07% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.78 bps (+0.46% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 43.15 bps (+3.75% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 43.76 bps (+5.22% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 41.13 bps (-1.11% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 42.06 bps (+1.13% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 41.59 bps (+0.0% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 53.42 → 52.17 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 41.4 bps (-0.46% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: 72.21 vs 71.31 bps, p = 0.805, failed |
| L16 | submit | accepted |

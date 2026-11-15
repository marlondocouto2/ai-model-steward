# Weekly model review: 2026-03-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.71 bps vs 55.98 bps in the prior 26 weeks (-23.7%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5, scored 42.26 bps vs the champion's 42.71 bps (-1.05%). (L10)
- On the hidden window it scored 61.54 bps vs the champion's 61.58 bps (p = 0.466) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-03-27 |
| L02 | champion-report | champion MAE last 4w 49.27, last 26w 42.71, prior 26w 55.98 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.14 bps (+8.03% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.81 bps (+2.58% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.92 bps (+0.49% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.54 bps (+1.94% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 42.81 bps (+0.23% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 44.21 bps (+3.51% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 44.54 bps (+4.28% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 42.26 bps (-1.05% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.07 bps (+0.84% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 42.63 bps (-0.19% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 53.56 → 51.99 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 42.6 bps (-0.26% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: 61.54 vs 61.58 bps, p = 0.466, failed |
| L16 | submit | accepted |

# Weekly model review: 2026-01-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 43.5 bps vs 60.31 bps in the prior 26 weeks (-27.87%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5, scored 42.67 bps vs the champion's 43.5 bps (-1.91%). (L14)
- On the hidden window it scored 46.33 bps vs the champion's 45.24 bps (p = 0.962) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-23 |
| L02 | champion-report | champion MAE last 4w 37.25, last 26w 43.5, prior 26w 60.31 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.57 bps (+7.06% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.13 bps (+1.45% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.56 bps (+0.14% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.3 bps (+1.84% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 43.38 bps (-0.28% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 44.73 bps (+2.83% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 45.33 bps (+4.21% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 42.82 bps (-1.56% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.52 bps (+0.05% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 43.09 bps (-0.94% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 54.91 → 53.75 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 42.67 bps (-1.91% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: 46.33 vs 45.24 bps, p = 0.962, failed |
| L16 | submit | accepted |

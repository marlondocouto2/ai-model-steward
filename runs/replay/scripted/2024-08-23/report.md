# Weekly model review: 2024-08-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.15 bps vs 53.78 bps in the prior 26 weeks (-8.61%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20, scored 47.9 bps vs the champion's 49.15 bps (-2.54%). (L11)
- On the hidden window it scored 70.33 bps vs the champion's 66.15 bps (p = 0.981) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-08-23 |
| L02 | champion-report | champion MAE last 4w 81.85, last 26w 49.15, prior 26w 53.78 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.46 bps (+10.8% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 49.39 bps (+0.49% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 48.38 bps (-1.57% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 49.01 bps (-0.28% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 48.1 bps (-2.14% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 48.54 bps (-1.24% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 49.51 bps (+0.73% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 48.21 bps (-1.91% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 47.9 bps (-2.54% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl20: MAE 48.27 bps (-1.79% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl20: CV MAE 63.42 → 61.65 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl20: MAE 48.42 bps (-1.49% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: 70.33 vs 66.15 bps, p = 0.981, failed |
| L16 | submit | accepted |

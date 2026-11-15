# Weekly model review: 2025-11-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.71 bps vs 58.57 bps in the prior 26 weeks (-13.42%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 49.45 bps vs the champion's 50.71 bps (-2.48%). (L14)
- On the hidden window it scored 40.95 bps vs the champion's 38.86 bps (p = 0.999) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.77, last 26w 50.71, prior 26w 58.57 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 53.04 bps (+4.59% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.09 bps (+0.75% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 49.5 bps (-2.39% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 58.31 bps (+14.99% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 51.76 bps (+2.07% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 53.96 bps (+6.41% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.61 bps (+17.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.05 bps (+6.59% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.76 bps (+0.1% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.87 bps (+0.32% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 49.79 bps (-1.81% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 49.55 bps (-2.29% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 49.45 bps (-2.48% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 56.63 → 54.99 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 50.69 bps (-0.04% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 40.95 vs 38.86 bps, p = 0.999, failed |
| L18 | submit | accepted |

# Weekly model review: 2024-01-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.45 bps vs 62.55 bps in the prior 26 weeks (-9.75%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5, scored 54.94 bps vs the champion's 56.45 bps (-2.67%). (L13)
- On the hidden window it scored 38.46 bps vs the champion's 38.77 bps (p = 0.367) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 56.07, last 26w 56.45, prior 26w 62.55 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.9 bps (+2.57% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 55.01 bps (-2.55% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.53 bps (-1.63% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.91 bps (+9.67% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.71 bps (+2.23% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.16 bps (+6.57% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.51 bps (+12.51% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.88 bps (+9.62% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.13 bps (-0.57% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 56.04 bps (-0.73% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 55.2 bps (-2.21% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 54.94 bps (-2.67% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl5: MAE 56.64 bps (+0.34% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: CV MAE 69.43 → 68.41 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: MAE 55.77 bps (-1.2% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: 38.46 vs 38.77 bps, p = 0.367, failed |
| L18 | submit | accepted |

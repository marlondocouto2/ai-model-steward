# Weekly model review: 2025-09-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.95 bps vs 59.78 bps in the prior 26 weeks (-3.06%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 57.47 bps vs the champion's 57.95 bps (-0.83%). (L12)
- On the hidden window it scored 41.86 bps vs the champion's 42.73 bps (p = 0.021) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.62, last 26w 57.95, prior 26w 59.78 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 61.03 bps (+5.31% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 58.65 bps (+1.21% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.6 bps (-0.6% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.73 bps (+13.43% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 59.67 bps (+2.97% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.74 bps (+8.27% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 67.39 bps (+16.29% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.93 bps (+5.14% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 58.57 bps (+1.07% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 59.07 bps (+1.93% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.47 bps (-0.83% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 57.63 bps (-0.55% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 57.62 bps (-0.57% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 55.9 → 54.47 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 57.69 bps (-0.45% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 41.86 vs 42.73 bps, p = 0.021, failed |
| L18 | submit | accepted |

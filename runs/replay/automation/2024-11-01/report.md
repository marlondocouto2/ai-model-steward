# Weekly model review: 2024-11-01

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.56 bps vs 45.96 bps in the prior 26 weeks (+29.59%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 59.39 bps vs the champion's 59.56 bps (-0.29%). (L16)
- On the hidden window it scored 49.77 bps vs the champion's 50.53 bps (p = 0.148) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 55.45, last 26w 59.56, prior 26w 45.96 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.5 bps (+8.29% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.17 bps (+2.7% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 59.72 bps (+0.27% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 67.69 bps (+13.65% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.05 bps (+2.5% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.96 bps (+12.42% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.58 bps (+16.82% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 65.02 bps (+9.17% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.67 bps (+1.86% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 62.39 bps (+4.75% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.05 bps (+0.82% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 59.83 bps (+0.45% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 59.99 bps (+0.72% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 62.12 → 60.89 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 59.39 bps (-0.29% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 49.77 vs 50.53 bps, p = 0.148, failed |
| L18 | submit | accepted |

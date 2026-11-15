# Weekly model review: 2024-01-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.94 bps vs 63.0 bps in the prior 26 weeks (-12.79%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit7 hl5, scored 53.44 bps vs the champion's 54.94 bps (-2.73%). (L03)
- On the hidden window it scored 44.81 bps vs the champion's 43.09 bps (p = 0.951) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 47.62, last 26w 54.94, prior 26w 63.0 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.57 bps (+4.79% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.44 bps (-2.73% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 54.05 bps (-1.62% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 60.29 bps (+9.74% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.4 bps (+4.48% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 59.05 bps (+7.48% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 61.28 bps (+11.54% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.03 bps (+11.08% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.7 bps (-0.44% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.84 bps (-0.18% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 53.81 bps (-2.06% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 53.53 bps (-2.57% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit7 hl5: MAE 57.2 bps (+4.11% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 69.23 → 67.71 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 53.61 bps (-2.42% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: 44.81 vs 43.09 bps, p = 0.951, failed |
| L18 | submit | accepted |

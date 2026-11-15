# Weekly model review: 2024-09-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.88 bps vs 53.32 bps in the prior 26 weeks (-6.45%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit30 hl5, scored 49.09 bps vs the champion's 49.88 bps (-1.58%). (L12)
- On the hidden window it scored 72.37 bps vs the champion's 68.36 bps (p = 0.89) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.94, last 26w 49.88, prior 26w 53.32 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.69 bps (+9.64% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 49.1 bps (-1.56% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 49.52 bps (-0.72% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.4 bps (+15.08% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.7 bps (-0.36% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.82 bps (+11.91% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 58.58 bps (+17.44% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.51 bps (+9.28% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.31 bps (+0.86% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.67 bps (+1.58% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 49.09 bps (-1.58% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 52.35 bps (+4.95% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 49.63 bps (-0.5% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: CV MAE 61.89 → 60.6 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: MAE 49.95 bps (+0.14% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: 72.37 vs 68.36 bps, p = 0.89, failed |
| L18 | submit | accepted |

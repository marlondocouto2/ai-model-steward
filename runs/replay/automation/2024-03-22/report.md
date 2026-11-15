# Weekly model review: 2024-03-22

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.52 bps vs 54.27 bps in the prior 26 weeks (-1.38%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 52.21 bps vs the champion's 53.52 bps (-2.45%). (L14)
- On the hidden window it scored 27.99 bps vs the champion's 28.43 bps (p = 0.247) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 49.31, last 26w 53.52, prior 26w 54.27 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.0 bps (+8.37% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.36 bps (-0.3% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.77 bps (-1.4% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 60.62 bps (+13.27% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.72 bps (+2.24% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 59.55 bps (+11.27% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.09 bps (+12.28% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.91 bps (+13.81% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.4 bps (-0.22% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.74 bps (+2.28% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.19 bps (-0.62% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.56 bps (-1.79% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.21 bps (-2.45% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 66.96 → 66.39 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 53.84 bps (+0.6% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 27.99 vs 28.43 bps, p = 0.247, failed |
| L18 | submit | accepted |

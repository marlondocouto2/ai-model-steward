# Weekly model review: 2025-04-25

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.11 bps vs 59.1 bps in the prior 26 weeks (-6.75%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 54.17 bps vs the champion's 55.11 bps (-1.71%). (L16)
- On the hidden window it scored 78.8 bps vs the champion's 79.27 bps (p = 0.407) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.64, last 26w 55.11, prior 26w 59.1 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.54 bps (+8.04% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.34 bps (+4.05% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.66 bps (+1.0% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.51 bps (+11.61% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.68 bps (+6.48% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.55 bps (+9.87% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.7 bps (+10.14% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.13 bps (+9.11% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.24 bps (+2.05% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.7 bps (+4.7% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.34 bps (+0.42% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.68 bps (+1.03% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 55.83 bps (+1.31% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.99 → 55.79 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 54.17 bps (-1.71% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 78.8 vs 79.27 bps, p = 0.407, failed |
| L18 | submit | accepted |

# Weekly model review: 2024-06-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 39.77 bps vs 53.98 bps in the prior 26 weeks (-26.32%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 39.26 bps vs the champion's 39.77 bps (-1.28%). (L13)
- On the hidden window it scored 58.47 bps vs the champion's 59.07 bps (p = 0.102) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.02, last 26w 39.77, prior 26w 53.98 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.91 bps (+12.92% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 40.3 bps (+1.33% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 39.5 bps (-0.68% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 43.59 bps (+9.61% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 40.21 bps (+1.11% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.53 bps (+9.45% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 43.56 bps (+9.53% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.79 bps (+12.62% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 39.75 bps (-0.05% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.46 bps (+4.25% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 39.56 bps (-0.53% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 39.26 bps (-1.28% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 39.29 bps (-1.21% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.2 → 62.53 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 39.63 bps (-0.35% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 58.47 vs 59.07 bps, p = 0.102, failed |
| L18 | submit | accepted |

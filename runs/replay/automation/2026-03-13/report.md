# Weekly model review: 2026-03-13

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.76 bps vs 57.59 bps in the prior 26 weeks (-27.49%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 41.39 bps vs the champion's 41.76 bps (-0.89%). (L04)
- On the hidden window it scored 59.57 bps vs the champion's 59.65 bps (p = 0.444) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.73, last 26w 41.76, prior 26w 57.59 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 43.75 bps (+4.77% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.95 bps (+0.45% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.39 bps (-0.89% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.52 bps (+13.79% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.3 bps (+1.29% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.49 bps (+6.54% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.26 bps (+15.57% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.62 bps (+6.85% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.17 bps (+0.98% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.78 bps (+0.05% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.74 bps (-0.05% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.44 bps (-0.77% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.83 bps (+0.17% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 53.13 → 51.95 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 41.61 bps (-0.36% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 59.57 vs 59.65 bps, p = 0.444, failed |
| L18 | submit | accepted |

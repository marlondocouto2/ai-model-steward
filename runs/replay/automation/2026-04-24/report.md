# Weekly model review: 2026-04-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.59 bps vs 55.98 bps in the prior 26 weeks (-25.71%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5, scored 41.36 bps vs the champion's 41.59 bps (-0.55%). (L16)
- On the hidden window it scored 72.57 bps vs the champion's 71.31 bps (p = 0.931) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 36.2, last 26w 41.59, prior 26w 55.98 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.63 bps (+9.71% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.71 bps (+0.29% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.86 bps (+0.65% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.18 bps (+13.44% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.62 bps (+2.48% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.36 bps (+6.66% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 47.39 bps (+13.95% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.63 bps (+7.31% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.61 bps (+0.05% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.52 bps (+2.24% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 42.16 bps (+1.37% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 41.43 bps (-0.38% vs champion) |
| L14 | backtest | lightgbm[fx,vol,dxy,mk] all refit30 hl20: MAE 42.66 bps (+2.57% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: CV MAE 53.8 → 52.13 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: MAE 41.36 bps (-0.55% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: 72.57 vs 71.31 bps, p = 0.931, failed |
| L18 | submit | accepted |

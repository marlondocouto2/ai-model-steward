# Weekly model review: 2024-05-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.98 bps vs 51.91 bps in the prior 26 weeks (-19.13%). (L01)
- The best development candidate, lightgbm[fx,dxy,mk] all refit7 hl20, scored 41.4 bps vs the champion's 41.98 bps (-1.38%). (L10)
- On the hidden window it scored 55.8 bps vs the champion's 53.69 bps (p = 0.972) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 29.17, last 26w 41.98, prior 26w 51.91 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 47.14 bps (+12.29% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.42 bps (+1.05% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.69 bps (-0.69% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 45.99 bps (+9.55% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.94 bps (+2.29% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 47.09 bps (+12.17% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 45.47 bps (+8.31% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 47.3 bps (+12.67% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.4 bps (-1.38% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.76 bps (+4.24% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 41.98 bps (+0.0% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.45 bps (-1.26% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk,cal,lag] 2y refit7 hl20: MAE 42.57 bps (+1.41% vs champion) |
| L15 | tune | lightgbm[fx,dxy,mk] tuned all refit7 hl20: CV MAE 63.27 → 62.31 bps |
| L16 | backtest | lightgbm[fx,dxy,mk] tuned all refit7 hl20: MAE 41.57 bps (-0.98% vs champion) |
| L17 | promote | lightgbm[fx,dxy,mk] all refit7 hl20: 55.8 vs 53.69 bps, p = 0.972, failed |
| L18 | submit | accepted |

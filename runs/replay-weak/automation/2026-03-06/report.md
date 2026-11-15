# Weekly model review: 2026-03-06

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] all refit7 hl20` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.9 bps vs 63.01 bps in the prior 26 weeks (-28.74%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 40.92 bps vs the champion's 44.9 bps (-8.86%). (L04)
- On the hidden window it scored 51.51 bps vs the champion's 59.39 bps (p = 0.0) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 49.79, last 26w 44.9, prior 26w 63.01 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 43.64 bps (-2.81% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.34 bps (-7.93% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 40.92 bps (-8.86% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.53 bps (+5.86% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.85 bps (-6.79% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.88 bps (-2.27% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.4 bps (+7.8% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.04 bps (+0.31% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.61 bps (-7.33% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.45 bps (-7.68% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.21 bps (-8.22% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.95 bps (-8.8% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.3 bps (-8.02% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 53.2 → 52.1 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 41.05 bps (-8.57% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 51.51 vs 59.39 bps, p = 0.0, passed |
| L18 | submit | accepted |

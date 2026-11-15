# Weekly model review: 2026-01-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 43.5 bps vs 60.31 bps in the prior 26 weeks (-27.87%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.88 bps vs the champion's 43.5 bps (-1.43%). (L04)
- On the hidden window it scored 45.6 bps vs the champion's 45.24 bps (p = 0.912) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 37.25, last 26w 43.5, prior 26w 60.31 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.31 bps (+4.16% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 43.13 bps (-0.85% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.88 bps (-1.43% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.33 bps (+13.4% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 44.23 bps (+1.68% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.93 bps (+0.99% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.62 bps (+16.37% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.33 bps (+6.51% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.92 bps (+0.97% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 44.1 bps (+1.38% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 43.18 bps (-0.74% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 43.01 bps (-1.13% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 44.39 bps (+2.05% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.55 → 53.48 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 43.29 bps (-0.48% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 45.6 vs 45.24 bps, p = 0.912, failed |
| L18 | submit | accepted |

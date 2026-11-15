# Weekly model review: 2024-03-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.44 bps vs 54.13 bps in the prior 26 weeks (-1.27%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 52.27 bps vs the champion's 53.44 bps (-2.19%). (L14)
- On the hidden window it scored 28.37 bps vs the champion's 29.01 bps (p = 0.21) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.99, last 26w 53.44, prior 26w 54.13 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.89 bps (+8.33% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.45 bps (+0.02% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.81 bps (-1.18% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 60.59 bps (+13.38% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.97 bps (+2.86% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 59.41 bps (+11.17% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.92 bps (+12.13% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.89 bps (+13.94% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.42 bps (-0.04% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.77 bps (+2.49% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.15 bps (-0.54% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.64 bps (-1.5% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.27 bps (-2.19% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 66.57 → 66.06 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 53.59 bps (+0.28% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 28.37 vs 29.01 bps, p = 0.21, failed |
| L18 | submit | accepted |

# Weekly model review: 2026-01-09

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] all refit7 hl20` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.67 bps vs 67.6 bps in the prior 26 weeks (-30.96%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.94 bps vs the champion's 46.67 bps (-7.99%). (L04)
- On the hidden window it scored 43.51 bps vs the champion's 46.71 bps (p = 0.016) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 36.58, last 26w 46.67, prior 26w 67.6 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.16 bps (-1.09% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 43.15 bps (-7.54% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.94 bps (-7.99% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.24 bps (+5.51% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 44.33 bps (-5.01% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.99 bps (-3.6% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.16 bps (+7.48% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.46 bps (-0.45% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.61 bps (-6.56% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.7 bps (-6.36% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 43.25 bps (-7.33% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 43.02 bps (-7.82% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 45.42 bps (-2.68% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.62 → 53.48 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 43.43 bps (-6.94% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 43.51 vs 46.71 bps, p = 0.016, passed |
| L18 | submit | accepted |

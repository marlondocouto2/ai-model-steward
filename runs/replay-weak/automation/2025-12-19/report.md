# Weekly model review: 2025-12-19

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] all refit7 hl20` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 48.38 bps vs 68.63 bps in the prior 26 weeks (-29.51%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 44.31 bps vs the champion's 48.38 bps (-8.41%). (L04)
- On the hidden window it scored 41.0 bps vs the champion's 42.67 bps (p = 0.023) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.42, last 26w 48.38, prior 26w 68.63 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.28 bps (-0.21% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.69 bps (-7.63% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.31 bps (-8.41% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.1 bps (+5.62% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.89 bps (-5.15% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 47.77 bps (-1.26% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.36 bps (+8.23% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.44 bps (+0.12% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.07 bps (-6.84% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.51 bps (-5.93% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.8 bps (-7.4% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 44.42 bps (-8.19% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 47.63 bps (-1.55% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.02 → 54.79 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 45.01 bps (-6.97% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 41.0 vs 42.67 bps, p = 0.023, passed |
| L18 | submit | accepted |

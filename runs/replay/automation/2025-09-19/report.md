# Weekly model review: 2025-09-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.5 bps vs 59.68 bps in the prior 26 weeks (-5.33%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 56.18 bps vs the champion's 56.5 bps (-0.57%). (L12)
- On the hidden window it scored 46.3 bps vs the champion's 47.07 bps (p = 0.038) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 42.26, last 26w 56.5, prior 26w 59.68 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.94 bps (+6.09% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.5 bps (+1.77% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 56.41 bps (-0.16% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 64.49 bps (+14.14% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.01 bps (+2.67% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.37 bps (+8.62% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 66.09 bps (+16.97% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.47 bps (+5.26% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.27 bps (+1.36% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.7 bps (+2.12% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 56.18 bps (-0.57% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 56.4 bps (-0.18% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 57.2 bps (+1.24% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.01 → 54.49 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 56.59 bps (+0.16% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 46.3 vs 47.07 bps, p = 0.038, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-07-25

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 65.47 bps vs 66.5 bps in the prior 26 weeks (-1.55%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 60.49 bps vs the champion's 65.47 bps (-7.61%). (L16)
- On the hidden window it scored 47.14 bps vs the champion's 49.17 bps (p = 0.234) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.95, last 26w 65.47, prior 26w 66.5 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.07 bps (-2.14% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.03 bps (-5.25% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.57 bps (-7.48% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.94 bps (+5.3% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.05 bps (-3.7% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.26 bps (+2.73% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 68.55 bps (+4.7% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.39 bps (-1.65% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.02 bps (-6.8% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.34 bps (-6.31% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.52 bps (-7.56% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.7 bps (-7.29% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 60.98 bps (-6.86% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.77 → 55.28 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 60.49 bps (-7.61% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 47.14 vs 49.17 bps, p = 0.234, failed |
| L18 | submit | accepted |

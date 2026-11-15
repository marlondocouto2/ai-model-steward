# Weekly model review: 2026-01-16

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.22 bps vs 63.01 bps in the prior 26 weeks (-32.99%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 41.63 bps vs the champion's 42.22 bps (-1.4%). (L04)
- On the hidden window it scored 42.89 bps vs the champion's 42.52 bps (p = 0.935) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 33.1, last 26w 42.22, prior 26w 63.01 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.34 bps (+5.02% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.98 bps (-0.57% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.63 bps (-1.4% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.6 bps (+15.11% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.91 bps (+1.63% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.61 bps (+3.29% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 49.54 bps (+17.34% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.43 bps (+7.6% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.48 bps (+0.62% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.9 bps (+1.61% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.94 bps (-0.66% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.77 bps (-1.07% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 42.07 bps (-0.36% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.54 → 53.41 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.09 bps (-0.31% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 42.89 vs 42.52 bps, p = 0.935, failed |
| L18 | submit | accepted |

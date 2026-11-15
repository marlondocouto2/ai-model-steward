# Weekly model review: 2024-10-18

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.71 bps vs 48.4 bps in the prior 26 weeks (+19.24%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 57.44 bps vs the champion's 57.71 bps (-0.47%). (L04)
- On the hidden window it scored 58.13 bps vs the champion's 56.98 bps (p = 0.854) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 77.24, last 26w 57.71, prior 26w 48.4 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 63.28 bps (+9.65% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.79 bps (+0.14% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.44 bps (-0.47% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.4 bps (+13.33% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.47 bps (+1.32% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 64.62 bps (+11.97% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 66.97 bps (+16.05% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 63.05 bps (+9.25% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 58.04 bps (+0.57% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 59.9 bps (+3.79% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.8 bps (+0.16% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 57.69 bps (-0.03% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 61.07 bps (+5.82% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.7 → 60.67 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 57.65 bps (-0.1% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 58.13 vs 56.98 bps, p = 0.854, failed |
| L18 | submit | accepted |

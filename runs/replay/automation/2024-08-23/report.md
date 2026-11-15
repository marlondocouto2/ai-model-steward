# Weekly model review: 2024-08-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.15 bps vs 53.78 bps in the prior 26 weeks (-8.61%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit30 hl5, scored 48.05 bps vs the champion's 49.15 bps (-2.24%). (L12)
- On the hidden window it scored 69.86 bps vs the champion's 66.15 bps (p = 0.921) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 81.85, last 26w 49.15, prior 26w 53.78 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 53.92 bps (+9.7% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.17 bps (-1.99% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 48.54 bps (-1.24% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.98 bps (+13.9% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.17 bps (+0.04% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.48 bps (+12.88% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.51 bps (+14.97% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.11 bps (+12.13% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 49.54 bps (+0.79% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.81 bps (+3.38% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 48.05 bps (-2.24% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 52.6 bps (+7.02% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 48.54 bps (-1.24% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: CV MAE 63.32 → 61.56 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: MAE 48.54 bps (-1.24% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: 69.86 vs 66.15 bps, p = 0.921, failed |
| L18 | submit | accepted |

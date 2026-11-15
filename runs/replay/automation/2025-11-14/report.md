# Weekly model review: 2025-11-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.22 bps vs 56.0 bps in the prior 26 weeks (-3.18%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 52.9 bps vs the champion's 54.22 bps (-2.43%). (L04)
- On the hidden window it scored 38.5 bps vs the champion's 37.95 bps (p = 0.786) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.97, last 26w 54.22, prior 26w 56.0 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.06 bps (+5.24% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.53 bps (+0.57% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.9 bps (-2.43% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.64 bps (+13.68% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.21 bps (-0.02% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.89 bps (+6.77% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.16 bps (+16.49% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.43 bps (+5.92% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.28 bps (+0.11% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.2 bps (-0.04% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.18 bps (-1.92% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.0 bps (-2.25% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.95 bps (-2.34% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.45 → 55.05 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 54.07 bps (-0.28% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 38.5 vs 37.95 bps, p = 0.786, failed |
| L18 | submit | accepted |

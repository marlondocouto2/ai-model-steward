# Weekly model review: 2025-12-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.65 bps vs 63.71 bps in the prior 26 weeks (-29.92%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 43.97 bps vs the champion's 44.65 bps (-1.52%). (L04)
- On the hidden window it scored 41.06 bps vs the champion's 40.65 bps (p = 0.91) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.24, last 26w 44.65, prior 26w 63.71 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 47.41 bps (+6.18% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.52 bps (-0.29% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 43.97 bps (-1.52% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 50.63 bps (+13.39% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 46.4 bps (+3.92% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.91 bps (+5.06% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 51.99 bps (+16.44% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.22 bps (+8.0% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 44.71 bps (+0.13% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.31 bps (+1.48% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.37 bps (-0.63% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 44.12 bps (-1.19% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 44.51 bps (-0.31% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.73 → 54.13 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 44.62 bps (-0.07% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 41.06 vs 40.65 bps, p = 0.91, failed |
| L18 | submit | accepted |

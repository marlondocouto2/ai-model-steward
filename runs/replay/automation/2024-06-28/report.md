# Weekly model review: 2024-06-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 40.4 bps vs 56.84 bps in the prior 26 weeks (-28.92%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 39.8 bps vs the champion's 40.4 bps (-1.49%). (L13)
- On the hidden window it scored 64.51 bps vs the champion's 64.29 bps (p = 0.595) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 66.88, last 26w 40.4, prior 26w 56.84 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.3 bps (+12.13% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 40.69 bps (+0.72% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 39.88 bps (-1.29% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 46.81 bps (+15.87% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.14 bps (+1.83% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.45 bps (+12.5% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 46.91 bps (+16.11% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.67 bps (+13.04% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 40.75 bps (+0.87% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.36 bps (+2.38% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 39.84 bps (-1.39% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 39.8 bps (-1.49% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 41.01 bps (+1.51% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 63.88 → 62.53 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 40.65 bps (+0.62% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 64.51 vs 64.29 bps, p = 0.595, failed |
| L18 | submit | accepted |

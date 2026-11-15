# Weekly model review: 2024-06-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.34 bps vs 54.64 bps in the prior 26 weeks (-24.34%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 40.8 bps vs the champion's 41.34 bps (-1.31%). (L13)
- On the hidden window it scored 63.05 bps vs the champion's 62.64 bps (p = 0.701) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 59.07, last 26w 41.34, prior 26w 54.64 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.09 bps (+11.49% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.12 bps (+1.89% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 40.98 bps (-0.87% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 45.92 bps (+11.08% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.51 bps (+0.41% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.07 bps (+11.44% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 46.61 bps (+12.75% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.23 bps (+11.83% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.47 bps (+0.31% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.83 bps (+3.6% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 40.96 bps (-0.92% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.8 bps (-1.31% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 42.09 bps (+1.81% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.54 → 63.17 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 41.53 bps (+0.46% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 63.05 vs 62.64 bps, p = 0.701, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-01-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.43 bps vs 46.12 bps in the prior 26 weeks (+28.86%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 58.82 bps vs the champion's 59.43 bps (-1.03%). (L16)
- On the hidden window it scored 62.22 bps vs the champion's 62.93 bps (p = 0.147) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 62.1, last 26w 59.43, prior 26w 46.12 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.68 bps (+8.83% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.75 bps (+5.59% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.18 bps (+1.26% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.59 bps (+12.05% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.59 bps (+5.32% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 65.06 bps (+9.47% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 67.28 bps (+13.21% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 65.31 bps (+9.89% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.31 bps (+1.48% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.13 bps (+6.23% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.24 bps (+1.36% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 59.96 bps (+0.89% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 59.48 bps (+0.08% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 61.16 → 58.23 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 58.82 bps (-1.03% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 62.22 vs 62.93 bps, p = 0.147, failed |
| L18 | submit | accepted |

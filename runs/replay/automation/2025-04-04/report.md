# Weekly model review: 2025-04-04

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.49 bps vs 54.96 bps in the prior 26 weeks (+4.6%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 56.54 bps vs the champion's 57.49 bps (-1.65%). (L16)
- On the hidden window it scored 54.27 bps vs the champion's 53.99 bps (p = 0.723) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 62.71, last 26w 57.49, prior 26w 54.96 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.18 bps (+8.16% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 60.38 bps (+5.03% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 58.0 bps (+0.89% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.58 bps (+10.59% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.86 bps (+7.6% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.12 bps (+8.05% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 62.86 bps (+9.34% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.91 bps (+9.43% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 58.93 bps (+2.5% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.01 bps (+4.38% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.86 bps (+0.64% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 58.01 bps (+0.9% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 58.17 bps (+1.18% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 57.83 → 56.38 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 56.54 bps (-1.65% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 54.27 vs 53.99 bps, p = 0.723, failed |
| L18 | submit | accepted |

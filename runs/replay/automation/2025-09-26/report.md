# Weekly model review: 2025-09-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.68 bps vs 59.6 bps in the prior 26 weeks (-6.58%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 55.14 bps vs the champion's 55.68 bps (-0.97%). (L14)
- On the hidden window it scored 45.46 bps vs the champion's 45.83 bps (p = 0.211) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.77, last 26w 55.68, prior 26w 59.6 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.6 bps (+7.04% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 56.91 bps (+2.21% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.26 bps (-0.75% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.85 bps (+14.67% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.1 bps (+2.55% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.08 bps (+9.7% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.83 bps (+18.23% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.69 bps (+7.2% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.38 bps (+1.26% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.14 bps (+2.62% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.18 bps (-0.9% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.29 bps (-0.7% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 55.14 bps (-0.97% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 56.15 → 54.43 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 55.7 bps (+0.04% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 45.46 vs 45.83 bps, p = 0.211, failed |
| L18 | submit | accepted |

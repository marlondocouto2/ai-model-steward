# Weekly model review: 2025-05-16

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.63 bps vs 62.14 bps in the prior 26 weeks (-10.48%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 54.77 bps vs the champion's 55.63 bps (-1.55%). (L16)
- On the hidden window it scored 72.03 bps vs the champion's 73.09 bps (p = 0.258) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 58.78, last 26w 55.63, prior 26w 62.14 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.78 bps (+7.46% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 58.08 bps (+4.4% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.91 bps (+0.5% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.72 bps (+10.95% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.91 bps (+5.9% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.06 bps (+9.76% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.72 bps (+9.15% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.22 bps (+8.25% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.46 bps (+1.49% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 58.86 bps (+5.81% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.75 bps (+0.22% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.83 bps (+0.36% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 55.95 bps (+0.58% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 57.08 → 55.41 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 54.77 bps (-1.55% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 72.03 vs 73.09 bps, p = 0.258, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-08-01

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.85 bps vs 59.22 bps in the prior 26 weeks (+2.75%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 60.38 bps vs the champion's 60.85 bps (-0.77%). (L16)
- On the hidden window it scored 46.48 bps vs the champion's 46.51 bps (p = 0.438) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.66, last 26w 60.85, prior 26w 59.22 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.02 bps (+5.21% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.31 bps (+2.4% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.63 bps (-0.36% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 69.14 bps (+13.62% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.51 bps (+2.73% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.46 bps (+10.86% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.16 bps (+13.66% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.07 bps (+5.29% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.19 bps (+0.56% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.74 bps (+1.46% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.61 bps (-0.39% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.78 bps (-0.12% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 60.93 bps (+0.13% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.9 → 55.5 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 60.38 bps (-0.77% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 46.48 vs 46.51 bps, p = 0.438, failed |
| L18 | submit | accepted |

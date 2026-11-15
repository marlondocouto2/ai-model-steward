# Weekly model review: 2025-05-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.62 bps vs 62.92 bps in the prior 26 weeks (-11.6%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 55.02 bps vs the champion's 55.62 bps (-1.08%). (L16)
- On the hidden window it scored 71.56 bps vs the champion's 72.51 bps (p = 0.244) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 57.77, last 26w 55.62, prior 26w 62.92 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.85 bps (+7.61% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.98 bps (+4.24% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.9 bps (+0.5% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.87 bps (+11.24% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.71 bps (+5.56% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.28 bps (+10.18% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.88 bps (+9.46% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.82 bps (+7.55% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.45 bps (+1.49% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 58.94 bps (+5.97% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.84 bps (+0.4% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.85 bps (+0.41% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 56.05 bps (+0.77% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.75 → 55.27 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 55.02 bps (-1.08% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 71.56 vs 72.51 bps, p = 0.244, failed |
| L18 | submit | accepted |

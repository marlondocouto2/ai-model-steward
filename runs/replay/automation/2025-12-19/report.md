# Weekly model review: 2025-12-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.09 bps vs 63.38 bps in the prior 26 weeks (-28.86%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 44.31 bps vs the champion's 45.09 bps (-1.73%). (L04)
- On the hidden window it scored 41.0 bps vs the champion's 40.68 bps (p = 0.852) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 38.05, last 26w 45.09, prior 26w 63.38 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.28 bps (+7.07% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.69 bps (-0.89% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.31 bps (-1.73% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.1 bps (+13.33% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.89 bps (+1.77% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 47.77 bps (+5.94% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.36 bps (+16.12% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.44 bps (+7.43% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.07 bps (-0.04% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.51 bps (+0.93% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.8 bps (-0.64% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 44.42 bps (-1.49% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 47.63 bps (+5.63% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.02 → 54.79 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 45.01 bps (-0.18% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 41.0 vs 40.68 bps, p = 0.852, failed |
| L18 | submit | accepted |

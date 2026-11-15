# Weekly model review: 2025-01-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.3 bps vs 43.55 bps in the prior 26 weeks (+40.76%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 60.76 bps vs the champion's 61.3 bps (-0.88%). (L16)
- On the hidden window it scored 60.13 bps vs the champion's 60.06 bps (p = 0.542) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 62.01, last 26w 61.3, prior 26w 43.55 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 66.78 bps (+8.94% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 65.03 bps (+6.08% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.25 bps (+1.55% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.62 bps (+11.94% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.87 bps (+5.82% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.42 bps (+9.98% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.44 bps (+13.28% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 67.14 bps (+9.53% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 62.56 bps (+2.06% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.88 bps (+7.47% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.46 bps (+1.89% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.09 bps (+1.29% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 61.75 bps (+0.73% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 61.49 → 57.97 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 60.76 bps (-0.88% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 60.13 vs 60.06 bps, p = 0.542, failed |
| L18 | submit | accepted |

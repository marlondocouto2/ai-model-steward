# Weekly model review: 2024-09-13

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.56 bps vs 53.5 bps in the prior 26 weeks (-7.36%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit7 hl5, scored 48.67 bps vs the champion's 49.56 bps (-1.8%). (L03)
- On the hidden window it scored 73.01 bps vs the champion's 65.9 bps (p = 0.98) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 57.26, last 26w 49.56, prior 26w 53.5 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.09 bps (+9.14% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.67 bps (-1.8% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 49.17 bps (-0.79% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.06 bps (+15.13% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.27 bps (-0.59% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.38 bps (+11.74% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 58.11 bps (+17.25% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.31 bps (+9.58% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 49.78 bps (+0.44% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.25 bps (+1.39% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 48.79 bps (-1.55% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 49.15 bps (-0.83% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit7 hl5: MAE 51.78 bps (+4.48% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 63.3 → 61.95 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 49.45 bps (-0.22% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: 73.01 vs 65.9 bps, p = 0.98, failed |
| L18 | submit | accepted |

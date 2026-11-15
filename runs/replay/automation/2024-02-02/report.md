# Weekly model review: 2024-02-02

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.28 bps vs 60.62 bps in the prior 26 weeks (-12.11%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 52.5 bps vs the champion's 53.28 bps (-1.46%). (L04)
- On the hidden window it scored 41.92 bps vs the champion's 42.22 bps (p = 0.449) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 37.38, last 26w 53.28, prior 26w 60.62 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.61 bps (+6.25% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 52.74 bps (-1.01% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.5 bps (-1.46% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 59.41 bps (+11.51% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.54 bps (+2.36% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.87 bps (+8.61% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.0 bps (+12.61% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.58 bps (+11.82% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.51 bps (+0.43% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.92 bps (+1.2% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 52.9 bps (-0.71% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 52.85 bps (-0.81% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 52.62 bps (-1.24% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 68.23 → 66.8 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 53.49 bps (+0.39% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 41.92 vs 42.22 bps, p = 0.449, failed |
| L18 | submit | accepted |

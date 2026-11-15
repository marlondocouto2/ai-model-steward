# Weekly model review: 2024-08-02

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.58 bps vs 53.4 bps in the prior 26 weeks (-16.52%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 43.89 bps vs the champion's 44.58 bps (-1.55%). (L04)
- On the hidden window it scored 58.04 bps vs the champion's 57.62 bps (p = 0.655) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 59.26, last 26w 44.58, prior 26w 53.4 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 49.01 bps (+9.94% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.19 bps (-0.87% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 43.89 bps (-1.55% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.06 bps (+14.54% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 44.69 bps (+0.25% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 49.87 bps (+11.87% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 51.64 bps (+15.84% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 49.85 bps (+11.82% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 44.67 bps (+0.2% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.61 bps (+2.31% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 43.99 bps (-1.32% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 43.9 bps (-1.53% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 43.95 bps (-1.41% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 62.94 → 61.6 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 44.48 bps (-0.22% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 58.04 vs 57.62 bps, p = 0.655, failed |
| L18 | submit | accepted |

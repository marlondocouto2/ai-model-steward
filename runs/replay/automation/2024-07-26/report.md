# Weekly model review: 2024-07-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.89 bps vs 52.5 bps in the prior 26 weeks (-20.21%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 41.34 bps vs the champion's 41.89 bps (-1.31%). (L13)
- On the hidden window it scored 68.37 bps vs the champion's 67.26 bps (p = 0.862) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 36.59, last 26w 41.89, prior 26w 52.5 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.06 bps (+9.95% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.91 bps (+0.05% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.39 bps (-1.19% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.08 bps (+14.78% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.98 bps (+0.21% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.72 bps (+11.53% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.88 bps (+16.69% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 47.26 bps (+12.82% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.41 bps (+1.24% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.95 bps (+2.53% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.47 bps (-1.0% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.34 bps (-1.31% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.4 bps (-1.17% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 62.52 → 61.57 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 42.13 bps (+0.57% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 68.37 vs 67.26 bps, p = 0.862, failed |
| L18 | submit | accepted |

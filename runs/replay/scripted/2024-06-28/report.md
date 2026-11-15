# Weekly model review: 2024-06-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 40.4 bps vs 56.84 bps in the prior 26 weeks (-28.92%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10, scored 39.95 bps vs the champion's 40.4 bps (-1.11%). (L08)
- On the hidden window it scored 64.31 bps vs the champion's 64.29 bps (p = 0.503) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-06-28 |
| L02 | champion-report | champion MAE last 4w 66.88, last 26w 40.4, prior 26w 56.84 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 45.12 bps (+11.68% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.05 bps (+1.61% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 40.07 bps (-0.82% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 40.42 bps (+0.05% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 40.57 bps (+0.42% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 39.95 bps (-1.11% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 40.88 bps (+1.19% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 40.25 bps (-0.37% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 40.0 bps (-0.99% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 39.96 bps (-1.09% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: CV MAE 64.04 → 62.22 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: MAE 40.3 bps (-0.25% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: 64.31 vs 64.29 bps, p = 0.503, failed |
| L16 | submit | accepted |

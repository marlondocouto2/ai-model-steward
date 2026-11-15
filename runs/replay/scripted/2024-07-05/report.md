# Weekly model review: 2024-07-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.53 bps vs 56.0 bps in the prior 26 weeks (-25.84%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20, scored 41.05 bps vs the champion's 41.53 bps (-1.16%). (L12)
- On the hidden window it scored 65.83 bps vs the champion's 64.52 bps (p = 0.697) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-07-05 |
| L02 | champion-report | champion MAE last 4w 59.77, last 26w 41.53, prior 26w 56.0 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.19 bps (+11.22% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.24 bps (+1.71% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.35 bps (-0.43% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.74 bps (+0.51% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.61 bps (+0.19% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 41.29 bps (-0.58% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 42.2 bps (+1.61% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl5: MAE 41.49 bps (-0.1% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl20: MAE 41.12 bps (-0.99% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20: MAE 41.05 bps (-1.16% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit7 hl20: CV MAE 64.34 → 62.73 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit7 hl20: MAE 42.12 bps (+1.42% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl20: 65.83 vs 64.52 bps, p = 0.697, failed |
| L16 | submit | accepted |

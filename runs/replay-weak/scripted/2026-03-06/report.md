# Weekly model review: 2026-03-06

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.9 bps vs 63.01 bps in the prior 26 weeks (-28.74%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20, scored 40.98 bps vs the champion's 44.9 bps (-8.73%). (L12)
- On the hidden window it scored 51.32 bps vs the champion's 59.39 bps (p = 0.0) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-03-06 |
| L02 | champion-report | champion MAE last 4w 49.79, last 26w 44.9, prior 26w 63.01 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 44.9 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.09 bps (-6.26% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.45 bps (-7.68% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.69 bps (-7.15% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.45 bps (-7.68% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 42.92 bps (-4.41% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 42.87 bps (-4.52% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 41.41 bps (-7.77% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 41.07 bps (-8.53% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 40.98 bps (-8.73% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: CV MAE 53.58 → 52.41 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: MAE 41.01 bps (-8.66% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: 51.32 vs 59.39 bps, p = 0.0, failed |
| L16 | submit | accepted |

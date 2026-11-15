# Weekly model review: 2025-07-04

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.09 bps vs 60.33 bps in the prior 26 weeks (+4.57%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10, scored 63.0 bps vs the champion's 63.09 bps (-0.14%). (L04)
- On the hidden window it scored 47.57 bps vs the champion's 46.42 bps (p = 0.746) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-03 |
| L02 | champion-report | champion MAE last 4w 52.64, last 26w 63.09, prior 26w 60.33 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 67.82 bps (+7.5% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.0 bps (-0.14% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.5 bps (+0.65% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 64.2 bps (+1.76% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 63.76 bps (+1.06% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 64.21 bps (+1.78% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 66.99 bps (+6.18% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 63.0 bps (-0.14% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 63.03 bps (-0.1% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 63.1 bps (+0.02% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 60.15 → 55.79 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 63.01 bps (-0.13% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: 47.57 vs 46.42 bps, p = 0.746, failed |
| L16 | submit | accepted |

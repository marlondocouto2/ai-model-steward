# Weekly model review: 2025-10-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.73 bps vs 55.82 bps in the prior 26 weeks (+1.63%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10, scored 55.69 bps vs the champion's 56.73 bps (-1.83%). (L07)
- On the hidden window it scored 41.64 bps vs the champion's 40.18 bps (p = 0.908) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-17 |
| L02 | champion-report | champion MAE last 4w 50.45, last 26w 56.73, prior 26w 55.82 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 62.05 bps (+9.38% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.43 bps (-0.53% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.59 bps (-0.25% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.19 bps (+0.81% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 55.69 bps (-1.83% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 57.61 bps (+1.55% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 59.57 bps (+5.01% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 55.71 bps (-1.8% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 55.81 bps (-1.62% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10: MAE 55.86 bps (-1.53% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: CV MAE 57.81 → 55.4 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: MAE 56.38 bps (-0.62% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: 41.64 vs 40.18 bps, p = 0.908, failed |
| L16 | submit | accepted |

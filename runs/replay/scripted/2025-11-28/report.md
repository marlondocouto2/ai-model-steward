# Weekly model review: 2025-11-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.71 bps vs 58.57 bps in the prior 26 weeks (-13.42%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10, scored 49.56 bps vs the champion's 50.71 bps (-2.27%). (L12)
- On the hidden window it scored 39.07 bps vs the champion's 38.86 bps (p = 0.616) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-11-28 |
| L02 | champion-report | champion MAE last 4w 43.77, last 26w 50.71, prior 26w 58.57 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.69 bps (+7.85% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.6 bps (-0.22% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.74 bps (+0.06% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.36 bps (+1.28% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 49.72 bps (-1.95% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 51.72 bps (+1.99% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 52.97 bps (+4.46% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 49.72 bps (-1.95% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 49.74 bps (-1.91% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10: MAE 49.56 bps (-2.27% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl10: CV MAE 58.16 → 55.25 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl10: MAE 49.99 bps (-1.42% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10: 39.07 vs 38.86 bps, p = 0.616, failed |
| L16 | submit | accepted |

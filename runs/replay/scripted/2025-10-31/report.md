# Weekly model review: 2025-10-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.98 bps vs 56.29 bps in the prior 26 weeks (-2.33%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5, scored 53.93 bps vs the champion's 54.98 bps (-1.91%). (L12)
- On the hidden window it scored 42.8 bps vs the champion's 41.27 bps (p = 0.963) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-31 |
| L02 | champion-report | champion MAE last 4w 38.1, last 26w 54.98, prior 26w 56.29 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 59.88 bps (+8.91% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.65 bps (-0.6% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.72 bps (-0.47% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.17 bps (+0.35% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 54.04 bps (-1.71% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 55.64 bps (+1.2% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 57.44 bps (+4.47% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 54.0 bps (-1.78% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 54.16 bps (-1.49% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 53.93 bps (-1.91% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl5: CV MAE 57.85 → 55.18 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl5: MAE 54.95 bps (-0.05% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: 42.8 vs 41.27 bps, p = 0.963, failed |
| L16 | submit | accepted |

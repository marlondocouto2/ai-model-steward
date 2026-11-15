# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.39 bps vs 55.34 bps in the prior 26 weeks (+1.9%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5, scored 55.3 bps vs the champion's 56.39 bps (-1.93%). (L10)
- On the hidden window it scored 43.55 bps vs the champion's 41.51 bps (p = 0.982) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-24 |
| L02 | champion-report | champion MAE last 4w 47.15, last 26w 56.39, prior 26w 55.34 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 61.41 bps (+8.9% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.94 bps (-0.8% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.13 bps (-0.46% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.59 bps (+0.35% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 55.34 bps (-1.86% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 57.24 bps (+1.51% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 60.02 bps (+6.44% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 55.3 bps (-1.93% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 55.48 bps (-1.61% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 55.3 bps (-1.93% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 57.87 → 55.36 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 56.17 bps (-0.39% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: 43.55 vs 41.51 bps, p = 0.982, failed |
| L16 | submit | accepted |

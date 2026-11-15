# Weekly model review: 2025-04-04

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.49 bps vs 54.96 bps in the prior 26 weeks (+4.6%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 57.69 bps vs the champion's 57.49 bps (+0.35%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-04-04 |
| L02 | champion-report | champion MAE last 4w 62.71, last 26w 57.49, prior 26w 54.96 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 61.21 bps (+6.47% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.08 bps (+1.03% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.59 bps (+1.91% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 59.45 bps (+3.41% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 62.47 bps (+8.66% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 63.1 bps (+9.76% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 64.03 bps (+11.38% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 58.01 bps (+0.9% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 58.36 bps (+1.51% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 57.99 bps (+0.87% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 58.99 → 57.43 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 57.69 bps (+0.35% vs champion) |
| L15 | submit | accepted |

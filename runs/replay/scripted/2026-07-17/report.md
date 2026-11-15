# Weekly model review: 2026-07-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.98 bps vs 42.71 bps in the prior 26 weeks (+24.05%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10, scored 52.99 bps vs the champion's 52.98 bps (+0.02%). (L05)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-17 |
| L02 | champion-report | champion MAE last 4w 51.77, last 26w 52.98, prior 26w 42.71 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 56.29 bps (+6.25% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.67 bps (+3.19% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.99 bps (+0.02% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.25 bps (+0.51% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 53.71 bps (+1.38% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 54.79 bps (+3.42% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 55.61 bps (+4.96% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 53.2 bps (+0.42% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 53.54 bps (+1.06% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 53.16 bps (+0.34% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 55.85 → 54.76 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 53.25 bps (+0.51% vs champion) |
| L15 | submit | accepted |

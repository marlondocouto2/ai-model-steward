# Weekly model review: 2026-08-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.44 bps vs 43.22 bps in the prior 26 weeks (+23.65%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10, scored 53.56 bps vs the champion's 53.44 bps (+0.22%). (L05)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-08-07 |
| L02 | champion-report | champion MAE last 4w 47.97, last 26w 53.44, prior 26w 43.22 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 57.09 bps (+6.83% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.09 bps (+3.09% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.56 bps (+0.22% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.68 bps (+0.45% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 54.03 bps (+1.1% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 54.91 bps (+2.75% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 57.21 bps (+7.05% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 53.69 bps (+0.47% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 53.95 bps (+0.95% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 53.56 bps (+0.22% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 56.51 → 55.17 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 53.69 bps (+0.47% vs champion) |
| L15 | submit | accepted |

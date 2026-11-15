# Weekly model review: 2025-09-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.5 bps vs 59.68 bps in the prior 26 weeks (-5.33%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10, scored 56.53 bps vs the champion's 56.5 bps (+0.05%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-09-19 |
| L02 | champion-report | champion MAE last 4w 42.26, last 26w 56.5, prior 26w 59.68 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 60.48 bps (+7.04% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.01 bps (+0.9% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.64 bps (+0.25% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.17 bps (+1.19% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 56.69 bps (+0.34% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 58.12 bps (+2.87% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 60.47 bps (+7.03% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 57.2 bps (+1.24% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 56.65 bps (+0.27% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 56.61 bps (+0.19% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: CV MAE 55.91 → 54.54 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 56.53 bps (+0.05% vs champion) |
| L15 | submit | accepted |

# Weekly model review: 2024-11-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.33 bps vs 44.29 bps in the prior 26 weeks (+40.73%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20, scored 62.03 bps vs the champion's 62.33 bps (-0.48%). (L14)
- On the hidden window it scored 48.83 bps vs the champion's 49.0 bps (p = 0.389) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-11-15 |
| L02 | champion-report | champion MAE last 4w 60.94, last 26w 62.33, prior 26w 44.29 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 67.97 bps (+9.05% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.57 bps (+1.99% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 62.54 bps (+0.34% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.2 bps (+1.4% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 63.55 bps (+1.96% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 65.54 bps (+5.15% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 64.87 bps (+4.08% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 62.67 bps (+0.55% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 62.17 bps (-0.26% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 62.24 bps (-0.14% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: CV MAE 61.06 → 60.08 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 62.03 bps (-0.48% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: 48.83 vs 49.0 bps, p = 0.389, failed |
| L16 | submit | accepted |

# Weekly model review: 2024-11-29

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.9 bps vs 39.75 bps in the prior 26 weeks (+58.24%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20, scored 62.69 bps vs the champion's 62.9 bps (-0.33%). (L14)
- On the hidden window it scored 52.67 bps vs the champion's 52.5 bps (p = 0.628) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-11-29 |
| L02 | champion-report | champion MAE last 4w 58.35, last 26w 62.9, prior 26w 39.75 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 68.72 bps (+9.25% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 64.08 bps (+1.88% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 62.99 bps (+0.14% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.7 bps (+1.27% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 63.82 bps (+1.46% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 65.49 bps (+4.12% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 64.83 bps (+3.07% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 62.92 bps (+0.03% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 62.88 bps (-0.03% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 62.91 bps (+0.02% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: CV MAE 60.37 → 59.57 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 62.69 bps (-0.33% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: 52.67 vs 52.5 bps, p = 0.628, failed |
| L16 | submit | accepted |

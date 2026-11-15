# Weekly model review: 2024-04-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 47.3 bps vs 53.68 bps in the prior 26 weeks (-11.89%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 46.68 bps vs the champion's 47.3 bps (-1.31%). (L10)
- On the hidden window it scored 45.98 bps vs the champion's 46.13 bps (p = 0.432) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-04-26 |
| L02 | champion-report | champion MAE last 4w 25.48, last 26w 47.3, prior 26w 53.68 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 51.83 bps (+9.58% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 48.13 bps (+1.75% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.74 bps (-1.18% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 47.1 bps (-0.42% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 47.8 bps (+1.06% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 47.16 bps (-0.3% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 49.43 bps (+4.5% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 46.68 bps (-1.31% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 46.7 bps (-1.27% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 46.72 bps (-1.23% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 64.12 → 63.85 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 47.18 bps (-0.25% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: 45.98 vs 46.13 bps, p = 0.432, failed |
| L16 | submit | accepted |

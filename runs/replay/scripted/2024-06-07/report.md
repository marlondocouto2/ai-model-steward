# Weekly model review: 2024-06-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 39.77 bps vs 53.98 bps in the prior 26 weeks (-26.32%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 39.36 bps vs the champion's 39.77 bps (-1.03%). (L14)
- On the hidden window it scored 60.0 bps vs the champion's 59.07 bps (p = 0.951) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-06-07 |
| L02 | champion-report | champion MAE last 4w 43.02, last 26w 39.77, prior 26w 53.98 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 42.69 bps (+7.34% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 40.17 bps (+1.01% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 39.58 bps (-0.48% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 39.85 bps (+0.2% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 40.26 bps (+1.23% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 39.77 bps (+0.0% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 40.99 bps (+3.07% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 39.39 bps (-0.96% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 39.39 bps (-0.96% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 39.38 bps (-0.98% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 63.07 → 62.42 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 39.36 bps (-1.03% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: 60.0 vs 59.07 bps, p = 0.951, failed |
| L16 | submit | accepted |

# Weekly model review: 2024-08-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.65 bps vs 53.77 bps in the prior 26 weeks (-13.24%). (L02)
- The best development candidate, lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10, scored 46.42 bps vs the champion's 46.65 bps (-0.49%). (L06)
- On the hidden window it scored 65.92 bps vs the champion's 65.91 bps (p = 0.531) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-08-09 |
| L02 | champion-report | champion MAE last 4w 76.63, last 26w 46.65, prior 26w 53.77 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 51.29 bps (+9.95% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 47.08 bps (+0.92% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.46 bps (-0.41% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.42 bps (-0.49% vs champion) |
| L07 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 46.8 bps (+0.32% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 47.02 bps (+0.79% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 47.99 bps (+2.87% vs champion) |
| L10 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 46.91 bps (+0.56% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 47.19 bps (+1.16% vs champion) |
| L12 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 46.69 bps (+0.09% vs champion) |
| L13 | tune | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 62.56 → 61.61 bps |
| L14 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 46.78 bps (+0.28% vs champion) |
| L15 | promote | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: 65.92 vs 65.91 bps, p = 0.531, failed |
| L16 | submit | accepted |

# Weekly model review: 2024-04-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.4 bps vs 52.25 bps in the prior 26 weeks (-3.54%). (L02)
- The best development candidate, lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 49.85 bps vs the champion's 50.4 bps (-1.09%). (L10)
- On the hidden window it scored 35.58 bps vs the champion's 34.07 bps (p = 0.938) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-04-12 |
| L02 | champion-report | champion MAE last 4w 33.93, last 26w 50.4, prior 26w 52.25 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.86 bps (+8.85% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.02 bps (+1.23% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 49.87 bps (-1.05% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 49.86 bps (-1.07% vs champion) |
| L07 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 51.41 bps (+2.0% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 50.58 bps (+0.36% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 51.32 bps (+1.83% vs champion) |
| L10 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 49.85 bps (-1.09% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 49.88 bps (-1.03% vs champion) |
| L12 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 49.91 bps (-0.97% vs champion) |
| L13 | tune | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 65.83 → 65.36 bps |
| L14 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 50.06 bps (-0.67% vs champion) |
| L15 | promote | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: 35.58 vs 34.07 bps, p = 0.938, failed |
| L16 | submit | accepted |

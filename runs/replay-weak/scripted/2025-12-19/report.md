# Weekly model review: 2025-12-19

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 48.38 bps vs 68.63 bps in the prior 26 weeks (-29.51%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5, scored 44.34 bps vs the champion's 48.38 bps (-8.35%). (L14)
- On the hidden window it scored 41.23 bps vs the champion's 42.67 bps (p = 0.076) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-19 |
| L02 | champion-report | champion MAE last 4w 39.42, last 26w 48.38, prior 26w 68.63 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 48.38 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.64 bps (-5.66% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.24 bps (-6.49% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.06 bps (-4.8% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 44.95 bps (-7.09% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 46.66 bps (-3.56% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 48.14 bps (-0.5% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 44.36 bps (-8.31% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 44.56 bps (-7.9% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 44.63 bps (-7.75% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 56.0 → 54.74 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 44.34 bps (-8.35% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: 41.23 vs 42.67 bps, p = 0.076, failed |
| L16 | submit | accepted |

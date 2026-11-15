# Weekly model review: 2026-04-17

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.52 bps vs 62.34 bps in the prior 26 weeks (-28.59%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5, scored 41.13 bps vs the champion's 44.52 bps (-7.61%). (L12)
- On the hidden window it scored 72.12 bps vs the champion's 73.76 bps (p = 0.307) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-04-17 |
| L02 | champion-report | champion MAE last 4w 51.04, last 26w 44.52, prior 26w 62.34 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 44.52 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.29 bps (-5.01% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 41.35 bps (-7.12% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.09 bps (-5.46% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 41.4 bps (-7.01% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 42.3 bps (-4.99% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 43.38 bps (-2.56% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 41.19 bps (-7.48% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 41.43 bps (-6.94% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 41.13 bps (-7.61% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 53.41 → 51.94 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 41.23 bps (-7.39% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: 72.12 vs 73.76 bps, p = 0.307, failed |
| L16 | submit | accepted |

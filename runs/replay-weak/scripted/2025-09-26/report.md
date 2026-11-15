# Weekly model review: 2025-09-26

**Decision: Switch.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.26 bps vs 63.75 bps in the prior 26 weeks (-5.47%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20, scored 55.68 bps vs the champion's 60.26 bps (-7.6%). (L11)
- On the hidden window it scored 44.66 bps vs the champion's 50.79 bps (p = 0.013) and passed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-09-26 |
| L02 | champion-report | champion MAE last 4w 53.07, last 26w 60.26, prior 26w 63.75 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 60.26 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.96 bps (-7.14% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.78 bps (-7.43% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.1 bps (-6.9% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 56.91 bps (-5.56% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 57.55 bps (-4.5% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 59.82 bps (-0.73% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 56.5 bps (-6.24% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 55.68 bps (-7.6% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 55.79 bps (-7.42% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: CV MAE 56.69 → 55.2 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 56.18 bps (-6.77% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: 44.66 vs 50.79 bps, p = 0.013, passed |
| L16 | submit | accepted |

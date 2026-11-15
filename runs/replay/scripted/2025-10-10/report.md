# Weekly model review: 2025-10-10

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.07 bps vs 57.23 bps in the prior 26 weeks (-2.03%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5, scored 55.61 bps vs the champion's 56.07 bps (-0.82%). (L12)
- On the hidden window it scored 39.45 bps vs the champion's 40.06 bps (p = 0.324) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-10 |
| L02 | champion-report | champion MAE last 4w 45.97, last 26w 56.07, prior 26w 57.23 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 60.68 bps (+8.22% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.97 bps (-0.18% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.0 bps (-0.12% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.33 bps (+0.46% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 55.66 bps (-0.73% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 57.53 bps (+2.6% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 59.86 bps (+6.76% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 55.65 bps (-0.75% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 55.74 bps (-0.59% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 55.61 bps (-0.82% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl5: CV MAE 58.04 → 55.65 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit7 hl5: MAE 56.25 bps (+0.32% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: 39.45 vs 40.06 bps, p = 0.324, failed |
| L16 | submit | accepted |

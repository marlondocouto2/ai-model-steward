# Weekly model review: 2025-11-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.22 bps vs 56.0 bps in the prior 26 weeks (-3.18%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10, scored 53.07 bps vs the champion's 54.22 bps (-2.12%). (L07)
- On the hidden window it scored 39.31 bps vs the champion's 37.95 bps (p = 0.949) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-11-14 |
| L02 | champion-report | champion MAE last 4w 39.97, last 26w 54.22, prior 26w 56.0 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 58.29 bps (+7.51% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.13 bps (-0.17% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.17 bps (-0.09% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.37 bps (+0.28% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 53.07 bps (-2.12% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 55.13 bps (+1.68% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 57.05 bps (+5.22% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 53.09 bps (-2.08% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 53.12 bps (-2.03% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10: MAE 53.27 bps (-1.75% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: CV MAE 57.87 → 55.62 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: MAE 53.63 bps (-1.09% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: 39.31 vs 37.95 bps, p = 0.949, failed |
| L16 | submit | accepted |

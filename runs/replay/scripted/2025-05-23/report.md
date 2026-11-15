# Weekly model review: 2025-05-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.62 bps vs 62.92 bps in the prior 26 weeks (-11.6%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5, scored 55.53 bps vs the champion's 55.62 bps (-0.16%). (L14)
- On the hidden window it scored 72.66 bps vs the champion's 72.51 bps (p = 0.538) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-05-23 |
| L02 | champion-report | champion MAE last 4w 57.77, last 26w 55.62, prior 26w 62.92 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 59.69 bps (+7.32% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.68 bps (+0.11% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.51 bps (+1.6% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.25 bps (+2.93% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 58.08 bps (+4.42% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 58.66 bps (+5.47% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 59.98 bps (+7.84% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 55.64 bps (+0.04% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 55.79 bps (+0.31% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 55.65 bps (+0.05% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 59.16 → 56.36 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 55.53 bps (-0.16% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: 72.66 vs 72.51 bps, p = 0.538, failed |
| L16 | submit | accepted |

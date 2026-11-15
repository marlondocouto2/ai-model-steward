# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.41 bps vs 59.31 bps in the prior 26 weeks (+3.54%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5, scored 55.3 bps vs the champion's 61.41 bps (-9.95%). (L10)
- On the hidden window it scored 43.55 bps vs the champion's 43.01 bps (p = 0.599) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-24 |
| L02 | champion-report | champion MAE last 4w 54.88, last 26w 61.41, prior 26w 59.31 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 61.41 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.94 bps (-8.91% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.13 bps (-8.6% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.59 bps (-7.85% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 55.34 bps (-9.88% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 57.24 bps (-6.79% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 60.02 bps (-2.26% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 55.3 bps (-9.95% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 55.48 bps (-9.66% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 55.3 bps (-9.95% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 57.87 → 55.36 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 56.17 bps (-8.53% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: 43.55 vs 43.01 bps, p = 0.599, failed |
| L16 | submit | accepted |

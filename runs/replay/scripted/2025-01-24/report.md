# Weekly model review: 2025-01-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.3 bps vs 43.55 bps in the prior 26 weeks (+40.76%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 61.56 bps vs the champion's 61.3 bps (+0.42%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-01-24 |
| L02 | champion-report | champion MAE last 4w 62.01, last 26w 61.3, prior 26w 43.55 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 65.43 bps (+6.74% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.7 bps (+0.65% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 62.61 bps (+2.14% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.2 bps (+3.1% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 66.18 bps (+7.96% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 67.69 bps (+10.42% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 67.39 bps (+9.93% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 61.66 bps (+0.59% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 62.01 bps (+1.16% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 61.63 bps (+0.54% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 59.91 → 59.38 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 61.56 bps (+0.42% vs champion) |
| L15 | submit | accepted |

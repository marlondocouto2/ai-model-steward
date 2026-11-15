# Weekly model review: 2025-04-25

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.11 bps vs 59.1 bps in the prior 26 weeks (-6.75%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5, scored 54.93 bps vs the champion's 55.11 bps (-0.33%). (L14)
- On the hidden window it scored 78.8 bps vs the champion's 79.27 bps (p = 0.322) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-04-25 |
| L02 | champion-report | champion MAE last 4w 43.64, last 26w 55.11, prior 26w 59.1 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 59.2 bps (+7.42% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.99 bps (-0.22% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.03 bps (+1.67% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.61 bps (+2.72% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 58.08 bps (+5.39% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 58.71 bps (+6.53% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 59.79 bps (+8.49% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 54.95 bps (-0.29% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 55.19 bps (+0.15% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 54.95 bps (-0.29% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 58.31 → 56.71 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 54.93 bps (-0.33% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: 78.8 vs 79.27 bps, p = 0.322, failed |
| L16 | submit | accepted |

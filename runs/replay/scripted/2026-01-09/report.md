# Weekly model review: 2026-01-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 43.73 bps vs 62.82 bps in the prior 26 weeks (-30.39%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5, scored 42.96 bps vs the champion's 43.73 bps (-1.76%). (L14)
- On the hidden window it scored 43.68 bps vs the champion's 42.96 bps (p = 0.86) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-09 |
| L02 | champion-report | champion MAE last 4w 34.56, last 26w 43.73, prior 26w 62.82 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 46.67 bps (+6.72% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.4 bps (+1.53% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.7 bps (-0.07% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.04 bps (+0.71% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 43.67 bps (-0.14% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 45.19 bps (+3.34% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 45.88 bps (+4.92% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 43.12 bps (-1.39% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.2 bps (-1.21% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 43.13 bps (-1.37% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 54.97 → 53.74 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 42.96 bps (-1.76% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: 43.68 vs 42.96 bps, p = 0.86, failed |
| L16 | submit | accepted |

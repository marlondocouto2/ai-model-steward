# Weekly model review: 2026-06-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.62 bps vs 45.31 bps in the prior 26 weeks (+11.72%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5, scored 50.61 bps vs the champion's 50.62 bps (-0.02%). (L12)
- On the hidden window it scored 48.1 bps vs the champion's 47.25 bps (p = 0.979) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-06-12 |
| L02 | champion-report | champion MAE last 4w 58.37, last 26w 50.62, prior 26w 45.31 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.15 bps (+6.97% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.29 bps (+3.3% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.88 bps (+0.51% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.1 bps (+0.95% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 50.93 bps (+0.61% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 51.93 bps (+2.59% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 52.83 bps (+4.37% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 50.7 bps (+0.16% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 51.31 bps (+1.36% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 50.61 bps (-0.02% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 55.28 → 54.29 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 51.07 bps (+0.89% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: 48.1 vs 47.25 bps, p = 0.979, failed |
| L16 | submit | accepted |

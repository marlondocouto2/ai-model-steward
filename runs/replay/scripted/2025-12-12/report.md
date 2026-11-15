# Weekly model review: 2025-12-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.25 bps vs 63.15 bps in the prior 26 weeks (-28.35%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20, scored 44.82 bps vs the champion's 45.25 bps (-0.95%). (L14)
- On the hidden window it scored 36.92 bps vs the champion's 36.59 bps (p = 0.725) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-12 |
| L02 | champion-report | champion MAE last 4w 40.28, last 26w 45.25, prior 26w 63.15 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 48.3 bps (+6.74% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.47 bps (+0.49% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.18 bps (-0.15% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.51 bps (+0.57% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 46.01 bps (+1.68% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 47.12 bps (+4.13% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 48.43 bps (+7.03% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 45.18 bps (-0.15% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 45.02 bps (-0.51% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 44.92 bps (-0.73% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: CV MAE 56.6 → 54.93 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: MAE 44.82 bps (-0.95% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: 36.92 vs 36.59 bps, p = 0.725, failed |
| L16 | submit | accepted |

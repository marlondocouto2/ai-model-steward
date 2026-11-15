# Weekly model review: 2025-08-08

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.97 bps vs 58.12 bps in the prior 26 weeks (+4.9%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20, scored 60.53 bps vs the champion's 60.97 bps (-0.72%). (L14)
- On the hidden window it scored 48.7 bps vs the champion's 48.75 bps (p = 0.456) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-08-08 |
| L02 | champion-report | champion MAE last 4w 42.15, last 26w 60.97, prior 26w 58.12 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 64.84 bps (+6.35% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.85 bps (+1.44% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.19 bps (+0.36% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.34 bps (+0.61% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 61.82 bps (+1.39% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 62.64 bps (+2.74% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 66.04 bps (+8.32% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 61.58 bps (+1.0% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 60.89 bps (-0.13% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 60.9 bps (-0.11% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: CV MAE 55.73 → 55.16 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 60.53 bps (-0.72% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: 48.7 vs 48.75 bps, p = 0.456, failed |
| L16 | submit | accepted |

# Weekly model review: 2026-04-10

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.64 bps vs 55.92 bps in the prior 26 weeks (-23.75%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5, scored 42.35 bps vs the champion's 42.64 bps (-0.68%). (L10)
- On the hidden window it scored 68.49 bps vs the champion's 68.19 bps (p = 0.618) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-04-10 |
| L02 | champion-report | champion MAE last 4w 51.95, last 26w 42.64, prior 26w 55.92 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 45.74 bps (+7.27% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.73 bps (+2.56% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.83 bps (+0.45% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 43.11 bps (+1.1% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 42.51 bps (-0.3% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 43.32 bps (+1.59% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 44.33 bps (+3.96% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 42.35 bps (-0.68% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.28 bps (+1.5% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl5: MAE 42.43 bps (-0.49% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: CV MAE 53.56 → 52.03 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl5: MAE 42.5 bps (-0.33% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: 68.49 vs 68.19 bps, p = 0.618, failed |
| L16 | submit | accepted |

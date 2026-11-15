# Weekly model review: 2024-08-02

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.58 bps vs 53.4 bps in the prior 26 weeks (-16.52%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10, scored 43.74 bps vs the champion's 44.58 bps (-1.88%). (L07)
- On the hidden window it scored 60.36 bps vs the champion's 57.62 bps (p = 0.876) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-08-02 |
| L02 | champion-report | champion MAE last 4w 59.26, last 26w 44.58, prior 26w 53.4 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 49.64 bps (+11.35% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.18 bps (+1.35% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.47 bps (-0.25% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 44.67 bps (+0.2% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 43.74 bps (-1.88% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 43.91 bps (-1.5% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 45.19 bps (+1.37% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl5: MAE 44.12 bps (-1.03% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl20: MAE 43.84 bps (-1.66% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit7 hl10: MAE 43.95 bps (-1.41% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: CV MAE 63.02 → 61.74 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 3y refit30 hl10: MAE 44.13 bps (-1.01% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: 60.36 vs 57.62 bps, p = 0.876, failed |
| L16 | submit | accepted |

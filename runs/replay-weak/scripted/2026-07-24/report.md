# Weekly model review: 2026-07-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.37 bps vs 46.35 bps in the prior 26 weeks (+21.62%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10, scored 52.68 bps vs the champion's 56.37 bps (-6.55%). (L05)
- On the hidden window it scored 51.06 bps vs the champion's 50.69 bps (p = 0.568) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-24 |
| L02 | champion-report | champion MAE last 4w 53.97, last 26w 56.37, prior 26w 46.35 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 56.37 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 54.3 bps (-3.67% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.68 bps (-6.55% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.18 bps (-5.66% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 53.59 bps (-4.93% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 54.96 bps (-2.5% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 56.54 bps (+0.3% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 52.96 bps (-6.05% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 53.27 bps (-5.5% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 52.8 bps (-6.33% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 56.01 → 54.86 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 53.04 bps (-5.91% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: 51.06 vs 50.69 bps, p = 0.568, failed |
| L16 | submit | accepted |

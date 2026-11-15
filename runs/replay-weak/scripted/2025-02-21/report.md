# Weekly model review: 2025-02-21

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.57 bps vs 54.4 bps in the prior 26 weeks (+11.34%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5, scored 57.17 bps vs the champion's 60.57 bps (-5.61%). (L14)
- On the hidden window it scored 61.73 bps vs the champion's 65.06 bps (p = 0.134) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-02-21 |
| L02 | champion-report | champion MAE last 4w 45.28, last 26w 60.57, prior 26w 54.4 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 60.57 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.34 bps (-5.33% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.56 bps (-3.32% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.79 bps (-2.94% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 60.96 bps (+0.64% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 62.09 bps (+2.51% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 62.35 bps (+2.94% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 57.27 bps (-5.45% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 57.66 bps (-4.8% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 57.29 bps (-5.42% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 59.33 → 58.48 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 57.17 bps (-5.61% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: 61.73 vs 65.06 bps, p = 0.134, failed |
| L16 | submit | accepted |

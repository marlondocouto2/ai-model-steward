# Weekly model review: 2026-06-12

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.15 bps vs 48.51 bps in the prior 26 weeks (+11.63%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5, scored 50.61 bps vs the champion's 54.15 bps (-6.54%). (L12)
- On the hidden window it scored 48.1 bps vs the champion's 49.84 bps (p = 0.212) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-06-12 |
| L02 | champion-report | champion MAE last 4w 57.63, last 26w 54.15, prior 26w 48.51 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.15 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.29 bps (-3.43% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.88 bps (-6.04% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.1 bps (-5.63% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 50.93 bps (-5.95% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 51.93 bps (-4.1% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 52.83 bps (-2.44% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 50.7 bps (-6.37% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 51.31 bps (-5.24% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 50.61 bps (-6.54% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 55.28 → 54.29 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 51.07 bps (-5.69% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: 48.1 vs 49.84 bps, p = 0.212, failed |
| L16 | submit | accepted |

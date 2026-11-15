# Weekly model review: 2025-08-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.23 bps vs 57.46 bps in the prior 26 weeks (+6.56%). (L02)
- The best development candidate, lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10, scored 60.95 bps vs the champion's 61.23 bps (-0.46%). (L14)
- On the hidden window it scored 46.99 bps vs the champion's 47.46 bps (p = 0.151) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-08-15 |
| L02 | champion-report | champion MAE last 4w 40.83, last 26w 61.23, prior 26w 57.46 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 65.3 bps (+6.65% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.79 bps (+0.91% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.51 bps (+0.46% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.37 bps (+0.23% vs champion) |
| L07 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 62.26 bps (+1.68% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 62.48 bps (+2.04% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 63.32 bps (+3.41% vs champion) |
| L10 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 61.94 bps (+1.16% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 61.89 bps (+1.08% vs champion) |
| L12 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 61.89 bps (+1.08% vs champion) |
| L13 | tune | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 55.85 → 54.46 bps |
| L14 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 60.95 bps (-0.46% vs champion) |
| L15 | promote | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: 46.99 vs 47.46 bps, p = 0.151, failed |
| L16 | submit | accepted |

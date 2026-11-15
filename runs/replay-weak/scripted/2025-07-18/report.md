# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 67.67 bps vs 66.06 bps in the prior 26 weeks (+2.44%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 63.3 bps vs the champion's 67.67 bps (-6.46%). (L10)
- On the hidden window it scored 45.99 bps vs the champion's 49.47 bps (p = 0.228) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-18 |
| L02 | champion-report | champion MAE last 4w 51.92, last 26w 67.67, prior 26w 66.06 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 67.67 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.35 bps (-6.38% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.36 bps (-6.37% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.84 bps (-5.66% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 63.45 bps (-6.24% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 64.54 bps (-4.63% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 67.56 bps (-0.16% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 63.3 bps (-6.46% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 63.41 bps (-6.3% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 63.38 bps (-6.34% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 58.3 → 56.21 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 63.33 bps (-6.41% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: 45.99 vs 49.47 bps, p = 0.228, failed |
| L16 | submit | accepted |

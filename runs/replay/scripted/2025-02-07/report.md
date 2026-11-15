# Weekly model review: 2025-02-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 58.44 bps vs 46.69 bps in the prior 26 weeks (+25.17%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 58.65 bps vs the champion's 58.44 bps (+0.36%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-02-07 |
| L02 | champion-report | champion MAE last 4w 57.78, last 26w 58.44, prior 26w 46.69 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 62.65 bps (+7.2% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.85 bps (+0.7% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 59.88 bps (+2.46% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 60.48 bps (+3.49% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 62.95 bps (+7.72% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 63.68 bps (+8.97% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 63.75 bps (+9.09% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 58.78 bps (+0.58% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 59.19 bps (+1.28% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 58.77 bps (+0.56% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 59.75 → 59.25 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 58.65 bps (+0.36% vs champion) |
| L15 | submit | accepted |

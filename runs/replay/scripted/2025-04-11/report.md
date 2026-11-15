# Weekly model review: 2025-04-11

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.06 bps vs 55.83 bps in the prior 26 weeks (+2.2%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 57.39 bps vs the champion's 57.06 bps (+0.58%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-04-11 |
| L02 | champion-report | champion MAE last 4w 55.52, last 26w 57.06, prior 26w 55.83 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 61.36 bps (+7.54% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 57.78 bps (+1.26% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.36 bps (+2.28% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 58.89 bps (+3.21% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 61.84 bps (+8.38% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 62.69 bps (+9.87% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 63.39 bps (+11.09% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 57.68 bps (+1.09% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 58.06 bps (+1.75% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 57.67 bps (+1.07% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 58.52 → 56.99 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 57.39 bps (+0.58% vs champion) |
| L15 | submit | accepted |

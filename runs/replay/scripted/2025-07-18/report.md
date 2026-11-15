# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.06 bps vs 61.91 bps in the prior 26 weeks (+1.86%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 63.3 bps vs the champion's 63.06 bps (+0.38%). (L10)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-18 |
| L02 | champion-report | champion MAE last 4w 49.9, last 26w 63.06, prior 26w 61.91 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 67.67 bps (+7.31% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.35 bps (+0.46% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.36 bps (+0.48% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.84 bps (+1.24% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 63.45 bps (+0.62% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 64.54 bps (+2.35% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 67.56 bps (+7.14% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 63.3 bps (+0.38% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 63.41 bps (+0.56% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 63.38 bps (+0.51% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 58.3 → 56.21 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 63.33 bps (+0.43% vs champion) |
| L15 | submit | accepted |

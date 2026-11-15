# Weekly model review: 2025-06-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.94 bps vs 60.42 bps in the prior 26 weeks (+5.83%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5, scored 63.99 bps vs the champion's 63.94 bps (+0.08%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-06-20 |
| L02 | champion-report | champion MAE last 4w 99.57, last 26w 63.94, prior 26w 60.42 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 69.21 bps (+8.24% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 64.08 bps (+0.22% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 64.7 bps (+1.19% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 65.14 bps (+1.88% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 64.94 bps (+1.56% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 66.22 bps (+3.57% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 68.31 bps (+6.83% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 64.03 bps (+0.14% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 64.2 bps (+0.41% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 64.11 bps (+0.27% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 58.66 → 56.56 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 63.99 bps (+0.08% vs champion) |
| L15 | submit | accepted |

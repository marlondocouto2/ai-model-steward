# Weekly model review: 2025-06-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 64.22 bps vs 59.19 bps in the prior 26 weeks (+8.5%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5, scored 63.96 bps vs the champion's 64.22 bps (-0.4%). (L10)
- On the hidden window it scored 47.96 bps vs the champion's 47.21 bps (p = 0.691) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-06-27 |
| L02 | champion-report | champion MAE last 4w 82.1, last 26w 64.22, prior 26w 59.19 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 69.29 bps (+7.89% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.97 bps (-0.39% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 64.66 bps (+0.69% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 65.11 bps (+1.39% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 64.65 bps (+0.67% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 65.45 bps (+1.92% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 67.81 bps (+5.59% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 63.96 bps (-0.4% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 64.01 bps (-0.33% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 64.05 bps (-0.26% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 59.06 → 56.66 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 64.04 bps (-0.28% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: 47.96 vs 47.21 bps, p = 0.691, failed |
| L16 | submit | accepted |

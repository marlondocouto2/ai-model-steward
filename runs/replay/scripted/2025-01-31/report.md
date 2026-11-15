# Weekly model review: 2025-01-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.43 bps vs 46.12 bps in the prior 26 weeks (+28.86%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5, scored 59.36 bps vs the champion's 59.43 bps (-0.12%). (L14)
- On the hidden window it scored 62.98 bps vs the champion's 62.93 bps (p = 0.483) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-01-31 |
| L02 | champion-report | champion MAE last 4w 62.1, last 26w 59.43, prior 26w 46.12 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 63.46 bps (+6.78% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 59.53 bps (+0.17% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 60.63 bps (+2.02% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.28 bps (+3.11% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 64.16 bps (+7.96% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 65.12 bps (+9.57% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 65.66 bps (+10.48% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 59.48 bps (+0.08% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 59.85 bps (+0.71% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 59.48 bps (+0.08% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: CV MAE 60.04 → 59.43 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 59.36 bps (-0.12% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: 62.98 vs 62.93 bps, p = 0.483, failed |
| L16 | submit | accepted |

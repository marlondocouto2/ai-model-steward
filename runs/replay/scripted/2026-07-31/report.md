# Weekly model review: 2026-07-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.11 bps vs 43.32 bps in the prior 26 weeks (+20.29%). (L02)
- The best development candidate, lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10, scored 51.83 bps vs the champion's 52.11 bps (-0.54%). (L14)
- On the hidden window it scored 47.92 bps vs the champion's 47.93 bps (p = 0.497) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-31 |
| L02 | champion-report | champion MAE last 4w 44.6, last 26w 52.11, prior 26w 43.32 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 55.75 bps (+6.99% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.67 bps (+2.99% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.28 bps (+0.33% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.19 bps (+0.15% vs champion) |
| L07 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 53.66 bps (+2.97% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 54.13 bps (+3.88% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 55.62 bps (+6.74% vs champion) |
| L10 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 52.4 bps (+0.56% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 52.55 bps (+0.84% vs champion) |
| L12 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 52.15 bps (+0.08% vs champion) |
| L13 | tune | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: CV MAE 55.91 → 54.53 bps |
| L14 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 51.83 bps (-0.54% vs champion) |
| L15 | promote | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: 47.92 vs 47.93 bps, p = 0.497, failed |
| L16 | submit | accepted |

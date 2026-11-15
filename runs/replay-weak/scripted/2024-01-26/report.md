# Weekly model review: 2024-01-26

**Decision: Switch.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.51 bps vs 68.69 bps in the prior 26 weeks (-17.73%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20, scored 52.38 bps vs the champion's 56.51 bps (-7.31%). (L11)
- On the hidden window it scored 46.22 bps vs the champion's 49.96 bps (p = 0.009) and passed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-01-26 |
| L02 | champion-report | champion MAE last 4w 32.71, last 26w 56.51, prior 26w 68.69 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 56.51 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.44 bps (-5.43% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.53 bps (-7.04% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.7 bps (-4.97% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 53.63 bps (-5.1% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 53.41 bps (-5.49% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 56.08 bps (-0.76% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 52.53 bps (-7.04% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 52.38 bps (-7.31% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 52.51 bps (-7.08% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: CV MAE 69.02 → 66.76 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 53.27 bps (-5.73% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: 46.22 vs 49.96 bps, p = 0.009, passed |
| L16 | submit | accepted |

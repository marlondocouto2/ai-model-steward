# Weekly model review: 2025-01-17

**Decision: Switch.** Champion: `ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5` (was `ewma all refit30 hl10`)

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 66.33 bps vs 46.41 bps in the prior 26 weeks (+42.92%). (L02)
- The best development candidate, ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5, scored 62.55 bps vs the champion's 66.33 bps (-5.7%). (L14)
- On the hidden window it scored 64.09 bps vs the champion's 67.99 bps (p = 0.073) and passed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-01-17 |
| L02 | champion-report | champion MAE last 4w 60.78, last 26w 66.33, prior 26w 46.41 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 66.33 bps (+0.0% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 62.68 bps (-5.5% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.39 bps (-4.43% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.57 bps (-4.16% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 67.12 bps (+1.19% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 68.38 bps (+3.09% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 67.95 bps (+2.44% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 62.64 bps (-5.56% vs champion) |
| L11 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 62.98 bps (-5.05% vs champion) |
| L12 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 62.62 bps (-5.59% vs champion) |
| L13 | tune | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: CV MAE 59.92 → 59.32 bps |
| L14 | backtest | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: MAE 62.55 bps (-5.7% vs champion) |
| L15 | promote | ridge[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl5: 64.09 vs 67.99 bps, p = 0.073, passed |
| L16 | submit | accepted |

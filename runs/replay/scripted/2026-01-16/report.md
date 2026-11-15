# Weekly model review: 2026-01-16

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.22 bps vs 63.01 bps in the prior 26 weeks (-32.99%). (L02)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20, scored 41.84 bps vs the champion's 42.22 bps (-0.9%). (L12)
- On the hidden window it scored 43.08 bps vs the champion's 42.52 bps (p = 0.944) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-16 |
| L02 | champion-report | champion MAE last 4w 33.1, last 26w 42.22, prior 26w 63.01 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 45.68 bps (+8.2% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.85 bps (+1.49% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.23 bps (+0.02% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.97 bps (+1.78% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 42.38 bps (+0.38% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 43.55 bps (+3.15% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 44.86 bps (+6.25% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 42.19 bps (-0.07% vs champion) |
| L11 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 41.86 bps (-0.85% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: MAE 41.84 bps (-0.9% vs champion) |
| L13 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: CV MAE 54.5 → 53.38 bps |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl20: MAE 42.08 bps (-0.33% vs champion) |
| L15 | promote | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl20: 43.08 vs 42.52 bps, p = 0.944, failed |
| L16 | submit | accepted |

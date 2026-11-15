# Weekly model review: 2024-07-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.53 bps vs 56.0 bps in the prior 26 weeks (-25.84%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 41.07 bps vs the champion's 41.53 bps (-1.11%). (L13)
- On the hidden window it scored 64.95 bps vs the champion's 64.52 bps (p = 0.697) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 59.77, last 26w 41.53, prior 26w 56.0 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.74 bps (+12.55% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.61 bps (+0.19% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.12 bps (-0.99% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.33 bps (+13.97% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.42 bps (-0.26% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.59 bps (+12.18% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.01 bps (+15.6% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.61 bps (+12.23% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.73 bps (+0.48% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.39 bps (+2.07% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.17 bps (-0.87% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.07 bps (-1.11% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.13 bps (-0.96% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.02 → 62.62 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 41.88 bps (+0.84% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 64.95 vs 64.52 bps, p = 0.697, failed |
| L18 | submit | accepted |

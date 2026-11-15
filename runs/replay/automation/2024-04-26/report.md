# Weekly model review: 2024-04-26

**Decision: Switch.** Champion: `xgboost[fx,mk,cal] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 47.3 bps vs 53.68 bps in the prior 26 weeks (-11.89%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 46.55 bps vs the champion's 47.3 bps (-1.59%). (L14)
- On the hidden window it scored 45.03 bps vs the champion's 46.13 bps (p = 0.019) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 25.48, last 26w 47.3, prior 26w 53.68 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 51.43 bps (+8.73% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 47.24 bps (-0.13% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 46.92 bps (-0.8% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 53.5 bps (+13.11% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 48.58 bps (+2.71% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 51.82 bps (+9.56% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.47 bps (+10.93% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 53.46 bps (+13.02% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 47.1 bps (-0.42% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 48.47 bps (+2.47% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 47.01 bps (-0.61% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 46.64 bps (-1.4% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 46.55 bps (-1.59% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 64.69 → 64.1 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 47.21 bps (-0.19% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 45.03 vs 46.13 bps, p = 0.019, passed |
| L18 | submit | accepted |

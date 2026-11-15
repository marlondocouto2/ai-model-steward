# Weekly model review: 2024-05-03

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.08 bps vs 53.01 bps in the prior 26 weeks (-13.07%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 45.41 bps vs the champion's 46.08 bps (-1.45%). (L13)
- On the hidden window it scored 49.75 bps vs the champion's 50.39 bps (p = 0.104) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 24.04, last 26w 46.08, prior 26w 53.01 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 50.84 bps (+10.33% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 45.89 bps (-0.41% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 45.7 bps (-0.82% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 52.32 bps (+13.54% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 47.24 bps (+2.52% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 50.67 bps (+9.96% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 51.18 bps (+11.07% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 52.2 bps (+13.28% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.59 bps (-1.06% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 47.11 bps (+2.24% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 46.77 bps (+1.5% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 45.41 bps (-1.45% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk,cal,lag] 2y refit7 hl20: MAE 46.59 bps (+1.11% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.81 → 63.73 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 46.65 bps (+1.24% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 49.75 vs 50.39 bps, p = 0.104, failed |
| L18 | submit | accepted |

# Weekly model review: 2024-03-01

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.12 bps vs 56.74 bps in the prior 26 weeks (-6.38%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 51.71 bps vs the champion's 53.12 bps (-2.65%). (L14)
- On the hidden window it scored 34.95 bps vs the champion's 35.04 bps (p = 0.438) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 37.85, last 26w 53.12, prior 26w 56.74 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.94 bps (+7.19% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 52.69 bps (-0.81% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.16 bps (-1.81% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 59.76 bps (+12.5% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.63 bps (+2.84% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 58.03 bps (+9.24% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.7 bps (+12.39% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.49 bps (+11.99% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.17 bps (+0.09% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.47 bps (+0.66% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 52.55 bps (-1.07% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.07 bps (-1.98% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 51.71 bps (-2.65% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 66.92 → 66.33 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 52.98 bps (-0.26% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 34.95 vs 35.04 bps, p = 0.438, failed |
| L18 | submit | accepted |

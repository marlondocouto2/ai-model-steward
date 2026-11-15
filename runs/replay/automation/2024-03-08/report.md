# Weekly model review: 2024-03-08

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.9 bps vs 54.98 bps in the prior 26 weeks (-3.78%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 51.66 bps vs the champion's 52.9 bps (-2.34%). (L14)
- On the hidden window it scored 32.97 bps vs the champion's 33.01 bps (p = 0.513) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 38.46, last 26w 52.9, prior 26w 54.98 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.58 bps (+6.96% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 52.69 bps (-0.4% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.11 bps (-1.49% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 59.66 bps (+12.78% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.29 bps (+2.63% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 58.36 bps (+10.32% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.13 bps (+11.78% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.59 bps (+12.65% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 52.99 bps (+0.17% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.71 bps (+1.53% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 52.47 bps (-0.81% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 51.97 bps (-1.76% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 51.66 bps (-2.34% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 67.14 → 66.48 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 52.9 bps (+0.0% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 32.97 vs 33.01 bps, p = 0.513, failed |
| L18 | submit | accepted |

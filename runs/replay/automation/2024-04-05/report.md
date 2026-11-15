# Weekly model review: 2024-04-05

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.94 bps vs 52.95 bps in the prior 26 weeks (-3.8%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 50.37 bps vs the champion's 50.94 bps (-1.12%). (L04)
- On the hidden window it scored 29.44 bps vs the champion's 30.17 bps (p = 0.058) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.15, last 26w 50.94, prior 26w 52.95 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.39 bps (+6.77% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.03 bps (+0.18% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.37 bps (-1.12% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.67 bps (+13.21% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 52.05 bps (+2.18% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.48 bps (+8.91% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.7 bps (+11.31% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 56.69 bps (+11.29% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.62 bps (-0.63% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 52.25 bps (+2.57% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.84 bps (-0.2% vs champion) |
| L13 | backtest | lightgbm[fx,dxy,mk,cal] all refit7 hl20: MAE 50.73 bps (-0.41% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 51.01 bps (+0.14% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 66.73 → 65.68 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 51.29 bps (+0.69% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 29.44 vs 30.17 bps, p = 0.058, passed |
| L18 | submit | accepted |

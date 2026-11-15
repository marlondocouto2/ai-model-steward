# Weekly model review: 2025-10-03

**Decision: Switch.** Champion: `xgboost[fx,mk,cal] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.11 bps vs 57.34 bps in the prior 26 weeks (-2.15%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 55.23 bps vs the champion's 56.11 bps (-1.57%). (L14)
- On the hidden window it scored 40.67 bps vs the champion's 41.72 bps (p = 0.012) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.31, last 26w 56.11, prior 26w 57.34 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.51 bps (+6.06% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.35 bps (+2.21% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.34 bps (-1.37% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 64.42 bps (+14.81% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.35 bps (+2.21% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.85 bps (+8.45% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.95 bps (+17.54% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.81 bps (+6.59% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.53 bps (+0.75% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.03 bps (+1.64% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.42 bps (-1.23% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.34 bps (-1.37% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 55.23 bps (-1.57% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 56.72 → 54.87 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 56.35 bps (+0.43% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 40.67 vs 41.72 bps, p = 0.012, passed |
| L18 | submit | accepted |

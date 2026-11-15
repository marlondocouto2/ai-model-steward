# Weekly model review: 2025-10-10

**Decision: Switch.** Champion: `xgboost[fx,mk,cal] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.07 bps vs 57.23 bps in the prior 26 weeks (-2.03%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 55.03 bps vs the champion's 56.07 bps (-1.85%). (L14)
- On the hidden window it scored 39.29 bps vs the champion's 40.06 bps (p = 0.092) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.97, last 26w 56.07, prior 26w 57.23 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 60.05 bps (+7.1% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.35 bps (+2.28% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.11 bps (-1.71% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 64.22 bps (+14.54% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.36 bps (+2.3% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.67 bps (+8.2% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.95 bps (+17.62% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.75 bps (+6.56% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.29 bps (+0.39% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.06 bps (+1.77% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.21 bps (-1.53% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.08 bps (-1.77% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 55.03 bps (-1.85% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 56.73 → 55.05 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 56.3 bps (+0.41% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 39.29 vs 40.06 bps, p = 0.092, passed |
| L18 | submit | accepted |

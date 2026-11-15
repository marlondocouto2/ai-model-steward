# Weekly model review: 2025-12-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.73 bps vs 61.98 bps in the prior 26 weeks (-26.22%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 44.52 bps vs the champion's 45.73 bps (-2.65%). (L04)
- On the hidden window it scored 36.02 bps vs the champion's 35.3 bps (p = 0.821) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 36.43, last 26w 45.73, prior 26w 61.98 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.36 bps (+5.75% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 45.88 bps (+0.33% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.52 bps (-2.65% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.9 bps (+13.49% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 46.59 bps (+1.88% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 48.33 bps (+5.69% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 54.14 bps (+18.39% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.81 bps (+6.74% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.62 bps (-0.24% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 46.14 bps (+0.9% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.72 bps (-2.21% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 44.61 bps (-2.45% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 44.67 bps (-2.32% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.98 → 54.67 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 45.18 bps (-1.2% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 36.02 vs 35.3 bps, p = 0.821, failed |
| L18 | submit | accepted |

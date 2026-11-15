# Weekly model review: 2025-12-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 45.25 bps vs 63.15 bps in the prior 26 weeks (-28.35%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 44.49 bps vs the champion's 45.25 bps (-1.68%). (L04)
- On the hidden window it scored 36.77 bps vs the champion's 36.59 bps (p = 0.722) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.28, last 26w 45.25, prior 26w 63.15 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.11 bps (+6.32% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 45.19 bps (-0.13% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.49 bps (-1.68% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.05 bps (+12.82% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.97 bps (+1.59% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 48.2 bps (+6.52% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.31 bps (+15.6% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.5 bps (+7.18% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.0 bps (-0.55% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.91 bps (+1.46% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.83 bps (-0.93% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 44.63 bps (-1.37% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 44.88 bps (-0.82% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.18 → 54.91 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 44.78 bps (-1.04% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 36.77 vs 36.59 bps, p = 0.722, failed |
| L18 | submit | accepted |

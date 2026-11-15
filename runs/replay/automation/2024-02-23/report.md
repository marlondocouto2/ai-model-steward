# Weekly model review: 2024-02-23

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.22 bps vs 57.96 bps in the prior 26 weeks (-6.45%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 52.77 bps vs the champion's 54.22 bps (-2.67%). (L14)
- On the hidden window it scored 38.76 bps vs the champion's 38.9 bps (p = 0.454) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 46.21, last 26w 54.22, prior 26w 57.96 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.85 bps (+6.69% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.77 bps (-0.83% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.18 bps (-1.92% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 59.86 bps (+10.4% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 55.72 bps (+2.77% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 58.35 bps (+7.62% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.34 bps (+11.29% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.04 bps (+10.73% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.16 bps (-0.11% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.31 bps (+0.17% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.65 bps (-1.05% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.15 bps (-1.97% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.77 bps (-2.67% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 67.99 → 66.46 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 54.0 bps (-0.41% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 38.76 vs 38.9 bps, p = 0.454, failed |
| L18 | submit | accepted |

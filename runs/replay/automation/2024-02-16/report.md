# Weekly model review: 2024-02-16

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.55 bps vs 58.75 bps in the prior 26 weeks (-7.15%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 53.19 bps vs the champion's 54.55 bps (-2.49%). (L14)
- On the hidden window it scored 38.18 bps vs the champion's 38.38 bps (p = 0.382) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.65, last 26w 54.55, prior 26w 58.75 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.17 bps (+6.64% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.21 bps (-0.62% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.63 bps (-1.69% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 60.75 bps (+11.37% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 56.31 bps (+3.23% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 58.66 bps (+7.53% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 61.67 bps (+13.05% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.88 bps (+11.6% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.55 bps (+0.0% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 55.03 bps (+0.88% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 54.03 bps (-0.95% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.64 bps (-1.67% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 53.19 bps (-2.49% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 68.63 → 66.69 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 54.51 bps (-0.07% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 38.18 vs 38.38 bps, p = 0.382, failed |
| L18 | submit | accepted |

# Weekly model review: 2024-10-11

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.64 bps vs 49.95 bps in the prior 26 weeks (+11.39%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 55.51 bps vs the champion's 55.64 bps (-0.23%). (L04)
- On the hidden window it scored 59.32 bps vs the champion's 58.13 bps (p = 0.888) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 73.37, last 26w 55.64, prior 26w 49.95 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 61.59 bps (+10.69% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 55.89 bps (+0.45% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.51 bps (-0.23% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.23 bps (+13.64% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 56.64 bps (+1.8% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.76 bps (+12.8% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 64.74 bps (+16.36% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.31 bps (+10.19% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.02 bps (+0.68% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 58.03 bps (+4.3% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.71 bps (+0.13% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.6 bps (-0.07% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 55.78 bps (+0.25% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.61 → 60.72 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 56.14 bps (+0.9% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 59.32 vs 58.13 bps, p = 0.888, failed |
| L18 | submit | accepted |

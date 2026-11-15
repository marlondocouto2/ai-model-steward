# Weekly model review: 2024-11-08

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.96 bps vs 44.34 bps in the prior 26 weeks (+37.48%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 60.9 bps vs the champion's 60.96 bps (-0.1%). (L16)
- On the hidden window it scored 47.19 bps vs the champion's 47.82 bps (p = 0.194) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 58.61, last 26w 60.96, prior 26w 44.34 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.78 bps (+7.91% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.12 bps (+1.9% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 61.06 bps (+0.16% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.98 bps (+13.16% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.41 bps (+2.38% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.75 bps (+11.14% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.98 bps (+16.44% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.98 bps (+9.88% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.83 bps (+1.43% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.43 bps (+4.05% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 61.3 bps (+0.56% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 61.2 bps (+0.39% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 61.18 bps (+0.36% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.77 → 59.93 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 60.9 bps (-0.1% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 47.19 vs 47.82 bps, p = 0.194, failed |
| L18 | submit | accepted |

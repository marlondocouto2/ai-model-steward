# Weekly model review: 2025-08-08

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.97 bps vs 58.12 bps in the prior 26 weeks (+4.9%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 60.43 bps vs the champion's 60.97 bps (-0.89%). (L16)
- On the hidden window it scored 49.12 bps vs the champion's 48.75 bps (p = 0.696) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 42.15, last 26w 60.97, prior 26w 58.12 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.16 bps (+5.23% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.59 bps (+2.66% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.87 bps (-0.16% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.16 bps (+11.79% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.39 bps (+3.97% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.88 bps (+9.69% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 68.23 bps (+11.91% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 63.79 bps (+4.63% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.36 bps (+0.64% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 62.01 bps (+1.71% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.81 bps (-0.26% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 61.0 bps (+0.05% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 61.29 bps (+0.52% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.18 → 54.81 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 60.43 bps (-0.89% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 49.12 vs 48.75 bps, p = 0.696, failed |
| L18 | submit | accepted |

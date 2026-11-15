# Weekly model review: 2024-12-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.8 bps vs 41.7 bps in the prior 26 weeks (+45.8%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 60.53 bps vs the champion's 60.8 bps (-0.44%). (L16)
- On the hidden window it scored 52.93 bps vs the champion's 53.74 bps (p = 0.194) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 46.66, last 26w 60.8, prior 26w 41.7 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 66.29 bps (+9.03% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.49 bps (+4.42% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 61.48 bps (+1.12% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 67.72 bps (+11.38% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.68 bps (+3.09% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.63 bps (+9.59% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.73 bps (+14.69% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.58 bps (+9.51% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.81 bps (+1.66% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.03 bps (+6.96% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 61.63 bps (+1.37% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 61.4 bps (+0.99% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 61.18 bps (+0.63% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 62.0 → 59.33 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 60.53 bps (-0.44% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 52.93 vs 53.74 bps, p = 0.194, failed |
| L18 | submit | accepted |

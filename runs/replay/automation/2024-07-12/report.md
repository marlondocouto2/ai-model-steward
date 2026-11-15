# Weekly model review: 2024-07-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.09 bps vs 56.17 bps in the prior 26 weeks (-26.85%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 40.52 bps vs the champion's 41.09 bps (-1.39%). (L13)
- On the hidden window it scored 70.24 bps vs the champion's 68.82 bps (p = 0.927) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.23, last 26w 41.09, prior 26w 56.17 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.79 bps (+11.44% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.12 bps (+0.07% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 40.56 bps (-1.29% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.26 bps (+15.02% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.2 bps (+0.27% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.68 bps (+11.17% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 47.81 bps (+16.35% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.9 bps (+11.71% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.27 bps (+0.44% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.05 bps (+2.34% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 40.63 bps (-1.12% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.52 bps (-1.39% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 40.59 bps (-1.22% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 63.58 → 62.17 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 40.94 bps (-0.37% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 70.24 vs 68.82 bps, p = 0.927, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-08-22

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.57 bps vs 57.47 bps in the prior 26 weeks (+5.39%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 60.39 bps vs the champion's 60.57 bps (-0.3%). (L12)
- On the hidden window it scored 44.8 bps vs the champion's 46.46 bps (p = 0.001) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 48.86, last 26w 60.57, prior 26w 57.47 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 63.7 bps (+5.17% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.76 bps (+1.96% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.61 bps (+0.07% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.8 bps (+13.59% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.44 bps (+3.09% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.27 bps (+9.41% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.38 bps (+14.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.5 bps (+6.49% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.34 bps (+1.27% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.31 bps (+1.22% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.39 bps (-0.3% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.79 bps (+0.36% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 60.75 bps (+0.3% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.21 → 54.49 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 60.42 bps (-0.25% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 44.8 vs 46.46 bps, p = 0.001, failed |
| L18 | submit | accepted |

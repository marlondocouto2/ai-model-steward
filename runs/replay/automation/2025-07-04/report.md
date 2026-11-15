# Weekly model review: 2025-07-04

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.09 bps vs 60.33 bps in the prior 26 weeks (+4.57%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 62.63 bps vs the champion's 63.09 bps (-0.73%). (L16)
- On the hidden window it scored 45.87 bps vs the champion's 46.42 bps (p = 0.182) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 52.64, last 26w 63.09, prior 26w 60.33 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 66.67 bps (+5.67% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.5 bps (+2.23% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.81 bps (-0.44% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 71.27 bps (+12.97% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.7 bps (+2.55% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 70.16 bps (+11.21% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.05 bps (+11.03% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.27 bps (+5.04% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.86 bps (+1.22% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.09 bps (+1.59% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.78 bps (-0.49% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.94 bps (-0.24% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.12 bps (+0.05% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.8 → 55.45 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 62.63 bps (-0.73% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 45.87 vs 46.42 bps, p = 0.182, failed |
| L18 | submit | accepted |

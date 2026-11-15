# Weekly model review: 2024-10-04

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.37 bps vs 50.53 bps in the prior 26 weeks (+7.6%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 54.06 bps vs the champion's 54.37 bps (-0.57%). (L04)
- On the hidden window it scored 57.86 bps vs the champion's 56.44 bps (p = 0.916) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 68.35, last 26w 54.37, prior 26w 50.53 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.62 bps (+9.66% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.57 bps (+0.37% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 54.06 bps (-0.57% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.78 bps (+13.63% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 55.09 bps (+1.32% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.48 bps (+13.08% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.33 bps (+16.48% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.4 bps (+9.25% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.46 bps (+0.17% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 56.47 bps (+3.86% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 54.18 bps (-0.35% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 54.18 bps (-0.35% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 54.59 bps (+0.4% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.98 → 60.8 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 54.57 bps (+0.37% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 57.86 vs 56.44 bps, p = 0.916, failed |
| L18 | submit | accepted |

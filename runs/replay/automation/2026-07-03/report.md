# Weekly model review: 2026-07-03

**Decision: Switch.** Champion: `xgboost[mk,lag] all refit7 hl10` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 51.21 bps vs 43.96 bps in the prior 26 weeks (+16.49%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 51.14 bps vs the champion's 51.21 bps (-0.14%). (L14)
- On the hidden window it scored 50.76 bps vs the champion's 52.76 bps (p = 0.033) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.1, last 26w 51.21, prior 26w 43.96 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 55.86 bps (+9.08% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 52.23 bps (+1.99% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 51.45 bps (+0.47% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 56.26 bps (+9.86% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 52.84 bps (+3.18% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 54.52 bps (+6.46% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 55.53 bps (+8.44% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.08 bps (+7.56% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.87 bps (+1.29% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 52.46 bps (+2.44% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 51.18 bps (-0.06% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 51.57 bps (+0.7% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 51.14 bps (-0.14% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.66 → 54.02 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 51.75 bps (+1.05% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 50.76 vs 52.76 bps, p = 0.033, passed |
| L18 | submit | accepted |

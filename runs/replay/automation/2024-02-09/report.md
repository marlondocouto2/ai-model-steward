# Weekly model review: 2024-02-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.62 bps vs 60.19 bps in the prior 26 weeks (-10.92%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 52.31 bps vs the champion's 53.62 bps (-2.44%). (L14)
- On the hidden window it scored 40.57 bps vs the champion's 41.45 bps (p = 0.108) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 35.5, last 26w 53.62, prior 26w 60.19 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.15 bps (+6.58% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.26 bps (-0.67% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.7 bps (-1.72% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 59.9 bps (+11.71% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.36 bps (+1.38% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.92 bps (+8.02% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 60.38 bps (+12.61% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.64 bps (+11.23% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.57 bps (-0.09% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.5 bps (+1.64% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.11 bps (-0.95% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.69 bps (-1.73% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.31 bps (-2.44% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 68.53 → 66.7 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 53.37 bps (-0.47% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 40.57 vs 41.45 bps, p = 0.108, failed |
| L18 | submit | accepted |

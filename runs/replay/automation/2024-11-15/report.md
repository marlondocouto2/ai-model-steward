# Weekly model review: 2024-11-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.33 bps vs 44.29 bps in the prior 26 weeks (+40.73%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 62.75 bps vs the champion's 62.33 bps (+0.67%). (L04)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 60.94, last 26w 62.33, prior 26w 44.29 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 68.01 bps (+9.11% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.63 bps (+2.09% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.75 bps (+0.67% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 71.09 bps (+14.05% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.81 bps (+2.37% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.79 bps (+11.97% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 73.02 bps (+17.15% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.59 bps (+10.04% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.34 bps (+1.62% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.81 bps (+3.98% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.92 bps (+0.95% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.87 bps (+0.87% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 62.75 bps (+0.67% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 62.2 → 60.33 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 62.95 bps (+0.99% vs champion) |
| L17 | submit | accepted |

# Weekly model review: 2025-01-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.14 bps vs 41.39 bps in the prior 26 weeks (+50.13%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 62.14 bps vs the champion's 62.14 bps (+0.0%). (L16)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.54, last 26w 62.14, prior 26w 41.39 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.74 bps (+9.01% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 65.57 bps (+5.52% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.08 bps (+1.51% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 69.46 bps (+11.78% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.91 bps (+4.46% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 68.23 bps (+9.8% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.04 bps (+12.71% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.65 bps (+10.48% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.27 bps (+1.82% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 66.45 bps (+6.94% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.16 bps (+1.64% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.93 bps (+1.27% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 62.64 bps (+0.8% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 61.37 → 58.37 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 62.14 bps (+0.0% vs champion) |
| L17 | submit | accepted |

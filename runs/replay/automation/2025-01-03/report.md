# Weekly model review: 2025-01-03

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.24 bps vs 41.65 bps in the prior 26 weeks (+44.63%). (L01)
- The best development candidate, lightgbm[fx,dxy,mk] tuned all refit7 hl20, scored 60.51 bps vs the champion's 60.24 bps (+0.45%). (L16)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.81, last 26w 60.24, prior 26w 41.65 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.04 bps (+7.97% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.23 bps (+4.96% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 61.1 bps (+1.43% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 67.77 bps (+12.5% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.68 bps (+5.71% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.12 bps (+9.76% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 69.56 bps (+15.47% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.84 bps (+10.96% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.95 bps (+1.18% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.5 bps (+7.07% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 61.12 bps (+1.46% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.95 bps (+1.18% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk,cal,lag] 2y refit7 hl20: MAE 62.92 bps (+4.45% vs champion) |
| L15 | tune | lightgbm[fx,dxy,mk] tuned all refit7 hl20: CV MAE 60.48 → 58.55 bps |
| L16 | backtest | lightgbm[fx,dxy,mk] tuned all refit7 hl20: MAE 60.51 bps (+0.45% vs champion) |
| L17 | submit | accepted |

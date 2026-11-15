# Weekly model review: 2026-08-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.44 bps vs 43.22 bps in the prior 26 weeks (+23.65%). (L01)
- The best development candidate, xgboost[vol,mk,lag] all refit7 hl20, scored 53.56 bps vs the champion's 53.44 bps (+0.22%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 47.97, last 26w 53.44, prior 26w 43.22 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.81 bps (+10.05% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.32 bps (+1.65% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.71 bps (+0.51% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 58.4 bps (+9.28% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 55.26 bps (+3.41% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 56.39 bps (+5.52% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 57.19 bps (+7.02% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.75 bps (+8.07% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.66 bps (+0.41% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.65 bps (+2.26% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 54.48 bps (+1.95% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.91 bps (+0.88% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 53.56 bps (+0.22% vs champion) |
| L15 | tune | xgboost[vol,mk,lag] tuned all refit7 hl20: CV MAE 56.87 → 55.34 bps |
| L16 | backtest | xgboost[vol,mk,lag] tuned all refit7 hl20: MAE 54.76 bps (+2.47% vs champion) |
| L17 | submit | accepted |

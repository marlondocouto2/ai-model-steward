# Weekly model review: 2025-03-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.91 bps vs 49.59 bps in the prior 26 weeks (+20.81%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 59.27 bps vs the champion's 59.91 bps (-1.07%). (L16)
- On the hidden window it scored 50.75 bps vs the champion's 50.96 bps (p = 0.365) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 74.69, last 26w 59.91, prior 26w 49.59 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.9 bps (+10.0% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.12 bps (+7.03% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.5 bps (+0.98% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.34 bps (+9.06% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.32 bps (+7.36% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 65.52 bps (+9.36% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.13 bps (+8.71% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.4 bps (+10.83% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.79 bps (+1.47% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.05 bps (+6.91% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.52 bps (+1.02% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.42 bps (+0.85% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 60.02 bps (+0.18% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 59.63 → 57.41 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 59.27 bps (-1.07% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 50.75 vs 50.96 bps, p = 0.365, failed |
| L18 | submit | accepted |

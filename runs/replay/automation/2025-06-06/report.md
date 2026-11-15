# Weekly model review: 2025-06-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.23 bps vs 62.21 bps in the prior 26 weeks (-3.18%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 60.72 bps vs the champion's 60.23 bps (+0.81%). (L04)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 84.69, last 26w 60.23, prior 26w 62.21 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.22 bps (+8.28% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.39 bps (+3.59% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.72 bps (+0.81% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 67.39 bps (+11.89% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.09 bps (+6.41% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.68 bps (+10.71% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 64.9 bps (+7.75% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 65.29 bps (+8.4% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.27 bps (+1.73% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.69 bps (+5.74% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.77 bps (+0.9% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.8 bps (+0.95% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 61.14 bps (+1.51% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 57.7 → 55.96 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 60.72 bps (+0.81% vs champion) |
| L17 | submit | accepted |

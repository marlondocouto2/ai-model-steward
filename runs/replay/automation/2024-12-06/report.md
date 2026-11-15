# Weekly model review: 2024-12-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.35 bps vs 40.77 bps in the prior 26 weeks (+52.93%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 62.59 bps vs the champion's 62.35 bps (+0.38%). (L12)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 51.12, last 26w 62.35, prior 26w 40.77 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 66.82 bps (+7.17% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.83 bps (+2.37% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.63 bps (+0.45% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 71.06 bps (+13.97% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.96 bps (+4.19% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.66 bps (+11.72% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 73.58 bps (+18.01% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.72 bps (+10.22% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.39 bps (+1.67% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.56 bps (+3.54% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.59 bps (+0.38% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.67 bps (+0.51% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.51 bps (+1.86% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 61.03 → 59.65 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 62.85 bps (+0.8% vs champion) |
| L17 | submit | accepted |

# Weekly model review: 2025-02-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 58.44 bps vs 46.69 bps in the prior 26 weeks (+25.17%). (L01)
- The best development candidate, ridge[fx,dxy,mk] tuned all refit7 hl20, scored 58.02 bps vs the champion's 58.44 bps (-0.72%). (L16)
- On the hidden window it scored 64.94 bps vs the champion's 64.94 bps (p = 0.499) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 57.78, last 26w 58.44, prior 26w 46.69 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 63.53 bps (+8.71% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.62 bps (+5.44% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 59.15 bps (+1.21% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.6 bps (+12.25% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.15 bps (+4.64% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 63.96 bps (+9.45% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 66.42 bps (+13.66% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.39 bps (+10.18% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 59.03 bps (+1.01% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.74 bps (+5.65% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 58.73 bps (+0.5% vs champion) |
| L13 | backtest | ridge[fx,dxy,mk,cal] all refit7 hl20: MAE 58.96 bps (+0.89% vs champion) |
| L14 | backtest | ridge[fx,mk,cal] all refit7 hl20: MAE 58.92 bps (+0.82% vs champion) |
| L15 | tune | ridge[fx,dxy,mk] tuned all refit7 hl20: CV MAE 59.83 → 57.79 bps |
| L16 | backtest | ridge[fx,dxy,mk] tuned all refit7 hl20: MAE 58.02 bps (-0.72% vs champion) |
| L17 | promote | ridge[fx,dxy,mk] tuned all refit7 hl20: 64.94 vs 64.94 bps, p = 0.499, failed |
| L18 | submit | accepted |

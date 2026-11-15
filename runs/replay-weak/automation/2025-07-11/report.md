# Weekly model review: 2025-07-11

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 67.95 bps vs 65.02 bps in the prior 26 weeks (+4.51%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 62.77 bps vs the champion's 67.95 bps (-7.62%). (L12)
- On the hidden window it scored 46.86 bps vs the champion's 48.15 bps (p = 0.359) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.42, last 26w 67.95, prior 26w 65.02 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.38 bps (-0.84% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.28 bps (-5.4% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.85 bps (-7.51% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 71.24 bps (+4.84% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.92 bps (-4.46% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.99 bps (+3.0% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.65 bps (+3.97% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.53 bps (-2.09% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.54 bps (-6.49% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.07 bps (-5.71% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.77 bps (-7.62% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.04 bps (-7.23% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.18 bps (-7.02% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.86 → 55.34 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 62.85 bps (-7.51% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 46.86 vs 48.15 bps, p = 0.359, failed |
| L18 | submit | accepted |

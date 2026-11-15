# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.41 bps vs 59.31 bps in the prior 26 weeks (+3.54%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 55.11 bps vs the champion's 61.41 bps (-10.26%). (L14)
- On the hidden window it scored 42.48 bps vs the champion's 43.01 bps (p = 0.409) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 54.88, last 26w 61.41, prior 26w 59.31 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 59.91 bps (-2.44% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.07 bps (-7.07% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.24 bps (-10.05% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.26 bps (+6.27% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.67 bps (-6.09% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.9 bps (-0.83% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 66.63 bps (+8.5% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.34 bps (-1.74% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.58 bps (-7.87% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 56.54 bps (-7.93% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.49 bps (-9.64% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.2 bps (-10.11% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 55.11 bps (-10.26% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 56.3 → 54.66 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 56.65 bps (-7.75% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 42.48 vs 43.01 bps, p = 0.409, failed |
| L18 | submit | accepted |

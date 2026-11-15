# Weekly model review: 2024-12-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.28 bps vs 40.61 bps in the prior 26 weeks (+45.97%). (L01)
- The best development candidate, xgboost[vol,mk,lag] tuned all refit7 hl20, scored 59.08 bps vs the champion's 59.28 bps (-0.34%). (L16)
- On the hidden window it scored 57.23 bps vs the champion's 57.06 bps (p = 0.565) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 43.16, last 26w 59.28, prior 26w 40.61 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.39 bps (+8.62% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.26 bps (+5.03% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.23 bps (+1.6% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.44 bps (+12.08% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 62.92 bps (+6.14% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 64.94 bps (+9.55% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 68.5 bps (+15.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 65.21 bps (+10.0% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.26 bps (+1.65% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.77 bps (+7.57% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.29 bps (+1.7% vs champion) |
| L13 | backtest | lightgbm[fx,dxy,mk,cal] all refit7 hl20: MAE 60.96 bps (+2.83% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 59.87 bps (+1.0% vs champion) |
| L15 | tune | xgboost[vol,mk,lag] tuned all refit7 hl20: CV MAE 60.65 → 58.8 bps |
| L16 | backtest | xgboost[vol,mk,lag] tuned all refit7 hl20: MAE 59.08 bps (-0.34% vs champion) |
| L17 | promote | xgboost[vol,mk,lag] tuned all refit7 hl20: 57.23 vs 57.06 bps, p = 0.565, failed |
| L18 | submit | accepted |

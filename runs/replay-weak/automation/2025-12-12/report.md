# Weekly model review: 2025-12-12

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 48.3 bps vs 68.64 bps in the prior 26 weeks (-29.63%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 44.49 bps vs the champion's 48.3 bps (-7.89%). (L04)
- On the hidden window it scored 36.77 bps vs the champion's 38.55 bps (p = 0.017) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.05, last 26w 48.3, prior 26w 68.64 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.11 bps (-0.39% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 45.19 bps (-6.44% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.49 bps (-7.89% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 51.05 bps (+5.69% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.97 bps (-4.82% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 48.2 bps (-0.21% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.31 bps (+8.3% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.5 bps (+0.41% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 45.0 bps (-6.83% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.91 bps (-4.95% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 44.83 bps (-7.18% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 44.63 bps (-7.6% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 44.88 bps (-7.08% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.18 → 54.91 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 44.78 bps (-7.29% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 36.77 vs 38.55 bps, p = 0.017, failed |
| L18 | submit | accepted |

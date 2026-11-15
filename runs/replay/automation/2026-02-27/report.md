# Weekly model review: 2026-02-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.97 bps vs 59.4 bps in the prior 26 weeks (-29.34%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 41.45 bps vs the champion's 41.97 bps (-1.24%). (L04)
- On the hidden window it scored 43.68 bps vs the champion's 43.53 bps (p = 0.621) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.81, last 26w 41.97, prior 26w 59.4 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.43 bps (+5.86% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.74 bps (-0.55% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.45 bps (-1.24% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.77 bps (+16.2% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.9 bps (+2.22% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.86 bps (+6.89% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 49.77 bps (+18.58% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.58 bps (+8.6% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.28 bps (+0.74% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.31 bps (+0.81% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.7 bps (-0.64% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.49 bps (-1.14% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.83 bps (-0.33% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 53.42 → 52.15 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 41.78 bps (-0.45% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 43.68 vs 43.53 bps, p = 0.621, failed |
| L18 | submit | accepted |

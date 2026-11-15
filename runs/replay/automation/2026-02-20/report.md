# Weekly model review: 2026-02-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.31 bps vs 60.79 bps in the prior 26 weeks (-30.4%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 41.71 bps vs the champion's 42.31 bps (-1.42%). (L04)
- On the hidden window it scored 45.32 bps vs the champion's 44.93 bps (p = 0.816) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.15, last 26w 42.31, prior 26w 60.79 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.61 bps (+5.44% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.1 bps (-0.5% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.71 bps (-1.42% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.61 bps (+14.89% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.59 bps (+0.66% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.67 bps (+5.58% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 49.92 bps (+17.99% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.94 bps (+6.22% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.77 bps (+1.09% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.67 bps (+0.85% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 42.05 bps (-0.61% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 41.75 bps (-1.32% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 42.06 bps (-0.59% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.73 → 52.83 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.42 bps (+0.26% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 45.32 vs 44.93 bps, p = 0.816, failed |
| L18 | submit | accepted |

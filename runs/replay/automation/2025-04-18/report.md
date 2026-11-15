# Weekly model review: 2025-04-18

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.78 bps vs 57.57 bps in the prior 26 weeks (-3.11%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 54.79 bps vs the champion's 55.78 bps (-1.77%). (L16)
- On the hidden window it scored 80.24 bps vs the champion's 80.03 bps (p = 0.546) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 48.91, last 26w 55.78, prior 26w 57.57 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 60.32 bps (+8.14% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 58.6 bps (+5.06% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 56.34 bps (+1.0% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.88 bps (+10.94% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.94 bps (+5.67% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.91 bps (+9.2% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 61.44 bps (+10.15% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.6 bps (+8.64% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.07 bps (+2.31% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 58.37 bps (+4.64% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 56.11 bps (+0.59% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 56.39 bps (+1.09% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 56.52 bps (+1.33% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 57.4 → 55.85 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 54.79 bps (-1.77% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 80.24 vs 80.03 bps, p = 0.546, failed |
| L18 | submit | accepted |

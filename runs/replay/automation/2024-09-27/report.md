# Weekly model review: 2024-09-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.74 bps vs 51.74 bps in the prior 26 weeks (-1.93%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 50.32 bps vs the champion's 50.74 bps (-0.83%). (L04)
- On the hidden window it scored 68.01 bps vs the champion's 65.48 bps (p = 0.995) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.15, last 26w 50.74, prior 26w 51.74 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.1 bps (+10.56% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.03 bps (+0.57% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.32 bps (-0.83% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 58.52 bps (+15.33% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 51.81 bps (+2.11% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.93 bps (+14.17% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.98 bps (+18.21% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.72 bps (+9.81% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.17 bps (+0.85% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 52.63 bps (+3.72% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.4 bps (-0.67% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 50.55 bps (-0.37% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 50.94 bps (+0.39% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.47 → 60.45 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 50.96 bps (+0.43% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 68.01 vs 65.48 bps, p = 0.995, failed |
| L18 | submit | accepted |

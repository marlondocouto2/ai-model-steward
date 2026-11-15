# Weekly model review: 2026-03-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.64 bps vs 56.44 bps in the prior 26 weeks (-24.45%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.32 bps vs the champion's 42.64 bps (-0.75%). (L04)
- On the hidden window it scored 62.41 bps vs the champion's 62.23 bps (p = 0.564) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 46.95, last 26w 42.64, prior 26w 56.44 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.86 bps (+5.21% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.76 bps (+0.28% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.32 bps (-0.75% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.28 bps (+13.23% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.92 bps (+0.66% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.95 bps (+7.76% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 49.0 bps (+14.92% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.17 bps (+8.28% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.95 bps (+0.73% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.67 bps (+0.07% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 42.6 bps (-0.09% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 42.35 bps (-0.68% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 42.63 bps (-0.02% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 53.2 → 52.26 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.59 bps (-0.12% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 62.41 vs 62.23 bps, p = 0.564, failed |
| L18 | submit | accepted |

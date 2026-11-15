# Weekly model review: 2026-05-22

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 47.79 bps vs 53.5 bps in the prior 26 weeks (-10.67%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 47.47 bps vs the champion's 47.79 bps (-0.67%). (L14)
- On the hidden window it scored 52.48 bps vs the champion's 51.89 bps (p = 0.913) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 87.52, last 26w 47.79, prior 26w 53.5 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 52.16 bps (+9.14% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.59 bps (+1.67% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 48.09 bps (+0.63% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 53.34 bps (+11.61% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.22 bps (+2.99% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 50.41 bps (+5.48% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 53.18 bps (+11.28% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 50.7 bps (+6.09% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 48.76 bps (+2.03% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 48.86 bps (+2.24% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 47.89 bps (+0.21% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 48.28 bps (+1.03% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 47.47 bps (-0.67% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.14 → 53.36 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 47.96 bps (+0.36% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 52.48 vs 51.89 bps, p = 0.913, failed |
| L18 | submit | accepted |

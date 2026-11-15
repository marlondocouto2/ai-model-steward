# Weekly model review: 2026-05-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 47.36 bps vs 54.11 bps in the prior 26 weeks (-12.47%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 46.99 bps vs the champion's 47.36 bps (-0.78%). (L14)
- On the hidden window it scored 49.73 bps vs the champion's 49.27 bps (p = 0.88) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 83.33, last 26w 47.36, prior 26w 54.11 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 51.7 bps (+9.16% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.1 bps (+1.56% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 47.69 bps (+0.7% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 53.11 bps (+12.14% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 48.37 bps (+2.13% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 50.36 bps (+6.33% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.65 bps (+11.17% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 50.21 bps (+6.02% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 48.35 bps (+2.09% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 48.56 bps (+2.53% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 47.44 bps (+0.17% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 47.85 bps (+1.03% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 46.99 bps (-0.78% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.01 → 53.05 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 47.39 bps (+0.06% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 49.73 vs 49.27 bps, p = 0.88, failed |
| L18 | submit | accepted |

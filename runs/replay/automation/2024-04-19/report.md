# Weekly model review: 2024-04-19

**Decision: Switch.** Champion: `xgboost[fx,mk,cal] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 48.72 bps vs 53.87 bps in the prior 26 weeks (-9.56%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 48.02 bps vs the champion's 48.72 bps (-1.44%). (L14)
- On the hidden window it scored 42.65 bps vs the champion's 43.67 bps (p = 0.023) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 27.92, last 26w 48.72, prior 26w 53.87 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 52.74 bps (+8.25% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.73 bps (+0.02% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 48.36 bps (-0.74% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.01 bps (+12.91% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 50.61 bps (+3.88% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 52.9 bps (+8.58% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 54.09 bps (+11.02% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.14 bps (+13.18% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 48.65 bps (-0.14% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 49.98 bps (+2.59% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 48.41 bps (-0.64% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 48.12 bps (-1.23% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 48.02 bps (-1.44% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 65.27 → 64.79 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 48.69 bps (-0.06% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 42.65 vs 43.67 bps, p = 0.023, passed |
| L18 | submit | accepted |

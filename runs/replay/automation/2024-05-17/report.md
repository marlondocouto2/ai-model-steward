# Weekly model review: 2024-05-17

**Decision: Switch.** Champion: `xgboost[fx,mk,cal,lag] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.43 bps vs 51.36 bps in the prior 26 weeks (-13.49%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 43.74 bps vs the champion's 44.43 bps (-1.55%). (L13)
- On the hidden window it scored 53.4 bps vs the champion's 54.06 bps (p = 0.076) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 29.07, last 26w 44.43, prior 26w 51.36 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 49.41 bps (+11.21% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.63 bps (+0.45% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.08 bps (-0.79% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.85 bps (+9.95% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.42 bps (+2.23% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 49.72 bps (+11.91% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.23 bps (+8.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 49.82 bps (+12.13% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.88 bps (-1.24% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.96 bps (+3.44% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 44.62 bps (+0.43% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 43.74 bps (-1.55% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk,cal,lag] 2y refit7 hl20: MAE 45.05 bps (+1.4% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.66 → 63.38 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 44.66 bps (+0.52% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 53.4 vs 54.06 bps, p = 0.076, passed |
| L18 | submit | accepted |

# Weekly model review: 2024-05-10

**Decision: Switch.** Champion: `xgboost[fx,mk,cal,lag] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.51 bps vs 51.99 bps in the prior 26 weeks (-14.39%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 43.76 bps vs the champion's 44.51 bps (-1.69%). (L13)
- On the hidden window it scored 53.63 bps vs the champion's 54.27 bps (p = 0.095) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 25.35, last 26w 44.51, prior 26w 51.99 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 49.63 bps (+11.5% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.7 bps (+0.43% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.12 bps (-0.88% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.49 bps (+11.19% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.49 bps (+2.2% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 49.55 bps (+11.32% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.82 bps (+9.68% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 50.05 bps (+12.45% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.85 bps (-1.48% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.68 bps (+2.63% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 44.78 bps (+0.61% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 43.76 bps (-1.69% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk,cal,lag] 2y refit7 hl20: MAE 44.99 bps (+1.08% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.66 → 63.37 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 44.73 bps (+0.49% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 53.63 vs 54.27 bps, p = 0.095, passed |
| L18 | submit | accepted |

# Weekly model review: 2024-07-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.59 bps vs 54.54 bps in the prior 26 weeks (-23.74%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 40.9 bps vs the champion's 41.59 bps (-1.66%). (L13)
- On the hidden window it scored 72.12 bps vs the champion's 70.95 bps (p = 0.872) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.0, last 26w 41.59, prior 26w 54.54 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.98 bps (+10.56% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.6 bps (+0.02% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 40.96 bps (-1.51% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.95 bps (+15.29% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.58 bps (-0.02% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.38 bps (+11.52% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.65 bps (+16.98% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.55 bps (+11.93% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.91 bps (+0.77% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.6 bps (+2.43% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.11 bps (-1.15% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.9 bps (-1.66% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 40.97 bps (-1.49% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 63.44 → 62.35 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 42.16 bps (+1.37% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 72.12 vs 70.95 bps, p = 0.872, failed |
| L18 | submit | accepted |

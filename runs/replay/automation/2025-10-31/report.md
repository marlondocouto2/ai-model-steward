# Weekly model review: 2025-10-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.98 bps vs 56.29 bps in the prior 26 weeks (-2.33%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 53.81 bps vs the champion's 54.98 bps (-2.13%). (L04)
- On the hidden window it scored 41.47 bps vs the champion's 41.27 bps (p = 0.595) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 38.1, last 26w 54.98, prior 26w 56.29 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.47 bps (+6.35% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 55.64 bps (+1.2% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.81 bps (-2.13% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.23 bps (+15.01% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 56.3 bps (+2.4% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 59.34 bps (+7.93% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 64.8 bps (+17.86% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.33 bps (+7.91% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 55.06 bps (+0.15% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 55.22 bps (+0.44% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 54.04 bps (-1.71% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.87 bps (-2.02% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 53.81 bps (-2.13% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.93 → 54.6 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 55.21 bps (+0.42% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 41.47 vs 41.27 bps, p = 0.595, failed |
| L18 | submit | accepted |

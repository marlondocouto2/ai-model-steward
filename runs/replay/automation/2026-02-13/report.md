# Weekly model review: 2026-02-13

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 43.11 bps vs 61.22 bps in the prior 26 weeks (-29.58%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.25 bps vs the champion's 43.11 bps (-1.99%). (L04)
- On the hidden window it scored 46.44 bps vs the champion's 46.05 bps (p = 0.836) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.73, last 26w 43.11, prior 26w 61.22 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.17 bps (+4.78% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.74 bps (-0.86% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.25 bps (-1.99% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.46 bps (+14.73% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.24 bps (+0.3% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.95 bps (+4.27% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.81 bps (+17.86% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.74 bps (+6.1% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.37 bps (+0.6% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.34 bps (+0.53% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 42.71 bps (-0.93% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 42.28 bps (-1.93% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 42.72 bps (-0.9% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.83 → 53.38 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.93 bps (-0.42% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 46.44 vs 46.05 bps, p = 0.836, failed |
| L18 | submit | accepted |

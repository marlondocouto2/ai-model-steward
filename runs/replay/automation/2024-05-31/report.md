# Weekly model review: 2024-05-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 39.84 bps vs 54.4 bps in the prior 26 weeks (-26.76%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 39.33 bps vs the champion's 39.84 bps (-1.28%). (L13)
- On the hidden window it scored 51.77 bps vs the champion's 52.15 bps (p = 0.264) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 35.36, last 26w 39.84, prior 26w 54.4 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.94 bps (+12.8% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 40.36 bps (+1.31% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 39.62 bps (-0.55% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 44.9 bps (+12.7% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 40.56 bps (+1.81% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.12 bps (+10.74% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 44.33 bps (+11.27% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.9 bps (+12.7% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 39.89 bps (+0.13% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.66 bps (+4.57% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 39.68 bps (-0.4% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 39.33 bps (-1.28% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 39.38 bps (-1.15% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.05 → 62.63 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 39.99 bps (+0.38% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 51.77 vs 52.15 bps, p = 0.264, failed |
| L18 | submit | accepted |

# Weekly model review: 2024-03-29

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 51.9 bps vs 54.28 bps in the prior 26 weeks (-4.38%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 51.24 bps vs the champion's 51.9 bps (-1.27%). (L04)
- On the hidden window it scored 26.71 bps vs the champion's 27.35 bps (p = 0.093) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.08, last 26w 51.9, prior 26w 54.28 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 55.59 bps (+7.11% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.84 bps (-0.12% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 51.24 bps (-1.27% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 58.16 bps (+12.06% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 53.16 bps (+2.43% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.51 bps (+10.81% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 57.5 bps (+10.79% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 58.52 bps (+12.76% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.6 bps (-0.58% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.17 bps (+2.45% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 51.74 bps (-0.31% vs champion) |
| L13 | backtest | lightgbm[fx,dxy,mk,cal] all refit7 hl20: MAE 51.6 bps (-0.58% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 52.02 bps (+0.23% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 66.7 → 66.06 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 51.99 bps (+0.17% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 26.71 vs 27.35 bps, p = 0.093, passed |
| L18 | submit | accepted |

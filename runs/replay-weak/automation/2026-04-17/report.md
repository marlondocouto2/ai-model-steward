# Weekly model review: 2026-04-17

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.52 bps vs 62.34 bps in the prior 26 weeks (-28.59%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5, scored 40.7 bps vs the champion's 44.52 bps (-8.58%). (L14)
- On the hidden window it scored 71.58 bps vs the champion's 73.76 bps (p = 0.272) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 51.04, last 26w 44.52, prior 26w 62.34 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.58 bps (+0.13% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.11 bps (-7.66% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.32 bps (-7.19% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 46.73 bps (+4.96% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.23 bps (-5.14% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.6 bps (+0.18% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 46.99 bps (+5.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 44.69 bps (+0.38% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.35 bps (-7.12% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.11 bps (-5.41% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 40.82 bps (-8.31% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 44.13 bps (-0.88% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 40.7 bps (-8.58% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk,lag] tuned 3y refit30 hl5: CV MAE 53.41 → 52.09 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk,lag] tuned 3y refit30 hl5: MAE 41.02 bps (-7.86% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: 71.58 vs 73.76 bps, p = 0.272, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-11-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.05 bps vs 55.35 bps in the prior 26 weeks (-2.35%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 52.71 bps vs the champion's 54.05 bps (-2.48%). (L04)
- On the hidden window it scored 39.27 bps vs the champion's 39.07 bps (p = 0.604) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.54, last 26w 54.05, prior 26w 55.35 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.97 bps (+7.25% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.53 bps (+0.89% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.71 bps (-2.48% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.38 bps (+15.41% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.68 bps (+1.17% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 58.13 bps (+7.55% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.97 bps (+18.35% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 58.3 bps (+7.86% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.15 bps (+0.19% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.12 bps (+0.13% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 52.96 bps (-2.02% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.8 bps (-2.31% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.81 bps (-2.29% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.74 → 54.72 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 54.15 bps (+0.19% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 39.27 vs 39.07 bps, p = 0.604, failed |
| L18 | submit | accepted |

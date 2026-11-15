# Weekly model review: 2024-04-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.4 bps vs 52.25 bps in the prior 26 weeks (-3.54%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5, scored 49.38 bps vs the champion's 50.4 bps (-2.02%). (L14)
- On the hidden window it scored 33.77 bps vs the champion's 34.07 bps (p = 0.389) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 33.93, last 26w 50.4, prior 26w 52.25 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 53.96 bps (+7.06% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 50.02 bps (-0.75% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 49.81 bps (-1.17% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.33 bps (+13.75% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 51.54 bps (+2.26% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 54.53 bps (+8.19% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.54 bps (+12.18% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 56.56 bps (+12.22% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.14 bps (-0.52% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.49 bps (+2.16% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.12 bps (-0.56% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 50.41 bps (+0.02% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 49.38 bps (-2.02% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: CV MAE 65.96 → 65.26 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: MAE 50.26 bps (-0.28% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: 33.77 vs 34.07 bps, p = 0.389, failed |
| L18 | submit | accepted |

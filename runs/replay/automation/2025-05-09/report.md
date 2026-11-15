# Weekly model review: 2025-05-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.23 bps vs 61.99 bps in the prior 26 weeks (-12.52%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 53.43 bps vs the champion's 54.23 bps (-1.48%). (L16)
- On the hidden window it scored 73.65 bps vs the champion's 74.32 bps (p = 0.35) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.54, last 26w 54.23, prior 26w 61.99 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.49 bps (+7.86% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 56.5 bps (+4.19% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 54.77 bps (+1.0% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 60.88 bps (+12.26% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 58.63 bps (+8.11% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 59.97 bps (+10.58% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.83 bps (+10.33% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 58.33 bps (+7.56% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 55.13 bps (+1.66% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.42 bps (+5.88% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 54.53 bps (+0.55% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 54.66 bps (+0.79% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 54.69 bps (+0.85% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.6 → 55.25 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 53.43 bps (-1.48% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 73.65 vs 74.32 bps, p = 0.35, failed |
| L18 | submit | accepted |

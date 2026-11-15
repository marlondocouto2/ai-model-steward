# Weekly model review: 2026-02-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.97 bps vs 60.99 bps in the prior 26 weeks (-29.55%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.0 bps vs the champion's 42.97 bps (-2.26%). (L04)
- On the hidden window it scored 48.91 bps vs the champion's 48.23 bps (p = 0.95) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 39.93, last 26w 42.97, prior 26w 60.99 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.12 bps (+5.0% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.33 bps (-1.49% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.0 bps (-2.26% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.46 bps (+15.1% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.09 bps (+0.28% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 44.53 bps (+3.63% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.84 bps (+18.32% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.31 bps (+7.77% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.28 bps (+0.72% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.05 bps (+0.19% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 42.34 bps (-1.47% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 42.25 bps (-1.68% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 44.71 bps (+4.05% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.66 → 53.1 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.77 bps (-0.47% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 48.91 vs 48.23 bps, p = 0.95, failed |
| L18 | submit | accepted |

# Weekly model review: 2026-05-08

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.23 bps vs 54.48 bps in the prior 26 weeks (-15.14%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 46.06 bps vs the champion's 46.23 bps (-0.37%). (L14)
- On the hidden window it scored 54.68 bps vs the champion's 54.25 bps (p = 0.823) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 68.71, last 26w 46.23, prior 26w 54.48 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 51.13 bps (+10.6% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 46.57 bps (+0.74% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 46.5 bps (+0.58% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 53.15 bps (+14.97% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 47.36 bps (+2.44% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 49.69 bps (+7.48% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.52 bps (+13.61% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 50.0 bps (+8.15% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 46.81 bps (+1.25% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 47.27 bps (+2.25% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 46.24 bps (+0.02% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 46.7 bps (+1.02% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 46.06 bps (-0.37% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 53.56 → 52.62 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 46.37 bps (+0.3% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 54.68 vs 54.25 bps, p = 0.823, failed |
| L18 | submit | accepted |

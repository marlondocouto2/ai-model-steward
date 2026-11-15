# Weekly model review: 2025-05-30

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.79 bps vs 62.6 bps in the prior 26 weeks (-9.28%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 56.41 bps vs the champion's 56.79 bps (-0.67%). (L16)
- On the hidden window it scored 62.39 bps vs the champion's 63.18 bps (p = 0.308) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 60.69, last 26w 56.79, prior 26w 62.6 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 61.49 bps (+8.28% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 59.17 bps (+4.19% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 56.95 bps (+0.28% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.62 bps (+10.27% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 60.27 bps (+6.13% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.2 bps (+9.53% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 61.75 bps (+8.73% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.03 bps (+7.47% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.64 bps (+1.5% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.17 bps (+5.95% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.0 bps (+0.37% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 56.99 bps (+0.35% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 56.84 bps (+0.09% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 57.49 → 55.53 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 56.41 bps (-0.67% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 62.39 vs 63.18 bps, p = 0.308, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-10-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.73 bps vs 55.82 bps in the prior 26 weeks (+1.63%). (L01)
- The best development candidate, xgboost[fx,mk,cal] all refit7 hl20, scored 55.7 bps vs the champion's 56.73 bps (-1.82%). (L14)
- On the hidden window it scored 40.64 bps vs the champion's 40.18 bps (p = 0.687) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.45, last 26w 56.73, prior 26w 55.82 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 60.37 bps (+6.42% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 57.8 bps (+1.89% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.74 bps (-1.75% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.74 bps (+15.88% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.86 bps (+1.99% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.24 bps (+7.95% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 67.2 bps (+18.46% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 60.74 bps (+7.07% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 56.98 bps (+0.44% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 57.46 bps (+1.29% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 55.87 bps (-1.52% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 55.71 bps (-1.8% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 55.7 bps (-1.82% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 56.65 → 54.84 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 56.94 bps (+0.37% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] all refit7 hl20: 40.64 vs 40.18 bps, p = 0.687, failed |
| L18 | submit | accepted |

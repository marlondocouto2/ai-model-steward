# Weekly model review: 2025-03-07

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 58.43 bps vs 50.3 bps in the prior 26 weeks (+16.16%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 57.68 bps vs the champion's 58.43 bps (-1.28%). (L16)
- On the hidden window it scored 54.79 bps vs the champion's 54.6 bps (p = 0.616) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 65.41, last 26w 58.43, prior 26w 50.3 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.11 bps (+9.72% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.45 bps (+6.88% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 58.91 bps (+0.82% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 64.93 bps (+11.12% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.32 bps (+8.37% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 64.13 bps (+9.76% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 64.78 bps (+10.87% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.41 bps (+10.23% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 59.34 bps (+1.56% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 62.52 bps (+7.0% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 58.92 bps (+0.84% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 58.81 bps (+0.65% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 58.47 bps (+0.07% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 59.72 → 57.18 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 57.68 bps (-1.28% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 54.79 vs 54.6 bps, p = 0.616, failed |
| L18 | submit | accepted |

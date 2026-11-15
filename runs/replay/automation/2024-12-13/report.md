# Weekly model review: 2024-12-13

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.67 bps vs 41.33 bps in the prior 26 weeks (+49.21%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 61.46 bps vs the champion's 61.67 bps (-0.34%). (L16)
- On the hidden window it scored 51.97 bps vs the champion's 52.32 bps (p = 0.349) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.63, last 26w 61.67, prior 26w 41.33 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 66.56 bps (+7.93% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.86 bps (+3.55% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.26 bps (+0.96% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 69.25 bps (+12.29% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.64 bps (+3.19% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.43 bps (+9.34% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 71.35 bps (+15.7% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 67.41 bps (+9.31% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 62.62 bps (+1.54% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.95 bps (+5.32% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.31 bps (+1.04% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.28 bps (+0.99% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 62.03 bps (+0.58% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 62.12 → 59.7 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 61.46 bps (-0.34% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 51.97 vs 52.32 bps, p = 0.349, failed |
| L18 | submit | accepted |

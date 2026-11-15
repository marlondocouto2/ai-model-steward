# Weekly model review: 2025-02-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.32 bps vs 49.78 bps in the prior 26 weeks (+15.15%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] tuned all refit7 hl20, scored 56.75 bps vs the champion's 57.32 bps (-0.99%). (L16)
- On the hidden window it scored 56.48 bps vs the champion's 56.75 bps (p = 0.399) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 52.82, last 26w 57.32, prior 26w 49.78 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.61 bps (+9.23% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.55 bps (+7.38% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.91 bps (+1.03% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.92 bps (+9.77% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.03 bps (+6.47% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.2 bps (+8.51% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.51 bps (+10.8% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.99 bps (+9.89% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.97 bps (+1.13% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.28 bps (+6.91% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.9 bps (+1.01% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 57.77 bps (+0.79% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 58.46 bps (+1.99% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 59.52 → 57.19 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 56.75 bps (-0.99% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: 56.48 vs 56.75 bps, p = 0.399, failed |
| L18 | submit | accepted |

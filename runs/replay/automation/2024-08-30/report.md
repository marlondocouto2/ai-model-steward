# Weekly model review: 2024-08-30

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.01 bps vs 53.32 bps in the prior 26 weeks (-8.08%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit30 hl5, scored 48.22 bps vs the champion's 49.01 bps (-1.61%). (L12)
- On the hidden window it scored 71.99 bps vs the champion's 65.89 bps (p = 0.989) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 60.3, last 26w 49.01, prior 26w 53.32 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 53.86 bps (+9.9% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 48.27 bps (-1.51% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 48.49 bps (-1.06% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.73 bps (+13.71% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.34 bps (+0.67% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.35 bps (+12.94% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.79 bps (+15.87% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.52 bps (+11.24% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 49.67 bps (+1.35% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.63 bps (+3.31% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 48.22 bps (-1.61% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 52.69 bps (+7.51% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 48.45 bps (-1.14% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: CV MAE 63.41 → 61.47 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: MAE 49.02 bps (+0.02% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: 71.99 vs 65.89 bps, p = 0.989, failed |
| L18 | submit | accepted |

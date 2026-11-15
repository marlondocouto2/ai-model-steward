# Weekly model review: 2026-04-03

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.79 bps vs 56.21 bps in the prior 26 weeks (-23.87%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit30 hl5, scored 42.31 bps vs the champion's 42.79 bps (-1.12%). (L12)
- On the hidden window it scored 67.07 bps vs the champion's 64.99 bps (p = 0.922) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.34, last 26w 42.79, prior 26w 56.21 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.46 bps (+6.24% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.58 bps (-0.49% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.94 bps (+0.35% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.28 bps (+12.83% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.34 bps (+1.29% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.22 bps (+8.02% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 49.0 bps (+14.51% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.06 bps (+7.64% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.05 bps (+0.61% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.32 bps (+1.24% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 42.31 bps (-1.12% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 45.26 bps (+5.77% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 42.36 bps (-1.0% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: CV MAE 53.82 → 52.1 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit30 hl5: MAE 42.55 bps (-0.56% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: 67.07 vs 64.99 bps, p = 0.922, failed |
| L18 | submit | accepted |

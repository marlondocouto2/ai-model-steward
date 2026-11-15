# Weekly model review: 2026-04-10

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.64 bps vs 55.92 bps in the prior 26 weeks (-23.75%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5, scored 42.09 bps vs the champion's 42.64 bps (-1.29%). (L14)
- On the hidden window it scored 68.18 bps vs the champion's 68.19 bps (p = 0.487) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 51.95, last 26w 42.64, prior 26w 55.92 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.69 bps (+7.15% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.41 bps (-0.54% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.79 bps (+0.35% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.07 bps (+12.73% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.41 bps (+1.81% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.66 bps (+7.08% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.58 bps (+13.93% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.63 bps (+7.01% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.91 bps (+0.63% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.2 bps (+1.31% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 42.11 bps (-1.24% vs champion) |
| L13 | backtest | ridge[fx,vol,dxy] 3y refit30 hl5: MAE 45.27 bps (+6.17% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: MAE 42.09 bps (-1.29% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk,lag] tuned 3y refit30 hl5: CV MAE 53.6 → 52.05 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk,lag] tuned 3y refit30 hl5: MAE 42.43 bps (-0.49% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk,lag] 3y refit30 hl5: 68.18 vs 68.19 bps, p = 0.487, failed |
| L18 | submit | accepted |

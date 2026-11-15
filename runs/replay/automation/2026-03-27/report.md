# Weekly model review: 2026-03-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.71 bps vs 55.98 bps in the prior 26 weeks (-23.7%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl20, scored 42.24 bps vs the champion's 42.71 bps (-1.1%). (L13)
- On the hidden window it scored 60.61 bps vs the champion's 61.58 bps (p = 0.1) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 49.27, last 26w 42.71, prior 26w 55.98 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 45.61 bps (+6.79% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.62 bps (-0.21% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.62 bps (-0.21% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.23 bps (+12.92% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.86 bps (+2.69% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.94 bps (+7.56% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.71 bps (+14.05% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.19 bps (+8.15% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 42.97 bps (+0.61% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 43.03 bps (+0.75% vs champion) |
| L12 | backtest | xgboost[fx,mk,cal,lag] 1y refit7 hl20: MAE 45.45 bps (+6.42% vs champion) |
| L13 | backtest | xgboost[mk,lag] all refit7 hl20: MAE 42.24 bps (-1.1% vs champion) |
| L14 | backtest | xgboost[lag] 1y refit7 hl20: MAE 46.82 bps (+9.62% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl20: CV MAE 52.77 → 51.82 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl20: MAE 42.77 bps (+0.14% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl20: 60.61 vs 61.58 bps, p = 0.1, failed |
| L18 | submit | accepted |

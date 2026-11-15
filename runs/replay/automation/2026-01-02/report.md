# Weekly model review: 2026-01-02

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 43.78 bps vs 63.1 bps in the prior 26 weeks (-30.62%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 42.91 bps vs the champion's 43.78 bps (-1.99%). (L04)
- On the hidden window it scored 40.71 bps vs the champion's 40.12 bps (p = 0.985) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 33.41, last 26w 43.78, prior 26w 63.1 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.25 bps (+5.64% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 43.46 bps (-0.73% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 42.91 bps (-1.99% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 49.37 bps (+12.77% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 44.76 bps (+2.24% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 45.55 bps (+4.04% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.79 bps (+16.01% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.91 bps (+7.15% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.76 bps (-0.05% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 44.21 bps (+0.98% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 43.33 bps (-1.03% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 43.09 bps (-1.58% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 43.45 bps (-0.75% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 55.13 → 53.85 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 43.49 bps (-0.66% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 40.71 vs 40.12 bps, p = 0.985, failed |
| L18 | submit | accepted |

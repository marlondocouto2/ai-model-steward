# Weekly model review: 2025-08-29

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.47 bps vs 57.75 bps in the prior 26 weeks (+2.98%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 59.23 bps vs the champion's 59.47 bps (-0.4%). (L16)
- On the hidden window it scored 47.9 bps vs the champion's 46.83 bps (p = 0.952) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 48.56, last 26w 59.47, prior 26w 57.75 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.52 bps (+5.13% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 60.71 bps (+2.09% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 59.5 bps (+0.05% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.66 bps (+12.09% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 60.89 bps (+2.39% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 64.62 bps (+8.66% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 67.65 bps (+13.75% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.65 bps (+5.35% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.49 bps (+1.72% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.41 bps (+1.58% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 59.43 bps (-0.07% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 59.63 bps (+0.27% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 59.8 bps (+0.55% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.19 → 54.46 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 59.23 bps (-0.4% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 47.9 vs 46.83 bps, p = 0.952, failed |
| L18 | submit | accepted |

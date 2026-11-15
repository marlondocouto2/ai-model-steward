# Weekly model review: 2026-05-29

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.11 bps vs 50.45 bps in the prior 26 weeks (-0.67%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 49.75 bps vs the champion's 50.11 bps (-0.72%). (L14)
- On the hidden window it scored 47.33 bps vs the champion's 47.54 bps (p = 0.318) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 81.66, last 26w 50.11, prior 26w 50.45 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.27 bps (+8.3% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 50.91 bps (+1.6% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.45 bps (+0.68% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.71 bps (+11.18% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 51.1 bps (+1.98% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 52.62 bps (+5.01% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 55.45 bps (+10.66% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 53.13 bps (+6.03% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.13 bps (+2.04% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.13 bps (+2.04% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.21 bps (+0.2% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 50.65 bps (+1.08% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 49.75 bps (-0.72% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.32 → 53.73 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 50.54 bps (+0.86% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 47.33 vs 47.54 bps, p = 0.318, failed |
| L18 | submit | accepted |

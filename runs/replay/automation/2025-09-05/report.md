# Weekly model review: 2025-09-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 58.68 bps vs 58.77 bps in the prior 26 weeks (-0.15%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 58.35 bps vs the champion's 58.68 bps (-0.56%). (L16)
- On the hidden window it scored 40.88 bps vs the champion's 40.28 bps (p = 0.873) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 52.02, last 26w 58.68, prior 26w 58.77 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 61.66 bps (+5.08% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 59.57 bps (+1.52% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 58.45 bps (-0.39% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 65.79 bps (+12.12% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 60.5 bps (+3.1% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 63.42 bps (+8.08% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 67.12 bps (+14.38% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.84 bps (+5.39% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 59.42 bps (+1.26% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 59.38 bps (+1.19% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 58.39 bps (-0.49% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 58.45 bps (-0.39% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 58.6 bps (-0.14% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 55.9 → 54.45 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 58.35 bps (-0.56% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 40.88 vs 40.28 bps, p = 0.873, failed |
| L18 | submit | accepted |

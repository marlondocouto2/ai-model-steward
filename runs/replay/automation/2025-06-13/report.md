# Weekly model review: 2025-06-13

**Decision: Switch.** Champion: `xgboost[fx,mk,lag] tuned all refit7 hl20` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.14 bps vs 61.25 bps in the prior 26 weeks (+3.09%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 62.87 bps vs the champion's 63.14 bps (-0.43%). (L16)
- On the hidden window it scored 43.61 bps vs the champion's 44.11 bps (p = 0.093) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 100.75, last 26w 63.14, prior 26w 61.25 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.77 bps (+7.33% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.71 bps (+2.49% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.0 bps (-0.22% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 71.76 bps (+13.65% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 65.8 bps (+4.21% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.97 bps (+10.82% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.07 bps (+10.98% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.05 bps (+7.78% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.67 bps (+0.84% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 64.71 bps (+2.49% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.0 bps (-0.22% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.09 bps (-0.08% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.49 bps (+0.55% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 58.67 → 56.3 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 62.87 bps (-0.43% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 43.61 vs 44.11 bps, p = 0.093, passed |
| L18 | submit | accepted |

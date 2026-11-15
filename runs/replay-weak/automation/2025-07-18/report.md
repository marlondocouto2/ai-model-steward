# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 67.67 bps vs 66.06 bps in the prior 26 weeks (+2.44%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 62.72 bps vs the champion's 67.67 bps (-7.31%). (L12)
- On the hidden window it scored 45.43 bps vs the champion's 49.47 bps (p = 0.132) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 51.92, last 26w 67.67, prior 26w 66.06 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.03 bps (-0.95% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.27 bps (-5.02% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.87 bps (-7.09% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 70.84 bps (+4.68% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.65 bps (-4.46% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.83 bps (+3.19% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.85 bps (+4.7% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.3 bps (-2.02% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.42 bps (-6.28% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.87 bps (-5.62% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.72 bps (-7.31% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.0 bps (-6.9% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.14 bps (-6.69% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.61 → 55.37 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 62.8 bps (-7.2% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 45.43 vs 49.47 bps, p = 0.132, failed |
| L18 | submit | accepted |

# Weekly model review: 2026-06-12

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 54.15 bps vs 48.51 bps in the prior 26 weeks (+11.63%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 50.36 bps vs the champion's 54.15 bps (-7.0%). (L14)
- On the hidden window it scored 47.23 bps vs the champion's 49.84 bps (p = 0.108) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 57.63, last 26w 54.15, prior 26w 48.51 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.89 bps (+1.37% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.29 bps (-5.28% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.76 bps (-6.26% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.87 bps (+3.18% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 52.33 bps (-3.36% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 53.39 bps (-1.4% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 55.12 bps (+1.79% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.0 bps (-0.28% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.38 bps (-5.12% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.61 bps (-4.69% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.49 bps (-6.76% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 50.89 bps (-6.02% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 50.36 bps (-7.0% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.43 → 53.81 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 50.99 bps (-5.84% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 47.23 vs 49.84 bps, p = 0.108, failed |
| L18 | submit | accepted |

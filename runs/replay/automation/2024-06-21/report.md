# Weekly model review: 2024-06-21

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.56 bps vs 54.91 bps in the prior 26 weeks (-24.31%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] all refit7 hl20, scored 40.92 bps vs the champion's 41.56 bps (-1.54%). (L13)
- On the hidden window it scored 62.17 bps vs the champion's 61.67 bps (p = 0.725) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 62.11, last 26w 41.56, prior 26w 54.91 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 46.43 bps (+11.72% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.83 bps (+0.65% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.04 bps (-1.25% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.61 bps (+14.56% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 42.05 bps (+1.18% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 46.62 bps (+12.18% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 47.93 bps (+15.33% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 46.7 bps (+12.37% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.73 bps (+0.41% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.7 bps (+2.74% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 40.94 bps (-1.49% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.92 bps (-1.54% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 42.27 bps (+1.71% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 64.91 → 63.28 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 41.99 bps (+1.03% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] all refit7 hl20: 62.17 vs 61.67 bps, p = 0.725, failed |
| L18 | submit | accepted |

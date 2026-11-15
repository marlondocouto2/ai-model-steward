# Weekly model review: 2024-10-25

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.24 bps vs 47.07 bps in the prior 26 weeks (+25.86%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 59.22 bps vs the champion's 59.24 bps (-0.03%). (L04)
- On the hidden window it scored 52.4 bps vs the champion's 51.5 bps (p = 0.793) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 75.83, last 26w 59.24, prior 26w 47.07 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.2 bps (+8.37% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 60.18 bps (+1.59% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 59.22 bps (-0.03% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.92 bps (+12.96% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.22 bps (+3.34% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.11 bps (+11.6% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 68.85 bps (+16.22% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.7 bps (+9.22% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 59.9 bps (+1.11% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 61.67 bps (+4.1% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 59.5 bps (+0.44% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 59.32 bps (+0.14% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 59.47 bps (+0.39% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 62.24 → 60.88 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 59.33 bps (+0.15% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 52.4 vs 51.5 bps, p = 0.793, failed |
| L18 | submit | accepted |

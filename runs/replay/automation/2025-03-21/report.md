# Weekly model review: 2025-03-21

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.85 bps vs 50.26 bps in the prior 26 weeks (+19.08%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] tuned all refit7 hl20, scored 59.36 bps vs the champion's 59.85 bps (-0.82%). (L16)
- On the hidden window it scored 54.17 bps vs the champion's 53.72 bps (p = 0.768) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 72.7, last 26w 59.85, prior 26w 50.26 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.3 bps (+9.11% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 63.38 bps (+5.9% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.53 bps (+1.14% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.18 bps (+10.58% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.09 bps (+5.41% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 65.22 bps (+8.97% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.67 bps (+9.72% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.62 bps (+11.31% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.99 bps (+1.9% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.49 bps (+6.08% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.51 bps (+1.1% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.39 bps (+0.9% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 61.43 bps (+2.64% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 59.22 → 57.45 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 59.36 bps (-0.82% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: 54.17 vs 53.72 bps, p = 0.768, failed |
| L18 | submit | accepted |

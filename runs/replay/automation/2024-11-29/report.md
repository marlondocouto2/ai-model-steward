# Weekly model review: 2024-11-29

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 62.9 bps vs 39.75 bps in the prior 26 weeks (+58.24%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 63.34 bps vs the champion's 62.9 bps (+0.7%). (L12)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 58.35, last 26w 62.9, prior 26w 39.75 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.98 bps (+8.08% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.07 bps (+1.86% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.38 bps (+0.76% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 72.18 bps (+14.75% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 65.33 bps (+3.86% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 70.34 bps (+11.83% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 73.98 bps (+17.62% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 69.46 bps (+10.43% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.92 bps (+1.62% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.05 bps (+3.42% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.34 bps (+0.7% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.5 bps (+0.95% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 64.15 bps (+1.99% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 61.34 → 59.63 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 63.44 bps (+0.86% vs champion) |
| L17 | submit | accepted |

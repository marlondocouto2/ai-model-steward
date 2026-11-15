# Weekly model review: 2026-07-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.66 bps vs 43.31 bps in the prior 26 weeks (+21.59%). (L01)
- The best development candidate, xgboost[vol,mk,lag] all refit7 hl20, scored 52.99 bps vs the champion's 52.66 bps (+0.63%). (L14)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.45, last 26w 52.66, prior 26w 43.31 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.05 bps (+10.24% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.7 bps (+1.97% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.07 bps (+0.78% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.57 bps (+9.32% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.63 bps (+3.74% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 56.73 bps (+7.73% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.72 bps (+7.71% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.15 bps (+8.53% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.01 bps (+0.66% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.12 bps (+2.77% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 53.77 bps (+2.11% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.21 bps (+1.04% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 52.99 bps (+0.63% vs champion) |
| L15 | tune | xgboost[vol,mk,lag] tuned all refit7 hl20: CV MAE 56.43 → 55.01 bps |
| L16 | backtest | xgboost[vol,mk,lag] tuned all refit7 hl20: MAE 54.24 bps (+3.0% vs champion) |
| L17 | submit | accepted |

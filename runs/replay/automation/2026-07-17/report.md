# Weekly model review: 2026-07-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.98 bps vs 42.71 bps in the prior 26 weeks (+24.05%). (L01)
- The best development candidate, lightgbm[fx,dxy,mk] all refit7 hl20, scored 53.23 bps vs the champion's 52.98 bps (+0.47%). (L10)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 51.77, last 26w 52.98, prior 26w 42.71 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.59 bps (+8.7% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.86 bps (+1.66% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.36 bps (+0.72% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.64 bps (+8.8% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.97 bps (+3.76% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 56.37 bps (+6.4% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.67 bps (+6.96% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.0 bps (+7.59% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.23 bps (+0.47% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.15 bps (+2.21% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 54.13 bps (+2.17% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.52 bps (+1.02% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 53.26 bps (+0.53% vs champion) |
| L15 | tune | lightgbm[fx,dxy,mk] tuned all refit7 hl20: CV MAE 55.31 → 54.56 bps |
| L16 | backtest | lightgbm[fx,dxy,mk] tuned all refit7 hl20: MAE 53.75 bps (+1.45% vs champion) |
| L17 | submit | accepted |

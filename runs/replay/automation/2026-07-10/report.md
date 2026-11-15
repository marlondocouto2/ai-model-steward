# Weekly model review: 2026-07-10

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 51.75 bps vs 43.44 bps in the prior 26 weeks (+19.13%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 51.6 bps vs the champion's 51.75 bps (-0.29%). (L12)
- On the hidden window it scored 50.51 bps vs the champion's 50.32 bps (p = 0.615) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 41.66, last 26w 51.75, prior 26w 43.44 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.4 bps (+8.99% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 52.88 bps (+2.18% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 51.91 bps (+0.31% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 56.91 bps (+9.97% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.07 bps (+4.48% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.4 bps (+7.05% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.22 bps (+8.64% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.84 bps (+7.9% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 52.32 bps (+1.1% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.09 bps (+2.59% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 51.6 bps (-0.29% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.0 bps (+0.48% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 51.63 bps (-0.23% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 55.12 → 54.28 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 52.12 bps (+0.71% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 50.51 vs 50.32 bps, p = 0.615, failed |
| L18 | submit | accepted |

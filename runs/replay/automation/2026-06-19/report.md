# Weekly model review: 2026-06-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.9 bps vs 44.77 bps in the prior 26 weeks (+13.69%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 50.72 bps vs the champion's 50.9 bps (-0.35%). (L14)
- On the hidden window it scored 49.4 bps vs the champion's 49.84 bps (p = 0.201) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.79, last 26w 50.9, prior 26w 44.77 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 55.19 bps (+8.43% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.73 bps (+1.63% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 51.14 bps (+0.47% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 56.38 bps (+10.77% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 52.36 bps (+2.87% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 53.56 bps (+5.23% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 55.53 bps (+9.1% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.69 bps (+7.45% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.64 bps (+1.45% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.98 bps (+2.12% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.85 bps (-0.1% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 51.23 bps (+0.65% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 50.72 bps (-0.35% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.28 → 53.67 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 51.34 bps (+0.86% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 49.4 vs 49.84 bps, p = 0.201, failed |
| L18 | submit | accepted |

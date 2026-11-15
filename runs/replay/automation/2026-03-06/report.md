# Weekly model review: 2026-03-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 41.26 bps vs 59.23 bps in the prior 26 weeks (-30.34%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 40.92 bps vs the champion's 41.26 bps (-0.82%). (L04)
- On the hidden window it scored 51.51 bps vs the champion's 51.16 bps (p = 0.782) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.14, last 26w 41.26, prior 26w 59.23 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 43.64 bps (+5.77% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 41.34 bps (+0.19% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 40.92 bps (-0.82% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 47.53 bps (+15.2% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 41.85 bps (+1.43% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.88 bps (+6.35% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 48.4 bps (+17.3% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.04 bps (+9.16% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 41.61 bps (+0.85% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 41.45 bps (+0.46% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 41.21 bps (-0.12% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 40.95 bps (-0.75% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 41.3 bps (+0.1% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 53.2 → 52.1 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 41.05 bps (-0.51% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 51.51 vs 51.16 bps, p = 0.782, failed |
| L18 | submit | accepted |

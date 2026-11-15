# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.06 bps vs 61.91 bps in the prior 26 weeks (+1.86%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl10, scored 62.72 bps vs the champion's 63.06 bps (-0.54%). (L12)
- On the hidden window it scored 45.43 bps vs the champion's 46.14 bps (p = 0.117) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 49.9, last 26w 63.06, prior 26w 61.91 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.03 bps (+6.3% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.27 bps (+1.92% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 62.87 bps (-0.3% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 70.84 bps (+12.34% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.65 bps (+2.52% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 69.83 bps (+10.74% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.85 bps (+12.35% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.3 bps (+5.14% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.42 bps (+0.57% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 63.87 bps (+1.28% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.72 bps (-0.54% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.0 bps (-0.1% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 63.14 bps (+0.13% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.61 → 55.37 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 62.8 bps (-0.41% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl10: 45.43 vs 46.14 bps, p = 0.117, failed |
| L18 | submit | accepted |

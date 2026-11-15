# Weekly model review: 2026-06-05

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 49.72 bps vs 46.82 bps in the prior 26 weeks (+6.19%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 49.46 bps vs the champion's 49.72 bps (-0.52%). (L14)
- On the hidden window it scored 42.61 bps vs the champion's 42.67 bps (p = 0.459) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 64.62, last 26w 49.72, prior 26w 46.82 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.11 bps (+8.83% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 50.52 bps (+1.61% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.13 bps (+0.82% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.45 bps (+11.52% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 51.06 bps (+2.7% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 52.67 bps (+5.93% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 55.04 bps (+10.7% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 53.33 bps (+7.26% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.69 bps (+1.95% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 50.69 bps (+1.95% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 49.91 bps (+0.38% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 50.27 bps (+1.11% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 49.46 bps (-0.52% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.34 → 53.74 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 50.11 bps (+0.78% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 42.61 vs 42.67 bps, p = 0.459, failed |
| L18 | submit | accepted |

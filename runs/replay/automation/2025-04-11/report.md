# Weekly model review: 2025-04-11

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.06 bps vs 55.83 bps in the prior 26 weeks (+2.2%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 56.18 bps vs the champion's 57.06 bps (-1.54%). (L16)
- On the hidden window it scored 69.82 bps vs the champion's 68.04 bps (p = 0.944) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 55.52, last 26w 57.06, prior 26w 55.83 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 61.59 bps (+7.94% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 60.19 bps (+5.49% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.69 bps (+1.1% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.76 bps (+11.74% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 61.41 bps (+7.62% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.06 bps (+8.76% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.02 bps (+10.45% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.23 bps (+9.06% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 58.42 bps (+2.38% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 59.46 bps (+4.21% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 57.44 bps (+0.67% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 57.75 bps (+1.21% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 57.9 bps (+1.47% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 57.38 → 56.08 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 56.18 bps (-1.54% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 69.82 vs 68.04 bps, p = 0.944, failed |
| L18 | submit | accepted |

# Weekly model review: 2025-02-21

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.14 bps vs 49.17 bps in the prior 26 weeks (+16.21%). (L01)
- The best development candidate, ridge[fx,dxy,mk] tuned all refit7 hl20, scored 56.57 bps vs the champion's 57.14 bps (-1.0%). (L16)
- On the hidden window it scored 61.38 bps vs the champion's 60.12 bps (p = 0.954) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.28, last 26w 57.14, prior 26w 49.17 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.4 bps (+9.21% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.09 bps (+6.91% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.91 bps (+1.35% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.97 bps (+10.2% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 59.73 bps (+4.53% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.22 bps (+8.89% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.31 bps (+10.8% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.44 bps (+9.28% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.8 bps (+1.16% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.87 bps (+6.53% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 57.14 bps (+0.0% vs champion) |
| L13 | backtest | ridge[fx,dxy,mk,cal] all refit7 hl20: MAE 57.29 bps (+0.26% vs champion) |
| L14 | backtest | ridge[fx,mk,cal] all refit7 hl20: MAE 57.26 bps (+0.21% vs champion) |
| L15 | tune | ridge[fx,dxy,mk] tuned all refit7 hl20: CV MAE 59.65 → 57.15 bps |
| L16 | backtest | ridge[fx,dxy,mk] tuned all refit7 hl20: MAE 56.57 bps (-1.0% vs champion) |
| L17 | promote | ridge[fx,dxy,mk] tuned all refit7 hl20: 61.38 vs 60.12 bps, p = 0.954, failed |
| L18 | submit | accepted |

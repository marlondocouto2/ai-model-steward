# Weekly model review: 2025-02-21

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.57 bps vs 54.4 bps in the prior 26 weeks (+11.34%). (L01)
- The best development candidate, ridge[fx,dxy,mk] tuned all refit7 hl20, scored 56.57 bps vs the champion's 60.57 bps (-6.6%). (L16)
- On the hidden window it scored 61.38 bps vs the champion's 65.06 bps (p = 0.112) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.28, last 26w 60.57, prior 26w 54.4 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.4 bps (+3.02% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.09 bps (+0.86% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 57.91 bps (-4.39% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.97 bps (+3.96% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 59.73 bps (-1.39% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.22 bps (+2.72% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.31 bps (+4.52% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.44 bps (+3.09% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.8 bps (-4.57% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.87 bps (+0.5% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 57.14 bps (-5.66% vs champion) |
| L13 | backtest | ridge[fx,dxy,mk,cal] all refit7 hl20: MAE 57.29 bps (-5.42% vs champion) |
| L14 | backtest | ridge[fx,mk,cal] all refit7 hl20: MAE 57.26 bps (-5.46% vs champion) |
| L15 | tune | ridge[fx,dxy,mk] tuned all refit7 hl20: CV MAE 59.65 → 57.15 bps |
| L16 | backtest | ridge[fx,dxy,mk] tuned all refit7 hl20: MAE 56.57 bps (-6.6% vs champion) |
| L17 | promote | ridge[fx,dxy,mk] tuned all refit7 hl20: 61.38 vs 65.06 bps, p = 0.112, failed |
| L18 | submit | accepted |

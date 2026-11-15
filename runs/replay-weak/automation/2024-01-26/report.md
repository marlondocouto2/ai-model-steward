# Weekly model review: 2024-01-26

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.51 bps vs 68.69 bps in the prior 26 weeks (-17.73%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5, scored 51.59 bps vs the champion's 56.51 bps (-8.71%). (L16)
- On the hidden window it scored 47.84 bps vs the champion's 49.96 bps (p = 0.139) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 32.71, last 26w 56.51, prior 26w 68.69 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.15 bps (-0.64% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.92 bps (-8.12% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.21 bps (-7.61% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 58.65 bps (+3.79% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.53 bps (-3.5% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.47 bps (+1.7% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 59.55 bps (+5.38% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 59.13 bps (+4.64% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.0 bps (-6.21% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.27 bps (-5.73% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 52.26 bps (-7.52% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 51.92 bps (-8.12% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit7 hl5: MAE 55.78 bps (-1.29% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 68.6 → 67.44 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 51.59 bps (-8.71% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: 47.84 vs 49.96 bps, p = 0.139, failed |
| L18 | submit | accepted |

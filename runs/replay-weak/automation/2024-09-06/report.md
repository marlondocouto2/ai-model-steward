# Weekly model review: 2024-09-06

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 55.48 bps vs 57.27 bps in the prior 26 weeks (-3.13%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit7 hl5, scored 49.3 bps vs the champion's 55.48 bps (-11.14%). (L03)
- On the hidden window it scored 71.55 bps vs the champion's 66.32 bps (p = 0.844) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 70.44, last 26w 55.48, prior 26w 57.27 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 54.84 bps (-1.15% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 49.3 bps (-11.14% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 49.77 bps (-10.29% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.11 bps (+2.94% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 49.77 bps (-10.29% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 56.15 bps (+1.21% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 58.52 bps (+5.48% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 55.17 bps (-0.56% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 50.5 bps (-8.98% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.17 bps (-7.77% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 49.61 bps (-10.58% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 49.89 bps (-10.08% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit7 hl5: MAE 52.7 bps (-5.01% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 63.52 → 61.35 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 49.98 bps (-9.91% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: 71.55 vs 66.32 bps, p = 0.844, failed |
| L18 | submit | accepted |

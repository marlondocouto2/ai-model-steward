# Weekly model review: 2024-01-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.14 bps vs 62.06 bps in the prior 26 weeks (-9.54%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5, scored 54.77 bps vs the champion's 56.14 bps (-2.44%). (L13)
- On the hidden window it scored 37.7 bps vs the champion's 38.15 bps (p = 0.322) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 50.77, last 26w 56.14, prior 26w 62.06 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.3 bps (+3.85% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.78 bps (-2.42% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 55.31 bps (-1.48% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 61.8 bps (+10.08% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 57.18 bps (+1.85% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 60.19 bps (+7.21% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 62.76 bps (+11.79% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.32 bps (+11.01% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 55.85 bps (-0.52% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 55.84 bps (-0.53% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 55.19 bps (-1.69% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 54.77 bps (-2.44% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit7 hl5: MAE 56.59 bps (+0.8% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: CV MAE 68.93 → 67.91 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk,cal] tuned 2y refit7 hl5: MAE 55.49 bps (-1.16% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: 37.7 vs 38.15 bps, p = 0.322, failed |
| L18 | submit | accepted |

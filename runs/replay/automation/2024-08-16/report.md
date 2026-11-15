# Weekly model review: 2024-08-16

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.59 bps vs 54.39 bps in the prior 26 weeks (-14.34%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 46.19 bps vs the champion's 46.59 bps (-0.86%). (L04)
- On the hidden window it scored 65.64 bps vs the champion's 64.92 bps (p = 0.765) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 81.75, last 26w 46.59, prior 26w 54.39 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 51.94 bps (+11.48% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 46.24 bps (-0.75% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 46.19 bps (-0.86% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 53.49 bps (+14.81% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 47.4 bps (+1.74% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 53.15 bps (+14.08% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 53.76 bps (+15.39% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 52.35 bps (+12.36% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 47.23 bps (+1.37% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 48.84 bps (+4.83% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 46.29 bps (-0.64% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 46.71 bps (+0.26% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 46.56 bps (-0.06% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 62.62 → 61.38 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 46.72 bps (+0.28% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 65.64 vs 64.92 bps, p = 0.765, failed |
| L18 | submit | accepted |

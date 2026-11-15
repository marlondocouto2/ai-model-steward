# Weekly model review: 2025-11-21

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 53.85 bps vs 56.06 bps in the prior 26 weeks (-3.94%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 52.79 bps vs the champion's 53.85 bps (-1.97%). (L04)
- On the hidden window it scored 35.5 bps vs the champion's 34.72 bps (p = 0.851) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 46.33, last 26w 53.85, prior 26w 56.06 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 56.61 bps (+5.13% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 54.32 bps (+0.87% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.79 bps (-1.97% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 62.02 bps (+15.17% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.85 bps (+1.86% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 57.44 bps (+6.67% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 63.43 bps (+17.79% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.45 bps (+6.69% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 54.15 bps (+0.56% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.88 bps (+0.06% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 53.0 bps (-1.58% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.89 bps (-1.78% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 52.8 bps (-1.95% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 56.54 → 55.27 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 54.07 bps (+0.41% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 35.5 vs 34.72 bps, p = 0.851, failed |
| L18 | submit | accepted |

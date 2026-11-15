# Weekly model review: 2025-05-02

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.29 bps vs 59.27 bps in the prior 26 weeks (-5.03%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 55.48 bps vs the champion's 56.29 bps (-1.44%). (L16)
- On the hidden window it scored 75.58 bps vs the champion's 76.69 bps (p = 0.246) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 46.93, last 26w 56.29, prior 26w 59.27 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 60.37 bps (+7.25% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 58.0 bps (+3.04% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 56.8 bps (+0.91% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.12 bps (+12.13% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 59.87 bps (+6.36% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 61.66 bps (+9.54% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 62.22 bps (+10.53% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 61.03 bps (+8.42% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 57.33 bps (+1.85% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 58.59 bps (+4.09% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 56.46 bps (+0.3% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 56.72 bps (+0.76% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 56.46 bps (+0.3% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.61 → 55.32 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 55.48 bps (-1.44% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 75.58 vs 76.69 bps, p = 0.246, failed |
| L18 | submit | accepted |

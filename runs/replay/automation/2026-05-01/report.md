# Weekly model review: 2026-05-01

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 44.32 bps vs 55.03 bps in the prior 26 weeks (-19.46%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5, scored 44.27 bps vs the champion's 44.32 bps (-0.11%). (L16)
- On the hidden window it scored 64.0 bps vs the champion's 62.1 bps (p = 0.978) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 48.58, last 26w 44.32, prior 26w 55.03 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 48.32 bps (+9.03% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 44.35 bps (+0.07% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 44.62 bps (+0.68% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 50.13 bps (+13.11% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 45.1 bps (+1.76% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 47.16 bps (+6.41% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.23 bps (+13.33% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 48.15 bps (+8.64% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 44.35 bps (+0.07% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 45.29 bps (+2.19% vs champion) |
| L12 | backtest | lightgbm[fx,dxy,mk,cal] all refit7 hl20: MAE 44.59 bps (+0.61% vs champion) |
| L13 | backtest | ridge[fx,dxy] all refit7 hl10: MAE 46.73 bps (+5.44% vs champion) |
| L14 | backtest | lightgbm[fx,dxy,mk] 2y refit30 hl20: MAE 45.98 bps (+3.75% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 54.45 → 52.62 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 44.27 bps (-0.11% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: 64.0 vs 62.1 bps, p = 0.978, failed |
| L18 | submit | accepted |

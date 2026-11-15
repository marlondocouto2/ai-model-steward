# Weekly model review: 2024-11-22

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.12 bps vs 42.17 bps in the prior 26 weeks (+49.68%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 62.94 bps vs the champion's 63.12 bps (-0.29%). (L16)
- On the hidden window it scored 47.76 bps vs the champion's 49.21 bps (p = 0.047) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 57.04, last 26w 63.12, prior 26w 42.17 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 68.32 bps (+8.24% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.28 bps (+1.84% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.66 bps (+0.86% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 72.38 bps (+14.67% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.82 bps (+2.69% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 70.65 bps (+11.93% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 74.2 bps (+17.55% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 69.64 bps (+10.33% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 64.27 bps (+1.82% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.37 bps (+3.56% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.66 bps (+0.86% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 63.73 bps (+0.97% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 64.44 bps (+2.09% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 61.75 → 60.21 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 62.94 bps (-0.29% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 47.76 vs 49.21 bps, p = 0.047, failed |
| L18 | submit | accepted |

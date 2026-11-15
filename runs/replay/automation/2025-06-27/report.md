# Weekly model review: 2025-06-27

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 64.22 bps vs 59.19 bps in the prior 26 weeks (+8.5%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 63.7 bps vs the champion's 64.22 bps (-0.81%). (L16)
- On the hidden window it scored 47.32 bps vs the champion's 47.21 bps (p = 0.529) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 82.1, last 26w 64.22, prior 26w 59.19 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 68.04 bps (+5.95% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 65.8 bps (+2.46% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.88 bps (-0.53% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 72.53 bps (+12.94% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 66.16 bps (+3.02% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 71.32 bps (+11.06% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 71.4 bps (+11.18% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.14 bps (+6.1% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 64.97 bps (+1.17% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.15 bps (+1.45% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.88 bps (-0.53% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 64.0 bps (-0.34% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 64.29 bps (+0.11% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 57.9 → 56.3 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 63.7 bps (-0.81% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 47.32 vs 47.21 bps, p = 0.529, failed |
| L18 | submit | accepted |

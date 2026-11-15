# Weekly model review: 2025-06-20

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 63.94 bps vs 60.42 bps in the prior 26 weeks (+5.83%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 63.66 bps vs the champion's 63.94 bps (-0.44%). (L16)
- On the hidden window it scored 45.55 bps vs the champion's 45.82 bps (p = 0.32) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 99.57, last 26w 63.94, prior 26w 60.42 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.95 bps (+6.27% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 66.04 bps (+3.28% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.89 bps (-0.08% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 72.24 bps (+12.98% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 65.82 bps (+2.94% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 71.14 bps (+11.26% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 71.07 bps (+11.15% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.04 bps (+6.41% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 64.8 bps (+1.35% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.39 bps (+2.27% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.77 bps (-0.27% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 64.02 bps (+0.13% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 64.27 bps (+0.52% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 57.85 → 56.35 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 63.66 bps (-0.44% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 45.55 vs 45.82 bps, p = 0.32, failed |
| L18 | submit | accepted |

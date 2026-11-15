# Weekly model review: 2026-01-30

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 42.73 bps vs 60.59 bps in the prior 26 weeks (-29.48%). (L01)
- The best development candidate, xgboost[fx,mk,lag] all refit7 hl20, scored 41.84 bps vs the champion's 42.73 bps (-2.08%). (L04)
- On the hidden window it scored 46.64 bps vs the champion's 46.25 bps (p = 0.929) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 35.37, last 26w 42.73, prior 26w 60.59 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 44.35 bps (+3.79% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 42.16 bps (-1.33% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 41.84 bps (-2.08% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 48.72 bps (+14.02% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 43.1 bps (+0.87% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 43.27 bps (+1.26% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 50.11 bps (+17.27% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 45.79 bps (+7.16% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 43.0 bps (+0.63% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 42.88 bps (+0.35% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 42.22 bps (-1.19% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 42.16 bps (-1.33% vs champion) |
| L14 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 42.64 bps (-0.21% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl20: CV MAE 54.1 → 53.16 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 42.24 bps (-1.15% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] all refit7 hl20: 46.64 vs 46.25 bps, p = 0.929, failed |
| L18 | submit | accepted |

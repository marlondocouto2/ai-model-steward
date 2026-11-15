# Weekly model review: 2024-08-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is down compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 46.65 bps vs 53.77 bps in the prior 26 weeks (-13.24%). (L01)
- The best development candidate, xgboost[fx,vol,dxy,mk] 3y refit7 hl5, scored 46.2 bps vs the champion's 46.65 bps (-0.96%). (L03)
- On the hidden window it scored 67.85 bps vs the champion's 65.91 bps (p = 0.718) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 76.63, last 26w 46.65, prior 26w 53.77 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 52.12 bps (+11.73% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 46.2 bps (-0.96% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 46.26 bps (-0.84% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 52.44 bps (+12.41% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 47.44 bps (+1.69% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 52.26 bps (+12.03% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 52.95 bps (+13.5% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 52.03 bps (+11.53% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 47.42 bps (+1.65% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 48.29 bps (+3.52% vs champion) |
| L12 | backtest | xgboost[fx,vol,dxy,mk] 3y refit30 hl5: MAE 46.38 bps (-0.58% vs champion) |
| L13 | backtest | xgboost[fx,vol,dxy,mk,cal] 2y refit7 hl5: MAE 46.37 bps (-0.6% vs champion) |
| L14 | backtest | ridge[fx,vol,dxy] 3y refit7 hl5: MAE 50.9 bps (+9.11% vs champion) |
| L15 | tune | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: CV MAE 63.31 → 61.95 bps |
| L16 | backtest | xgboost[fx,vol,dxy,mk] tuned 3y refit7 hl5: MAE 46.34 bps (-0.66% vs champion) |
| L17 | promote | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: 67.85 vs 65.91 bps, p = 0.718, failed |
| L18 | submit | accepted |

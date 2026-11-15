# Weekly model review: 2025-03-28

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 59.63 bps vs 51.76 bps in the prior 26 weeks (+15.2%). (L01)
- The best development candidate, xgboost[fx,mk,cal,lag] tuned all refit7 hl20, scored 59.0 bps vs the champion's 59.63 bps (-1.06%). (L16)
- On the hidden window it scored 52.18 bps vs the champion's 51.48 bps (p = 0.922) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 70.04, last 26w 59.63, prior 26w 51.76 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.4 bps (+8.0% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.41 bps (+4.66% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 60.3 bps (+1.12% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 66.33 bps (+11.24% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.33 bps (+6.2% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 64.41 bps (+8.02% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 65.55 bps (+9.93% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 66.16 bps (+10.95% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 60.8 bps (+1.96% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 62.35 bps (+4.56% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 60.27 bps (+1.07% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 60.13 bps (+0.84% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal,lag] 3y refit7 hl10: MAE 60.76 bps (+1.9% vs champion) |
| L15 | tune | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: CV MAE 58.34 → 56.95 bps |
| L16 | backtest | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: MAE 59.0 bps (-1.06% vs champion) |
| L17 | promote | xgboost[fx,mk,cal,lag] tuned all refit7 hl20: 52.18 vs 51.48 bps, p = 0.922, failed |
| L18 | submit | accepted |

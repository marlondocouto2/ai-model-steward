# Weekly model review: 2026-07-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 56.37 bps vs 46.35 bps in the prior 26 weeks (+21.62%). (L01)
- The best development candidate, xgboost[vol,mk,lag] all refit7 hl20, scored 52.99 bps vs the champion's 56.37 bps (-6.0%). (L14)
- On the hidden window it scored 48.87 bps vs the champion's 50.69 bps (p = 0.171) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 53.97, last 26w 56.37, prior 26w 46.35 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 58.05 bps (+2.98% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.7 bps (-4.74% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 53.07 bps (-5.85% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.57 bps (+2.13% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.63 bps (-3.09% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 56.73 bps (+0.64% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.72 bps (+0.62% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 57.15 bps (+1.38% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 53.01 bps (-5.96% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 54.12 bps (-3.99% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 53.77 bps (-4.61% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 53.21 bps (-5.61% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 52.99 bps (-6.0% vs champion) |
| L15 | tune | xgboost[vol,mk,lag] tuned all refit7 hl20: CV MAE 56.43 → 55.01 bps |
| L16 | backtest | xgboost[vol,mk,lag] tuned all refit7 hl20: MAE 54.24 bps (-3.78% vs champion) |
| L17 | promote | xgboost[vol,mk,lag] all refit7 hl20: 48.87 vs 50.69 bps, p = 0.171, failed |
| L18 | submit | accepted |

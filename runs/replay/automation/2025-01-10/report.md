# Weekly model review: 2025-01-10

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 60.86 bps vs 41.06 bps in the prior 26 weeks (+48.22%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 60.58 bps vs the champion's 60.86 bps (-0.46%). (L16)
- On the hidden window it scored 60.7 bps vs the champion's 60.42 bps (p = 0.659) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.99, last 26w 60.86, prior 26w 41.06 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 65.9 bps (+8.28% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 64.55 bps (+6.06% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 61.92 bps (+1.74% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.22 bps (+12.09% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.28 bps (+5.62% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 67.21 bps (+10.43% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.04 bps (+15.08% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 67.3 bps (+10.58% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 62.2 bps (+2.2% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 65.35 bps (+7.38% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 62.0 bps (+1.87% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 61.8 bps (+1.54% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 61.5 bps (+1.05% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 61.71 → 58.5 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 60.58 bps (-0.46% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 60.7 vs 60.42 bps, p = 0.659, failed |
| L18 | submit | accepted |

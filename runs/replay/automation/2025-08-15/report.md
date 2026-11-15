# Weekly model review: 2025-08-15

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.23 bps vs 57.46 bps in the prior 26 weeks (+6.56%). (L01)
- The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl10, scored 61.0 bps vs the champion's 61.23 bps (-0.38%). (L16)
- On the hidden window it scored 47.83 bps vs the champion's 47.46 bps (p = 0.681) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 40.83, last 26w 61.23, prior 26w 57.46 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 64.1 bps (+4.69% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 62.67 bps (+2.35% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 61.21 bps (-0.03% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 68.54 bps (+11.94% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 63.6 bps (+3.87% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 66.86 bps (+9.19% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 68.66 bps (+12.13% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 64.34 bps (+5.08% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 61.79 bps (+0.91% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 62.1 bps (+1.42% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 61.07 bps (-0.26% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 61.38 bps (+0.24% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 61.53 bps (+0.49% vs champion) |
| L15 | tune | xgboost[fx,mk,lag] tuned all refit7 hl10: CV MAE 56.3 → 54.75 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl10: MAE 61.0 bps (-0.38% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl10: 47.83 vs 47.46 bps, p = 0.681, failed |
| L18 | submit | accepted |

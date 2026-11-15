# Weekly model review: 2025-01-17

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 66.33 bps vs 46.41 bps in the prior 26 weeks (+42.92%). (L01)
- The best development candidate, xgboost[fx,mk,cal] tuned all refit7 hl20, scored 62.14 bps vs the champion's 66.33 bps (-6.32%). (L16)
- On the hidden window it scored 65.26 bps vs the champion's 67.99 bps (p = 0.109) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 60.78, last 26w 66.33, prior 26w 46.41 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 67.74 bps (+2.13% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 65.57 bps (-1.15% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 63.08 bps (-4.9% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 69.46 bps (+4.72% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 64.91 bps (-2.14% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 68.23 bps (+2.86% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 70.04 bps (+5.59% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 68.65 bps (+3.5% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 63.27 bps (-4.61% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 66.45 bps (+0.18% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 63.16 bps (-4.78% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 62.93 bps (-5.13% vs champion) |
| L14 | backtest | xgboost[fx,mk,cal] all refit7 hl20: MAE 62.64 bps (-5.56% vs champion) |
| L15 | tune | xgboost[fx,mk,cal] tuned all refit7 hl20: CV MAE 61.37 → 58.37 bps |
| L16 | backtest | xgboost[fx,mk,cal] tuned all refit7 hl20: MAE 62.14 bps (-6.32% vs champion) |
| L17 | promote | xgboost[fx,mk,cal] tuned all refit7 hl20: 65.26 vs 67.99 bps, p = 0.109, failed |
| L18 | submit | accepted |

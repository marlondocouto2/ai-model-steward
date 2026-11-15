# Weekly model review: 2025-02-14

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 57.45 bps vs 47.37 bps in the prior 26 weeks (+21.28%). (L01)
- The best development candidate, ridge[fx,dxy,mk] tuned all refit7 hl20, scored 56.91 bps vs the champion's 57.45 bps (-0.94%). (L16)
- On the hidden window it scored 64.92 bps vs the champion's 64.49 bps (p = 0.719) and failed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 54.2, last 26w 57.45, prior 26w 47.37 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 62.6 bps (+8.96% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 61.06 bps (+6.28% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 58.16 bps (+1.24% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 63.65 bps (+10.79% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 59.73 bps (+3.97% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 62.24 bps (+8.34% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 64.5 bps (+12.27% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 62.66 bps (+9.07% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 58.02 bps (+0.99% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 60.85 bps (+5.92% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 57.58 bps (+0.23% vs champion) |
| L13 | backtest | ridge[fx,dxy,mk,cal] all refit7 hl20: MAE 57.84 bps (+0.68% vs champion) |
| L14 | backtest | ridge[fx,mk,cal] all refit7 hl20: MAE 57.79 bps (+0.59% vs champion) |
| L15 | tune | ridge[fx,dxy,mk] tuned all refit7 hl20: CV MAE 60.02 → 57.58 bps |
| L16 | backtest | ridge[fx,dxy,mk] tuned all refit7 hl20: MAE 56.91 bps (-0.94% vs champion) |
| L17 | promote | ridge[fx,dxy,mk] tuned all refit7 hl20: 64.92 vs 64.49 bps, p = 0.719, failed |
| L18 | submit | accepted |

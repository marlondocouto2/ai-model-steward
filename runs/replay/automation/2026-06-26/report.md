# Weekly model review: 2026-06-26

**Decision: Switch.** Champion: `xgboost[mk,lag] all refit7 hl10` (was `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`)

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 50.74 bps vs 44.71 bps in the prior 26 weeks (+13.49%). (L01)
- The best development candidate, xgboost[mk,lag] all refit7 hl10, scored 50.58 bps vs the champion's 50.74 bps (-0.32%). (L14)
- On the hidden window it scored 53.19 bps vs the champion's 55.23 bps (p = 0.025) and passed the promotion rule. (L17)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 45.42, last 26w 50.74, prior 26w 44.71 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 55.25 bps (+8.89% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 51.54 bps (+1.58% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 50.95 bps (+0.41% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 55.9 bps (+10.17% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 52.3 bps (+3.07% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 53.96 bps (+6.35% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 54.9 bps (+8.2% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 54.64 bps (+7.69% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 51.35 bps (+1.2% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 51.68 bps (+1.85% vs champion) |
| L12 | backtest | xgboost[fx,mk,lag] all refit7 hl10: MAE 50.65 bps (-0.18% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 51.07 bps (+0.65% vs champion) |
| L14 | backtest | xgboost[mk,lag] all refit7 hl10: MAE 50.58 bps (-0.32% vs champion) |
| L15 | tune | xgboost[mk,lag] tuned all refit7 hl10: CV MAE 54.22 → 53.7 bps |
| L16 | backtest | xgboost[mk,lag] tuned all refit7 hl10: MAE 51.2 bps (+0.91% vs champion) |
| L17 | promote | xgboost[mk,lag] all refit7 hl10: 53.19 vs 55.23 bps, p = 0.025, passed |
| L18 | submit | accepted |

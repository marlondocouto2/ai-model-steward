# Weekly model review: 2026-07-31

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 52.11 bps vs 43.32 bps in the prior 26 weeks (+20.29%). (L01)
- The best development candidate, lightgbm[fx,dxy,mk] all refit7 hl20, scored 52.31 bps vs the champion's 52.11 bps (+0.38%). (L10)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 14, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 44.6, last 26w 52.11, prior 26w 43.32 bps |
| L02 | backtest | ridge[fx,vol,cal] 2y refit30 hl20: MAE 57.42 bps (+10.19% vs champion) |
| L03 | backtest | xgboost[fx,vol,dxy,mk] 3y refit7 hl5: MAE 53.01 bps (+1.73% vs champion) |
| L04 | backtest | xgboost[fx,mk,lag] all refit7 hl20: MAE 52.41 bps (+0.58% vs champion) |
| L05 | backtest | ewma all refit30 hl5: MAE 57.06 bps (+9.5% vs champion) |
| L06 | backtest | xgboost[vol,mk] 2y refit30 hl20: MAE 54.15 bps (+3.91% vs champion) |
| L07 | backtest | lightgbm[fx,lag] 1y refit7 hl5: MAE 55.84 bps (+7.16% vs champion) |
| L08 | backtest | xgboost[dxy,cal] 3y refit7 hl5: MAE 56.23 bps (+7.91% vs champion) |
| L09 | backtest | xgboost[lag] 2y refit30 hl10: MAE 56.52 bps (+8.46% vs champion) |
| L10 | backtest | lightgbm[fx,dxy,mk] all refit7 hl20: MAE 52.31 bps (+0.38% vs champion) |
| L11 | backtest | lightgbm[fx,mk] 3y refit7 hl5: MAE 53.43 bps (+2.53% vs champion) |
| L12 | backtest | ridge[fx,dxy,mk] all refit7 hl20: MAE 53.15 bps (+2.0% vs champion) |
| L13 | backtest | xgboost[fx,mk,cal,lag] all refit7 hl20: MAE 52.6 bps (+0.94% vs champion) |
| L14 | backtest | xgboost[vol,mk,lag] all refit7 hl20: MAE 52.39 bps (+0.54% vs champion) |
| L15 | tune | lightgbm[fx,dxy,mk] tuned all refit7 hl20: CV MAE 55.62 → 54.56 bps |
| L16 | backtest | lightgbm[fx,dxy,mk] tuned all refit7 hl20: MAE 52.82 bps (+1.36% vs champion) |
| L17 | submit | accepted |

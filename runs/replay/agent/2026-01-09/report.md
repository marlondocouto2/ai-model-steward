# Weekly model review: 2026-01-09

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error has fallen in every corridor compared with the prior half-year, and its risk band is breached at a healthy rate. BR stays the hardest corridor, with the largest errors and a mild tendency to forecast too high. No structural break shows up that would call for a different config.

## Evidence

- The champion's error over the last 26 weeks was 43.73 bps vs 62.82 bps before (-30.39%), with a breach rate of 0.045. (L02)
- The champion's largest corridor bias is in BR at -13.99 bps, and its worst days are all BR. (L03)
- Refitting weekly instead of monthly gave 43.58 bps vs 43.73 bps (-0.34%), which is within noise and far from the 1% promotion bar. (L05)
- A shorter 2y window with halflife 5 was no better at 43.75 bps (+0.05%), and ridge was worse at 44.25 bps (+1.19%). (L08, L09)
- LightGBM was worse at 45.54 bps (+4.14%) and the EWMA baseline was worse at 46.67 bps (+6.72%). (L06, L07)

**Risks:** BR volatility and its larger markup swings could produce a run of large misses that a faster-refitting config would catch sooner. IN volatility is high relative to its history, which could hurt a model trained on calmer periods.

**Watch next week:** Watch BR bias and worst-day errors, IN errors while its volatility stays elevated, and whether the weekly-refit variant's small edge in BR becomes consistent.

## Ledger

Budget used: backtests 5, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-09 |
| L02 | champion-report | champion MAE last 4w 34.56, last 26w 43.73, prior 26w 62.82 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 43.73 bps (+0.0% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 43.58 bps (-0.34% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 45.54 bps (+4.14% vs champion) |
| L07 | backtest | ewma all refit30 hl10: MAE 46.67 bps (+6.72% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl5: MAE 43.75 bps (+0.05% vs champion) |
| L09 | backtest | ridge[vol,mk,cal,lag] all refit7 hl10: MAE 44.25 bps (+1.19% vs champion) |
| L10 | submit | accepted |

# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's slight degradation over the development window comes mainly from the early-April shock in BR and MX; error has since returned to normal levels and current volatility is unremarkable. IN error rose relative to its unusually calm prior period, and the model carries a persistent tendency to forecast too high in BR and MX.

## Evidence

- The champion's error over the last 26 weeks was 56.39 bps vs 55.34 bps before (+1.9%), with the last 4 weeks at 47.15 bps. (L02)
- The champion's monthly error peaked at 89.27 bps in 2025-04 and was 47.15 bps in 2025-08; its bias was -11.84 bps in BR and -10.59 bps in MX. (L03)
- Faster adaptation did not help: weekly refit scored 56.34 bps (-0.09%), and a 2y window with halflife 5 scored 58.78 bps (+4.24%). (L04, L05)
- Switching family gave no gain: LightGBM with the same features scored 56.59 bps (+0.35%) and the EWMA baseline 61.41 bps (+8.9%). (L06, L07)
- The best candidate, dropping FX-return and dollar-index features, scored 55.67 bps vs 56.39 bps (-1.28%), lower in every corridor but within normal development noise, and its BR bias stayed at -11.81 bps. (L08, L09)

**Risks:** The leaner feature set may hold a small real edge that we are leaving on the table, and the champion's monthly refit could lag if another sharp shock like April hits. The over-forecasting bias in BR and MX persists and is not fixed by any configuration tried.

**Watch next week:** Re-check whether the leaner candidate's edge holds and stays consistent across corridors as the window rolls forward; watch IN error and the BR and MX bias, and revisit faster refit if volatility percentiles jump.

## Ledger

Budget used: backtests 5, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-24 |
| L02 | champion-report | champion MAE last 4w 47.15, last 26w 56.39, prior 26w 55.34 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 56.34 bps (-0.09% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl5: MAE 58.78 bps (+4.24% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.59 bps (+0.35% vs champion) |
| L07 | backtest | ewma all refit30 hl10: MAE 61.41 bps (+8.9% vs champion) |
| L08 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 55.67 bps (-1.28% vs champion) |
| L09 | diagnose | diagnosis of xgboost[vol,mk,cal,lag] tuned all refit30 hl10 |
| L10 | submit | accepted |

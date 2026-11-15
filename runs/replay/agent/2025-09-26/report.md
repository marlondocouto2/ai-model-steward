# Weekly model review: 2025-09-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's overall error improved versus the prior half-year, driven by MX and BR recovering after the April shock, while IN error rose sharply from an unusually calm base. MX forecasts are biased high. No alternative window, refit cadence, halflife, family or feature set produced a consistent, material improvement in development.

## Evidence

- The champion's error over the last 26 weeks was 55.68 bps vs 59.6 bps before (-6.58%), an improvement; IN rose to 32.94 bps from 13.19 bps. (L02)
- The champion over-forecasts MX, with a bias of -11.44 bps, and its worst days cluster around the April shock. (L03)
- The best candidate, xgboost on volatility, markup and lagged residuals, scored 55.22 bps vs the champion's 55.68 bps (-0.83%), within development noise and short of the promotion threshold. (L09)
- Tuning that candidate cut CV error by -1.17%, but its backtest gain shrank to -0.09% (55.63 bps vs 55.68 bps), so the tuning gain did not hold. (L10, L11)
- A one-year training window was worse at 59.18 bps (+6.29%), and weekly refit (+0.11%), LightGBM (+0.75%), ridge (+0.5%) and a shorter halflife (+0.95%) were all slightly worse. (L05, L04, L06, L07, L08)

**Risks:** IN volatility is elevated relative to its history while the champion's IN error has drifted up; if that regime persists, a faster-adapting config could start to win. The persistent MX bias could widen if markups keep falling.

**Watch next week:** Watch IN error and its breach rate, the sign and size of the MX bias, and whether the lean feature set keeps its small edge across all corridors; retest it if it does.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-09-26 |
| L02 | champion-report | champion MAE last 4w 43.77, last 26w 55.68, prior 26w 59.6 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 55.74 bps (+0.11% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit30 hl10: MAE 59.18 bps (+6.29% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 56.1 bps (+0.75% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 55.96 bps (+0.5% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 56.21 bps (+0.95% vs champion) |
| L09 | backtest | xgboost[vol,mk,lag] tuned all refit30 hl10: MAE 55.22 bps (-0.83% vs champion) |
| L10 | tune | xgboost[vol,mk,lag] tuned all refit30 hl10: CV MAE 55.18 → 54.53 bps |
| L11 | backtest | xgboost[vol,mk,lag] tuned all refit30 hl10: MAE 55.63 bps (-0.09% vs champion) |
| L12 | submit | accepted |

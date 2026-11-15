# Weekly model review: 2025-07-11

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error drifted up modestly, driven mainly by the IN corridor losing its earlier unusually low error and by the April tariff shock days in BR and MX, while MX improved overall. No candidate configuration showed a consistent, material edge over the champion across corridors, so the drift looks like a regime effect rather than a fixable model weakness.

## Evidence

- The champion's development-window error was 63.07 bps vs 60.91 bps in the prior period (+3.55%). (L02)
- The deterioration is concentrated in IN, where error rose to 29.53 bps from 9.08 bps, while MX improved to 77.68 bps from 98.07 bps. (L02)
- The best challenger, a re-tuned XGBoost, scored 62.71 bps vs the champion's 63.07 bps (-0.57%), too small and within development noise to justify a promotion test. (L10)
- Faster adaptation did not help: weekly refits alone scored 62.98 bps (-0.14%), and a shorter window with a shorter halflife was worse at 66.02 bps (+4.68%). (L04, L05)
- Alternative families were worse: LightGBM 63.55 bps (+0.76%), ridge 64.36 bps (+2.05%), and EWMA 67.95 bps (+7.74%). (L08, L06, L07)

**Risks:** IN volatility is near the top of its recent range and its markup jumped last week, so if that regime persists the champion's slow monthly refit and long training window may lag. BR had a large weekly move, and the champion's breach rate there is near the upper edge of the acceptable band.

**Watch next week:** Watch whether IN error keeps rising alongside elevated volatility and markup, whether BR breaches move outside the acceptable band, and whether the tuned XGBoost's small edge grows enough to warrant a promotion test.

## Ledger

Budget used: backtests 6, tunes 1, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-11 |
| L02 | champion-report | champion MAE last 4w 46.23, last 26w 63.07, prior 26w 60.91 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 62.98 bps (-0.14% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl5: MAE 66.02 bps (+4.68% vs champion) |
| L06 | backtest | ridge[vol,mk,lag] 2y refit7 hl5: MAE 64.36 bps (+2.05% vs champion) |
| L07 | backtest | ewma all refit30 hl10: MAE 67.95 bps (+7.74% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.55 bps (+0.76% vs champion) |
| L09 | tune | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 56.65 → 55.42 bps |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 62.71 bps (-0.57% vs champion) |
| L11 | submit | accepted |

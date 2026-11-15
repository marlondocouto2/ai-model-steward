# Weekly model review: 2025-02-21

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error rose in the recent development half-year, driven by the MX and BR corridors during volatile episodes, with forecasts biased low in both, while IN improved. Error has eased again in the most recent weeks, and no alternative family, window, refit cadence, halflife or feature subset beat the champion beyond noise.

## Evidence

- The champion's error over the recent half-year was 57.14 bps vs 49.17 bps before (+16.21%), worse in MX (83.17 bps vs 70.2 bps) and BR (78.96 bps vs 66.47 bps) but improved in IN (9.28 bps vs 10.83 bps); the last four weeks were 45.28 bps. (L02)
- The champion forecasts too low in MX (bias 14.53 bps) and BR (bias 10.96 bps), and its worst months were 2024-08 (72.84 bps) and 2024-11 (67.36 bps). (L03)
- Faster adaptation did not help: weekly refits gave 57.19 bps (+0.09%) and a one-year window with weekly refits was worse at 58.54 bps (+2.45%). (L04, L05)
- Other families were clearly worse: lightgbm 61.94 bps (+8.4%), ridge 61.55 bps (+7.72%), ewma 62.97 bps (+10.2%). (L06, L07, L08)
- Halflife and feature changes on the champion were within noise: halflife 5 gave 57.19 bps (+0.09%), halflife 20 gave 57.3 bps (+0.28%), and markup, calendar and lagged residuals alone gave 57.18 bps (+0.07%). (L09, L10, L11)

**Risks:** The persistent low bias in MX and BR could reflect a structural shift in markups that the champion's long training window adapts to slowly; if BR's recent markup drop persists, the champion may keep under-performing there while development tests lack the power to detect a better config.

**Watch next week:** Watch MX and BR bias and error, especially whether BR error stays elevated as its markup falls and volatility stays low, and whether the BR risk band breach rate drifts above the acceptable range.

## Ledger

Budget used: backtests 8, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-02-21 |
| L02 | champion-report | champion MAE last 4w 45.28, last 26w 57.14, prior 26w 49.17 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 57.19 bps (+0.09% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl10: MAE 58.54 bps (+2.45% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit7 hl5: MAE 61.94 bps (+8.4% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit7 hl5: MAE 61.55 bps (+7.72% vs champion) |
| L08 | backtest | ewma 2y refit7 hl5: MAE 62.97 bps (+10.2% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 57.19 bps (+0.09% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 57.3 bps (+0.28% vs champion) |
| L11 | backtest | xgboost[mk,cal,lag] tuned all refit30 hl10: MAE 57.18 bps (+0.07% vs champion) |
| L12 | submit | accepted |

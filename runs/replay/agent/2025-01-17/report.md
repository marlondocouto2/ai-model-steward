# Weekly model review: 2025-01-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error rose sharply over the development window, driven almost entirely by MX, where a high-volatility regime caused large under-forecasts; IN stayed stable and BR worsened moderately with too many risk-band breaches. Every alternative degraded in the same way, so the problem is the regime, not the champion's configuration.

## Evidence

- The champion's error over the last 26 weeks was 62.14 bps vs 41.39 bps before (+50.13%). (L02)
- MX drove the deterioration: its error was 100.17 bps vs 50.87 bps before, with a bias of 29.4 bps (forecasts too low). (L02, L03)
- Faster adaptation did not help: weekly refits scored 62.27 bps (+0.21%) and a halflife of 20 scored 62.29 bps (+0.24%), both worse than the champion's 62.14 bps. (L04, L09)
- Shorter training windows were worse: 1y with weekly refits scored 64.78 bps (+4.25%) and 2y scored 64.88 bps (+4.41%). (L05, L10)
- Other families were worse: lightgbm scored 63.57 bps (+2.3%), ridge 64.52 bps (+3.83%) and ewma 69.46 bps (+11.78%). (L08, L07, L06)
- The champion's BR breach rate of 0.106 over the last 26 weeks is above the risk band, while overall it was 0.054. (L02)

**Risks:** If MX stays in a high-volatility regime, the champion's persistent low bias there may keep inflating error, and its BR risk band may keep breaching too often. A model better suited to the new regime may exist outside the configurations tested this week.

**Watch next week:** Watch MX volatility and the sign of MX bias, the BR breach rate, and whether the champion's recent error keeps falling toward its earlier level. If MX bias persists, test bias-correcting or markup-focused variants.

## Ledger

Budget used: backtests 7, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-01-17 |
| L02 | champion-report | champion MAE last 4w 53.54, last 26w 62.14, prior 26w 41.39 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 62.27 bps (+0.21% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl5: MAE 64.78 bps (+4.25% vs champion) |
| L06 | backtest | ewma all refit7 hl5: MAE 69.46 bps (+11.78% vs champion) |
| L07 | backtest | ridge[vol,mk,lag] 1y refit7 hl5: MAE 64.52 bps (+3.83% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.57 bps (+2.3% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 62.29 bps (+0.24% vs champion) |
| L10 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: MAE 64.88 bps (+4.41% vs champion) |
| L11 | submit | accepted |

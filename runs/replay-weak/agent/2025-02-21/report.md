# Weekly model review: 2025-02-21

**Decision: Switch.** Champion: `lightgbm[mk,cal,lag] tuned all refit7 hl10` (was `ewma all refit30 hl10`)

**What changed:** The champion's error rose in the latest half-year, driven by the MX and BR corridors, with a clear weekday pattern and a downward bias in MX that a feature-free EWMA cannot capture. A tuned LightGBM using markup, calendar and lagged-residual features beat the champion in every corridor in development and passed the promotion test.

## Evidence

- The champion's error over the last 26 weeks was 60.57 bps vs 54.4 bps before (+11.34%). (L02)
- The champion's MAE by target weekday ranged from 41.24 bps on Sunday to 76.61 bps on Wednesday, and its MX bias was -12.16 bps. (L03)
- In development the tuned challenger had 56.77 bps MAE vs the champion's 60.57 bps (-6.27%), better in every corridor: MX 82.35 bps vs 85.73 bps, IN 9.35 bps vs 13.28 bps, BR 78.62 bps vs 82.71 bps. (L12)
- Tuning improved the untuned LightGBM config, whose development MAE was 58.09 bps (-4.09% vs the champion). (L08, L12)
- In the promotion window the challenger's MAE was 60.04 bps vs the champion's 65.06 bps (-7.72%), with a Diebold-Mariano p-value of 0.043 and a breach rate of 0.087; all checks passed. (L13)

**Risks:** The challenger's breach rate in the promotion window is near the upper limit of the band, so its risk intervals may be too narrow, and BR breaches were already high in development. The tuned parameters came from historical cross-validation and may not hold if the markup regime shifts, such as BR's recent markup drop.

**Watch next week:** Watch the new champion's breach rate and whether it stays inside the band. Also watch the per-corridor bias in MX and BR, and whether BR markup keeps falling. If breaches keep rising, consider retuning or reverting.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-02-21 |
| L02 | champion-report | champion MAE last 4w 45.28, last 26w 60.57, prior 26w 54.4 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 62.97 bps (+3.96% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 59.01 bps (-2.58% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 59.09 bps (-2.44% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 61.55 bps (+1.62% vs champion) |
| L08 | backtest | lightgbm[mk,cal,lag] all refit7 hl10: MAE 58.09 bps (-4.09% vs champion) |
| L09 | backtest | xgboost[vol,mk,cal,lag] 2y refit7 hl10: MAE 59.97 bps (-0.99% vs champion) |
| L10 | diagnose | diagnosis of lightgbm[mk,cal,lag] all refit7 hl10 |
| L11 | tune | lightgbm[mk,cal,lag] tuned all refit7 hl10: CV MAE 59.5 → 57.09 bps |
| L12 | backtest | lightgbm[mk,cal,lag] tuned all refit7 hl10: MAE 56.77 bps (-6.27% vs champion) |
| L13 | promote | lightgbm[mk,cal,lag] tuned all refit7 hl10: 60.04 vs 65.06 bps, p = 0.043, passed |
| L14 | submit | rejected: 1 error(s) |
| L15 | submit | accepted |

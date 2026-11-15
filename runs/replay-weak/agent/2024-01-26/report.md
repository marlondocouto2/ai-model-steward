# Weekly model review: 2024-01-26

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error eased compared with the prior half-year, but it still trails a ridge model built on markup and lagged-residual features, which beat it in every corridor during development and on the hidden window. The challenger failed promotion only because its risk band was too wide: it breached on too few days, so its uncertainty is miscalibrated and the rule does not allow a switch.

## Evidence

- The champion's error over the last 26 weeks was 56.51 bps vs 68.69 bps before (-17.73%). (L02)
- In development, the tuned ridge on markup and lagged residuals had lower error than the champion: 53.13 bps vs 56.51 bps (-5.98%), and lower in every corridor (MX 69.8 bps vs 74.49 bps, IN 14.66 bps vs 15.47 bps, BR 75.04 bps vs 79.7 bps). (L12)
- Adding calendar features to the ridge did not help: 54.48 bps with calendar vs 53.53 bps without. (L05, L07)
- In the promotion test the challenger had lower error, 46.32 bps vs 49.96 bps (-7.29%), with a Diebold-Mariano p-value of 0.045, but its risk band breach rate of 0.012 was below the required band, so the promotion failed. (L13)

**Risks:** Keeping the champion leaves a consistent accuracy gain unused, and the champion may keep losing ground to the feature-based ridge, especially in the MX and BR corridors where its error is largest and the MX markup is rising. The challenger's advantage could also be partly noise in a short hidden window.

**Watch next week:** Re-test the ridge on markup and lagged residuals with attention to its risk band calibration, since an overly wide band was the only reason it failed; watch the MX markup trend and whether the champion's early-week errors keep exceeding its weekend errors.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-01-26 |
| L02 | champion-report | champion MAE last 4w 32.71, last 26w 56.51, prior 26w 68.69 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 58.65 bps (+3.79% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 54.48 bps (-3.59% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 55.77 bps (-1.31% vs champion) |
| L07 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 53.53 bps (-5.27% vs champion) |
| L08 | backtest | ridge[vol,mk,cal,lag] 2y refit7 hl10: MAE 54.44 bps (-3.66% vs champion) |
| L09 | backtest | ridge[mk,cal,lag] 3y refit7 hl10: MAE 54.23 bps (-4.03% vs champion) |
| L10 | diagnose | diagnosis of ridge[mk,lag] 2y refit7 hl10 |
| L11 | tune | ridge[mk,lag] tuned 2y refit7 hl10: CV MAE 67.28 → 66.56 bps |
| L12 | backtest | ridge[mk,lag] tuned 2y refit7 hl10: MAE 53.13 bps (-5.98% vs champion) |
| L13 | promote | ridge[mk,lag] tuned 2y refit7 hl10: 46.32 vs 49.96 bps, p = 0.045, failed |
| L14 | submit | accepted |

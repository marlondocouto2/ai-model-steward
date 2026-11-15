# Weekly model review: 2026-03-06

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The peso and real moved sharply against the dollar last week and the Mexico markup widened, while Brazil remains the dominant source of error. The champion has no markup information, and a ridge model using markup and lagged-residual features beat it consistently across all corridors in development, but it failed the promotion test on risk-band calibration, so the champion stays.

## Evidence

- The champion's error over the last 26 weeks was 44.9 bps vs 63.01 bps before (-28.74%), but rose to 49.79 bps over the last 4 weeks, with Brazil at 81.31 bps. (L02)
- The Mexico markup rose to 148.1 bps last week from 130.5 bps over the prior 4 weeks, with a 1-week move z-score of 2.95. (L01)
- The ridge challenger with markup and lagged residuals had a development error of 41.48 bps vs the champion's 44.9 bps (-7.62%), and was better in every corridor: MX 39.07 bps vs 42.61 bps, IN 24.02 bps vs 27.1 bps, BR 61.47 bps vs 65.09 bps. (L07)
- Markup is the feature that matters: dropping it in favour of calendar features cut the improvement to -0.91%, and tuning alpha did not help (-7.51%). (L08, L12)
- In the promotion window the challenger's error was 51.8 bps vs the champion's 59.39 bps (-12.78%, DM p-value 0.001), but its band breach rate of 11.3% was outside the allowed range, so the test failed and the switch is not allowed. (L13)

**Risks:** The champion is clearly less accurate than the markup-aware challenger in both windows, so keeping it gives up accuracy, especially in Mexico and Brazil while markups and volatility are elevated. The challenger's risk band is too narrow in the recent regime, so switching would have under-stated tail risk.

**Watch next week:** Check whether the champion's recent error in Brazil and Mexico keeps rising, and whether the Mexico markup stays wide. Next week, retest the markup-aware ridge with settings that widen its risk band, such as a longer half-life or added volatility features, before trying promotion again.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-03-06 |
| L02 | champion-report | champion MAE last 4w 49.79, last 26w 44.9, prior 26w 63.01 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 41.91 bps (-6.66% vs champion) |
| L05 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 43.17 bps (-3.85% vs champion) |
| L06 | backtest | ewma all refit7 hl5: MAE 47.53 bps (+5.86% vs champion) |
| L07 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 41.48 bps (-7.62% vs champion) |
| L08 | backtest | ridge[cal,lag] 2y refit7 hl10: MAE 44.49 bps (-0.91% vs champion) |
| L09 | backtest | ridge[mk,cal,lag] all refit7 hl10: MAE 41.62 bps (-7.31% vs champion) |
| L10 | diagnose | diagnosis of ridge[mk,cal,lag] 2y refit7 hl10 |
| L11 | tune | ridge[mk,lag] tuned 2y refit7 hl10: CV MAE 53.21 → 51.71 bps |
| L12 | backtest | ridge[mk,lag] tuned 2y refit7 hl10: MAE 41.53 bps (-7.51% vs champion) |
| L13 | promote | ridge[mk,lag] 2y refit7 hl10: 51.8 vs 59.39 bps, p = 0.001, failed |
| L14 | submit | rejected: 1 error(s) |
| L15 | submit | accepted |

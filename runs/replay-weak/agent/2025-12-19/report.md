# Weekly model review: 2025-12-19

**Decision: Switch.** Champion: `ridge[mk,lag] tuned all refit7 hl10` (was `ewma all refit30 hl10`)

**What changed:** The champion's error has come down from the prior half-year, but it still under-forecasts margins, especially in MX, and BR dominates the error. A ridge model on markup and lagged-residual features fixes this structure consistently across all corridors, weekdays and volatility regimes, while faster EWMA adaptation and volatility features did not help.

## Evidence

- The champion's MAE over the last 26 weeks was 48.38 bps vs 68.63 bps before, with a positive MX bias of 6.93 bps (forecasting too low). (L02, L03)
- Faster adaptation was worse: EWMA refit7 hl5 scored 51.1 bps, +5.62% vs the champion. (L04)
- Markup plus lagged residuals is the core signal: ridge on those features over all history scored 44.78 bps (-7.44%), while adding volatility gave a smaller gain of -3.06%. (L10, L09)
- The tuned ridge (alpha 846.61897) scored 44.55 bps vs 48.38 bps (-7.92%), better in every corridor: MX 42.05 vs 47.05 bps, IN 26.03 vs 28.16 bps, BR 65.54 vs 69.92 bps. (L11, L12)
- In the hidden promotion window the challenger scored 41.16 bps vs 42.67 bps for the champion (-3.54%), DM p-value 0.071, breach rate 0.025, and passed all checks. (L14)

**Risks:** The promotion improvement is smaller than in development and significance is only moderate, so part of the development gain may be luck. The challenger's bias flipped to over-forecasting in BR and MX, which could cost margin if it persists, and BR tail days remain large for both models. IN volatility is near the top of its historical range, which neither model was tested on much.

**Watch next week:** Track the new champion's bias in BR and MX and whether over-forecasting persists, its IN breach rate given elevated IN volatility, and whether BR's large-error days recur.

## Ledger

Budget used: backtests 8, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-19 |
| L02 | champion-report | champion MAE last 4w 39.42, last 26w 48.38, prior 26w 68.63 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 51.1 bps (+5.62% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 46.2 bps (-4.51% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 47.6 bps (-1.61% vs champion) |
| L07 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 45.2 bps (-6.57% vs champion) |
| L08 | backtest | ridge[mk,cal,lag] all refit7 hl10: MAE 45.13 bps (-6.72% vs champion) |
| L09 | backtest | ridge[vol,mk,cal,lag] 2y refit7 hl10: MAE 46.9 bps (-3.06% vs champion) |
| L10 | backtest | ridge[mk,lag] all refit7 hl10: MAE 44.78 bps (-7.44% vs champion) |
| L11 | tune | ridge[mk,lag] tuned all refit7 hl10: CV MAE 57.97 → 54.27 bps |
| L12 | backtest | ridge[mk,lag] tuned all refit7 hl10: MAE 44.55 bps (-7.92% vs champion) |
| L13 | diagnose | diagnosis of ridge[mk,lag] tuned all refit7 hl10 |
| L14 | promote | ridge[mk,lag] tuned all refit7 hl10: 41.16 vs 42.67 bps, p = 0.071, passed |
| L15 | submit | accepted |

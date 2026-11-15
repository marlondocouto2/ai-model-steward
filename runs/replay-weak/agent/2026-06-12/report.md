# Weekly model review: 2026-06-12

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error rose across all three corridors in the development window, worst in March and on volatile days, with opposite-signed bias in BR (forecasting too high) and IN (forecasting too low). Feature-based models using markup, volatility and lagged residuals looked better in development, but the advantage reversed on the recent hidden weeks, so it does not appear durable.

## Evidence

- The champion's error over the last 26 weeks was 54.15 bps vs 48.51 bps before (+11.63%). (L02)
- A faster-adapting EWMA was worse in development: 55.87 bps vs the champion's 54.15 bps (+3.18%). (L04)
- The best development candidate, LightGBM on markup, volatility and lagged residuals, scored 51.24 bps vs the champion's 54.15 bps (-5.37%), lower in MX, IN and BR. (L06)
- Tuning that candidate did not help in development: 51.33 bps tuned vs 51.24 bps untuned. (L12, L06)
- In the promotion test the challenger was worse than the champion, 52.27 bps vs 49.84 bps (+4.88%), with a Diebold-Mariano p-value of 0.943 and a breach rate of 0.012, failing all three checks. (L13)

**Risks:** The champion is a slow, featureless average that has lost accuracy over recent months and remains biased in BR and IN; if volatility in IN and BR stays elevated or markups keep widening, a feature-based model could overtake it, and keeping the champion would forgo that gain.

**Watch next week:** Watch whether the champion's recent error keeps falling or rises again, whether BR and IN bias persists, whether IN volatility stays near the top of its range, and whether last week's widening of markups continues; retest the markup-plus-lagged-residual candidates if the champion deteriorates.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-06-12 |
| L02 | champion-report | champion MAE last 4w 57.63, last 26w 54.15, prior 26w 48.51 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 55.87 bps (+3.18% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 51.7 bps (-4.52% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl10: MAE 51.24 bps (-5.37% vs champion) |
| L07 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 51.3 bps (-5.26% vs champion) |
| L08 | backtest | lightgbm[vol,mk,lag] 1y refit7 hl10: MAE 51.8 bps (-4.34% vs champion) |
| L09 | backtest | ridge[vol,mk,lag] 2y refit7 hl10: MAE 51.87 bps (-4.21% vs champion) |
| L10 | diagnose | diagnosis of lightgbm[vol,mk,lag] 2y refit7 hl10 |
| L11 | tune | lightgbm[vol,mk,lag] tuned 2y refit7 hl10: CV MAE 54.82 → 53.75 bps |
| L12 | backtest | lightgbm[vol,mk,lag] tuned 2y refit7 hl10: MAE 51.33 bps (-5.21% vs champion) |
| L13 | promote | lightgbm[vol,mk,lag] 2y refit7 hl10: 52.27 vs 49.84 bps, p = 0.943, failed |
| L14 | submit | accepted |

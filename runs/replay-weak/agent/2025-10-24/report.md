# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error rose versus the prior half-year, mostly from the April volatility shock in BR and MX and a higher error level in IN. A ridge model on markup and lagged-residual features beat the champion in development in every corridor, but its lead in the promotion window was smaller and not statistically significant, so the rule does not allow a switch.

## Evidence

- The champion's error over the last 26 weeks was 61.41 bps vs 59.31 bps before (+3.54%). (L02)
- Making the EWMA adapt faster (refit7, hl5) was worse: 65.26 bps vs the champion's 61.41 bps (+6.27%). (L04)
- Markup features drive the gain: ridge on markup alone reached 56.03 bps (-8.76%), while lagged residuals alone reached 60.5 bps (-1.48%). (L07, L08)
- The tuned ridge on markup and lagged residuals improved development error to 55.89 bps (-8.99%), better in every corridor: MX 60.47 bps vs 67.56 bps, IN 31.33 bps vs 34.53 bps, BR 75.84 bps vs 82.1 bps, with a 0.065 breach rate. (L12)
- In the promotion test the challenger scored 41.6 bps vs the champion's 43.01 bps (-3.28%), but the Diebold-Mariano p-value of 0.262 is not below the threshold, so the promotion failed. (L13)

**Risks:** The ridge challenger's advantage may be real but too small to detect over a short calm window; keeping the champion could leave accuracy on the table if markup dynamics keep mattering. The challenger also showed a negative bias in MX and BR in development, which could matter in a sharp move.

**Watch next week:** Re-run the champion report to see whether IN error stays elevated, check whether a volatility spike in BR or MX returns, and consider retesting the markup-based ridge challenger once the promotion window holds more evidence.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-10-24 |
| L02 | champion-report | champion MAE last 4w 54.88, last 26w 61.41, prior 26w 59.31 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 65.26 bps (+6.27% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 56.82 bps (-7.47% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl10: MAE 57.61 bps (-6.19% vs champion) |
| L07 | backtest | ridge[mk] 2y refit7 hl10: MAE 56.03 bps (-8.76% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 60.5 bps (-1.48% vs champion) |
| L09 | backtest | ridge[mk,lag] all refit7 hl10: MAE 56.11 bps (-8.63% vs champion) |
| L10 | diagnose | diagnosis of ridge[mk,lag] 2y refit7 hl10 |
| L11 | tune | ridge[mk,lag] tuned all refit7 hl10: CV MAE 56.61 → 54.7 bps |
| L12 | backtest | ridge[mk,lag] tuned all refit7 hl10: MAE 55.89 bps (-8.99% vs champion) |
| L13 | promote | ridge[mk,lag] tuned all refit7 hl10: 41.6 vs 43.01 bps, p = 0.262, failed |
| L14 | submit | accepted |

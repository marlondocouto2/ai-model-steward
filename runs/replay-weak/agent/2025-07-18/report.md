# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The INR corridor's margin markup rose sharply and the champion's IN error worsened markedly versus the prior half-year, while the April tariff shock drove the largest misses in BR and MX. Models that use the markup features track this better in every corridor, but the advantage did not pass the significance test on the hidden window.

## Evidence

- The champion's error over the last 26 weeks was 67.67 bps vs 66.06 bps before (+2.44%), with IN at 33.4 bps vs 13.24 bps before. (L02)
- IN markup was 69.9 bps last week vs 52.3 bps over the prior four weeks. (L01)
- Markup features drive the gain: LightGBM with markup alone scored 63.04 bps (-6.84% vs champion), while lagged residuals alone scored 66.63 bps (-1.54%). (L07, L08)
- The tuned LightGBM challenger scored 62.93 bps in development (-7.0% vs champion), better in all three corridors (MX 75.86 vs 81.84 bps, IN 30.05 vs 33.4 bps, BR 82.81 vs 87.7 bps), with a 0.067 breach rate. (L12)
- In the promotion test the challenger scored 45.98 bps vs the champion's 49.47 bps (-7.05%), but the Diebold-Mariano p-value of 0.139 is not below 0.1, so the rule failed and the champion stays. (L13)

**Risks:** The markup-based challenger was better in both development and the hidden window, so keeping the champion may leave accuracy on the table, especially in IN if the markup shift persists. Conversely, the challenger's gain is not yet statistically distinguishable from luck, and its band breach rate runs higher than the champion's.

**Watch next week:** Whether IN markup stays elevated and the champion's IN error keeps rising; re-test the tuned markup LightGBM challenger as more promotion-window days accumulate, since a consistent gain may reach significance.

## Ledger

Budget used: backtests 7, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-18 |
| L02 | champion-report | champion MAE last 4w 51.92, last 26w 67.67, prior 26w 66.06 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 70.84 bps (+4.68% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 64.13 bps (-5.23% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl10: MAE 63.36 bps (-6.37% vs champion) |
| L07 | backtest | lightgbm[mk] 2y refit7 hl10: MAE 63.04 bps (-6.84% vs champion) |
| L08 | backtest | lightgbm[lag] 2y refit7 hl10: MAE 66.63 bps (-1.54% vs champion) |
| L09 | backtest | lightgbm[vol,mk,lag] all refit7 hl10: MAE 63.4 bps (-6.31% vs champion) |
| L10 | diagnose | diagnosis of lightgbm[vol,mk,lag] 2y refit7 hl10 |
| L11 | tune | lightgbm[vol,mk,lag] tuned all refit7 hl10: CV MAE 56.61 → 55.31 bps |
| L12 | backtest | lightgbm[vol,mk,lag] tuned all refit7 hl10: MAE 62.93 bps (-7.0% vs champion) |
| L13 | promote | lightgbm[vol,mk,lag] tuned all refit7 hl10: 45.98 vs 49.47 bps, p = 0.139, failed |
| L14 | submit | accepted |

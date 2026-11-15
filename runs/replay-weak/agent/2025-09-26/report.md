# Weekly model review: 2025-09-26

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion improved overall in development, but India got worse while Mexico improved, and Mexico's customer markup has moved recently. A ridge model on markup features beat the champion consistently across corridors, but its risk band was too wide in the promotion window, so the rule does not allow a switch.

## Evidence

- The champion's error over the last 26 weeks was 60.26 bps vs 63.75 bps before (-5.47%), but India worsened from 17.97 bps to 34.78 bps. (L02)
- The markup-only ridge model with all history had 55.75 bps error vs the champion's 60.26 bps (-7.48%), and was lower in every corridor: MX 60.56 bps vs 67.6 bps, IN 32.78 bps vs 34.78 bps, BR 73.77 bps vs 78.26 bps. (L10)
- Markup was the driver: ridge on markup alone with a 2y window improved error by -6.7%, while lagged residuals alone improved it by only -0.73%. (L07, L08)
- In the promotion window the challenger had 45.34 bps error vs the champion's 50.79 bps (-10.73%) with a DM p-value of 0.021, but its band breach rate of 1.2% is outside 2%-9%, so the promotion test failed. (L13)

**Risks:** Keeping the champion leaves a consistent accuracy gain unused; the markup model's lower error looks real, and the champion's India error has been drifting up. The challenger's band may simply be miscalibrated rather than the model being worse.

**Watch next week:** Watch India error for the champion and whether Mexico's markup keeps shifting. Re-test a markup-feature challenger, checking its band breach rate is within the allowed range before using the promotion test.

## Ledger

Budget used: backtests 8, tunes 0, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-09-26 |
| L02 | champion-report | champion MAE last 4w 53.07, last 26w 60.26, prior 26w 63.75 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 63.85 bps (+5.96% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 57.72 bps (-4.22% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 57.63 bps (-4.36% vs champion) |
| L07 | backtest | ridge[mk] 2y refit7 hl10: MAE 56.22 bps (-6.7% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 59.82 bps (-0.73% vs champion) |
| L09 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 57.17 bps (-5.13% vs champion) |
| L10 | backtest | ridge[mk] all refit7 hl10: MAE 55.75 bps (-7.48% vs champion) |
| L11 | backtest | ridge[mk] 1y refit7 hl10: MAE 57.7 bps (-4.25% vs champion) |
| L12 | diagnose | diagnosis of ridge[mk] 2y refit7 hl10 |
| L13 | promote | ridge[mk] all refit7 hl10: 45.34 vs 50.79 bps, p = 0.021, failed |
| L14 | submit | accepted |

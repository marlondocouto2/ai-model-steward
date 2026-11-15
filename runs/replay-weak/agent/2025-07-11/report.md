# Weekly model review: 2025-07-11

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error rose modestly versus the prior half-year, driven mainly by the INR corridor and by the early-April shock days in BRL and MXN. Feature models using the markup signal beat the champion in development across all corridors, but the advantage did not hold up with statistical significance in the promotion window.

## Evidence

- The champion's error over the last 26 weeks was 67.95 bps vs 65.02 bps before (+4.51%), with IN rising from 12.82 bps to 33.29 bps. (L02)
- Markup features drive the development gain: ridge with markup alone was -6.33% vs the champion, while lagged residuals alone were only -0.47%. (L07, L08)
- The best candidate, lightgbm[vol,mk,lag] all refit7 hl10, scored 63.4 bps vs 67.95 bps (-6.7%) in development, lower in every corridor, with a breach rate of 0.065. (L09)
- It also had lower error than the champion in every month, weekday and volatility regime, e.g. 64.25 bps vs 72.06 bps in volatile conditions. (L10, L03)
- In the promotion window it improved error only -1.08% (47.63 bps vs 48.15 bps) with a Diebold-Mariano p-value of 0.457, so the promotion rule failed and the champion is kept. (L11)

**Risks:** The markup-based challenger may genuinely be better and the promotion window simply too short or too calm to show it, so keeping the champion could forgo a real gain. The champion's risk band was breached far less often than nominal in the promotion window, suggesting its bands may be too wide, while its development error trend is still drifting upward, especially in INR.

**Watch next week:** Whether INR error and markup keep rising, whether BRL's sharp recent move turns into a volatile regime, and whether the markup-feature challenger's advantage reappears so it can be retested with the next promotion test.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-11 |
| L02 | champion-report | champion MAE last 4w 50.42, last 26w 67.95, prior 26w 65.02 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 71.24 bps (+4.84% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 64.15 bps (-5.59% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl10: MAE 63.7 bps (-6.25% vs champion) |
| L07 | backtest | ridge[mk] 2y refit7 hl10: MAE 63.65 bps (-6.33% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 67.63 bps (-0.47% vs champion) |
| L09 | backtest | lightgbm[vol,mk,lag] all refit7 hl10: MAE 63.4 bps (-6.7% vs champion) |
| L10 | diagnose | diagnosis of lightgbm[vol,mk,lag] all refit7 hl10 |
| L11 | promote | lightgbm[vol,mk,lag] all refit7 hl10: 47.63 vs 48.15 bps, p = 0.457, failed |
| L12 | submit | accepted |

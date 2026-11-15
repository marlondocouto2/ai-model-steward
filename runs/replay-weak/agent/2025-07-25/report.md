# Weekly model review: 2025-07-25

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** Customer markups rose in all three corridors, and India error rose sharply compared with the prior half-year while Mexico improved. Development backtests suggested that markup features help, but that edge did not hold in the hidden promotion window.

## Evidence

- The champion's error over the last 26 weeks was 65.47 bps vs 66.5 bps before (-1.55%), but India worsened from 13.12 bps to 34.3 bps. (L02)
- Markup features drove the development gain: ridge with markup alone scored 61.59 bps (-5.93% vs champion), while ridge with lagged residuals alone scored 64.95 bps (-0.79%). (L07, L08)
- The LightGBM challenger with volatility, markup and lagged-residual features scored 61.64 bps vs the champion's 65.47 bps in development (-5.85%), better in every corridor, with a 0.074 breach rate. (L06)
- In the promotion window the challenger was worse: 51.57 bps vs the champion's 49.17 bps (+4.88%), with a Diebold-Mariano p-value of 0.757, so the promotion rule failed. (L13)

**Risks:** Markups are still rising, so the champion, which has no markup features, could fall behind if the markup regime persists. The promotion window was short and calm, so it may have understated the value of the markup-aware challenger.

**Watch next week:** Watch whether markups keep rising and whether India error stays high. Retest a markup-feature challenger if the champion's recent error turns back up.

## Ledger

Budget used: backtests 8, tunes 0, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-25 |
| L02 | champion-report | champion MAE last 4w 50.95, last 26w 65.47, prior 26w 66.5 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 68.94 bps (+5.3% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 61.97 bps (-5.35% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl10: MAE 61.64 bps (-5.85% vs champion) |
| L07 | backtest | ridge[mk] 2y refit7 hl10: MAE 61.59 bps (-5.93% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 64.95 bps (-0.79% vs champion) |
| L09 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 61.8 bps (-5.61% vs champion) |
| L10 | diagnose | diagnosis of ridge[mk] 2y refit7 hl10 |
| L11 | backtest | ridge[mk] 1y refit7 hl10: MAE 63.54 bps (-2.95% vs champion) |
| L12 | backtest | ridge[mk] all refit30 hl10: MAE 60.97 bps (-6.87% vs champion) |
| L13 | promote | lightgbm[vol,mk,lag] 2y refit7 hl10: 51.57 vs 49.17 bps, p = 0.757, failed |
| L14 | submit | accepted |

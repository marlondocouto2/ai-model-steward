# Weekly model review: 2024-09-06

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** Peso volatility is near the top of its multi-year range and the champion's errors are concentrated in MX and BR during volatile spells, while IN stays calm. Markup-aware feature models looked clearly stronger in development, but that edge did not carry into the hidden promotion window.

## Evidence

- The champion's error over the last 26 weeks was 55.48 bps vs 57.27 bps before (-3.13%), but the last 4 weeks ran at 70.44 bps, driven by MX at 96.18 bps and BR at 104.77 bps. (L02)
- In development, ridge with markup, volatility and lagged-residual features scored 49.97 bps against the champion's 55.48 bps (-9.93%), ahead in all three corridors. (L06)
- Ablations show the markup features carry most of that gain: lagged residuals alone scored 56.82 bps (+2.42%) while markup plus lagged residuals scored 50.64 bps (-8.72%). (L07, L08)
- The promotion test failed: on the hidden window the challenger scored 72.96 bps vs the champion's 66.32 bps (+10.01% error), with a Diebold-Mariano p-value of 0.904; only the risk-band check passed. (L13)

**Risks:** The champion still carries a breach rate above the band in the volatile corridors and a mild low bias in MX and IN; if peso volatility persists, its slow monthly refit may keep lagging. The feature models' development edge may have been tied to a markup regime that has since shifted, so we may be discarding a model that recovers.

**Watch next week:** Check whether MX and BR champion errors ease as volatility normalizes, whether the champion's breach rate in those corridors stays elevated, and whether recent markup behavior has stabilized enough to retest a markup-aware challenger.

## Ledger

Budget used: backtests 7, tunes 0, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-09-06 |
| L02 | champion-report | champion MAE last 4w 70.44, last 26w 55.48, prior 26w 57.27 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 57.11 bps (+2.94% vs champion) |
| L05 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl5: MAE 49.83 bps (-10.18% vs champion) |
| L06 | backtest | ridge[vol,mk,lag] 2y refit7 hl5: MAE 49.97 bps (-9.93% vs champion) |
| L07 | backtest | ridge[lag] 2y refit7 hl5: MAE 56.82 bps (+2.42% vs champion) |
| L08 | backtest | ridge[mk,lag] 2y refit7 hl5: MAE 50.64 bps (-8.72% vs champion) |
| L09 | diagnose | diagnosis of ridge[vol,mk,lag] 2y refit7 hl5 |
| L10 | backtest | ridge[vol,mk,lag] 1y refit7 hl5: MAE 50.7 bps (-8.62% vs champion) |
| L11 | backtest | ridge[vol,dxy,mk,lag] 2y refit7 hl5: MAE 50.09 bps (-9.72% vs champion) |
| L12 | diagnose | diagnosis of lightgbm[vol,mk,lag] 2y refit7 hl5 |
| L13 | promote | ridge[vol,mk,lag] 2y refit7 hl5: 72.96 vs 66.32 bps, p = 0.904, failed |
| L14 | submit | accepted |

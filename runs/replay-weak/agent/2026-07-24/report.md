# Weekly model review: 2026-07-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error rose in every corridor, with Brazil still the hardest and India biased low. Feature models using markup consistently beat the plain EWMA champion in development. The markup-plus-volatility ridge challenger also beat it in the hidden window, but its risk band was never breached, which means the band is too wide, so the promotion rule blocks the switch.

## Evidence

- The champion's error over the last 26 weeks was 56.37 bps vs 46.35 bps before (+21.62%), with the worst corridor BR at 73.49 bps. (L02)
- Markup features drive the gain: ridge with markup alone scored 53.47 bps (-5.14% vs the champion), while ridge with lagged residuals alone was worse at 56.96 bps (+1.05%). (L07, L08)
- The tuned ridge with markup and volatility scored 53.49 bps vs the champion's 56.37 bps (-5.11%), lower in MX (54.63 bps), IN (35.06 bps) and BR (70.78 bps), with a breach rate of 0.061. (L16)
- In the promotion window the challenger had lower error, 49.35 bps vs 50.69 bps (-2.64%), with a DM p-value of 0.068, but failed the band check because its breach rate of 0.0% is below the allowed range. (L17)

**Risks:** The champion keeps degrading while a better point forecaster is blocked only by an overly wide risk band, so keeping it may cost margin accuracy. The challenger's edge in the hidden window was also smaller than in development, so part of the development gain may have been luck.

**Watch next week:** Recheck the markup-plus-volatility ridge, focusing on calibrating its risk band so breaches fall inside the allowed range. Track the champion's Brazil error and India bias, and watch whether markup keeps falling across corridors.

## Ledger

Budget used: backtests 10, tunes 1, promotion tests 1. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-24 |
| L02 | champion-report | champion MAE last 4w 53.97, last 26w 56.37, prior 26w 46.35 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 57.57 bps (+2.13% vs champion) |
| L05 | backtest | ridge[mk,lag] 2y refit7 hl10: MAE 53.9 bps (-4.38% vs champion) |
| L06 | backtest | lightgbm[vol,mk,lag] 2y refit7 hl5: MAE 54.12 bps (-3.99% vs champion) |
| L07 | backtest | ridge[mk] 2y refit7 hl10: MAE 53.47 bps (-5.14% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 56.96 bps (+1.05% vs champion) |
| L09 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 53.73 bps (-4.68% vs champion) |
| L10 | backtest | lightgbm[vol,mk,lag] 1y refit7 hl5: MAE 55.22 bps (-2.04% vs champion) |
| L11 | diagnose | diagnosis of ridge[mk] 2y refit7 hl10 |
| L12 | diagnose | diagnosis of lightgbm[vol,mk,lag] 2y refit7 hl5 |
| L13 | backtest | lightgbm[vol,mk] 2y refit7 hl5: MAE 55.21 bps (-2.06% vs champion) |
| L14 | backtest | ridge[vol,mk] 2y refit7 hl10: MAE 53.6 bps (-4.91% vs champion) |
| L15 | tune | ridge[vol,mk] tuned 2y refit7 hl10: CV MAE 55.15 → 54.49 bps |
| L16 | backtest | ridge[vol,mk] tuned 2y refit7 hl10: MAE 53.49 bps (-5.11% vs champion) |
| L17 | promote | ridge[vol,mk] tuned 2y refit7 hl10: 49.35 vs 50.69 bps, p = 0.068, failed |
| L18 | submit | rejected: 1 error(s) |
| L19 | submit | accepted |

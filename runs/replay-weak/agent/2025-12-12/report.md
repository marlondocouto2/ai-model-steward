# Weekly model review: 2025-12-12

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's error has fallen versus the prior half-year as markets calmed, especially in MX, but it still forecasts too low in MX and its error swings by weekday. A regularized ridge using markup, calendar and lagged-residual features beat it in development across all corridors, but did not clear the promotion rule on the hidden window.

## Evidence

- The champion's error over the last 26 weeks was 48.3 bps vs 68.64 bps before (-29.63%), with a positive MX bias of 8.34 bps (forecasting too low). (L02, L03)
- In development, the tuned ridge (markup, calendar, lagged residuals, all history) had 44.95 bps error vs the champion's 48.3 bps (-6.94%), better in MX (42.51 bps vs 47.44 bps), IN (26.72 bps vs 28.56 bps) and BR (65.63 bps vs 68.9 bps). (L11)
- The ridge advantage held across nearby variants: -4.39% with a 2y window, -5.32% without lagged residuals, and -6.17% untuned on all history, while a faster EWMA was worse at +5.69%. (L05, L07, L08, L04)
- On the promotion window the tuned ridge had 37.44 bps error vs the champion's 38.55 bps (-2.88%), but the Diebold-Mariano p-value was 0.135 and its breach rate of 1.9% was outside the band, so the rule failed. (L12)

**Risks:** The ridge challenger looked consistently better and may truly be better, so keeping the champion could forgo a real gain; the failed promotion may reflect a short, calm window rather than a lack of edge. The champion's low-side bias in MX could cost margin if markups shift again.

**Watch next week:** Re-test the tuned ridge challenger as more promotion data accumulates, check whether its band breach rate moves into the allowed range, and monitor the champion's MX bias and BR errors around volatile spells.

## Ledger

Budget used: backtests 6, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-12 |
| L02 | champion-report | champion MAE last 4w 39.05, last 26w 48.3, prior 26w 68.64 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 51.05 bps (+5.69% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 46.18 bps (-4.39% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 47.56 bps (-1.53% vs champion) |
| L07 | backtest | ridge[mk,cal] 2y refit7 hl10: MAE 45.73 bps (-5.32% vs champion) |
| L08 | backtest | ridge[mk,cal,lag] all refit7 hl10: MAE 45.32 bps (-6.17% vs champion) |
| L09 | diagnose | diagnosis of ridge[mk,cal,lag] 2y refit7 hl10 |
| L10 | tune | ridge[mk,cal,lag] tuned all refit7 hl10: CV MAE 58.56 → 54.71 bps |
| L11 | backtest | ridge[mk,cal,lag] tuned all refit7 hl10: MAE 44.95 bps (-6.94% vs champion) |
| L12 | promote | ridge[mk,cal,lag] tuned all refit7 hl10: 37.44 vs 38.55 bps, p = 0.135, failed |
| L13 | submit | accepted |

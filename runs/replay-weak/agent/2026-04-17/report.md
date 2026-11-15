# Weekly model review: 2026-04-17

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** Markups shifted in India and Brazil while Indian volatility rose to near its three-year high, and the EWMA champion ignores markup, so a markup-aware ridge model beat it consistently in development. On the hidden promotion window that advantage shrank to a statistically insignificant edge with too many risk-band breaches, so the switch is not justified.

## Evidence

- The champion's error over the last 26 weeks was 44.52 bps vs 62.34 bps in the prior 26 weeks (-28.59%). (L02)
- In development, the markup-only ridge (ridge_m) scored 41.29 bps vs the champion's 44.52 bps (-7.26%), lower in all three corridors: MX 39.71 bps vs 40.5 bps, IN 25.28 bps vs 29.48 bps, BR 58.97 bps vs 63.7 bps. (L10)
- Markup is the source of the gain: calendar-only ridge changed error by 0.79% and lagged-residual-only ridge by -0.09% vs the champion. (L11, L08)
- Adapting faster did not help: EWMA with weekly refits and a halflife of 5 scored 46.73 bps (+4.96% vs the champion). (L04)
- The ridge_m promotion test failed: 73.01 bps vs the champion's 73.76 bps (-1.02%), with a Diebold-Mariano p-value of 0.387 and a breach rate of 0.123. (L15)
- Markup models over-forecast MX: ridge_m bias was -20.02 bps vs -2.41 bps for the champion. (L12, L03)

**Risks:** The markup signal is real in development and may still be worth switching to. Keeping the champion means giving up a consistent edge if the promotion window was just an unusually hard stretch. The champion's breach rate in Brazil is also high, so its risk band is not reliable there either.

**Watch next week:** Whether the markup-aware ridge's edge comes back once the recent volatile stretch leaves the hidden window, whether its risk band can be calibrated (especially the Mexico over-forecast), and whether Indian volatility and markups stay elevated.

## Ledger

Budget used: backtests 8, tunes 0, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-04-17 |
| L02 | champion-report | champion MAE last 4w 51.04, last 26w 44.52, prior 26w 62.34 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ewma all refit7 hl5: MAE 46.73 bps (+4.96% vs champion) |
| L05 | backtest | ridge[mk,cal,lag] 2y refit7 hl10: MAE 42.17 bps (-5.28% vs champion) |
| L06 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 42.16 bps (-5.3% vs champion) |
| L07 | backtest | ridge[mk,cal] 2y refit7 hl10: MAE 41.77 bps (-6.18% vs champion) |
| L08 | backtest | ridge[lag] 2y refit7 hl10: MAE 44.48 bps (-0.09% vs champion) |
| L09 | backtest | ridge[mk,cal,lag] all refit7 hl10: MAE 41.87 bps (-5.95% vs champion) |
| L10 | backtest | ridge[mk] 2y refit7 hl10: MAE 41.29 bps (-7.26% vs champion) |
| L11 | backtest | ridge[cal] 2y refit7 hl10: MAE 44.87 bps (+0.79% vs champion) |
| L12 | diagnose | diagnosis of ridge[mk] 2y refit7 hl10 |
| L13 | diagnose | diagnosis of ridge[mk,cal] 2y refit7 hl10 |
| L14 | diagnose | diagnosis of lightgbm[vol,mk,cal,lag] 2y refit7 hl10 |
| L15 | promote | ridge[mk] 2y refit7 hl10: 73.01 vs 73.76 bps, p = 0.387, failed |
| L16 | submit | accepted |

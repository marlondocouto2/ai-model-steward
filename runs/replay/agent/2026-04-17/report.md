# Weekly model review: 2026-04-17

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error fell versus the prior half-year across all three corridors, and no variant tested this week beat it in development. Volatility is elevated in IN and subdued in BR, with markups shifting in opposite directions there, and the champion runs a mild high-forecast bias in MX and BR.

## Evidence

- The champion's error over the last 26 weeks was 41.02 bps vs 57.17 bps before (-28.25%), improving in every corridor. (L02)
- Faster adaptation did not help: a 2y window with weekly refits was 3.02% worse (42.26 bps) and LightGBM with weekly refits was 2.34% worse (41.98 bps). (L05, L06)
- A shorter halflife (41.05 bps, +0.07%) and a leaner feature set without FX returns and dollar index (41.11 bps, +0.22%) were statistically indistinguishable from the champion. (L07, L08)
- A ridge model with the same features was 3.1% worse at 42.29 bps, worse in every corridor. (L09)
- The champion's bias was -14.17 bps in MX and -8.57 bps in BR, and its risk band breach rate was 0.058, inside the acceptable range. (L03, L02)

**Risks:** IN volatility sits near the top of its history and its markup has jumped, which a slowly refitted model trained on all history may track late. BR errors are dominated by a few large tail days, so a regime shift there could quickly erode the champion's lead.

**Watch next week:** Watch IN error and breach rate under the high-volatility regime, whether the MX and BR high-forecast bias persists, and whether late-week errors keep rising; if IN degrades, retest shorter windows or faster refits.

## Ledger

Budget used: backtests 5, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-04-17 |
| L02 | champion-report | champion MAE last 4w 42.37, last 26w 41.02, prior 26w 57.17 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 41.02 bps (+0.0% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit7 hl10: MAE 42.26 bps (+3.02% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 41.98 bps (+2.34% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 41.05 bps (+0.07% vs champion) |
| L08 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 41.11 bps (+0.22% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.29 bps (+3.1% vs champion) |
| L10 | submit | accepted |

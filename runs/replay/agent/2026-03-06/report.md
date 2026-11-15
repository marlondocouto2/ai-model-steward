# Weekly model review: 2026-03-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion is performing well: its development error fell sharply versus the prior period and its risk band coverage is healthy. Brazil remains the hardest corridor and the latest week saw a sharp peso move and wider Mexico markup, but no tested change to refit cadence, recency weighting, training window or model family improved on the champion beyond noise.

## Evidence

- The champion's error over the development window was 41.26 bps vs 59.23 bps in the prior period (-30.34%), an improvement, with a breach rate of 0.032. (L02)
- Brazil is the weakest corridor at 60.64 bps versus 38.67 bps for Mexico and 24.59 bps for India. (L02)
- Refitting weekly instead of monthly gave 41.24 bps vs 41.26 bps (-0.05%), a negligible difference well inside noise. (L05)
- A shorter recency halflife gave 41.27 bps (+0.02%), marginally worse. (L07)
- A one-year training window was worse at 42.45 bps (+2.88%), and a ridge model was worse at 42.09 bps (+2.01%). (L08, L09)
- LightGBM on a two-year window was worse at 43.48 bps (+5.38%), worse in every corridor. (L06)

**Risks:** The recent sharp Mexico and Brazil moves and the rising Mexico markup could signal a regime shift the long training window adapts to slowly; Brazil's error has been trending up in recent weeks; the champion carries a mild low bias in India and a mild high bias in Mexico and Brazil.

**Watch next week:** Watch whether Brazil's recent error keeps rising, whether the Mexico markup widening persists, whether the late-week error pattern grows, and whether the corridor biases drift further; if so, test faster-adapting configurations focused on Brazil.

## Ledger

Budget used: backtests 5, tunes 0, promotion tests 0. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-03-06 |
| L02 | champion-report | champion MAE last 4w 44.14, last 26w 41.26, prior 26w 59.23 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 41.26 bps (+0.0% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 41.24 bps (-0.05% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 43.48 bps (+5.38% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 41.27 bps (+0.02% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit30 hl10: MAE 42.45 bps (+2.88% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 42.09 bps (+2.01% vs champion) |
| L10 | submit | rejected: 1 error(s) |
| L11 | submit | accepted |

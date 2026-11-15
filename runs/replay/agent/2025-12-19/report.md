# Weekly model review: 2025-12-19

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error has fallen sharply versus the prior half-year, driven by MX calming down, while BR remains the hardest corridor with a tendency to over-forecast and IN volatility has climbed to the top of its multi-year range. No tested change to window, refit cadence, halflife, model family or feature set produced a consistent, meaningful improvement.

## Evidence

- The champion's error over the last 26 weeks was 45.09 bps vs 63.38 bps before (-28.86%), so it is improving, not degrading. (L02)
- BR is the weakest corridor at 66.53 bps with a bias of -11.87 bps (forecasts too high), and IN 20-day volatility is at the 99.0 percentile of its 3-year history. (L02, L03, L01)
- The best challenger, a leaner feature set, was only -0.64% vs the champion (44.8 bps vs 45.09 bps), well short of the 1% promotion threshold. (L11)
- A shorter halflife moved error by only -0.58%, with BR at 66.85 bps vs the champion's 66.53 bps and a breach rate of 0.054, so its gain is not consistent across corridors. (L08)
- Weekly refits (+0.07%), a 2y window (+4.08%), lightgbm (+2.15%), ridge (+1.22%) and ewma (+7.3%) were all worse than the champion. (L05, L06, L09, L10, L07)

**Risks:** The leaner feature set's small but corridor-consistent edge may be real and could grow; the elevated IN volatility could expose the champion's slow monthly refit and long training window if the regime shifts persistently; BR's over-forecasting bias could widen during further real depreciation.

**Watch next week:** Check whether the BR bias persists or grows, whether IN error rises with its high volatility, and whether the leaner feature set keeps its consistent edge across corridors, which would make it worth tuning and promoting.

## Ledger

Budget used: backtests 7, tunes 0, promotion tests 0. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-19 |
| L02 | champion-report | champion MAE last 4w 38.05, last 26w 45.09, prior 26w 63.38 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 45.09 bps (+0.0% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 45.12 bps (+0.07% vs champion) |
| L06 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 2y refit30 hl10: MAE 46.93 bps (+4.08% vs champion) |
| L07 | backtest | ewma all refit30 hl10: MAE 48.38 bps (+7.3% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 44.83 bps (-0.58% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 46.06 bps (+2.15% vs champion) |
| L10 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 45.64 bps (+1.22% vs champion) |
| L11 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 44.8 bps (-0.64% vs champion) |
| L12 | submit | rejected: 1 error(s) |
| L13 | submit | accepted |

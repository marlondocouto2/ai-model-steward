# Weekly model review: 2026-07-24

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error rose in the recent development period, driven by a March spike and large BR misses, with opposite-signed biases across corridors (IN forecast too low, BR and MX too high). Faster refits, shorter windows, simpler models, a different tree family and a leaner feature set all failed to beat it, so the deterioration looks like a harder market rather than a fixable config problem.

## Evidence

- The champion's error over the last 26 weeks was 52.66 bps vs 43.31 bps before (+21.59%). (L02)
- Champion bias differs in sign by corridor: IN 12.62 bps (forecasts too low) vs BR -12.73 bps and MX -7.37 bps (forecasts too high). (L03)
- Refitting weekly instead of monthly was slightly worse: 52.76 bps vs 52.66 bps (+0.19%), and also shortening the window to 1y was worse at 55.41 bps (+5.22%). (L04, L05)
- Simpler models were worse: ridge at 54.22 bps (+2.96%) and the EWMA baseline at 56.37 bps (+7.05%), the latter with a BR breach rate of 0.139. (L07, L06)
- The closest alternatives were still worse than the champion: LightGBM at 53.18 bps (+0.99%) and a lean xgboost without fx and dollar features at 52.87 bps (+0.4%), both within noise. (L08, L09)

**Risks:** If the corridor biases reflect a persistent shift in customer markups, a model that adapts its level faster could start to outperform, and keeping a long-window model would leave that gain unrealised. The champion's IN error has also been rising recently, which could signal a corridor-specific regime change.

**Watch next week:** Watch whether the IN under-forecast bias and the BR over-forecast bias persist or grow, whether markups keep falling across corridors, and whether recent-weeks IN error keeps rising; if so, test markup-focused or corridor-adaptive configs.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-24 |
| L02 | champion-report | champion MAE last 4w 50.45, last 26w 52.66, prior 26w 43.31 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 52.76 bps (+0.19% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl10: MAE 55.41 bps (+5.22% vs champion) |
| L06 | backtest | ewma all refit30 hl10: MAE 56.37 bps (+7.05% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 54.22 bps (+2.96% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 53.18 bps (+0.99% vs champion) |
| L09 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 52.87 bps (+0.4% vs champion) |
| L10 | submit | accepted |

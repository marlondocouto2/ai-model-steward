# Weekly model review: 2024-09-06

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** Error rose sharply from April onward, driven by MX and BR during a high-volatility stretch for the peso, with the worst misses clustered in early June MX. The champion under-forecasts margin in MX and BR, while IN stays calm and well forecast. None of the alternatives tested — faster adaptation, other model families, or a leaner feature set — beat the champion by more than noise.

## Evidence

- The champion's error over the recent half-year was 50.02 bps vs 52.92 bps before (-5.48%), but the last quarter alone ran at 62.97 bps. (L02)
- The champion is biased low in BR (15.26 bps) and MX (11.17 bps), and nearly unbiased in IN (-0.01 bps). (L03)
- Faster adaptation did not help: weekly refit changed error by +0.3%, a shorter half-life by +0.12%, and a 1y window by +1.4%. (L04, L05, L06)
- Other families were no better: LightGBM changed error by +0.18% and ridge by +0.88%, while an EWMA baseline was +10.92% worse. (L08, L09, L07)
- The best candidate, XGBoost without FX and dollar-index features, was only -0.46% vs the champion and not consistent across corridors: MX 69.09 bps vs 69.98 bps, but IN 10.82 bps vs 10.56 bps. (L10)

**Risks:** If the MX volatility regime persists or BR markup keeps widening, the champion's low bias could grow and a faster-adapting or bias-corrected model might start to pay off; development differences were small enough that a real improvement could be hidden in the noise.

**Watch next week:** Track MX and BR bias and error against the prior weeks, whether MX volatility comes down, and whether the BR markup jump persists; if the low bias keeps growing, test markup-focused or bias-corrected candidates.

## Ledger

Budget used: backtests 7, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-09-06 |
| L02 | champion-report | champion MAE last 4w 62.89, last 26w 50.02, prior 26w 52.92 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 50.17 bps (+0.3% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 50.08 bps (+0.12% vs champion) |
| L06 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit30 hl10: MAE 50.72 bps (+1.4% vs champion) |
| L07 | backtest | ewma all refit30 hl10: MAE 55.48 bps (+10.92% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.11 bps (+0.18% vs champion) |
| L09 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 50.46 bps (+0.88% vs champion) |
| L10 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 49.79 bps (-0.46% vs champion) |
| L11 | submit | accepted |

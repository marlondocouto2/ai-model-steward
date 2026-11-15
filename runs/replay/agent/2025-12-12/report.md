# Weekly model review: 2025-12-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** Markets were calm this period, especially in MX where volatility sits near the bottom of its multi-year range, and the champion's error kept falling relative to the prior half-year. It slightly over-forecasts margins in BR and MX, and BR remains the hardest corridor. None of the tested alternatives beat it by more than noise.

## Evidence

- The champion's error over the last 26 weeks was 45.25 bps vs 63.15 bps before (-28.35%), so it improved. (L02)
- The champion over-forecasts in BR (bias -11.9 bps) and MX (bias -7.55 bps), while IN is close to unbiased (2.22 bps). (L03)
- The best challenger, a shorter halflife, reached 44.77 bps vs the champion's 45.25 bps (-1.06%), a gain inside the range that is often luck. (L08)
- Refitting weekly (-0.2%) and a linear ridge model (0.0%) matched the champion but did not beat it. (L04, L09)
- A shorter one-year training window was worse (+5.41%), and the EWMA baseline was worse too (+6.74%). (L05, L07)

**Risks:** If volatility returns to MX or BR, the champion's long training window and slow monthly refit could adapt too slowly, and the small edge of a shorter halflife could turn out to be real. The persistent over-forecast in BR and MX could widen if markups keep falling in MX.

**Watch next week:** Check whether the BR and MX bias persists or grows, whether MX volatility rises from its lows, and whether the shorter-halflife variant keeps a consistent edge across all three corridors.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-12-12 |
| L02 | champion-report | champion MAE last 4w 40.28, last 26w 45.25, prior 26w 63.15 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 45.16 bps (-0.2% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit30 hl10: MAE 47.7 bps (+5.41% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 45.78 bps (+1.17% vs champion) |
| L07 | backtest | ewma all refit7 hl10: MAE 48.3 bps (+6.74% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 44.77 bps (-1.06% vs champion) |
| L09 | backtest | ridge[vol,mk,cal,lag] all refit7 hl10: MAE 45.25 bps (+0.0% vs champion) |
| L10 | submit | accepted |

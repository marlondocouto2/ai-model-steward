# Weekly model review: 2025-07-18

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** Overall champion error is roughly flat versus the prior half-year, but the mix shifted: the IN corridor got markedly worse as its markup widened and its volatility rose to the high end of its history, while MX improved. Every alternative tested shows the same IN deterioration, so it reflects a harder regime rather than a fault specific to the champion.

## Evidence

- The champion's error over the last 26 weeks was 63.06 bps vs 61.91 bps before (+1.86%). (L02)
- IN error got worse, 29.87 bps vs 9.23 bps in the prior 26 weeks, while MX improved, 77.35 bps vs 99.72 bps. (L02)
- IN markup widened to 69.9 bps last week from 52.3 bps over the prior four weeks. (L01)
- The best challengers were only marginally better: a lean-feature xgboost at 62.97 bps (-0.14%) and weekly refit at 63.02 bps (-0.06%), both far short of the 1% promotion threshold. (L09, L04)
- Faster adaptation did not help: a 1y window was worse at 64.55 bps (+2.36%), halflife 5 was worse at 63.59 bps (+0.84%), and LightGBM was worse at 63.84 bps (+1.24%). (L05, L07, L08)
- The simple EWMA baseline was clearly worse at 67.67 bps (+7.31%), so the champion's learned stage still adds value. (L06)

**Risks:** If the IN markup widening is a lasting structural change, an all-history training window may adapt too slowly and IN error could keep rising. The champion also carries a small negative bias in MX and BR, and the BR corridor remains the largest source of error.

**Watch next week:** Watch whether IN markup and volatility settle back or persist, IN corridor error in the champion report, the champion's breach rate staying inside the risk band, and any sign that BR error trends up.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-18 |
| L02 | champion-report | champion MAE last 4w 49.9, last 26w 63.06, prior 26w 61.91 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 63.02 bps (-0.06% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl10: MAE 64.55 bps (+2.36% vs champion) |
| L06 | backtest | ewma all refit7 hl10: MAE 67.67 bps (+7.31% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 63.59 bps (+0.84% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 63.84 bps (+1.24% vs champion) |
| L09 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 62.97 bps (-0.14% vs champion) |
| L10 | submit | accepted |

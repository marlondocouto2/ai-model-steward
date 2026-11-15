# Weekly model review: 2025-07-25

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** Volatility is calm in MX and BR while markups have widened in every corridor; the champion's overall error edged down, but the India corridor became much harder to forecast than it was a half-year ago and early-April shocks drove the worst days. No configuration change tested shows an advantage beyond noise.

## Evidence

- The champion's error over the last 26 weeks was 60.81 bps vs 62.22 bps before (-2.27%), an improvement overall. (L02)
- The IN corridor got worse: 30.74 bps over the last 26 weeks vs 9.11 bps in the prior 26 weeks, while MX improved from 97.74 bps to 73.66 bps. (L02)
- The best challengers were only marginally better than the champion: weekly refit at 60.76 bps (-0.08%) and dropping the dollar index at 60.78 bps (-0.05%), far short of the 1% promotion bar. (L04, L09)
- A shorter 1y training window was worse at 62.64 bps (+3.01%), with every corridor worse, so faster adaptation does not help. (L05)
- Other families and decay settings were also worse: LightGBM 61.08 bps (+0.44%), ridge 61.16 bps (+0.58%), halflife 5 at 61.23 bps (+0.69%). (L06, L08, L07)
- The champion shows a mild bias of -8.37 bps in BR and -6.37 bps in MX (forecasting slightly high), with a breach rate of 0.065 inside the 2-9% band. (L03, L02)

**Risks:** The India corridor's higher error may reflect a lasting regime shift the champion's long training window adapts to slowly; widening markups could keep the champion biased in BR and MX; a renewed volatility shock like early April could expose the model.

**Watch next week:** Track India corridor error and whether markups keep widening; check whether the BR and MX bias persists; revisit shorter refit or markup-focused configs if India error keeps rising.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2025-07-25 |
| L02 | champion-report | champion MAE last 4w 48.15, last 26w 60.81, prior 26w 62.22 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 60.76 bps (-0.08% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit30 hl10: MAE 62.64 bps (+3.01% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.08 bps (+0.44% vs champion) |
| L07 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 61.23 bps (+0.69% vs champion) |
| L08 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 61.16 bps (+0.58% vs champion) |
| L09 | backtest | xgboost[fx,vol,mk,cal,lag] tuned all refit30 hl10: MAE 60.78 bps (-0.05% vs champion) |
| L10 | submit | accepted |

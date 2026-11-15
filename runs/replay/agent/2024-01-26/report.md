# Weekly model review: 2024-01-26

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion is not degrading: its recent error has fallen in every corridor, with the largest gains in IN and BR as volatility there sits near multi-year lows, and its forecasts show negligible bias. No alternative window, refit cadence, halflife, family or feature set produced an improvement that is both material and consistent across corridors.

## Evidence

- The champion's error over the last 26 weeks was 52.88 bps vs 62.75 bps before (-15.73%), improving in all three corridors. (L02)
- Champion bias is small in every corridor: -1.15 bps for MX, 0.36 bps for IN and -0.7 bps for BR. (L03)
- The best challenger, weekly refit with halflife 5, scored 52.56 bps vs the champion's 52.88 bps (-0.61%), below the 1% promotion threshold, and in IN it scored 15.16 bps against the champion's 14.46 bps. (L08)
- Weekly refit alone gave only -0.38% (52.68 bps), while a 2y window (+1.0%), LightGBM (+1.85%), ridge (+1.06%) and a lean feature set (+1.76%) were all worse than the champion. (L04, L05, L06, L07, L09)

**Risks:** MX markup has widened recently and MX volatility is above its typical level, so a regime shift there could expose the champion's monthly refit cadence; conversely, the unusually calm IN and BR conditions may not persist and the champion's recent gains could partly reverse.

**Watch next week:** Watch MX error and breach rate given the wider markup, whether IN and BR volatility rises from its lows, and whether the faster-refit challengers start to pull ahead consistently across corridors.

## Ledger

Budget used: backtests 6, tunes 0, promotion tests 0. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2024-01-26 |
| L02 | champion-report | champion MAE last 4w 28.93, last 26w 52.88, prior 26w 62.75 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 52.68 bps (-0.38% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 53.41 bps (+1.0% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 53.86 bps (+1.85% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 53.44 bps (+1.06% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit7 hl5: MAE 52.56 bps (-0.61% vs champion) |
| L09 | backtest | xgboost[vol,mk,lag] all refit7 hl10: MAE 53.81 bps (+1.76% vs champion) |
| L10 | submit | rejected: 1 error(s) |
| L11 | submit | accepted |

# Weekly model review: 2026-06-12

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's error rose over the recent half-year, driven mostly by MX and a volatile March shock that hit every corridor, with BR still the hardest corridor and modest opposite-signed biases across corridors. No config change to adaptation speed, training window, feature set or model family produced a consistent, meaningful improvement, so the degradation looks regime-driven rather than a fixable model defect.

## Evidence

- The champion's error over the recent half-year was 50.62 bps vs 45.31 bps before (+11.72%), with MX worsening most at 53.68 bps vs 42.11 bps. (L02)
- The champion's error was 59.45 bps in volatile regimes vs 45.36 bps in calm ones, and peaked at 83.7 bps in March. (L03)
- The best variant, a shorter halflife, scored 50.48 bps vs the champion's 50.62 bps (-0.28%), a gain within noise that did not hold on IN (30.86 bps vs 30.5 bps). (L08)
- Refitting weekly gave 50.61 bps (-0.02%), essentially unchanged, while a one-year training window was worse at 52.11 bps (+2.94%). (L04, L05)
- Alternative families were all worse: LightGBM 51.1 bps (+0.95%), ridge 52.27 bps (+3.26%), and the EWMA baseline 54.15 bps (+6.97%). (L11, L07, L06)

**Risks:** If the recent volatility in MX and BR persists or a structural markup shift continues, the champion may keep drifting and a more adaptive config could start to pay off; the champion's MX risk band is also breaching more often than the other corridors.

**Watch next week:** Watch MX error and band breaches, the rising markup in MX and BR, IN volatility near the top of its range, and whether corridor biases persist; if a shorter-halflife or faster-refit variant pulls ahead consistently across corridors, tune and promote it.

## Ledger

Budget used: backtests 8, tunes 0, promotion tests 0. Memo submissions: 2.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-06-12 |
| L02 | champion-report | champion MAE last 4w 58.37, last 26w 50.62, prior 26w 45.31 bps |
| L03 | diagnose | diagnosis of xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10 |
| L04 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit7 hl10: MAE 50.61 bps (-0.02% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned 1y refit7 hl10: MAE 52.11 bps (+2.94% vs champion) |
| L06 | backtest | ewma all refit30 hl10: MAE 54.15 bps (+6.97% vs champion) |
| L07 | backtest | ridge[fx,vol,dxy,mk,cal,lag] 2y refit7 hl10: MAE 52.27 bps (+3.26% vs champion) |
| L08 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl5: MAE 50.48 bps (-0.28% vs champion) |
| L09 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl20: MAE 51.24 bps (+1.22% vs champion) |
| L10 | backtest | xgboost[vol,mk,cal,lag] tuned all refit30 hl10: MAE 50.78 bps (+0.32% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.1 bps (+0.95% vs champion) |
| L12 | submit | rejected: 1 error(s) |
| L13 | submit | accepted |

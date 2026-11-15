# Weekly model review: 2026-07-03

**Decision: Keep.** Champion: `xgboost[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 51.21 bps vs 43.96 bps in the prior 26 weeks (+16.49%). (L02)
- The best development candidate, lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10, scored 50.96 bps vs the champion's 51.21 bps (-0.49%). (L14)
- On the hidden window it scored 51.84 bps vs the champion's 52.76 bps (p = 0.152) and failed the promotion rule. (L15)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 11, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-07-02 |
| L02 | champion-report | champion MAE last 4w 40.1, last 26w 51.21, prior 26w 43.96 bps |
| L03 | backtest | ewma all refit30 hl10: MAE 54.78 bps (+6.97% vs champion) |
| L04 | backtest | ridge[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 52.98 bps (+3.46% vs champion) |
| L05 | backtest | xgboost[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.43 bps (+0.43% vs champion) |
| L06 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl10: MAE 51.26 bps (+0.1% vs champion) |
| L07 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 3y refit30 hl10: MAE 52.41 bps (+2.34% vs champion) |
| L08 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 2y refit30 hl10: MAE 52.7 bps (+2.91% vs champion) |
| L09 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] 1y refit30 hl10: MAE 53.85 bps (+5.16% vs champion) |
| L10 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl5: MAE 51.32 bps (+0.21% vs champion) |
| L11 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit30 hl20: MAE 51.73 bps (+1.02% vs champion) |
| L12 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] all refit7 hl10: MAE 51.51 bps (+0.59% vs champion) |
| L13 | tune | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: CV MAE 55.01 → 53.91 bps |
| L14 | backtest | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: MAE 50.96 bps (-0.49% vs champion) |
| L15 | promote | lightgbm[fx,vol,dxy,mk,cal,lag] tuned all refit30 hl10: 51.84 vs 52.76 bps, p = 0.152, failed |
| L16 | submit | accepted |

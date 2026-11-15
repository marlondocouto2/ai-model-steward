# Weekly model review: 2026-01-09

**Decision: Switch.** Champion: `ridge[mk] all refit30 hl10` (was `ewma all refit30 hl10`)

**What changed:** The champion's error has been falling, but it still under-forecasts margins in MX and does worst late in the week, which points to markup information it cannot use. A ridge model on the markup features captures that signal and beats the champion in every corridor, while calendar and lagged-residual features add nothing on top of markup.

## Evidence

- The champion's error over the last 26 weeks was 46.67 bps vs 67.6 bps before (-30.96%), with a positive MX bias of 5.37 bps. (L02, L03)
- In development, ridge on markup features scored 43.08 bps vs the champion's 46.67 bps (-7.69%), better in all three corridors: MX 43.71 bps vs 47.68 bps, IN 24.01 bps vs 27.31 bps, BR 61.43 bps vs 64.92 bps. (L10)
- Calendar features alone gave no improvement (46.86 bps, +0.41%), and adding calendar to markup was worse (43.44 bps) than markup alone, so the gain comes from the markup features. (L11, L08, L10)
- Tuning alpha did not help: the tuned config backtested at 43.12 bps (-7.61%), so the simpler untuned config was promoted. (L14, L15)
- The promotion test passed: the challenger scored 43.77 bps vs the champion's 46.71 bps (-6.29%), DM p-value 0.042, breach rate 0.05 vs the champion's 0.087. (L16)

**Risks:** The challenger over-forecasts margins in MX and BR, so a drop in markups could hurt it. Its development gain is concentrated in a few summer months rather than spread evenly, and the worst errors are still large BR spikes that no candidate fixes.

**Watch next week:** Watch the new model's bias in MX and BR, whether its error stays below the old champion's in each corridor, and the BR markup level, which has been falling.

## Ledger

Budget used: backtests 8, tunes 1, promotion tests 1. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | data-summary | market data through 2026-01-09 |
| L02 | champion-report | champion MAE last 4w 36.58, last 26w 46.67, prior 26w 67.6 bps |
| L03 | diagnose | diagnosis of ewma all refit30 hl10 |
| L04 | backtest | ridge[mk,cal,lag] all refit30 hl10: MAE 43.93 bps (-5.87% vs champion) |
| L05 | backtest | lightgbm[vol,mk,cal,lag] 2y refit7 hl10: MAE 45.65 bps (-2.19% vs champion) |
| L06 | backtest | ewma all refit7 hl10: MAE 46.67 bps (+0.0% vs champion) |
| L07 | diagnose | diagnosis of ridge[mk,cal,lag] all refit30 hl10 |
| L08 | backtest | ridge[mk,cal] all refit30 hl10: MAE 43.44 bps (-6.92% vs champion) |
| L09 | backtest | ridge[mk,cal,lag] all refit7 hl10: MAE 43.92 bps (-5.89% vs champion) |
| L10 | backtest | ridge[mk] all refit30 hl10: MAE 43.08 bps (-7.69% vs champion) |
| L11 | backtest | ridge[cal] all refit30 hl10: MAE 46.86 bps (+0.41% vs champion) |
| L12 | diagnose | diagnosis of ridge[mk,cal] all refit30 hl10 |
| L13 | diagnose | diagnosis of ridge[mk] all refit30 hl10 |
| L14 | tune | ridge[mk] tuned all refit30 hl10: CV MAE 55.93 → 53.32 bps |
| L15 | backtest | ridge[mk] tuned all refit30 hl10: MAE 43.12 bps (-7.61% vs champion) |
| L16 | promote | ridge[mk] all refit30 hl10: 43.77 vs 46.71 bps, p = 0.042, passed |
| L17 | submit | accepted |

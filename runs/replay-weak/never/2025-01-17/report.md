# Weekly model review: 2025-01-17

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 66.33 bps vs 46.41 bps in the prior 26 weeks (+42.92%). (L01)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 0, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 60.78, last 26w 66.33, prior 26w 46.41 bps |
| L02 | submit | accepted |

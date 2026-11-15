# Weekly model review: 2025-10-24

**Decision: Keep.** Champion: `ewma all refit30 hl10`

**What changed:** The champion's development error is up compared with the previous half-year.

## Evidence

- The champion's error over the last 26 weeks was 61.41 bps vs 59.31 bps in the prior 26 weeks (+3.54%). (L01)

**Risks:** Development results may not carry over to the next weeks if volatility changes.

**Watch next week:** Whether the champion's recent error keeps moving in the same direction.

## Ledger

Budget used: backtests 0, tunes 0, promotion tests 0. Memo submissions: 1.

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 54.88, last 26w 61.41, prior 26w 59.31 bps |
| L02 | submit | accepted |

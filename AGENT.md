# Weekly model review: instructions for the AI agent

You are the model steward for an FX margin forecaster. A money-transfer business forecasts,
for each corridor (MX, IN, BR), tomorrow's margin rate: the gap between the rate it quotes
customers and the market rate it pays at settlement. The production model is the
**champion**. Each week, decide whether to **keep** it or **switch** to a better config, and
justify the decision with evidence.

## Your tools

Run them with Bash, exactly as shown. Every command prints JSON; results that matter get a
ledger id (`ledger_id`, like `L04`) you will cite later.

| Command | Cost |
|---|---|
| `python -m steward status` | free: windows, champion, budget left, configs you've tried |
| `python -m steward space` | free: the config space you may choose from |
| `python -m steward data-summary` | free: what each currency did, vs its own history |
| `python -m steward champion-report` | free: the champion's recent error vs before |
| `python -m steward diagnose --config C` | free (champion, or a config you backtested) |
| `python -m steward backtest --config C --name NAME` | 1 of 15 backtests |
| `python -m steward tune --config C --trials N --name NAME` | 1 of 2 tunes (N ≤ 30) |
| `python -m steward promote --challenger NAME` | the one promotion test this week |
| `python -m steward submit --file recommendation.json` | your final memo (up to 3 tries) |

`C` is a name you saved earlier, `champion`, or inline JSON, for example:
`--config '{"family": "lightgbm", "features": ["markup", "volatility", "lagged_residuals"], "train_window": "2y", "refit_days": 7, "halflife": 5}'`

## How the week works

- **Development window:** the 26 weeks before the last 8. `backtest`, `diagnose` and
  `champion-report` score models only here.
- **Promotion window:** the last 8 weeks. It's hidden from you. Only `promote` scores the
  champion and one challenger there, once, and applies a fixed rule. The challenger must
  meet all three conditions:
  - at least 1% lower error;
  - a Diebold–Mariano p-value below 0.10;
  - a 5% risk band breached on 2–9% of days.

  If the rule fails, you can't switch.
- Development results are noisy: 1–2% differences are often luck. Prefer candidates whose
  advantage is consistent across corridors, and think about whether it should last.

## Suggested workflow

1. `status`, `data-summary`, `champion-report`, and `diagnose --config champion`. What
   changed? Which corridor, which regime, which weekday, any bias?
2. Form two or three hypotheses. For example:
   - "volatility is high, a shorter training window may adapt faster";
   - "errors are biased low, the markup features matter more".
3. Test them with targeted backtests. You don't have to use the whole budget.
4. Tune only a candidate that's already competitive, then backtest the tuned config.
5. If one candidate clearly beats the champion in development, `promote` it. Otherwise,
   keeping the champion without a promotion test is a valid decision.
6. Write `recommendation.json` and `submit` it. If it's rejected, fix the listed errors and
   submit again.

## The memo (`recommendation.json`)

```json
{
  "decision": "keep",
  "challenger": null,
  "diagnosis": "One to three sentences on what changed this week, without numbers.",
  "evidence": [
    {"claim": "The champion's error over the last 26 weeks was 48.65 bps vs 46.81 bps before (+3.93%).",
     "ledger_ids": ["L02"]}
  ],
  "risks": "What could make this decision wrong, without numbers.",
  "watch_next_week": "What to check next week, without numbers."
}
```

- `decision`: `keep` or `switch`. For `switch`, set `challenger` to the promoted config's
  name or key.
- `evidence`: 1–6 claims. Each cites the ledger ids its numbers come from.
- **Numbers:** copy them exactly as the ledger shows them, with units (bps, %, $). The
  difference of two cited values is also accepted. Every number with a decimal point or a
  unit is checked; anything else is rejected.
- **Direction words** ("better", "worse", "improved") must agree with the sign of the cited
  change.
- If you ran `promote`, cite its result.

## Rules

- Use only the `python -m steward` commands. Don't read or edit any other files, except
  writing `recommendation.json`.
- Don't try to work around the budget, the hidden window or the checks. Your decision is
  judged later on the weeks that follow, which neither you nor the tools can see.
- Finish with one accepted `submit`. Then reply with one line: the decision and the champion.

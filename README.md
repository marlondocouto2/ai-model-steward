# AI model steward

Every week, new FX data arrives and the production margin model may no longer be the best
choice. This project gives that weekly review to an **AI agent**:
- it checks how the current model (the "champion") is doing and diagnoses what changed;
- it tries and tunes challengers within a fixed budget;
- it opens a pull request recommending to **keep** or **switch**, with a memo whose every
  number is checked against a ledger of the tool results.

The model it manages is the
[two-stage FX margin forecaster](https://github.com/marlondocouto2/fx-margin-forecaster)
(Project 3). The AI decides *what to try and why*. Plain Python computes every number and
enforces the rules, and a human merges.

The question: **with the same budget, does an AI agent choose better models than plain
automation, or than never retraining at all?**

## Headline result (non-AI baselines, 136 replayed weeks)

![Change in future error vs never retraining](reports/figures/results.png)

Before any AI, the replay already gives two answers:

- **Project 3's tuned XGBoost is hard to beat.** Every week, the scripted playbook and Optuna
  automation each found a challenger that looked better in development. Accepted blindly,
  those challengers would have **raised** error over the following 12 weeks: by 1.07% for the
  playbook and 0.35% for automation.
- **The promotion rule is what protects the business.** It blocked 100 of the playbook's 101
  proposals and 115 of automation's 126. With the rule, both end up level with never
  retraining (0.00% and +0.05%).
  - Automation's 11 switches split 5 better and 6 worse.
  - In the volatile summer of 2024, blocked proposals would have added up to 9 bps of error.

The AI agent runs on 16 sampled weeks (see [The AI agent](#the-ai-agent)). The baselines'
results on those same weeks are in `reports/results_agent_weeks.csv`, ready for the comparison.

![Week by week](reports/figures/timeline.png)

*Each dot is one week's proposed challenger: its error over the next 12 weeks minus the
champion's. Below zero is better. Circled dots are weeks where the rule allowed a switch.*

## How a week works

```
status -> data-summary -> champion-report -> diagnose -> backtest x <=15 -> tune x <=2
       -> promote x <=1 (hidden window, fixed rule) -> submit memo (checked) -> pull request
```

| Guardrail | What it does |
|---|---|
| **Config space** | The agent can only choose among 4 model families (EWMA only, + Ridge, + XGBoost, + LightGBM), 6 feature groups, 4 training windows, refits every 7 or 30 days, 3 EWMA half-lives, and hyperparameters within fixed ranges (`steward/space.py`) |
| **Hidden window** | Model errors from the last 8 weeks are hidden. Development tools only score the 26 weeks before them, so the final test can't be overfit |
| **Budget** | 15 backtests, 2 tunes and 1 promotion test per week, enforced by the tools |
| **Promotion rule** | A challenger replaces the champion only if, on the hidden window, all three hold: its error is at least 1% lower; a one-sided Diebold–Mariano test (Newey–West variance, Harvey–Leybourne–Newbold correction) gives p < 0.10; and its 5% margin-at-risk band is breached on 2–9% of days |
| **Memo checks** | Every number must match a value in the cited ledger entries, cited ids must exist, "better/worse" must match the sign, and a switch needs a passed promotion test. After 3 failed tries the week is escalated, and the champion stays |
| **Pull request** | The agent proposes; CI checks that its PR only touches the champion, reports, runs and data; a human merges |

### A sample memo

From the replay, week of 2025-06-13 (Optuna automation). The full ledger is in
[`runs/replay/automation/2025-06-13/report.md`](runs/replay/automation/2025-06-13/report.md).

> **Decision: Switch.** Champion: `xgboost[fx,mk,lag] tuned all refit7 hl20`
>
> - The champion's error over the last 26 weeks was 63.14 bps vs 61.25 bps in the prior 26 weeks (+3.09%). (L01)
> - The best development candidate, xgboost[fx,mk,lag] tuned all refit7 hl20, scored 62.87 bps vs the champion's 63.14 bps (-0.43%). (L16)
> - On the hidden window it scored 43.61 bps vs the champion's 44.11 bps (p = 0.093) and passed the promotion rule. (L17)

| Id | Command | Result |
|---|---|---|
| L01 | champion-report | champion MAE last 4w 100.75, last 26w 63.14, prior 26w 61.25 bps |
| L16 | backtest | xgboost[fx,mk,lag] tuned all refit7 hl20: MAE 62.87 bps (-0.43% vs champion) |
| L17 | promote | xgboost[fx,mk,lag] tuned all refit7 hl20: 43.61 vs 44.11 bps, p = 0.093, passed |

Over the next 12 weeks, this switch lowered error from 45.87 to 45.05 bps.

## Data

- **Real:** daily FX rates from FRED (Mexican peso, Indian rupee, Brazilian real, and the broad
  dollar index), 2016 to November 2026, committed as a snapshot in `data/fred/`. FRED
  publishes them weekly, which sets the review's cadence.
- **Simulated:** the business layer from Project 3: a markup that reacts to volatility,
  settlement one or two business days later, and volumes from the Project 2 generator. It's
  simulated on a fixed calendar, so new data never changes past weeks. See `data/README.md`.

## Approach

- **Tools as a command-line interface** (`python -m steward ...`). Each prints JSON and writes
  its result to the week's ledger (`runs/<week>/ledger.jsonl`) with an id the memo must cite.
- **Interchangeable "brains"** use the same tools, budget and rule:
  - `never`: never retrain.
  - `scripted`: a fixed playbook (family → training window → half-life → refit frequency → tune).
  - `automation`: Optuna TPE over the whole config space, then tune the winner.
  - **The AI agent:** Claude Code following [`AGENT.md`](AGENT.md).
- **Replay:** each Friday from January 2024 to August 2026 is replayed from the same starting
  champion (Project 3's tuned XGBoost). The chosen model is then scored on the 12 weeks
  after the cutoff, which no tool could see.
- **The model code is reused, not copied.** Project 3 is installed from GitHub at a pinned
  commit; this repo adds feature-group selection, training windows, half-lives and the
  margin-at-risk band per config.

## Evaluation

Error of the chosen model over the 12 weeks after each cutoff (1 day ahead, all corridors),
averaged over 136 weeks (`reports/results.csv`). The dollar figure is the mean absolute error
of the daily USD margin per corridor.

| Method | Switches | Promotion tests | Future MAE (bps) | vs never | Future MAE (USD/day) | If every proposal were accepted (bps) |
|---|---|---|---|---|---|---|
| Never retrain | 0 | 0 | 52.83 | – | 375,952 | 52.83 |
| Scripted playbook | 1 | 101 | 52.83 | 0.00% | 375,958 | 53.39 (+1.07%) |
| Optuna automation | 11 | 126 | 52.85 | +0.05% | 376,136 | 53.01 (+0.35%) |

The memo's first-try pass rate was 100% for all three. That's expected, since their memos are
templated from the ledger; it becomes a real measure with the AI agent.

## The AI agent

The agent is [Claude Code](https://code.claude.com/docs) running headless with
[`AGENT.md`](AGENT.md) as its instructions.
- It may only run `python -m steward` commands and write `recommendation.json`.
- It runs on an existing Claude plan, so there's no API bill: **this project costs nothing to
  run.**
- Replayed weeks run in a sandbox whose FRED data stops at the cutoff, so it can't see later
  prices or other weeks' results.

The agent is evaluated on 16 weeks sampled evenly from calm, normal and volatile markets
(`reports/agent_weeks.txt`), a few at a time:

```bash
scripts/agent_week.sh 2025-07-18          # one replayed week, in a sandbox
python scripts/replay.py --score-only     # score it and update the results
```

Live, once a week after FRED's Monday release, `scripts/agent_week.sh` with no argument runs
this week's review and opens a pull request.

## How to run

```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
python scripts/run_week.py --brain scripted --cutoff 2025-03-07   # one week, no AI (~30 s)
python scripts/replay.py                                          # all baselines, all weeks (~3 h on 8 cores)
```

`pytest` runs the guardrail tests:
- corrupting the hidden window's data changes nothing the agent can see;
- the budget is enforced;
- golden cases for the promotion rule;
- the memo checks catch planted errors;
- the scripted brain runs end to end.

On macOS, XGBoost and LightGBM need OpenMP: `brew install libomp`.

## What I'd do next

- Run the AI agent on the 16 sampled weeks and compare it on the same weeks.
- Let the agent propose new features as code, reviewed in the pull request, beyond the fixed
  config space.
- Test a longer hidden window or a sequential test, since 8 weeks gives the
  Diebold–Mariano test little power.
- Chain the replay week to week (each week's champion carries over) to measure cumulative
  drift.

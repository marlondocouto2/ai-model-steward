"""Guardrail tests: config space, leakage and hidden windows, budget, promotion rule, memo checks."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
from pydantic import ValidationError

from steward import agents, backtest, memo, rule, tools
from steward.data import dataset
from steward.run import BudgetExceeded, Run
from steward.settings import ROOT, SETTINGS
from steward.space import ALL_GROUPS, ModelConfig, load_config

CUTOFF = pd.Timestamp("2021-06-04")
RIDGE = ModelConfig(family="ridge", features=("markup", "lagged_residuals"), train_window="2y")


@pytest.fixture
def run(tmp_path) -> Run:
    return Run.start(CUTOFF, load_config(ROOT / "configs" / "initial_champion.json"),
                     path=tmp_path / "run", mode="replay")


# ---------------------------------------------------------------- config space
def test_config_space_rejects_configs_outside_it():
    with pytest.raises(ValidationError):
        ModelConfig(family="ewma", features=("markup",))
    with pytest.raises(ValidationError):
        ModelConfig(family="xgboost")  # needs a feature group
    with pytest.raises(ValidationError):
        ModelConfig(family="xgboost", features=ALL_GROUPS, params={"max_depth": 12})
    with pytest.raises(ValidationError):
        ModelConfig(family="ridge", features=ALL_GROUPS, params={"learning_rate": 0.1})
    with pytest.raises(ValidationError):
        ModelConfig(family="ridge", features=("markup",), train_window="5y")


def test_config_key_is_stable_and_order_free():
    a = ModelConfig(family="ridge", features=("markup", "calendar"))
    b = load_config('{"family": "ridge", "features": ["calendar", "markup", "markup"]}')
    assert a == b and a.key() == b.key()
    assert a.key() != a.model_copy(update={"halflife": 5}).key()


# ---------------------------------------------------------------- leakage and hidden windows
def test_walk_forward_never_trains_or_scores_on_unsettled_margins(monkeypatch):
    seen = []
    orig = backtest.Candidate.fit

    def spy(self, train):
        seen.append(train["settle_date"].max())
        return orig(self, train)

    monkeypatch.setattr(backtest.Candidate, "fit", spy)
    start, until = pd.Timestamp("2020-01-01"), pd.Timestamp("2020-04-01")
    preds = backtest.walk_forward(RIDGE, start, until, visible_until=until)
    cuts = pd.date_range(start, until, freq="30D", inclusive="left")
    assert all(s < c for s, c in zip(seen, cuts))
    assert preds["settle_date"].max() < until


def _corrupt_after(data: pd.DataFrame, when: pd.Timestamp) -> pd.DataFrame:
    bad = data.copy()
    late = bad["settle_date"] >= when
    bad.loc[late, ["margin_rate", "resid"]] = 1.0  # absurd margins
    return bad


def test_development_tools_cant_see_the_promotion_window(run, monkeypatch):
    """Corrupting every margin that settles in the hidden window changes nothing the agent sees."""
    before = tools.backtest(run, RIDGE, "a")["result"]["mae_bps"]
    clean = dataset(RIDGE.halflife)
    monkeypatch.setattr(backtest, "dataset", lambda hl: _corrupt_after(dataset(hl), run.dev_end))
    for p in (run.path / "preds").glob("*.pkl"):
        p.unlink()
    after = tools.backtest(run, RIDGE, "b")["result"]["mae_bps"]
    assert before == after
    assert len(clean) == len(dataset(RIDGE.halflife))


def test_promote_sees_the_promotion_window_but_not_beyond(run, monkeypatch):
    tools.backtest(run, RIDGE, "ridge")
    monkeypatch.setattr(backtest, "dataset", lambda hl: _corrupt_after(dataset(hl), run.cutoff))
    out = tools.promote(run, "ridge")["result"]
    assert out["champion_mae_bps"] < 1000 and out["challenger_mae_bps"] < 1000


# ---------------------------------------------------------------- budget
def test_budget_is_enforced(run):
    for _ in range(dict(SETTINGS.budget)["promote"]):
        run.spend("promote")
    with pytest.raises(BudgetExceeded):
        run.spend("promote")


def test_promote_requires_a_backtested_challenger(run):
    with pytest.raises(ValueError, match="backtest"):
        tools.promote(run, RIDGE)


# ---------------------------------------------------------------- promotion rule (golden cases)
def test_rule_golden_cases():
    assert rule.evaluate(50.0, 48.0, 0.01, 0.05)["passed"]                 # clear win
    r = rule.evaluate(50.0, 48.0, 0.30, 0.05)                              # not significant
    assert not r["passed"] and not r["checks"]["significance"]
    r = rule.evaluate(50.0, 49.8, 0.01, 0.05)                              # too small
    assert not r["passed"] and not r["checks"]["improvement"]
    r = rule.evaluate(50.0, 45.0, 0.01, 0.15)                              # band too loose
    assert not r["passed"] and not r["checks"]["band"]


def test_diebold_mariano():
    rng = np.random.default_rng(0)
    champ = pd.Series(np.abs(rng.normal(0, 1, 120)))
    assert rule.diebold_mariano(champ, champ * 0.7)[1] < 0.01       # clearly better
    assert rule.diebold_mariano(champ, champ * 1.3)[1] > 0.99       # clearly worse
    noise = pd.Series(np.abs(rng.normal(0, 1, 120)))
    assert 0.05 < rule.diebold_mariano(champ, noise)[1] < 0.95       # no real difference


# ---------------------------------------------------------------- memo checks
def _fake_ledger(run: Run, passed: bool = False) -> None:
    run.log("champion-report", {}, {"mae_bps": {"last_26w": 48.65, "prior_26w": 46.81},
                                    "change_last_26w_vs_prior_pct": 3.93})
    run.log("backtest", {}, {"name": "ridge", "config_key": RIDGE.key(), "label": RIDGE.label(),
                             "mae_bps": 47.9, "champion_mae_bps": 48.65, "mae_change_vs_champion_pct": -1.54})
    run.log("promote", {}, {"challenger_mae_bps": 50.1, "champion_mae_bps": 51.3, "dm_p_value": 0.04,
                            "passed": passed})
    run.update(promotion={"config": RIDGE.model_dump(mode="json"), "passed": passed})


def _memo(**over) -> dict:
    rec = {"decision": "keep", "challenger": None, "diagnosis": "Errors rose in India.",
           "evidence": [{"claim": "Champion error was 48.65 bps, up 3.93% from 46.81 bps.", "ledger_ids": ["L01"]},
                        {"claim": "Ridge was better in development: 47.9 vs 48.65 bps (-1.54%).", "ledger_ids": ["L02"]},
                        {"claim": "On the hidden window: 50.1 vs 51.3 bps, p = 0.04.", "ledger_ids": ["L03"]}],
           "risks": "Volatility.", "watch_next_week": "India."}
    rec.update(over)
    return rec


def test_memo_accepts_a_correct_memo(run):
    _fake_ledger(run)
    assert memo.check(memo.Recommendation(**_memo()), run) == []


@pytest.mark.parametrize("claim, ids, expected", [
    ("Champion error was 48.9 bps.", ["L01"], "doesn't match"),                         # wrong number
    ("Ridge was worse in development (-1.54%).", ["L02"], "says worse"),                # wrong direction
    ("Champion error improved to 48.65 bps (+3.93%).", ["L01"], "says better"),         # wrong direction
    ("Champion error was 48.65 bps.", ["L09"], "don't exist"),                          # missing id
    ("Error was $1,200 per day.", ["L01"], "doesn't match"),                            # invented dollars
])
def test_memo_catches_planted_errors(run, claim, ids, expected):
    _fake_ledger(run)
    rec = _memo(evidence=[{"claim": claim, "ledger_ids": ids},
                          {"claim": "Hidden window p = 0.04.", "ledger_ids": ["L03"]}])
    errors = memo.check(memo.Recommendation(**rec), run)
    assert any(expected in e for e in errors), errors


def test_memo_blocks_switch_without_a_passed_promotion(run):
    _fake_ledger(run, passed=False)
    errors = memo.check(memo.Recommendation(**_memo(decision="switch", challenger=RIDGE.key())), run)
    assert any("blocked" in e for e in errors)
    run2 = Run.start(CUTOFF, RIDGE, path=run.path.parent / "r2", mode="replay")
    errors = memo.check(memo.Recommendation(**_memo(decision="switch", challenger=RIDGE.key(),
                                                    evidence=[{"claim": "x", "ledger_ids": ["L01"]}])), run2)
    assert any("ledger ids" in e or "promote" in e for e in errors)


def test_memo_numbers_ignore_labels_dates_and_counts():
    nums = [w for w, _, _ in memo.metric_numbers(
        "xgboost hl10 refit30 on 2y, last 4 weeks to 2025-03-07, L03: 1.5% and 49.11 bps, $1,234, 0.04")]
    assert nums == ["1.5%", "49.11 bps", "$1,234", "0.04"]


def test_three_failed_memos_escalate(run):
    _fake_ledger(run)
    bad = _memo(evidence=[{"claim": "Error was 99.9 bps.", "ledger_ids": ["L01"]}])
    for _ in range(2):
        assert memo.submit(run, bad)["accepted"] is False
    out = memo.submit(run, bad)
    assert out["escalated"] and run.state["status"] == "escalated"
    with pytest.raises(RuntimeError):
        run.spend("backtest")


# ---------------------------------------------------------------- end to end
def test_scripted_agent_runs_end_to_end(run):
    out = agents.scripted(run)
    assert out["accepted"] and run.state["status"] == "submitted"
    assert (run.path / "report.md").exists()
    used = run.state["used"]
    assert used["backtest"] <= 15 and used["tune"] <= 2

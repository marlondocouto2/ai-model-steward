"""Replay the weekly review on past weeks and score every decision on the weeks that followed.

    python scripts/replay.py                         # all non-AI methods, every week (parallel)
    python scripts/replay.py --methods scripted --weeks 2025-03-07 2025-06-13
    python scripts/replay.py --sample                # print the weeks sampled for the AI agent
    python scripts/replay.py --score-only            # (re)score finished weeks, incl. the agent's
    python scripts/replay.py --scenario weak         # start from a weak champion (EWMA only), sampled weeks

Writes runs/replay/<method>/<week>/ (ledger, memo, score) and, from all scored weeks,
reports/replay_weeks.csv, reports/results.csv and reports/results_agent_weeks.csv.
The weak scenario writes runs/replay-weak/ and reports/weak/ instead.
Weeks already finished are skipped, so an interrupted replay can simply be restarted.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd  # noqa: E402

from steward import plots, replay  # noqa: E402
from steward.agents import BRAINS  # noqa: E402
from steward.run import Run  # noqa: E402
from steward.settings import SETTINGS  # noqa: E402

AGENT_WEEKS = SETTINGS.reports_dir / "agent_weeks.txt"


def _one(method: str, week: str, scenario: str) -> str:
    replay.run_week(method, pd.Timestamp(week), BRAINS[method], scenario)
    return f"{method} {week}"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--methods", nargs="+", default=["never", "scripted", "automation"], choices=list(BRAINS))
    p.add_argument("--weeks", nargs="+")
    p.add_argument("--jobs", type=int, default=os.cpu_count())
    p.add_argument("--sample", action="store_true", help="write and print the agent's sampled weeks")
    p.add_argument("--score-only", action="store_true")
    p.add_argument("--scenario", default="strong", choices=list(replay.SCENARIOS))
    args = p.parse_args()
    if args.scenario != "strong":
        return weak(args)

    if args.sample:
        weeks = replay.sample_weeks()
        AGENT_WEEKS.parent.mkdir(parents=True, exist_ok=True)
        AGENT_WEEKS.write_text("\n".join(weeks) + "\n")
        print("\n".join(weeks))
        return

    replay.warm_cache()
    if args.score_only:
        for path in sorted(replay.REPLAY_DIR.glob("*/*/state.json")):
            run = Run(path.parent)
            if run.state["status"] != "open":
                replay.score_week(run, path.parent.parent.name)
    else:
        weeks = args.weeks or [f"{w:%Y-%m-%d}" for w in replay.replay_weeks()]
        jobs = [(m, w) for w in weeks for m in args.methods]
        print(f"Replaying {len(weeks)} weeks x {len(args.methods)} methods on {args.jobs} processes", flush=True)
        t0 = time.time()
        with ProcessPoolExecutor(args.jobs) as pool:
            futures = [pool.submit(_one, m, w, "strong") for m, w in jobs]
            for i, f in enumerate(as_completed(futures), 1):
                f.result()
                if i % 20 == 0 or i == len(jobs):
                    print(f"  {i}/{len(jobs)} done, {time.time() - t0:.0f}s", flush=True)

    weeks_df = replay.collect()
    out = SETTINGS.reports_dir
    weeks_df.to_csv(out / "replay_weeks.csv", index=False)
    summary = replay.summarize(weeks_df)
    summary.to_csv(out / "results.csv", index=False)
    print("\nAll replayed weeks:\n" + summary.to_string(index=False))
    figs = out / "figures"
    figs.mkdir(parents=True, exist_ok=True)
    base = summary[summary["method"] != "agent"].reset_index(drop=True)
    plots.plot_results(base, figs / "results.png",
                       f"Lower is better. {base['weeks'].max()} replayed weeks, January 2024 to August 2026")
    plots.plot_timeline(weeks_df, figs / "timeline.png")
    if AGENT_WEEKS.exists():
        sample = AGENT_WEEKS.read_text().split()
        on = replay.summarize(weeks_df, sample)
        on.to_csv(out / "results_agent_weeks.csv", index=False)
        print(f"\nOn the {len(sample)} weeks sampled for the AI agent:\n" + on.to_string(index=False))
        if "agent" in set(on["method"]):
            plots.plot_results(on, figs / "results_agent_weeks.png",
                               f"Lower is better. The {len(sample)} weeks sampled for the AI agent")


def weak(args) -> None:
    """The weak-champion scenario, on the agent's sampled weeks."""
    replay_dir = replay.SCENARIOS[args.scenario][1]
    replay.warm_cache()
    weeks = args.weeks or AGENT_WEEKS.read_text().split()
    if args.score_only:
        for path in sorted(replay_dir.glob("*/*/state.json")):
            run = Run(path.parent)
            if run.state["status"] != "open":
                replay.score_week(run, path.parent.parent.name)
    else:
        jobs = [(m, w) for w in weeks for m in args.methods]
        print(f"Scenario {args.scenario}: {len(weeks)} weeks x {len(args.methods)} methods", flush=True)
        with ProcessPoolExecutor(args.jobs) as pool:
            for f in as_completed([pool.submit(_one, m, w, args.scenario) for m, w in jobs]):
                f.result()
    out = SETTINGS.reports_dir / args.scenario
    (out / "figures").mkdir(parents=True, exist_ok=True)
    weeks_df = replay.collect(args.scenario)
    weeks_df.to_csv(out / "replay_weeks.csv", index=False)
    summary = replay.summarize(weeks_df, weeks)
    summary.to_csv(out / "results.csv", index=False)
    print(summary.to_string(index=False))
    plots.plot_results(summary, out / "figures" / "results.png",
                       f"Lower is better. Starting from a weak champion (EWMA only), {len(weeks)} sampled weeks")


if __name__ == "__main__":
    main()

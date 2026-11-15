"""Command-line tools for the weekly review. Every command prints JSON.

    python -m steward start [--cutoff YYYY-MM-DD]   open this week's run (default: latest data)
    python -m steward status                        windows, champion, budget left, configs tried
    python -m steward space                         the config space the agent may choose from
    python -m steward data-summary                  what the market did, per corridor
    python -m steward champion-report               the champion's recent error vs before
    python -m steward backtest --config C [--name N]   development backtest (costs 1 of 15)
    python -m steward diagnose --config C           where a backtested config goes wrong
    python -m steward tune --config C [--trials N]  hyperparameter search (costs 1 of 2)
    python -m steward promote --challenger C        hidden-window test and rule (once a week)
    python -m steward submit --file recommendation.json
    python -m steward refresh-data                  download the latest FRED snapshot

C is a saved config name from this week (see `status`), "champion", a JSON file path, or
inline JSON such as '{"family": "ridge", "features": ["markup", "volatility"]}'.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")

import pandas as pd  # noqa: E402

from . import memo, tools  # noqa: E402
from .data import last_date, refresh_fred  # noqa: E402
from .run import Run  # noqa: E402
from .settings import SETTINGS  # noqa: E402
from .space import load_config  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="steward", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--cutoff")
    s.add_argument("--champion", default=str(SETTINGS.champion_file))
    for name in ("status", "space", "data-summary", "champion-report", "refresh-data"):
        sub.add_parser(name)
    b = sub.add_parser("backtest")
    b.add_argument("--config", required=True)
    b.add_argument("--name")
    d = sub.add_parser("diagnose")
    d.add_argument("--config", required=True)
    t = sub.add_parser("tune")
    t.add_argument("--config", required=True)
    t.add_argument("--trials", type=int, default=20)
    t.add_argument("--name")
    pr = sub.add_parser("promote")
    pr.add_argument("--challenger", required=True)
    sm = sub.add_parser("submit")
    sm.add_argument("--file", required=True)
    args = p.parse_args(argv)

    try:
        if args.cmd == "refresh-data":
            out = {"data_through": f"{refresh_fred():%Y-%m-%d}"}
        elif args.cmd == "start":
            cutoff = pd.Timestamp(args.cutoff) if args.cutoff else last_date()
            if cutoff > last_date():
                raise ValueError(f"no data after {last_date():%Y-%m-%d}")
            run = Run.start(cutoff, load_config(args.champion))
            SETTINGS.runs_dir.mkdir(parents=True, exist_ok=True)
            (SETTINGS.runs_dir / "CURRENT").write_text(run.path.name + "\n")
            out = tools.status(run)
        else:
            run = Run.active()
            fn = {"status": tools.status, "space": tools.space, "data-summary": tools.data_summary,
                  "champion-report": tools.champion_report}.get(args.cmd)
            if fn:
                out = fn(run)
            elif args.cmd == "backtest":
                out = tools.backtest(run, args.config, args.name)
            elif args.cmd == "diagnose":
                out = tools.diagnose(run, args.config)
            elif args.cmd == "tune":
                out = tools.tune(run, args.config, args.trials, args.name)
            elif args.cmd == "promote":
                out = tools.promote(run, args.challenger)
            else:
                out = memo.submit(run, args.file)
    except Exception as e:  # report every failure as JSON so the agent can read it
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    if isinstance(out, dict) and {"id", "result"} <= set(out):
        out = {"ledger_id": out["id"], **out["result"]}
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

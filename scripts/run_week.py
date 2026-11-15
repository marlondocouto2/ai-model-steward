"""Run one week's review with a non-AI brain (no API key, no AI). Used in CI as the dry run.

    python scripts/run_week.py --brain scripted --cutoff 2025-03-07
    python scripts/run_week.py --brain scripted               # latest data, a throwaway run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd  # noqa: E402

from steward.agents import BRAINS  # noqa: E402
from steward.data import last_date  # noqa: E402
from steward.replay import INITIAL_CHAMPION  # noqa: E402
from steward.run import Run  # noqa: E402
from steward.space import load_config  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--brain", default="scripted", choices=list(BRAINS))
    p.add_argument("--cutoff")
    args = p.parse_args()
    cutoff = pd.Timestamp(args.cutoff) if args.cutoff else last_date()
    path = Path(tempfile.mkdtemp()) / f"{cutoff:%Y-%m-%d}"
    run = Run.start(cutoff, load_config(INITIAL_CHAMPION), path=path, mode="replay")
    out = BRAINS[args.brain](run)
    print(json.dumps(out, indent=1))
    print((path / "report.md").read_text())
    if not out.get("accepted"):
        sys.exit(1)


if __name__ == "__main__":
    main()

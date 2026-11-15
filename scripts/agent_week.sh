#!/usr/bin/env bash
# Run the AI agent (Claude Code, headless, on your existing plan) for one week.
#
#   scripts/agent_week.sh                 # live: this week's review, then open a pull request
#   scripts/agent_week.sh 2025-03-07      # replay: a past week, inside a sandbox
#
# Replay sandbox: a temporary copy of the code with FRED data cut at the cutoff, so the agent
# can't see later prices or other weeks' results. The finished run is copied back to
# runs/replay/agent/<week>/ and scored with `python scripts/replay.py --score-only`.
#
# Needs the `claude` CLI (Claude Code), signed in. No API key is used or needed.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PY="$REPO/.venv/bin/python"
CUTOFF="${1:-}"
PROMPT="Do this week's model review. Follow AGENT.md exactly. Start by reading it."
TOOLS=(--allowedTools "Read(AGENT.md)" "Bash(python -m steward:*)" "Edit(recommendation.json)"
       --disallowedTools "WebFetch" "WebSearch" --max-turns 60)

if [[ -z "$CUTOFF" ]]; then
  # ---------------------------------------------------------------- live week
  cd "$REPO"
  export PYTHONPATH="$REPO/src" PATH="$REPO/.venv/bin:$PATH"
  python -m steward refresh-data
  WEEK="$(python -m steward start | "$PY" -c 'import json,sys; print(json.load(sys.stdin)["cutoff"])')"
  claude -p "$PROMPT" "${TOOLS[@]}" | tee "runs/$WEEK/agent_transcript.txt"
  rm -f recommendation.json
  git switch -c "review-$WEEK"
  git add champion.json "reports/weekly/$WEEK.md" "runs/$WEEK" data/fred
  git commit -m "Weekly model review $WEEK"
  git push -u origin "review-$WEEK"
  gh pr create --title "Weekly model review $WEEK" --body-file "reports/weekly/$WEEK.md"
else
  # ---------------------------------------------------------------- replay week (sandbox)
  SANDBOX="$(mktemp -d)/steward"
  mkdir -p "$SANDBOX/data/fred"
  cp -R "$REPO/src" "$REPO/configs" "$REPO/AGENT.md" "$SANDBOX/"
  for f in "$REPO"/data/fred/*.csv; do
    awk -F, -v c="$CUTOFF" 'NR == 1 || $1 <= c' "$f" > "$SANDBOX/data/fred/$(basename "$f")"
  done
  cd "$SANDBOX"
  export PYTHONPATH="$SANDBOX/src" PATH="$REPO/.venv/bin:$PATH" STEWARD_RUN="$SANDBOX/run"
  "$PY" - "$CUTOFF" <<'EOF'
import sys
import pandas as pd
from steward.run import Run
from steward.space import load_config
Run.start(pd.Timestamp(sys.argv[1]), load_config("configs/initial_champion.json"), path=__import__("pathlib").Path("run"), mode="replay")
EOF
  claude -p "$PROMPT" "${TOOLS[@]}" | tee "run/agent_transcript.txt"
  DEST="$REPO/runs/replay/agent/$CUTOFF"
  rm -rf "$DEST" && mkdir -p "$(dirname "$DEST")" && cp -R run "$DEST"
  rm -rf "$DEST/preds"
  echo "Saved to $DEST. Score it with: python scripts/replay.py --score-only"
fi

"""A weekly run: its cutoff, champion, budget and ledger, stored in one folder.

    runs/<cutoff>/state.json      cutoff W, development end D, champion, budget used
    runs/<cutoff>/ledger.jsonl    every tool call and its result, each with an id (L01, L02, ...)
    runs/<cutoff>/configs/        configs saved by the agent or by `tune`
    runs/<cutoff>/preds/          backtest forecasts (for `diagnose`; not committed)

The active run is the folder in the STEWARD_RUN environment variable, or the one named in
runs/CURRENT.
"""

from __future__ import annotations

import json
import os
import pickle
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .settings import BUDGET, SETTINGS
from .space import ModelConfig


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class Run:
    path: Path

    # ---- creation and lookup
    @classmethod
    def start(cls, cutoff: pd.Timestamp, champion: ModelConfig, path: Path | None = None,
              mode: str = "live") -> "Run":
        path = path or SETTINGS.runs_dir / f"{cutoff:%Y-%m-%d}"
        if (path / "state.json").exists():
            raise FileExistsError(f"{path} already exists; delete it to start this week again")
        path.mkdir(parents=True, exist_ok=True)
        dev_end = cutoff - pd.Timedelta(days=SETTINGS.promotion_days)
        state = {"cutoff": f"{cutoff:%Y-%m-%d}", "dev_end": f"{dev_end:%Y-%m-%d}", "mode": mode,
                 "champion": champion.model_dump(mode="json"), "used": {k: 0 for k in BUDGET},
                 "submissions": 0, "status": "open"}
        run = cls(path)
        run._write_state(state)
        (path / "ledger.jsonl").touch()
        return run

    @classmethod
    def active(cls) -> "Run":
        env = os.environ.get("STEWARD_RUN")
        if env:
            return cls(Path(env))
        pointer = SETTINGS.runs_dir / "CURRENT"
        if not pointer.exists():
            raise RuntimeError("no active run: start one with `python -m steward start`")
        return cls(SETTINGS.runs_dir / pointer.read_text().strip())

    # ---- state
    @property
    def state(self) -> dict:
        return json.loads((self.path / "state.json").read_text())

    def _write_state(self, state: dict) -> None:
        (self.path / "state.json").write_text(json.dumps(state, indent=2) + "\n")

    def update(self, **changes) -> None:
        s = self.state
        s.update(changes)
        self._write_state(s)

    @property
    def cutoff(self) -> pd.Timestamp:
        return pd.Timestamp(self.state["cutoff"])

    @property
    def dev_end(self) -> pd.Timestamp:
        return pd.Timestamp(self.state["dev_end"])

    @property
    def dev_start(self) -> pd.Timestamp:
        return self.dev_end - pd.Timedelta(days=SETTINGS.dev_eval_days)

    @property
    def champion(self) -> ModelConfig:
        return ModelConfig.model_validate(self.state["champion"])

    def remaining(self) -> dict:
        used = self.state["used"]
        return {k: BUDGET[k] - used.get(k, 0) for k in BUDGET}

    def spend(self, kind: str) -> None:
        if self.state["status"] != "open":
            raise RuntimeError(f"this run is {self.state['status']}; no more tool calls")
        if self.remaining()[kind] <= 0:
            raise BudgetExceeded(f"weekly budget for '{kind}' is used up ({BUDGET[kind]} per week)")
        s = self.state
        s["used"][kind] = s["used"].get(kind, 0) + 1
        self._write_state(s)

    # ---- ledger
    def ledger(self) -> list[dict]:
        lines = (self.path / "ledger.jsonl").read_text().splitlines()
        return [json.loads(x) for x in lines if x.strip()]

    def log(self, command: str, inputs: dict, result: dict) -> dict:
        entry = {"id": f"L{len(self.ledger()) + 1:02d}", "command": command, "inputs": inputs,
                 "result": result, "time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        with open(self.path / "ledger.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry

    # ---- artifacts
    def config_path(self, name: str) -> Path:
        return self.path / "configs" / f"{name}.json"

    def save_preds(self, cfg: ModelConfig, preds: pd.DataFrame) -> None:
        p = self.path / "preds" / f"{cfg.key()}.pkl"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(pickle.dumps(preds))

    def load_preds(self, cfg: ModelConfig) -> pd.DataFrame | None:
        p = self.path / "preds" / f"{cfg.key()}.pkl"
        return pickle.loads(p.read_bytes()) if p.exists() else None

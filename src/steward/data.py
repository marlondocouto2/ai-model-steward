"""Market data, the simulated business and the modelling dataset, reused from Project 3.

The business layer is simulated on a calendar that always runs to 2030, so its random draws
don't change when a new week of FRED data arrives: last week's history stays identical.
"""

from __future__ import annotations

import contextlib
import hashlib
import pickle
from dataclasses import replace
from functools import lru_cache

import fx_margin.features as fx_features
import pandas as pd
from fx_margin.business import simulate_business
from fx_margin.config import CONFIG as FX
from fx_margin.data import download_fred, load_market

from .settings import SETTINGS

SIM_END = "2030-12-31"
SERIES = [s for _, s, _ in FX.corridors] + [FX.dollar_index]
CORRIDORS = [c for c, _, _ in FX.corridors]


def refresh_fred() -> pd.Timestamp:
    """Download the latest FRED snapshot (no API key needed). Returns the new last date."""
    for s in SERIES:
        download_fred(s, out_dir=SETTINGS.fred_dir)
    load_all.cache_clear()
    return load_market(fred_dir=SETTINGS.fred_dir).index.max()


def _snapshot_hash() -> str:
    h = hashlib.sha1()
    for s in SERIES:
        h.update((SETTINGS.fred_dir / f"{s}.csv").read_bytes())
    return h.hexdigest()[:10]


@lru_cache(maxsize=1)
def load_all() -> tuple[pd.DataFrame, pd.DataFrame]:
    """(market, business) for the whole snapshot."""
    market = load_market(fred_dir=SETTINGS.fred_dir)
    last = market.index.max()
    ext = market.reindex(pd.date_range(market.index.min(), SIM_END, freq="D"))
    ext["is_trading_day"] = ext["is_trading_day"].astype("boolean").fillna(False).astype(bool)
    business = simulate_business(ext)
    business = business[(business["date"] <= last) & (business["settle_date"] <= last)
                        & business["margin_rate"].notna()].reset_index(drop=True)
    return market, business


@contextlib.contextmanager
def _halflife(hl: float):
    """Temporarily build Project 3's features with another stage 1 half-life, 1 day ahead only."""
    old = fx_features.CONFIG
    fx_features.CONFIG = replace(old, ewma_halflife=float(hl), horizons=(1,))
    try:
        yield
    finally:
        fx_features.CONFIG = old


_DATASETS: dict[int, pd.DataFrame] = {}


def dataset(halflife: int) -> pd.DataFrame:
    """One row per (corridor, origin): features known at the origin, stage 1 forecast, realized margin.

    Cached on disk per half-life and FRED snapshot.
    """
    if halflife in _DATASETS:
        return _DATASETS[halflife]
    path = SETTINGS.cache_dir / f"dataset_hl{halflife}_{_snapshot_hash()}.pkl"
    if path.exists():
        data = pickle.loads(path.read_bytes())
    else:
        market, business = load_all()
        with _halflife(halflife):
            data = fx_features.build_dataset(business, market)
        data = data.sort_values(["origin", "corridor"]).reset_index(drop=True)
        path.parent.mkdir(parents=True, exist_ok=True)
        for old in path.parent.glob(f"dataset_hl{halflife}_*.pkl"):
            old.unlink()
        path.write_bytes(pickle.dumps(data))
    _DATASETS[halflife] = data
    return data


def last_date() -> pd.Timestamp:
    return load_all()[0].index.max()

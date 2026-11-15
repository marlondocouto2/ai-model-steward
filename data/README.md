# Data

## Real: FX rates from FRED (`data/fred/`)

The same daily series as [Project 3](https://github.com/marlondocouto2/fx-margin-forecaster),
downloaded from [FRED](https://fred.stlouisfed.org/) as CSV (no API key) and committed as a
snapshot so every run is reproducible:

| File | Series |
|---|---|
| `DEXMXUS.csv` | Mexican pesos per U.S. dollar |
| `DEXINUS.csv` | Indian rupees per U.S. dollar |
| `DEXBZUS.csv` | Brazilian reais per U.S. dollar |
| `DTWEXBGS.csv` | Broad trade-weighted U.S. dollar index |

FRED publishes these weekly (the Federal Reserve's H.10 release), which is why the review runs
weekly. `python -m steward refresh-data` downloads the latest snapshot.

## Simulated: the business

The markup policy, settlement lags and volumes come from Project 3's simulator
(`fx_margin.business`), installed as a dependency. The simulation always runs on a calendar to
2030, so adding a new week of FRED data never changes the simulated history of earlier weeks.
None of this represents any real company's data.

## Cache (`data/cache/`, not committed)

Modelling datasets per EWMA half-life, and the replay's future-window scores.

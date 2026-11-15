"""Charts for the README: replay results by method, and week-by-week decisions."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

COLORS = {"never": "#8a8984", "scripted": "#eb6834", "automation": "#2a78d6", "agent": "#6250d6"}
NAMES = {"never": "Never retrain", "scripted": "Scripted playbook", "automation": "Optuna automation",
         "agent": "AI agent (Claude Code)"}


def plot_results(summary: pd.DataFrame, path: Path, title: str) -> None:
    """Change in future error vs never retraining, with the promotion rule and without it."""
    s = summary[summary["method"] != "never"].reset_index(drop=True)
    base = summary.loc[summary["method"] == "never", "future_MAE_bps"].iloc[0]
    with_rule = s["change_vs_never_pct"]
    no_rule = (s["if_rule_ignored_MAE_bps"] - base) / base * 100
    fig, ax = plt.subplots(figsize=(8, 4.2))
    x = range(len(s))
    for off, vals, alpha, hatch, label in ((-0.2, with_rule, 1.0, None, "With the promotion rule"),
                                           (0.2, no_rule, 0.35, "//", "If every proposal were accepted")):
        ax.bar([i + off for i in x], vals, width=0.4, color=[COLORS[m] for m in s["method"]],
               alpha=alpha, hatch=hatch, label=label)
        for i, v in zip(x, vals):
            v = 0.0 if abs(v) < 0.005 else v
            ax.text(i + off, v, f"{v:+.2f}%" if v else "0.00%", ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    ax.axhline(0, color="#444", lw=0.8)
    ax.set_xticks(list(x), [f"{NAMES[m]}\n{n} switch{'es' if n != 1 else ''} in {w} weeks"
                            for m, n, w in zip(s["method"], s["switches"], s["weeks"])])
    lim = max(0.3, float(max(with_rule.abs().max(), no_rule.abs().max())) * 1.35)
    ax.set_ylim(-lim, lim)
    ax.set_ylabel("Error over the next 12 weeks\nvs never retraining (%)")
    ax.set_title(title, fontsize=11, loc="left")
    ax.legend(frameon=False, fontsize=9, loc="upper right" if float(min(with_rule.min(), no_rule.min())) < -0.5 else "lower right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_timeline(weeks: pd.DataFrame, path: Path) -> None:
    """Week by week: how much better (below zero) or worse each method's proposal and final
    choice did than never retraining, over the following 12 weeks."""
    methods = [m for m in ("scripted", "automation") if m in set(weeks["method"])]
    fig, axes = plt.subplots(len(methods), 1, figsize=(9, 2.3 * len(methods)), sharex=True, sharey=True)
    axes = [axes] if len(methods) == 1 else axes
    for ax, m in zip(axes, methods):
        g = weeks[weeks["method"] == m].sort_values("cutoff")
        t = pd.to_datetime(g["cutoff"])
        prop = g["proposed_future_mae_bps"] - g["start_future_mae_bps"]
        chosen = g["chosen_future_mae_bps"] - g["start_future_mae_bps"]
        ax.axhline(0, color="#8a8984", lw=0.8)
        ax.scatter(t, prop, s=14, color=COLORS[m], alpha=0.35, label="Proposed challenger (rule ignored)")
        sw = g["decision"] == "switch"
        ax.scatter(t[sw], chosen[sw], s=40, color=COLORS[m], edgecolor="black", lw=0.6, label="Switch made")
        ax.set_title(NAMES[m], fontsize=10, loc="left")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8, loc="upper right")
    fig.supylabel("Future MAE vs never retraining (bps)", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

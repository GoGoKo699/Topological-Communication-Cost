#!/usr/bin/env python3
"""Draw the explicit R=1 braiding geometry. Optional dependency: matplotlib.

The figure illustrates exact cell sets; the all-radius proof is in
science/local-braiding.md. This is not part of the standard-library check suite.
"""
from pathlib import Path
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from verify_geometry import multiply_supports, path_edges, star, thicken, verify_radius


def draw(preview=None):
    matplotlib.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                                "svg.hashsalt": "toric-braiding-R1"})
    radius, scale = 1, 2
    verify_radius(radius)
    p, q = (6 * scale, 12 * scale), (26 * scale, 12 * scale)
    upper = path_edges([p, (6 * scale, 22 * scale), (26 * scale, 22 * scale), q])
    lower = path_edges([p, (6 * scale, 2 * scale), (26 * scale, 2 * scale), q])
    loop = multiply_supports(star(x, y) for x in range(3 * scale, 9 * scale + 1)
                             for y in range(8 * scale, 16 * scale + 1))
    colors = ("#3075B7", "#D78028", "#7352A2")
    fig = plt.figure(figsize=(11, 6.8), facecolor="white")
    ax = fig.add_axes([0.065, 0.13, 0.51, 0.76])
    ax.set(xlim=(0, 64), ylim=(0, 64), aspect="equal", xlabel="cell x", ylabel="cell y")
    ax.set_xticks([0, 16, 32, 48, 64])
    ax.set_yticks([0, 16, 32, 48, 64])
    ax.tick_params(labelsize=10)
    ax.grid(color="#E2E6EA", linewidth=0.7)
    ax.set_axisbelow(True)
    for edges, color in zip((upper, lower, loop), colors):
        cells = thicken(edges, radius)
        for y in sorted({y for _, y in cells}):
            xs = sorted(x for x, yy in cells if yy == y)
            start = last = xs[0]
            for x in xs[1:] + [xs[-1] + 2]:
                if x != last + 1:
                    ax.add_patch(Rectangle((start, y), last - start + 1, 1,
                                           facecolor=color, edgecolor="none", alpha=0.72))
                    start = x
                last = x
    for point, label in ((p, "p"), (q, "q")):
        x, y = point
        ax.add_patch(Rectangle((x - 2 * scale, y - 2 * scale), 4 * scale + 1,
                               4 * scale + 1, facecolor="none", edgecolor="#177257",
                               linewidth=2, linestyle=(0, (4, 2))))
        ax.plot(x + 0.5, y + 0.5, "o", color="#142A39", markersize=4)
        ax.text(x + 2, y + 0.7, label, fontsize=13, weight="bold", color="#142A39")
    fig.text(0.065, 0.955, "One causal braiding patch", fontsize=21, weight="bold", color="#142A39")
    fig.text(0.065, 0.914, "Exact cell neighborhoods at R = 1; s = R + 1 = 2", fontsize=12, color="#4F6170")
    labels = [(colors[0], "Upper open Z string: N_R(S_B)"),
              (colors[1], "Lower open Z string: N_R(S_B')"),
              (colors[2], "Closed X string: N_R(S_A)"),
              ("#177257", "Endpoint regions E (dashed)")]
    for index, (color, label) in enumerate(labels):
        y = 0.81 - index * 0.064
        fig.add_artist(Rectangle((0.62, y - 0.006), 0.021, 0.021,
                                 transform=fig.transFigure, facecolor=color,
                                 edgecolor="none"))
        fig.text(0.655, y, label, fontsize=11, color="#142A39")
    explanations = ["The two open-string neighborhoods",
                    "can overlap only inside E.", "",
                    "The closed-string neighborhood",
                    "stays entirely outside E.", "",
                    "All supports fit inside this",
                    "64 × 64-cell patch.", "",
                    "Color overlap marks shared cells;",
                    "it does not identify shared qubits."]
    fig.text(0.62, 0.48, "\n".join(explanations), va="top", fontsize=12,
             linespacing=1.45, color="#334B5B")
    fig.text(0.065, 0.042,
             "The same coordinate construction uses side 32(R+1) at every integer radius R ≥ 0.",
             fontsize=11, color="#4F6170")
    destination = Path(__file__).resolve().parents[1] / "figures" / "braiding-patch.svg"
    destination.parent.mkdir(exist_ok=True)
    fig.savefig(destination, metadata={"Date": None, "Creator": "plot_geometry.py; exact cell sets"})
    if preview:
        fig.savefig(preview, dpi=150)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", type=Path, help="optional PNG preview path")
    draw(parser.parse_args().preview)

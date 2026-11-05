#!/usr/bin/env python3
"""Finite checks of the explicit toric-string geometry; no quantum libraries.

The analytic proof covers every radius.  This script independently constructs
the Pauli supports from stars, plaquettes and paths for representative radii,
then checks their algebra, buffered supports, and finite packing inequalities.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def path_edges(vertices):
    edges = set()
    for (x0, y0), (x1, y1) in zip(vertices, vertices[1:]):
        require(x0 == x1 or y0 == y1, "Path segment is not axis aligned")
        if y0 == y1:
            edges.symmetric_difference_update(("h", x, y0) for x in range(min(x0, x1), max(x0, x1)))
        else:
            edges.symmetric_difference_update(("v", x0, y) for y in range(min(y0, y1), max(y0, y1)))
    return edges


def star(x, y):
    return {("h", x, y), ("h", x - 1, y), ("v", x, y), ("v", x, y - 1)}


def plaquette(x, y):
    return {("h", x, y), ("h", x, y + 1), ("v", x, y), ("v", x + 1, y)}


def multiply_supports(supports):
    answer = set()
    for support in supports:
        answer.symmetric_difference_update(support)
    return answer


def thicken(edges, radius):
    cells = {(x, y) for _, x, y in edges}
    return {(x + dx, y + dy) for x, y in cells
            for dx in range(-radius, radius + 1)
            for dy in range(-radius, radius + 1)}


def square(center, radius):
    x, y = center
    return {(a, b) for a in range(x - radius, x + radius + 1)
            for b in range(y - radius, y + radius + 1)}


def verify_radius(radius):
    s = radius + 1
    p, q = (6 * s, 12 * s), (26 * s, 12 * s)
    upper = path_edges([p, (6 * s, 22 * s), (26 * s, 22 * s), q])
    lower = path_edges([p, (6 * s, 2 * s), (26 * s, 2 * s), q])
    loop = multiply_supports(star(x, y) for x in range(3 * s, 9 * s + 1)
                             for y in range(8 * s, 16 * s + 1))
    filling = multiply_supports(plaquette(x, y) for x in range(6 * s, 26 * s)
                                for y in range(2 * s, 22 * s))
    require(upper ^ lower == filling, "Open-string deformation is not a plaquette stabilizer")
    require(len(loop & upper) % 2 == 1, "Upper string does not anticommute with loop")
    require(len(loop & lower) % 2 == 1, "Lower string does not anticommute with loop")
    a, b, bp = (thicken(edges, radius) for edges in (loop, upper, lower))
    e = square(p, 2 * s) | square(q, 2 * s)
    patch = {(x, y) for x in range(32 * s) for y in range(32 * s)}
    require((a | b | bp | e) <= patch, "Buffered support escapes its patch")
    require((b & bp) <= e, "Dressed-string overlap escapes endpoint regions")
    require(not a & e, "Dressed loop touches an endpoint region")
    u = b - e
    v = patch - (e | u)
    require(not (e & u or e & v or u & v), "Region partition is not disjoint")
    require(e | u | v == patch, "Region partition is incomplete")
    require(b <= e | u and bp <= e | v and a <= u | v,
            "Local lemma support hypotheses fail")
    return {"radius": radius, "patch_side": 32 * s,
            "loop_edges": len(loop), "upper_edges": len(upper),
            "lower_edges": len(lower), "buffered_intersection_cells": len(b & bp),
            "upper_crossings": len(loop & upper), "lower_crossings": len(loop & lower),
            "pauli_and_support_checks": "pass"}


def verify_scalar_bounds():
    lam = math.log2(17 / 16)
    count = 0
    for radius in range(13):
        s = radius + 1
        side = 32 * s
        for length in sorted({3, side - 1, side, side + 1, 2 * side - 1,
                              2 * side, 3 * side + 7, 8 * side}):
            if length < 3:
                continue
            m = (length // side) ** 2
            require(m + 1 >= length * length / (4096 * s * s),
                    "All-size packing inequality fails")
            for fidelity in (1.0, 0.9, 0.5, 0.01, 1e-8):
                gamma = math.log2(1 / fidelity)
                hard = max(0, math.ceil(lam * m - gamma))
                rhs = lam * (m + 1) / max(1, gamma + lam)
                require(hard + 1 + 1e-12 >= rhs, "Hard-cap scalar corollary fails")
                mean_lower = max(0.0, fidelity * lam * m + fidelity * math.log2(fidelity))
                require(mean_lower + 1 + 1e-12 >= fidelity * lam * (m + 1),
                        "Expected-length scalar corollary fails")
                count += 1
    return {"cases": count, "all_size_and_cost_inequalities": "pass"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"schema_version": 1, "purpose": "Finite Pauli/support checks of the analytical local geometry",
              "radii": [verify_radius(r) for r in (0, 1, 2, 3, 5, 8)],
              "scalar_checks": verify_scalar_bounds(),
              "scope": "Checks representative finite radii and scalar cases. Does not prove the all-radius lemma, channel bound, or novelty.",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()

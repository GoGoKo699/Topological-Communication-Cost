#!/usr/bin/env python3
"""Finite, exact checks of the toric-code preparation construction.

Python >= 3.10, standard library only. This verifies the implemented finite
protocol and its resource accounting; it does not prove an asymptotic converse.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SEED = 20261105


def require(condition: bool, message: str) -> None:
    """Keep verification active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def vertex(x: int, y: int, length: int) -> int:
    return (y % length) * length + x % length


def horizontal(x: int, y: int, length: int) -> int:
    return vertex(x, y, length)


def vertical(x: int, y: int, length: int) -> int:
    return length * length + vertex(x, y, length)


def edge_endpoints(edge: int, length: int) -> tuple[int, int]:
    cells = length * length
    position = edge % cells
    x, y = position % length, position // length
    if edge < cells:
        return vertex(x, y, length), vertex(x + 1, y, length)
    return vertex(x, y, length), vertex(x, y + 1, length)


def bit_positions(mask: int) -> Iterable[int]:
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def boundary(edges: int, length: int) -> int:
    """Independent incidence calculation from the physical correction mask."""
    result = 0
    for edge in bit_positions(edges):
        a, b = edge_endpoints(edge, length)
        result ^= (1 << a) ^ (1 << b)
    return result


def xor_mask(indices: Iterable[int]) -> int:
    mask = 0
    for index in indices:
        mask ^= 1 << index
    return mask


def gf2_rank(rows: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            lead = row.bit_length() - 1
            if lead in pivots:
                row ^= pivots[lead]
            else:
                pivots[lead] = row
                break
    return len(pivots)


def balanced_intervals(length: int, ell: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    count = length // ell
    small, remainder = divmod(length, count)
    sizes = tuple(small + (index < remainder) for index in range(count))
    starts = []
    position = 0
    for size in sizes:
        starts.append(position)
        position += size
    require(position == length, "partition does not cover its axis")
    require(all(ell <= size <= 2 * ell - 1 for size in sizes), "unbalanced partition")
    return tuple(starts), sizes


def cycle_color(tail: int, length: int) -> int:
    if length % 2 and tail == length - 1:
        return 2
    return tail % 2


def support_distance(a: int, b: int, length: int) -> int:
    ax, ay, bx, by = a % length, a // length, b % length, b // length
    dx = min(abs(ax - bx), length - abs(ax - bx))
    dy = min(abs(ay - by), length - abs(ay - by))
    return max(dx, dy)


def verify_layer(supports: Iterable[tuple[int, ...]], length: int) -> None:
    used: set[int] = set()
    for support in supports:
        sites = set(support)
        require(not used.intersection(sites), "parallel operations share a site")
        require(all(support_distance(a, b, length) <= 1 for a in sites for b in sites),
                "operation exceeds unit lattice diameter")
        used.update(sites)


@dataclass(frozen=True)
class SweepOperation:
    child: int
    parent: int
    edge: int


@dataclass(frozen=True)
class RouteOperation:
    coarse_child: int
    hop: int
    tail: int
    head: int
    edge: int


@dataclass
class Plan:
    length: int
    ell: int
    starts: tuple[int, ...]
    sizes: tuple[int, ...]
    roots: tuple[int, ...]
    blocks: tuple[tuple[int, ...], ...]
    parents: tuple[int, ...]
    sweep_layers: list[list[SweepOperation]]
    route_layers: list[list[RouteOperation]]
    route_lengths: dict[int, int]
    measurement_layers: list[list[tuple[int, int]]]

    @property
    def block_count(self) -> int:
        return len(self.roots)

    @property
    def local_depth(self) -> int:
        # One ancilla preparation and one X-measurement layer.
        return 2 + len(self.measurement_layers) + len(self.sweep_layers) + len(self.route_layers)

    @property
    def delivered_bits(self) -> int:
        children_of_controller = sum(parent == 0 for parent in self.parents[1:])
        return 2 * (self.block_count - 1) - children_of_controller


def make_measurement_layers(length: int) -> list[list[tuple[int, int]]]:
    layers: list[list[tuple[int, int]]] = []
    cells = length * length
    # A pair is (control-ancilla vertex, target data-edge label).
    layers.append([(vtx, horizontal(vtx % length, vtx // length, length)) for vtx in range(cells)])
    for color in range(3):
        layer = []
        for y in range(length):
            for tail_x in range(length):
                if cycle_color(tail_x, length) == color:
                    layer.append((vertex(tail_x + 1, y, length), horizontal(tail_x, y, length)))
        if layer:
            layers.append(layer)
    layers.append([(vtx, vertical(vtx % length, vtx // length, length)) for vtx in range(cells)])
    for color in range(3):
        layer = []
        for tail_y in range(length):
            for x in range(length):
                if cycle_color(tail_y, length) == color:
                    layer.append((vertex(x, tail_y + 1, length), vertical(x, tail_y, length)))
        if layer:
            layers.append(layer)
    actual: set[tuple[int, int]] = set()
    for layer in layers:
        verify_layer(((control, edge % cells) for control, edge in layer), length)
        for pair in layer:
            require(pair not in actual, "duplicate star-extraction CNOT")
            actual.add(pair)
    expected = set()
    for y in range(length):
        for x in range(length):
            vtx = vertex(x, y, length)
            for edge in (horizontal(x, y, length), horizontal(x - 1, y, length),
                         vertical(x, y, length), vertical(x, y - 1, length)):
                expected.add((vtx, edge))
    require(actual == expected and len(actual) == 4 * cells, "star CNOT inventory mismatch")
    require(len(layers) + 2 <= 10, "measurement depth bound exceeded")
    return layers


def make_plan(length: int, ell: int) -> Plan:
    if length < 2 or not 1 <= ell <= length:
        raise ValueError("require integer L>=2 and 1<=ell<=L")
    starts, sizes = balanced_intervals(length, ell)
    count = len(starts)
    roots, blocks, parents = [], [], []
    for j, y0 in enumerate(starts):
        for i, x0 in enumerate(starts):
            roots.append(vertex(x0, y0, length))
            blocks.append(tuple(vertex(x, y, length)
                                for y in range(y0, y0 + sizes[j])
                                for x in range(x0, x0 + sizes[i])))
            parents.append(j * count + i - 1 if i else ((j - 1) * count if j else -1))
    require(sorted(v for block in blocks for v in block) == list(range(length * length)),
            "blocks overlap or omit vertices")

    sweep_layers: list[list[SweepOperation]] = []
    for offset in range(max(sizes) - 1, 0, -1):
        layer = []
        for j, y0 in enumerate(starts):
            for i, x0 in enumerate(starts):
                if offset < sizes[i]:
                    for y in range(y0, y0 + sizes[j]):
                        layer.append(SweepOperation(vertex(x0 + offset, y, length),
                                                    vertex(x0 + offset - 1, y, length),
                                                    horizontal(x0 + offset - 1, y, length)))
        sweep_layers.append(layer)
    for offset in range(max(sizes) - 1, 0, -1):
        layer = []
        for j, y0 in enumerate(starts):
            if offset < sizes[j]:
                for x0 in starts:
                    layer.append(SweepOperation(vertex(x0, y0 + offset, length),
                                                vertex(x0, y0 + offset - 1, length),
                                                vertical(x0, y0 + offset - 1, length)))
        sweep_layers.append(layer)
    for layer in sweep_layers:
        verify_layer(((op.child, op.parent) for op in layer), length)
    require(sum(map(len, sweep_layers)) == length * length - count * count,
            "local comb has wrong edge count")

    segments: dict[str, list[list[RouteOperation]]] = {"horizontal": [], "vertical": []}
    route_lengths: dict[int, int] = {}
    for child in range(1, count * count):
        parent = parents[child]
        px, py = roots[parent] % length, roots[parent] // length
        cx, cy = roots[child] % length, roots[child] // length
        if cy == py:
            require(cx > px, "horizontal route wraps or points backward")
            segment = [RouteOperation(child, hop, vertex(px + hop, py, length),
                                      vertex(px + hop + 1, py, length),
                                      horizontal(px + hop, py, length)) for hop in range(cx - px)]
            segments["horizontal"].append(segment)
        else:
            require(cx == px == 0 and cy > py, "vertical route is not on the nonwrapping spine")
            segment = [RouteOperation(child, hop, vertex(px, py + hop, length),
                                      vertex(px, py + hop + 1, length),
                                      vertical(px, py + hop, length)) for hop in range(cy - py)]
            segments["vertical"].append(segment)
        require(boundary(xor_mask(op.edge for op in segment), length)
                == (1 << roots[parent]) ^ (1 << roots[child]), "coarse path has wrong boundary")
        require(1 <= len(segment) <= 2 * ell - 1, "coarse path exceeds block size")
        route_lengths[child] = len(segment)

    route_layers: list[list[RouteOperation]] = []
    for direction in ("horizontal", "vertical"):
        phase = segments[direction]
        longest = max(map(len, phase), default=0)
        for hop in range(longest):
            for color in range(2):
                layer = []
                for segment in phase:
                    if hop < len(segment):
                        op = segment[hop]
                        coordinate = op.tail % length if direction == "horizontal" else op.tail // length
                        if coordinate % 2 == color:
                            layer.append(op)
                if layer:
                    verify_layer(((op.tail, op.head) for op in layer), length)
                    route_layers.append(layer)
    route_edges = [op.edge for layer in route_layers for op in layer]
    require(len(route_edges) == len(set(route_edges)), "coarse physical segments share an edge")
    expected_route_edges = (count + 1) * (length - sizes[-1])
    require(len(route_edges) == expected_route_edges, "coarse physical edge count mismatch")

    plan = Plan(length, ell, starts, sizes, tuple(roots), tuple(blocks), tuple(parents),
                sweep_layers, route_layers, route_lengths, make_measurement_layers(length))
    require(plan.local_depth <= 12 * ell + 2, "claimed local-depth bound exceeded")
    require(plan.delivered_bits <= 2 * (plan.block_count - 1), "claimed bit bound exceeded")
    require(plan.delivered_bits * ell * ell <= 2 * length * length, "N/ell^2 bound exceeded")
    if count == 1:
        require(plan.delivered_bits == 0 and plan.local_depth <= 2 * length + 8,
                "all-local endpoint failed")
    return plan


def execute(plan: Plan, syndrome: int) -> tuple[int, list[tuple[str, int, int, int, int]]]:
    length, blocks = plan.length, plan.block_count
    cells = length * length
    if syndrome < 0 or syndrome >= 1 << cells or syndrome.bit_count() % 2:
        raise ValueError("syndrome must be an even L^2-bit string")
    registers = [(syndrome >> v) & 1 for v in range(cells)]
    correction = 0
    for layer in plan.sweep_layers:
        for op in layer:
            value = registers[op.child]
            if value:
                correction ^= 1 << op.edge
            registers[op.parent] ^= value
            registers[op.child] = 0
    root_parities = []
    for root, block in zip(plan.roots, plan.blocks):
        expected = sum((syndrome >> v) & 1 for v in block) % 2
        require(registers[root] == expected, "root does not contain its block parity")
        require(all(registers[v] == 0 for v in block if v != root), "nonroot defect survived sweep")
        root_parities.append(expected)
    root_mask = xor_mask(root for root, value in zip(plan.roots, root_parities) if value)
    require(syndrome ^ boundary(correction, length) == root_mask, "physical sweep boundary mismatch")

    # Every tuple is one delivered bit: phase, sender, recipient, edge-label, value.
    # Block IDs are fixed public addresses, not separately encoded private data.
    messages: list[tuple[str, int, int, int, int]] = []
    controller = [root_parities[0]] + [0] * (blocks - 1)
    for block in range(1, blocks):
        message = ("collect", block, 0, -1, root_parities[block])
        messages.append(message)
        controller[block] = message[-1]
    accumulated = controller[:]
    flow: dict[int, int] = {}
    for child in range(blocks - 1, 0, -1):
        flow[child] = accumulated[child]
        accumulated[plan.parents[child]] ^= accumulated[child]
    require(accumulated[0] == 0, "controller found odd total syndrome")
    coarse_boundary = [0] * blocks
    for child, value in flow.items():
        coarse_boundary[child] ^= value
        coarse_boundary[plan.parents[child]] ^= value
    require(coarse_boundary == root_parities, "coarse flow incidence check failed")

    received: dict[int, int] = {}
    for child in range(1, blocks):
        parent = plan.parents[child]
        if parent == 0:
            received[child] = flow[child]  # Already at the controller; no delivered message.
        else:
            message = ("return", 0, parent, child, flow[child])
            messages.append(message)
            received[child] = message[-1]
    require(len(messages) == plan.delivered_bits, "delivered-bit count mismatch")

    # Each segment owns its token. At a shared root, incoming terminal tokens and
    # outgoing instruction tokens occupy separate constant-size registers.
    token_positions = {child: 0 for child in range(1, blocks)}
    coarse_correction = 0
    for layer in plan.route_layers:
        for op in layer:
            require(token_positions[op.coarse_child] == op.hop, "instruction outran its local token")
            value = received[op.coarse_child]
            if value:
                correction ^= 1 << op.edge
                coarse_correction ^= 1 << op.edge
            token_positions[op.coarse_child] += 1
    require(token_positions == plan.route_lengths, "a route token did not reach its endpoint")
    require(boundary(coarse_correction, length) == root_mask, "physical coarse boundary mismatch")
    require(boundary(correction, length) == syndrome, "final physical correction leaves a star defect")
    return correction, messages


def stabilizer_data(length: int) -> tuple[dict[str, int], tuple[tuple[int, int], ...] | None]:
    cells = length * length
    stars, plaquettes = [], []
    for y in range(length):
        for x in range(length):
            stars.append(xor_mask((horizontal(x, y, length), horizontal(x - 1, y, length),
                                   vertical(x, y, length), vertical(x, y - 1, length))))
            plaquettes.append(xor_mask((horizontal(x, y, length), vertical(x + 1, y, length),
                                       horizontal(x, y + 1, length), vertical(x, y, length))))
    logicals = [xor_mask(horizontal(x, 0, length) for x in range(length)),
                xor_mask(vertical(0, y, length) for y in range(length))]
    require(all(mask.bit_count() == 4 for mask in stars + plaquettes), "small-torus edge labels collapsed")
    require(all(boundary(mask, length) == 0 for mask in plaquettes + logicals),
            "a Z plaquette or logical loop anticommutes with a star")
    star_rank, plaquette_rank = gf2_rank(stars), gf2_rank(plaquettes)
    full_z_rank = gf2_rank(plaquettes + logicals)
    require((star_rank, plaquette_rank, full_z_rank) == (cells - 1, cells - 1, cells + 1),
            "stabilizer/logical ranks do not identify the specified pure state")

    orbit = None
    if length <= 3:
        # Omit vertex zero. Product-star orbit, represented exactly by bit masks.
        basis: list[tuple[int, int]] = [(0, 0)]
        for vtx in range(1, cells):
            basis += [(word ^ stars[vtx], subset ^ (1 << vtx)) for word, subset in basis]
        require(len({word for word, _ in basis}) == 1 << (cells - 1), "star orbit is not independent")
        require(all((word & stabilizer).bit_count() % 2 == 0
                    for word, _ in basis for stabilizer in plaquettes + logicals),
                "target orbit leaves a plaquette or logical-Z eigenspace")
        orbit = tuple(basis)
    return {"L": length, "data_qubits": 2 * cells, "star_rank": star_rank,
            "plaquette_rank": plaquette_rank, "plaquette_plus_logical_Z_rank": full_z_rank}, orbit


def even_syndromes(cells: int) -> Iterable[int]:
    for lower in range(1 << (cells - 1)):
        yield lower | ((lower.bit_count() % 2) << (cells - 1))


def random_even_syndrome(cells: int, generator: random.Random) -> int:
    lower = generator.getrandbits(cells - 1)
    return lower | ((lower.bit_count() % 2) << (cells - 1))


def run_suite() -> dict:
    generator = random.Random(SEED)
    reports = []
    algebra_reports = []
    syndrome_cases = amplitude_checks = zero_message_checks = 0
    digest = hashlib.sha256()
    sizes = [2, 3, 4, 5, 7, 8, 10, 11, 16, 17, 31, 48]
    for length in sizes:
        algebra, orbit = stabilizer_data(length)
        algebra_reports.append(algebra)
        ell_values = list(range(1, length + 1)) if length <= 3 else sorted(
            {1, 2, 3, max(1, length // 3), max(1, length // 2), length - 1, length})
        for ell in ell_values:
            plan = make_plan(length, ell)
            cells = length * length
            if length <= 3:
                cases = list(even_syndromes(cells))
                mode = "all even syndromes"
            else:
                cases = [0, (1 << 0) | (1 << (cells - 1)),
                         (1 << (cells - cells % 2)) - 1]
                cases += [random_even_syndrome(cells, generator) for _ in range(12)]
                mode = "3 structured and 12 seeded random syndromes"
            reference_schedule = None
            for syndrome in cases:
                correction, messages = execute(plan, syndrome)
                schedule = tuple(message[:-1] for message in messages)
                if reference_schedule is None:
                    reference_schedule = schedule
                require(schedule == reference_schedule, "message schedule depends on a private outcome")
                if syndrome == 0:
                    require(correction == 0 and all(message[-1] == 0 for message in messages),
                            "all-zero case did not execute its full fixed zero-message schedule")
                    zero_message_checks += 1
                if orbit is not None:
                    for basis_word, vertex_subset in orbit:
                        projected_phase = (vertex_subset & syndrome).bit_count() % 2
                        correction_phase = (basis_word & correction).bit_count() % 2
                        require(projected_phase == correction_phase,
                                "corrected projected-state amplitude differs from the fixed target")
                        amplitude_checks += 1
                digest.update(json.dumps([length, ell, syndrome, correction, messages],
                                         separators=(",", ":")).encode())
                syndrome_cases += 1
            try:
                execute(plan, 1)
            except ValueError:
                pass
            else:
                raise AssertionError("an odd syndrome was accepted")
            reports.append({"L": length, "ell": ell, "block_side_lengths": list(plan.sizes),
                            "blocks": plan.block_count, "divisible": length % ell == 0,
                            "cases": len(cases), "mode": mode,
                            "local_depth": plan.local_depth, "depth_bound": 12 * ell + 2,
                            "delivered_bits": plan.delivered_bits,
                            "collect_bits": plan.block_count - 1,
                            "return_bits": plan.delivered_bits - (plan.block_count - 1),
                            "local_sweep_edge_operations": sum(map(len, plan.sweep_layers)),
                            "coarse_path_edge_operations": sum(map(len, plan.route_layers)),
                            "maximum_coarse_path_length": max(plan.route_lengths.values(), default=0)})
    return {"status": "PASS", "suite": "exact finite toric preparation and resource accounting",
            "schema_version": 1, "seed": SEED,
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "case_digest_sha256": digest.hexdigest(),
            "summary": {"partition_configurations": len(reports), "syndrome_cases": syndrome_cases,
                        "exact_small_state_amplitude_checks": amplitude_checks,
                        "fixed_zero_message_schedule_checks": zero_message_checks,
                        "nondivisible_partition_configurations": sum(not row["divisible"] for row in reports),
                        "odd_syndrome_rejections": len(reports)},
            "stabilizer_rank_checks": algebra_reports, "configurations": reports,
            "scope": ["Every even syndrome for L=2,3 and every ell in those sizes.",
                      "Fixed-seed and structured larger cases, including nondivisible partitions.",
                      "Independent physical incidence boundaries and exact small-state amplitudes.",
                      "Disjoint unit-range local layers and fixed point-to-point message schedules.",
                      "CSS ranks, logical-Z labels, zero-valued messages, return traffic and endpoint C=0."],
            "limitations": ["Finite checks do not prove the arbitrary-size construction or a lower bound.",
                            "No physical noise, finite controller computation time or signal latency is modeled.",
                            "No heralded protocol or omitted remote Pauli frame is counted as a corrected output."]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the complete JSON report to this new path")
    arguments = parser.parse_args()
    report = run_suite()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        # Never silently refresh an existing evidence file.
        with arguments.output.open("x", encoding="utf-8") as destination:
            destination.write(rendered)
    print(json.dumps({"status": report["status"], **report["summary"],
                      "case_digest_sha256": report["case_digest_sha256"],
                      "output": str(arguments.output) if arguments.output else None}, indent=2))


if __name__ == "__main__":
    main()

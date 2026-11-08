#!/usr/bin/env python3
"""Finite audit of constant-memory toric syndrome compression.

Finite exact-amplitude, stabilizer, schedule and detector checks supplement
the analytical proof. They do not certify an asymptotic converse or optimality.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import platform
from pathlib import Path
import random
import sys

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'verify_construction.py'
spec = importlib.util.spec_from_file_location('toric_source', SOURCE)
src = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = src
spec.loader.exec_module(src)

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def sweep(plan, syndrome):
    pointer = [(syndrome >> v) & 1 for v in range(plan.length ** 2)]
    data_syndrome = syndrome
    correction = 0
    for layer in plan.sweep_layers:
        src.verify_layer(((op.child, op.parent) for op in layer), plan.length)
        for op in layer:
            value = pointer[op.child]
            # CNOT child pointer -> parent pointer (a counted quantum gate).
            pointer[op.parent] ^= value
            # Controlled Z on physical edge (a counted quantum gate).
            if value:
                correction ^= 1 << op.edge
                data_syndrome ^= (1 << op.child) ^ (1 << op.parent)
            # Local pointer reset, with no report or controller access.
            pointer[op.child] = 0
            require(data_syndrome == src.xor_mask(v for v, bit in enumerate(pointer) if bit),
                    'pointer/data syndrome consistency failed')
    root = tuple(pointer[v] for v in plan.roots)
    require(all(pointer[v] == 0 for v in range(plan.length ** 2) if v not in plan.roots),
            'nonroot pointer not reset')
    require(syndrome ^ src.boundary(correction, plan.length) == data_syndrome,
            'independent physical boundary failed')
    return pointer, root, correction

def fanout_layers(plan):
    L, starts, sizes = plan.length, plan.starts, plan.sizes
    result = []
    for offset in range(1, max(sizes)):
        layer = []
        for j, y0 in enumerate(starts):
            for i, x0 in enumerate(starts):
                if offset < sizes[i]:
                    layer.append((src.vertex(x0 + offset - 1, y0, L),
                                  src.vertex(x0 + offset, y0, L)))
        result.append(layer)
    for offset in range(1, max(sizes)):
        layer = []
        for j, y0 in enumerate(starts):
            if offset < sizes[j]:
                for i, x0 in enumerate(starts):
                    for x in range(x0, x0 + sizes[i]):
                        layer.append((src.vertex(x, y0 + offset - 1, L),
                                      src.vertex(x, y0 + offset, L)))
        result.append(layer)
    for layer in result:
        src.verify_layer(layer, L)
    require(sum(map(len, result)) == L * L - plan.block_count,
            'fanout CNOT count mismatch')
    return result

def root_mask(plan, roots):
    return src.xor_mask(v for v, bit in zip(plan.roots, roots) if bit)

def majority_error(m, p):
    return sum(math.comb(m, k) * p ** k * (1-p) ** (m-k)
               * (1 if 2*k > m else 0.5 if 2*k == m else 0)
               for k in range(m + 1))

def verify_coherent_extraction(length):
    """Simulate the actual circuit with exact unnormalized integer amplitudes.

    Each H is represented without its common 1/sqrt(2) normalization. There
    are 2*L^2 such gates, so every final integer amplitude is scaled by 2^-L^2.
    Sparse dictionaries retain exact cancellation, including forbidden odd
    syndrome branches. This tests the gate circuit, not just syndrome rules.
    """
    cells = length * length
    data_qubits = 2 * cells
    state = {0: 1}

    def hadamard(qubit):
        nonlocal state
        result = {}
        mask = 1 << qubit
        for word, amplitude in state.items():
            low = word & ~mask
            high = low | mask
            result[low] = result.get(low, 0) + amplitude
            result[high] = result.get(high, 0) + (-amplitude if word & mask else amplitude)
        state = {word: amplitude for word, amplitude in result.items() if amplitude}

    for vertex in range(cells):
        hadamard(data_qubits + vertex)
    for layer in src.make_measurement_layers(length):
        for control, target in layer:
            control_mask = 1 << (data_qubits + control)
            target_mask = 1 << target
            state = {word ^ (target_mask if word & control_mask else 0): amplitude
                     for word, amplitude in state.items()}
    for vertex in range(cells):
        hadamard(data_qubits + vertex)

    _, orbit = src.stabilizer_data(length)
    expected = {}
    for syndrome in src.even_syndromes(cells):
        for word, subset in orbit:
            expected[word | (syndrome << data_qubits)] = (
                -2 if (syndrome & subset).bit_count() % 2 else 2)
    require(state == expected, 'coherent star-extraction circuit branch amplitudes failed')
    require(sum(amplitude * amplitude for amplitude in state.values()) == 1 << (2*cells),
            'coherent star-extraction normalization failed')
    return len(expected)

def run():
    rng = random.Random(20261108)
    rows = []
    syndrome_checks = amplitude_checks = error_pattern_checks = uniform_checks = 0
    extraction_checks = sum(verify_coherent_extraction(length) for length in (2, 3))
    for L in (2, 3, 4, 5, 7, 11, 16, 31):
        _, orbit = src.stabilizer_data(L)
        bs = range(1, L+1) if L <= 3 else sorted({1, 2, 3, max(1,L//2), L-1, L})
        for b in bs:
            plan = src.make_plan(L, b)
            fanout = fanout_layers(plan)
            counts = {}
            cases = list(src.even_syndromes(L*L)) if L <= 3 else [0] + [src.random_even_syndrome(L*L, rng) for _ in range(20)]
            for s in cases:
                pointer, root, local_z = sweep(plan, s)
                require(sum(root) % 2 == 0, 'root syndrome odd')
                require(root == tuple(sum((s>>v)&1 for v in block)%2 for block in plan.blocks),
                        'root pointer is not actual block parity')
                counts[root] = counts.get(root, 0) + 1
                for layer in fanout:
                    for control, target in layer:
                        pointer[target] ^= pointer[control]
                require(all(pointer[v] == r for block, r in zip(plan.blocks, root) for v in block),
                        'protected pointer fanout incorrect')
                if orbit is not None:
                    rm = root_mask(plan, root)
                    for word, subset in orbit:
                        require(((subset & s).bit_count() + (word & local_z).bit_count()) % 2
                                == (subset & rm).bit_count() % 2,
                                'actual controlled-Z sweep changes canonical state phase')
                        amplitude_checks += 1
                # Exhaust every independent root misdecoding pattern for small instances;
                # sample larger ones, and physically evaluate actual coarse Z corrections.
                n = plan.block_count - 1
                errors = range(1 << n) if L <= 3 else [0] + [rng.getrandbits(n) for _ in range(8)]
                for errors_mask in errors:
                    estimated = [0] + [root[j] ^ ((errors_mask>>(j-1))&1) for j in range(1, len(root))]
                    estimated[0] = sum(estimated[1:]) % 2
                    correction, _ = src.execute(plan, root_mask(plan, estimated))
                    residual = s ^ src.boundary(local_z ^ correction, L)
                    require((residual == 0) == (errors_mask == 0),
                            'ground-space membership does not equal correct root decoding')
                    error_pattern_checks += 1
                syndrome_checks += 1
            if L <= 3:
                require(len(counts) == 1 << (plan.block_count - 1), 'root support not full even subspace')
                require(set(counts.values()) == {1 << (L*L - plan.block_count)},
                        'root vector not uniform even after discarding old pointers')
                uniform_checks += 1
            d = len(plan.sweep_layers)
            depth = 2 + len(plan.measurement_layers) + 1 + 3*d + len(fanout) + b + 1
            require(depth <= 17*b - 4, 'conservative elementary depth failed')
            rows.append({'L': L, 'b': b, 'blocks': plan.block_count,
                         'side_lengths': list(plan.sizes), 'sweep_edge_channels': L*L-plan.block_count,
                         'fanout_CNOTs': sum(map(len, fanout)), 'elementary_depth_t_equals_b':depth,
                         'depth_bound':17*b-4, 'qubits':3*L*L,
                         'minimum_reports_per_decoded_root': b**3 if plan.block_count>1 else 0})
    # Direct probability enumeration of independent fair-tie majority decisions
    # and all root-error patterns, checked against product physical overlap.
    probability_checks = 0
    for areas in ((1,1), (2,3,4), (4,4,6,9)):
        for p in (.01,.1,.25,.49):
            for t in (1,2,3):
                es = [majority_error(a*t,p) for a in areas[1:]]
                explicit = 0.0
                for errors in itertools.product((0,1),repeat=len(es)):
                    probability = math.prod(e if err else 1-e for err,e in zip(errors,es))
                    if not any(errors):
                        explicit += probability
                physical = math.prod(1-e for e in es)
                require(abs(explicit-physical)<1e-14,'physical overlap product failed')
                D=-.5*math.log(4*p*(1-p))
                require(1-physical <= sum(math.exp(-D*a*t) for a in areas[1:]) + 1e-12,
                        'Chernoff upper estimate failed')
                probability_checks += 1
    return {'status':'PASS', 'source_repository':'GoGoKo699/Topological-Communication-Cost',
            'inherited_source_commit':'47e2a2632a939c96546b199b3ff08a1cd059f194',
            'schema_version':1, 'seed':20261108,
            'python_version':platform.python_version(),
            'python_implementation':platform.python_implementation(),
            'source_helper_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'summary':{'configurations':len(rows),'syndrome_cases':syndrome_checks,
                       'exact_coherent_extraction_amplitude_checks':extraction_checks,
                       'exact_state_amplitude_checks':amplitude_checks,
                       'physical_root_error_pattern_checks':error_pattern_checks,
                       'uniform_even_root_distribution_checks':uniform_checks,
                       'probability_checks':probability_checks},
            'configurations':rows,
            'scope':['Exact sparse coherent star-extraction circuits for L=2,3.',
                     'Every even small syndrome, actual controlled-Z phases and residual edge boundaries.',
                     'Fixed-density pointer compression and fanout with disjoint cell supports.',
                     'Uniform-even root distribution and physical output for decoder error patterns.',
                     'Fair-tie majority, independent-root error probabilities and Chernoff estimates.'],
            'limitations':['Finite checks supplement the analytic construction, not a universal converse.',
                           'Ideal coherent gates, reset, storage and repeatable QND pointer readout.',
                           'No bounded classical signal latency or processor runtime is modeled.',
                           'The inherited helper commit identifies construction antecedents; script and helper hashes identify the tested local code.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='write complete JSON report to a new path')
    arguments = parser.parse_args()
    output = run()
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        with arguments.output.open('x', encoding='utf-8') as destination:
            destination.write(json.dumps(output, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status':output['status'], 'summary':output['summary'],
                      'output':str(arguments.output) if arguments.output else None}, indent=2))

if __name__ == '__main__':
    main()

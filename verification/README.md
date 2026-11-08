# Verification evidence

The written proofs establish the universal statements. The supplied programs check finite implementations and specific algebraic/geometric constructions. Their results are supporting evidence, not independent peer review or a numerical proof of an asymptotic lower bound.

## Construction checks

Run from the repository root with **Python 3.10 or later**; no third-party package is required:

```bash
python3 tools/verify_construction.py
```

To preserve a new complete report, choose an output path that does not already exist:

```bash
python3 tools/verify_construction.py --output verification/local-construction-check.json
```

The program refuses to overwrite an existing report. Its checks remain active under `python -O`; they are explicit failures rather than removable Python `assert` statements. An unsuccessful check raises an error and no completed report is written.

### What is checked

The implementation follows [the exact preparation protocol](../science/preparation.md). It checks several independent representations of the construction:

| Check | Evidence and purpose |
|---|---|
| Block partition and local schedules | Every vertex belongs to exactly one balanced block. Every operation layer has disjoint site supports and unit lattice diameter. The four-direction star circuit contains exactly the required CNOTs, including the distinct parallel edge labels at $`L=2`$. |
| Local and coarse parity processing | Local register updates are compared with direct block parities. The controller's subtree coefficients are checked against an independently computed coarse incidence boundary. |
| Physical correction | The actual Pauli-$`Z`$ edge mask is assembled from executed sweep and routing operations. A fresh physical edge-incidence calculation verifies cancellation of every initial star defect. Local instruction tokens must reach a gate before it can run. |
| Classical communication | Both collection and return traffic are present. Sender, recipient and order stay fixed across all tested syndromes. The all-zero syndrome still executes the full prescribed zero-bit transcript. Controller-owned instructions are local and are not mislabeled as delivered messages. |
| Target logical sector | Binary stabilizer ranks verify $`L^2-1`$ independent stars, $`L^2-1`$ independent plaquettes and two independent logical-$`Z`$ constraints. Closed-loop incidence verifies their commutation. Every implemented correction is explicitly a $`Z`$ edge mask. |
| Exact small-state amplitudes | For $`L=2,3`$, the program builds the full product-star orbit of $`\lvert0\rangle`$. For every even syndrome and every block parameter in those sizes, the measured-state phase and the physical correction phase cancel exactly on every basis amplitude. The corrected state is the same fixed ground state in every branch. |
| Resource bounds and endpoints | The program checks the actual local layer count against $`12\ell+2`$, exact delivered-bit counts against $`2(B-1)`$ and $`N/\ell^2`$, local/coarse edge-operation inventories, route lengths, and the zero-communication endpoint when $`B=1`$. |

The all-even-syndrome enumeration covers $`L=2,3`$. Larger sizes are $`L=4,5,7,8,10,11,16,17,31,48`$, using several block sizes for each. Each larger configuration has three structured syndromes and twelve samples from the fixed seed `20261105`. The structured cases include no defects, a pair straddling the coordinate cut, and the largest all-one even pattern. Odd syndromes are explicitly rejected because they cannot arise from the complete star measurement.

### Preserved construction result

[construction-results.json](construction-results.json) was produced with **CPython 3.12.14**. It reports:

| Quantity | Count |
|---|---:|
| Partition configurations | 65 |
| Nondivisible partition configurations | 30 |
| Syndrome instances | 1,684 |
| Exact small-state amplitude comparisons | 196,736 |
| Fixed all-zero transcript checks | 65 |
| Odd-syndrome rejection checks | 65 |

Every listed check passed. The report contains per-configuration sizes, depth, collection/return counts and path statistics; stabilizer rank results; the random seed; Python metadata; and the script SHA-256.

The deterministic case digest is

```text
0e031cc09ef63b347f6a1ec3e1e3f369c1221f1d680d705352e9be4de7b007c1
```

This digest covers the tested lattice/block parameters, syndromes, actual physical correction masks and delivered-message logs. Compare it and the structured results when reproducing. Exact JSON bytes additionally depend on the reported Python version and the verifier's source hash; a changed environment or source revision should not be hidden by refreshing the preserved report.

### Limits

These checks do not verify all lattice sizes, derive the communication converse, optimize the finite constants, or establish a physical-noise threshold. They do not simulate a controller with finite processor speed, network transit latency or faulty hardware. The small-state check is an exact stabilizer-amplitude calculation, not a general-purpose full-circuit simulator. The arbitrary-size upper bound rests on the local-sweep, tree-flow and boundary argument in the scientific account.

## Noisy-report compression checks

[The noisy-readout account](../science/noisy-readout.md) studies a different resource convention from the charged-communication construction above: global classical processing and communication are free, but every measurement outcome supplied to that controller passes through an independent unflagged binary symmetric channel. The controller must deliver a physically corrected toric-code state. This extension combines the inherited local toric-code correction with the protected quantum-pointer readout of [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b/science/construction.md).

Run the additional finite audit from this repository root:

```bash
python3 tools/verify_compression.py
```

To save a fresh complete report, use a new path:

```bash
python3 tools/verify_compression.py --output verification/local-compression-check.json
```

The program uses only the Python standard library, imports [the existing construction helper](../tools/verify_construction.py), and refuses to overwrite an existing report. Explicit checks remain active under `python -O`. Its report records both source hashes and the inherited construction revision; that historical revision identifies the antecedent and is not a claim that the new verifier existed there.

### Physical invariant and resource convention

The protocol uses two owned data qubits and one quantum pointer ancilla per cell, so $`q=3`$. A fixed neighboring-cell sweep step applies a pointer CNOT, a pointer-controlled physical $`Z`$, and an unconditional child-pointer reset. Its surviving pointer equals the **actual remaining star defect**. No raw true outcome is supplied to the classical controller. Freed ancillas copy the block-root pointer across the block through counted local CNOT gates; repeated QND readout then produces independent noisy reports of that same bit.

For blocks with side lengths in $`[b,2b-1]`$, area $`A_j`$, and $`t`$ readout layers, the elementary schedule has

```math
T\le16b+t-4,\qquad q=3,\qquad r=1,\qquad \nu=1,
\qquad m_j=A_jt\ge b^2t.
```

There are $`B=\lfloor L/b\rfloor^2`$ blocks. The controller decodes $`B-1`$ roots and infers the last from even syndrome parity. After the actual physical correction, the unconditional ground-space overlap is exactly

```math
F_{\rm phys}=\prod_{j=1}^{B-1}[1-e_{A_jt}(p)],
\qquad
1-F_{\rm phys}\le(B-1)e^{-D(p)b^2t},
```

where $`e_m(p)`$ is the fair-tie majority error and $`D(p)=-\tfrac12\log[4p(1-p)]`$. The empty product for $`B=1`$ is one; no readout is then required. The audit checks physical residual syndromes rather than accepting a proposed Pauli frame or a reweighted estimator as the output.

### What is checked

| Check | Evidence and purpose |
|---|---|
| Coherent star extraction | Sparse exact integer amplitudes simulate the actual ancilla Hadamards and scheduled extraction CNOTs at $`L=2,3`$. Every joint syndrome/data amplitude is compared with its canonical projected-state value. Forbidden odd-syndrome amplitudes cancel exactly, and normalization is checked. |
| Quantum-pointer compression | Every local CNOT, controlled physical $`Z`$ and pointer reset is evaluated on the resulting classical pointer branches. Pointer/data syndrome consistency is checked after every step, along with the independently computed physical edge boundary. For small instances the actual controlled-$`Z`$ phases are compared on every canonical-state basis amplitude. |
| Discarded records and root distribution | Exhaustion of all small even syndromes verifies that each even root vector has exactly $`2^{L^2-B}`$ preimages. The retained roots remain correlated with their actual data defects after nonroot records are discarded. |
| Pointer fanout and fixed density | The row/column CNOT schedule has disjoint cell supports and unit range, uses exactly $`L^2-B`$ CNOTs, and fills every block with its root bit. No extra pointer memory or simultaneous report density is introduced. |
| Corrected output under decoding errors | All independent-root error patterns are exhausted in small layouts and sampled in larger ones. The actual coarse physical edge correction is assembled, and an independent boundary calculation verifies that ground-space membership occurs precisely when every decoded independent root is correct. |
| Detector and depth estimates | Fair-tie majority probabilities, independent-root physical overlaps and Chernoff bounds are checked at several detector probabilities and repetition counts. The actual elementary layer count is compared with $`16b+t-4`$, using $`t=b`$ in the layout audit. |

[compression-results.json](compression-results.json) records a passing run with:

| Quantity | Count |
|---|---:|
| Layout configurations | 37 |
| Syndrome instances | 1,456 |
| Exact coherent-extraction amplitude comparisons | 65,600 |
| Exact compressed-state amplitude comparisons | 196,736 |
| Physical root-decoding error-pattern checks | 72,168 |
| Complete uniform-even root-distribution checks | 5 |
| Detector-probability checks | 36 |

All even syndromes and all block parameters are exhausted at $`L=2,3`$. Larger tested sizes are $`L=4,5,7,11,16,31`$, with a zero syndrome and twenty samples from seed `20261108` per layout. Those larger layouts sample decoding-error patterns rather than enumerating every pattern.

### Limits

These checks support the finite upper construction. They do not prove the buffered blind-core lemma, its application to adaptive protocols, or the universal depth lower bound; those require the analytical argument in [the noisy-readout account](../science/noisy-readout.md). The exact circuit test covers coherent star extraction, while later steps use exact pointer branches and stabilizer amplitudes; it is not a full density-matrix simulation of every layout. The stated memory/depth constants use ideal coherent gates, storage, reset and repeatable QND readout. Destructive readout needs a retained pointer and a separate resettable readout register, changing the fixed memory and depth constants. Signal latency, bounded classical processing time and noisy quantum gates are outside this report.

## Geometry checks

[verify_geometry.py](../tools/verify_geometry.py) and [geometry-results.json](geometry-results.json) concern the separate finite braiding geometry used in the converse. Run:

```bash
python3 tools/verify_geometry.py
```

The program independently forms Pauli supports by multiplying stars and plaquettes and traversing the two paths. For radii $`R=0,1,2,3,5,8`$, it checks the open-string deformation identity, one crossing of each open string with the closed string, containment of the thickened supports, separation from the endpoint regions, and the required partition into $`E,U,V`$. Every tested radius passes. It also checks **520** finite combinations of radius, lattice size and overlap in the packing and hard/mean-cost scalar inequalities, including the zero-patch and small-overlap cases.

These checks use explicit integer sets and exact Pauli incidence; only the scalar logarithms use floating-point arithmetic with a stated numerical tolerance. The [all-radius proof](../science/local-braiding.md) and [channel argument](../science/channel-overlap.md) establish the general converse. The programs do not simulate arbitrary local channels or certify the transcript proof.

The [braiding illustration](../figures/braiding-patch.svg) displays the exact $`R=1`$ cell neighborhoods. To regenerate it, install the optional plotting dependency `matplotlib` and run:

```bash
python3 tools/plot_geometry.py
```

The plotting dependency is not needed for either verification program. The figure is a geometric illustration, not additional statistical evidence.

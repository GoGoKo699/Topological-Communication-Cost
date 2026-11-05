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
| Block partition and local schedules | Every vertex belongs to exactly one balanced block. Every operation layer has disjoint site supports and unit lattice diameter. The four-direction star circuit contains exactly the required CNOTs, including the distinct parallel edge labels at $L=2$. |
| Local and coarse parity processing | Local register updates are compared with direct block parities. The controller's subtree coefficients are checked against an independently computed coarse incidence boundary. |
| Physical correction | The actual Pauli-$Z$ edge mask is assembled from executed sweep and routing operations. A fresh physical edge-incidence calculation verifies cancellation of every initial star defect. Local instruction tokens must reach a gate before it can run. |
| Classical communication | Both collection and return traffic are present. Sender, recipient and order stay fixed across all tested syndromes. The all-zero syndrome still executes the full prescribed zero-bit transcript. Controller-owned instructions are local and are not mislabeled as delivered messages. |
| Target logical sector | Binary stabilizer ranks verify $L^2-1$ independent stars, $L^2-1$ independent plaquettes and two independent logical-$Z$ constraints. Closed-loop incidence verifies their commutation. Every implemented correction is explicitly a $Z$ edge mask. |
| Exact small-state amplitudes | For $L=2,3$, the program builds the full product-star orbit of $|0\rangle$. For every even syndrome and every block parameter in those sizes, the measured-state phase and the physical correction phase cancel exactly on every basis amplitude. The corrected state is the same fixed ground state in every branch. |
| Resource bounds and endpoints | The program checks the actual local layer count against $12\ell+2$, exact delivered-bit counts against $2(B-1)$ and $N/\ell^2$, local/coarse edge-operation inventories, route lengths, and the zero-communication endpoint when $B=1$. |

The all-even-syndrome enumeration covers $L=2,3$. Larger sizes are $L=4,5,7,8,10,11,16,17,31,48$, using several block sizes for each. Each larger configuration has three structured syndromes and twelve samples from the fixed seed `20261105`. The structured cases include no defects, a pair straddling the coordinate cut, and the largest all-one even pattern. Odd syndromes are explicitly rejected because they cannot arise from the complete star measurement.

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

## Geometry checks

[verify_geometry.py](../tools/verify_geometry.py) and [geometry-results.json](geometry-results.json) concern the separate finite braiding geometry used in the converse. Run:

```bash
python3 tools/verify_geometry.py
```

The program independently forms Pauli supports by multiplying stars and plaquettes and traversing the two paths. For radii $R=0,1,2,3,5,8$, it checks the open-string deformation identity, one crossing of each open string with the closed string, containment of the thickened supports, separation from the endpoint regions, and the required partition into $E,U,V$. Every tested radius passes. It also checks **520** finite combinations of radius, lattice size and overlap in the packing and hard/mean-cost scalar inequalities, including the zero-patch and small-overlap cases.

These checks use explicit integer sets and exact Pauli incidence; only the scalar logarithms use floating-point arithmetic with a stated numerical tolerance. The [all-radius proof](../science/local-braiding.md) and [channel argument](../science/channel-overlap.md) establish the general converse. The programs do not simulate arbitrary local channels or certify the transcript proof.

The [braiding illustration](../figures/braiding-patch.svg) displays the exact $R=1$ cell neighborhoods. To regenerate it, install the optional plotting dependency `matplotlib` and run:

```bash
python3 tools/plot_geometry.py
```

The plotting dependency is not needed for either verification program. The figure is a geometric illustration, not additional statistical evidence.

# Related work and attribution

The result studied here is an optimal tradeoff between local propagation and the amount of nonlocal classical information used to prepare a physically corrected toric-code ground state. Its main topological obstruction is inherited. The additional step is to turn that obstruction into a communication bound that retains branch probabilities, remains valid with arbitrary local channels and discarded environments, and matches a compressed correction protocol.

The corresponding bibliographic entries are in [bibliography.bib](bibliography.bib).

| Earlier result | Resource or conclusion | Relation to this work |
|---|---|---|
| Bravyi–Hastings–Verstraete; König–Pastawski | Local preparation takes time of order the system diameter, including open-system settings | Establish the local endpoint and the broader preparation obstruction |
| Li–Lee–Yoshida | Depth-dependent geometric-entanglement exponent of order $`N/(D+1)^2`$ | Supplies the spatial exponent and local braiding mechanism |
| Piroli–Styliaris–Cirac; Lu–Lessa–Kim–Hsieh | Shallow preparation assisted by free classical communication | Establish measurement-assisted preparation capabilities |
| Chen–Yan–Cui | Measurement-assisted gluing of prepared pieces; a measurement/depth tradeoff | Supplies a close construction antecedent without a charged-transcript converse |
| Tantivasadakarn–Vishwanath–Verresen | Locally correctable measurement protocols can be coherified; clean toric preparation requires nonlocal dependence | Supplies the qualitative local-feedforward obstruction |
| Friedman–Yin–Hong–Lucas | Diameter versus time and number of utilized measurement regions | Gives a different resource bound, including a toric-code application |
| Present result | At fixed ground-space overlap, $`(C+1)(D+1)^2=\Omega(N)`$, attained up to constants | Prices the actual nonlocal binary transcript after arbitrary local processing |

## BHV06 and KP14: local preparation limits

S. Bravyi, M. B. Hastings, and F. Verstraete, [*Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order*](https://doi.org/10.1103/PhysRevLett.97.050401), Physical Review Letters **97**, 050401 (2006), derive consequences of locality for generating correlations and topological order.

R. König and F. Pastawski, [*Generating topological order: No speedup by dissipation*](https://doi.org/10.1103/PhysRevB.90.045101), Physical Review B **90**, 045101 (2014), treat local unitary and nonunitary preparation, including locally generated open-system dynamics. Their bounds include a preparation time proportional to system diameter for the toric code and other topologically ordered systems.

Thus neither the need for long local preparation time nor its survival under dissipation is claimed here as new. The present finite-depth model adds a separately charged nonlocal classical channel and asks how many transmitted bits replace a given amount of local processing. Its exponential overlap estimate is stronger than the statement that high-fidelity preparation requires linear local time when no such channel is supplied.

## LLY25: spatial geometric entanglement

Z. Li, D. Lee, and B. Yoshida, [*How Much Entanglement Is Needed for Topological Codes and Mixed States with Anomalous Symmetry?*](https://arxiv.org/html/2405.07970v3), Physical Review X **15**, 021090 (2025).

Their Theorem 1 proves the toric-code geometric-entanglement scaling $`E_D=\Omega(N/(D+1)^2)`$ in the relevant shallow regime. Lemma 2 derives a constant local product-overlap obstruction from anyon braiding and string deformability. Section IV.3 uses sequential patch projections for a related model, preserving the local identities on unprojected patches.

These are the load-bearing spatial ideas in our converse. Our [local lemma](../science/local-braiding.md) gives a dimension-independent vector proof, and our [channel theorem](../science/channel-overlap.md) applies it after local dilation and projection onto the full code space. The projected code state may remain correlated with arbitrary environments, so independence of patch marginals cannot be assumed. Sequential projections remove that difficulty.

The spatial exponent is credited to LLY25. The new operational conclusion is the optimal communicated-bit cost after arbitrary local processing, with all branch probabilities retained and a matching physical correction protocol.

## PSC21 and LLKH22: measurement-assisted preparation

L. Piroli, G. Styliaris, and J. I. Cirac, [*Quantum Circuits Assisted by Local Operations and Classical Communication: Transformations and Phases of Matter*](https://doi.org/10.1103/PhysRevLett.127.220503), Physical Review Letters **127**, 220503 (2021), study deterministic transformations using shallow circuits followed by local operations and classical communication. Their definition treats classical communication as free. It therefore establishes preparation capabilities without determining a finite classical-bit budget.

T.-C. Lu, L. A. Lessa, I. H. Kim, and T. H. Hsieh, [*Measurement as a Shortcut to Long-Range Entangled Quantum Matter*](https://doi.org/10.1103/PRXQuantum.3.040337), PRX Quantum **3**, 040337 (2022), construct local adaptive circuits for topological states, conformal states, and CSS codes. Their circuit model allows measurement results to be globally processed and communicated to later components. This supplies important preparation antecedents, including the use of measured syndromes and corrective strings.

Our blockwise preparation retains that mechanism. Its purpose is to attain the communication frontier after local syndrome compression, including return instructions and actual Pauli corrections. It is not a claim that measuring toric stabilizers or correcting their outcomes is a new preparation principle.

## CYC24: measurement-assisted gluing

P. Chen, B. Yan, and S. X. Cui, [*Quantum circuits for toric code and X-cube fracton model*](https://doi.org/10.22331/q-2024-03-13-1276), Quantum **8**, 1276 (2024); [full text](https://quantum-journal.org/papers/q-2024-03-13-1276/pdf/).

Section 3 glues independently prepared pieces using Clifford gates, ancilla measurements, and corrective strings. Section 3.2 permits simultaneous gluing and combines corrections for paired excitations. The introduction and conclusion explicitly identify a tradeoff between measurements and circuit depth.

This is a close antecedent for constructing larger topological states from locally prepared pieces. Partitioning the lattice and using measurement-dependent corrections are therefore established ideas. The additional resource here is the actual classical transcript after local compression, charging both collected information and returned correction instructions. Our construction counts those messages and applies the physical corrections; the converse bounds their necessary total for arbitrary adaptive local channels, rather than counting measurements or gluing steps.

## TVV23: why purely local feedforward is insufficient

N. Tantivasadakarn, A. Vishwanath, and R. Verresen, [*Hierarchy of Topological Order From Finite-Depth Unitaries, Measurement, and Feedforward*](https://doi.org/10.1103/PRXQuantum.4.020339), PRX Quantum **4**, 020339 (2023).

Theorem 3 states that a deterministic pure output obtained by single-site measurements followed by finite-depth local corrections can be coherently related to the input by a finite-depth local unitary, with an additional output state on discarded systems. Corollary 2 and the surrounding discussion identify the resulting obstruction to locally correctable preparation of noninvertible topological order. The paper explicitly discusses the nonlocal dependence of corrections needed for the clean toric-code state.

Accordingly, the qualitative necessity of nonlocal classical control is inherited. Our question is quantitative: with depth $`D`$ available for both quantum processing and local classical propagation, how many nonlocal binary messages remain necessary? The bounds allow imperfect mixed outputs and apply to the full toric ground-space projector, while the matching construction prepares a fixed pure ground state.

## FYHL23: measurement-assisted locality

A. J. Friedman, C. Yin, Y. Hong, and A. Lucas, [*Locality and error correction in quantum dynamics with measurement*](https://arxiv.org/html/2206.09929v4), arXiv:2206.09929v4 (2023).

Their main locality bound has the form

```math
L\le (2M+M_0)v(T+T_0),
```

where $`M`$ counts utilized measurement regions. Section 5.1 applies the bound to toric-code preparation; Section 4.7 treats general quantum channels. Instantaneous classical communication is allowed.

This is a diameter bound in terms of measurement regions. A count of regions whose measurements assist a protocol is not the length of the physical transcript after arbitrary local computation and compression. In particular, an arbitrarily large collection of private local outcomes is permitted in our model without being counted as remotely transmitted bits. Replacing $`M`$ by $`C`$ is therefore not a valid specialization.

The common use of dilation and adaptive measurements is established methodology. The distinct conclusion here is the area-per-causal-patch law for actual communicated information and the corresponding exponential ground-space-overlap bound.

## LGY26: sequential and measurement-feedback circuits

T.-C. Lu, S. Gopalakrishnan, and Y. You, [*Spacetime duality between sequential and measurement-feedback circuits*](https://doi.org/10.1103/lh1b-g4w8), Physical Review B **114**, 045123 (2026); [public author preprint](https://arxiv.org/html/2507.12523v1).

The paper connects sequential unitary preparation with measurement-feedback circuits through spacetime rotation, including toric-code examples. It explains relations between linear-depth and constant-depth constructions when the requisite feedback is available.

The comparison here uses Sections I, II.6, III.2, V, and Appendix C of the public author preprint. Those constructions do not charge a finite nonlocal bit transcript or state the interpolating communication/depth frontier proved here. The source provides a structural relation between preparation mechanisms, rather than a bound on the information that their classical controller must receive and return.

## CE26: shallow sampling circuits and quantum interaction cost

C. Cao and J. Eisert, [*Measurement-Driven Quantum Advantages in Shallow Circuits*](https://doi.org/10.1103/4b99-xmqn), Physical Review Letters **136**, 080601 (2026); [arXiv:2505.04705v3](https://arxiv.org/html/2505.04705v3).

Their target includes IQP sampling and structured phase states using measurement-driven fan-out constructions. Appendix C defines a geometrically local quantum circuit cost by integrated interaction strength,

```math
C_g(U)=\inf\int_0^1\sum_e |y_e(s)|\,ds,
```

and relates it to entanglement across spatial cuts. This quantity concerns a unitary implementation's quantum interactions. It is distinct from the binary classical transcript charged here. The preparation task, resource currency, and lower-bound mechanism therefore differ; the Appendix C theorem does not imply our toric-code bit/depth tradeoff.

## FWDGR26: communication-robust self-testing

G. Fróes, A. Wei, C. de Gois, D. Rochette, and M.-O. Renou, [*Self-testing the toric code against classical communication*](https://arxiv.org/html/2609.40259v1), arXiv:2609.40259v1 (2026).

This work certifies a toric-code subspace against bounded-distance communication between untrusted devices. Its Section 1.2 allows messages depending on classical measurement-setting inputs but explicitly excludes messages depending on quantum measurement outcomes. Arbitrary preshared quantum states are allowed in the certification setting.

The present task starts from spatially unentangled quantum inputs and permits outcome-dependent feedforward while charging its communicated bits. Preparation cost and communication-robust certification are therefore different operational questions.

## Related open research records

The following are versioned research repositories, not cited as peer-reviewed publications.

R. Lin, [*GHZ Communication Cost*](https://github.com/GoGoKo699/GHZ-Communication-Cost/tree/99bd0004bcd1b395d27bff9b092db64dc0672c24), considers arbitrary independent bipartite quantum sources and unrestricted processing within each laboratory. Its branch, finite-transcript, and expected-cost arguments supply closely related probability-sensitive communication accounting. For a qubit GHZ target it proves extensive communication at fidelity above the product-state baseline $`1/2`$, using a quantum Finner constraint.

That source-network theorem cannot be specialized by merely drawing its graph on a lattice. Our protocol includes successive local quantum interactions, which need not leave independent edge sources; its target is a toric ground space with an exponentially small shallow-channel overlap. The geometric local-channel obstruction is a separate necessary ingredient. See the pinned [model](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/model.md), [branch proof](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/branch-bound.md), and [mean-cost account](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/expected-and-heralded.md).

R. Lin, [*Quantum Routing Bandwidth*](https://github.com/GoGoKo699/Quantum-Routing-Bandwidth/tree/03435de579e4a051907775300a486e1c39b317fd), concerns reference-preserving exchange of unknown registers through a one-qubit Hamiltonian bus. It charges bounded-contact interaction time, grants free internal module operations, and forbids measurements and resets. Its initialization-dependent entropy-flow law does not bound classical transcripts or geometric toric-state preparation. The common theme is explicit resource accounting; the tasks, allowed controls, and converse mechanisms are different.

## What the present theorem adds

After crediting these results, the remaining statement is precise: a local causal patch of area of order $`(D+1)^2`$ determines how much global classical coordination can be saved in toric-code preparation. For fixed nonzero unconditional ground-space weight, both hard and mean communication obey an extensive cost per patch. A local syndrome sweep followed by coarse-tree correction attains that scaling with ordinary delivered bits.

The proof combines established spatial entanglement and communication methods. It does not claim a new anyon obstruction, a new qualitative impossibility of local feedforward, or a universal hardware-latency law. Its operational content is the matched classical-information frontier under the [stated resource model](../science/model.md).

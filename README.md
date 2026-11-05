# Topological Communication Cost

**How much nonlocal classical information is needed to prepare topological order quickly?** This project determines the optimal scaling between local circuit depth and communicated classical bits for physical toric-code ground-state preparation.

The system has $N=2L^2$ data qubits on an $L\times L$ torus. It starts without entanglement between lattice cells. Local quantum channels, measurements, private records, resets and arbitrary finite local ancillas are permitted. Local propagation consumes depth $D$; classical information sent outside those local layers consumes bits $C$. The output is the corrected quantum state itself, with unconditional ground-space weight $F=\operatorname{Tr}(P_{\mathrm{TC}}\rho)$.

For every fixed target overlap $F\ge f>0$ and fixed interaction range,

$$
(C+1)(D+1)^2=\Omega(N).
$$

The same scaling holds for expected communication $\overline C$ in almost surely terminating protocols. An explicit exact preparation matches the resource frontier: for every integer block scale $1\le\ell\le L$,

$$
D\le12\ell+2,\qquad
C\le2\!\left(\left\lfloor L/\ell\right\rfloor^2-1\right)
\le\frac{N}{\ell^2}.
$$

At the wholly local endpoint, $C=0$ and $D\le2L+8$. Both the collection of block parities and the returned correction instructions are included in the communication cost.

| Local processing budget | Communication needed at fixed overlap | Attained preparation |
| --- | --- | --- |
| Constant depth | Order $N$ bits | Constant-size blocks |
| Growing depth $D=o(L)$ | Order $N/(D+1)^2$ bits, up to depth rescaling by constants | Blocks with side proportional to $D$ |
| Depth of order $L$ | Zero nonlocal bits are possible | A full-lattice local syndrome sweep |

## Finite converse and its mechanism

For local gate range $r\ge1$, define

$$
m=\left\lfloor\frac{L}{32(rD+1)}\right\rfloor^2,
\qquad \lambda=\log_2(17/16).
$$

Every protocol with a hard cap of $C$ nonlocal bits obeys

$$
F\le\min\{1,\,2^{C-\lambda m}\}.
$$

Thus constant-depth preparation with $o(N)$ bits has exponentially small global ground-space weight. For prefix-free variable-length physical transcripts,

$$
\overline C\ge
\max\{0,\,F\lambda m+F\log_2F\},
$$

with $0\log_2 0=0$.

The proof places a braiding obstruction in each of $m$ disjoint causal patches. A local trace-preserving circuit has ground-space weight at most $(16/17)^m$, even when the logical state is entangled with discarded environments. Fixing a communicated transcript produces a local trace-preserving completion that dominates that branch's **subnormalized** output. Counting transcript leaves, or bounding their entropy, then prices the communication.

The topological obstruction and spatial exponent build on [Li, Lee and Yoshida](https://arxiv.org/html/2405.07970v3). Standard measurement-assisted toric preparation supplies the ingredients of the upper construction. The [source comparison](references/related-work.md) identifies these antecedents and distinguishes the charged-bit model from free feedforward, measurement-region counts and other communication tasks.

## Read the science

Start with the [scientific overview](science/README.md) and the [precise protocol model](science/model.md).

| Question | Authoritative account |
| --- | --- |
| What operations, schedules and messages are allowed? | [Model and output contract](science/model.md) |
| Why does braiding obstruct a product reference on one patch? | [Local braiding lemma and explicit geometry](science/local-braiding.md) |
| Why do arbitrary local channels and discarded ancillas obey the exponential overlap bound? | [Channel-overlap theorem](science/channel-overlap.md) |
| How do physical transcript bits become a lower bound? | [Hard-cap and expected-cost converses](science/communication-bound.md) |
| How are root parities compressed and corrections physically executed? | [Exact preparation protocol](science/preparation.md) |
| What does the frontier imply, and what changes under an ideal bandwidth limit? | [Consequences and scope](science/consequences.md) |
| Which ingredients are established prior work? | [Related work](references/related-work.md) and [bibliography](references/bibliography.bib) |
| Which finite calculations can be reproduced? | [Verification guide](verification/README.md) |

[The LLM reading guide](llms.txt) maps claims to their complete proofs and records the distinctions needed when explaining the result.

## Reproduce the finite checks

From the repository root, use Python 3.10 or later:

```bash
python3 tools/verify_geometry.py
python3 tools/verify_construction.py
```

Both programs use only the standard library. The checks cover the explicit Pauli/string geometry, packing inequalities, physical correction boundaries, causal schedules, delivered messages, stabilizer ranks and exact small-state amplitudes. The [saved reports](verification/README.md) describe their scope. Universal converses and arbitrary-size correctness follow from the written arguments; finite enumeration does not establish them.

## Scope

The lower bound grants each charged bit global broadcast, while the construction pays ordinary point-to-point delivered bits. It applies to the full toric ground space and hence also constrains preparation of a specified pure ground state. The construction prepares one fixed pure logical sector exactly.

The target is global physical ground-space overlap. An unapplied remotely described Pauli frame, small energy density, a noisy topological phase and a free global success flag define different tasks. The theorem assumes exact finite-depth causal cones and initially unentangled cells. Its constants are conservative and not optimized. A preparation-time law requires the additional ideal-switch assumptions stated in [the consequences](science/consequences.md#4-a-conditional-preparation-time-law).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

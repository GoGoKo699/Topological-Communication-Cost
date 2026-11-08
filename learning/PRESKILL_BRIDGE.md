# From Preskill's quantum error correction chapter to topological communication cost

This bridge connects the stabilizer description of a toric code to two costs of preparing its physical state. The question is: after allowing local quantum operations and local classical propagation for depth $`D`$, how many classical bits must still travel outside those local layers?

The educational anchor is John Preskill, [*Quantum Information*, Chapter 7: *Quantum Error Correction*, March 2026 author draft](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf), listed on the [author's course page](https://www.preskill.caltech.edu/ph219/index.html). The chapter supplies the code language. The preparation model, probability accounting, and quantitative bounds developed below come from this project's [science pages](../science/README.md) and their [research references](../references/related-work.md).

The [milestone map](MILESTONES.md) gives a dependency order for the material. This page supplies the explanations, conventions, and complete finite examples.

A second question uses the same target but a different classical interface: **if only the measurement reports are noisy, how much local operation depth prepares a reliable physical toric state at fixed memory density?** The [joint noisy-readout account](../science/noisy-readout.md) establishes cube-root logarithmic depth for fixed detector quality and fixed positive target overlap. It combines the local topological obstruction developed here with the retained-record and protected-pointer methods of [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits). The sections below teach the extra steps; Preskill's chapter is the common educational source, not the source of either resource theorem.

## Source map

The table gives section starting pages. Printed page $`p`$ is physical PDF page $`p+6`$ in this 92-page file. The PDF contains unfinished passages in §§7.18.2–7.18.3; §7.18.4 is only a heading. The bridge uses the definitions and equations actually present.

| Chapter section | Printed page / PDF page | Connection developed here |
|---|---:|---|
| §7.2; §§7.3.2–7.3.3 | 4 / 10; 9 / 15 | [Channels and environments](#local-channels-and-correlated-environments) |
| §7.6 | 18 / 24 | Classical redundancy for protected pointer reports |
| §7.7 | 21 / 27 | Separate $`X`$ and $`Z`$ checks |
| §§7.10.1–7.10.2 | 27 / 33; 30 / 36 | [Stabilizers and commutation](#stabilizers-and-logical-labels) |
| §7.10.4 | 33 / 39 | Logical Pauli operators |
| §7.14 | 43 / 49 | Changing an operator's support using stabilizers |
| §7.18.1 | 52 / 58 | Toric checks and logical sectors |
| §§7.18.2–7.18.3 | 54 / 60; 55 / 61 | [Boundaries and correction](#syndromes-and-physical-output) |
| §7.19 | 60 / 66 | Geometric restrictions on code parameters |
| §7.20 | 63 / 69 | Strings and energy barriers |

The last two sections give geometric background. Their code-parameter and thermal-memory questions are distinct from the preparation-resource theorem here.

## Two resource models for the same physical target

Both tasks start from a product across toric cells, allow local channels, and assess $`F=\mathrm{Tr}(P_{\mathrm{TC}}\rho_{\mathrm{out}})`$ after corrections are physically applied. The information rules differ:

| Rule | Charged-communication frontier | Noisy-report depth theorem |
|---|---|---|
| Local quantum processing | Depth $`D`$; fixed range $`r`$ | Depth $`T`$; fixed range $`r`$ |
| New classical outcome information | Private local records may be processed locally | Every outcome supplied to classical control crosses its own independent BSC |
| Global feedforward | Count delivered nonlocal bits, including return instructions | Processing and communication of already public reports are free |
| Readout resources | No detector-noise theorem is assumed | At most $`\nu`$ binary slots per cell per layer; readout layers count |
| Matching construction's quantum memory | Explicit local preparation registers | Two data qubits and one reusable pointer per cell |
| Ideal quantum hardware | Channels and chosen gates follow the stated model | Gates, reset, dephasing, storage, and QND pointer readout are ideal |

A BSC report has the form $`y=x\oplus e`$, where $`x`$ is the true pointer value and $`e`$ is a fresh independent flip of probability $`p`$. “Unflagged” means the controller receives $`y`$ without learning $`e`$ or which reports were randomized. A true pointer may remain as a local quantum register and control a nearby counted gate. It is never provided noiselessly as classical advice to the global controller.

The charged theorem therefore cannot be converted to the noisy theorem by replacing bits with detector uses. Conversely, the noisy construction's simultaneous globally chosen Pauli corrections use free public feedforward; they are not a zero-cost correction protocol in the charged model. The respective [model](../science/model.md) and [noisy-readout account](../science/noisy-readout.md) make that boundary precise.

## Stabilizers and logical labels

### Convention translation

Preskill's site check $`X_s`$ is our star $`A_v`$; his plaquette check $`Z_P`$ is our $`B_p`$. No interchange of $`X`$ and $`Z`$ is needed. His §7.10.1 uses $`Y=ZX=i\sigma_y`$, with $`Y^2=-I`$. All operators needed below use the usual Hermitian $`X`$ and $`Z`$ directly.

| Chapter notation or role | Project convention |
|---|---|
| Physical code length $`n`$ | $`N=2L^2`$ |
| Encoded-qubit count $`k`$ | Two logical qubits |
| Code distance $`d`$ | $`L`$ for the square toric code |
| Spatial dimension in geometric code bounds | Fixed at two; project $`D`$ means circuit depth |
| Boundary map $`\partial_1`$ on edge chains | $`\partial`$ on binary sets of physical edges |

The construction also uses $`\lfloor L/\ell\rfloor`$ blocks per axis. That count is unrelated to the number of encoded qubits.

### The actual physical operators

Use coordinates $`(x,y)\in\mathbb Z_L^2`$, with $`L\ge2`$. Let $`h(x,y)`$ join $`(x,y)`$ to $`(x+1,y)`$ and $`v(x,y)`$ join $`(x,y)`$ to $`(x,y+1)`$. Each cell owns those two outgoing edge qubits. All coordinates are periodic. At $`L=2`$, edge labels still distinguish parallel physical edges.

The checks are

```math
\begin{aligned}
A_{x,y}
&=X_{h(x,y)}X_{h(x-1,y)}X_{v(x,y)}X_{v(x,y-1)},\\
B_{x,y}
&=Z_{h(x,y)}Z_{v(x+1,y)}Z_{h(x,y+1)}Z_{v(x,y)}.
\end{aligned}
```

A star and a plaquette share either zero or two edges, so their Pauli anticommutation signs cancel. The ground space is therefore well defined by

```math
P_{\mathrm{TC}}
=\prod_{x,y}\frac{I+A_{x,y}}2
 \prod_{x,y}\frac{I+B_{x,y}}2.
```

The two identities $`\prod A_{x,y}=I`$ and $`\prod B_{x,y}=I`$ leave $`N-2`$ independent constraints and a four-dimensional code space.

We fix the two logical labels using

```math
\overline Z_x=\prod_{x=0}^{L-1}Z_{h(x,0)},
\qquad
\overline Z_y=\prod_{y=0}^{L-1}Z_{v(0,y)}.
```

One compatible conjugate pair is

```math
\overline X_x=\prod_{y=0}^{L-1}X_{h(0,y)},
\qquad
\overline X_y=\prod_{x=0}^{L-1}X_{v(x,0)}.
```

Each $`\overline X_i`$ crosses its paired $`\overline Z_i`$ once, so they anticommute; differently indexed pairs commute. The subscripts label conjugate logical qubits, not identical directions of primal and dual paths.

Adding $`\overline Z_x=\overline Z_y=+1`$ to the stabilizers specifies a unique state $`|\psi_{++}\rangle`$. The [construction](../science/preparation.md) prepares this state. The converse uses the weaker requirement of reaching any state in the entire code space:

```math
F=\mathrm{Tr}(P_{\mathrm{TC}}\rho).
```

Consequently, its bound also applies to the squared fidelity $`\langle\psi_{++}|\rho|\psi_{++}\rangle`$, which is at most $`F`$.

## Syndromes and physical output

For a binary edge set $`E`$, define

```math
Z(E)=\prod_{e\in E}Z_e,
\qquad
(\partial E)_v=\bigoplus_{e\ni v}\mathbf1_{e\in E}.
```

An edge $`Z`$ anticommutes with the stars at its two endpoints. Thus $`Z(E)`$ changes the star-syndrome vector by $`\partial E`$. If a measured star has eigenvalue $`(-1)^{s_v}`$, a correction with

```math
\partial E=s
```

sets every star to $`+1`$. The necessary total-parity condition $`\bigoplus_v s_v=0`$ follows both from $`\prod_v A_v=I`$ and from the fact that each edge has two endpoints.

This boundary equation is the connection to the chain description in §§7.18.1–7.18.3. It also exposes a distinction between preparing a specified state and recovering an unknown encoded state. Unknown-state recovery must preserve the logical information; a correction in the wrong homology class can act as a nontrivial logical operator. Here the initial data are $`|0\rangle^{\otimes N}`$, which already fixes all plaquettes and both logical $`Z`$ values to $`+1`$. Star measurement preserves those values, and every subsequent $`Z`$ correction preserves them too. Any correction solving the boundary equation therefore reaches the same specified pure state. A minimum-weight decoder is unnecessary for this preparation task.

### Measurement alone does not prepare the requested physical state

For an even syndrome $`s`$, let

```math
P_s=\prod_v\frac{I+(-1)^{s_v}A_v}{2},
\qquad
|\phi_s\rangle=
2^{(L^2-1)/2}P_s|0\rangle^{\otimes N}.
```

Every even $`s`$ occurs with probability $`2^{-(L^2-1)}`$. One way to verify this is to expand $`P_s`$ into products of independent stars: every nonidentity product flips a nonempty computational-basis string and has zero expectation in $`|0\rangle^{\otimes N}`$.

If the classical record is discarded before correction, the data are

```math
\rho_{\mathrm{meas}}
=2^{-(L^2-1)}
\sum_{s:\,\oplus_v s_v=0}|\phi_s\rangle\langle\phi_s|,
\qquad
\mathrm{Tr}(P_{\mathrm{TC}}\rho_{\mathrm{meas}})
=2^{-(L^2-1)}.
```

A correct Pauli-frame description identifies how each branch could be corrected. It does not change this physical overlap. In an application that permits frame tracking, deferred corrections can be useful; this project's output criterion explicitly assesses the data before any unapplied correction. Moving the needed information to the correcting sites is therefore part of preparation.

## Locality and causal depth

The [model](../science/model.md) treats quantum operations and local classical propagation with the same spatial rule. One local layer is a product of channels on disjoint cell sets of diameter at most a fixed integer $`r`$. Every execution has at most $`D`$ such layers.

A record that traverses $`j`$ adjacent links serially has used $`j`$ local propagation steps, even if an implementation calls the sequence one controller round. Arbitrary computation on records already at one cell is free; transmitting them to another cell is not. Fresh measurements and outcome-controlled quantum gates remain counted local operations.

Following an operator backward through the circuit gives the exact causal radius

```math
R=rD.
```

Each layer can enlarge its support by at most $`r`$. Disjoint supports prevent a sequence of within-layer hops from being hidden inside one layer.

Nonlocal messages form a separate binary transcript $`\mathsf T`$. Its previous bits and the public seed determine the next sender, recipient, clock position, support schedule, and stopping decision. Private records can control actions within a scheduled support. They cannot secretly alter the public schedule. Zero messages are transmitted when scheduled; outcome-dependent silence cannot carry a free bit.

Complete transcripts are therefore prefix-free. This condition later connects the length of a physically executed protocol to Shannon entropy.

## Local channels and correlated environments

The preparation lower bound must permit resets, measurements, private records, and discarded ancillas. A proof for unitary circuits on the data alone would leave those operations uncovered.

### Retaining an environment preserves spatial locality

Condition on the shared classical seed and purify each initial local state at its own cell. Realize each local channel by a unitary on its support and fresh local environments. Retain all those environments, including measurement records and reset registers. The resulting unitary $`W`$ acts on a pure cell-product input $`|\boldsymbol0\rangle`$ and has the same support-spread bound:

```math
\mathrm{supp}(W^\dagger O_XW)
\subseteq X^{+rD}.
```

There is no bound on the finite number of ancillas at a cell. Their dimension does not change the set of cells touched by a gate.

Let $`\mathcal E`$ denote every retained register outside the data output. When $`F>0`$, define

```math
|\chi\rangle
=\frac{(P_{\mathrm{TC}}\otimes I_{\mathcal E})
W|\boldsymbol0\rangle}{\sqrt F},
\qquad
|\Omega\rangle=W^\dagger|\chi\rangle.
```

Then

```math
|\langle\boldsymbol0|\Omega\rangle|^2=F.
```

Every toric stabilizer acts as $`+1`$ on $`|\chi\rangle`$, but the logical state can remain entangled with $`\mathcal E`$. For example,

```math
\frac{|\psi_{++}\rangle|0\rangle_{\mathcal E}
      +|\psi_{-+}\rangle|1\rangle_{\mathcal E}}{\sqrt2}
```

is a valid code-space vector with an environment correlation. Here $`|\psi_{-+}\rangle`$ has logical $`Z`$ labels $`-1,+1`$. Projecting onto the whole code space does not remove such a correlation.

The proof uses stabilizer identities on $`|\chi\rangle`$ without assuming a product of a target state and an environment state. The projector above is an analytical device; no physical global test is supplied to the preparation protocol.

### A constant obstruction on every causal patch

The [local braiding proof](../science/local-braiding.md) constructs three dressed string operators on a patch partitioned as $`E\sqcup U\sqcup V`$. Their supports and actions satisfy

```math
\begin{gathered}
\mathrm{supp}(B)\subseteq E\cup U,\quad
\mathrm{supp}(B')\subseteq E\cup V,\quad
\mathrm{supp}(A)\subseteq U\cup V,\\
A|\Omega\rangle=|\Omega\rangle,\qquad
B|\Omega\rangle=B'|\Omega\rangle,\qquad
AB|\Omega\rangle=-B|\Omega\rangle.
\end{gathered}
```

The equality between the two open strings expresses deformability; the minus sign records a crossing with the closed string. Conjugation by $`W`$ preserves these identities and only thickens the strings by radius $`R`$.

Let $`P_{\mathcal P}`$ project all registers of that patch onto their initial product vector, and put

```math
|\phi\rangle=P_{\mathcal P}|\Omega\rangle,\qquad
p=\|\phi\|^2,\qquad e=\sqrt{1-p}.
```

The support relations give the norm estimates

```math
\|(A-I)B|\phi\rangle\|\le6e,
\qquad
\|(A+I)B|\phi\rangle\|\le2e.
```

Subtracting the two vectors and using unitarity of $`B`$ gives $`2\sqrt p\le8\sqrt{1-p}`$, hence $`p\le16/17`$. The companion proof derives the two estimates explicitly. No Hilbert-space dimension enters this calculation.

Patches of side $`32(rD+1)`$ can be packed in number

```math
m=\left\lfloor\frac{L}{32(rD+1)}\right\rfloor^2.
```

Project them successively onto their initial vectors. A previous patch projection commutes with the string operators of each untouched patch. The same $`16/17`$ bound therefore holds for each conditional projection probability. The patch states need not be independent.

The [channel-overlap theorem](../science/channel-overlap.md) concludes that every no-message local channel satisfies

```math
F\le q,\qquad
q=\left(\frac{16}{17}\right)^m.
```

This exponent counts spatial patches, not ancillas or measurement outcomes. The spatial mechanism and exponent are inherited from [Li–Lee–Yoshida](https://arxiv.org/html/2405.07970v3); the project states the local-channel and full-code-space argument explicitly.

## From overlap to communicated bits

### Keep the probability of a transcript

Fix a public seed and a complete transcript $`t`$. Its output contribution is a positive operator $`\sigma_t`$ with

```math
p_t=\mathrm{Tr}\sigma_t,\qquad
a_t=\mathrm{Tr}(P_{\mathrm{TC}}\sigma_t).
```

The normalized branch $`\sigma_t/p_t`$ might have perfect overlap even when $`p_t`$ is tiny. The no-message theorem cannot simply be applied to that normalized postselection.

Instead, preprogram all remote control bits to their values in $`t`$ and remove the sender-side consistency checks. For a stored classical record with bit projectors $`Q_0,Q_1`$, the selected map $`X\mapsto Q_bXQ_b`$ is dominated in completely positive order by

```math
X\longmapsto Q_0XQ_0+Q_1XQ_1.
```

The latter acts as the identity on valid classical records, even when correlated with quantum data. It adds no quantum layer. Private outcomes remain local and are averaged rather than fixed. The resulting no-message channel has output $`\widehat\rho_t`$ with

```math
0\le\sigma_t\le\widehat\rho_t,\qquad a_t\le q.
```

The [communication proof](../science/communication-bound.md) establishes this operator inequality by composing the completely positive map inequalities.

### Hard and mean message lengths

A binary prefix tree with maximum leaf depth $`C`$ has at most $`2^C`$ leaves. Therefore

```math
F=\sum_t a_t\le\min\{1,2^Cq\}.
```

For mean length $`\overline C=\mathbb E\,\ell(\mathsf T)`$, the corresponding statement is

```math
\overline C
\ge H(\mathsf T\mid\mathsf S)
\ge\max\left\{0,F\log_2\frac Fq\right\}.
```

Here $`\mathsf S`$ is the free shared classical seed; it must be conditioned out. The convention at $`F=0`$ is $`0\log_2(0/q)=0`$.

The entropy step can be seen without any additional textbook prerequisite. Imagine a mathematical binary variable $`G`$ whose joint probability of $`t`$ and $`G=1`$ is $`a_t`$. For a fixed seed with ground-space weight $`F_s>0`$,

```math
\Pr(t\mid G=1,s)=\frac{a_t}{F_s}\le\frac q{F_s}.
```

No outcome of this distribution is more likely than $`q/F_s`$, so its entropy is at least $`\log_2(F_s/q)`$. Entropy concavity gives

```math
H(\mathsf T\mid s)\ge
F_s H(\mathsf T\mid G=1,s)
\ge F_s\log_2(F_s/q).
```

Averaging over the seed uses convexity of $`x\log_2(x/q)`$. Finally, prefix-free physical words satisfy Kraft's inequality, which implies mean length at least Shannon entropy. The full proof handles almost sure termination, countably many transcripts, zero-probability branches, and infinite mean length.

The imagined variable $`G`$ is used only in the inequality. It is not a free physically distributed success flag.

## The matching construction

Choose an integer $`1\le\ell\le L`$. Partition each coordinate axis into $`k_{\mathrm{blk}}=\lfloor L/\ell\rfloor`$ balanced consecutive intervals. Their lengths lie between $`\ell`$ and $`2\ell-1`$, giving $`B=k_{\mathrm{blk}}^2`$ blocks.

The [exact preparation](../science/preparation.md) has three stages:

1. Measure all stars and sweep each block's syndrome toward its root using local $`Z`$ corrections. Only the block parity remains.
2. Collect the $`B-1`$ noncontroller root parities. Solve the boundary equation on a fixed coarse comb tree.
3. Return correction coefficients to the roots that own the relevant paths, then propagate each coefficient locally while applying its physical $`Z`$ string.

For a coarse tree edge from child $`b`$ to its parent, the coefficient is

```math
z_b=\bigoplus_{b'\text{ in the subtree of }b}p_{b'}.
```

At each coarse vertex, the incident coefficients have XOR equal to its root parity. Replacing every coarse edge by a physical path therefore corrects precisely the residual root syndrome.

The finite bounds are

```math
D\le12\ell+2,\qquad
C\le2(B-1)\le\frac N{\ell^2}.
```

The message count includes return traffic and zero bits. When $`B=1`$, no nonlocal bit is needed and $`D\le2L+8`$.

Conversely, write $`\lambda=\log_2(17/16)`$. For $`F\ge f>0`$ the hard-cost bound requires

```math
C\ge\lambda m-\log_2(1/f).
```

The exact floor may vanish at large depth. A uniform formulation retains the local endpoint:

```math
(C+1)(D+1)^2
\ge
\frac{\lambda N}
{8192r^2\max\{1,\log_2(1/f)+\lambda\}}.
```

The mean-cost counterpart is

```math
(\overline C+1)(D+1)^2
\ge\frac{f\lambda N}{8192r^2}.
```

At fixed $`r`$ and fixed nonzero target overlap, the construction attains the scaling of both bounds. The geometric reason is that depth of order $`\ell`$ permits local processing over an area of order $`\ell^2`$, leaving one item of global coordination per block.

## Worked four-block correction

This example follows the canonical construction on an $`L=4`$ torus with $`\ell=2`$. It uses $`N=32`$ data qubits, 16 star-measurement ancillas, and four $`2\times2`$ blocks. Denote the blocks by $`\mathsf A,\mathsf B,\mathsf C,\mathsf D`$; these letters label blocks, not stabilizer operators.

| Block | Vertices | Root | Coarse parent |
|---|---|---|---|
| $`\mathsf A`$ | $`x,y\in\{0,1\}`$ | $`(0,0)`$ | Controller |
| $`\mathsf B`$ | $`x\in\{2,3\},\ y\in\{0,1\}`$ | $`(2,0)`$ | $`\mathsf A`$ |
| $`\mathsf C`$ | $`x\in\{0,1\},\ y\in\{2,3\}`$ | $`(0,2)`$ | $`\mathsf A`$ |
| $`\mathsf D`$ | $`x,y\in\{2,3\}`$ | $`(2,2)`$ | $`\mathsf C`$ |

Take the measured syndrome with defects only at $`(1,1)`$ and $`(3,3)`$. Its parity is even, so it is a possible branch, with probability $`2^{-15}`$.

### Local sweeps

The row sweeps apply $`Z`$ on $`h(0,1)`$ and $`h(2,3)`$. The column sweeps then apply $`Z`$ on $`v(0,0)`$ and $`v(2,2)`$. Thus

```math
E_{\mathrm{sweep}}
=\{h(0,1),h(2,3),v(0,0),v(2,2)\}.
```

The remaining root parities are

```math
(p_{\mathsf A},p_{\mathsf B},p_{\mathsf C},p_{\mathsf D})
=(1,0,0,1).
```

All 12 local tree-edge operations execute; only four have nonzero correction values on this branch. They fit in one row layer and one column layer.

### Exactly four delivered bits

The fixed nonlocal schedule is:

| Bit | Sender → recipient | Meaning | Value |
|---:|---|---|---:|
| 1 | $`\mathsf B\to\mathsf A`$ | $`p_{\mathsf B}`$ | 0 |
| 2 | $`\mathsf C\to\mathsf A`$ | $`p_{\mathsf C}`$ | 0 |
| 3 | $`\mathsf D\to\mathsf A`$ | $`p_{\mathsf D}`$ | 1 |
| 4 | $`\mathsf A\to\mathsf C`$ | $`z_{\mathsf D}=p_{\mathsf D}`$ | 1 |

The transcript is $`0011`$ and $`C=4`$. The first two zero bits count. The controller already holds the other two coarse instructions:

```math
z_{\mathsf B}=p_{\mathsf B}=0,\qquad
z_{\mathsf C}=p_{\mathsf C}\oplus p_{\mathsf D}=1.
```

The parent owns each path. Accordingly, $`\mathsf C`$ needs the returned bit to correct its path to $`\mathsf D`$; that instruction was not delivered to $`\mathsf C`$ by the earlier point-to-point collection.

### Physical paths and the final state

The nonzero coarse corrections are

```math
\begin{aligned}
\mathsf A\text{ to }\mathsf C &: \{v(0,0),v(0,1)\},\\
\mathsf C\text{ to }\mathsf D &: \{h(0,2),h(1,2)\}.
\end{aligned}
```

The zero instruction for $`\mathsf A`$ to $`\mathsf B`$ also traverses its two scheduled local hops. Because $`v(0,0)`$ is corrected once in each stage, its two $`Z`$ factors cancel. The net correction is

```math
E_{\mathrm{net}}
=\{h(0,1),v(0,1),h(0,2),h(1,2),v(2,2),h(2,3)\}.
```

This is a path from $`(1,1)`$ to $`(3,3)`$, so its only boundary vertices are the original defects. All stars become $`+1`$. Plaquettes and logical $`Z`$ labels remain $`+1`$, yielding $`|\psi_{++}\rangle`$.

Eight conditional single-edge $`Z`$ applications occur on this branch, with six edges in their net product. This distinction has no effect on correctness.

### Exact resource ledger

| Resource or phase | Count in this fixed implementation |
|---|---:|
| Data qubits | 32 |
| Star-measurement ancillas | 16 |
| Star outcomes | 16 bits, subject to one parity constraint |
| Ancilla preparation + six CNOT layers + readout | 8 local layers |
| Row and column sweeps | 2 local layers |
| Horizontal paths, then vertical path | 4 local layers |
| Total local depth | $`D=14`$ |
| Collected nonlocal bits | 3 |
| Returned nonlocal bits | 1 |
| Total delivered bits | $`C=4`$ |

The local routing uses two horizontal hop layers followed by two vertical hop layers. Each layer's active site pairs are disjoint. Globally empty parity-color sublayers are omitted using the known geometry; outcome-dependent zero instructions remain in the schedule.

The same depth and message schedule works for all $`2^{15}`$ allowed original syndromes. The four root parities are uniform on their eight even patterns. Consequently $`(p_{\mathsf B},p_{\mathsf C},p_{\mathsf D})`$ is uniform on three bits, while the fourth transmitted value repeats the third. Thus

```math
H(\mathsf T)=3,\qquad \ell(\mathsf T)=C=4.
```

Entropy measures uncertainty of the complete transcript. Delivered-bit cost also records that a value must reach another recipient. The example does not assert that four is the smallest possible finite communication cost.

For the unconditional states, star measurement alone gives $`F=2^{-15}`$; local sweeps give $`F=1/8`$; completing all corrections gives $`F=1`$. These are ensemble overlaps, not the probability of accepting only a favorable branch.

The [construction verifier](../tools/verify_construction.py) reproduces the $`14`$ layers, four messages, net edge set, and boundary. Checking its eight root-parity inputs gives the eight distinct transcripts $`0000,0011,0100,0111,1000,1011,1100,1111`$. This finite example illustrates the construction and accounting. Its lattice is too small for the explicit braiding-patch exponent to be nontrivial.

## The local two-loop test

The original converse projects onto the entire toric ground space. A locally blind region needs a test supported strictly inside that region. Use the closed $`X`$ cut $`A_0`$ and the two alternative open $`Z`$ strings $`B_0,B'_0`$ from the braiding patch. Their product $`C_0=B_0B'_0`$ is a closed stabilizer loop. The two closed loops commute, so

```math
K=\frac{I+A_0}{2}\frac{I+C_0}{2}
```

is a projector, with $`P_{\mathrm{TC}}\preceq K`$. These are local contractible loop constraints; no logical-sector eigenvalue is tested.

A vector in the range of $`K`$ satisfies $`A_0\chi=\chi`$ and $`B_0\chi=B'_0\chi`$. The operator relation $`A_0B_0=-B_0A_0`$ supplies the third braiding identity. Projecting a local-channel output onto $`K`$ and pulling it back through a local dilation therefore reuses the dimension-independent inequality already explained above. On a side-$`32(R+1)`$ core, with $`R=rT`$, every fixed-schedule depth-$`T`$ local CPTP circuit from a cell-product input obeys

```math
\mathrm{Tr}(K\rho)\le c,\qquad c=\frac{16}{17}.
```

The geometry and algebra are inherited from the [local braiding account](../science/local-braiding.md), which credits Li–Lee–Yoshida. The extra question is whether this deficit survives arbitrary outside records and global report-dependent control.

## Buffered blindness with outside records

Place that core inside a square blind block of side $`36(R+1)`$, offset by $`2(R+1)`$ cells on each side. The distance from the core to the block's complement is greater than $`2R`$. Suppose every report originating in the block is a fair coin independent of its true outcome. Outside reports may still be informative.

Freeze a full public history. This fixes all public choices of gates, instruments, and support schedules. An inside fair report has probability $`1/2`$ regardless of the true outcome; summing that outcome gives the corresponding nonselective CPTP instrument. Retained pointer outputs and later local pointer-controlled gates remain in this channel.

Outside outcomes require a different order of operations. A selected outside instrument is trace decreasing. One cannot remove it using the trace-preserving cancellation valid for an averaged measurement. Instead complete it to the CPTP map

```math
\mathcal J(X)=\sum_x\mathcal I_x(X)\otimes|x\rangle\langle x|_{\mathsf R},
```

and retain its outcome register $`\mathsf R`$ at the place and time of creation. Retain every outside final system on which a later test will act. These mathematical registers are used only to recover the branch weights; they create no extra control interface.

The core's backward quantum cone and the cones of those outside retained histories are disjoint because of the buffer. After unretained trace-preserving operations are canceled, the fixed-history CPTP state factors between the core and those outside outputs. **Now** select the outside record values and apply any positive outside effect $`H`$. Their contribution is a nonnegative scalar multiplying the core state, so the uniform local deficit survives:

```math
\mathrm{Tr}(KH\Omega)\le c\,\mathrm{Tr}(H\Omega).
```

Here $`\Omega`$ is the subnormalized physical output selected by any public-history event, and $`K,H`$ act on disjoint supports. The actual adaptive output need not factor. The proof needs only the CPTP factorization before outside selection. This retained-record discipline is the ingredient imported from the [blind-strip proof of Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b/science/blind_strip.md).

## From blind cores to a depth bound

Pack

```math
M=\left\lfloor\frac{L}{36(rT+1)}\right\rfloor^2
```

disjoint blind blocks. Apply the previous trace inequality successively, taking $`H`$ to include already selected tests in other blocks. If $`j`$ blocks have blind reports, the output passes all their core tests with probability at most $`c^j`$. This multiplication does not assume independent quantum core marginals.

A BSC has a useful hidden representation: with probability $`1-2p`$ it reports the true value, and with probability $`2p`$ it reports an independent fair bit. The controller does not receive the choice flag. Pad each block to its allowed maximum

```math
k=\nu[36(rT+1)]^2T
=1296\nu(rT+1)^2T
```

potential report slots, including unused slots. All $`k`$ hidden choices are fair with probability $`(2p)^k`$, independently for disjoint spatial blocks. Average the conditional $`c^j`$ bound over this flag table:

```math
F\le\left[1-\frac{(2p)^k}{17}\right]^M
\le\exp\!\left[-\frac{M(2p)^k}{17}\right].
```

For fixed $`p,r,\nu`$ and a fixed required $`F\ge f>0`$, there are of order $`L^2/T^2`$ spatial opportunities for blindness, while each block contains only $`O(T^3)`$ detector slots. Keeping their total failure probability bounded forces $`T^3=\Omega(\log L)`$. If no block fits, the finite bound is simply $`F\le1`$; that regime is already at linear depth in $`L`$. Together these cases give the fixed-parameter lower order.

The finite estimate is sufficient for the fixed-detector theorem. Its constants are not uniform as the detector becomes uninformative. The [full noisy-readout account](../science/noisy-readout.md) keeps that limitation separate from the matched fixed-parameter conclusion; it does not establish a uniformly matched crossover in $`p`$, accuracy, and the linear-depth cap.

## Physical compression before readout

Protecting every raw star report separately wastes the blocks that local gates can already correct. First extract the true star syndrome coherently into one pointer per vertex. Site-local dephasing of those pointers, with no public outcome, gives

```math
2^{-(L^2-1)}
\sum_{s:\,\oplus_v s_v=0}
|\psi_s\rangle\langle\psi_s|_{\mathsf D}
\otimes|s\rangle\langle s|_{\mathsf A}.
```

The canonical data branch $`|\psi_s\rangle`$ has star syndrome $`s`$, all plaquettes $`+1`$, and both selected logical $`Z`$ labels $`+1`$. The branches satisfy

```math
Z(E)|\psi_s\rangle=|\psi_{s\oplus\partial E}\rangle.
```

Partition the torus into balanced rectangles with side lengths in $`[b,2b-1]`$. Use the local comb sweep of the original preparation, but implement each step through the pointers. For a child and parent with consistent data/pointer bits $`(a,b')`$, apply:

1. CNOT from child pointer to parent pointer.
2. Child-pointer-controlled $`Z`$ on the shared data edge.
3. Reset the child pointer to zero without exposing a report.

The data's child syndrome becomes zero; the parent's data and pointer both become $`a\oplus b'`$. The child pointer remains unchanged until it has controlled the edge correction. Reset then transfers its discarded detail to an inaccessible environment. Three elementary layers implement this step on disjoint scheduled cell pairs.

Induction leaves every nonroot star satisfied, every nonroot pointer zero, and each root pointer equal to its **actual remaining data defect**. If there are $`B=\lfloor L/b\rfloor^2`$ blocks, the root vector is uniform on the even $`B`$-bit subspace. The controller will need only $`B-1`$ independent bits.

This is physical syndrome compression. Computing a parity of already noisy raw reports would not satisfy the data/pointer invariant. For comparison, correcting an estimate formed from $`L^2-1`$ independently reported raw syndrome bits succeeds with probability $`(1-p)^{L^2-1}`$ in the simple one-report scheme. Discarding entropy is useful here because the local gates have already removed the corresponding physical defects.

## Protected pointer readout and the delivered state

The nonroot pointers freed by compression provide a readout bank without increasing quantum memory. Copy a root's orthogonal basis value along its row and then up the columns. This fills its rectangle of area $`A_j\ge b^2`$ in $`O(b)`$ local layers. It copies one classical basis label, rather than cloning an arbitrary unknown state.

Read every pointer copy nondestructively for $`t`$ rounds. Every true value in that block is the same root bit; each public report has its own independent flip. Root $`j`$ therefore has $`A_jt`$ reports. Majority with a fair random tie has error

```math
e_m(p)=\Pr[\mathrm{Bin}(m,p)>m/2]
+\frac12\Pr[\mathrm{Bin}(m,p)=m/2]
\le e^{-\mathcal D(p)m},
\qquad
\mathcal D(p)=-\frac12\log[4p(1-p)].
```

The Chernoff exponent and pointer amplification are established ingredients attributed in the [related-work account](../references/related-work.md) and in Readout Entanglement Limits. The local implementation and available block area are essential to their use here.

Decode $`B-1`$ roots and infer the final root from the exact even-parity constraint. Compute a physical edge set whose boundary is the estimated root syndrome. In this model free global classical feedforward permits every chosen single-qubit $`Z`$ correction to be applied in one counted layer. The same statement would require transported return instructions in the charged-communication model.

After these actual gates the residual syndrome is the true root vector XOR its estimate. It vanishes exactly when every independently decoded root is correct, so

```math
F_{\mathrm{phys}}
=\prod_{j=1}^{B-1}[1-e_{A_jt}(p)],
\qquad
1-F_{\mathrm{phys}}
\le(B-1)e^{-\mathcal D(p)b^2t}.
```

Several wrong root estimates do not become harmless merely because their parity is even: they still leave nonzero physical star defects. The formula averages every true syndrome, report error, and tie coin. It is neither success-conditioned fidelity nor a Pauli-frame claim.

## Small protected-readout example

Take $`L=4`$, four $`2\times2`$ blocks, $`t=3`$ readout rounds, and $`p=1/10`$. There are 32 data qubits and 16 reusable pointers, hence 48 quantum memory qubits. Each root is copied to its four pointer sites and receives 12 reports; all four blocks together use 48 report slots. Decode three roots and infer the fourth from even parity.

For one root,

```math
e_{12}(1/10)=\frac{1848163}{6250000000}
=0.00029570608.
```

The unconditional corrected physical overlap is therefore

```math
F_{\mathrm{phys}}=[1-e_{12}(1/10)]^3
\approx0.9991131441.
```

The general conservative schedule gives $`T\le16b+t-4=31`$ layers. It includes coherent extraction, dephasing, local compression, pointer fanout, three readouts, and the final physical correction. This finite example illustrates the exact ensemble and resource accounting; its lattice is too small for the explicit blind-core lower bound to be nontrivial. It is also a different implementation and classical interface from the earlier four-message example.

## The fixed-detector preparation law

For general balanced blocks, coherent extraction takes at most ten elementary layers. Write $`d_{\mathrm{sweep}}\le4b-4`$ for the number of child-parent levels in the row/column schedule. Dephasing, compression, fanout, QND readout, and final correction yield

```math
T\le10+1+3d_{\mathrm{sweep}}+d_{\mathrm{sweep}}+t+1
\le16b+t-4.
```

This construction uses exactly three qubits per cell, nearest-neighbor gates, and one report per cell per readout round. Choose $`t=b`$. Then its depth is $`O(b)`$ and its decoding failure bound is $`(B-1)e^{-\mathcal D(p)b^3}`$. At fixed $`p`$ and target $`F_0\in(0,1)`$, taking $`b`$ of order $`(\log L)^{1/3}`$ makes the physical output meet that target. A single block gives the exact ordinary linear-depth fallback without noisy root decoding.

Combining this construction with the independent blind-core lower bound establishes

```math
T_{\mathrm{det}}(L,p;F_0)
=\Theta_{p,F_0}\!\left((\log L)^{1/3}\right)
```

for fixed range/report density and an admissible fixed local-memory budget containing the three-qubit construction. The lower bound permits arbitrary larger finite local Hilbert spaces at the same report density.

Only reports are noisy. Reliable gates, storage, dephasing and reset are central to the construction. Repeatable QND pointer readout is also an explicit resource: a destructive detector can use an additional reusable readout qubit per cell, keeping constant density but changing the exact three-qubit implementation. Neither version establishes noisy-gate fault tolerance or a finite-speed classical-latency theorem.

## What the chapter does and does not supply

The chapter provides the stabilizer, logical-operator, and chain language in the source map. The following ingredients are supplied by the project and its primary research antecedents:

| Additional ingredient | Where its argument is given |
|---|---|
| Exact local causal model and charged public schedule | [Model](../science/model.md) |
| Dimension-independent braiding inequality and explicit patch geometry | [Local braiding](../science/local-braiding.md) |
| Projection onto the full code space with correlated environments | [Channel overlap](../science/channel-overlap.md) |
| Positive branch domination and hard/mean transcript bounds | [Communication bound](../science/communication-bound.md) |
| Local compression, collected and returned messages, physical correction | [Preparation](../science/preparation.md) |
| What follows under an additional aggregate-throughput assumption | [Consequences](../science/consequences.md) |
| Buffered two-loop test and retained outside-record conditioning | [Noisy readout](../science/noisy-readout.md) |
| Fixed-memory pointer compression, protected reports, and physical overlap | [Noisy readout](../science/noisy-readout.md) |
| Which mechanisms and results are inherited | [Related work](../references/related-work.md) |

Both results address unconditional global ground-space overlap from spatially unentangled initial resources, with a depth cap on every branch. The charged-communication construction is exact in its stated circuit model. The noisy-report extension has a matching fixed-detector depth theorem at constant quantum-memory density, with ideal gates/storage and independent imperfect classical reports. Neither upper construction establishes a noisy-gate fault-tolerance threshold.

A low density of violated checks is a different target from global ground-space weight. A classical description of a future correction is a different output from an already corrected data state. A bit budget is also distinct from laboratory latency: signal speed, controller runtime, and aggregate bandwidth require their own physical assumptions. These distinctions determine where the matched communication–depth frontier applies.

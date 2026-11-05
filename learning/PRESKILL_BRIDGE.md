# From Preskill's quantum error correction chapter to topological communication cost

This bridge connects the stabilizer description of a toric code to the cost of preparing its physical state. The question is: after allowing local quantum operations and local classical propagation for depth $`D`$, how many classical bits must still travel outside those local layers?

The educational anchor is John Preskill, [*Quantum Information*, Chapter 7: *Quantum Error Correction*, March 2026 author draft](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf), listed on the [author's course page](https://www.preskill.caltech.edu/ph219/index.html). The chapter supplies the code language. The preparation model, probability accounting, and quantitative bounds developed below come from this project's [science pages](../science/README.md) and their [research references](../references/related-work.md).

The [milestone map](MILESTONES.md) gives a dependency order for the material. This page supplies the explanations, conventions, and a complete finite example.

## Source map

The table gives section starting pages. Printed page $`p`$ is physical PDF page $`p+6`$ in this 92-page file. The PDF contains unfinished passages in §§7.18.2–7.18.3; §7.18.4 is only a heading. The bridge uses the definitions and equations actually present.

| Chapter section | Printed page / PDF page | Connection developed here |
|---|---:|---|
| §7.2; §§7.3.2–7.3.3 | 4 / 10; 9 / 15 | [Channels and environments](#local-channels-and-correlated-environments) |
| §7.7 | 21 / 27 | Separate $`X`$ and $`Z`$ checks |
| §§7.10.1–7.10.2 | 27 / 33; 30 / 36 | [Stabilizers and commutation](#stabilizers-and-logical-labels) |
| §7.10.4 | 33 / 39 | Logical Pauli operators |
| §7.14 | 43 / 49 | Changing an operator's support using stabilizers |
| §7.18.1 | 52 / 58 | Toric checks and logical sectors |
| §§7.18.2–7.18.3 | 54 / 60; 55 / 61 | [Boundaries and correction](#syndromes-and-physical-output) |
| §7.19 | 60 / 66 | Geometric restrictions on code parameters |
| §7.20 | 63 / 69 | Strings and energy barriers |

The last two sections give geometric background. Their code-parameter and thermal-memory questions are distinct from the preparation-resource theorem here.

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
| Which mechanisms and results are inherited | [Related work](../references/related-work.md) |

The theorem addresses unconditional global ground-space overlap from spatially unentangled initial resources. It allows arbitrary finite local ancillas and local channels, and requires a depth cap on every branch. The construction is exact in that circuit model; it does not analyze faulty measurement or gate noise.

A low density of violated checks is a different target from global ground-space weight. A classical description of a future correction is a different output from an already corrected data state. A bit budget is also distinct from laboratory latency: signal speed, controller runtime, and aggregate bandwidth require their own physical assumptions. These distinctions determine where the matched communication–depth frontier applies.

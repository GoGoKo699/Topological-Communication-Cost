# Toric-code preparation with noisy measurement reports

Independent errors in measurement reports impose a preparation-depth cost even when global classical processing is free. In two dimensions, a local syndrome sweep can physically remove most defects before any report is read. One protected pointer then remains for each block. Its orthogonal copies occupy a block area and can be read repeatedly, providing order $`T^3`$ independent reports per surviving syndrome bit at depth $`T`$. A buffered local two-loop test proves that arbitrary competing protocols cannot avoid the corresponding logarithmic requirement.

For fixed detector crossover probability $`p\in(0,1/2)`$ and any fixed required physical ground-space overlap $`F_0\in(0,1)`$, the resulting optimum is given below. Achievability assumes at least three memory qubits per toric cell and an operation set containing ideal nearest-neighbor CNOT, controlled-$`Z`$, reset, local dephasing, one-qubit gates and QND pointer readout; the converse permits arbitrary local CPTP maps.

```math
T_{\mathrm{opt}}(L,p;F_0)
=\Theta_{p,F_0}\!\bigl((\log L)^{1/3}\bigr).
```

This is a theorem in the **noisy-report model defined below**. The [charged-communication frontier](communication-bound.md) remains a different result: there nonlocal bits cost communication, whereas here reported bits can be communicated freely and their reliability is the limiting resource. The present theorem does not assert a uniform detector-quality/accuracy crossover.

The authoritative two-dimensional proof is this page. Its sister project, [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits), supplies the retained-outside-record method and protected-pointer readout; its [two-dimensional companion account](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/main/science/toric_extension.md) explains their relation to the one-dimensional Bell-pair theorem. The inherited ingredients and their exact source versions are identified in [Section 8](#8-attribution-and-boundaries).

## 1. Physical model and target

Let $`L\ge2`$ and let the cells form $`\Lambda_L=(\mathbb Z/L\mathbb Z)^2`$, with cyclic $`\ell_\infty`$ distance. Cell $`(x,y)`$ owns the east-going data qubit $`h_{x,y}`$ and north-going data qubit $`v_{x,y}`$. Thus there are $`N=2L^2`$ designated data qubits. The stabilizers are

```math
\begin{aligned}
A_{x,y}
&=X_{h_{x,y}}X_{h_{x-1,y}}X_{v_{x,y}}X_{v_{x,y-1}},\\
B_{x,y}
&=Z_{h_{x,y}}Z_{v_{x+1,y}}Z_{h_{x,y+1}}Z_{v_{x,y}},\\
P_{\mathrm{TC}}
&=\prod_{x,y}\frac{I+A_{x,y}}2
  \prod_{x,y}\frac{I+B_{x,y}}2.
\end{aligned}
```

The parallel edge labels at $`L=2`$ remain distinct physical qubits. Conditional on any shared classical seed, the initial quantum state is a product across cells. There is no initially shared quantum entanglement. A cell has a fixed number $`q`$ of physical memory qubits; the construction below uses $`q=3`$, consisting of its two data qubits and one reusable pointer. The converse even permits arbitrary finite local dimension.

A protocol has at most $`T`$ synchronous local layers on every branch, padded with idle layers after early stopping. Each layer consists of quantum channels on disjoint cell supports of diameter at most fixed integer $`r\ge1`$. Readout layers and actual correction gates count in $`T`$. Sequential overlapping gates or repeated readouts require separate layers. Locally retained quantum records, reset, local dephasing and discarded environments are allowed. Retained quantum systems obey the memory and range restrictions; environments supply no preshared entanglement.

Every classical use of a fresh binary outcome $`x`$ crosses a site-local independent binary symmetric channel:

```math
y=x\oplus e,\qquad \Pr(e=1)=p,\qquad 0\lt p\lt 1/2.
```

There are at most $`\nu`$ potential binary report slots per cell and layer, where $`\nu\ge1`$ is a fixed positive integer. Every potential slot, including an unused one, has its own independent noise variable. No flip is reused. Instruments and subsequent gates may depend on all earlier public reports and shared randomness; reports from a layer become available for the next layer. The controller has unrestricted global classical computation and communication of these reports. It cannot see true outcomes, realized flips, or a flag identifying a truthful component of a detector decomposition. Outcome-dependent timing, measurement presence or another side interface cannot reveal an extra noiseless copy.

An outcome may remain in a local **quantum pointer**. Local gates may coherently process or copy its orthogonal basis states, at counted depth. That permission supplies no noiseless classical outcome to a distant controller. Fixed-range measurement interfaces must be implemented by counted local gates and site-local readout before applying the stated slot count.

The output criterion is the unconditional physical overlap

```math
F=\mathrm{Tr}(P_{\mathrm{TC}}\rho_{\mathrm{out}}).
```

All report-dependent corrections have actually acted before $`\rho_{\mathrm{out}}`$ is evaluated. An unapplied Pauli-frame description, a selected syndrome sector, a signed observable estimator, small energy density and decoded logical fidelity with residual defects are different outputs. The theorem below concerns deterministic preparation under this unconditional criterion. Ideal coherent gates, storage, reset and QND pointer readout are used for the upper bound; only the public reports are noisy.

## 2. A local two-loop test

Set $`R=rT`$ and $`s=R+1`$. The [explicit braiding geometry](local-braiding.md#3-an-explicit-braiding-patch) fits in a nonwrapping side-$`32s`$ patch $`\mathcal P`$. Its primal endpoints are $`p_*=(6s,12s)`$ and $`q_*=(26s,12s)`$. Two paths join them through heights $`22s`$ and $`2s`$:

```math
\begin{aligned}
\gamma_+ &:p_*\to(6s,22s)\to(26s,22s)\to q_*,\\
\gamma_- &:p_*\to(6s,2s)\to(26s,2s)\to q_*.
\end{aligned}
```

Let $`B_0=Z(\gamma_+)`$, $`B'_0=Z(\gamma_-)`$, and define

```math
\begin{aligned}
A_0&=\prod_{x=3s}^{9s}\prod_{y=8s}^{16s}A_{x,y},\\
C_0&=B_0B'_0
=\prod_{x=6s}^{26s-1}\prod_{y=2s}^{22s-1}B_{x,y},\\
K&=\frac{I+A_0}{2}\frac{I+C_0}{2}.
\end{aligned}
```

The two closed loops $`A_0,C_0`$ are contractible stabilizer products, and they commute. They are not noncontractible logical-loop tests. Each open string anticommutes with $`A_0`$. Every toric ground state passes $`K`$, so $`P_{\mathrm{TC}}\preceq K`$.

**Local test lemma.** Every depth-$`T`$ nonadaptive local CPTP circuit on a cell-product input obeys

```math
\mathrm{Tr}(K\rho)\le c,\qquad c=16/17,
```

when this patch fits. Local dimension, retained records and discarded environments are unrestricted.

**Proof.** Purify the input separately at every cell and dilate each local channel while retaining its environment. This gives a unitary $`W`$ with support spread at most $`R`$ and a cell-product input $`|\boldsymbol0\rangle`$. If $`z=\mathrm{Tr}(K\rho)\gt 0`$, define

```math
|\chi\rangle
=\frac{(K\otimes I_{\mathrm{env}})W|\boldsymbol0\rangle}{\sqrt z},
\qquad
|\Omega\rangle=W^\dagger|\chi\rangle.
```

The range of $`K`$ gives $`A_0|\chi\rangle=|\chi\rangle`$ and $`B_0|\chi\rangle=B'_0|\chi\rangle`$. Anticommutation also gives $`A_0B_0|\chi\rangle=-B_0|\chi\rangle`$. Conjugating these relations by $`W`$ supplies the three state identities of the [dimension-independent algebra lemma](local-braiding.md#1-dimension-independent-algebra-lemma). The [explicit dressed-support partition](local-braiding.md#4-dressed-supports-and-the-endpoint-regions) places all three operators in $`\mathcal P`$ and satisfies that lemma's support conditions. Hence

```math
z=|\langle\boldsymbol0|\Omega\rangle|^2
\le
\langle\Omega|
\bigl(|0_{\mathcal P}\rangle\langle0_{\mathcal P}|\otimes I\bigr)
|\Omega\rangle
\le16/17.
```

No factorization of $`|\chi\rangle`$ from the environments is assumed. Local purification and averaging cover mixed factors and shared randomness. The $`z=0`$ case is immediate. $`\square`$

The only change from the [full-code-space channel proof](channel-overlap.md) is that projection onto $`K`$ already supplies the required local string identities. This localization is what permits a buffered blind-core argument.

## 3. Buffered blind-core lemma

Take a square $`\mathcal B`$ of side $`b_{\mathrm{blind}}=36s`$. Put the side-$`32s`$ patch $`\mathcal P`$ at offset $`(2s,2s)`$ inside it. In the cyclic metric,

```math
\mathrm{dist}_\infty(\mathcal P,\mathcal B^c)
\ge2s+1\gt 2R.
```

Assume $`L\ge36s`$. Suppose every report originating in $`\mathcal B`$ is an independent fair coin, independent of the physical outcome and the preceding history. Outside $`\mathcal B`$, reports may follow the original BSC, fixed flip bits, fixed truthful/fair assignments, or mixtures of these alternatives.

Let $`H\ge0`$ be an effect on final quantum outputs outside $`\mathcal B`$; in particular, it may be a product of tests on other cores. Let $`\Omega`$ be a subnormalized output selected or positively weighted by allowed public information.

**Buffered lemma.** The translated core test satisfies

```math
\mathrm{Tr}[(K\otimes H)\Omega]
\le c\mathrm{Tr}[(I\otimes H)\Omega],
\qquad c=16/17.
```

The outside effect is a mathematical device. This statement does not supply the protocol with an extra physical nonlocal measurement or an ideal success flag.

### Retain outside records before conditioning

Fix shared randomness and a complete public transcript $`y`$. It fixes the chosen instruments, local maps and layer supports, including the policy evaluated on every successive public prefix. Refine this record by the true outcomes of all measurements originating **outside** $`\mathcal B`$. Inside true outcomes are not selected.

For a fixed inside public report, the report probability is $`1/2`$ for either true outcome. Its quantum contribution is the nonselective CPTP sum $`\mathcal I_0+\mathcal I_1`$, with a scalar $`1/2`$ extracted. The output of this sum includes any retained local pointer, so later pointer-controlled quantum gates remain represented. All later classical choices are already fixed by $`y`$.

An outside selected map $`\mathcal I_x`$ is trace decreasing and cannot be canceled. Replace it by the CPTP map

```math
\mathcal C(\rho)
=\sum_x\mathcal I_x(\rho)\otimes|x\rangle\langle x|_{R_x}.
```

Retain $`R_x`$ at its measurement time without using it for extra control. Also retain the core data and every outside output system on which $`H`$ acts. Denote the latter systems together with all outside outcome registers by $`E`$. Before projecting any outside outcome register, the resulting fixed-schedule circuit is CPTP and has a normalized retained output $`\Xi^y_{\mathcal P E}`$.

The backward histories from core outputs lie in $`N_R(\mathcal P)`$. An outside outcome register is retained at its creation time, so its history, like the history of an outside final output, lies in $`N_R(\mathcal B^c)`$. These neighborhoods are disjoint by the buffer. Operations outside both retained histories can now be removed because their maps are trace preserving. No selected outside measurement is removed: its register has been retained. The remaining histories have disjoint product-input cells, giving

```math
\Xi^y_{\mathcal P E}=\Xi^y_{\mathcal P}\otimes\Xi^y_E.
```

This factorization is before outside conditioning. It is not independence of the actual adaptive output marginals.

Project the retained registers onto the refined outside true record and apply $`H`$. For that record the core state is multiplied by a nonnegative scalar. The local test lemma applies to $`\Xi^y_{\mathcal P}`$ uniformly over the frozen public history. Multiply by the scalar and all nonnegative report probabilities, and sum over refined records, public transcripts and shared randomness. Public selection or weighting only removes terms or changes their nonnegative coefficients. This proves the buffered lemma. $`\square`$

Without the buffer the retained outside histories can overlap the core history, so outside postselection can change the core in a way this argument does not bound. Conditioning outside outcomes first and then deleting their trace-decreasing maps would be invalid.

### Several blind cores

Pack

```math
M=\left\lfloor\frac{L}{36(rT+1)}\right\rfloor^2
```

disjoint blind squares, with translated core tests $`K_1,\ldots,K_M`$. All tests commute, have disjoint supports, and are passed by every toric ground state. If a set $`J`$ of squares is blind, apply the buffered lemma successively with $`H`$ equal to the product of the preceding other-core tests. Their output supports are outside the current blind square and were retained before conditioning. Thus

```math
F\le\mathrm{Tr}\!\left[\left(\prod_{j\in J}K_j\right)\rho\right]
\le c^{|J|}.
```

Each application may use its own positive refinement of the same public branch. Summing that refinement recovers the actual branch, so a globally identical refinement is unnecessary. No independence of adaptive core marginals is asserted.

## 4. Finite noisy-report converse

For a BSC with $`0\lt p\lt 1/2`$, each report can equivalently be produced by a hidden choice: report the true outcome with probability $`1-2p`$, or report an independent fair coin with probability $`2p`$. This is an analysis representation of the **unflagged** detector. Its hidden choice is never revealed to the controller.

Presample independent choices at every potential slot, including idle slots. Each blind square has at most

```math
k=\nu[36(rT+1)]^2T
```

slots; pad to exactly $`k`$. All reports in a square are blind whenever its $`k`$ choices select fair reports, an event of probability $`q_{\mathrm{blind}}=(2p)^k`$. These events are independent for disjoint squares. Conditional on every hidden choice outside the blind squares, the preceding lemma still applies. Averaging $`c`$ to the number of blind squares gives

```math
\boxed{
F\le\left[1-\frac{(2p)^k}{17}\right]^M
\le\exp\!\left[-\frac{M(2p)^k}{17}\right].
}
```

When $`M=0`$, this is the valid trivial bound $`F\le1`$. The argument covers arbitrary adaptive local channels and arbitrary finite local quantum dimension. The fixed report density is essential to $`k=O(T^3)`$.

For a fixed target $`F\ge F_0\gt 0`$, a fitting packing implies

```math
k\log\frac1{2p}
\ge\log M-\log\!\left[17\log\frac1{F_0}\right].
```

To obtain an explicit asymptotic order bound, take $`K_{r,\nu}=1296\nu(r+1)^2`$. For $`T\ge1`$, the slot count obeys $`k\le K_{r,\nu}T^3`$. Choose a constant $`a\gt 0`$ with $`K_{r,\nu}a^3\log[1/(2p)]\lt 1`$. If $`T\le a(\log L)^{1/3}`$, then for all sufficiently large $`L`$ the packing fits and $`\log M\ge\tfrac32\log L`$, whereas the left side of the preceding inequality is less than $`\log L`$. Its $`F_0`$-dependent additive constant cannot close this gap. This rules out every such $`T`$ for sufficiently large $`L`$. The case $`T=0`$ is also excluded at fixed positive target for large $`L`$ by the finite bound itself, and larger depths already satisfy the claimed order. Thus

```math
T=\Omega_{p,F_0,r,\nu}\!\bigl((\log L)^{1/3}\bigr).
```

For $`p\gt 0`$, exact $`F=1`$ is impossible whenever a blind square fits. This is consistent with exact coherent preparation at linear depth, where the packing disappears. The rare-blind estimate is not uniform as $`p\to1/2`$; no uniform optimum is inferred from it.

## 5. Physically compress the syndrome before readout

The upper protocol uses $`q=3`$, $`r=1`$, $`\nu=1`$ and ideal CNOT, controlled-$`Z`$, reset, local dephasing and QND pointer readout. Let $`V=L^2`$. Start all data in $`|0\rangle`$. Define

```math
\Pi_a=\prod_v\frac{I+(-1)^{a_v}A_v}{2},
\qquad
|\psi_a\rangle
=\frac{\Pi_a|0\rangle^{\otimes N}}
{\|\Pi_a|0\rangle^{\otimes N}\|}.
```

Every even star syndrome $`a`$ occurs with probability $`2^{-(V-1)}`$; odd syndromes have zero probability. Every $`|\psi_a\rangle`$ has all plaquettes and the two chosen logical $`Z`$ loops equal to $`+1`$. For a physical edge set $`E`$, let $`\partial E`$ be its vertex boundary. With the displayed phase convention,

```math
Z(E)|\psi_a\rangle=|\psi_{a\oplus\partial E}\rangle.
```

Indeed, $`Z(E)\Pi_a=\Pi_{a\oplus\partial E}Z(E)`$, $`Z(E)|0\rangle^{\otimes N}=|0\rangle^{\otimes N}`$, and all even branches have equal norm.

### Coherent extraction

The [star-extraction schedule](preparation.md#3-star-extraction-in-bounded-depth) needs at most eight directional CNOT layers, because intercell directions use matching colors. Prepare each ancilla in $`|+\rangle`$, perform that schedule, and apply a final ancilla Hadamard instead of exposing an $`X`$ outcome to the controller. In at most ten layers this coherently stores each star syndrome in the computational basis of its local pointer. One site-local dephasing layer, with no public outcome, gives exactly

```math
\rho_{DA}
=2^{-(V-1)}\sum_{a:\,\oplus_v a_v=0}
|\psi_a\rangle\langle\psi_a|_D\otimes|a\rangle\langle a|_A.
```

There has been no noiseless classical use of $`a`$. Dephasing is a permitted local CPTP operation; its environment is inaccessible.

### A constant-memory sweep

Choose an integer $`1\le b\le L`$ and the [balanced rectangular partition](preparation.md#4-balanced-partitions-for-arbitrary-l) with

```math
B=\lfloor L/b\rfloor^2
```

blocks. Every side length lies in $`[b,2b-1]`$. Sweep each row to its leftmost vertex, then sweep that column to the block root. For a child $`u`$, parent $`v`$ and shared data edge $`e`$, perform three elementary layers:

1. CNOT the child pointer into the parent pointer.
2. Apply $`Z_e`$ controlled by the unchanged child pointer.
3. Reset the child pointer to $`|0\rangle`$ without producing a public report.

If the child and parent pointer values are $`\alpha,\beta`$, the controlled correction clears the child's actual star defect and leaves the parent's defect and pointer both equal to $`\alpha\oplus\beta`$. The reset discards the old child bit into a local inaccessible environment; it is not unitary erasure. All pairs at one sweep index have disjoint cell supports. With maximum side lengths $`w_{\max},h_{\max}`$, the comb has

```math
d=w_{\max}+h_{\max}-2\le4b-4
```

indices and costs $`3d`$ elementary layers.

Every nonroot star is now $`+1`$ and every nonroot pointer is zero. If $`r_j`$ is the remaining root bit, it equals the parity of the original true syndrome in block $`j`$. The root vector is uniform over the even $`B`$-bit subspace. Every such vector has exactly $`2^{V-B}`$ preimages. The data/pointer state is therefore

```math
2^{-(B-1)}\sum_{r:\,\oplus_jr_j=0}
|\psi_{\iota(r)}\rangle\langle\psi_{\iota(r)}|
\otimes|r\rangle\langle r|_{\mathrm{roots}}
\otimes|0\rangle\langle0|_{\mathrm{nonroots}},
```

where $`\iota(r)`$ places the bits at their physical roots. In particular, the surviving pointers describe the actual remaining defects, rather than parities of noisy reports. The reset environments retain discarded information but cannot alter this unconditional reduced-state identity.

## 6. Protected pointers and actual correction

For each block, copy its orthogonal root pointer along the bottom row using nearest-neighbor CNOTs, then copy each bottom-row pointer up its column in parallel. The nonroot pointers freed during the sweep provide the target qubits. This takes at most $`d`$ layers with disjoint cell supports and uses no extra memory. It copies basis states correlated with a syndrome; it does not clone arbitrary quantum states.

If block $`j`$ has area $`A_j`$, its $`A_j`$ pointers now all hold $`r_j`$. Read each in the $`Z`$ basis nondestructively for $`t\ge1`$ layers. The physical pointer value stays fixed, while every public report gets a fresh independent BSC flip. Thus root $`j`$ receives

```math
m_j=A_jt\ge b^2t
```

independent reports, with one report per cell per readout layer. This explicitly charges both fanout depth and report density.

Decode roots $`j=1,\ldots,B-1`$ by majority, using independent fair tie coins. Infer root $`0`$ from the exact even-total-parity identity. Its reports may be ignored. The majority error for $`m`$ reports is

```math
e_m(p)=\Pr[\mathrm{Bin}(m,p)\gt m/2]
+\frac12\Pr[\mathrm{Bin}(m,p)=m/2].
```

BSC symmetry and fair ties make this error independent of the true root value. Errors for the $`B-1`$ independently decoded roots are independent. The controller computes an edge set $`\widehat E`$ satisfying $`\partial\widehat E=\iota(\widehat r)`$, for example using the [coarse comb tree](preparation.md#6-fixed-nonlocal-collection-and-return-traffic). Its existence follows because the inferred syndrome is even.

Apply the resulting product of physical single-qubit $`Z`$ gates in one final site-local layer. Under the present free-global-feedforward convention, every site already has the public reports needed to choose its local Pauli. This layer supplies no instantaneous quantum propagation. Charging classical signal latency or delivered bits would return a different model and requires the additional routing costs in the original [preparation protocol](preparation.md#7-local-execution-of-the-coarse-correction).

The actual final star syndrome is $`\iota(r\oplus\widehat r)`$. It vanishes if and only if every independently decoded root is correct. Any wrong root leaves a nonzero physical syndrome, including even error patterns. Plaquettes and logical $`Z`$ values remain $`+1`$. Hence the unconditional ground-space overlap, also the overlap with the selected pure ground state in this construction, is **exactly**

```math
\boxed{
F_{\mathrm{phys}}
=\prod_{j=1}^{B-1}\bigl[1-e_{A_jt}(p)\bigr].
}
```

This averages all original quantum branches, all noisy reports and all tie coins. There is no postselection or reinterpretation as a Pauli frame.

Write

```math
\mathcal D(p)=-\frac12\log[4p(1-p)]\gt 0.
```

For $`a\gt 0`$, the exponential Markov bound gives $`\Pr[\mathrm{Bin}(m,p)\ge m/2]\le[e^{-a/2}(1-p+pe^a)]^m`$. Minimizing at $`e^a=(1-p)/p`$ yields $`[2\sqrt{p(1-p)}]^m=e^{-\mathcal D(p)m}`$. The fair-tie majority error is no larger than this tail probability. Therefore

```math
1-F_{\mathrm{phys}}
\le\sum_{j=1}^{B-1}e^{-\mathcal D(p)A_jt}
\le(B-1)e^{-\mathcal D(p)b^2t}.
```

The conservative elementary schedule is

```math
T\le10+1+3d+d+t+1
\le16b+t-4,
\qquad q=3,\quad r=1,\quad\nu=1.
```

For $`B=1`$, every defect is cleared by the local sweep since total syndrome parity is even. Omit fanout, reports and the last correction: $`T\le11+3(2L-2)=6L+5`$ and $`F=1`$ exactly. The memory bound concerns quantum memory at lattice cells, not the ideal global classical controller.

## 7. Matching the fixed-detector depth

Take $`t=b`$. Then $`T\le17b-4`$ and

```math
1-F_{\mathrm{phys}}
\le(B-1)e^{-\mathcal D(p)b^3}
\le\frac{L^2}{b^2}e^{-\mathcal D(p)b^3}.
```

For any $`0\lt \epsilon\lt 1`$, choose $`b`$ of order $`[\log(L^2/\epsilon)/\mathcal D(p)]^{1/3}`$, rounded up, while this scale is below $`L`$. The last display is at most $`\epsilon`$ after an appropriate constant choice. If that choice reaches $`L`$, use the exact one-block sweep. At fixed $`p`$ and fixed $`\epsilon`$, this is $`O_{p,\epsilon}((\log L)^{1/3})`$.

Together with Section 4, this proves for every fixed $`p\in(0,1/2)`$ and $`F_0\in(0,1)`$,

```math
\boxed{
T_{\mathrm{opt}}(L,p;F_0)
=\Theta_{p,F_0}\!\bigl((\log L)^{1/3}\bigr)
=\Theta_{p,F_0}\!\bigl((\log N)^{1/3}\bigr).
}
```

The optimum is over the model with $`q\ge3`$ and an operation set containing the stated native upper-bound primitives. The lower constant also depends on the fixed microscopic range and report density; the upper constant uses the explicit $`q=3,r=1,\nu=1`$ implementation. The theorem does not extend its uniformity to $`F_0\to0`$, $`F_0\to1`$, $`p\to0`$ or $`p\to1/2`$. In particular, exact $`F_0=1`$ has a different finite-depth requirement. The finite upper estimate above and the finite lower estimate remain available in their stated domains, but matching them into a full varying-parameter law is not claimed.

The exponent has two separately proved ingredients: the blind-core volume contains $`O(T^2)`$ cells and $`T`$ report times, and the construction actually obtains $`\Omega(b^2t)`$ independent reports after physically reducing the syndrome to one pointer per block. Dimensional analogy alone would establish neither ingredient.

## 8. Attribution and boundaries

The local anyon-braiding obstruction and spatial exponent are inherited from [Li–Lee–Yoshida](https://arxiv.org/html/2405.07970v3). The [dimension-independent local algebra](local-braiding.md), [local-channel dilation](channel-overlap.md) and [balanced syndrome sweeps](preparation.md) provide their toric-code implementation here. Standard star measurement and string correction retain the preparation attribution to [Lu–Lessa–Kim–Hsieh](https://doi.org/10.1103/PRXQuantum.3.040337), [Tantivasadakarn–Vishwanath–Verresen](https://doi.org/10.1103/PRXQuantum.4.020339), and the other sources in [related work](../references/related-work.md).

[Readout Entanglement Limits, revision `10ec6b4`](https://github.com/GoGoKo699/Readout-Entanglement-Limits/tree/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b), supplies the [outside-outcome retention argument](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b/science/blind_strip.md), the [unflagged detector interface](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b/science/model.md), and [spatial copying plus repeated protected-pointer readout](https://github.com/GoGoKo699/Readout-Entanglement-Limits/blob/10ec6b4ebfdd3f6dc20e83a7e73d8b36126e9c0b/science/construction.md). The source toric account is [revision `47e2a26`](https://github.com/GoGoKo699/Topological-Communication-Cost/tree/47e2a2632a939c96546b199b3ff08a1cd059f194). These are versioned research records, not independent peer-reviewed publications.

The joint contribution is the buffered two-loop transfer with outside conditioning controlled, together with a local quantum compression channel that preserves the actual pointer/defect relation and a fully counted readout/correction construction. The two source projects' earlier communication and Bell-pair theorems are not rediscovered here. The new two-dimensional proof has one authoritative home on this page; the sister account states its definitions, mechanism and consequences independently and points here for the full derivation.

The following limitations are load bearing:

- **Reading raw syndromes first changes the protocol.** A sweep controlled by one noisy report per raw star does not preserve the pointer/defect invariant. With $`V-1`$ independent raw bits and the last inferred by parity, correcting that estimate has physical overlap $`(1-p)^{V-1}`$. XORing noisy reports is not protected compression.
- **The original syndrome need not reach the controller.** Local resets physically remove $`V-B`$ defects while discarded information remains in inaccessible environments. Requiring recovery of every raw syndrome would impose an unjustified restriction on competing protocols.
- **Readout must preserve a usable pointer.** The stated $`q=3`$ schedule assumes QND readout. A destructive interface can instead keep a pointer and a resettable readout ancilla, with $`q=4`$ and fixed per-repeat overhead. Assuming a destructively measured sole pointer survives would be invalid.
- **Only reports are noisy.** Reliable coherent copying, reset, correction and storage are explicit assumptions. Additional gate or memory errors need their own construction analysis.
- **Classical latency is free here.** This is operation depth under global public feedforward, not laboratory elapsed time, a bounded-throughput network or a finite-runtime decoder theorem.
- **The output is a physical ground-space state.** No result here certifies a noisy topological phase, a merely low-energy output, or postselection using inaccessible true outcomes.

The [verification guide](../verification/README.md) records finite checks of geometry, pointer/data invariants, quantum memory, schedules, syndrome distributions, physical correction boundaries and exact overlap probabilities. These calculations supplement the arbitrary-size written arguments; they do not establish the universal converse by enumeration or constitute external peer review.

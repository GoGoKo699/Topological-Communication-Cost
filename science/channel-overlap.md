# Ground-space overlap of local channels

A local channel circuit cannot obtain appreciable global toric ground-space overlap when its propagation radius is small compared with the system size. The bound below allows arbitrary finite-dimensional local ancillary systems, local measurement records, resets, discarded outputs and shared classical randomness. It refers to the full four-dimensional toric code space, so no choice of logical state or factorization from retained environments is required.

## 1. Statement and locality convention

Use the cell torus, edge ownership and cyclic $`\ell_\infty`$ metric defined in [A local braiding obstruction](local-braiding.md). The system has $`N=2L^2`$ designated data qubits, with $`L\ge2`$.

A local circuit has $`D\ge0`$ scheduled layers. Within a layer, its channel supports are disjoint sets of cells, each of diameter at most an integer $`r\ge1`$. A channel may read and update all quantum and classical registers within its support. Private classical records may control its map. Propagation of a classical record between cells obeys the same support and layer constraints as quantum processing. On-site classical computation and copying have zero spatial spread.

For a fixed shared seed and fixed public controls, the support sets of the layers are fixed. In particular, a private outcome does not choose an uncommunicated change to a distant support or schedule. Several serial local transmissions in one coarse clock round must be expanded into their scheduled layers when defining $`D`$. This is the local part of the [communication model](model.md).

Conditioned on the shared classical seed $`\mathsf S`$, the initial state is a product across cells. There is no initially shared quantum entanglement between cells. Every cell may contain arbitrarily large finite-dimensional quantum and classical registers. The circuit output is the reduced state $`\rho_{\rm out}`$ on the designated data qubits.

Define

```math
R=rD,\qquad s=R+1,\qquad
m_{L,r}(D)=
\left\lfloor\frac{L}{32(rD+1)}\right\rfloor^2,
```

and the explicit overlap bound

```math
\begin{aligned}
q_{L,r}(D)=
\left(\frac{16}{17}\right)^{m_{L,r}(D)}.
\end{aligned}
\tag{1}
```

**Theorem 1.** Every trace-preserving local circuit in this model satisfies

```math
\begin{aligned}
F:=\mathrm{Tr}(P_{\rm TC}\rho_{\rm out})
\le q_{L,r}(D).
\end{aligned}
\tag{2}
```

Equation (2) holds for every $`L\ge2`$, $`r\ge1`$ and $`D\ge0`$. When $`L\lt 32(rD+1)`$, its right-hand side is $`1`$. This loss of a nontrivial bound at large depth is necessary: the [local preparation construction](preparation.md) reaches the ground space at depth of order $`L`$.

The exponent counts disjoint braiding patches. It is not the number of measured stabilizers or the dimension of the retained record.

## 2. Local dilation and the exact propagation radius

First condition on the shared seed. Purify each initially mixed local state by adjoining a purifying register at the same cell. The enlarged input is then a pure cell-product vector

```math
\begin{aligned}
|\boldsymbol 0\rangle=\bigotimes_{z\in\Lambda_L}|0_z\rangle.
\end{aligned}
\tag{3}
```

The notation $`|0_z\rangle`$ denotes the actual purified local input vector; it does not require a computational-basis state or a product over the registers within that cell.

For each channel on a support set $`S`$, introduce a fresh environment in a pure state at a cell of $`S`$ and use a Stinespring isometry on that support. Adding unused local registers extends the isometry to a unitary. All fresh registers can be allocated in product states before the first layer and left unused until needed; changing local register sizes can likewise be embedded in fixed larger local Hilbert spaces. Retain all these environments. Their introduction does not enlarge the set of cells touched by the channel.

A local instrument with a retained classical outcome is itself a channel on the system and its local record register. Its dilation can retain an additional environment recording the outcome, so subsequent controlled operations reproduce the intended classical adaptation after the environments are traced out. A reset similarly keeps the replaced input in an environment and supplies a fresh local register. These representations allow measurements and dissipation without discarding any system in the purified calculation.

The resulting global unitary will be denoted by $`W`$. It produces a purification of the original data output:

```math
\begin{aligned}
\rho_{\rm out}
=\mathrm{Tr}_{\mathcal E}
\left(W|\boldsymbol0\rangle\langle\boldsymbol0|W^\dagger\right),
\end{aligned}
\tag{4}
```

where $`\mathcal E`$ contains all registers outside the designated data output. The registers in $`\mathcal E`$ can become arbitrarily correlated with one another and with the data.

For clarity, the property of $`W`$ needed below is its support spread, rather than the number of elementary unitary gates in a chosen dilation. Consider one layer and an operator supported on cells $`T`$. A gate block $`S`$ affects the operator only if $`S\cap T\ne\varnothing`$. Every cell of such a block lies within distance $`r`$ of a cell of $`T`$, because $`\mathrm{diam}(S)\le r`$. Disjoint blocks within the layer cannot form a serial chain of support expansion. Thus one layer sends $`T`$ into $`N_r(T)`$.

Iterating through the $`D`$ layers, with any intervening zero-radius on-site operations, gives the exact inclusion

```math
\begin{aligned}
\mathrm{supp}(W^\dagger O W)
\subseteq N_{rD}(\mathrm{supp}O)
=N_R(\mathrm{supp}O).
\end{aligned}
\tag{5}
```

There is no factor depending on ancillary dimension, outcome-alphabet size or the amount of classical computation within a cell.

## 3. Projecting onto the full code space

Let

```math
P=P_{\rm TC}\otimes I_{\mathcal E}.
```

If $`F=0`$, the theorem is immediate. Otherwise define the normalized vectors

```math
\begin{aligned}
|\chi\rangle
=\frac{P W|\boldsymbol0\rangle}{\sqrt F},
\qquad
|\Omega\rangle=W^\dagger|\chi\rangle.
\end{aligned}
\tag{6}
```

Equation (4) gives

```math
\begin{aligned}
\langle\boldsymbol0|\Omega\rangle
=\frac{\langle\boldsymbol0|W^\dagger P W|\boldsymbol0\rangle}
{\sqrt F}
=\sqrt F.
\end{aligned}
\tag{7}
```

By construction, every toric stabilizer acts as $`+1`$ on $`|\chi\rangle`$. This remains true if the logical state is mixed after tracing $`\mathcal E`$, or if logical degrees of freedom are entangled with $`\mathcal E`$.

On each braiding patch, the undressed closed string stabilizes $`|\chi\rangle`$, the two undressed open strings agree on $`|\chi\rangle`$, and the closed string anticommutes with either open string. Conjugating by $`W`$ transfers these three identities to $`|\Omega\rangle`$. Equation (5) controls the dressed supports. These are precisely the hypotheses established in [Sections 3–5 of the local braiding proof](local-braiding.md).

Projecting onto $`P_{\rm TC}`$ in (6) is only an analysis device. The physical preparation protocol does not perform this nonlocal projection.

## 4. Packing and successive product projections

Set

```math
k=\left\lfloor\frac{L}{32s}\right\rfloor.
```

If $`k=0`$, (2) is the trivial inequality $`F\le1`$. Otherwise use the $`k^2`$ disjoint patches

```math
\begin{aligned}
\mathcal P_{a,b}
=(32sa,32sb)+\{0,1,\ldots,32s-1\}^2,
\qquad 0\le a,b\lt k.
\end{aligned}
\tag{8}
```

Their coordinate rectangles do not wrap around the torus. Each contains a translated copy of the explicit dressed-string geometry. All data, private records and environmental registers assigned to its cells are included in the patch.

Order these patches as $`\mathcal P_1,\ldots,\mathcal P_m`$, where $`m=k^2`$, and let

```math
P_j=|0_{\mathcal P_j}\rangle\langle0_{\mathcal P_j}|
\otimes I
```

be their initial product-vector projectors. The reference vectors are induced by (3).

Consider projecting $`P_1,P_2,\ldots`$ successively on $`|\Omega\rangle`$. If some prefix has zero probability, the joint probability of all projections is already zero. Otherwise, before step $`j`$ the normalized conditional state is

```math
\begin{aligned}
|\Omega_{j-1}\rangle
=
\frac{P_{j-1}\cdots P_1|\Omega\rangle}
{\|P_{j-1}\cdots P_1|\Omega\rangle\|}.
\end{aligned}
\tag{9}
```

The three dressed strings for patch $`j`$ are wholly supported in $`\mathcal P_j`$. They commute with every earlier $`P_i`$. Therefore the three local string identities that hold on $`|\Omega\rangle`$ also hold exactly on $`|\Omega_{j-1}\rangle`$.

Lemma 1 of the local braiding proof applies at every step and gives

```math
\begin{aligned}
\Pr(P_j=1\mid P_1=\cdots=P_{j-1}=1)
\le\frac{16}{17}.
\end{aligned}
\tag{10}
```

No independence of patch marginals is asserted. The state in (9) generally changes globally after each projection; the proof uses only the identities on the untouched patch.

The commuting projectors satisfy

```math
|\boldsymbol0\rangle\langle\boldsymbol0|
\preceq \prod_{j=1}^m P_j.
```

Together with (7) and (10), this yields

```math
\begin{aligned}
F
&=|\langle\boldsymbol0|\Omega\rangle|^2\\
&\le
\langle\Omega|\prod_{j=1}^m P_j|\Omega\rangle\\
&\le
\left(\frac{16}{17}\right)^m
=q_{L,r}(D).
\end{aligned}
```

This proves (2) for each fixed shared seed. Averaging over $`\mathsf S`$ preserves the same bound. $`\square`$

## 5. Explicit exponential and all-size estimates

Let

```math
\lambda=\log_2(17/16),\qquad
a=\frac{\lambda}{8192}.
```

If

```math
\begin{aligned}
L\ge64(rD+1),
\end{aligned}
\tag{11}
```

then $`L/(32s)\ge2`$ and

```math
\begin{aligned}
m_{L,r}(D)
\ge\left(\frac{L}{64s}\right)^2
=\frac{N}{8192(rD+1)^2}.
\end{aligned}
\tag{12}
```

Therefore

```math
\begin{aligned}
F\le
2^{-aN/(rD+1)^2}
\le
2^{-aN/[r^2(D+1)^2]}.
\end{aligned}
\tag{13}
```

The second inequality uses $`r\ge1`$. For fixed interaction range, (13) is the area divided by squared local-depth exponent.

For statements that include small lattices and deep circuits, the exact floor in (1) is convenient. A useful uniform packing estimate is

```math
\begin{aligned}
m_{L,r}(D)+1
\ge\frac{N}{8192(rD+1)^2}.
\end{aligned}
\tag{14}
```

Indeed, with $`x=L/(32s)`$, the inequality $`\lfloor x\rfloor^2+1\ge x^2/4`$ follows from $`\lfloor x\rfloor\ge x/2`$ when $`x\ge2`$, and from $`1\ge x^2/4`$ when $`x\lt 2`$. Equation (14) does not assert a strictly negative overlap exponent when no braiding patch fits.

## 6. Scope and proof provenance

The theorem permits arbitrary finite-dimensional ancillary registers at each cell, arbitrary local channels and private records, mixed data outputs, and classical mixtures of product initial states. It does not supply entanglement between cells before the circuit begins.

The overlap is with the full physical code-space projector. A state described only by a remotely stored Pauli frame need not have this overlap before its correction. Agreement of local observables or a small energy density is a different target and is not bounded by (2).

Equation (2) applies to trace-preserving local circuits. A normalized branch conditioned on nonlocal communicated information need not be such a circuit; a communication converse must first compare its subnormalized output with an appropriate local trace-preserving completion.

The strict support inclusion (5) is a finite circuit statement. Continuous-time local Hamiltonian or Lindblad evolution has propagation tails and requires a separate estimate before the same argument can be applied.

The spatial exponent and the local braiding obstruction are inherited from [Li, Lee and Yoshida (2025)](https://arxiv.org/html/2405.07970v3). Their honeycomb-code proof uses successive projections that preserve string identities on the remaining regions. Here that argument is applied to a projection onto the entire toric code space after a local dilation, using the dimension-independent lemma in the companion proof. No decoupling of ancillary systems or independence of target marginals is required.

The dilation of measurements, records and local channels is standard; [Friedman, Yin, Hong and Lucas (2023), Section 3](https://arxiv.org/pdf/2206.09929) develops the relevant Stinespring description for measurement-assisted dynamics. The qualitative relation between locally correctable measurement protocols and finite-depth unitary preparation is established by [Tantivasadakarn, Vishwanath and Verresen (2023), Theorem 3](https://doi.org/10.1103/PRXQuantum.4.020339). The present bound quantifies the global ground-space overlap within the specified local-channel model.


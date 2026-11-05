# Consequences of the communication–depth frontier

The [communication converse](communication-bound.md) and [preparation protocol](preparation.md) determine how much nonlocal classical information can be replaced by local processing. The target is a physically prepared toric-code ground-space state, measured by the unconditional overlap $F=\operatorname{Tr}(P_{\mathrm{TC}}\rho)$.

Throughout this page, the local interaction range $r$ and required overlap $f\in(0,1]$ are fixed. Constants may depend on them. The system contains $N=2L^2$ data qubits. Local depth includes both quantum operations and local classical propagation; $C$ counts the additional nonlocal classical bits in the [protocol model](model.md).

## 1. An optimal exchange of resources

Every allowed protocol with $F\geq f$ satisfies

$$
(C+1)(D+1)^2\geq c_{f,r}N.
$$

For every block scale $1\leq\ell\leq L$, a concrete exact preparation uses

$$
D\leq a_0\ell+a_1,
\qquad
C\leq a_2\frac{N}{\ell^2},
$$

with constants independent of $L$ and $\ell$. At $\ell=L$, the construction is wholly local and uses $C=0$. The upper and lower bounds match up to constants along the achievable tradeoff frontier. The assertion is not that every feasible pair satisfies an equality, nor that preparation is possible with literally zero local gates and enough classical messages.

Several useful regimes follow directly.

| Available local depth | Necessary nonlocal bits at fixed overlap | Matching construction |
| --- | --- | --- |
| Constant depth | $\Omega(N)$ | Constant-size blocks and $O(N)$ delivered bits |
| $D$ growing below order $L$ | $\Omega(N/(D+1)^2)$, up to the additive endpoint term | Blocks of side proportional to $D$ |
| Order $L$ | Zero nonlocal bits are possible | A local syndrome sweep over the full lattice |

Increasing local depth by a factor $k$ can reduce the necessary nonlocal communication by order $k^2$ in the intermediate regime. The square is the area of a local causal patch. It is not a count of logical qubits: the converse holds even for the full four-dimensional ground space, and the upper construction prepares one fixed logical sector.

## 2. What happens below the required budget

Let

$$
m=\left\lfloor\frac{L}{32(rD+1)}\right\rfloor^2,
\qquad
\lambda=\log_2\frac{17}{16}.
$$

The finite converse is

$$
F\leq\min\{1,2^{C-\lambda m}\}.
$$

If $C\leq(\lambda-\varepsilon)m$ for a fixed $\varepsilon\in(0,\lambda)$, then

$$
F\leq 2^{-\varepsilon m}.
$$

In particular, at constant depth, any $C=o(N)$ protocol has exponentially small unconditional ground-space overlap. This is stronger than a restriction to exact preparation. Approximation with a fixed positive overlap does not remove the extensive communication requirement.

The numerical constants are conservative proof constants. They should not be used as engineering estimates of the smallest decoder message count. The matching statement concerns scaling with system size and local depth.

## 3. Variable-length communication

If the physical transcript is prefix free and the protocol terminates almost surely, its expected length $\overline C$ obeys

$$
\overline C\geq F\lambda m+F\log_2 F.
$$

Consequently, for fixed $F\geq f>0$,

$$
(\overline C+1)(D+1)^2=\Omega_{f,r}(N).
$$

Allowing rare branches to send many more bits therefore does not change the fixed-overlap scaling. A randomly selected exact preparation run, mixed with inexpensive failures, can reduce the average cost in proportion to its success fraction; the unconditional overlap decreases with the same fraction. The theorem keeps that probability in the accounting.

The expected-length result does not provide the same exponential tail bound as a hard cap. These are separate statements: the hard-cap converse controls $F$ through the number of transcript leaves, while the mean-cost converse uses the entropy of those leaves.

## 4. A conditional preparation-time law

An additional architecture model converts the resource frontier into a timing statement. Suppose the nonlocal classical network is an ideal switch with aggregate delivered throughput $\beta$ bits per local circuit time. Every delivered bit, including each copy in a point-to-point fanout, counts against that throughput. Propagation latency is negligible and local classical computation is unrestricted. Let $T$ be the full elapsed time, including waiting for the switch.

Any protocol completed by time $T$ has

$$
D\leq T,
\qquad
C\leq\beta T.
$$

For a hard completion deadline and fixed target overlap, the resource converse implies

$$
(\beta T+1)(T+1)^2\geq c_{f,r}N.
$$

The block protocol supplies a matching upper bound. Its local sweep and physical correction take $O(\ell)$ time, while gathering and returning the $O(N/\ell^2)$ nonlocal bits take $O(N/(\beta\ell^2))$ time. Thus, for $\beta>0$,

$$
T\leq O\!\left(\ell+\frac{N}{\beta\ell^2}\right).
$$

A separate wholly local choice takes $O(L)$ time and uses no switch traffic. Optimizing the block scale, for asymptotically large $L$ at fixed $f,r$, gives

$$
T_\star(N,\beta;f,r)
=\Theta_{f,r}\!\left(
\max\left\{1,\min\left\{L,(N/\beta)^{1/3}\right\}\right\}
\right).
$$

For $\beta=0$, interpret the inner second term as infinity, so $T_\star=\Theta_{f,r}(L)$. To see the lower bound directly, split into two cases. If $\beta T\leq1$, the displayed resource inequality forces $T+1=\Omega(\sqrt N)$. If $\beta T>1$, then $T+1=\Omega((N/\beta)^{1/3})$, up to constants and the minimum one-step scale. The upper bound uses $\ell$ of order $(N/\beta)^{1/3}$ when it lies between the constant and whole-lattice endpoints.

At fixed positive aggregate throughput, this ideal architecture has $T_\star=\Theta(N^{1/3})$. The result identifies the optimal compromise between slower local aggregation and a smaller remote transcript. It is conditional on the specified switch model: physical signal delays, a finite controller computation rate, port restrictions and storage noise require additional costs and are not included in this timing theorem.

## 5. The output contract

Measuring all star checks can leave a state with random anyon defects together with a classical syndrome record. That is a useful intermediate state, and every realized pure branch can be related to a clean ground state by a syndrome-dependent Pauli correction. The target here is the corrected quantum output itself. An arbitrarily accessible global decoder or an uncharged interpretation of a distributed Pauli frame would supply a different output resource.

This distinction also matters for postselection. The converse applies to a selected subnormalized output through its unconditional contribution $p f_{\mathrm{cond}}$. A matching *operationally heralded* tradeoff would additionally have to deliver a trustworthy success flag. Simply selecting that all uncommunicated root syndromes vanish does not account for the communication needed to certify that event.

The present result gives no noise threshold and no general theorem for continuous-time dynamics with nonzero light-cone tails. Its exact scope is finite local circuits, charged nonlocal classical communication, and global toric-ground-space overlap. Within that scope, the matching bounds determine an optimal resource frontier without restricting the preparation to stabilizer operations or a particular decoder.

## Reading onward

The full proofs are in [local braiding](local-braiding.md), [channel overlap](channel-overlap.md), and [communication bounds](communication-bound.md). The [construction](preparation.md) gives the physical schedule and its message count. [Related work](../references/related-work.md) separates the inherited braiding, measurement-feedback and communication ingredients from the operational frontier proved here.

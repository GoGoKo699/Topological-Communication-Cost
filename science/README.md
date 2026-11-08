# Scientific overview

Local measurements can create long-range quantum correlations in a shallow quantum circuit when their outcomes can control distant corrections. That observation leaves a resource question: how much classical information must actually cross the system once local propagation time is limited?

For the toric code, the complete syndrome has order $`N`$ bits, but transmitting every measured bit is unnecessary when neighboring cells can process their records first. The [preparation protocol](preparation.md) removes defects inside each block and leaves one parity at each block root. Only those root parities and the instructions for joining them need nonlocal messages. A block of linear size $`\ell`$ takes order $`\ell`$ local depth and contains order $`\ell^2`$ data qubits. This produces the candidate scale $`N/\ell^2`$ for communication.

The converse shows that this scale is unavoidable for arbitrary local channels, including protocols unrelated to stabilizer decoding. Its content is stronger than a count of syndrome bits used by one particular decoder.

A second model grants free global classical processing but makes every measurement report independently unreliable. The [noisy-readout account](noisy-readout.md), developed with [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits), proves fixed-detector depth $`\Theta((\log L)^{1/3})`$ for any fixed positive overlap below one. It transfers the local braiding geometry to buffered two-loop tests and audits a physical quantum-pointer compression/readout protocol. The classical resource conventions of the two models are distinct.

## The charged-communication results

Use the [model](model.md) with $`N=2L^2`$, local range $`r\ge1`$, local-depth cap $`D`$, unconditional ground-space weight $`F`$, and

```math
m=\left\lfloor\frac{L}{32(rD+1)}\right\rfloor^2,
\qquad \lambda=\log_2(17/16).
```

| Result | Statement | Proof |
| --- | --- | --- |
| Local-channel overlap | Without nonlocal communication, $`F\le(16/17)^m`$, uniformly over arbitrary finite local environments | [Local braiding](local-braiding.md) and [channel overlap](channel-overlap.md) |
| Charged communication | A hard cap gives $`F\le\min\{1,2^{C-\lambda m}\}`$; expected cost gives $`\overline C\ge\max\{0,F\lambda m+F\log_2F\}`$ | [Communication bounds](communication-bound.md) |
| Exact matching preparation | For $`1\le\ell\le L`$, $`D\le12\ell+2`$ and $`C\le2(\lfloor L/\ell\rfloor^2-1)`$; the wholly local endpoint uses $`C=0`$, $`D\le2L+8`$ | [Preparation](preparation.md) |

At fixed nonzero target overlap and fixed $`r`$, these establish the frontier

```math
(C+1)(D+1)^2=\Omega(N),
\qquad
(\overline C+1)(D+1)^2=\Omega(N),
```

with an exact construction attaining the scaling. The added ones retain a valid statement at zero communication and small depth. The matching claim permits constant rescaling of the depth and communication budgets; it does not optimize finite coefficients.

## The noisy-report result

Use the separate [noisy-report model](noisy-readout.md#1-physical-model-and-target): fixed local memory and report density, range-$`r`$ quantum operations, independent unflagged BSC reports, and free global classical processing of those reports. The physical output is still $`F=\mathrm{Tr}(P_{\mathrm{TC}}\rho)`$ after actual corrections. For a depth-$`T`$ competitor define

```math
M=\left\lfloor\frac{L}{36(rT+1)}\right\rfloor^2,
\qquad
k=\nu[36(rT+1)]^2T.
```

The [buffered blind-core proof](noisy-readout.md#3-buffered-blind-core-lemma) gives

```math
F\le\left[1-\frac{(2p)^k}{17}\right]^M.
```

The [constant-memory construction](noisy-readout.md#5-physically-compress-the-syndrome-before-readout) leaves one true defect pointer per block, copies it over block area and reads every copy $`t`$ times. For block areas $`A_j`$ and $`B`$ blocks, the final physically corrected state has the exact overlap

```math
F_{\mathrm{phys}}=\prod_{j=1}^{B-1}[1-e_{A_jt}(p)],
\qquad
1-F_{\mathrm{phys}}\le(B-1)e^{-\mathcal D(p)b^2t},
```

where $`e_m`$ is the fair-tie majority error and $`\mathcal D(p)=-\tfrac12\log[4p(1-p)]`$. Its explicit schedule uses $`q=3`$, $`r=1`$, $`\nu=1`$ and $`T\le16b+t-4`$. Taking $`t=b`$ establishes the [matched fixed-detector theorem](noisy-readout.md#7-matching-the-fixed-detector-depth). This is a new two-dimensional consequence; it does not identify a uniform crossover in varying detector quality or accuracy.

## Why the lower bound survives local measurements

The [single-patch lemma](local-braiding.md#1-dimension-independent-algebra-lemma) compares two deformations of an open string with a closed string that braids around one endpoint. Their algebra forces the probability of a prescribed product reference vector on the patch to be at most $`16/17`$. The lemma is independent of local dimension and allows arbitrary entanglement with the exterior.

The [channel proof](channel-overlap.md) keeps every local environment in a unitary dilation, projects the output onto the **entire** code space, and pulls that vector back through the circuit. Each dressed string stays inside a causal patch. Successive product projections on disjoint patches preserve the string identities on all untouched patches, so their conditional probability bounds multiply. No independence of patch marginals or factorization between the code and its environments is assumed.

The [transcript proof](communication-bound.md) then fixes a complete nonlocal transcript. All remote controls become preset constants. Dropping local consistency checks produces a trace-preserving local circuit that dominates the selected branch as a positive operator. This step keeps the branch probability; normalizing a rare postselected state before applying a local-circuit theorem would lose it. A depth-$`C`$ binary communication tree has at most $`2^C`$ leaves. A variable-length prefix tree instead bounds the conditional entropy by its mean physical length.

## Why the upper bound pays for the physical state

The [construction](preparation.md) starts with data in $`|0\rangle`$, measures the $`X`$ stars, and locally sweeps each block syndrome to one root. A controller collects the root parities, solves the correction flow on a fixed coarse tree, and returns the relevant coefficients to the parent roots. Those roots propagate instructions along short physical paths and apply the $`Z`$ corrections. The schedule includes zero-valued messages and local travel of every instruction.

Every branch ends in the same pure ground state with fixed logical $`Z`$ values. Therefore discarding the records leaves that state unconditionally. A classical description of a correction that has not yet acted would not satisfy this output contract.

## Interpretation and boundaries

The frontier exchanges local causal area for nonlocal information. It yields an extensive classical requirement at constant depth, a quadratic reduction in that requirement as local depth grows, and an all-local preparation route at depth of order the system diameter. The [consequences](consequences.md) also derive a conditional $`N^{1/3}`$ time law under fixed aggregate throughput and an ideal classical switch.

The theorem does not identify a noise threshold, bound only local observables, grant free heralding, or directly cover continuous-time dynamics with propagation tails. These are distinct questions. The [source comparison](../references/related-work.md) attributes the inherited topological obstruction and standard preparation ingredients; the [verification guide](../verification/README.md) separates finite reproducible checks from the general written proofs.

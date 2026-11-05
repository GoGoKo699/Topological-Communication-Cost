# Model: local processing and communicated classical information

The task is to prepare an actual toric-code ground state from spatially unentangled resources. We charge two resources separately: local circuit depth $`D`$, which limits propagation through the lattice, and classical communication $`C`$ that can bypass that local propagation rule. Local measurements and private records are allowed throughout.

The converse grants each charged bit global broadcast. The [preparation](preparation.md) attains the same asymptotic frontier with ordinary point-to-point delivered bits, including both syndrome collection and correction instructions.

## 1. Lattice, registers, and target

Let

```math
\Lambda_L=(\mathbb Z/L\mathbb Z)^2,\qquad L\ge 2,\qquad N=2L^2.
```

Each cell owns the qubits on its east-going and north-going edges. Distances between cells use the cyclic $`\ell_\infty`$ metric. Every register, including an ancilla or a classical record, has an assigned cell. A gate supported on a set of cells of diameter at most the fixed integer $`r\ge1`$ is local.

The toric code has $`X`$-star stabilizers $`A_v`$ and $`Z`$-plaquette stabilizers $`B_p`$. Its ground-space projector is

```math
P_{\mathrm{TC}}
=\prod_v\frac{I+A_v}{2}\prod_p\frac{I+B_p}{2}.
```

The redundant global stabilizer constraints do not affect this expression. For an output state $`\rho`$ on the designated $`N`$ data qubits, our figure of merit is the unconditional ground-space weight

```math
F=\mathrm{Tr}(P_{\mathrm{TC}}\rho).
```

For a specified pure ground state $`|\psi\rangle`$, the squared fidelity $`\langle\psi|\rho|\psi\rangle`$ is at most $`F`$. The construction prepares a particular pure ground state exactly, so the converse and construction also bracket that stronger task.

The data qubits themselves must have the claimed overlap. A syndrome-dependent state accompanied by a remotely stored Pauli-frame description is assessed before any unapplied correction. If a decoder or frame-controlled operation is part of the output task, its local depth and communicated bits belong to the protocol.

## 2. Initial resources and local operations

A public classical seed $`\mathsf S`$ may be supplied freely. Conditional on every seed value $`s`$, the initial state is a product over cells:

```math
\rho_{\mathrm{in}\mid s}
=\bigotimes_{x\in\Lambda_L}\rho_{x\mid s}.
```

Each factor may contain arbitrarily many finite-dimensional quantum and classical registers. Dimensions need not be bounded uniformly in $`L`$. The local states may be mixed. Independent local randomness can be generated or included in these registers. There is no initially shared quantum entanglement between cells.

A declared classical register is block diagonal in its distinguished record basis, including its correlations with other registers. Turning a quantum system into a fresh classical record requires a measurement in a counted local layer. Free onsite classical computation does not supply free quantum gates controlled by its result; those gates remain local-layer operations.

This formulation also covers spatially separable initial mixtures: conditioning on a product-state decomposition only grants additional classical information. Free shared randomness does not supply a spatially entangled quantum resource.

A local layer is a tensor product of completely positive trace-preserving maps on pairwise disjoint cell sets, each of diameter at most $`r`$. A map may:

- perform a unitary or a general quantum channel;
- measure and retain a private classical outcome;
- condition its action on records already present in its support;
- introduce local ancillas, reset registers, or discard them;
- transmit classical information between cells in its support.

Nearest-neighbor classical propagation therefore consumes local layers, just as quantum propagation does. The converse permits arbitrary finite local message size and unrestricted onsite classical computation. These privileges do not enlarge the spatial range of one layer. The construction uses only bounded-size local messages.

Every execution path contains at most $`D`$ local layers. Padding with identity maps permits a common depth cap. The cap is on each branch, not on expected depth.

## 3. A causal adaptive schedule

The schedule is part of the protocol. Conditional on the public seed and the already communicated transcript, the following are fixed:

1. whether the next event is a local layer, a charged classical bit, or termination;
2. the cell-support partition for a local layer;
3. the sender, recipient or recipients, and local-clock position of a charged bit.

Private local outcomes may choose the channel performed inside a scheduled support. For example, a fixed two-cell gate may be the identity when a local control bit is zero and a correction when it is one. The controlled operation is a valid channel on that same support for every private record value.

This convention allows local adaptivity without granting a global scheduler access to uncommunicated records. Only the public seed and charged transcript may change the scheduled support partition or the global next-event decision. Information arriving through counted local propagation may control a channel inside an already scheduled support; it does not change the public message schedule or global termination rule. Ordinary local gate activation can be expressed with controlled channels on a predetermined schedule; any coloring or coordination overhead is included in $`D`$.

A classical record needed at another cell must actually arrive there. It is insufficient for an external circuit description to declare that a distant gate is controlled by that record.

### The communication tree

Suppressing the prescribed local operations between messages leaves a binary protocol tree for each public seed. A node is the public history $`h`$. The next bit is read from a classical record at its prescribed sender, or computed there from locally available classical records. A fresh quantum measurement producing that record is a local-layer operation.

The two children append $`0`$ or $`1`$. A terminal history is a leaf. Consequently, complete finite transcripts form a prefix-free set: a transcript at which the protocol has terminated is not also the beginning of another legal complete execution.

The public history fixes message locations, clock positions, and global termination. An outcome-dependent sender, address, timing, packet length, silence, or stopping decision may not convey additional information outside the charged transcript. Local records can instead travel through counted local layers and control actions within the fixed schedule, but this does not supply an unrecorded change of the next public event or terminal leaf. In particular, local inactivity is not global termination. Predetermined zero bits remain physical messages; omitting one according to its value is not free.

These rules do not charge the static description of the protocol, its fixed wiring, or a schedule known before the run. They charge information generated during execution that would otherwise evade the bit count.

## 4. Broadcast and delivered-bit conventions

For the lower bound, every charged bit may be broadcast instantly to every cell and to a classical controller at cost one. All cells may use the public history in subsequent scheduled operations. This is a deliberately permissive communication resource.

A point-to-point implementation instead counts every delivered binary message. A bit sent separately to $`k`$ recipients costs $`k`$ delivered bits. Such a protocol is included in the broadcast model by revealing each of its messages more widely; this can only enlarge the available information. Thus a converse proved for broadcast cost also applies when $`C`$ counts delivered point-to-point bits.

A classical controller may perform unrestricted classical computation on its initial randomness and the messages it receives. It does not read private lattice records without communication. Controller-local computation is free in this resource model, but its incoming and outgoing messages are charged. No claim about processor runtime or signal transit latency follows solely from this convention.

The term “nonlocal communication” means communication outside the counted local layers. Even a short-distance message consumes $`C`$ if it is used as a zero-depth shortcut. Conversely, a message carried through local gates is charged in $`D`$ rather than counted again in $`C`$.

Let $`\mathsf T`$ denote the complete transcript and $`\ell(\mathsf T)`$ its number of bits. We consider:

- a hard communication cap $`\ell(\mathsf T)\le C`$ on every branch and seed;
- almost surely terminating, possibly unbounded-length protocols with mean cost $`\overline C=\mathbb E\,\ell(\mathsf T)`$.

For the second case, the tree is countable and its terminal transcripts remain prefix-free. Infinite expected cost is permitted, in which case a finite lower bound on mean cost is automatic.

## 5. Why local dilation preserves the needed geometry

After conditioning on the seed, purify every initial factor at its own cell. A local channel can be implemented by a Stinespring unitary on its existing support and a fresh environment placed in that support. Environments introduced for distinct gates are initially independent. A reset is treated by retaining the replaced register and supplying a fresh local register; a measurement is treated by retaining its outcome and environment.

Local classical processing can be coherently dilated while keeping its records and discarded work locally. The sender-side read completions used in the [communication proof](communication-bound.md) act as the identity on valid classical records and can be omitted from the completed physical circuit. Any coherent implementation of free onsite classical processing has zero spatial radius.

Therefore, after all records and environments are retained, the complete no-message evolution has a unitary dilation $`W`$ with the support property

```math
\mathrm{supp}(W^\dagger O_X W)
\subseteq X^{+R},
\qquad R=rD,
```

where $`X^{+R}`$ is the radius-$`R`$ neighborhood of $`X`$. At each of the at most $`D`$ spatial layers a support can expand by at most $`r`$; arbitrary onsite factors do not enlarge it. The same statement holds with $`W`$ and $`W^\dagger`$ interchanged.

The argument needs this propagation bound, not equality between the channel depth and an elementary two-qubit decomposition of its dilation. Arbitrarily large onsite environments do not alter the bound.

For variable-length communication, each fixed finite transcript has a finite completed local circuit. The no-message overlap estimate is uniform in its local dimensions and in the number of zero-radius factors, so the same estimate applies to every transcript.

## 6. Error, success, and scope

All fidelity statements are unconditional unless a success event is explicitly introduced. A selected output with success probability $`p`$ and conditional ground-space weight $`f`$ contributes $`pf`$ to the unconditional weight. The converse can bound that contribution, but this does not by itself provide a protocol that makes the success flag physically available.

If a final global success test is required, its communication or local propagation must be charged. The matching theorem here concerns deterministic preparation and unconditional fidelity; it does not grant free global postselection.

The model describes finite-depth local channels with an exact causal radius. A continuous-time local Lindblad or Hamiltonian evolution has propagation tails and requires a separate approximation argument. Likewise, small energy density, agreement of local observables, or a noisy topological phase is a different accuracy criterion from the global projector weight $`F`$.

## Reading route

The [local braiding lemma](local-braiding.md) supplies a dimension-independent obstruction. The [channel-overlap theorem](channel-overlap.md) converts it into a no-message bound despite discarded environments. The [communication theorem](communication-bound.md) then prices nonlocal classical information, and the [preparation](preparation.md) attains the resulting scaling. The [source comparison](../references/related-work.md) identifies the inherited topological obstruction and earlier measurement-assisted preparation results.

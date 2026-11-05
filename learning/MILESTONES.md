# Thirty milestones for topological communication cost

This map follows one question: **how much nonlocal classical information is needed to physically prepare a toric-code ground state when local propagation has limited depth?** The single learning anchor is John Preskill's [Quantum Information, Chapter 7: Quantum Error Correction, updated March 2026][preskill]. The [Preskill bridge](PRESKILL_BRIDGE.md#source-map) connects that chapter to the additional circuit, probability, and communication arguments used here.

The allocation is **14 milestones for background and preliminaries, followed by 16 for the narrative and innovation**. The first fourteen establish the local operator and channel language, the toric code, and the complete global output and resource contract. The remaining sixteen follow the distinct steps of the obstruction and construction through to the matching resource frontier and its timing consequence. Each phase starts with local objects, builds toward global statements, and ends with a synthesis.

The assumed starting language is finite-dimensional vectors and operators, tensor products, and elementary probability. The chapter is a source for the quantum-error-correction concepts; the bridge supplies the additional tools that the chapter does not establish. In particular, section pointers below do not attribute the project's channel-overlap or communicated-bit theorems to Preskill. The canonical claims and proofs remain in [science](../science/README.md).

Each milestone states its immediate earlier dependencies. Those dependencies are conceptual: a source may point ahead to a proof whose definitions or result are being introduced. Throughout, $`N=2L^2`$, $`D`$ is a branchwise local-depth cap, $`C`$ is a hard cap on nonlocal bits, $`\overline C`$ is their expected number, and $`F=\mathrm{Tr}(P_{\mathrm{TC}}\rho)`$ is the unconditional weight of the physical data output in the full toric-code ground space.

## Phase I — Background and preliminaries

### M01

**Pauli signs on a small support**

**Central question.** How does a local $`XZ=-ZX`$ relation become a commutation sign between extended operators?

**Understanding target.** Determine the sign obtained by exchanging two $`X`$- and $`Z`$-type Pauli products from the parity of their shared data qubits. Keep a data qubit's edge label separate from the cell that owns it.

**Earlier dependencies.** None.

**Story role.** Supplies the elementary algebra from which the later braiding obstruction is built.

**Conceptual connection.** A crossing of geometric strings records a local operator relation; an odd number of crossings can survive as a global sign.

**Sources.** Preskill [§7.10.1][p7101] and [§7.10.2][p7102]; bridge [stabilizers and logical labels](PRESKILL_BRIDGE.md#stabilizers-and-logical-labels); [local braiding, §2](../science/local-braiding.md#2-cell-lattice-and-toric-operators).

### M02

**A parity measurement and its classical record**

**Central question.** What does measuring a Pauli product reveal, and what does the measured quantum system become?

**Understanding target.** Describe a two-outcome parity measurement by its projectors, its outcome probabilities, and its conditional data states. Explain how an ancilla can record the collective parity without measuring every data qubit separately, and why averaging over the record differs from choosing one outcome.

**Earlier dependencies.** [M01](#m01).

**Story role.** Introduces the actual quantum and classical outputs of a local measurement before measurement outcomes are used as controls.

**Conceptual connection.** A syndrome bit is information extracted from a quantum operation; its existence at one location does not make it available everywhere.

**Sources.** Preskill [§7.1][p71] and [§7.10.1][p7101]; bridge [syndromes and physical output](PRESKILL_BRIDGE.md#syndromes-and-physical-output); [preparation, §3](../science/preparation.md#3-star-extraction-in-bounded-depth).

### M03

**Local channels, instruments, and retained environments**

**Central question.** How can measurements, private records, resets, and discards be represented within one local quantum description?

**Understanding target.** Treat an instrument with its retained outcome as a completely positive trace-preserving map, and represent a local channel by a local dilation with an initially uncorrelated environment. Understand that retaining discarded registers changes the description of the evolution without changing its reduced data output.

**Earlier dependencies.** [M02](#m02).

**Story role.** Makes the later converse apply to open local processing rather than requiring a unitary preparation protocol.

**Conceptual connection.** Irreversibility in the data can be represented by correlations with additional registers whose spatial locations remain explicit.

**Sources.** Preskill [§7.2][p72]; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [model, §2](../science/model.md#2-initial-resources-and-local-operations) and [channel overlap, §2](../science/channel-overlap.md#2-local-dilation-and-the-exact-propagation-radius).

### M04

**Local depth as a causal radius**

**Central question.** How far can an operator or a classical record propagate through $`D`$ local layers?

**Understanding target.** Use disjoint gate supports of cell diameter at most $`r`$ to obtain the exact radius $`R=rD`$. Include local classical transmission in the depth, while recognizing that arbitrary on-site classical computation and on-site dilation factors have zero spatial spread.

**Earlier dependencies.** [M01](#m01), [M03](#m03).

**Story role.** Establishes the geometric resource that will determine both the size of a braiding patch and the amount of syndrome information a block can aggregate.

**Conceptual connection.** The same causal constraint governs quantum support growth and locally transported classical control.

**Sources.** Preskill [§7.18.1][p7181] supplies the local-code setting; bridge [locality and causal depth](PRESKILL_BRIDGE.md#locality-and-causal-depth) adds the circuit convention; [model, §5](../science/model.md#5-why-local-dilation-preserves-the-needed-geometry).

### M05

**Commuting checks and their common code space**

**Central question.** How do commuting local constraints define a quantum subspace?

**Understanding target.** Relate simultaneous $`+1`$ stabilizer conditions to a product of commuting projectors. Distinguish the number of listed checks from the number of independent constraints, and distinguish an operator that fixes the whole code space from one that distinguishes states within it.

**Earlier dependencies.** [M01](#m01), [M02](#m02).

**Story role.** Provides the language needed to project onto a code space without specifying one codeword.

**Conceptual connection.** Local constraints can be redundant while their common solution space still supports nontrivial quantum information.

**Sources.** Preskill [§7.10.1][p7101] and [§7.10.4][p7104]; bridge [stabilizers and logical labels](PRESKILL_BRIDGE.md#stabilizers-and-logical-labels); [model, §1](../science/model.md#1-lattice-registers-and-target).

### M06

**Assembling the toric lattice**

**Central question.** Which qubits and checks constitute the toric code in the project's locality convention?

**Understanding target.** Identify the $`2L^2`$ horizontal and vertical edge qubits, their owning cells, the $`X`$ stars, and the $`Z`$ plaquettes. Verify their commutation and the two global product constraints. Keep distinct edge labels distinct even on the $`L=2`$ torus.

**Earlier dependencies.** [M01](#m01), [M04](#m04), [M05](#m05).

**Story role.** Fixes the shared geometry and notation used by the lower bound and the physical preparation.

**Conceptual connection.** The stabilizer lattice and the circuit's cell lattice describe the same physical system but assign different roles to edges and sites.

**Sources.** Preskill [§7.18.1][p7181]; bridge [stabilizers and logical labels](PRESKILL_BRIDGE.md#stabilizers-and-logical-labels); [local braiding, §2](../science/local-braiding.md#2-cell-lattice-and-toric-operators) and [preparation, §1](../science/preparation.md#1-lattice-target-and-permitted-operations).

### M07

**Open strings and endpoint syndromes**

**Central question.** Why does a $`Z`$ string change the star syndrome only at its endpoints?

**Understanding target.** Express the syndrome produced by an edge set as its binary vertex boundary. Track how applying a single-edge correction moves or cancels a defect, and why an allowed full star syndrome has even total parity.

**Earlier dependencies.** [M01](#m01), [M06](#m06).

**Story role.** Gives both sides of the argument a common object: open strings create the algebraic obstruction and also remove preparation defects.

**Conceptual connection.** Error correction becomes a relation between a binary edge flow and its boundary.

**Sources.** Preskill [§7.18.2][p7182] and [§7.18.3][p7183]; bridge [syndromes and physical output](PRESKILL_BRIDGE.md#syndromes-and-physical-output); [preparation, §5](../science/preparation.md#5-local-removal-of-all-nonroot-defects).

### M08

**Deforming a string within a region**

**Central question.** When do two different paths act identically on a toric-code state?

**Understanding target.** Show that two paths with the same endpoints agree on the code space when their product is a contractible plaquette boundary. Relate a product of stars to a closed cut, and retain the distinction between an exact operator identity and an equality that holds only on code states.

**Earlier dependencies.** [M05](#m05), [M06](#m06), [M07](#m07).

**Story role.** Supplies the deformation relation needed for the local braiding lemma and the freedom to choose correction paths.

**Conceptual connection.** Multiplying by local constraints changes a geometric representative while preserving its action on the encoded state.

**Sources.** Preskill [§7.18.1][p7181] and [§7.18.2][p7182]; bridge [stabilizers and logical labels](PRESKILL_BRIDGE.md#stabilizers-and-logical-labels); [local braiding, §3](../science/local-braiding.md#3-an-explicit-braiding-patch).

### M09

**Global cycles and logical labels**

**Central question.** What information remains after every local star and plaquette is satisfied?

**Understanding target.** Identify the two encoded qubits on the torus and distinguish contractible stabilizer loops from noncontractible logical loops. Explain why fixing two independent logical $`Z`$ eigenvalues selects one pure state from the four-dimensional ground space.

**Earlier dependencies.** [M05](#m05), [M08](#m08).

**Story role.** Separates the full-code-space target used by the converse from the particular pure state produced by the construction.

**Conceptual connection.** Local deformation equivalence leaves global winding classes that label encoded information.

**Sources.** Preskill [§7.10.4][p7104] and [§7.18.1][p7181]; bridge [stabilizers and logical labels](PRESKILL_BRIDGE.md#stabilizers-and-logical-labels); [preparation, §1](../science/preparation.md#1-lattice-target-and-permitted-operations).

### M10

**Code membership with correlated environments**

**Central question.** Does satisfying every code constraint require the logical state to factor from all other systems?

**Understanding target.** Distinguish membership in the code space from decoupling of the encoded information. Allow the logical degrees of freedom to remain entangled with retained environments and correlated with private classical records while every stabilizer still acts as $`+1`$. Identify which identities survive this generality.

**Earlier dependencies.** [M03](#m03), [M05](#m05), [M09](#m09).

**Story role.** Removes an unjustified factorization assumption that would otherwise weaken the local-channel converse.

**Conceptual connection.** Error-correction language about environments clarifies why a projector constraint and a statement of independence are different mathematical claims.

**Sources.** Preskill [§§7.3.2–7.3.3][p733]; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [channel overlap, §3](../science/channel-overlap.md#3-projecting-onto-the-full-code-space).

### M11

**The physical output and its accuracy criterion**

**Central question.** What must be present in the data registers when preparation is declared complete?

**Understanding target.** Interpret $`F=\mathrm{Tr}(P_{\mathrm{TC}}\rho)`$ as unconditional ground-space weight, compare it with the fidelity to one specified pure ground state, and distinguish it from small energy density or agreement on local observables. Explain why a stored description of an unapplied Pauli correction does not by itself meet this output contract.

**Earlier dependencies.** [M02](#m02), [M07](#m07), [M09](#m09), [M10](#m10).

**Story role.** Defines the common task against which the converse and construction are compared.

**Conceptual connection.** The operational meaning of “prepared” determines whether correction information must be transported and acted upon.

**Sources.** Preskill [§7.5.1][p751] and [§7.18.3][p7183] provide the fidelity and recovery context; bridge [syndromes and physical output](PRESKILL_BRIDGE.md#syndromes-and-physical-output); [model, §1](../science/model.md#1-lattice-registers-and-target) and [consequences, §5](../science/consequences.md#5-the-output-contract).

### M12

**A causal protocol with charged communication**

**Central question.** Which information can change a distant operation or the global execution schedule?

**Understanding target.** Separate private local records, a freely shared initial seed, counted local propagation, and charged nonlocal bits. Require the seed and charged transcript to determine global event choices, support partitions, message routing, and termination. Count outcome-dependent timing, silence, or addressing when they convey information.

**Earlier dependencies.** [M02](#m02), [M04](#m04), [M11](#m11).

**Story role.** States the information boundary that makes a communicated-bit theorem meaningful.

**Conceptual connection.** A decoder is a distributed causal procedure; its control signals have locations and cannot be supplied by an uncharged global scheduler.

**Sources.** Preskill [§7.18.3][p7183] supplies the recovery setting; bridge [locality and causal depth](PRESKILL_BRIDGE.md#locality-and-causal-depth) and [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) add the resource model; [model, §§3–4](../science/model.md#3-a-causal-adaptive-schedule).

### M13

**Branch probabilities and two communication budgets**

**Central question.** How should a rare execution branch contribute to the preparation's accuracy and cost?

**Understanding target.** Use a positive subnormalized output $`\sigma_t`$ whose trace is the branch probability; its contribution to $`F`$ is $`\mathrm{Tr}(P_{\mathrm{TC}}\sigma_t)`$. Distinguish a cap $`C`$ on every transcript from its mean length $`\overline C`$, and recognize why physically terminating transcript leaves are prefix free.

**Earlier dependencies.** [M03](#m03), [M11](#m11), [M12](#m12).

**Story role.** Preserves probability weights before any branchwise lower-bound argument is attempted.

**Conceptual connection.** Quantum branch weights and classical codeword lengths describe the same execution tree from two different perspectives.

**Sources.** Preskill [§7.2][p72] provides the channel language; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) adds the transcript and coding tools; [model, §4](../science/model.md#4-broadcast-and-delivered-bit-conventions) and [communication bounds, §2](../science/communication-bound.md#2-fixed-transcript-domination).

### M14

**Background synthesis: one complete preparation problem**

**Central question.** How do the quantum target, spatial causality, and classical information rules fit into one precise task?

**Understanding target.** Specify an admissible protocol from a seed-conditioned product input through local channels and charged messages to a physical data output. State exactly what $`L,N,r,D,C,\overline C,F`$ measure, why local ancillas and private records are allowed, and which global controls must appear in the transcript.

**Earlier dependencies.** [M04](#m04), [M09](#m09), [M10](#m10), [M11](#m11), [M12](#m12), [M13](#m13).

**Story role.** Completes the background phase with the full model that every subsequent claim must obey.

**Conceptual connection.** The toric code supplies the target's algebra, while the causal protocol determines which physical resources can create it.

**Sources.** Preskill [§§7.18.1–7.18.3][p7181]; bridge [source map](PRESKILL_BRIDGE.md#source-map) and [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [model](../science/model.md) and [scientific overview](../science/README.md).

## Phase II — Narrative and innovation

The two local mechanisms now develop together: a causal patch imposes an unavoidable overlap loss, while a correction block removes all but one syndrome parity. Their global extensions meet at the same area-per-depth-squared scale.

### M15

**Three string identities on one patch**

**Central question.** Which local relations encode braiding strongly enough to constrain a prepared state?

**Understanding target.** Construct a star-product cut $`A_0`$ and two deformable open strings $`B_0,B'_0`$ such that, on every code-space vector, $`A_0\chi=\chi`$, $`B_0\chi=B'_0\chi`$, and $`A_0B_0\chi=-B_0\chi`$. Explain the odd crossing around one endpoint and why the identities also hold with correlated auxiliary systems.

**Earlier dependencies.** [M08](#m08), [M10](#m10), [M14](#m14).

**Story role.** Isolates the local topological obstruction before any circuit or communication estimate is applied.

**Conceptual connection.** String deformation and an anticommuting crossing jointly constrain a state more strongly than either fact alone.

**Sources.** Preskill [§7.18.1][p7181] and [§7.18.2][p7182] supply the string setting; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments) connects it to the project; [local braiding, §3](../science/local-braiding.md#3-an-explicit-braiding-patch).

### M16

**A dimension-independent loss of product overlap**

**Central question.** Why do those string identities forbid near-unit probability for a prescribed product reference on the patch?

**Understanding target.** Follow the vector-norm proof for a partition $`E\sqcup U\sqcup V`$, ending with $`2\sqrt p\le8\sqrt{1-p}`$ and hence $`p\le16/17`$. Identify exactly where the reference vector factors, why the state itself need not factor, and why no local dimension enters the estimate.

**Earlier dependencies.** [M03](#m03), [M10](#m10), [M15](#m15).

**Story role.** Converts the qualitative local algebra into a numerical obstruction that can be repeated across space.

**Conceptual connection.** Approximate agreement with a product reference is incompatible with the two exact ways the braiding operators act on the state.

**Sources.** Preskill [§7.10.1][p7101] and [§§7.3.2–7.3.3][p733] provide the operator and environment background; bridge [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply) separates the additional lemma; [local braiding, §1](../science/local-braiding.md#1-dimension-independent-algebra-lemma).

### M17

**A braiding patch that survives causal spreading**

**Central question.** How can the algebraic support partition remain valid after every operator is dressed by a local circuit?

**Understanding target.** Set $`R=rD`$ and $`s=R+1`$, and follow the explicit side-$`32s`$ patch. Check that the two thickened open strings meet only inside the endpoint regions, that the thickened closed cut avoids those regions, and that all dressed supports remain inside the patch whenever it fits on the torus.

**Earlier dependencies.** [M04](#m04), [M15](#m15), [M16](#m16).

**Story role.** Turns a topological drawing into the exact finite geometry required by the algebra lemma.

**Conceptual connection.** A light cone converts circuit depth into the spatial buffer needed to preserve a braiding relation.

**Sources.** Preskill [§7.18.1][p7181] supplies the geometric code language; bridge [locality and causal depth](PRESKILL_BRIDGE.md#locality-and-causal-depth) adds operator dressing; [local braiding, §§3–5](../science/local-braiding.md#3-an-explicit-braiding-patch).

### M18

**A correction block compresses to one parity**

**Central question.** How much syndrome information remains after a block is allowed depth proportional to its side length?

**Understanding target.** Partition any $`L\times L`$ torus into $`B=\lfloor L/\ell\rfloor^2`$ balanced blocks whose side lengths lie between $`\ell`$ and $`2\ell-1`$. Trace the local row and column sweeps that physically remove all nonroot defects and leave each root holding exactly its block's parity.

**Earlier dependencies.** [M02](#m02), [M07](#m07), [M09](#m09), [M14](#m14).

**Story role.** Provides the constructive counterpart of a causal patch and explains the candidate scale $`N/\ell^2`$ before it is proved necessary.

**Conceptual connection.** Local correction eliminates detailed defect positions while conserving one boundary-relevant parity per block.

**Sources.** Preskill [§7.18.2][p7182] and [§7.18.3][p7183]; bridge [the matching construction](PRESKILL_BRIDGE.md#the-matching-construction) and [worked four-block correction](PRESKILL_BRIDGE.md#worked-four-block-correction); [preparation, §§3–5](../science/preparation.md#3-star-extraction-in-bounded-depth).

### M19

**Projecting the output while retaining every environment**

**Central question.** How does a bound on product overlap constrain the actual output of an arbitrary local channel circuit?

**Understanding target.** Purify the cell-product input and retain all local environments in a dilation $`W`$. For $`F>0`$, define $`|\chi\rangle=(P_{\mathrm{TC}}\otimes I)W|\boldsymbol0\rangle/\sqrt F`$ and $`|\Omega\rangle=W^\dagger|\chi\rangle`$. Derive $`|\langle\boldsymbol0|\Omega\rangle|^2=F`$ without factoring the logical state from its environment. Treat the projection as an analysis device rather than an allowed preparation step.

**Earlier dependencies.** [M03](#m03), [M10](#m10), [M14](#m14), [M17](#m17).

**Story role.** Extends the local obstruction to the full class of channels allowed by the model.

**Conceptual connection.** Pulling back a projected output transfers exact code identities into a state whose overlap with the original product input is the desired accuracy.

**Sources.** Preskill [§7.2][p72] and [§7.3.3][p733] provide the dilation and reference-system background; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [channel overlap, §§2–3](../science/channel-overlap.md#2-local-dilation-and-the-exact-propagation-radius).

### M20

**Multiplying patch losses without assuming independence**

**Central question.** Why can many local overlap obstructions give an exponential global bound even when the patches are correlated?

**Understanding target.** Pack $`m=\lfloor L/[32(rD+1)]\rfloor^2`$ disjoint patches and apply their product-reference projections successively. Show that earlier projections commute with the untouched patch's dressed strings and preserve its identities, giving the conditional bound at every step and therefore $`F\le q=(16/17)^m`$.

**Earlier dependencies.** [M16](#m16), [M17](#m17), [M19](#m19).

**Story role.** Produces the global no-message theorem from a local algebraic loss.

**Conceptual connection.** Preserved conditional constraints can multiply probabilities even when marginal distributions do not factor. The packing number, rather than a count of records or logical qubits, sets the exponent.

**Sources.** Preskill [§7.18.1][p7181] supplies the code identities; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments) introduces the project extension; [channel overlap, §§4–5](../science/channel-overlap.md#4-packing-and-successive-product-projections).

### M21

**Solving the remaining global parity problem**

**Central question.** How can the block-root parities be joined with only order one communicated bits per block?

**Understanding target.** Gather the noncontroller root parities in a fixed schedule, solve the binary correction flow on a nonwrapping coarse comb tree, and return each subtree-parity coefficient to the parent that owns its physical correction path. Explain why total even parity makes the root equation consistent.

**Earlier dependencies.** [M08](#m08), [M09](#m09), [M12](#m12), [M18](#m18).

**Story role.** Shows where genuinely nonlocal information enters the construction and accounts for both incoming and outgoing traffic.

**Conceptual connection.** The coarse syndrome is a boundary condition for a tree flow; the controller must communicate the solution to the sites that execute it.

**Sources.** Preskill [§7.18.2][p7182] and [§7.18.3][p7183] supply the boundary and recovery language; bridge [worked four-block correction](PRESKILL_BRIDGE.md#worked-four-block-correction); [preparation, §6](../science/preparation.md#6-fixed-nonlocal-collection-and-return-traffic).

### M22

**Executing the correction and closing the upper bound**

**Central question.** What additional work turns the controller's answer into the claimed quantum output?

**Understanding target.** Propagate every correction coefficient along its assigned short physical path, including zero-valued instructions, using disjoint-support layers. Prove that the resulting boundary cancels the syndrome while preserving both logical $`Z`$ labels. Recover $`D\le12\ell+2`$, $`C\le2(B-1)`$, and the all-local endpoint $`C=0`$, $`D\le2L+8`$.

**Earlier dependencies.** [M11](#m11), [M18](#m18), [M21](#m21).

**Story role.** Completes an exact preparation whose output and resource accounting satisfy the same model as the converse.

**Conceptual connection.** Solving a decoding equation and physically applying its answer are separate causal tasks; identical corrected branch outputs make record disposal harmless.

**Sources.** Preskill [§7.18.3][p7183]; bridge [the matching construction](PRESKILL_BRIDGE.md#the-matching-construction) and [worked four-block correction](PRESKILL_BRIDGE.md#worked-four-block-correction); [preparation, §§7–8](../science/preparation.md#7-local-execution-of-the-coarse-correction).

### M23

**A fixed transcript has a local completion**

**Central question.** How can the no-message theorem constrain a branch that used nonlocal communication?

**Understanding target.** Fix the public seed and communicated transcript, preprogram its remote controls, and retain all uncommunicated private outcomes. Complete each local consistency selection to obtain a local trace-preserving output $`\widehat\rho_t`$ with $`\sigma_t\preceq\widehat\rho_t`$ and the same depth cap. Understand the CP-order composition argument and why classical-read completions add no spatial layers.

**Earlier dependencies.** [M03](#m03), [M12](#m12), [M13](#m13), [M20](#m20).

**Story role.** Transfers the geometric overlap obstruction to each communicated branch without discarding its probability.

**Conceptual connection.** Presetting a transcript removes remote control, while positive-map domination preserves the weight of the histories consistent with that transcript.

**Sources.** Preskill [§7.2][p72] supplies the channel background; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) adds completion and branch accounting; [communication bounds, §2](../science/communication-bound.md#2-fixed-transcript-domination).

### M24

**A hard communication cap limits total ground-space weight**

**Central question.** How many bounded-overlap branches can a $`C`$-bit protocol combine?

**Understanding target.** For each public seed, use at most $`2^C`$ prefix-free terminal transcripts and the contribution bound $`\mathrm{Tr}(P_{\mathrm{TC}}\sigma_t)\le q`$ to derive $`F\le\min\{1,2^Cq\}`$ after averaging over the seed. Obtain the uniform fixed-overlap inequality $`(C+1)(D+1)^2\ge c_{f,r}N`$ from the finite packing estimate, including the small-lattice and deep-circuit endpoints.

**Earlier dependencies.** [M13](#m13), [M20](#m20), [M23](#m23).

**Story role.** Establishes the worst-case communicated-bit converse and its robust accuracy dependence.

**Conceptual connection.** A geometric bound on one branch becomes an information-resource bound through the number of distinguishable terminal histories.

**Sources.** Preskill [§7.18.1][p7181] supplies the code-space context; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) supplies the additional counting argument; [communication bounds, §3](../science/communication-bound.md#3-worst-case-communication).

### M25

**Expected communication requires an entropy argument**

**Central question.** Can rare long transcripts evade the cost required at fixed unconditional accuracy?

**Understanding target.** Derive $`\overline C\ge H(\mathsf T\mid\mathsf S)\ge\max\{0,F\log_2(F/q)\}`$ from branch contributions and physical prefix coding. Keep the imagined ground-space test as a mathematical random variable, retain the branchwise depth cap, and handle almost sure termination after conditioning on almost every seed.

**Earlier dependencies.** [M13](#m13), [M23](#m23), [M24](#m24).

**Story role.** Gives the separate mean-cost converse needed for variable-length protocols.

**Conceptual connection.** Successful ground-space weight must be spread over enough transcripts to force entropy, and a physical prefix code must pay at least that entropy in mean length.

**Sources.** Preskill [§7.2][p72] supplies the outcome-probability setting; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) adds the classical coding and entropy proof; [communication bounds, §4](../science/communication-bound.md#4-expected-communication-and-prefix-coding).

### M26

**Acceptance, unconditional weight, and a usable success flag**

**Central question.** What changes if a protocol is assessed only on selected successful executions?

**Understanding target.** Select existing positive classical branch contributions and retain their unconditional contribution $`p f_{\mathrm{acc}}`$. Explain why the same hard-cap converse bounds that quantity, why it does not authorize an added global quantum filter, and why making a distributed acceptance condition available at one site can itself require resources.

**Earlier dependencies.** [M11](#m11), [M13](#m13), [M23](#m23), [M24](#m24).

**Story role.** Specifies the probability and output conditions under which the communication theorem remains operationally meaningful.

**Conceptual connection.** A conditional state, its probability of occurrence, and a physically available herald are three distinct objects.

**Sources.** Preskill [§7.2][p72] and [§7.18.3][p7183] provide the channel and recovery context; bridge [syndromes and physical output](PRESKILL_BRIDGE.md#syndromes-and-physical-output) and [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits); [communication bounds, §5](../science/communication-bound.md#5-selected-success-events).

### M27

**Matching the depth–communication frontier**

**Central question.** In what precise sense do the converse and construction determine the optimal resource scaling?

**Understanding target.** Compare the fixed-$`f,r`$ lower bounds for $`C`$ and $`\overline C`$ with the exact block preparation. Explain the extensive bit cost at constant depth, the $`N/(D+1)^2`$ scale in the intermediate regime, and the zero-communication endpoint at depth of order $`L`$. Interpret matching as equality of scaling up to constants and resource rescaling.

**Earlier dependencies.** [M20](#m20), [M22](#m22), [M24](#m24), [M25](#m25), [M26](#m26).

**Story role.** Brings the obstruction and the constructive protocol together in the main global result.

**Conceptual connection.** Local causal area sets both how much syndrome detail can be eliminated before communication and how many unavoidable obstructions remain.

**Sources.** Preskill [§7.18.1][p7181] and [§7.18.3][p7183] supply the common code and recovery setting; bridge [the matching construction](PRESKILL_BRIDGE.md#the-matching-construction) and [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [consequences, §§1–3](../science/consequences.md#1-an-optimal-exchange-of-resources).

### M28

**Identifying the contribution and its reach**

**Central question.** What does a quantitative communicated-bit frontier add to known code geometry and measurement-assisted preparation?

**Understanding target.** Separate the inherited braiding obstruction and standard syndrome-correction ingredients from their conversion into a charged-information theorem for arbitrary allowed local channels. Explain why a bound valid for every decoder is stronger than counting the messages in one stabilizer algorithm, and distinguish preparation-resource bounds from bounds on code parameters.

**Earlier dependencies.** [M15](#m15), [M20](#m20), [M23](#m23), [M27](#m27).

**Story role.** Locates the innovation and states the generality that gives the resource law its significance.

**Conceptual connection.** The same spatial structure can constrain encoded information, local preparation, or communication, but those are different tasks with different resource variables.

**Sources.** Preskill [§7.19][p719] and [§7.20][p720] give the comparison with geometric code constraints; bridge [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [communication bounds, §6](../science/communication-bound.md#6-relation-to-the-construction-and-prior-work) and the [research-source comparison](../references/related-work.md).

### M29

**Converting the resource law into preparation time**

**Central question.** What time law follows when the classical network has a fixed aggregate delivered throughput?

**Understanding target.** Under the stated ideal-switch assumptions, use $`D\le T`$ and $`C\le\beta T`$ and optimize the constructive time $`\ell+N/(\beta\ell^2)`$. Interpret the resulting scale $`\max\{1,\min\{L,(N/\beta)^{1/3}\}\}`$, including the all-local $`\beta=0`$ limit. Identify exactly which additional architecture assumptions make this conversion valid.

**Earlier dependencies.** [M12](#m12), [M22](#m22), [M27](#m27).

**Story role.** Gives an end-to-end operational consequence of the matched resource frontier.

**Conceptual connection.** Local aggregation time and remote traffic compete, so their balance selects a block size and a preparation-time exponent.

**Sources.** Preskill [§7.18.3][p7183] supplies the recovery task, while the timing model is an added project assumption; bridge [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [consequences, §4](../science/consequences.md#4-a-conditional-preparation-time-law).

### M30

**Narrative synthesis: from one crossing to a global resource law**

**Central question.** How do local braiding, branch probabilities, and executed corrections jointly determine the cost of preparation?

**Understanding target.** Reconstruct the complete chain: local string algebra, buffered causal patches, full-code-space channel overlap, fixed-transcript domination, hard and mean communication bounds, and exact physical correction. Explain how the two directions meet, what the conditional timing consequence adds, and which changes to initial resources, causality, accuracy, or output would require a different theorem.

**Earlier dependencies.** [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29).

**Story role.** Completes the narrative phase with one coherent account of the theorem, its mechanism, and its scope.

**Conceptual connection.** The local algebra fixes a global preparation cost only after spatial causality, probability, and the physical output are kept in the same accounting.

**Sources.** Preskill [§§7.18–7.20][p718]; bridge [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [scientific overview](../science/README.md), [communication bounds](../science/communication-bound.md), [preparation](../science/preparation.md), and [consequences](../science/consequences.md).

## Anchor source

All Preskill links below refer to the same March 2026 author draft. A PDF page number is six larger than the printed chapter page number; the links use physical PDF page numbers. The [bridge source map](PRESKILL_BRIDGE.md#source-map) records the relevant sections and conventions. No additional textbook is required by this map.

[preskill]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf
[p71]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=7
[p72]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=10
[p733]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=15
[p751]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=21
[p7101]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=33
[p7102]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=36
[p7104]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=39
[p718]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=57
[p7181]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=58
[p7182]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=60
[p7183]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=61
[p719]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=66
[p720]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=69


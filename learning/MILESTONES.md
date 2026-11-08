# Thirty milestones for topological preparation resources

Two questions share the same physical output: **how many nonlocal classical bits replace local toric-code preparation depth, and how much depth is needed when measurement reports are noisy?** The single educational anchor is John Preskill's [Quantum Information, Chapter 7: Quantum Error Correction, updated March 2026][preskill]. The [Preskill bridge](PRESKILL_BRIDGE.md#source-map) connects that chapter to the additional circuit, probability, communication, and readout arguments.

The allocation remains **14 background milestones and 16 narrative milestones**. The background builds from Pauli signs and local records to the toric target and the two distinct information interfaces. The narrative first develops the shared braiding obstruction and the original charged-bit frontier, then combines a buffered local test with physical syndrome compression and protected readout. Its final synthesis explains why both resource laws require actual corrected data states. This is one connected 30-stop map, not two appended courses.

The assumed starting language is finite-dimensional vectors and operators, tensor products, and elementary probability. Preskill supplies the error-correction foundations. The bridge and primary research sources supply the additional preparation-resource proofs; neither theorem is attributed to the textbook. The canonical statements are in [science](../science/README.md).

Throughout, $`N=2L^2`$ and $`F=\mathrm{Tr}(P_{\mathrm{TC}}\rho_{\mathrm{out}})`$ is unconditional physical ground-space weight. In the charged-communication model, $`D`$ is local depth, $`C`$ is the hard nonlocal-bit cap, and $`\overline C`$ is mean message length. In the noisy-report model, $`T`$ includes readouts and physical corrections, $`p`$ is BSC crossover probability, $`\nu`$ bounds report slots per cell and layer, and already public reports have free global classical feedforward. Fixed local memory is counted in quantum qubits, not controller storage.

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

**Two information interfaces for one preparation task**

**Central question.** Which information is paid for, and which information can the controller actually see?

**Understanding target.** Contrast charged nonlocal communication with the noisy-report interface. In the first model local propagation counts and nonlocal control needs a paid transcript. In the second, each fresh true outcome entering classical control crosses an independent unflagged BSC, while already public reports can be processed and broadcast for free. Retained true pointers are local quantum memory operated on through counted gates. Identify why a perfect classical copy of such a pointer, a free extra detector, or finite-speed feedforward would change the theorem.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M04](#m04), [M11](#m11).

**Story role.** Defines the receiving model before any result is transferred between the sister projects.

**Conceptual connection.** Identical data targets can have different preparation costs because accessible records and communication conventions differ.

**Sources.** Preskill [§7.1][p71] and [§7.18.3][p7183]; bridge [two resource models](PRESKILL_BRIDGE.md#two-resource-models-for-the-same-physical-target); [charged model](../science/model.md) and [noisy-readout model](../science/noisy-readout.md).

### M13

**Weighted branches, report noise, and independent slots**

**Central question.** Which probabilities survive averaging over private outcomes and noisy reports?

**Understanding target.** Use a positive subnormalized branch state whose trace is its physical probability. Distinguish a hard transcript cap from a mean length, and explain prefix-free termination. In the noisy model write a public report as $`y=x\oplus e`$ with independent $`e\sim\mathrm{Ber}(p)`$, including a fresh error for every repeated report. Distinguish report independence from independence of the quantum states or true pointer values. Hidden noise flags used by a proof are inaccessible to the protocol.

**Earlier dependencies.** [M03](#m03), [M11](#m11), [M12](#m12).

**Story role.** Preserves execution weights and the exact detector interface.

**Conceptual connection.** Conditioning, latent quantum records, and public observations are different operations on one joint probability model.

**Sources.** Preskill [§7.2][p72]; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits) and [buffered blindness](PRESKILL_BRIDGE.md#buffered-blindness-with-outside-records); [communication bound](../science/communication-bound.md) and [noisy readout](../science/noisy-readout.md).

### M14

**Background synthesis: specify the whole physical contract**

**Central question.** What must a complete statement say before its preparation depth or communication can be optimized?

**Understanding target.** Specify the seed-conditioned cell-product input, fixed range, disjoint supports, branchwise depth cap, output data, and unconditional $`F`$. State separately each information interface. In the noisy case include fixed report density and quantum-memory density, ideal quantum gates/storage, and the distinction between QND and destructive pointer readout. Explain why low energy density, a frame label, or logical recoverability after a hypothetical ideal recovery does not establish the requested physical output.

**Earlier dependencies.** [M04](#m04), [M09](#m09), [M10](#m10), [M11](#m11), [M12](#m12), [M13](#m13).

**Story role.** Completes the local-to-global background phase.

**Conceptual connection.** An operational resource theorem is a relation between an explicit input, allowed causal controls, and an output already delivered.

**Sources.** Preskill [§§7.18.1–7.18.3][p7181]; bridge [source map](PRESKILL_BRIDGE.md#source-map) and [two resource models](PRESKILL_BRIDGE.md#two-resource-models-for-the-same-physical-target); [model](../science/model.md) and [noisy readout](../science/noisy-readout.md).

## Phase II — Narrative and innovation

The shared local obstruction first gives the charged-bit frontier. A buffered version then couples to report noise, while physical quantum compression makes protected readout attainable at fixed memory density.

### M15

**Braiding identities on one patch**

**Central question.** Which local operator relations constrain every toric ground-space state?

**Understanding target.** Construct a star-product cut $`A_0`$ and deformable open strings $`B_0,B'_0`$. Explain $`A_0\chi=\chi`$, $`B_0\chi=B'_0\chi`$, and $`A_0B_0\chi=-B_0\chi`$ from stabilizer deformation and one crossing. Keep the identities valid when the code state is correlated with other systems. These are contractible local structures, not fixed noncontractible logical labels.

**Earlier dependencies.** [M08](#m08), [M10](#m10), [M14](#m14).

**Story role.** Isolates the common topological obstruction.

**Conceptual connection.** Deformation and an anticommuting crossing constrain a state jointly.

**Sources.** Preskill [§7.18.1][p7181] and [§7.18.2][p7182]; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [local braiding](../science/local-braiding.md).

### M16

**A constant loss on a dressed causal patch**

**Central question.** Why does the obstruction survive finite depth and arbitrary local Hilbert-space dimension?

**Understanding target.** Follow the product-reference vector argument on $`E\sqcup U\sqcup V`$: $`2\sqrt a\le8\sqrt{1-a}`$ forces $`a\le16/17`$. Distinguish factorization of the reference from factorization of the tested state. Dressing by a local dilation thickens the strings by radius $`R`$, so a side-$`32(R+1)`$ patch suffices. No ancilla dimension appears in the algebra.

**Earlier dependencies.** [M03](#m03), [M04](#m04), [M15](#m15).

**Story role.** Makes the qualitative obstruction quantitative and usable in both models.

**Conceptual connection.** Causality sets the patch size; the operator identities set its nonzero loss.

**Sources.** Preskill [§7.10.1][p7101] and [§§7.3.2–7.3.3][p733]; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [local braiding, §§3–5](../science/local-braiding.md).

### M17

**From a local loss to full code-space overlap**

**Central question.** How can many local obstructions bound a mixed output without assuming independent patches?

**Understanding target.** Dilate the local CPTP circuit, project its output onto the full code space, and pull the normalized projection back. Its squared overlap with the original product vector is $`F`$. Pack $`m=\lfloor L/[32(rD+1)]\rfloor^2`$ patches and project their product references successively. Earlier projections preserve the untouched patch identities, giving $`F\le q_0=(16/17)^m`$. Neither output purity nor environment decoupling is needed.

**Earlier dependencies.** [M10](#m10), [M11](#m11), [M16](#m16).

**Story role.** Establishes the original no-message theorem.

**Conceptual connection.** Conditional inequalities can multiply even when adaptive or projected marginals are correlated.

**Sources.** Preskill [§7.2][p72] and [§7.3.3][p733]; bridge [local channels and correlated environments](PRESKILL_BRIDGE.md#local-channels-and-correlated-environments); [channel overlap](../science/channel-overlap.md).

### M18

**A block physically removes syndrome detail**

**Central question.** Why does local processing of a rectangle leave only one relevant parity?

**Understanding target.** Partition the torus into $`B=\lfloor L/\ell\rfloor^2`$ balanced rectangles of side lengths between $`\ell`$ and $`2\ell-1`$. Follow the row/column comb sweep: moving a defect along a corrected edge clears its child and adds its bit to the parent. All nonroots become defect free and each root retains its block parity. This is a change of the physical data, rather than a compressed description of defects still present.

**Earlier dependencies.** [M07](#m07), [M09](#m09), [M14](#m14).

**Story role.** Provides the constructive counterpart of causal patch area.

**Conceptual connection.** Local correction can reduce the remaining coordination task while sending discarded detail into local environments or records.

**Sources.** Preskill [§7.18.2][p7182] and [§7.18.3][p7183]; bridge [the matching construction](PRESKILL_BRIDGE.md#the-matching-construction); [preparation, §§3–5](../science/preparation.md).

### M19

**A transcript pays for its total branch weight**

**Central question.** How does the geometric theorem constrain a protocol with nonlocal messages?

**Understanding target.** Fix a transcript and preset its remote controls. Complete sender consistency selections locally while preserving all private outcomes, obtaining $`\sigma_t\preceq\widehat\rho_t`$ and branch contribution at most $`q_0`$. Use at most $`2^C`$ leaves to derive $`F\le\min\{1,2^Cq_0\}`$. Then connect physical prefix lengths to $`\overline C\ge H(\mathsf T\mid\mathsf S)\ge\max\{0,F\log_2(F/q_0)\}`$. A normalized rare branch cannot replace its subnormalized contribution.

**Earlier dependencies.** [M13](#m13), [M17](#m17).

**Story role.** Turns the spatial obstruction into hard and mean communication converses.

**Conceptual connection.** Removing remote dependence and retaining probabilities are both necessary before transcript counting applies.

**Sources.** Preskill [§7.2][p72] supplies channel background; bridge [from overlap to communicated bits](PRESKILL_BRIDGE.md#from-overlap-to-communicated-bits); [communication bound, §§2–5](../science/communication-bound.md).

### M20

**Closing the charged-communication frontier**

**Central question.** What work makes the coarse decoder's answer into the physical toric state?

**Understanding target.** Solve the residual even syndrome on a coarse comb tree. Count collected parities and returned subtree coefficients, then propagate each instruction through local layers while applying its physical $`Z`$ edges. Recover $`D\le12\ell+2`$ and $`C\le2(B-1)`$, matching $`(C+1)(D+1)^2=\Omega(N)`$ at fixed positive overlap. Explain why the additional throughput law from $`C\le\beta T`$ needs its own ideal-switch assumptions and is unrelated to detector noise.

**Earlier dependencies.** [M18](#m18), [M19](#m19).

**Story role.** Completes the original constructive/converse story before changing interfaces.

**Conceptual connection.** Local aggregation and delivered correction messages attain the same area-per-depth-squared resource scale.

**Sources.** Preskill [§7.18.3][p7183]; bridge [worked four-block correction](PRESKILL_BRIDGE.md#worked-four-block-correction); [preparation](../science/preparation.md) and [consequences](../science/consequences.md).

### M21

**The local two-loop test**

**Central question.** What local test can detect the same obstruction when only one region loses its reports?

**Understanding target.** Define $`C_0=B_0B'_0`$ and $`K=(I+A_0)(I+C_0)/4`$. Verify that the two closed loop factors commute, every toric ground state passes, and $`P_{\mathrm{TC}}\preceq K`$. Projecting onto $`K`$ supplies exactly the three identities of M15, hence $`\mathrm{Tr}(K\rho)\le16/17`$ for a fixed-schedule depth-$`T`$ local CPTP circuit from a product input. It does not test logical-sector labels.

**Earlier dependencies.** [M15](#m15), [M16](#m16), [M17](#m17).

**Story role.** Makes the inherited obstruction local enough to couple to report blindness.

**Conceptual connection.** A weak local acceptance test can still provide a uniform deficit for every admissible local channel.

**Sources.** Preskill [§7.18.1][p7181]; bridge [the local two-loop test](PRESKILL_BRIDGE.md#the-local-two-loop-test); [noisy-readout converse](../science/noisy-readout.md).

### M22

**Buffer first, retain outside records, then condition**

**Central question.** Why is averaging unread outcomes insufficient when outside outcomes are selected later?

**Understanding target.** Put the side-$`32(R+1)`$ core inside a side-$`36(R+1)`$ blind block, with distance greater than $`2R`$ from its complement. Freeze a complete public history. Complete each outside instrument to a CPTP map retaining its true-outcome register at creation; retain other outside test outputs too. Their backward cones are disjoint from the core cone, so the fixed-history CPTP state factors before record selection. Only then project outside registers, obtaining $`\mathrm{Tr}(KH\Omega)\le(16/17)\mathrm{Tr}(H\Omega)`$ for every allowed positive outside effect $`H`$.

**Earlier dependencies.** [M03](#m03), [M04](#m04), [M10](#m10), [M13](#m13), [M21](#m21).

**Story role.** Supplies the load-bearing transfer from a blind strip to a blind topological core.

**Conceptual connection.** Trace-decreasing branches cannot be canceled as trace preserving; retaining their records makes the later conditioning legitimate.

**Sources.** Preskill [§§7.3.2–7.3.3][p733] provide environment background; bridge [buffered blindness](PRESKILL_BRIDGE.md#buffered-blindness-with-outside-records); [noisy readout](../science/noisy-readout.md), using the retained-record discipline of [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits).

### M23

**Many blind cores under unflagged BSC noise**

**Central question.** How do rare local blindness events constrain the unconditional physical output?

**Understanding target.** Represent a BSC as truthful reporting with probability $`1-2p`$ and a fair independent report with probability $`2p`$, keeping the mixture flags hidden. Pack $`M=\lfloor L/[36(rT+1)]\rfloor^2`$ blocks and pad each to $`k=1296\nu(rT+1)^2T`$ potential slots. Each block is blind with probability $`(2p)^k`$. Apply M22 successively with the other core tests retained, then average the independent hidden flags to obtain $`F\le[1-(2p)^k/17]^M`$. Final quantum core states need not be independent.

**Earlier dependencies.** [M13](#m13), [M21](#m21), [M22](#m22).

**Story role.** Turns buffered conditioning into a finite unconditional overlap bound.

**Conceptual connection.** Independence is used for detector flags; multiplicativity of quantum tests comes from the conditional trace inequality.

**Sources.** Preskill [§7.5.2][p752] supplies independent-noise context; bridge [from blind cores to a depth bound](PRESKILL_BRIDGE.md#from-blind-cores-to-a-depth-bound); [noisy readout](../science/noisy-readout.md).

### M24

**What the lower bound proves**

**Central question.** Why does a space-time blind block lead to a cube root of a logarithm?

**Understanding target.** For fixed $`p,r,\nu`$ and $`F\ge f>0`$, use $`F\le\exp[-M(2p)^k/17]`$ to compare the logarithm of the number of available cores with their $`O(T^3)`$ report volume. Derive $`T=\Omega((\log L)^{1/3})`$, treating the no-fitting-core and linear-depth regimes separately. Keep the dependence of the constants on the fixed detector and target explicit; this finite estimate does not prove a full uniform detector/accuracy crossover.

**Earlier dependencies.** [M23](#m23).

**Story role.** Extracts the necessary depth with its actual quantifiers.

**Conceptual connection.** The logarithm comes from many spatial opportunities for a finite probability of locally losing the required information.

**Sources.** Preskill [§7.5][p751] supplies probability/fidelity background; bridge [from blind cores to a depth bound](PRESKILL_BRIDGE.md#from-blind-cores-to-a-depth-bound); [noisy readout](../science/noisy-readout.md).

### M25

**Coherent extraction with three qubits per cell**

**Central question.** How can a true syndrome control local operations without becoming free classical advice?

**Understanding target.** Starting from all-zero data, extract each star into one ancilla pointer with counted local gates and dephase it without reporting an outcome. Obtain the cq mixture over uniform even syndromes $`s`$, with data branch $`|\psi_s\rangle`$ and pointer string $`|s\rangle`$. Use $`Z(E)|\psi_s\rangle=|\psi_{s\oplus\partial E}\rangle`$. Count two designated edge qubits and one reusable pointer per cell; no true syndrome is handed noiselessly to the controller.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M07](#m07), [M09](#m09), [M12](#m12).

**Story role.** Begins the fixed-memory upper bound in the exact noisy-report interface.

**Conceptual connection.** An orthogonal quantum pointer can drive a nearby counted gate without opening a noiseless public measurement channel.

**Sources.** Preskill [§7.1][p71], [§7.10.1][p7101], and [§7.18.3][p7183]; bridge [physical compression before readout](PRESKILL_BRIDGE.md#physical-compression-before-readout); [noisy readout](../science/noisy-readout.md).

### M26

**A compression invariant for data and pointers**

**Central question.** What must remain true after every child-to-parent syndrome sweep?

**Understanding target.** For adjacent child and parent pointers with bits $`(a,b)`$, apply pointer CNOT, child-controlled $`Z`$ on their shared data edge, then reset the child pointer. Track the child's data defect to zero and both parent data/pointer bits to $`a\oplus b`$. Reset transfers discarded detail to an inaccessible environment. Iteration leaves only root defects, a uniform even root vector, and zero nonroot pointers. Explain why XORing noisy raw reports would violate this invariant.

**Earlier dependencies.** [M18](#m18), [M25](#m25).

**Story role.** Certifies compression of the actual remaining physical correction problem.

**Conceptual connection.** Discarded syndrome entropy is harmless only after the local physical defects it described have been removed.

**Sources.** Preskill [§7.2][p72] and [§7.18.3][p7183]; bridge [physical compression before readout](PRESKILL_BRIDGE.md#physical-compression-before-readout); [noisy-readout construction](../science/noisy-readout.md).

### M27

**Area times time protects one pointer**

**Central question.** How does one surviving root bit acquire a cubic number of reports at linear depth?

**Understanding target.** Reuse the freed pointers to fan out each orthogonal root value over its block in $`O(b)`$ local layers. Repeat QND readout $`t`$ times on each of $`A_j\ge b^2`$ copies, with one report per cell per round. Derive $`m_j=A_jt`$ and majority error $`e_{m_j}(p)\le e^{-\mathcal D(p)m_j}`$, where $`\mathcal D(p)=-\tfrac12\log[4p(1-p)]`$. The pointer values are correlated copies; their detector errors are independent. Fanout, readout time, and local density all count.

**Earlier dependencies.** [M13](#m13), [M25](#m25), [M26](#m26).

**Story role.** Connects reliable report extraction to the available two-dimensional block volume.

**Conceptual connection.** Classical basis information can be copied locally without cloning an arbitrary unknown state; spatial redundancy multiplies temporal observations.

**Sources.** Preskill [§7.6][p76] and [§7.18.3][p7183] supply coding/recovery background; bridge [protected pointer readout](PRESKILL_BRIDGE.md#protected-pointer-readout-and-the-delivered-state); [noisy readout](../science/noisy-readout.md), retaining the pointer-amplification attribution of [Readout Entanglement Limits](https://github.com/GoGoKo699/Readout-Entanglement-Limits).

### M28

**The corrected ensemble has an exact ground-space weight**

**Central question.** Which decoding errors still leave physical anyons after the final gates?

**Understanding target.** Decode $`B-1`$ roots and infer the last from even parity. Compute a correction edge set and physically apply its $`Z`$ gates in a counted layer using the permitted free public feedforward. A wrong decoded root leaves a nonzero residual syndrome even if several errors have even parity. Derive $`F_{\mathrm{phys}}=\prod_{j=1}^{B-1}[1-e_{A_jt}(p)]`$ by averaging every true syndrome, report error, and tie coin. Relate this exact ensemble formula to the four-block pointer example.

**Earlier dependencies.** [M07](#m07), [M11](#m11), [M20](#m20), [M27](#m27).

**Story role.** Closes the output requirement instead of stopping at an inferred frame.

**Conceptual connection.** Reliable reports matter because their decoded values select the actual corrected quantum state.

**Sources.** Preskill [§7.5.1][p751] and [§7.18.3][p7183]; bridge [protected pointer readout](PRESKILL_BRIDGE.md#protected-pointer-readout-and-the-delivered-state) and [small protected-readout example](PRESKILL_BRIDGE.md#small-protected-readout-example); [noisy readout](../science/noisy-readout.md).

### M29

**Attaining and matching cube-root logarithmic depth**

**Central question.** How do the fully counted upper and lower bounds meet?

**Understanding target.** Combine $`T\le16b+t-4`$ and $`1-F\le(B-1)e^{-\mathcal D(p)b^2t}`$. Set $`t=b`$ and choose $`b=O((\log L)^{1/3})`$ for fixed detector quality and fixed infidelity; use the exact one-block sweep when needed. Together with M24 obtain $`T_{\mathrm{det}}=\Theta_{p,f}((\log L)^{1/3})`$. Distinguish this fixed-parameter theorem from the separate finite constructive upper bound and from a claimed matched crossover. QND readout uses three qubits per cell; a destructive interface needs an additional reusable readout qubit.

**Earlier dependencies.** [M24](#m24), [M26](#m26), [M27](#m27), [M28](#m28).

**Story role.** Completes the new matched depth theorem.

**Conceptual connection.** The construction and converse meet through the same two-dimensional space-time volume, after both data correction and information access are accounted for.

**Sources.** Preskill [§7.18.3][p7183]; bridge [the fixed-detector preparation law](PRESKILL_BRIDGE.md#the-fixed-detector-preparation-law); [noisy readout](../science/noisy-readout.md).

### M30

**Narrative synthesis: two costs of physical preparation**

**Central question.** What changes, and what remains shared, between the two preparation laws?

**Understanding target.** Reconstruct the charged-bit frontier and the noisy-report depth law from their common local braiding and physical syndrome removal. Assign the retained-record/statistical and pointer-readout ingredients to Readout Entanglement Limits, and preserve Li–Lee–Yoshida attribution for the geometric obstruction. Explain why free public feedforward, noisy quantum gates/storage, unbounded report bandwidth, postselection, finite-speed communication, or replacing physical overlap by logical recoverability require different conclusions. Keep the original aggregate-throughput cube root distinct from the new cube root of a logarithm.

**Earlier dependencies.** [M20](#m20), [M22](#m22), [M23](#m23), [M28](#m28), [M29](#m29).

**Story role.** Completes the narrative phase with the contribution, ownership, and limits.

**Conceptual connection.** A common topological obstruction yields different optimal costs only after the classical interface and the delivered physical state have both been specified.

**Sources.** Preskill [§§7.18–7.20][p718]; bridge [what the chapter does and does not supply](PRESKILL_BRIDGE.md#what-the-chapter-does-and-does-not-supply); [communication bound](../science/communication-bound.md), [noisy readout](../science/noisy-readout.md), and [research attribution](../references/related-work.md).

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


[p76]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=24
[p752]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=23

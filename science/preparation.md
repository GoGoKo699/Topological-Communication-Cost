# Exact preparation with compressed classical communication

This construction prepares one specified pure toric-code ground state. It includes the physical Pauli corrections, the traffic returning from the controller, and the time required to distribute those instructions locally. The standard stabilizer-measurement and string-correction ingredients are established; the resource accounting here supplies the upper bound for the communication–depth tradeoff. For measurement-assisted topological preparation antecedents, see [Lu–Lessa–Kim–Hsieh](https://doi.org/10.1103/PRXQuantum.3.040337) and [Tantivasadakarn–Vishwanath–Verresen](https://doi.org/10.1103/PRXQuantum.4.020339).

## 1. Lattice, target and permitted operations

Let $L\geq2$ be an integer. Vertices are $(x,y)\in\mathbb Z_L^2$. The data qubits are the distinct oriented edge labels

$$
h(x,y): (x,y)\longleftrightarrow(x+1,y),\qquad
v(x,y): (x,y)\longleftrightarrow(x,y+1).
$$

There are $N=2L^2$ data qubits. An edge is owned by its tail vertex, which stores its data qubit. A vertex also has one measurement ancilla and a constant number of local classical registers. The edge labels remain distinct at $L=2$, where some pairs of vertices are joined by parallel physical edges. No $L=1$ claim is made.

The stabilizers are

$$
\begin{aligned}
A_{x,y}&=X_{h(x,y)}X_{h(x-1,y)}X_{v(x,y)}X_{v(x,y-1)},\\
B_{x,y}&=Z_{h(x,y)}Z_{v(x+1,y)}Z_{h(x,y+1)}Z_{v(x,y)}.
\end{aligned}
$$

Choose logical operators

$$
\overline Z_x=\prod_{x=0}^{L-1}Z_{h(x,0)},\qquad
\overline Z_y=\prod_{y=0}^{L-1}Z_{v(0,y)}.
$$

The output is the unique simultaneous $+1$ eigenstate of all stars, all plaquettes and these two logical $Z$ operators. There are $L^2-1$ independent stars, $L^2-1$ independent plaquettes and two independent logical constraints, totaling $N$.

All data start in $|0\rangle$. No initially shared quantum resource or shared random seed is needed. On-site classical processing is unrestricted. A local operation may act on two neighboring vertex sites, including their owned registers; its support has lattice diameter one. Parallel operations have disjoint site supports. Nonlocal messages use a fixed binary point-to-point schedule and are charged individually, including zero values. Sender identities, destinations and order are predetermined by the lattice and partition, so they carry no extra private-outcome information.

## 2. Statement with finite resource bounds

For every integer $1\leq\ell\leq L$, there is an exact deterministic preparation with

$$
D\leq12\ell+2,\qquad
C\leq2(B-1)\leq\frac{N}{\ell^2},\qquad
B=\left\lfloor\frac L\ell\right\rfloor^2.
$$

Here $D$ counts local operation layers and $C$ counts point-to-point delivered nonlocal bits. Nonlocal transfer and unrestricted controller computation do not themselves consume local layers in this circuit-resource model. If $B=1$, no nonlocal bit is used and the sharper depth bound is $D\leq2L+8$.

The constants are deliberately conservative. The protocol uses $O(1)$ quantum and classical working registers per ordinary vertex and $O(B)$ classical memory at the controller. The controller performs $O(B)$ elementary XOR operations; making this work free is an explicit on-site-processing convention, not a laboratory-time claim.

## 3. Star extraction in bounded depth

At each vertex, prepare an ancilla in $|+\rangle$, apply CNOTs from it to the four incident data qubits, and measure it in the $X$ basis. The ancilla outcome $(-1)^{s_{x,y}}$ measures $A_{x,y}$.

Separate the four CNOT directions into east, west, north and south families. East and north targets are owned by the control vertex and each family is one on-site layer. In the west family, color the horizontal torus edges with at most three colors so each color is a matching; do the same with vertical edges for the south family. A concrete cycle coloring assigns alternating colors to the first $L-1$ edges and, for odd $L$, a third color to the wrap edge. For even $L$, ordinary alternating colors suffice. Thus at most eight CNOT layers, one ancilla-preparation layer and one local $X$-measurement layer suffice:

$$
D_{\rm star}\leq10.
$$

The common ancilla controls and commuting target-$X$ factors give the joint projective measurement of the commuting stars. The resulting measurement projectors commute with the data plaquettes and logical $Z$ operators; individual intermediate CNOT gates need not preserve those eigenspaces. The product of all stars is identity, so

$$
\bigoplus_{x,y}s_{x,y}=0.
$$

Every even syndrome occurs with probability $2^{-(L^2-1)}$. To see this, products of distinct independent stars act on $|0\rangle$ as distinct computational-basis strings, so every nonidentity product has zero expectation. Expanding the commuting projectors gives the uniform distribution on the even subspace. Conditional on the syndrome, the data state is pure and still has all plaquettes and both logical $Z$ values equal to $+1$.

## 4. Balanced partitions for arbitrary $L$

Set $k=\lfloor L/\ell\rfloor\geq1$ and write

$$
L=ka+r,\qquad 0\leq r<k.
$$

Partition each coordinate axis into $k$ consecutive intervals, the first $r$ of length $a+1$ and the remaining intervals of length $a$. Let their lengths be $w_i$ horizontally and $h_j$ vertically, with starts $x_i$ and $y_j$. The blocks are

$$
\mathcal B_{i,j}=[x_i,x_i+w_i)\times[y_j,y_j+h_j),\qquad
0\leq i,j<k.
$$

Choose root $r_{i,j}=(x_i,y_j)$. The definition of $k$ implies

$$
\ell\leq w_i,h_j\leq2\ell-1.
$$

Indeed $L\geq k\ell$ and $L\leq(k+1)\ell-1$, so the largest interval is at most $\ell+\lceil(\ell-1)/k\rceil\leq2\ell-1$. This includes $k=1$, where the single side is $L<2\ell$.

Nothing is discarded at an incomplete boundary block. These are exact partitions of every vertex, and all lengths and routing schedules are known before any outcome is generated.

## 5. Local removal of all nonroot defects

Store the current star syndrome in one classical bit $p_{x,y}$ at each vertex. If adjacent vertices $u$ and $v$ share edge $e$, applying $Z_e$ toggles precisely their two star eigenvalues.

In each block, first sweep every row toward its leftmost vertex. At global sweep index $a=w_{\max}-1,w_{\max}-2,\ldots,1$, a block with $a<w_i$ performs, on each of its rows, the following fixed-support operation from child $u=(x_i+a,y)$ to parent $v=(x_i+a-1,y)$:

1. Transfer the bit $b=p_u$ to the parent through the neighboring link.
2. Apply $Z_{h(x_i+a-1,y)}^b$.
3. Set $p_v\leftarrow p_v\oplus b$ and $p_u\leftarrow0$.

This is one allowed bounded-range classical–quantum channel on the neighboring sites. Its support and its execution do not depend on $b$; a zero bit still executes the scheduled operation. At each sweep index, all pairs are disjoint: they lie within disjoint blocks and in distinct rows.

Then sweep the leftmost column of each block downward toward its root, using the analogous operation at indices $b=h_{\max}-1,\ldots,1$. Again all active pairs are disjoint. These two sweeps take

$$
D_{\rm sweep}=w_{\max}+h_{\max}-2
$$

local layers. They use exactly $L^2-B$ local tree-edge operations. Every nonroot syndrome is zero and each root contains

$$
p_{i,j}=\bigoplus_{(x,y)\in\mathcal B_{i,j}}s_{x,y}.
$$

The root vector has even total parity. It is uniform over the even $B$-bit subspace, although correctness and the resource bounds do not require that distributional fact.

## 6. Fixed nonlocal collection and return traffic

Place the controller at root $r_{0,0}$. Every other root sends its parity bit to it, in fixed row-major order. This costs exactly $B-1$ delivered bits, even when every bit is zero. The controller already has its own root parity.

Use the following nonwrapping comb spanning tree of the coarse $k\times k$ block grid:

- A block $(i,j)$ with $i>0$ has parent $(i-1,j)$.
- A block $(0,j)$ with $j>0$ has parent $(0,j-1)$.

For the coarse edge leading from a noncontroller block $b$ to its parent, set

$$
z_b=\bigoplus_{b'\text{ in the subtree rooted at }b}p_{b'}.
$$

The incidence boundary of these selected edges is exactly the root-syndrome vector. At a nonroot block, its incoming coefficient XOR its child coefficients equals its own parity; at the controller, the same identity follows from total even parity.

The **parent** block owns the physical correction for each of its child edges. The controller sends $z_b$ to that parent, unless the parent is the controller itself. Each block has at most two children and therefore receives at most two instruction bits. Every coefficient is sent in the predetermined schedule, including zero coefficients. With

$$
d_0=\mathbf1_{k>1}+\mathbf1_{k>1},
$$

the exact delivered count of this particular implementation is

$$
C=(B-1)+(B-1-d_0)=2(B-1)-d_0.
$$

For $B=1$, both terms are zero. For $k\geq2$, $d_0=2$. No free broadcast, remote quantum correction, uncharged outcome-dependent address, or omitted return phase is used. The exact coefficient is a construction count, not a claim of optimality.

## 7. Local execution of the coarse correction

A horizontal coarse edge from $(i,j)$ to $(i+1,j)$ is represented by the physical path

$$
h(x_i,y_j),h(x_i+1,y_j),\ldots,h(x_{i+1}-1,y_j),
$$

of length $w_i$. A vertical spine edge from $(0,j)$ to $(0,j+1)$ is the path of $h_j$ vertical physical edges at $x=0$. Each path has precisely the prescribed pair of roots as boundary.

The parent root propagates its coefficient along the path, applying the corresponding $Z$ to each traversed edge. The schedule also propagates zero coefficients. The receiving endpoint discards the arriving token; it does not forward it into another coarse segment. A coarse root has separate registers for its own outgoing instruction and any incoming terminal token, so the case of a one-edge segment creates no overwrite or uncharged memory assumption.

Run horizontal paths first, then vertical spine paths. In each routing round, split active horizontal edges by the parity of their tail $x$ coordinate, and active vertical edges by the parity of their tail $y$ coordinate. These are matchings because the paths do not wrap. Consequently all operations in a layer have disjoint site supports, even for $\ell=1$ and unequal block sizes. The conservative bound is

$$
D_{\rm route}\leq2w_{\max}+2h_{\max}.
$$

The horizontal and vertical phases use distinct physical edges. Shared endpoints and crossings of their supports are handled by the separate phases. Local sweep corrections may overlap these paths; their net action is the XOR of their edge sets, as required for Pauli $Z$ corrections.

## 8. Correctness and resources

Let $E_{\rm sweep}$ be the binary set of local sweep edges and $E_{\rm coarse}$ the binary union of selected coarse paths. Write $\partial E$ for the vertex incidence boundary of a physical edge set. The two stages give

$$
\partial E_{\rm sweep}=s\oplus p_{\rm roots},\qquad
\partial E_{\rm coarse}=p_{\rm roots}.
$$

Thus the implemented correction $Z(E_{\rm sweep}\oplus E_{\rm coarse})$ has boundary $s$ and makes every star $+1$. Every correction is of $Z$ type, so it preserves every plaquette and both logical $Z$ labels. Since the measured branch was pure, the corrected output is the unique specified pure ground state for every physically possible syndrome. Discarding the records therefore leaves that same state unconditionally.

Combining the schedules,

$$
\begin{aligned}
D&\leq10+(w_{\max}+h_{\max}-2)+2(w_{\max}+h_{\max})\\
 &\leq12\ell+2,\\
C&\leq2(B-1)\leq2(L/\ell)^2= N/\ell^2.
\end{aligned}
$$

When $k=1$, the local sweep already removes all defects because its root parity is zero. There is no coarse routing or nonlocal communication, and $D\leq10+2L-2=2L+8$.

## 9. Verification and its limits

[The construction verifier](../tools/verify_construction.py) uses only the Python standard library. It enumerates all even syndromes on small tori, samples fixed-seed larger cases with divisible and nondivisible blocks, independently recomputes physical edge boundaries, checks all local layers for disjoint support and range, checks exact message counts and zero-message schedules, and verifies the CSS stabilizer ranks and logical constraints. For the small cases it also checks exact computational-basis amplitudes of the projected star state after the actual correction.

[The verification guide](../verification/README.md) states the command and the scope of [the saved results](../verification/construction-results.json). These are finite implementation checks. The arbitrary-$L$ construction follows from the preceding argument; neither these checks nor this upper-bound construction establish the asymptotic communication lower bound.

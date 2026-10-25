[Notes](../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 196](../index/algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md)

# 196 — A counterexample to Kaplansky's zero-divisor conjecture

[Index page](../index/algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md)

## Original CONTENTS.md summary

 carries the family entry:

> Constructs a finitely presented torsion-free group $G$ whose group algebra $\mathbb F_2[G]$ has nonzero zero divisors, disproving Kaplansky's zero-divisor conjecture. The group has a finite two-dimensional classifying space. [S1:473]

The entry names the manuscript "A Torsion-Free Group Algebra with Zero Divisors [S1:473]" .

The README title is `A Torsion-Free Group Algebra with Zero Divisors` [S2:1].

The README dates it 2026-09-23 [S2:5].

## Undergraduate summary

Kaplansky's zero-divisor conjecture says the group algebra of a torsion-free group over a field has no zero divisors. Finite-order elements do give zero divisors, so torsion-freeness is the natural condition to remove.

The manuscript's abstract states the counterexample. says: "We disprove Kaplansky's zero-divisor conjecture by constructing a finitely presented torsion-free group \(G\) for which \(\mathbb F_2[G]\) has nonzero zero divisors. The group admits a finite two-dimensional classifying space. [S3:45]"

The theorem names the group and the two elements. gives it: "There exist a finitely presented torsion-free group \(G\) and nonzero elements \(\alpha,\beta\in\mathbb F_2[G]\) such that \(\alpha\beta=0\). Moreover, \(G\) admits a finite two-dimensional classifying space. [S3:53–55]"

The construction pairs two graphs whose vertex label sets intersect in odd size, so the product's contributions cancel in characteristic two, and then proves the group is torsion-free by showing the resulting complex is aspherical.

## Graduate summary

The conjecture is stated. [S3:50–50] states it: "Kaplansky's zero-divisor conjecture asserts that \(K[G]\) has no nonzero zero divisors whenever \(K\) is a field and \(G\) is torsion-free. Here \(K[G]\) is the algebra of finite formal sums of elements of \(G\), with multiplication extended bilinearly from the group law. We prove the following negative resolution. [S3:50]"

The elementary obstruction is recorded. records it: "Finite-order elements give elementary zero divisors: if \(g\) has order \(m>1\), then \((1-g)(1+g+\cdots+g^m-1)=0\). The conjecture asks whether removing this obstruction suffices. [S3:60]"

The unique-product property is defined. defines it: "A group has the _unique-product property_ if, for every pair of finite nonempty subsets \(P,Q\), some element of \(PQ\) has exactly one expression \(pq\) with \(p\in P\), \(q\in Q\). Applying this property to the supports of two nonzero group-algebra elements gives a nonzero product coefficient. [S3:64]"

The gap is stated. states it: "Failure of unique product alone does not produce a zero divisor: over \(\mathbb F_2\), the relevant representation counts must be even, not merely greater than one. [S3:64]"

The construction is stated. states it: "We use two finite graphs \(\Gamma_A,\Gamma_B\) immersed into one rose \(F\), a graph with one vertex and one edge for each generator. Every edge is read with a signed label, reversed when its orientation is reversed. Choose roots \(x_A,x_B\), and let \(A',B'\) be the full vertex sets of their connected components. Attach an abstract cone on each graph component along its labelled map to \(F\), obtaining a complex \(X\), and put \(G=\pi_1(X)\). Coning kills the labels of all closed graph paths. Thus a path from \(x_A\) to \(x\in A'\) has a well-defined label \(g_x\in G\), independent of the chosen path; define \(h_y\) from \(x_B\) to \(y\in B'\) in the same way. [S3:72]"

The cancellation is stated. [S3:78–79] states it: "Let \(S_x\) and \(S_y\) be the outgoing signed-label sets. We prescribe them so that \(|S_x\cap S_y|\) is odd for every pair. Form a graph on \(A'\times B'\) by simultaneous steps of a common label \(t\). Along each step the product is unchanged, since [S3:78]"

The parity count is stated. states it: "Every vertex of this finite graph has odd degree \(|S_x\cap S_y|\). Hence each connected component has even cardinality, by the degree-sum formula. Its vertices all contribute the same group element to \(\alpha\beta\), so their contributions cancel in characteristic two. [S3:82]"

The two safeguards are stated. states them: "This simple cancellation leaves two substantial safeguards. First, both factors must survive in the quotient: we prove that a path from either prescribed root to any different vertex in its component has nontrivial label. The root is then the only contributor to the identity coefficient in each factor, so both are nonzero. We do not need to distinguish labels of two non-root vertices. Second, the quotient group must be torsion-free: we prove that \(X\) is aspherical, making it a finite two-dimensional classifying space and ruling out torsion. Both safeguards will follow by excluding certain planar configurations of paired path occurrences. [S3:84]"

The probabilistic step is stated. states it: "The outgoing-label types use lines in a finite projective plane together with three extra letters. Their cross-intersections force parity, while their turn frequencies satisfy an exponentially decaying squared-word estimate. We convert this estimate into an exclusion of bounded systems of almost completely paired paths. Paths may traverse the same edge repeatedly; multiplicity stages keep track of those repeated uses, while nearly aligned blocks control comparisons of arbitrary subpaths. Multiplying numerical expectation bounds selects one stage with a small expected count, without asserting independence between stages. [S3:88]"

The planar step is stated. states it: "The remaining obstacle is that a sphere can involve arbitrarily many paths of arbitrarily large total length. Lipton–Tarjan planar separation reduces each such configuration to a bounded system. Long boundaries are first split and closed at a controlled cost, and planar gap counting bounds the number of comparison intervals after localization. The proportion of unpaired positions allowed by the probabilistic estimate is fixed before the bounds on the number and lengths of paths. This order permits the same bounded class to detect every large spherical arrangement, rather than a union bound over all arrangement sizes. [S3:90]"

The antecedents are recorded. records them: "Graphical small cancellation provides important antecedents for this strategy. [S3:92]"

and by "Distinguishing genuinely different graph lifts from coincident lifts is central to these arguments and to Bereznyuk's spherical-diagram approach [S3:92]"

and by "Here the prescribed vertex types and repeated traversals require a separate probability estimate, and the needed topology is proved directly by cone-picture surgery. We do not invoke a small-cancellation or \(\mathrmCAT(0)\) criterion for these graphs. [S3:92]"

The conventions are recorded. records them: "All graphs are finite unless stated otherwise. A graph may initially have loops or parallel edges; both are counted in its girth. A signed alphabet \(T\) has a fixed-point-free involution \(t\mapsto\bar t\), with \(\bar t\) denoting the inverse letter. The rose \(F\) has one vertex and one unoriented edge for each inverse pair. A labelled graph maps immersively to \(F\) when each outgoing label occurs at most once at each vertex. An _immersed path_ is an edge path with no immediate reversal; a closed path is _cyclically immersed_ if this also holds at its last/first junction. Length always counts edge traversals, including repetitions. [S3:96]"

The types section opens with the design. opens it: "We construct the two immersed graphs so that their outgoing-label sets have odd cross-intersections, the condition needed for cancellation. The same vertex types also provide a squared-word decay estimate. Conditioning the matchings on large girth will preserve enough control to prove a diameter bound and, in  , exclude the path configurations that could defeat the geometric safeguards. [S4:3–8]"

The entropy section opens. opens it: "All probabilities in this section refer to the distribution conditioned on \(\operatornamegirth(\Gamma)\ge L\).  We retain the predetermined vertices \(x_A\) and \(x_B\). The possible rooted interval will accommodate a null-homotopy of a root-to-vertex path in  . [S5:4–7]"

The bounded-pattern estimate is given. gives it: "There is a constant \(\varepsilon>0\), depending only on the fixed types and turn weights, with the following property.  For every fixed positive integer \(K\), fixed real \(C\ge1\), and fixed nonnegative integer \(I\), the conditional probability tends to zero that there exists a system as above having at most \(K\) paths, total length \(H\) with [S5:30–34]"

The planar section opens. opens it: "Proposition   controls systems of bounded size. We now show that any spherical arrangement of the kind needed for the topological argument contains such a system.  The number of disks in the arrangement is unrestricted.  Throughout this section, probability is taken in the distribution conditioned on girth at least $L$. [S6:4–8]"

The arrangement exclusion is given. gives it: "With probability $1-o(1)$, $\Gamma$ admits no reduced spherical arrangement.  In particular, for all sufficiently large admissible $n$ there exist graphs of the prescribed types, with girth at least $L$ and the diameter bound of Lemma  , admitting no such arrangement. [S6:254–258]"

The topology section opens. opens it: "Fix graphs supplied by  . Attach to the rose \(F\), for each connected component \(\Lambda\) of \(\Gamma\), its abstract cone \(K_\Lambda\) along the labelled map \(\Lambda\to F\). Denote the resulting finite two-dimensional CW complex by \(X\), and put \(G=\pi_1(X)\), based at the rose vertex. In particular, labels of all closed walks in \(\Gamma\) are trivial in \(G\). [S7:3]"

The asphericity conclusion is given. gives it: "The complex \(X\) satisfies \(\pi_2(X)=0\). Moreover, if a path in \(\Gamma\) starts at \(x_A\) or \(x_B\) and ends at a different vertex, its label is nontrivial in \(G\). [S7:6]"

The method is stated. states it: "We prove the two conclusions together, using minimal surface pictures. The proof keeps track of the actual boundary lifts in \(\Gamma\). Removing overlaps with coincident graph lifts is also central to the graphical-diagram arguments of Gruber and Bereznyuk [S7:9]"

and by "Their hypotheses are not imported here: we give the cone-picture reduction needed for   directly, without a graphical small-cancellation condition. [S7:9]"

The factors section opens. opens it: "Use the graphs of   and the complex \(X\) constructed in  . It is finite and two-dimensional. By  , it is a classifying space for the torsion-free group \(G=\pi_1(X)\), which is finitely presented. [S8:4]"

The factors' nonvanishing is stated. states it: "Both sums are finite. The root contributes the identity to each. By  , no other vertex contributes identity, so its coefficient is one in each factor. Thus \(\alpha\ne0\) and \(\beta\ne0\). No assertion about equality between two non-root labels is needed. [S8:14]"

The cancellation step is stated. states it: "The reverse step has label \(\bar t\). Since full components are used, the degree at \((x,y)\) is the entire number \(|S_x\cap S_y|\), which is odd by  . The girth condition excludes loops for the chosen large \(n\); parallel edges would not affect the degree-sum argument. [S8:26]"

## Section skeleton

- `build/paper.tex` [S3]
- `build/sections/types.tex` [S4:3–8]
- `build/sections/entropy.tex` [S5]
- `build/sections/planar.tex` [S6]
- `build/sections/topology.tex` [S7]
- `build/sections/factors.tex` [S8]
- `build/figures/band-surgery.tex` [S9]
- `build/figures/block-alignment.tex` [S10]
- `build/references/references.bib` [S11]

## Comparison with the formalized statement

The scope note states the formalized claim. says: "Kaplansky's zero-divisor conjecture asserts that the group algebra of a torsion-free group over a field has no zero divisors. The formalized result constructs a finitely presented torsion-free group $G$ and nonzero elements $\alpha,\beta\in\mathbb F_2[G]$ with $\alpha\beta=0$, giving a counterexample. [S12:9]"

The scope note states the second formalized fact. says: "The same group admits a finite two-dimensional classifying space $K(G,1)$. [S12:11]"

The declaration is `OAI.TorsionFreeZeroDivisors.main` at `lean/OAI/Algebra/GroupRing/Main.lean:13` [S13:13]. The comparator stub carries `sorry` at `lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean:36` [S14:36].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../overview.tex) | 859 | Family entry, line 473 |
| S2 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/README.md`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/README.md) | 18 | Title, date |
| S3 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex) | 108 | Abstract, theorem, introduction, proof structure |
| S4 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/types.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/types.tex) | 170 | Vertex types |
| S5 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/entropy.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/entropy.tex) | 548 | Entropy and bounded patterns |
| S6 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/planar.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/planar.tex) | 423 | Planar separation |
| S7 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/topology.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/topology.tex) | 113 | Topology |
| S8 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/factors.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/factors.tex) | 34 | Factors |
| S9 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/figures/band-surgery.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/figures/band-surgery.tex) | 31 | Figure source |
| S10 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/figures/block-alignment.tex`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/figures/block-alignment.tex) | 26 | Figure source |
| S11 | [`preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/references/references.bib`](../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/references/references.bib) | 261 | Bibliography entries |
| S12 | [`lean/docs/196.md`](../../lean/docs/196.md) | 17 | Scope |
| S13 | [`lean/OAI/Algebra/GroupRing/Main.lean`](../../lean/OAI/Algebra/GroupRing/Main.lean) | 24 | Declaration |
| S14 | [`lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean`](../../lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean) | 40 | Comparator stub |

## Bibliography

- Bereznyuk, Vadim, Asphericity of groups defined by graphs (2019)
- Brown, Kenneth S., Cohomology of Groups (1982)
- Sam P. Fisher, Pablo Sánchez-Peralta, Division rings for group algebras of virtually compact special groups and $3$-manifold groups (2026)
- Gardam, Giles, A counterexample to the unit conjecture for group rings (2021)
- Giles Gardam, Non-trivial units of complex group rings (2024)
- Garg, Manisha, Mineyev, Igor, On zero-divisors and units in group rings of torsion-free CAT(0) groups (2025)
- Gromov, M., Random walk in random groups (2003)
- Gruber, Dominik, Groups with graphical $C(6)$ and $C(7)$ small cancellation presentations (2015)
- Hatcher, Allen, Algebraic Topology (2002)
- Graham Higman, Units in group rings (1940)
- Graham Higman, The units of group-rings (1940)
- Irving Kaplansky, Problems in the theory of rings (1957)
- P. H. Kropholler, P. A. Linnell, J. A. Moody, Applications of a new $K$-theoretic theorem to soluble group rings (1988)
- Lipton, Richard J., Tarjan, Robert Endre, A separator theorem for planar graphs (1979)
- Ibrahim Mian, Shayaan Siddique, A Machine-Checked Proof that Gardam's $\widetilde A_2$ Lattice Does Not Have Unique Products (2026)
- Igor Mineyev, The Topology and Geometry of Units and Zero-Divisors: Origami (2024)
- Ollivier, Yann, On a small cancellation theorem of Gromov (2006)
- Ollivier, Yann, A January 2005 invitation to random groups (2005)
- Rips, E., Segev, Y. S., Torsion-free group without unique product property (1987)
- Robert Sandling, Graham Higman's thesis ``Units in group rings'' (1981)
- Henry Shin, A global girth obstruction for Garg–Mineyev taiko product structures (2026)
- Markus Steenbock, Rips–Segev torsion-free groups without the unique product property (2015)

[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 305](../index/topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md)

# 305 — Counterexamples to disk embedding and Wall's manifold conjecture

[Index page](../index/topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:7528] and the catalog abstract [S2:704] state
the family's claim: the unrestricted four-dimensional disk-embedding
conjecture fails — framed algebraic dual spheres do not suffice to
obtain disjoint locally flat spanning disks, so the free group $F_2$
is not "good" in the sense of Freedman--Quinn — and separately a
finitely presented integral Poincaré duality group of dimension four
has a finite classifying space but no realization as the fundamental
group of a closed aspherical topological four-manifold, disproving
Wall's conjecture. The boundary-only obstruction manuscript
 "We disprove the four-dimensional disc embedding conjecture without a
fundamental-group hypothesis, even when no homotopy classes or output framings
are prescribed. We construct a compact oriented smooth four-manifold containing
finitely many disc maps with framed algebraic dual spheres whose boundary
circles bound no disjoint locally flat discs. Consequently, the free group on
two generators is not good in the sense of Freedman–Quinn, and neither is any
group containing it as a subgroup. [S3:47–55]" The marked tensor manuscript "We disprove the unrestricted four-dimensional disk-embedding conjecture.
We construct immersed disks in a compact oriented smooth four-manifold with
framed algebraic dual spheres satisfying the usual equivariant intersection
and reduced self-intersection conditions, but with no pairwise disjoint locally
flat replacements that preserve the boundary maps and induced normal framings.
The obstruction holds even when the replacement disks' relative homotopy classes
are not prescribed. [S5:1–9]"
The PD4 manuscript "We construct a finitely presented integral Poincaré duality group of
dimension four that has a finite classifying space but is not the fundamental
group of any closed aspherical topological four-manifold. This gives a negative
answer to Wall's manifold-realization question in dimension four. [S6:43–48]"

## Undergraduate summary

The disk-embedding problem sits at the heart of four-dimensional
topology, where smooth structure is replaced by a topological one and
the usual tools weaken. Given a collection of immersed disks in a
four-manifold, together with "dual" spheres that intersect each disk in
the expected algebraic way (a disk $f_i$ meets its dual $g_i$ once and
every other disk not at all, and the spheres have vanishing
self-intersection), one wants to find genuine, embedded, pairwise
disjoint disks spanning the same boundary circles, preserving the
normal framings. The disk-embedding conjecture predicted that this
should always be possible under the algebraic conditions. The
manuscripts of this family show it is not: the first two construct
four-manifolds in which the algebraic data — the intersection and
self-intersection numbers — are satisfied, yet no such disjoint locally
flat disks exist 

> **theorem**
There exist a compact connected oriented smooth four-manifold $M$ with nonempty boundary, an integer $k\geq1$, proper generically immersed discs
\[
 f_i\colon(D^2,S^1)\longrightarrow(M,\partial M),\qquad 1\leq i\leq k,
\]
whose boundary restrictions form an embedding of $\coprod_iS^1$, and framed sphere maps $g_i\colon S^2\to M$ such that
$$\label{eq:input-invariants}
 \lambda(f_i,g_j)=\delta_{ij}\,1,\qquad
 \lambda(g_i,g_j)=0,\qquad
 \widetilde\mu(g_i)=0
 \quad(1\leq i,j\leq k),$$
but the given boundary circles do not bound pairwise disjoint proper locally flat embedded discs in $M$. Each $g_i$ can be chosen to be a smooth embedded sphere; different $g_i$ are allowed to intersect. [S4:40–53]

The third manuscript attacks a related long-standing question in
dimension four, Wall's conjecture, which asked whether every
finitely presented four-dimensional Poincaré duality group with a
finite classifying space occurs as the fundamental group of a closed
aspherical topological four-manifold. A Poincaré duality group is one
whose group cohomology mimics that of a closed manifold; an aspherical
space is one whose higher homotopy groups vanish, so its fundamental
group captures all of its topology. The group the third manuscript
builds has the right algebraic shape — a finite four-dimensional
aspherical Poincaré complex with the correct cohomology — but cannot be
the fundamental group of any such manifold 

> **theorem**
There is a finitely presented group $G$ with a finite, oriented,
four-dimensional aspherical Poincaré complex $Q$ such that
\[
 H^i(G;\mathbb Z G)=0\quad(i\ne4),\qquad H^4(G;\mathbb Z G)\cong\mathbb Z
\]
with trivial right $G$-action on the last group, but no closed aspherical
topological four-manifold has fundamental group $G$.
In particular the trivial left $\mathbb Z G$-module $\mathbb Z$ has a finite resolution
by finitely generated free modules. [S6:94–104]

## Graduate summary

**The two disk-embedding obstructions.** The boundary-only manuscript
proves that the failure can occur even without prescribing the
homotopy classes of the prospective replacement disks: the obstruction
lives entirely in the boundary configuration. Its input disks have
disjoint embedded boundary circles and framed dual spheres with the
diagonal intersection and vanishing self-intersection invariants, yet
the boundary circles bound no disjoint locally flat discs, and changing
the relative homotopy classes of the would-be disks cannot evade this
[S4:55–59]. The marked tensor manuscript strengthens the statement by
showing that even a *marking* — based curves and their paths fixing the
construction — does not help: the obstruction is genuinely geometric,
so the marked tensor algebra built from the edge germs and vertices
detects the absence of a disjoint replacement [S5:93–100].

**The free-group consequence.** A group is "good" in the sense of
Freedman--Quinn when the disk-embedding theorem lets one perform
surgery to realize its classifying space as a topological manifold.
Because the boundary-only construction places the obstruction where no
fundamental-group hypothesis helps, the free group on two generators is
not good, and neither is any group containing it as a subgroup
[S4:137–201].

**The Wall obstruction.** The PD4 manuscript builds a finitely
presented group $G$ from chamber, reflection, and stable pieces, with a
control argument that forces the vanishing Wall self-intersection
obstructions. The group admits a finite, oriented, four-dimensional
aspherical Poincaré complex $Q$ with $H^i(G;\mathbb Z G)=0$ for $i\ne4$ and
$H^4(G;\mathbb Z G)\cong\mathbb Z$, so the trivial $\mathbb Z$-module has a finite free
resolution — the algebraic signature of a closed aspherical
four-manifold — yet no closed aspherical topological four-manifold has
fundamental group $G$ [S6:114–217].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

The disk-embedding conjecture is a central ingredient of the
 Freedman--Quinn program for four-dimensional manifolds: under the
right hypotheses it lets one replace immersed disks by embedded ones
and carry out topological surgery. Earlier obstruction approaches
localized the obstruction in the fundamental group or in prescribed
homotopy classes, and the surgery-theoretic antecedents supply the
algebraic input invariants. The present construction moves the
obstruction out of both, showing the algebraic conditions are not
sufficient on their own [S4:137–201]. Wall's conjecture sits in the
same era of four-dimensional structure theory; the question of when a
Poincaré duality group with a finite classifying space is realized by
an aspherical manifold was open, and the algebraic side — Poincaré
duality groups, finite free resolutions of the trivial module, and the
vanishing of Wall self-intersection obstructions — had been developed
as a separate line [S6:114–160].

## Consequences

**The unrestricted four-dimensional disk-embedding conjecture is
false.** There are immersed disks in a compact oriented smooth
four-manifold with framed algebraic dual spheres satisfying the
intersection and self-intersection conditions, but with no pairwise
disjoint locally flat replacements preserving the boundary maps and
framings [S4:40–53] [S5:75–91].

**The free group $F_2$ is not good.** In the sense of Freedman--Quinn,
the free group on two generators — and any group containing it as a
subgroup — cannot be realized as the fundamental group of a
four-manifold by the surgery program [S3:47–55].

**Wall's manifold-realization conjecture is false in dimension four.**
A finitely presented integral Poincaré duality group of dimension four
with a finite classifying space need not be the fundamental group of a
closed aspherical topological four-manifold [S6:94–104].

## Section skeleton

**Boundary-only obstruction manuscript** [S3:47–55], 7 sections under
`build/sections/`: introduction [S4:40–53], geometry, deformation,
connections, algebra, frobenius, conclusion. Plus three figures under
`build/figures/`. Its root is `build/paper.tex`, with a
`references.bib` bibliography [S7].

**Marked tensor obstruction manuscript** [S5], 8 sections under
`build/sections/`: 00-introduction, 01-geometry, 02-tensor,
03-edge-germs, 04-algebraicity, 04a-formal-comparison, 05-vertices,
06-conclusion. Plus two figures under `build/figures/` and one appendix
(`build/appendices/formal-trace-comparison`). Its root is
`build/paper.tex`, with a `references.bib` bibliography [S8].

**PD4-without-aspherical-manifold manuscript** [S6], 4 sections under
`build/sections/`: chamber, reflection, stable, control. Its root is
`build/paper.tex`, with a `references.tex` bibliography [S9].

None of the three manuscripts ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships three LaTeX
manuscripts — 7 `.tex` sections plus a root and three figures in the
boundary-only `build/`, 8 plus a root, a preamble, two figures, and an
appendix in the marked-tensor `build/`, and 4 sections plus a root and
a bibliography in the PD4 `build/` — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 305 at line 7528. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 704. |
| S3 | [`preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/paper.tex`](../../../preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/paper.tex) | 69 | Boundary-only obstruction manuscript: title and abstract. |
| S4 | [`preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/sections/introduction.tex`](../../../preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/sections/introduction.tex) | 303 | Boundary-only obstruction introduction: the main theorem, the free-group problem, the surgery antecedents, and the obstruction. |
| S5 | [`preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/sections/00-introduction.tex) | 275 | Marked tensor obstruction manuscript: abstract, the main theorem, the idea of the proof, and the geometric and algebraic antecedents. |
| S6 | [`preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/build/paper.tex`](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/build/paper.tex) | 242 | PD4-without-aspherical-manifold manuscript: abstract, the main theorem, the source of the obstruction, and the proof architecture. |
| S7 | [`preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/references.bib`](../../../preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/references.bib) | 244 | Boundary-only obstruction bibliography. |
| S8 | [`preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/references.bib`](../../../preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/build/references.bib) | 190 | Marked tensor obstruction bibliography. |
| S9 | [`preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/build/references.tex`](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/build/references.tex) | 161 | PD4-without-aspherical-manifold bibliography. |

## Bibliography

- Artin, Michael, Algebraic approximation of structures over complete local rings (1969)
- The Stacks Project Authors, The Stacks Project (2026)
- Brav, Christopher, Bussi, Vittoria, Joyce, Dominic, A Darboux theorem for derived schemes with shifted symplectic structure (2019)
- Calaque, Damien, Lagrangian structures on mapping stacks and semi-classical TFTs (2015)
- Chern, Shiing-Shen, Simons, James, Characteristic forms and geometric invariants (1974)
- Chern, Shiing-Shen, Simons, James, Characteristic forms and geometric invariants (1974)
- Michael W. Davis, _The Geometry and Topology of Coxeter Groups_, London Mathematical Society Monographs Series, vol. 32, Princeton University Press, Princeton, NJ, 2008. doi:10.1515/9781400845941.
- Michael W. Davis, _Groups generated by reflections and aspherical manifolds not covered by Euclidean space_, Annals of Mathematics (2) **117** (1983), no. 2, 293–324. doi:10.2307/2007079.
- Michael W. Davis, _The cohomology of a Coxeter group with group ring coefficients_, Duke Mathematical Journal **91** (1998), no. 2, 297–314. doi:10.1215/S0012-7094-98-09113-X.
- Michael W. Davis, _Poincaré duality groups_, in _Surveys on Surgery Theory_, Vol. 1, Sylvain Cappell, Andrew Ranicki, and Jonathan Rosenberg, eds., Annals of Mathematics Studies, vol. 145, Princeton University Press, Princeton, NJ, 2000, 167–193. Author's version.
- Dupont, Johan L., Simplicial de Rham cohomology and characteristic classes of flat bundles (1976)
- Jim Fowler, _Finiteness properties for some rational Poincaré duality groups_, Illinois Journal of Mathematics **56** (2012), no. 2, 281–299. doi:10.1215/ijm/1385129948. The cited theorem locator refers to arXiv:1204.4667v1.
- Freedman, Michael H., The topology of four-dimensional manifolds (1982)
- Freedman, Michael H., Quinn, Frank, Topology of 4-manifolds (1990)
- Freedman, Michael H., Teichner, Peter, 4-manifold topology. I. Subexponential groups (1995)
- Freedman, Michael H., Are the Borromean rings {$A$–$B$}-slice? (1986)
- Freedman, Michael H., Lin, Xiao-Song, On the $(A,B)$-slice problem (1989)
- Freedman, Michael H., Krushkal, Vyacheslav S., Engel relations in $4$-manifold topology (2016)
- Freedman, Michael, Krushkal, Vyacheslav, Engel relations in 4-manifold topology (2016)
- Freedman, Michael, Krushkal, Vyacheslav, Engel groups and universal surgery models (2020)
- Freedman, Michael H., Quinn, Frank, Topology of 4-Manifolds (1990)
- Freedman, Michael H., The topology of four-dimensional manifolds (1982)
- Freedman, Michael H., Teichner, Peter, 4-manifold topology. I. Subexponential groups (1995)
- Getzler, Ezra, Lie theory for nilpotent $L_\infty$-algebras (2009)
- Goldman, William M., Millson, John J., The deformation theory of representations of fundamental groups of compact Kähler manifolds (1988)
- Goldman, William M., Millson, John J., The deformation theory of representations of fundamental groups of compact Kähler manifolds (1988)
- Martin R. Bridson and André Haefliger, _Metric Spaces of Non-Positive Curvature_, Grundlehren der mathematischen Wissenschaften, vol. 319, Springer, Berlin, 1999.
- Hatcher, Allen, Algebraic Topology (2002)
- Allen Hatcher, _Algebraic Topology_, Cambridge University Press, 2002. Author's online edition.
- James F. Davis and J. A. Hillman, _Aspherical manifolds with boundary_, preprint, 2026, arXiv:2501.12509v2, version of June 29, 2026.
- Daniel Kasprowski, Mark Powell, and Arunima Ray, _Counterexamples in 4-manifold topology_, EMS Surveys in Mathematical Sciences **9** (2022), no. 1, 193–249. doi:10.4171/EMSS/56.
- Katz, Nicholas M., Nilpotent connections and the monodromy theorem: applications of a result of Turrittin (1970)
- Dawid Kielak, _Virtual Fibring of Manifolds and Groups_, in _Proceedings of the International Congress of Mathematicians 2026_, Vol. 4, _Invited Lectures (Sections 5–8)_, Susan Friedlander and Yuri Tschinkel, eds., Society for Industrial and Applied Mathematics, 2026, 343–362. doi:10.1137/25M1804741.
- Kim, Min Hoon, Orson, Patrick, Park, JungHwan, Ray, Arunima, Open problems (2021)
- Kim, Min Hoon, Powell, Mark, Teichner, Peter, Round handle problem (2021)
- Koszul, Jean-Louis, Homologie et cohomologie des alg\`ebres de Lie (1950)
- Krushkal, Vyacheslav S., Quinn, Frank, Subexponential groups in 4-manifold topology (2000)
- Krushkal, Vyacheslav S., A counterexample to the strong version of Freedman's conjecture (2008)
- Krushkal, Vyacheslav S., Lee, Ronnie, Surgery on closed $4$-manifolds with free fundamental group (2002)
- Krushkal, Vyacheslav S., Quinn, Frank, Subexponential groups in 4-manifold topology (2000)
- Daniel Kasprowski and Markus Land, _Topological 4-manifolds with 4-dimensional fundamental group_, Glasgow Mathematical Journal **64** (2022), no. 2, 454–461. doi:10.1017/S0017089521000215. Cited theorem and lemma locators refer to arXiv:2007.03399v3.
- Arthur Bartels and Wolfgang Lück, _The Borel Conjecture for hyperbolic and CAT(0)-groups_, Annals of Mathematics (2) **175** (2012), no. 2, 631–689. doi:10.4007/annals.2012.175.2.5.
- Wolfgang Lück, _Survey on the Farrell-Jones Conjecture_, Bulletin of the American Mathematical Society (N.S.) **63** (2026), no. 1, 79–117. The cited conjecture locator refers to arXiv:2507.11337v1, version of July 15, 2025.
- Milnor, John W., Topology from the Differentiable Viewpoint (1965)
- John Milnor, _On spaces having the homotopy type of a CW-complex_, Transactions of the American Mathematical Society **90** (1959), no. 2, 272–280. Original article.
- OpenAI, _A marked tensor obstruction to four-dimensional disk embedding_, OpenAI Math Release preprint OAI:A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026, 2026.
- Pantev, Tony, Toën, Bertrand, Vaquié, Michel, Vezzosi, Gabriele, Shifted symplectic structures (2013)
- Powell, Mark, Ray, Arunima, Teichner, Peter, The 4-dimensional disc embedding theorem and dual spheres (2025)
- Powell, Mark, Ray, Arunima, Teichner, Peter, The 4-dimensional disc embedding theorem and dual spheres (2025)
- Mark Powell, Arunima Ray, and Peter Teichner, _The 4-dimensional disc embedding theorem and dual spheres_, Selecta Mathematica (N.S.) **31** (2025), article 80. doi:10.1007/s00029-025-01069-y.
- Michael H. Freedman and Frank Quinn, _Topology of 4-manifolds_, Princeton Mathematical Series, vol. 39, Princeton University Press, Princeton, NJ, 1990. doi:10.1515/9781400861064. Section and lemma numbers refer to Frank Quinn's January 2013 reformatted, unrevised version.
- Frank Quinn, _Ends of maps. III: Dimensions 4 and 5_, Journal of Differential Geometry **17** (1982), no. 3, 503–521. doi:10.4310/jdg/1214437139.
- Frank Quinn, _The stable topology of 4-manifolds_, Topology and its Applications **15** (1983), no. 1, 71–77. doi:10.1016/0166-8641(83)90049-4.
- De Stefani, Alessandro, Grifo, Eloísa, Jeffries, Jack, A Zariski–Nagata theorem for smooth $\mathbb{Z}$-algebras (2020)
- Jacek Świątkowski, _Hyperbolic Coxeter groups with Sierpiński carpet boundary_, Bulletin of the London Mathematical Society **48** (2016), 708–716. The cited Appendix Proposition A.2 is in arXiv:1502.02044v1.
- C. T. C. Wall, _List of problems_, in _Homological Group Theory_, C. T. C. Wall, ed., London Mathematical Society Lecture Note Series, vol. 36, Cambridge University Press, 1979, 369–394.
- Christian Wegner, _The $K$-theoretic Farrell-Jones conjecture for CAT(0)-groups_, Proceedings of the American Mathematical Society **140** (2012), no. 3, 779–793. doi:10.1090/S0002-9939-2011-11150-X. Cited theorem locators refer to arXiv:1012.3349v2.

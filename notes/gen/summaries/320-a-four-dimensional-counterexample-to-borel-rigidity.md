[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 320](../index/topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md)

# 320 — A four-dimensional counterexample to Borel rigidity

[Index page](../index/topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md)

## Original CONTENTS.md summary

The release's blurb [S1:7847] and the catalog abstract [S2:734] state
the family's claim: closed connected aspherical topological
four-manifolds that are homotopy equivalent but not homeomorphic, with a
common word-hyperbolic fundamental group, so the homeomorphism-existence
formulation of the Borel conjecture fails in dimension four. The
manuscript's abstract "We construct closed connected aspherical topological four-manifolds
that are homotopy equivalent but not homeomorphic, disproving the
homeomorphism-existence formulation of the Borel conjecture in dimension
four. Their common
fundamental group is word-hyperbolic. One of the manifolds also has a
self-homotopy equivalence not homotopic to a homeomorphism. [S3:44–51]"

## Undergraduate summary

A manifold is aspherical when its universal cover is contractible, so
its fundamental group determines its homotopy type. The topological
Borel conjecture asks whether homotopy equivalence between closed
aspherical manifolds forces them to be homeomorphic — in the weaker
homeomorphism-existence form, merely that two homotopy-equivalent closed
aspherical manifolds are homeomorphic to each other. The conjecture is
true in dimensions at most two and for closed orientable aspherical
three-manifolds (geometrization), and for a wide range of
higher-dimensional manifolds with good group-theoretic hypotheses. The
manuscript shows the weakest form already fails in dimension four
[S4:3–10]:

> **theorem**
There exist closed connected aspherical topological four-manifolds
$M$ and $N$ that are homotopy equivalent but not homeomorphic.
Their common fundamental group is word-hyperbolic. [S4:12–16]

In addition, one of the two manifolds carries a self-homotopy
equivalence that no homeomorphism of the manifold is homotopic to, a
stronger obstruction that a nonhomeomorphic pair by itself would not
imply.

## Graduate summary

**The construction.** The pair is built from a finite collared Poincaré
chamber $(P,S)$ of dimension four whose fundamental group has an
epimorphism to $\Z$. Writing $S_d$ for the boundary in the connected
cyclic cover of degree $d$, a marked filling of $S_d$ is a compact
four-manifold with that identified boundary and the prescribed graph
homotopy type. The double cover $S_2$ has a marked filling, but $S_d$
has none for odd $d\geq3$ — a parity obstruction from two colors of
plumbing caps, each grope carrying four terminal caps grouped into two
red--blue pairs. For even $d$ one can choose red at one vertex and blue
at the other to make the selected sheets disjoint; for odd $d$ the
endpoint-assignment theorem would force the color choices to alternate
around the odd cycle, which is impossible [S4:82–171].

**The cyclic-cover criterion and the reflection step.** The
cyclic-cover criterion works in every manifold dimension: it converts a
double-cover model plus the eventual nonexistence of odd-cover models
into a self-homotopy equivalence not represented by any homeomorphism,
composing a lifted homeomorphism with a large deck translation and
imposing no finite-order condition on that homeomorphism. The reflection
method of Davis in the Poincaré-chamber form then gives a full
reflection of $P$ with no manifold model in its odd-degree cyclic covers;
quotienting its elementary abelian group of chamber labels by a binary
relation space acting freely forces every simplicial symmetry preserving
the relations to be trivial, yielding a finite aspherical complex $Q$
with the same odd-cover obstruction [S4:82–171].

**The two models and the outer-automorphism obstruction.** The chambers
of $Q_2$ are replaced by the filling of $S_2$ in two ways: in one every
boundary identification is the same, and in the other the gluing is
twisted by the double-cover deck involution according to a nonzero
linear functional on the label group. Both give closed manifold models
of $Q_2$ realizing two subgroups of $\mathrm{Out}(\Pi)$ — the horizontal
subgroup $\mathsf A$ on $M$ and the graph subgroup $\mathsf B_\ell$ on
$N$ — and the subgroups are not conjugate in $\mathrm{Out}(\Pi)$ because they
contain different numbers of elements admitting finite-order lifts to
$\mathrm{Aut}(\Pi)$. The final step proves $\mathrm{Out}(\Pi)$ is finite (a uniform bound
on square grids makes the support cubulation hyperbolic, and Poincaré
duality with the homological Shapiro lemma excludes the virtually cyclic
splittings an infinite outer group would force) and gives the normalizer
equality $N_{\mathrm{Out}(\Pi)}(\mathsf A)=\mathsf A\times\langle\delta\rangle$;
together with the absence of $\delta$ on $M$ this makes $\mathsf A$ a
Sylow $2$-subgroup of the realized outer automorphisms, so any
homeomorphism $M\to N$ would force the forbidden conjugacy
[S4:82–171].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The homeomorphism-existence question first appears in Borel's letter to
Serre of May 2, 1953, phrased for compact manifolds that are classifying
spaces. Rigidity is classical in dimensions at most two and for closed
orientable aspherical three-manifolds by geometrization and
three-dimensional rigidity. In higher dimensions Hsiang and Wall proved
the homeomorphism-existence statement for homotopy tori in dimensions at
least five, Farrell and Jones for closed negatively curved manifolds in
those dimensions, and Bartels and Lück proved the prescribed-class
formulation in dimensions at least five for a class of groups containing
word-hyperbolic groups and groups acting geometrically on
finite-dimensional CAT(0) spaces. In dimension four these rigidity
theorems use further geometric input: Bartels--Lück's four-dimensional
application assumes the fundamental group is good in the sense of
Freedman, Khan proves rigidity up to topological $s$-cobordism for
torsion-free word-hyperbolic fundamental groups, and the Freedman--Quinn
five-dimensional $s$-cobordism product theorem assumes a good
fundamental group. The word-hyperbolicity here lies within the
group-theoretic range of those results, while the dimension is essential
to their topological conclusion. Recent examples of Davis--Hayden--
Huang--Ruberman--Sunukjian are closed aspherical smooth
four-manifolds homeomorphic but not diffeomorphic, so the present
concern is homeomorphism in the topological category [S4:28–78].

## Consequences

**The homeomorphism-existence Borel conjecture is false in dimension
four.** There exist closed connected aspherical topological
four-manifolds $M$ and $N$ that are homotopy equivalent but not
homeomorphic, with a common word-hyperbolic fundamental group
[S4:12–16].

**A self-map obstruction.** There exists a closed connected aspherical
topological four-manifold $M$ and a homotopy equivalence $f\colon M\to M$
such that no homeomorphism $M\to M$ is homotopic to $f$; the nonhomeomorphic
pair alone does not imply this, so it is proved separately using the same
$M$ [S4:22–26].

**The obstruction is topological, not smooth.** The result concerns
homeomorphism; the Davis--Hayden--Huang--Ruberman--Sunukjian examples
address the smooth category, so the two obstructions are independent
[S3:44–51].

## Section skeleton

**Manuscript** [S3:44–51], 10 sections under `build/sections/`:
introduction [S4:12–16], cyclic, reflection, models, extension,
hyperbolicity, normalizer, chambers, tensors, formal. No figures. Its
root is `build/paper.tex`, with a `references.tex` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— a root `build/paper.tex`, 10 `.tex` files under `build/sections/`,
and a `references.tex` bibliography; no figures — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 320 at line 7847. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 734. |
| S3 | [`preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/paper.tex`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/paper.tex) | 63 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/sections/introduction.tex`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/sections/introduction.tex) | 171 | Introduction: the setup, the two main theorems, the history and significance, and the construction. |
| S5 | [`preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/references.tex`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/build/references.tex) | 178 | Manuscript bibliography. |

## Bibliography

- M. Artin, _Algebraic approximation of structures over complete local rings_, Publ. Math. Inst. Hautes Études Sci. **36** (1969), 23–58. doi:10.1007/BF02684596.
- A. Borel, _Letter to Jean-Pierre Serre_, May 2, 1953, reproduced with commentary by A. Ranicki in _The birth of the Borel conjecture_, September 22, 2016. .
- V. Chepoi, _Graphs of some CAT(0) complexes_, Adv. Appl. Math. **24** (2000), no. 2, 125–179. doi:10.1006/aama.1999.0677.
- M. W. Davis, _Groups generated by reflections and aspherical manifolds not covered by Euclidean space_, Ann. of Math. (2) **117** (1983), no. 2, 293–324. doi:10.2307/2007079.
- M. W. Davis, _The geometry and topology of Coxeter groups_, London Mathematical Society Monographs Series, vol. 32, Princeton University Press, Princeton, NJ, 2008.
- M. Davis, K. Hayden, J. Huang, D. Ruberman, and N. Sunukjian, _Exotic aspherical $4$-manifolds_, Ann. of Math. (2) **204** (2026), no. 2, 777–794. doi:10.4007/annals.2026.204.2.6.
- M. Bestvina and M. Feighn, _Stable actions of groups on real trees_, Invent. Math. **121** (1995), 287–321. doi:10.1007/BF01884300.
- M. Gutierrez, A. Piggott, and K. Ruane, _On the automorphisms of a graph product of abelian groups_, Groups Geom. Dyn. **6** (2012), no. 1, 125–153. doi:10.4171/GGD/153.
- M. R. Bridson and A. Haefliger, _Metric spaces of non-positive curvature_, Grundlehren der mathematischen Wissenschaften, vol. 319, Springer-Verlag, Berlin, 1999. doi:10.1007/978-3-662-12494-9.
- A. J. S. Hamilton, _The triangulation of $3$-manifolds_, Quart. J. Math. Oxford Ser. (2) **27** (1976), no. 1, 63–70. doi:10.1093/qmath/27.1.63.
- A. Hatcher, _Algebraic topology_, Cambridge University Press, Cambridge, 2002.
- F. T. Farrell and L. E. Jones, _Compact negatively curved manifolds (of dim $\ne 3,4$) are topologically rigid_, Proc. Natl. Acad. Sci. USA **86** (1989), no. 10, 3461–3463. doi:10.1073/pnas.86.10.3461.
- M. Gutierrez and A. Kaul, _Automorphisms of right-angled Coxeter groups_, Int. J. Math. Math. Sci. **2008** (2008), Article ID 976390, 10 pp. doi:10.1155/2008/976390.
- Q. Khan, _Homotopy invariance of $4$-manifold decompositions: Connected sums_, Topology Appl. **159** (2012), no. 16, 3432–3444. doi:10.1016/j.topol.2012.08.005.
- A. Bartels and W. Lück, _The Borel conjecture for hyperbolic and CAT(0)-groups_, Ann. of Math. (2) **175** (2012), no. 2, 631–689. doi:10.4007/annals.2012.175.2.5.
- M. Kreck and W. Lück, _Topological rigidity for non-aspherical manifolds_, Pure Appl. Math. Q. **5** (2009), no. 3, 873–914. .
- W. Lück, _Survey on aspherical manifolds_, in _European Congress of Mathematics_, European Mathematical Society, Zürich, 2010, 53–82. doi:10.4171/077-1/4.
- J. Milnor, _On spaces having the homotopy type of a CW-complex_, Trans. Amer. Math. Soc. **90** (1959), no. 2, 272–280. doi:10.1090/S0002-9947-1959-0100267-4.
- OpenAI, _A marked tensor obstruction to four-dimensional disk embedding_, OpenAI Math Release preprint OAI:A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026, 2026.
- OpenAI, _A PD4 group without an aspherical manifold model_, OpenAI Math Release preprint OAI:A-PD4-group-without-an-aspherical-manifold-model-September-24-2026, 2026.
- F. Paulin, _Outer automorphisms of hyperbolic groups and small actions on $\mathbb R$-trees_, in _Arboreal group theory_ (Berkeley, CA, 1988), R. C. Alperin (ed.), Mathematical Sciences Research Institute Publications, vol. 19, Springer-Verlag, New York, 1991, 331–343. doi:10.1007/978-1-4612-3142-4\_12.
- M. H. Freedman and F. Quinn, _Topology of $4$-manifolds_, Princeton Mathematical Series, vol. 39, Princeton University Press, Princeton, NJ, 1990.
- E. Spanier, _Singular homology and cohomology with local coefficients and duality for manifolds_, Pacific J. Math. **160** (1993), no. 1, 165–200. doi:10.2140/pjm.1993.160.165.
- J. Paix\ ao and J. Spreer, _Random collapsibility and $3$-sphere recognition_, arXiv:1509.07607v1 [math.GT], September 25, 2015.
- J. Stallings, _Group theory and three-dimensional manifolds_, Yale University Press, New Haven and London, 1971.
- P. Przytycki and J. Świątkowski, _Flag-no-square triangulations and Gromov boundaries in dimension $3$_, Groups Geom. Dyn. **3** (2009), no. 3, 453–468. doi:10.4171/GGD/66.
- W.-C. Hsiang and C. T. C. Wall, _On homotopy tori II_, Bull. London Math. Soc. **1** (1969), no. 3, 341–342. doi:10.1112/blms/1.3.341.
- C. A. Weibel, _An introduction to homological algebra_, Cambridge Studies in Advanced Mathematics, vol. 38, Cambridge University Press, Cambridge, 1994.
- J. Block and S. Weinberger, _On the generalized Nielsen realization problem_, Comment. Math. Helv. **83** (2008), no. 1, 21–33. doi:10.4171/CMH/116.

[Notes](../../README.md) / [Summaries](../README.md) / [Differential geometry](../../index/disciplines/differential-geometry.md) / [Family 342](../../index/differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md)

# 342 — Donaldson's tamed-to-compatible conjecture

[Index page](../../index/differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md)

## Original CONTENTS.md summary

The catalog's blurb is two sentences and a scope-note link: "Proves Donaldson's tamed-to-compatible conjecture: every smooth almost complex structure on a closed four-manifold that is tamed by a symplectic form admits a compatible symplectic form. The almost complex structure stays fixed; the form's cohomology class may change. [S1:8304]" The release's own entry list carries the identical two sentences, word for word, as the family's abstract text [S2:782].

The manuscript's abstract says the same thing and adds a second result the blurb leaves out 

> We prove that every smooth almost complex structure on a closed four-manifold which is tamed by a symplectic form is compatible with a symplectic form. This gives a positive solution to Donaldson's tamed-to-compatible conjecture. We also characterize the compatible cone by strict intersection positivity on the closure of the invariant part of the taming cone. [S4:9–13]

## Undergraduate summary

The manuscript fixes the two conditions in the introduction. A symplectic form is a closed nondegenerate two-form; it tames an almost complex structure `J` when it pairs positively with the `J`-rotated vector, and it is compatible when the form is also invariant under `J` 

> _tames_ \(J\) if \(\omega(v,Jv)>0\) for every nonzero tangent vector \(v\). It is _compatible_ with \(J\) if, in addition, \(\omega(Ju,Jv)=\omega(u,v)\). A taming form is automatically nondegenerate; thus a closed taming form is symplectic. [S6:7–10]

Compatibility is therefore taming plus invariance, and the manuscript notes that a taming form is already nondegenerate, so a closed taming form is symplectic. The question Donaldson posed is recorded in one sentence, with the citation attached 

> Donaldson asked whether the existence of a taming symplectic form on a closed four-manifold implies the existence of a compatible one \cite[Section 5.2, Question 2]Donaldson2006. [S6:12–14]

The answer the manuscript gives is yes. Its main theorem is stated at the top of the introduction 

> Suppose that a smooth almost complex structure \(J\) on a closed connected smooth real four-manifold \(X\) is tamed by a symplectic form. Then there is a smooth symplectic form compatible with \(J\). [S6:24–26]

The blurb's second sentence is the manuscript's own caveat, stated immediately after the theorem 

> The almost complex structure in Theorem   is the given one. The conclusion imposes no condition on the cohomology class of the compatible form. In particular, it does not assert that an arbitrary taming class contains a compatible representative. [S6:29–32]

So the form found need not live in the taming form's class. The cone machinery says how much room the class has to move, and the corollary gives the case where there is no room at all: when the positive index of the intersection form is 1, "every taming class has a smooth compatible symplectic representative. [S6:68–69]" 

The restriction in the corollary is not decoration. The manuscript records that the cone-sum inclusion can be strict, and points to an explicit example [S6:74–77]:

> The inclusion
> \(\mathcal K_J^c+H_J^-\subseteq\mathcal K_J^t\)
> can be strict when \(h_J^-<b_2^+-1\), even if \(H_J^-=0\);
> Example~\ref{ex:strict-cones} gives an explicit four-torus.

The result is used by a second manuscript in the release. The introduction defines the hypersymplectic triple and names the companion's theorem 

> A triple of closed two-forms on an oriented four-manifold is _hypersymplectic_ if every nonzero real linear combination is symplectic and induces the given orientation. The companion \cite[Theorem 1.1]OpenAIHypersymplectic2026 combines the current estimates above with additional prescribed-class and deformation arguments to deform hypersymplectic triples normalized by \(\int_X\omega_i\wedge\omega_j=\delta_ij\) on closed connected oriented smooth four-manifolds to hyperkähler triples, while fixing each class \([\omega_i]\in H^2(X;\R)\). [S6:207–215]

## Graduate summary

The cone theorem is the structural result, stated at [S6:37–58]. It fixes the orientation induced by `J`, writes `K_J^t` and `K_J^c` for the taming and compatible classes in `H²(X; R)`, writes `H_J^-` for the subspace represented by smooth closed real anti-invariant two-forms, and sets `V = (H_J^-)^⊥` and `C = K_J^t ∩ V` with orthogonality taken for the intersection pairing. It proves two identities: `K_J^t = C + H_J^-`, a Minkowski sum, and `K_J^c` as the set of elements of `C` that pair strictly positively with every nonzero element of the closure of `C`, the closure taken in `V`. The corollary at [S6:60–70] is the form the blurb's second sentence is about: if `h_J^- = b₂⁺ − 1` then `K_J^t = K_J^c + H_J^-`, and when `b₂⁺ = 1` the two cones coincide.

The proof runs through positive currents, not through forms. The introduction sets out the mechanism in one paragraph 

> Fix an auxiliary \(J\)-Hermitian metric. If no compatible form exists, separation produces a nonzero positive current \(P\) that annihilates closed invariant forms. An elliptic correction gives \(T=P+Q\), which annihilates every closed two-form, with \(Q\) initially an anti-invariant distribution. Represent \(P\) as a positive weighted average of unit complex-line bivectors, and let \(\mu\) be the resulting measure on \(X\), its trace measure. Corrected radial test functions give \(\mu(B_r(x))\le Cr^2\). [S6:135–142]

The quadratic mass bound `μ(B_r(x)) ≤ C r²` is the estimate the paragraph names, and the angular estimate is `O(r⁴)` for pairs of complex lines whose base points are less than `r` apart [S6:143–147]. The principal step is the density-splitting theorem, and the manuscript is explicit that it does not need the annihilation property 

> Existence of the limit is part of the argument. The principal step, Theorem  , proves that the restriction \(P_E=\ind_E P\) is closed. It applies to any closed current \(P+Q\) with an anti-invariant \(L^2\) correction and the stated mass and angular bounds; annihilation of all closed forms is not needed for this step. [S6:157–162]

The closing estimate is a balance between two errors, and the manuscript writes the balance out 

> where the two factors are the square roots of the angular and transverse moments. The \(L^2\) bound controls the correction's cutoff error separately. Together these estimates prove closedness of the density restriction without requiring a quantitative rate for tangent measure convergence. [S6:177–181]

The dimensionality is stated as a fact about the estimates, not as a limitation of the theorem: "The regularized pairing estimates use the four-dimensional fact that anti-invariant two-forms are self-dual. [S6:194–195]" The roadmap the introduction gives for the sections is 

> Sections   and   construct the separating current and prove its mass bound. Section   establishes the regularization and angular estimates. Section   proves density existence and the planar tangent description; Section   uses them to control cutoff boundaries and prove closedness of \(P_E\). Section   completes the existence argument. Section   develops the prescribed-class separation and proves the cone description. [S6:196–205]

The sections carry that roadmap: separation at `02-currents.tex:88`, quadratic mass growth at `03-mass.tex:7`, the energy proposition at `04-energy.tex:219`, the density-splitting theorem at `05-density.tex:8`, its proof in `06-splitting.tex`, the proof of the main theorem at `07-conclusion.tex:3`, and the cone theory in `08-cones.tex`. The density-splitting theorem is the single most referenced label in the manuscript: it is defined at `05-density.tex:8` and used at `05-density.tex:40`, `05-density.tex:149`, `06-splitting.tex:4`, `07-conclusion.tex:9`, `08-cones.tex:222`, `01-introduction.tex:158` and `01-introduction.tex:193`. The introduction contains exactly three statement environments — the main theorem, the cone theorem, and the corollary — and no named analytic theorem; the analytic estimates are stated in the sections.

The conclusion's closing step pairs the current with a residual current rather than with itself, and ends by intersecting two cones 

> The positive cone and the subspace of closed invariant smooth forms therefore intersect. Any form in their intersection is the required smooth compatible symplectic form for \(J\). [S12:67–70]

The strict-inclusion example is proved in the cone section, and the corollary's proof explains why the hypothesis `h_J^- = b₂⁺ − 1` is what makes the duality condition automatic 

> of its positive-square cone. Every element of that component pairs strictly positively with every nonzero element of its closure, by Cauchy–Schwarz in coordinates of signature [S13:364–366]

The example itself is the four-torus at [S13:375–418], and the example's closing sentence says which test fails: "In Theorem  , the class \([U+V_0]\) fails the strict positivity test against \([U-V_0]\in\mathcal C\), and conversely. [S13:415–417]" 

The formalization is the single-class statement, not the cone characterization. The scope note states the shape 

> Donaldson's tamed-to-compatible conjecture asks whether an almost-complex structure tamed by a symplectic form also admits a compatible symplectic form. The formalized result establishes this for every closed connected smooth four-manifold, keeping the almost-complex structure fixed. No integrability assumption or prescribed cohomology class for the compatible form is required. [S16:9]

The declaration is `OAI/Geometry/TamingCompatibility/Main.lean`, 56 lines, with the statement at [S20:30–34]:

> theorem taming_implies_compatibility
>     [T2Space X] [SecondCountableTopology X] [CompactSpace X] [ConnectedSpace X]
>     (J : AlmostComplexStructure X)
>     (h : ∃ α : TwoForm X, IsSymplectic α ∧ Tames α J) :
>     ∃ η : TwoForm X, IsSymplectic η ∧ Compatible η J := by

The proof body runs from line 35 to line 50 and ends with `norm_num at hnormal`; there is no final `exact`, so the body's shape is a chain of obtained lemmas. The comparator stub defines the predicates itself, and its definition of compatibility matches the manuscript's: "def Compatible (α : TwoForm X) (J : AlmostComplexStructure X) : Prop := Tames α J ∧ IsInvariant α J [S19:55–56]" . The stub restates the same theorem under its own definitions and ends in `sorry` 

> theorem taming_implies_compatibility
>     [T2Space X] [SecondCountableTopology X] [CompactSpace X] [ConnectedSpace X]
>     (J : AlmostComplexStructure X)
>     (h : ∃ α : TwoForm X, IsSymplectic α ∧ Tames α J) :
>     ∃ η : TwoForm X, IsSymplectic η ∧ Compatible η J := by
>   sorry

The stub is 68 lines and the `sorry` is at line 63, so the comparator states the target the release set for itself and does not prove it. The challenge record names the solution module, the theorem, and the axioms it expects [S18:1–14]:

> {
>   "challenge_module": "ComparatorChallenges.TamingCompatibility",
>   "solution_module": "OAI.Geometry.TamingCompatibility.Main",
>   "theorem_names": [
>     "OAI.TamingCompatibility.taming_implies_compatibility"
>   ],
>   "definition_names": [],
>   "permitted_axioms": [
>     "propext",
>     "Quot.sound",
>     "Classical.choice"
>   ],
>   "enable_nanoda": false
> }

The formalization record names the September edition of the manuscript as its source, not the October edition the catalog lists 

> - title: “Taming implies compatibility on four-manifolds” authors: [“OpenAI”] [S17:682–683]

The scope note names the same September edition [S16:5]. The `main_results` entry names the declaration, the comparator config, and the file [S17:1677–1679]:

> - comparator_config: ComparatorChallenges/TamingCompatibility.json
>   declaration: OAI.TamingCompatibility.taming_implies_compatibility
>   file: OAI/Geometry/TamingCompatibility/Main.lean

The status block carries the release-wide scope, not a per-family one [S17:969–970]:

> status:
>   scope: "Partial progress."

The automation and review blocks are the release-wide ones, with the review status unchecked [S17:1773–1778]:

> automation:
>   methods:
>     - method: agent
>
> review:
>   status: unchecked

The ledger's per-manuscript formalized flag for this family is 0, because the formalized path in the record is the superseded edition's directory and the listed manuscript is the October edition [S22]. The shipped PDF of the manuscript is [S15].

## History of the conjecture

The manuscript's bibliography opens with the Donaldson paper the introduction cites for the question, and the entry is the first in the file [S14:1–13]:

> @incollection{Donaldson2006,
>   author    = {Donaldson, S. K.},
>   title     = {Two-forms on four-manifolds and elliptic equations},
>   booktitle = {Inspired by S. S. Chern},
>   series    = {Nankai Tracts in Mathematics},
>   volume    = {11},
>   pages     = {153--172},
>   publisher = {World Scientific},
>   address   = {Hackensack, NJ},
>   year      = {2006},
>   doi       = {10.1142/9789812772688_0007},
>   url       = {https://arxiv.org/abs/math/0607083}
> }

The citation the introduction attaches to the question is to Section 5.2, Question 2 of that 2006 collection article [S6:12–14], not to a 1990 survey; the introduction does not date the question, and the bibliography carries no 1990 Donaldson entry. The manuscript's own framing of the question is the sentence quoted in the undergraduate section [S6:12–14].

The paper has two editions in the release. The October 6, 2026 edition is the one the catalog lists; the September 23, 2026 edition is on disk and is the edition the formalization record and the scope note name [S16:5]. The October edition's README carries the version note naming the changes 

> This version characterizes the compatible cone by intersection positivity, restricts the cone-sum equality to $h_J^-=b_2^+-1$, and adds a four-torus example of strict inclusion [S3:21]

The release's update log gives the reason for re-issuing both papers in this pair: "Taming and hypersymplectic deformation (2 manuscripts): corrected the cone-equality claim in Taming implies compatibility, added a strict-inclusion example, and removed an unnecessary cone-comparison dependency from the hypersymplectic paper. [S21:23]" The October edition's corollary is the one that carries the `h_J^- = b₂⁺ − 1` hypothesis, and the strict-inclusion four-torus example is its addition [S6:60–70] [S13:375–418].

## Consequences

The direct consequence inside the release is the companion paper. The introduction cites the companion's theorem by number, verbatim, in the passage quoted in the undergraduate section, and the companion's bibliography entry is the last in the manuscript's file [S6:207–215] [S14:289–292]:

> @misc{OpenAIHypersymplectic2026,
>   author = {{OpenAI}},
>   title = {{Deforming hypersymplectic four-manifolds to hyperk{\"a}hler triples}},
>   howpublished = {OpenAI Math Release preprint

The companion is family 341, Donaldson's hypersymplectic deformation conjecture, which the ledger records as one manuscript at tier T0 with no formalization, no scope note, no comparator challenge, and no verification bundle. The citation is the manuscript's own: the release's typed-edge inventory carries no edge between 342 and 341, and the measured citation tables do not record one.

The cone characterization is the part of the result with content beyond the theorem statement. It gives a criterion for compatibility that is checkable inside cohomology — strict positivity against the closure of the invariant part of the taming cone — and the four-torus example shows the cone-sum equality cannot be stated without the `h_J^- = b₂⁺ − 1` hypothesis [S13:364–366] [S13:415–417]. The corollary for `b₂⁺ = 1` is the case where taming and compatibility cones coincide, so in that case the class does not move [S6:67–69].

The formalization consequence is a gap, not a coverage. The declaration proves the single-class form, which is the shape the scope note describes; the cone theorem, the corollary, the density-splitting theorem, the quadratic mass bound, and the strict-inclusion example are not formalized. The comparator challenge for this family is a stub with one `sorry`, and the release's review status for the whole formalization is unchecked [S19:58–63] [S17:1773–1778]. The manuscript states no open directions: its conclusion section is the proof of the main theorem, and the introduction's closing paragraph points to the companion paper, not to a question [S12:1–70] [S6:207–215].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Release blurb, manuscript link, abstract |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family entry in the release's entry list |
| S3 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/README.md`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/README.md) | 21 | Title, date, bibtex key, version note |
| S4 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/main.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/main.tex) | 28 | Abstract and include list |
| S5 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/preamble.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/preamble.tex) | 54 | Macro preamble |
| S6 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/01-introduction.tex) | 215 | Conjecture, definitions, theorems, mechanism, companion |
| S7 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/02-currents.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/02-currents.tex) | 164 | Separation proposition |
| S8 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/03-mass.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/03-mass.tex) | 150 | Quadratic mass growth proposition |
| S9 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/04-energy.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/04-energy.tex) | 270 | Energy proposition |
| S10 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/05-density.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/05-density.tex) | 278 | Density-splitting theorem |
| S11 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/06-splitting.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/06-splitting.tex) | 271 | Proof of the density-splitting theorem |
| S12 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/07-conclusion.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/07-conclusion.tex) | 71 | Proof of the main theorem |
| S13 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/08-cones.tex`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/08-cones.tex) | 418 | Cone theory, class estimates, strict-inclusion example |
| S14 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/references.bib`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/references.bib) | 295 | Bibliography, Donaldson 2006, intra-corpus entry |
| S15 | [`preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf) | 7145 | Shipped manuscript PDF |
| S16 | [`lean/docs/342.md`](../../../lean/docs/342.md) | 15 | Scope note |
| S17 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1783 | Source, status, main_results, automation, review |
| S18 | [`lean/ComparatorChallenges/TamingCompatibility.json`](../../../lean/ComparatorChallenges/TamingCompatibility.json) | 14 | Challenge record |
| S19 | [`lean/ComparatorChallenges/TamingCompatibility.lean`](../../../lean/ComparatorChallenges/TamingCompatibility.lean) | 68 | Comparator stub, definitions, target, `sorry` |
| S20 | [`lean/OAI/Geometry/TamingCompatibility/Main.lean`](../../../lean/OAI/Geometry/TamingCompatibility/Main.lean) | 56 | Formalized declaration |
| S21 | [`history.md`](../../../history.md) | 31 | Release update log |
| S22 | [`notes/tables/catalog.tsv`](../../../notes/tables/catalog.tsv) | 373 | Ledger row for family 342 |

## Bibliography

- Buchdahl, Nicholas, On compact Kähler surfaces (1999)
- Donaldson, S. K., Two-forms on four-manifolds and elliptic equations (2006)
- Draghici, Tedi, Zhang, Weiyi, A note on exact forms on almost complex manifolds (2012)
- Elkhadhra, Fredj, Poincaré–Lelong formula, $J$-analytic subsets and Lelong numbers of currents on almost complex manifolds (2014)
- Elkhadhra, Fredj, Mimouni, Souad Khemiri, Sur l'existence du nombre de Lelong d'un courant positif psh défini sur une variété presque complexe (2007)
- Gromov, Mikhail, Pseudo holomorphic curves in symplectic manifolds (1985)
- Harvey, Reese, Lawson, Jr., H. Blaine, An intrinsic characterization of Kähler manifolds (1983)
- Kinnunen, Juha, Real Analysis (2026)
- Lamari, Ahc\`ene, Courants kählériens et surfaces compactes (1999)
- Lejmi, Mehdi, Strictly nearly Kähler 6-manifolds are not compatible with symplectic forms (2006)
- Li, Tian-Jun, Zhang, Weiyi, Comparing tamed and compatible symplectic cones and cohomological properties of almost complex manifolds (2009)
- Li, Tian-Jun, Zhang, Weiyi, Almost Kähler forms on rational 4-manifolds (2015)
- Tian-Jun Li, Shengzhen Ning, The spaces of Kähler and holomorphically tamed symplectic forms on closed 4-manifolds (2026)
- Lin, Dexie, Zhou, Hengyu, A note on $\widetilde{\mathcal{D}}^{+}_{J}$-operator (2025)
- Ludewig, Matthias, Strong short-time asymptotics and convolution approximation of the heat kernel (2019)
- Ludewig, Matthias, Heat kernel asymptotics, path integrals and infinite-dimensional determinants (2018)
- Melrose, Richard, Introduction to Microlocal Analysis (2007)
- OpenAI, {Deforming hypersymplectic four-manifolds to hyperkähler triples} (2026)
- Sullivan, Dennis, Cycles for the dynamical study of foliated manifolds and complex manifolds (1976)
- Tan, Qiang, Wang, Hongyu, Zhou, Jiuru, Zhu, Peng, On tamed almost complex four-manifolds (2022)
- Taubes, Clifford Henry, Tamed to compatible: Symplectic forms via moduli space integration (2011)
- Taubes, Clifford Henry, Tamed to compatible when $b^{2+}=1$ and $b^1=2$ (2017)
- Taylor, Michael E., Pseudodifferential Operators and Nonlinear PDE (1991)
- Ken Wang, Zuyi Zhang, Tao Zheng, Peng Zhu, On a generalized {Monge–Amp\`ere} equation on closed almost Kähler surfaces (2025)
- Hongyu Wang, Ken Wang, Peng Zhu, On closed almost complex four manifolds (2023)

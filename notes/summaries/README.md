# Family summary pages

Sixty extended summaries, one per family, each built from the manuscript's own LaTeX and
verified by script. The pages are rendered by `build_summaries.py` from a hand-edited data
file and the page skeleton, with each quote window resolved from `notes/tables/quotes.tsv`
through the normalizer; the checker measures the rendered bytes and writes nothing.

## Coverage, as four layers

The release's own formalization surface is four separate counts, and one percentage over them says
nothing. The numbers are the ledger's, quoted with the rule that yields each:

| Layer | Count | What the count is |
| --- | --- | --- |
| Formalized manuscripts | **172** of **719** listed manuscript directories | The per-manuscript formalized flag, counting only listed manuscripts. `formalization.yaml` names **173** paths; the extra one is the superseded `Taming-implies-compatibility-on-four-manifolds-September-23-2026`, which family 342's overview entry does not list. |
| Scope notes | **242** of **372** families | `lean/docs/NNN.md`, each with a `## Scope` section. **121** of the 242 sections state no exclusion at all. |
| Comparator challenges | **416** distinct configs | `lean/ComparatorChallenges/*.lean` files, each a challenge **stub**: 539 `sorry` occurrences, 415 files with at least one, the zero-`sorry` exception being `HarmonicGrowth.lean`. The scope notes link **426** occurrences; the 10-gap is one config linked twice inside each of 7 docs. |
| `main_results` entries | **200** entries over **189** unique configs, reaching **136** of 372 families | `lean/formalization.yaml`'s `main_results:` list. The yaml carries no family key, so family-to-config comes only from the scope notes' links. |

The summaries are a fifth layer, and it is the thinnest: **60** of **372** families have a page.

## The summaries layer

**60** family pages, **12,322** lines, over **128** manuscript directories carrying **8.5 MB** of
the LaTeX the Sources tables name (635 specifically-cited `.tex` files). The checker measures
**7,587** `[Sn:line]` marker positions and **1,994** quoted spans across the **61** pages it reads
(the 60 family pages and this link-only index page), and reports **440** problems: **210**
unresolved markdown links, which the slug-canonicalization pass clears, and **230** quoted spans
that are not verbatim against their source, which the quote pass clears, with **0** in the
manuscript-directory and bare-citation passes.

The cost model is the reading pass, not a build. Each page cites the files it read, so the cost per
page is the manuscript LaTeX its Sources table names: the median page cites **18.5** declared
sources and the largest cites **63**. The checker walks the cited files and compares each marker and
each quotation against the bytes the file carries, and it runs nothing.

The pages are not a build target: no Lean, no lake, no comparator runs here. A page states what the
manuscript says and where it sits, with a `file:line` anchor the checker resolves.

## The pages

- [195 — A counterexample to the small Cohen--Macaulay module conjecture](algebra/195-a-complete-local-domain-without-a-small-cohen-macaulay-module.md)
- [196 — A counterexample to Kaplansky's zero-divisor conjecture](algebra/196-a-torsion-free-group-algebra-with-zero-divisors.md)
- [197 — Nonsofic groups and group-ring counterexamples](algebra/197-nonsofic-groups-and-group-ring-counterexamples.md)
- [198 — A counterexample to the little finitistic-dimension conjecture](algebra/198-a-counterexample-to-the-little-finitistic-dimension-conjecture.md)
- [199 — Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama](algebra/199-counterexamples-to-conjectures-of-auslander-reiten-and-tachikawa.md)
- [032 — The rational Hodge conjecture for CM abelian varieties](algebraic-and-complex-geometry/032-the-rational-hodge-conjecture-for-cm-abelian-varieties.md)
- [039 — Nagata's conjecture and maximal Seshadri constants](algebraic-and-complex-geometry/039-nagatas-conjecture-and-maximal-seshadri-constants.md)
- [042 — Oka classification for K3 surfaces and other compact complex surfaces](algebraic-and-complex-geometry/042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md)
- [047 — Complex counterexamples to cancellation and affine fibrations](algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md)
- [049 — A stable-coordinate counterexample in four variables](algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md)
- [050 — A counterexample to Griffiths' positivity conjecture](algebraic-and-complex-geometry/050-counterexample-to-griffiths-positivity-conjecture.md)
- [052 — Tangent-bundle splittings and universal covers](algebraic-and-complex-geometry/052-integrability-of-split-tangent-bundles.md)
- [159 — Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds](combinatorics/159-quasipolynomial-bounds-for-arithmetic-progressions.md)
- [087 — The Mahler conjectures and symplectic width](convex-and-metric-geometry/087-the-mahler-conjectures-and-symplectic-width.md)
- [088 — Petty's projection-volume conjecture and simplex counterexamples](convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md)
- [089 — Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs](convex-and-metric-geometry/089-planar-and-bounded-treewidth-metrics-embed-into-l1.md)
- [098 — A negative answer to the Lang--Plaut problem](convex-and-metric-geometry/098-a-negative-answer-to-the-lang-plaut-problem.md)
- [101 — The sharp simplex conjecture for isotropic constants](convex-and-metric-geometry/101-the-sharp-simplex-conjecture-for-isotropic-constants.md)
- [334 — A smooth surface metric with no local immersion in $\mathbb R^3$](differential-geometry/334-a-smooth-surface-metric-with-no-local-immersion-in-r-3.md)
- [342 — Donaldson's tamed-to-compatible conjecture](differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md)
- [344 — The metric Blaschke conjecture](differential-geometry/344-metric-blaschke-conjecture.md)
- [345 — Infinitely many closed geodesics on spheres and three-manifolds](differential-geometry/345-infinitely-many-closed-geodesics-on-spheres-and-three-manifolds.md)
- [346 — Sharp singular-set bounds for stationary integral varifolds](differential-geometry/346-sharp-singular-set-bounds-for-stationary-integral-varifolds.md)
- [347 — Counterexamples to strong forms of Arnold's fixed-point conjecture](differential-geometry/347-counterexamples-to-stable-morse-fixed-point-bounds.md)
- [348 — Nonnegatively curved Einstein four-manifolds and a topological gap](differential-geometry/348-einstein-four-manifold-classification-and-l2-gap.md)
- [349 — The Solomon--Yau least-volume conjecture](differential-geometry/349-the-solomon-yau-least-volume-conjecture.md)
- [351 — Scalar curvature detects four-dimensional Ricci-flow singularities](differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md)
- [352 — Finite-time singularity of Calabi flow](differential-geometry/352-finite-time-singularity-of-calabi-flow.md)
- [147 — The near-boundary Birkhoff conjecture](dynamical-systems-and-ergodic-theory/147-the-near-boundary-birkhoff-conjecture.md)
- [324 — Lipschitz equivalence without linear isomorphism](functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md)
- [325 — The complete Crouzeix conjecture](functional-analysis/325-complete-crouzeix-conjecture.md)
- [331 — Asymptotic midpoint uniform convexity without asymptotically uniformly convex renorming](functional-analysis/331-asymptotic-midpoint-uniform-convexity-without-asymptotically-uniformly-convex-renorming.md)
- [332 — Metric Markov cotype two for $\ell_1$](functional-analysis/332-metric-markov-cotype-two-for-l1.md)
- [254 — Classifying spaces and geometric obstructions for Artin groups](group-theory/254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md)
- [258 — Gersten's conjecture for one-relator groups](group-theory/258-gerstens-conjecture-for-one-relator-groups.md)
- [259 — A group without fixed price](group-theory/259-a-group-without-fixed-price.md)
- [243 — Choiceless counting does not capture polynomial time](mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md)
- [244 — The partition principle does not imply choice](mathematical-logic/244-partition-principle-does-not-imply-choice.md)
- [271 — Bloch's law and spontaneous ferromagnetic order](mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md)
- [274 — Moore's parity conjecture for $\mathrm{QAC}^0$](mathematical-physics/274-moores-parity-conjecture-for-qac0.md)
- [001 — Milne's rationality conjecture](number-theory/001-milnes-rationality-conjecture.md)
- [002 — The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one](number-theory/002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md)
- [004 — Hilbert's tenth problem over $\mathbb Q$](number-theory/004-hilberts-tenth-problem-over-q.md)
- [006 — Goldfeld's conjecture](number-theory/006-goldfelds-conjecture.md)
- [007 — Two-point Chowla and the corrected binary Elliott conjecture](number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md)
- [010 — Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity](number-theory/010-fontaine-mazur-modularity-at-the-prime-2.md)
- [011 — The Ford--Konyagin--Luca conjecture on prime predecessors](number-theory/011-the-ford-konyagin-luca-conjecture-on-prime-predecessors.md)
- [014 — Restricted geometric Langlands, generic Ramanujan and Arthur parameters](number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md)
- [016 — Zilber--Pink in abelian varieties and the Siegel threefold](number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md)
- [017 — The irrationality exponent of $\pi$ is $2$](number-theory/017-the-irrationality-exponent-of-pi-is-2.md)
- [018 — The Margulis--Platonov conjecture over global fields](number-theory/018-margulis-platonov-conjecture-over-global-fields.md)
- [019 — The $p$-adic section conjecture](number-theory/019-p-adic-section-conjecture.md)
- [287 — All nonabelian free group factors are isomorphic](operator-algebras/287-all-nonabelian-free-group-factors-are-isomorphic.md)
- [362 — Global smoothness for relativistic Vlasov--Maxwell](partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md)
- [221 — The Mézard--Parisi formula for diluted spin glasses](probability-and-statistical-mechanics/221-mezard-parisi-formula-for-diluted-spin-glasses.md)
- [226 — The double-dimer $\mathrm{CLE}_4$ conjecture in the half-plane](probability-and-statistical-mechanics/226-the-curve-scaling-limit-of-half-plane-double-dimers.md)
- [072 — Brennan's conjecture and a counterexample to Kraetzer's prediction](real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md)
- [102 — The Unique Games Conjecture and optimal approximation thresholds](theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md)
- [109 — Integer multiplication below $n\log n$](theoretical-computer-science/109-integer-multiplication-below-n-n.md)
- [136 — The quasilinear PCP-for-PPAD conjecture](theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md)

## The checker

```
python3 notes/scripts/verify_summaries.py
```

It resolves every `[Sn:line]` marker against the shipped file, checks every quotation against the
lines it cites, counts a Sources-table `File` cell that resolves under both roots as a problem, and
writes nothing. Its self-tests are in `notes/scripts/tests/test_summaries.py`, run by
`python3 notes/scripts/run_tests.py notes/scripts/tests/test_summaries.py -q`: a real quotation
corrupted in each form the page uses, one fabricated quotation, a manuscript root retargeted to a
superseded sibling, and a bare locator citation moved above the family's own block.

Three more tools read the pages: `check_summary_manuscripts.py` reports which manuscripts each page
reads and whether the release still names them, `locate_summary_quotes.py` (takes a page path)
reports where a quotation's text actually sits when the checker flags a miss, and
`read_manuscript.py` takes a `preprints/` directory name and prints the abstract, the section
skeleton and the titled statement environments with anchors. All three write nothing.

This page is link-only: it names no manuscript directory and cites no family-keyed file, so the
checker's manuscript-directory pass and its family-citation pass skip it. Its links are checked.

## Not checked

- **312 families have no summary page.** The 60 pages cover 60 of 372 families; the rest are recorded
  in the ledger and the index, not summarized.
- **The 440 checker problems are owned downstream, not in the 60 rendered pages.** The 210
  unresolved links clear when the summary-page slug is canonicalized to the index slug; the 230
  not-verbatim spans clear when the quote pass collapses and the normalizer's rendered output is
  checked against the source it renders. The renderer produces all 60 pages byte-identical
  (`build_summaries.py --check-only` reads 0 problems), so neither class is a defect in the render.
- **The coverage counts are the release's own.** The yaml's `scope`, `automation` and `review` fields
  state partial progress, the agent method, and an unchecked review — those are the release's claims, not
  verified results. Zero `sorry` in a formalized file is not a comparator pass, and it does not mean the
  library elaborates.
- **No page was checked by running Lean.** Nothing in this repo builds, and a Lean run would prove the
  formalized statement, not the manuscript's theorem.
- **The cost model is the reading pass, measured as bytes cited.** It is not a build cost, and it is
  not a per-family estimate of the time a reader spends.

# The shared-bibliography graph

Measured 2026-10-08 by `python3 notes/scripts/extract_citations.py` — report-only, writes nothing,
run three times with byte-identical output. No `lake`, `lean`, `lake exe cache get`, or comparator
run. Every count below is printed by that report, and a count is quoted with the rule that yields it.

The bead's hypothesis was that a citation cluster crossing discipline boundaries is evidence that the
release's 17 disciplines are arbitrary. **At the threshold where sharing is a research signal, it is
not: 6 of 419 pairs at ≥5 shared titles cross a discipline boundary and 0 of 197 at ≥10.** The
boundaries in `overview.tex` line up with the bibliography clusters. The 1,979 cross-discipline pairs
at ≥1 shared title are a textbook floor, not a signal — see "The discipline crossings".

## Population

| Layer | Count | Rule |
|---|---|---|
| `.bib` files | **521** | every `preprints/**/*.bib` |
| Owner manuscripts | **513** of 719 | path component after `preprints`, never `parts[-2]` |
| Owners with >1 file | **7** (max 3) | `references.bib` 477, `refs.bib` 24, `sources.bib` 7, `literature.bib` 4, `bibliography.bib` 2, `companions.bib` 2, `projective_references.bib` 2, 3 singletons |
| Path depth | 4:435 5:79 6:5 9:2 | components of the repo-relative path |
| Families covered | **299** of 372 | via `notes/subfindings.tsv` manuscript rows |
| Disciplines covered | **17** of 17 | via the ledger `discipline` column |
| Entries | **13,802** | `@type{key,` at line start, body to the next line-start `@` |
| Entry types | article 9,451 · misc 2,337 · book 776 · incollection 734 · inproceedings 415 · techreport 37 · phdthesis 35 · unpublished 12 · mastersthesis 5 | `@` type lowercased |
| Distinct keys | **9,910** | key string, verbatim |
| Keys used by >1 manuscript | **2,393** | distinct owning manuscripts ≥2 |

Top keys by owning manuscripts: `StacksProject` 26, `Hatcher2002` 21, `Stacks` 12,
`DemaillyPaun2004` 11, `Penrose1973` 11, `SGA1` 11, `Yau1978` 11, `BCHM2010` 10, `Bray2001` 10,
`Carayol1986` 10.

`StacksProject` and `Stacks` are the same work under two keys, and the work layer counts it once
(42 manuscripts) while the key layer splits it 26 + 12. Keys are a lexical layer; works are the
matching layer.

## The bibliographies are live, not decorative

**13,058 of 13,797** manuscript-key pairs — a pair is a (manuscript, key) with the key appearing in
that manuscript's `.bib` files; 13,797 is below 13,802 because 5 keys repeat inside one manuscript —
appear in a `\cite…{…}` locator somewhere in that manuscript's own `.tex` tree. Per-manuscript cited
fraction: min **0.333**, median **1.000**, max **1.000**; **0** manuscripts at 0, **444** of 494 at
≥0.9. A manuscript that lists a work it never cites is the exception, and the corpus has no
bibliography that is pure decoration.

## Work identity

Two entries are the same work when their titles normalize equal. The rule, in order: LaTeX accent
macros folded to their base letter; `\& \% \_ \-` unescaped; remaining `\command` removed; braces and
`$` dropped; U+2019/U+2018 folded to ASCII apostrophe; NFKD with combining marks dropped; lowercased;
every non-alphanumeric run collapsed to one space.

The accent branch carries a `(?![a-zA-Z])` guard, so `\'e` followed by a letter is **not** folded.
The result is a deterministic artifact, not a crash:

| Source title | Normalized key |
|---|---|
| `Th{\'e}orie de {Hodge}. {II}` | `th eorie de hodge ii` |
| `Compact {K{\"a}hler} manifolds` | `compact k ahler manifolds` |
| `M{\"o}bius inversion` | `m obius inversion` |
| `The $\R^n$ case` | `the n case` |

Identical source spellings therefore match, which is what the corpus actually contains; the cost is
that a LaTeX-escaped accent and a Unicode precomposed accent of the same name do **not** match
(`K{\"a}hler` → `k ahler`, `Kähler` → `kahler`). The sensitivity of every headline number to that
guard is measured below; it is 0 at the thresholds that matter.

Sharing is set-based: a manuscript carries the **set** of its normalized titles, so a work listed
twice in one manuscript is one title. A work is *shared* when its owning set has size ≥2. A pair edge
exists when two manuscripts share ≥*k* titles; a cluster is a connected component of that pair graph.
*k* is quoted with every count.

## Most-cited works

Manuscripts owning the work, over 494 manuscripts. The title is the most frequent verbatim form
(ties: lexicographically first); the anchor is the first entry carrying that exact form.

| Mss | Title (verbatim, as written in the `.bib`) | Anchor |
|---|---|---|
| 42 | `The {Stacks Project}` | `preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/references.bib:106` |
| 23 | `Algebraic Topology` | `preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/references.bib:120` |
| 20 | `Introduction to Geometric Measure Theory` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:246` |
| 17 | `Existence of minimal models for varieties of log general type` | `preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/references/references.bib:87` |
| 16 | `Correlation inequalities on some partially ordered sets` | `preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/build/references.bib:98` |
| 14 | `Elliptic Partial Differential Equations of Second Order` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:183` |
| 13 | `Complex Analytic and Differential Geometry` | `preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/references.bib:96` |
| 12 | `Algebraic Number Theory` | `preprints/A-Counterexample-to-Kuroshs-Division-Ring-Problem-September-23-2026/build/references.bib:102` |
| 12 | `Naked singularities` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:18` |
| 12 | `Probability Inequalities for Sums of Bounded Random Variables` | `preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/build/references.bib:317` |
| 11 | `{Log abundance in characteristic zero}` | `preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/build/references.bib:377` |
| 11 | `Proof of the {Riemannian Penrose} inequality using the positive mass theorem` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:64` |
| 11 | `Th{\'e}orie de {Hodge}. {II}` | `preprints/Log-abundance-in-characteristic-zero-September-24-2026/build/references.bib:523` |
| 11 | `The inverse mean curvature flow and the {Riemannian Penrose} inequality` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:53` |
| 10 | `Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field` | `preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/references.bib:171` |
| 10 | `Birational Geometry of Algebraic Varieties` | `preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/build/references.bib:242` |
| 10 | `The pseudo-effective cone of a compact {K{\"a}hler} manifold and varieties of negative {Kodaira} dimension` | `preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-5-2026/build/references.bib:343` |
| 9 | `Fast Probabilistic Algorithms for Verification of Polynomial Identities` | `preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/build/references.bib:67` |
| 9 | `Functions of Bounded Variation and Free Discontinuity Problems` | `preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/build/references.bib:112` |
| 9 | `Orbifolds, special varieties and classification theory` | `preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/references.bib:10` |

The work layer: **8,775** distinct normalized titles, **2,251** owned by ≥2 manuscripts, **863** by
≥3, **193** by ≥5, **17** by ≥10. **932** of the 2,251 shared works cross a family boundary and
**333** cross a discipline boundary. **23** of the 494 manuscripts share no title with any other.

The top of the list is a textbook-and-standard-reference list (Stacks Project, Hatcher, de Giorgi,
Folland, Marcus–Weiss, Durrett, Gromov, Grothendieck, Kollár–Mori, Kontsevich–Soibelman, Huisken–
Ilmanen, Bray) plus four release works. A work at 11–42 manuscripts is a shared *toolkit*; a work at
17 owned by 17 manuscripts in one discipline is a shared *subfield*.

## Pair layers

A pair is an unordered pair of manuscripts; the count is shared titles.

| Shared titles | Pairs | Same-family | Cross-discipline |
|---|---|---|---|
| ≥1 | **3,668** | 389 | 1,979 |
| ≥2 | **1,133** | 364 | 234 |
| ≥3 | **700** | 347 | 61 |
| ≥5 | **419** | 296 | **6** |
| ≥10 | **197** | 173 | **0** |

Max pair overlap: **47** shared titles — the two manuscripts of family 068. **426** of 494
manuscripts share ≥1 title with a manuscript of another family.

Top pairs by shared titles: 47 `068×068` (same-family), 43 `004×006` (cross-family, both Number
theory), 38 `264×264`, 37 `034×034`, 36 `223×223`, 34 `267×267`, 34 `260×260`,
33 `267×267`, 33 `368×368`, 32 `238×238`, 31 `264×264`, 30 `260×260`. Ten of the twelve are
same-family pairs — the strongest bibliography overlap in the corpus is between sibling manuscripts
of one family, which is what a companion pair should look like.

## The discipline crossings

Cross-discipline pairs at ≥5 shared titles — **6 pairs over 9 families**, the complete list:

| Shared titles | Family pair | Disciplines |
|---|---|---|
| 9 | 217 × 281 | Probability and statistical mechanics × Mathematical physics |
| 9 | 217 × 281 | Probability and statistical mechanics × Mathematical physics |
| 6 | 086 × 154 | Real and complex analysis × Dynamical systems and ergodic theory |
| 5 | 041 × 357 | Algebraic and complex geometry × Differential geometry |
| 5 | 260 × 336 | Mathematical physics × Differential geometry |
| 5 | 260 × 346 | Mathematical physics × Differential geometry |

The two 217 × 281 rows are two distinct manuscript pairs — each family ships two manuscripts. At
≥10 shared titles the count is **0**.

The ≥1 layer is dominated by shared standards, and its discipline-pair histogram shows the shape of
the floor, not of a research program (pairs at ≥1 shared title, top 10):

| Pairs | Discipline pair |
|---|---|
| 658 | Algebraic and complex geometry × Algebraic and complex geometry |
| 312 | Probability and statistical mechanics × Probability and statistical mechanics |
| 199 | Algebraic and complex geometry × Number theory |
| 139 | Number theory × Number theory |
| 128 | Algebra × Algebraic and complex geometry |
| 115 | Mathematical physics × Mathematical physics |
| 113 | Algebraic and complex geometry × Topology |
| 106 | Differential geometry × Mathematical physics |
| 87 | Theoretical computer science × Theoretical computer science |
| 78 | Algebra × Number theory |

Same-discipline pairs are 1,689 of 3,668 at ≥1, 413 of 419 at ≥5, and 197 of 197 at ≥10. The
crossing rate falls monotonically as the threshold rises — 54% → 1.4% → 0% — which is the signature
of a shared-toolkit layer sitting on top of a discipline-structured research layer, not of an
arbitrary grouping.

## Clusters

A cluster is a connected component of the pair graph at a given threshold.

**At ≥1 shared title the graph does not partition the corpus.** 11 components, largest **436
manuscripts over 261 families and all 17 disciplines** (discipline counts: Probability and statistical
mechanics 57, Algebraic and complex geometry 56, Theoretical computer science 44, Number theory
37, Differential geometry 32, Mathematical physics 32, Combinatorics 27, Real and complex analysis
22, Operator algebras 21, Algebra 20, Topology 18, Partial differential equations 16, Dynamical
systems and ergodic theory 13, Group theory 13, Convex and metric geometry 12, Functional analysis
10, Mathematical logic 6). One shared title is a weak edge and it connects almost everything. Any
claim built on "one shared citation" is a claim about the Stacks Project.

**At ≥5 shared titles the clusters are discipline-shaped.** 89 components, all non-trivial, largest
34, **4** spanning ≥2 disciplines:

| Mss | Fams | Disciplines | Families | Composition |
|---|---|---|---|---|
| 34 | 14 | 1 | 033 034 035 036 037 046 051 054 056 057 058 065 066 068 | Algebraic and complex geometry 34 |
| 15 | 4 | 2 | 260 335 336 346 | Mathematical physics 11, Differential geometry 4 |
| 14 | 6 | 1 | 211 218 223 224 225 230 | Probability and statistical mechanics 14 |
| 9 | 5 | 1 | 002 004 006 010 030 | Number theory 9 |
| 8 | 4 | 1 | 102 105 106 117 | Theoretical computer science 8 |
| 7 | 3 | 1 | 311 313 318 | Topology 7 |
| 7 | 1 | 1 | 238 | Probability and statistical mechanics 7 |
| 7 | 5 | 1 | 074 077 078 079 080 | Real and complex analysis 7 |
| 6 | 3 | 1 | 221 222 235 | Probability and statistical mechanics 6 |
| 5 | 1 | 1 | 215 | Probability and statistical mechanics 5 |
| 5 | 1 | 1 | 331 | Functional analysis 5 |
| 5 | 3 | 2 | 041 356 357 | Differential geometry 3, Algebraic and complex geometry 2 |

The largest cluster is the birational-geometry / log-abundance block: 14 consecutive-numbered families
in one discipline, 34 manuscripts. The second is the spacetime-Penrose block — 11 manuscripts of
family 260 with the three Differential-geometry families 335, 336, 346, which is the clearest case in
the corpus of a discipline boundary cutting across one research program. The 041/356/357 cluster is
the same shape, smaller.

**At ≥10 shared titles, no cluster crosses a discipline boundary.** 67 components, largest **12**
(033 034 036 056, Algebraic and complex geometry), then 260 (10 mss, 1 family, Mathematical physics),
238 (7), 068 (7), 313+318 (6, Topology), 102+105 (5, Theoretical CS), 074+077+078 (5, Real and
complex analysis), 223+225 (5), 227 (5), 376 (5), 267 (4), 211 (4). **0** of 67 span ≥2 disciplines.

## Release-internal sharing

The release cites its own preprints by URL, and that layer has its own cluster structure. Rule: an
entry is release-labelled when its body contains `OpenAI Math Release`; its target is the
`preprints/<dir>/` component of the `\href{…pdf}` in the body — the rule `notes/links.tsv` records.

**432** release-labelled entries (393 in ledger-listed manuscripts), from **277** manuscripts,
pointing at **268** distinct targets; **80** targets are cited by ≥2 manuscripts. **203** manuscript
pairs share a cited release work, **19** pairs share ≥2, and **103** of the 203 pairs cross a family
boundary.

| Citing manuscripts | Release target |
|---|---|
| 11 | `Log-abundance-in-characteristic-zero-September-24-2026` |
| 7 | `Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026` |
| 6 | `Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026` |
| 5 | `The-spacetime-Penrose-inequality-and-enclosing-area-September-27-2026` |
| 4 | `A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026` |
| 4 | `Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026` |
| 4 | `Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026` |
| 4 | `The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026` |
| 4 | `The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026` |
| 3 | `A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026` |

The most-cited release works are release works, and the top of the list is the same birational-geometry
block that dominates the external cluster at ≥5. The internal layer is the sharpest available signal of
which results the release itself treats as load-bearing.

## Two entries, verbatim

`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/references.bib:106`

```bibtex
@misc{Stacks,
  author = {{The Stacks Project Authors}},
  title = {The {Stacks Project}},
  year = {2026},
  howpublished = {\url{https://stacks.math.columbia.edu}},
  note = {Continuously updated; accessed September 26, 2026},
  url = {https://stacks.math.columbia.edu},
```

`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/build/references.bib:407`

```bibtex
@misc{OpenAIMilneRationality2026,
  author = {{OpenAI}},
  title = {{Milne's rationality conjecture for abelian varieties}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf}{OAI:Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026}},
  year = {2026}
}
```

The second is the shape of a release-internal citation: author `OpenAI`, a title phrase as the entry
title, and the target carried by URL. It is why the title-phrase proxy in `notes/links.md` reaches 12
cross-family families while the href layer reaches 104.

## Sensitivity of the headline to the normalization rule

The accent guard is a choice, so the choice was tested against the headline. Rebuilt with the guard
removed (every accent macro folded, artifacts gone), over the same 521 files:

| Measure | Guarded (shipped) | Guard removed | Δ |
|---|---|---|---|
| Distinct works | 8,775 | 8,765 | -10 |
| Works shared ≥2 | 2,251 | 2,254 | +3 |
| Pairs ≥1 | 3,668 | 3,676 | +8 |
| Cross-discipline pairs ≥1 | 1,979 | 1,981 | +2 |
| Pairs ≥5 | 419 | 419 | **0** |
| Cross-discipline pairs ≥5 | 6 | 6 | **0** |
| Pairs ≥10 | 197 | 197 | **0** |
| Cross-discipline pairs ≥10 | 0 | 0 | **0** |

The normalization knob moves the weak layer by 8 pairs out of 3,668 (0.22%) and moves the strong layer
by nothing. The finding is not an artifact of the accent rule.

## What the graph does not say

- **A family's result is not inferable from its bibliography.** A manuscript citing Kontsevich–Soibelman
  is not a manuscript about log abundance; the same work sits in 11 manuscripts across the
  birational-geometry block. Bibliography is a record of what a manuscript leaned on, and this page
  infers nothing about any family's theorem from it.
- **Edges are untyped.** Why a manuscript cites another — builds-on, contrasts-with, refutes,
  acknowledges — is recorded nowhere in the release. A shared work is a citation-choice overlap, not a
  dependency, and the 103 cross-family internal pairs are not consequence edges.
- **A cluster is not a research program.** It is a connected component of a thresholded overlap graph.
  Membership at ≥5 is a statement about 5 shared bibliography titles, and the discipline composition of
  a cluster is a statement about the release's grouping, not about mathematics.
- **The disciplines are not refuted, and this page does not claim they are validated either.** The
  release's grouping is the release's own; the graph shows that strong bibliography overlap respects
  it, which is evidence the grouping tracks something in the bibliographies. It is not evidence the
  grouping is correct, and 4 of 89 clusters at ≥5 do cross a boundary.

## Not checked

- **225 of 719 manuscripts are invisible to this method.** They ship no `.bib`; all 225 carry an
  inline `\begin{thebibliography}` with `\bibitem` entries, and **0** carry neither. **5** manuscripts
  have both layers. Every count here is over 494 manuscripts, and a discipline-crossing claim that
  excludes 31% of the corpus is a claim about the BibTeX layer. The inline layer was not parsed —
  `\bibitem` titles are not normalized here, so the 225 contribute no titles, no pairs, and no clusters.
- **Work identity is title-only.** Author, year, and venue are not used, so two editions of one book
  under different titles are two works, and two different works with the same title are one. No entry
  was checked against an external bibliography, and no work was identified in the literature.
- **No entry was validated.** Entries are counted by `^\s*@\s*(\w+)\s*\{`; commented-out entries are
  included, and no check was made that an entry parses as BibTeX or that its fields are correct.
- **The cited-key test is a key match in a `\cite…{…}` locator** over the manuscript's own `.tex`
  tree. `\nocite{…}` is not matched by the pattern, a key cited in a file outside the manuscript's
  directory is not counted, and a key cited in a `.bib`-adjacent macro file is not attributed.
- **The 4 cross-discipline clusters at ≥5 were not read manuscript by manuscript.** The 260/335/336/346
  and 041/356/357 memberships are graph output; no manuscript's introduction was read to check whether
  the overlap is a shared subfield or a shared textbook.
- **No comparison with the Lean layer.** Clusters were not cross-tabulated against tier, `mainres`,
  `chal`, or scope notes, so nothing here says whether a bibliography cluster is more likely to be
  formalized.
- **The 23 manuscripts sharing no title with any other were not read**, and the reason — a small
  bibliography, an unusual topic, or a normalization miss — is not measured.
- Cluster membership is computed over manuscripts, not families; a family with two manuscripts
  contributes two nodes, so cluster sizes are manuscript counts and family counts are reported
  separately rather than derived from one another.

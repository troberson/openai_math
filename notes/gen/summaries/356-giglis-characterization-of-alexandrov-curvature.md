[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 356](../index/differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md)

# 356 — Gigli's characterization of Alexandrov curvature

[Index page](../index/differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md)

## Original CONTENTS.md summary

[S1:8649] (family entry):

> **356. Gigli's characterization of Alexandrov curvature.** Proves Gigli's conjecture: in every integer dimension $`n \ge 2`$, Alexandrov curvature at least $`\kappa`$ is characterized by the full-support $`\mathrm{RCD}((n-1)\kappa,n)`$ condition with reference measure $`\mathcal H^n`$ and distributional sectional curvature at least $`\kappa`$ in the original global test classes. The RCD condition is unreduced.

[S2:812] carries the `\resultentry` with two manuscripts.
Manuscript 1 [S3] (the characterization, the headline result) and
manuscript 2 [S4] (a supporting weak-Hessian lemma). The scope note
names **only** manuscript 2 [S6:5] and states the formalized result


> The formalization transfers a weak Hessian upper bound to every prescribed minimizing geodesic in an $`\mathrm{RCD}(K,N)`$ space with finite $`N>1`$. If a bounded globally Lipschitz function $`F`$ has weak Hessian bounded above by $`G`$ times the metric, where $`G`$ is bounded and continuous, then every constant-speed geodesic $`\gamma:[0,1]\to X`$ satisfies $`(F\circ\gamma)''\le G(\gamma)\,d(\gamma(0),\gamma(1))^2`$ in the distributional sense. Constant geodesics are included. The space is complete and separable with full support and measure finite on bounded sets; compactness and metric nonbranching are not assumed. [S6:9]

## Undergraduate summary

Geometer's way of saying "how curved is this space?" There are
several of them, and they agree in familiar cases — but proving they
agree in the most general "Alexandrov" spaces (spaces curved like a
mountain at least as much as $`\kappa`$) has been a long-standing
problem.

**Gigli's conjecture** proposed that, in any dimension at least two,
an Alexandrov space of curvature at least $`\kappa`$ is *exactly* a
space satisfying two modern, analytic conditions: (1) it is an
**RCD** space (a condition capturing "non-negative Ricci curvature"
for metric spaces, in its strongest "unreduced" form), and (2) its
**sectional curvature** (the "all directions" curvature) is at least
$`\kappa`$ in a distributional sense.

This paper (manuscript 1) **proves the conjecture**: the two
analytic conditions together pin down the Alexandrov condition
exactly, in every dimension $`\ge 2`$, with the RCD condition in its
strongest form and the reference measure being the natural volume.

Manuscript 2 is a **supporting lemma** — a technical ingredient
used in the proof, about how a bound on a function's second
derivatives (its **Hessian**) along one type of curve extends to
*every* shortest path (geodesic). The release formalizes *that*
lemma, not the headline characterization.

## Graduate summary

**Main theorem (characterization, manuscript 1)** [S3:8–15, S2:812].
For every integer $`n \ge 2`$ and $`\kappa \in \mathbb R`$, a
complete separable metric space is an $`n`$-dimensional Alexandrov
space of curvature at least $`\kappa`$ if and only if, with reference
measure $`\mathcal H^n`$, it is a full-support
$`\mathrm{RCD}((n-1)\kappa, n)`$ space whose distributional
sectional curvature is at least $`\kappa`$ in Gigli's original global
test classes. This resolves Gigli's characterization conjecture in
dimensions at least two.

**Formalized lemma (manuscript 2)** [S4:8–14, S6:9].
On a full-support $`\mathrm{RCD}(K,N)`$ space with
$`1 < N < \infty`$, a bounded globally Lipschitz function whose
distributional Hessian is bounded above by a bounded continuous
function $`G`$ satisfies the corresponding second-derivative
inequality — in the distributional sense — along **every** minimizing
geodesic, including constant geodesics. The space is assumed complete
and separable with full support and measure finite on bounded sets;
compactness and metric nonbranching are **not** assumed.

**The formalized statement** [S6:9, S5].
The scope note selects the weak-Hessian lemma [S6:9], *not* the
headline characterization. The comparator stub `WeakHessian.lean`
(233 lines) states `theorem every_geodesic` [S5:220] with the `sorry`
at [S5:227]. The `main_results` entry [S7:1811–1813] resolves the
declaration `OAI.WeakHessian.every_geodesic` to
`lean/OAI/Geometry/WeakHessian/Main.lean` [S8].

## History of the conjecture

**Gigli's characterization conjecture** is a central open problem in
metric measure geometry, proposed by Nicola Gigli in his program for
understanding curvature-dimension conditions. The **RCD**
condition (Lott–Sturm–Villani's Ricci curvature lower bound, plus a
"reduced" versus "unreduced" distinction) and **Alexandrov**
sectional curvature are two different ways of encoding curvature for
spaces that lack a smooth structure. The conjecture asks whether, in
the strong (Alexandrov) section, they are two faces of the same coin.

The **RCD$`(K,N)`$** condition, in its unreduced form, captures a
Ricci-curve curvature lower bound $`K`$ with dimension upper bound $`N`$;
the reference-measure requirement (that the measure be the natural
$`\mathcal H^n`$) and the "original global test classes" (Gigli's
definition of distributional sectional curvature, as opposed to later
reduced variants) are the load-bearing precision of the statement.

The **novel contribution** is the proof of the equivalence in every
dimension $`n \ge 2`$ in the unreduced setting [S3]. Manuscript 2
[S4] splits out a supporting analytic lemma — that a weak Hessian upper
bound propagates to every geodesic, not just a.s. one — which is the
piece the release chose to formalize.

**Prior (my training data, not this repo).** As of my training
cutoff, Gigli's characterization conjecture for Alexandrov spaces in
dimensions at least two, in the unreduced RCD setting with the
original global test classes, is a genuine open problem in metric
measure geometry. The reduced (or measure-theoretic) variants are
better understood; the full unreduced characterization with the
Alexandrov lower bound is the claimed novelty. I cannot verify the
metric-geometric analysis independently from training alone.

## Consequences

- **Gigli's characterization conjecture is resolved in every
  dimension $`n \ge 2`$** [S3:8–15, S2:812]: Alexandrov curvature at
  least $`\kappa`$ is characterized by the unreduced full-support
  $`\mathrm{RCD}((n-1)\kappa,n)`$ condition plus distributional
  sectional curvature at least $`\kappa`$ in the original global test
  classes.
- **The RCD condition is unreduced** [S3:8–15, S2:812]: the
  characterization holds in the strongest form of the Ricci lower
  bound, not a reduced variant.
- **The weak-Hessian lemma is the formalized piece, not the
  headline** [S6:9, S5, S7:1811–1813]: the release proves the
  supporting lemma (Hessian bounds propagate to every geodesic) and
  leaves the characterization itself as manuscript-only.
- **Compactness and metric nonbranching are not assumed** [S6:9]:
  the formalized lemma extends the a.s. geodesic statement to every
  geodesic under only completeness, separability, full support, and
  local finiteness of the measure.

## Section skeleton

Two manuscripts, both with `build/main.tex` roots.
Manuscript 1 [S3] (characterization, 40 lines): 6 `input` files
[S3:18–23]: `introduction`, `preliminaries`, `forward`,
`heat-index`, `frames`, `comparison`, then an inline
`\section{Conclusion of the proof}` [S3:24] with a
`Proof of Theorem` block, plus a BibTeX `references.bib`.
Manuscript 2 [S4] (weak-Hessian lemma, 23 lines): 5 `input` files
[S4:16–20]: `introduction`, `calculus`, `drift`, `curvature-change`,
`every-geodesic`, plus a BibTeX `references.bib`. **No verification
bundles.**

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S6:9], one comparator stub [S5], **one** `main_results` entry
[S7:1811–1813], and one proved OAI tree [S8]. The T3 shape is "scope
note, comparator stub, `main_results` entry, and proved OAI tree (0
`sorry`)."

The formalization is **asymmetric with the headline**: the scope note
names only manuscript 2 [S6:5] (the weak-Hessian lemma), and the
formalized statement is that lemma [S6:9], not the characterization
in manuscript 1 [S3]. The comparator stub `WeakHessian.lean` (233
lines) carries the full machinery — the curve/test-plan/Sobolev/Hessian
setup, the $`\sigma`$ and $`\tau`$ coefficients, the unreduced
$`\mathrm{CD}(K,N)`$ and $`\mathrm{RCD}(K,N)`$ definitions,
and the second-distributional-derivative conclusion — and states
`theorem every_geodesic` [S5:220] with the `sorry` at [S5:227].

The `main_results` entry [S7:1811–1813] resolves the declaration
`OAI.WeakHessian.every_geodesic` to
`lean/OAI/Geometry/WeakHessian/Main.lean` [S8] (59 lines), the entry
point of a 542-file OAI tree carrying 0 `sorry`. The reading is of
source text only.

## Coverage

The ledger row `fam=356` [S9] records the tier and the counts:
`tier=T3`, `paps=2`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=611`, `verification=0`, `trace=`. The T3
shape is "scope note, comparator stub, `main_results` entry, and
proved OAI tree (0 `sorry`)." The single comparator stub carries 1
`sorry`. The shape flags are `shapes=classification`,
`resolves_named=1`, `counterex_broad=0`, `covmd=0` — a
classification/characterization family (Gigli's characterization
conjecture), with a named conjecture in the title, with no
counterexample. Note `paps_form=1`: only manuscript 2
(the weak-Hessian lemma) appears in `formalization.yaml`'s `sources:`
list; the headline characterization [S3] does not — the formalized
statement [S6:9] is the lemma, so the per-manuscript formalized flag
is 1 (the lemma's manuscript), not 2.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8649] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 356 at [S2:812] |
| S3 | [`preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/build/main.tex`](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/build/main.tex) | 40 | the `\documentclass` root (manuscript 1, the characterization) — title [S3:3], date [S3:5], abstract [S3:8–15] |
| S4 | [`preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/main.tex`](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/main.tex) | 23 | the `\documentclass` root (manuscript 2, the formalized lemma) — title [S4:3], date [S4:5], abstract [S4:8–14] |
| S5 | [`lean/ComparatorChallenges/WeakHessian.lean`](../../../lean/ComparatorChallenges/WeakHessian.lean) | 233 | comparator stub — 233 lines, `theorem every_geodesic` [S5:220], `sorry` [S5:227] |
| S6 | [`lean/docs/356.md`](../../../lean/docs/356.md) | 15 | scope note — names only manuscript 2; Scope at [S6:9], comparator link at [S6:15] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry — [S7:1811–1813] |
| S8 | [`lean/OAI/Geometry/WeakHessian/Main.lean`](../../../lean/OAI/Geometry/WeakHessian/Main.lean) | 59 | proved OAI tree entry — 59 lines, 0 `sorry`; 542 files under the tree |
| S9 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=356`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

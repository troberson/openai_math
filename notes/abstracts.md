# Abstract comparison — `overview.tex` vs the manuscript abstracts

Every manuscript in `preprints/` ships its own `\begin{abstract}` environment, and the ledger's
claim-shape tags (`resolution`, `bound`, `counterexample`, `conditional`, …) are keyword rules run
over the abstract text in `overview.tex` — not over the manuscripts. This file compares the two
texts per family and records what the comparison shows.

**The rule that yields every count here:** `python3 notes/scripts/compare_abstracts.py` [S33] — it
parses the 372 `\resultentry` abstracts out of `overview.tex` [S1], extracts every
`\begin{abstract}` block from every manuscript's LaTeX, normalizes both, and compares them. It
writes nothing; `--tsv` writes `notes/abstracts.tsv` [S31] (one row per family, 372 rows) after its
reconciliation gates pass, and `--mutant` proves the gates discriminate. All counts below are from a
fresh run of that report.

## The headline

**No manuscript abstract is the overview abstract.** Over all 722 manuscript comparisons:
**0 identical, 0 abridged, 722 divergent.** Over the 372 family best matches: **0 identical,
0 abridged, 372 divergent.**

The overview abstract is a rewritten third-person paraphrase in every case. The dominant transform
is `We prove X` → `Proves X`, plus sentence-level re-combination. Family 198 is the closest the
corpus comes — overview “Constructs a finite-dimensional complex algebra whose finite-dimensional
modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension
conjecture.” [S1] against manuscript “We construct a finite-dimensional complex algebra whose
finite-dimensional modules have unbounded finite projective dimensions. This disproves the little
finitistic-dimension conjecture.” [S2]

Even here the relation is `divergent`, not `abridged`: the overview deletes `We construct`, so the
shorter string is not a contiguous substring of the longer one.

So the bead's premise is confirmed: the claim-shape tags are keyed to a paraphrase. What the tags
*miss* is smaller than the paraphrase suggests — see the tag-level section — but the direction of
the error is systematic, and the `conditional` tag is where it bites.

## What was compared

- **Units.** Manuscript-level: 722 comparisons (one per manuscript, against its family's overview
  abstract). Family-level: 372 comparisons (the best-matching manuscript per family). Tag-level:
  the ledger's shape rules [S32] run over the overview abstract, and re-run over the union of the
  family's manuscript abstracts.
- **Abstract environments: 725 over 722 directories.** Every one of the 722 manuscript directories
  contains at least one abstract; three ship two — family 057
  (`A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026`,
  `build/source/main.tex` and `build/source/inertia.tex`), family 039
  (`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026`, `build/main.tex` and
  `build/provenance/companion/main.tex`) and family 056
  (`Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-5-2026`,
  `build/main.tex` and `build/termination-generalized-lc-kahler-fourfolds.tex`). The `abstract`
  column in `notes/sources.tsv` is a 0/1 **flag** per directory, not an occurrence count, so it
  reads 722 and cannot show this.
- **Normalization is lossy, deliberately.** Comments, the abstract environment markers,
  `\label`/`\ref`/`\cite`-family macros, generic `\newcommand`-family macros, math delimiters,
  braces, `~` and `\\` are stripped and whitespace collapsed. This is why the relation classes are
  floors: a manuscript that differs from the overview only in markup counts identical, and a macro
  adjacent to punctuation leaves a space that no overview text contains, so such a pair can never
  read `identical` (it reads `abridged`). Nothing here claims semantic equivalence — the checker
  compares strings.

## Ratio distribution

`ratio` is `difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()` [S33] over the normalized
strings — character-level similarity, not meaning.

| unit | n | min | p10 | median | p90 | max |
|---|---|---|---|---|---|---|
| manuscript-level | 722 | 0.007 | 0.029 | **0.126** | 0.448 | 0.989 |
| family-level best match | 372 | 0.011 | 0.074 | **0.236** | 0.610 | 0.989 |

| bucket (<0.30 / 0.30–0.50 / 0.50–0.70 / 0.70–0.90 / ≥0.90) | manuscript-level | family-level |
|---|---|---|
| count | 569 / 97 / 32 / 20 / 4 | 227 / 90 / 32 / 19 / 4 |

Four families have a best match at ≥0.90: **005** (0.972), **098** (0.901), **198** (0.989),
**368** (0.929). Eighteen families have a best match below 0.05: 021, 027, 053, 081, 093, 124, 126,
128, 174, 206, 214, 231, 234, 261, 264, 275, 361, 373. Label the unit when quoting the floor:
counting per manuscript instead of per family, 87 of the 722 comparisons fall below 0.05.

## Tag-level: what the shape rules see in each text

`ovfam` = families whose **overview** abstract fires the shape (this is what the ledger records);
`msfam` = families whose **union of manuscript abstracts** fires it; `man722` = manuscripts that
fire it, which is the control for union inflation (a 14-manuscript family gets 14 chances to flag a
shape, so `msfam` ≥ `man722` by construction and the comparison to `ovfam` must be read through
`man722`).

| shape | ovfam | msfam | man722 | ov-only | ms-only |
|---|---|---|---|---|---|
| bound | 139 | 162 | 290 | 26 | 49 |
| classification | 34 | 43 | 71 | 4 | 13 |
| conditional | 5 | 10 | 15 | 3 | 8 |
| counterexample | 44 | 52 | 69 | 13 | 21 |
| density | 20 | 32 | 44 | 1 | 13 |
| partial | 42 | 73 | 102 | 7 | 38 |
| resolution | 144 | 127 | 153 | 78 | 61 |
| undecidability | 4 | 21 | 24 | 2 | 19 |
| uniform | 161 | 209 | 343 | 24 | 72 |

**282 of 372 families have at least one shape disagreement between the two texts; 90 have none.**
Of the 282, 147 are single-manuscript families and 135 are multi-manuscript families.

The direction is not "the union flags more". Per manuscript, the overview under-flags every shape
except `resolution`, which it **over**-flags: 144 of 372 families (39%) call a resolution in the
overview, against 153 of 722 manuscripts (21%). The overview is written to name a solved problem —
it uses `resolves`, `answers`, `settles`, `proves the … conjecture` at roughly twice the manuscript
rate, and `undecidability` language at a fifth of it (4 families vs 24 manuscripts). The
`resolution` tag and the `resolves_named` column are keyed to the paraphrase's rhetoric, not to the
manuscripts' claims.

## Conditional disagreements

11 families disagree on the `conditional` tag: 3 flagged by the overview only (125, 244, 282) and 8
by a manuscript only (034, 046, 065, 140, 216, 218, 238, 260). Each entry states which text the tag
should read.

**034 — Log abundance and effective Iitaka fibrations.** *Read the manuscript.* The overview
presents the hypothesis as a method: “Using logarithmic Iitaka subadditivity, proves log abundance
in every dimension for normal compact K\"ahler log canonical pairs with effective rational
boundary” [S1]. The manuscript states it as an assumption: “Assume logarithmic Iitaka subadditivity
for surjective morphisms with connected fibers between smooth projective complex varieties with
compatible reduced simple normal crossing boundaries. We prove log abundance for normal irreducible
compact Kähler spaces in every dimension” [S17]. A third manuscript in the family is conditional in
its own title and is absent from the overview: “Assuming orbifold Iitaka subadditivity, the
specified pseudo-effective fourfold minimal model program, and abundance for nef fourfold adjoints
of nonnegative Kodaira dimension, we prove the existence of good minimal models” [S18]. The overview
carries 14 manuscripts in about four sentences; the conditional result is not one of them.

**046 — Counterexamples to Shafarevich holomorphic convexity.** *Read the overview.* The manuscript
hit is “even under the large-fundamental-group hypothesis” [S19], which is the hypothesis of the
*conjecture being disproved*, not of the theorem: “so this disproves Shafarevich's
holomorphic-convexity conjecture even under the large-fundamental-group hypothesis” [S19]. The
result is a construction with no assumption. The overview is right and the manuscript text is the
false positive.

**065 — Virasoro constraints for complete intersections and projective bundles.** *Read the
manuscript; the overview is faithful in substance.* Manuscript: “Assuming the full constraints on
the base, the conclusion includes every genus, each individual integral curve class, and all
cohomology insertions, including primitive and odd classes.” [S20] Overview: “The constraints also
pass from any smooth projective complex base satisfying them to the projectivization of every
algebraic vector bundle of rank at least two” [S1] — the same conditional, phrased with `satisfying`,
which the rule does not match.

**125 — The approximation threshold for metric $k$-median.** *Read the manuscript.* The overview
flag is “Assuming $P\ne NP$, the optimal infimum approximation factor is $1+2/e$.” [S1] The
manuscript that carries it says “Under \(P\ne NP\), the infimum approximation factor in this model
is therefore \(1+2/e\).” [S21] — `Under P≠NP` is not in the rule's vocabulary, so the manuscript
side reads unconditional. The overview is faithful; the rule is the gap.

**140 — Memory–sample lower bounds for noiseless Gaussian regression.** *Read the overview.* Both
manuscript hits are the technical term, not a hypothesis: “we bound the information in a finite
message $W$ formed from exact Gaussian measurements, conditional on an independent projection
revealed only to the analyst” [S22] and “increases the remaining conditional information by at most
\(Cd\)” [S23]. `TECH_AFTER` [S32] drops `conditional expectation/law/probability/measure/
distribution/density` within 60 characters; `conditional on an independent projection` and
`conditional information` are not in that list.

**216 — Critical logarithmic corrections and BKT scaling for the planar XY model.** *Read the
manuscript; the overview is faithful.* Overview: “Critical center-magnetization and spin-field
conclusions retain their stated height, renormalization, and field-input assumptions.” [S1]
Manuscript: “Assuming the stated critical-height, local-renormalization, and spin-field inputs from
the companion papers, we determine the center magnetization of the planar XY model in a square with
aligned boundary spins at its mass-defined critical threshold.” [S24] The overview says the same
thing in a plural noun the rule does not match (see the rule-gap section).

**218 — Conformal universality for weakly interacting and disordered Ising models.** *Read the
manuscript.* “Assuming the stated deterministic critical-reference estimates, we prove that the
relative second moment of the quenched critical spin correlation … grows as $(\log r)^{1/4+o(1)}$”
[S25]. The overview does not mention that result at all, so the conditional half of the family is
invisible in the text the tag reads.

**238 — Optimal logarithmic mixing of the Thorp shuffle.** *Read the overview.* The manuscript hit
is a technical adjective in a sibling manuscript: “the conditional permutation of the remaining
labels approaches uniform in expected total variation as $d\to\infty$, uniformly in the initial
layout” [S27]. The overview describes only the
full-deck result: “Proves that the Thorp shuffle randomizes $N=2^d$ labeled cards in $\Theta(\log N)$
physical shuffles” [S1], and the manuscript of that result says “We prove that the Thorp shuffle on
$2^d$ cards mixes in $\Theta(d)$ complete shuffles” [S26] — consistent, since $N = 2^d$.

**244 — The partition principle does not imply choice.** *Read the manuscript.* Overview: “Assuming
ZF is consistent, constructs a model in which every surjective image of a set injects into that set,
yet the axiom of choice fails.” [S1] Manuscript: “We prove that the Partition Principle does not
imply the Axiom of Choice: if ZF is consistent, then so is ZF with the Partition Principle, Choice
for ordinal-indexed families, and the negation of the Axiom of Choice.” [S28] Same content;
`if ZF is consistent` is not in the rule's vocabulary.

**260 — Spacetime Penrose inequalities and rigidity.** *Read the manuscripts.* Four of its 13
manuscripts fire, in four different files: “Under the stated energy, decay, and trapping
hypotheses, we prove the sharp charged spacetime Penrose upper-area inequality” [S29], “under the
stated outermostness and decay hypotheses” [S34], “We assume that the hyperbolic metric four-flux
is future timelike” [S35], and “Under the stated horizon hypotheses, equality for the neutral
inequalities reconstructs the original exterior data as spacelike slices of Schwarzschild
spacetime” [S36]. The overview states the same hypotheses in plural nouns — “under dominant
energy, weak future trapping, positive enclosing area, and the stated decay assumptions” [S1] —
which the rule misses on the overview side.

**282 — Scale-to-conformal enhancement in four-dimensional QFT.** *Read the manuscript for the
hypothesis list; the overview is faithful.* Overview: “Under the stated bounded-local-net and
field-reconstruction hypotheses, proves that scale symmetry implies local conformal symmetry” [S1].
Manuscript: “Under these hypotheses, the stress tensor admits a symmetric, conserved, traceless
improvement with unchanged translation and Lorentz charges.” [S30] — `under these hypotheses` is not
matched (`under the … hypothes` requires the article), and the manuscript's hypothesis list is
enumerated in prose the overview compresses.

Net: of the 11 disagreements, **5 are real conditionals the overview presents unconditionally**
(034, 065, 216, 218, 260), **3 are rule artifacts on the manuscript side** (046, 140, 238), and
**3 are overview flags whose manuscript phrasing the rule misses** (125, 244, 282). That is the
conditional-tag lesson repeating at a larger sample: a keyword rule over a paraphrase flags a
number of families that is not the number of conditional results.

## Rule gaps this pass found

The `ASSUME` vocabulary in `notes/scripts/build_catalog.py` [S32] misses four phrasings that occur
in these abstracts:

1. **Bare plural `assumptions`.** `ASSUME` matches `assumption` only inside
   `under the … assumption`, and `\bassuming\b` has no boundary inside `assumptions`. Families 216
   and 260 state assumptions in the overview with the plural noun and are unflagged.
2. **`if ZF is consistent`** (244) — relative consistency stated as a conditional clause.
3. **`Under P≠NP`** (125) — `under the … hypothes` requires the noun.
4. **`under these hypotheses`** (282) — the pattern requires the article `the`.

`TECH_AFTER` also under-drops: `conditional on an independent projection` and `conditional
information` (140) and `conditional permutation` (238) are technical uses that pass the filter.

Recorded as a decision point, not applied: widening `ASSUME` for (1)–(4) would move families into
the `conditional` ledger column and change `notes/t0-triage.md`'s first-match buckets for
`conditional`-tagged families, which is the same taxonomy-change risk that kept `resolves_named`
and `counterex_broad` out of `SHAPES` [S32]. The bead asked which text the tag should read, not for
a new rule; the answer is per family, above.

## Where a low ratio is expected: the overview is a synthesis

For multi-manuscript families the overview is a merge, so a low per-manuscript ratio is not a
misstatement. Two clean cases:

**368 — The three-dimensional Ball--Evans approximation problem** (best match 0.929). Manuscript 1:
“We resolve the three-dimensional Ball--Evans approximation problem for $1\le p\le2$.” [S5]
Manuscript 2: “We resolve the three-dimensional Ball--Evans approximation problem for every finite
$p>2$.” [S6] Overview: “Resolves the three-dimensional Ball--Evans approximation problem: every
$W^{1,p}$ homeomorphism between arbitrary bounded domains in $\mathbb R^3$, for $1\le p<\infty$, is
a strong $W^{1,p}$ limit of smooth diffeomorphisms onto the same target.” [S1] The merge is correct.

**240 — Shelah's eventual categoricity conjecture** (best match 0.406). The family ships a ZFC
theorem and a CH-based obstruction, and the overview carries both in three sentences: “Proves
Shelah's eventual categoricity conjecture in ZFC: for each bound on the L\"owenheim--Skolem number,
a uniform threshold makes categoricity of an abstract elementary class in one cardinal above that
threshold imply categoricity throughout the same tail.” [S1] … “Under the continuum hypothesis, a
proposed specific Hanf threshold need not suffice.” [S1] The CH manuscript says “Assuming the
continuum hypothesis, we construct an abstract elementary class with L\"owenheim--Skolem number
\(\aleph_0\) that is categorical in every sufficiently large cardinal but has at least two
nonisomorphic models of cardinality \(\beth_{\omega_2}\)” [S7] and “Consequently, if ZFC is
consistent, the prescribed-threshold form of Shelah's categoricity conjecture is not provable in
ZFC.” [S7] The ZFC manuscript says “We prove Shelah's eventual categoricity conjecture for abstract
elementary classes in ZFC.” [S8] The overview's compression is faithful; the 0.406 ratio is the
merge, not an error.

The corollary matters for reading the floor: a family-level ratio near 0.02 usually means *the
overview describes a different manuscript than the one being compared*, not that it contradicts it.

## Largest divergences (8 lowest family ratios)

| fam | ratio | overview [S1] | manuscript |
|---|---|---|---|
| 093 | 0.011 | “Proves a dimension-free logarithmic Sobolev inequality for centered log-concave densities with uniformly subgaussian linear marginals, with constant bounded by a universal multiple of the squared linear subgaussian parameter.” [S1] | “We prove that every centered log-concave probability measure with a Lebesgue density on $\mathbb R^n$ and linear subgaussian parameter $a$ satisfies $\operatorname{Ent}_\mu(f^2)\le Ca^2\int|Df|^2\,d\mu$ for compactly supported smooth $f$, with one universal constant $C$.” [S9] |
| 373 | 0.012 | “An optimal three-particle Coulomb configuration need not be a deterministic function of the first particle, even for smooth identical spatial densities.” [S1] | “We construct a smooth compactly supported probability density on \(\R^3\), with a smooth compactly supported square root, for which the three-marginal Coulomb transport minimum is not attained by any pair of measure-preserving Borel maps.” [S10] |
| 231 | 0.014 | “On every infinite connected locally finite simple unweighted graph, the free uniform spanning forest is a factor of independent vertex labels, by one isomorphism-equivariant rule using no root.” [S1] | “We prove that the free uniform spanning forest is a factor of IID on every infinite connected locally finite simple unweighted graph. One Borel rule works for all such graphs and uses no root, answering affirmatively the general factor question for unimodular random graphs.” [S11] |
| 214 | 0.015 | “Proves $p_c<p_u$ for Bernoulli bond percolation on every infinite connected locally finite nonamenable quasi-transitive graph, resolving the Benjamini--Schramm nonuniqueness conjecture.” [S1] | “We prove the bond-percolation nonuniqueness conjecture of Benjamini and Schramm: every infinite connected, locally finite, nonamenable quasi-transitive graph has a nonempty interval of parameters for which Bernoulli bond percolation almost surely has infinitely many infinite clusters.” [S12] |
| 234 | 0.016 | “Gives an exact variational formula for the limiting pressure of orthogonally invariant Ising spin glasses at every fixed temperature, both almost surely and in expectation.” [S1] | “We determine the limiting pressure of an Ising spin glass with Haar orthogonal eigenvectors, a compact limiting spectral law, and no asymptotic outliers, at every fixed temperature. The pressure converges in expectation and almost surely to a variational formula.” [S13] |
| 021 | 0.017 | “Answers Jacobsthal's quadratic-bound question: every interval of $Ck^2$ consecutive integers contains an integer coprime to any prescribed positive integer with at most $k$ distinct prime divisors, for an absolute constant $C$.” [S1] | “Let $h(k)$ be the least integer such that every interval of $h(k)$ consecutive integers contains an integer coprime to any prescribed positive integer having at most $k$ distinct prime divisors. We prove $h(k)\ll k^2/(\log\log(3k))^2$, giving an affirmative answer to Jacobsthal's quadratic-bound question.” [S14] |
| 027 | 0.018 | “Resolves the determinant-one curve case of Litt's integral-density question.” [S1] | “We prove potential Zariski density of integral points on $\SL_r$-character varieties of smooth complex curves in every rank.” [S15] |
| 128 | 0.019 | “Gives a deterministic polynomial-time algorithm constructing a common superstring of length at most twice the optimum for every finite family of explicitly represented strings.” [S1] | “We give a deterministic algorithm that, for every finite family of explicitly represented ordinary strings, outputs a common superstring of length at most twice the optimum in time polynomial in the total encoded input size, including symbol labels.” [S16] |

Reading these eight, the pattern is consistent: the overview states the **conclusion in the
catalog's own vocabulary** (named conjecture, named question, the inequality in display form) and
drops the manuscript's hypotheses, constants, and scope sentences. 021 is the sharpest: the
manuscript proves $h(k)\ll k^2/(\log\log(3k))^2$ and the overview states the weaker corollary
$Ck^2$ without the logarithmic factor. Nothing here is a contradiction; the overview is a weaker,
shorter statement of the same result, written for a reader choosing which family to open.

## Consequence for the ledger

- The claim-shape tags read the overview paraphrase. For a family whose overview drops a manuscript
  (034, 218), the tags cannot see the shapes in the dropped manuscript at all.
- `resolution` and `resolves_named` are keyed to the paraphrase's rhetoric and over-flag relative to
  the manuscripts (144 of 372 families vs 153 of 722 manuscripts).
- `conditional` is the tag where paraphrase and rule interact worst: 11 families disagree, and only
  5 of them are real conditionals the overview presents unconditionally.
- `notes/abstracts.tsv` [S31] is the per-family record — 372 rows with the best-match ratio,
  relation, matched file, both shape sets, the disagreement sets, and the two conditional flags.
  Prose entries above cover the informative subset (4 near-identical, 8 largest divergences, 2
  syntheses, 11 conditional disagreements); the other divergent families are in the TSV, not in
  prose. That is a recorded decision point, not an omission.

## Not checked

Nothing here reads a manuscript body — only the `\begin{abstract}` blocks and the overview
abstracts. `difflib` ratio is character-level similarity, not semantic entailment: a low ratio says
the strings differ, and a high ratio says they are close, and neither says a manuscript proves what
the overview states. The normalization is lossy in both directions (markup stripped, math
delimiters stripped), so the relation classes are floors and a macro adjacent to punctuation can
never read `identical`. The tag-level comparison uses the ledger's rules re-run over manuscript
text; it does not re-run `resolves_named` or `counterex_broad`, whose input scope is title +
abstract. No family was checked against its Lean formalization in this pass, and nothing was built:
no `lake`, no `lean`, no comparator.

`python3 notes/scripts/verify_abstracts.py --mutant` [S37] resolves every `[S#]` marker in this page
against the shipped files and checks every quotation, verbatim modulo whitespace, against the text
its marker's file carries — the `\resultentry` abstracts for `overview.tex` [S1], the
`\begin{abstract}` bodies for a manuscript, the whole file for the TSV and the scripts. It writes
nothing. It reports no unanchored quotations: every quotation on this page carries a marker.

## Sources

Markers in the body are `[S#]`. Paths are repo-relative. Overview quotations are marked `[S1]`.

| # | File | What it carries |
|---|---|---|
| S1 | `overview.tex` | The 372 `\resultentry` abstracts the ledger's shape tags read. |
| S2 | `preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/paper.tex` | Family 198 manuscript abstract. |
| S5 | `preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/main.tex` | Family 368, $p\le2$ half. |
| S6 | `preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/main.tex` | Family 368, $p>2$ half. |
| S7 | `preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/sections/00-introduction.tex` | Family 240, CH obstruction. |
| S8 | `preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/build/main.tex` | Family 240, ZFC theorem. |
| S9 | `preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/main.tex` | Family 093. |
| S10 | `preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/build/paper.tex` | Family 373. |
| S11 | `preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/paper.tex` | Family 231. |
| S12 | `preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/main.tex` | Family 214. |
| S13 | `preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex` | Family 234. |
| S14 | `preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/main.tex` | Family 021. |
| S15 | `preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/main.tex` | Family 027. |
| S16 | `preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/paper.tex` | Family 128. |
| S17 | `preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-4-2026/build/main.tex` | Family 034, log abundance. |
| S18 | `preprints/Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-5-2026/build/main.tex` | Family 034, conditional fourfold result. |
| S19 | `preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/build/main.tex` | Family 046. |
| S20 | `preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/paper.tex` | Family 065. |
| S21 | `preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/main.tex` | Family 125, $P\ne NP$ threshold. |
| S22 | `preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/build/main.tex` | Family 140. |
| S23 | `preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/build/main.tex` | Family 140. |
| S24 | `preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/build/main.tex` | Family 216. |
| S25 | `preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/build/main.tex` | Family 218. |
| S26 | `preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex` | Family 238, full-deck mixing. |
| S27 | `preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/build/main.tex` | Family 238, conditional permutation. |
| S28 | `preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/main.tex` | Family 244. |
| S29 | `preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/build/paper.tex` | Family 260. |
| S30 | `preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/build/main.tex` | Family 282. |
| S31 | `notes/abstracts.tsv` | Generated per-family record, 372 rows. |
| S32 | `notes/scripts/build_catalog.py` | `SHAPES`, `ASSUME`, `TECH_AFTER`, `conditional_hits`. |
| S33 | `notes/scripts/compare_abstracts.py` | The comparison, the ratio function, and its gates. |
| S34 | `preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/build/paper.tex` | Family 260, outermostness and decay hypotheses. |
| S35 | `preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/build/main.tex` | Family 260, anti-de Sitter four-flux assumption. |
| S36 | `preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/build/paper.tex` | Family 260, equality rigidity under horizon hypotheses. |
| S37 | `notes/scripts/verify_abstracts.py` | The checker that resolves every marker and quotation on this page. |

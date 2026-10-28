[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 058](../index/algebraic-and-complex-geometry/058-kollar-pardon-universal-cover-conjecture.md)

# 058 — The Kollár–Pardon universal-cover conjecture

[Index page](../index/algebraic-and-complex-geometry/058-kollar-pardon-universal-cover-conjecture.md)

## Original CONTENTS.md summary

The release blurb 

> **058. Semialgebraic universal covers and bounded domains.** Proves the Kollár–Pardon conjecture: the semialgebraic universal covers of connected normal projective complex varieties are exactly products $`D\times\mathbb C^m\times F`$, with D bounded symmetric and F simply connected, normal, and projective. A universal cover is quasi-projective exactly when the bounded symmetric factor is absent. In particular, a smooth projective variety covered by ℂn has a finite étale cover by an abelian variety. [S1:1515]

This family ships **two** companion manuscripts. The classification:

Manuscript 1, the Kollár–Pardon universal-cover classification 

> We prove the Kollár–Pardon conjecture: the universal cover of a
connected normal projective complex variety is biholomorphic to a
semialgebraic open subset of a projective variety if and only if it
is a product of a bounded symmetric domain, a complex affine space,
and a simply connected normal projective variety. [S2:56–62]

The bounded-domain symmetry theorem (the one the Lean formalization
proves):

Manuscript 2, symmetry of semialgebraic bounded domains 

> Every nonempty connected semialgebraic bounded open subset of a complex
affine variety admitting a properly discontinuous cocompact group of
biholomorphisms is smooth and biholomorphic to a bounded symmetric domain.
This answers the bounded-domain question of Kollár and Pardon affirmatively. [S4:52–57]

## Undergraduate summary

The **Kollár–Pardon conjecture** asks: what does the universal cover of
a projective variety look like when it admits a "real-algebraic"
(description by finitely many polynomial equations and inequalities in
the real and imaginary parts) presentation? The answer this family
proves is a clean **product decomposition**: the universal cover is
biholomorphic to a bounded symmetric domain times a complex affine space
times a simply connected normal projective variety. The bounded
symmetric factor encodes the "hyperbolic" geometry, the affine factor
comes from the Albanese variety (the "torus-like" part), and the
projective factor is the "simply connected core." A special case gives
the familiar fact: if a smooth projective variety is covered by
$\mathbb C^n$, it has a finite étale cover by an abelian variety.

The second manuscript proves the **bounded-domain symmetry theorem**:
if a semialgebraic bounded domain in a complex affine variety admits a
properly discontinuous group of biholomorphisms with compact quotient,
then the domain is actually a **bounded symmetric domain** — a domain
with a holomorphic involution fixed at every point. This is the key
geometric input that the classification theorem uses to identify the
bounded factor.

## Graduate summary

**The Kollár–Pardon classification.** 

> **theorem**
Let $X$ be a connected normal projective variety over $\mathbb C$, and let
$\widetilde X$ be its universal cover. The following conditions are
equivalent:
\beginenumerate[label=\textup{(\roman*)}]
\item $\widetilde X$ is biholomorphic to a semialgebraic open subset
of a projective variety.
\item There are an integer $m\geq0$, a bounded symmetric domain $D$,
and a simply connected normal projective variety $F$ such that
$$\widetilde X\simeq D\times\mathbb C^m\times F.$$
\endenumerate
A point is allowed as either $D$ or $F$. No algebraicity of the
deck transformations is assumed. [S3:92–107]

For a connected normal projective variety $X$ over $\mathbb C$, its
universal cover $\widetilde X$ is biholomorphic to a semialgebraic open
subset of a projective variety if and only if
$\widetilde X \simeq D \times \mathbb C^m \times F$ for a bounded
symmetric domain $D$, an integer $m \geq 0$, and a simply connected
normal projective variety $F$. A point is allowed as either $D$ or $F$.
This proves Conjecture 2 of Kollár and Pardon in the normal-projective
scope. The three factors have distinct geometric roles: $D$ records
hyperbolic transverse geometry, $\mathbb C^m$ arises from Albanese
varieties of compact fibres after finite covers, and $F$ is the simply
connected core.

**Bounded-domain symmetry.** 

> **theorem**
Let $U$ be a nonempty connected semialgebraic bounded open subset of a
complex affine variety. Suppose that a group $\Gamma$ of
biholomorphisms acts properly discontinuously on $U$ and that
$U/\Gamma$ is compact. Then $U$ is smooth and is biholomorphic to a
bounded symmetric domain. [S5:77–83]

A nonempty connected semialgebraic bounded open subset $U$ of a complex
affine variety, admitting a properly discontinuous group $\Gamma$ of
biholomorphisms with compact quotient $U/\Gamma$, is smooth and
biholomorphic to a bounded symmetric domain. This answers the
bounded-domain question of Kollár and Pardon affirmatively. The
ambient algebraic set may be singular, and the quotient may have finite
quotient singularities; the semialgebraic hypothesis is on the domain
in one affine embedding, with no algebraicity requirement on the
biholomorphisms. This theorem is the one the Lean formalization proves.

## history of the conjecture

Prior (my training data, not this repo): **Kollár and Pardon** posed
the question in their study of algebraic varieties with semialgebraic
universal covers (arXiv 2012, Question 25 and Conjecture 2). The
bounded-domain question asks whether a semialgebraic bounded domain with
a cocompact holomorphic group action must be a bounded symmetric
domain; the universal-cover classification asks for the global product
decomposition. The bounded-domain theorem (manuscript 2) is the
geometric input: it identifies the bounded factor as symmetric, and the
classification (manuscript 1) assembles the three factors using
Albanese-variety arguments, finite-cover reduction, and the semialgebraic
hypothesis on the universal cover. The companion relationship is
explicit: manuscript 1 cites manuscript 2 as
`OpenAISemialgebraicCovers2026`, and manuscript 2 cites manuscript 1 as
the "companion article" establishing the classification.

## Consequences

**The Kollár–Pardon universal-cover classification**: the
semialgebraic universal covers of connected normal projective complex
varieties are exactly $D \times \mathbb C^m \times F$ with $D$
bounded symmetric and $F$ simply connected, normal, projective
[S3:92–107].

**A universal cover is quasi-projective** exactly when the bounded
symmetric factor $D$ is absent (a point) [S3:92–107].

**Bounded-domain symmetry**: a semialgebraic bounded domain with a
properly discontinuous cocompact group of biholomorphisms is a bounded
symmetric domain [S5:77–83].

**A smooth projective variety covered by $\mathbb C^n$** has a finite
étale cover by an abelian variety [S3:92–107].

## section skeleton

Two manuscripts. Manuscript 1 is a long single-file paper; manuscript 2
is a shorter paper with a flat section list.

Manuscript 1 [S2:56–62] `build/main.tex`, nine section inputs [S2:130, 246,
269–274, 369] (history, figures/proof-overview, preliminaries,
localization, windows, quotient, groups, compact, quasiprojective). The
abstract is at [S2:56–62] and the theorem at [S3:92–107].

Manuscript 2 [S4:52–57] `build/paper.tex`, seven inputs [S4:222, 224–229]
(figures/proof-overview, 01_geometry, 02_preparation, 03_noncollapse,
04_scaling, 05_symmetry, bibliography). The abstract is at
[S4:52–57] and the theorem at [S5:77–83].

## Comparison with the formalized statement

The scope note states:

> The formalized result answers the paper's symmetry question affirmatively. A nonempty connected bounded semialgebraic subset, relatively open in a complex affine algebraic set, is smooth and biholomorphic to a bounded symmetric domain whenever a discrete group acts properly and holomorphically with compact quotient. [S6:9]

The formalized result is manuscript 2's bounded-domain symmetry
theorem, not manuscript 1's classification. The comparator stub
[S7:58] ends in `sorry` — it states the target the release set itself.
The proved version lives in `OAI/Analysis/SymmetricDomains/Main.lean`,
where the declaration `OAI.Release061.main` [S8:55] carries 0 `sorry`:
the formalization imports two supporting modules
(`DivisibleHermitianModel` and `HermitianModelSymmetric`), splits on the
degenerate (singleton) case, and for the non-degenerate case invokes a
divisible-Hermitian-model construction, conjugates the group action
through the resulting biholomorphism, and applies the bounded-symmetric-domain
criterion. The action need not be free, and the ambient algebraic set
may be singular — both stated in the scope note.

## Coverage

T3: two manuscripts, one formalized (the symmetry manuscript), one
comparator challenge, one `main_results` entry, one scope note. The
ledger reads `paps 2`, `paps_form 1`, `mainres 1`, `chal 1`,
`scope_note 1`, `verification 0`, `trace` empty, `shapes
resolution|bound`, `resolves_named 1`. The catalog entry [S9:192]
names both PDFs. The formalization proves the bounded-domain symmetry
theorem (manuscript 2) affirmatively; the classification theorem
(manuscript 1) is not the declared `main_results` target.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 058 at line 1515) |
| S2 | [`preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/main.tex`](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/main.tex) | 376 | Manuscript 1: abstract, section inputs (Kollár–Pardon classification) |
| S3 | [`preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/main.tex`](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/main.tex) | 376 | Manuscript 1: main theorem (classification) |
| S4 | [`preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex`](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex) | 230 | Manuscript 2: abstract, section inputs (bounded-domain symmetry) |
| S5 | [`preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex`](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex) | 230 | Manuscript 2: main theorem (symmetry, the formalized statement) |
| S6 | [`lean/docs/058.md`](../../../lean/docs/058.md) | 17 | Scope note (the formalized result answers the symmetry question affirmatively) |
| S7 | [`lean/ComparatorChallenges/SymmetricDomains.lean`](../../../lean/ComparatorChallenges/SymmetricDomains.lean) | 62 | Comparator stub (ends in sorry) |
| S8 | [`lean/OAI/Analysis/SymmetricDomains/Main.lean`](../../../lean/OAI/Analysis/SymmetricDomains/Main.lean) | 92 | Lean proof (OAI.Release061.main, 0 sorry) |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 058 at line 192) |

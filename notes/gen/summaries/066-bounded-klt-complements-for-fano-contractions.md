[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 066](../index/algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md)

# 066 — Bounded klt complements for Fano contractions

[Index page](../index/algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md)

## Original CONTENTS.md summary

The release blurb 

> **066. Bounded klt complements for Fano contractions.** Proves the finite-rational-coefficient form of Shokurov’s bounded-klt-complement conjecture for ϵ-lc complex Fano-type pairs with nef anti-log-canonical divisor. For ϵ-lc Fano contractions over any algebraically closed characteristic-zero field, it gives klt complements near every base point, with index bounded only by dimension and positive rational ϵ. [S1:1654]

This family ships **two** companion manuscripts. The bounded klt
complement theorem (the headline):

Manuscript 1, bounded klt complements for Fano contractions 

> For fixed dimension $d$ and positive rational $\epsilon$, we prove that
every $\epsilon$-log-canonical Fano contraction over an algebraically
closed field of characteristic zero admits, near each closed base point,
a klt complement of index bounded only by $d$ and $\epsilon$.
Over $\mathbb C$, we also obtain monotone klt complements for Fano type
pairs with nef anti-log-canonical divisor and coefficients in a fixed
finite rational set. This proves the finite-rational-coefficient form of
Shokurov's bounded-klt-complement conjecture. [S2:9–18]

The uniform Cartier-section theorem (the statement the Lean
formalization links to, but does not prove):

Manuscript 2, uniform Cartier sections 

> We prove the Cartier-divisor conjecture of Birkar and Shokurov for rational boundaries in characteristic zero and for real boundaries over $\mathbb C$. For an $\epsilon$-lc Fano type contraction with positive-dimensional base and nef negative log canonical class, a Cartier divisor through any prescribed base point can be chosen with pullback log canonical threshold bounded below in terms of the dimension and $\epsilon$ alone. [S4:58–60]

## Undergraduate summary

**Fano contractions** are maps from a "Fano-type" variety (one whose
anticanonical bundle is "positive") onto a lower-dimensional base.
The **bounded klt complement conjecture** (Shokurov) asks: given such a
contraction over a field of characteristic zero, can we find a
"complement" — a divisor that, when added to the canonical divisor,
becomes torsion (a multiple of it is Cartier and trivial) — whose
**index** (the multiple needed) is *bounded in terms of only the
dimension and a lower bound on the singularities*? "klt" ("kawamata
log terminal") means the singularities are "mild" in a precise
surgical sense (all discrepancies strictly positive).

The **uniform Cartier-section conjecture** (Birkar–Shokurov) asks a
related question: through any prescribed point on the base, can we
choose a Cartier divisor whose pullback has a *log canonical threshold*
(a singularities-measuring number) bounded below uniformly, depending
only on dimension and the discrepancy lower bound? The two questions
are equivalent over $\mathbb C$ (a theorem of Chen), and this family
proves both forms in their natural settings: the klt-complement form
for $\mathbb C$ with finite rational coefficients (manuscript 1), and
the uniform Cartier-section form for rational boundaries in
characteristic zero and for real boundaries over $\mathbb C$
(manuscript 2).

## Graduate summary

**Bounded klt complements.** 

> **theorem**
For every positive integer $d$ and positive rational number $\epsilon$ there
is a positive integer $N=N(d,\epsilon)$ with the following property. Let $k$
be an algebraically closed field of characteristic zero, and let
$f\colon X\to Z$ be a projective surjective morphism of normal integral
$k$-varieties such that $f_*\mathcal O_X=\mathcal O_Z$, $\dim X=d$, $K_X$ is
$\mathbb Q$-Cartier, $X$ is $\epsilon$-lc, and $-K_X$ is ample over $Z$.
For every closed point $z\in Z$ there are an effective $\mathbb Q$-divisor $B$ on
$X$ and a Zariski open neighbourhood $U$ of $z$ such that $(X,B)$ is klt over
$U$ and
$$N(K_X+B)|_{f^{-1}(U)}\sim 0$$
is an integral Cartier divisor. [S3:22–36]

For every positive integer $d$ and positive rational $\epsilon$, there is
a positive integer $N = N(d, \epsilon)$ such that for every
$\epsilon$-lc Fano contraction $f : X \to Z$ of dimension $d$ over an
algebraically closed characteristic-zero field, every closed base point
$z \in Z$ has a neighbourhood $U$ and an effective $\mathbb Q$-divisor
$B$ on $X$ with $(X, B)$ klt over $U$ and
$N(K_X + B)|_{f^{-1}(U)} \sim 0$ an integral Cartier divisor. The index
$N$ depends only on $d$ and $\epsilon$.

**Uniform Cartier sections.** 

> **Theorem 1**
For every integer $d>0$ and every real number $\epsilon>0$, there is a real number $\tau=\tau(d,\epsilon)>0$ with the following property. Let $(X,B)$ be an $\epsilon$-lc rational pair of dimension $d$, and let $f:X\to Z$ be a Fano type contraction of normal integral quasi-projective varieties with $\dim Z>0$. Suppose that $-(K_X+B)$ is nef over $Z$. For every closed point $z\in Z$, there are an open neighbourhood $U$ of $z$ and a nonzero effective Cartier divisor $D$ on $U$, with $z\in\mathrm{Supp} D$, such that
$$\bigl(f^{-1}(U),B|_{f^{-1}(U)}+\tau f^*D\bigr)
\quad\text{is log canonical.}$$ [S5:21–27]

For every $d > 0$ and real $\epsilon > 0$, there is a real $\tau =
\tau(d, \epsilon) > 0$ such that for every $\epsilon$-lc rational pair
$(X, B)$ of dimension $d$ and Fano type contraction $f : X \to Z$ with
$\dim Z > 0$ and $-(K_X + B)$ nef over $Z$, every closed base point $z$
has a neighbourhood $U$ and a nonzero effective Cartier divisor $D$ on
$U$ with $z \in \mathrm{Supp} D$ such that
$(f^{-1}(U), B|_{f^{-1}(U)} + \tau f^* D)$ is log canonical. The
constant $\tau$ is uniform: it depends only on $d$ and $\epsilon$, not
on the contraction, the boundary, or any Cartier index.

## history of the conjecture

Prior (my training data, not this repo): **Shokurov** formulated the
bounded klt complement conjecture in his 2004 boundedness work, as a
strengthening of his earlier surface-local and threefold-flip
complements. **Birkar** proved boundedness of lc complements for Fano
type pairs with hyperstandard coefficients (2014, 2016); the klt
version and the uniform Cartier-section form are the remaining
directions. The **Birkar–Shokurov Cartier-divisor conjecture** asks for
a uniform positive lower bound on the log canonical threshold of a
Cartier divisor through a prescribed base point, depending only on
dimension and discrepancy. Chen's reduction (2025) establishes the
equivalence of the klt-complement, Cartier-section, and
identity-contraction forms over $\mathbb C$, and proves the surface and
curve-base cases. The two manuscripts here prove the missing general
directions: manuscript 1 by a valuation-optimization argument over the
cone of normalized valuations, and manuscript 2 by a character-and
pinning-obstruction argument over a constrained $h$-lc slice of
normalized-volume minimizers, invoking Chen's equivalence to transfer
the birational theorem to the uniform Cartier-section statement.

## Consequences

**Bounded klt complements** for $\epsilon$-lc Fano contractions over
any algebraically closed characteristic-zero field, index bounded by
$d$ and $\epsilon$ alone [S3:22–36].

**Monotone klt complements** over $\mathbb C$ for Fano-type pairs with
nef anti-log-canonical divisor and coefficients in a fixed finite
rational set, proving the finite-rational-coefficient form of
Shokurov's conjecture [S3:22–36, S2:14–16].

**Uniform Cartier sections** for $\epsilon$-lc rational pairs in
characteristic zero, and for real boundaries over $\mathbb C$, with a
uniform log-canonical-threshold lower bound [S5:21–27].

**The Birkar–Shokurov Cartier-divisor conjecture** is resolved
positively in these settings [S5:21–27].

## section skeleton

Two manuscripts, each a single main file with a flat section list.

Manuscript 1 [S2:9–18] `build/main.tex`, fourteen inputs [S2:22–35]
(introduction with the theorem at [S3:22], reduction, initial-cone,
constrained-minimum, compatible-filtrations, essential-system,
discrepancy-push, scale-tower, width-estimates, bounded-axes,
valuation-optimization, trace-lifting, cheap-collapse, rank-growth).
The abstract is in `main.tex` itself at [S2:9–18].

Manuscript 2 [S4:58–60] `build/main.tex`, nine inputs [S4:61, 68–75]
(introduction with the main theorem at [S5:21] and the birational and
real-boundary theorems at [S5:49] and [S5:61], A-discriminants,
B-phase-nonvanishing, C-cutoff-fields, D-cone-characters, E-lc-slices,
F-degeneration, G-pinning, H-reduction). The abstract is in `main.tex`
itself at [S4:58–60].

## Comparison with the formalized statement

The scope note [S6:13] is explicit that the formalization proves only a
supporting compactness lemma, not the paper's headline:

> This compactness result applies to one such chart. It does not construct a Cartier divisor through a prescribed base point whose pullback has a positive log-canonical-threshold bound along the whole fibre depending only on dimension and discrepancy, as required by the paper's uniform Cartier-section theorem. Bounded klt complements and the paper's real-boundary and companion conclusions are also outside this comparison. [S6:13]

The declared `main_results` target is
`OAI.CartierSections.isCompact_closedChartFieldRetraction_cone`
[S8:47], which carries 0 `sorry` in
`OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean`. The
comparator stub [S7:25] ends in `sorry` at line 30 — it states the target
the release set itself. The proved version is a local compactness result
for the chart-field retractions of one chart over an algebraically closed
field; the chart is built from the localization of a polynomial ring at
its origin, with the local domain Noetherian, essentially of finite type
and formally unramified over that localization, and formally étale over
the polynomial ring. The uniform Cartier-section theorem [S5:21–27],
the bounded klt complement theorem [S3:22–36], and the real-boundary and
companion conclusions of both manuscripts are outside this comparison.

## Coverage

T3: two manuscripts, one formalized (a supporting compactness lemma in
the companion manuscript's chain), one comparator challenge, one
`main_results` entry, one scope note. The ledger reads `paps 2`,
`paps_form 1`, `mainres 1`, `chal 1`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes bound|classification`, `resolves_named 1`. The
catalog entry [S9:206] names both PDFs. The formalization proves the
chart-field compactness lemma [S8:47]; the bounded klt complement and
uniform Cartier-section theorems, and the real-boundary and companion
conclusions, are not the declared `main_results` targets.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 066 at line 1654) |
| S2 | [`preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/main.tex`](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/main.tex) | 38 | Manuscript 1: abstract, section inputs (bounded klt complements) |
| S3 | [`preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/sections/introduction.tex`](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/sections/introduction.tex) | 299 | Manuscript 1: main theorem (bounded klt complements) |
| S4 | [`preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/main.tex`](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/main.tex) | 81 | Manuscript 2: abstract, section inputs (uniform Cartier sections) |
| S5 | [`preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/sections/introduction.tex`](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/sections/introduction.tex) | 103 | Manuscript 2: main theorem (uniform Cartier sections, the statement the formalization links to) |
| S6 | [`lean/docs/066.md`](../../../lean/docs/066.md) | 19 | Scope note (the formalization proves a supporting compactness lemma; the headline is outside) |
| S7 | [`lean/ComparatorChallenges/CartierChartCompactnessSupport.lean`](../../../lean/ComparatorChallenges/CartierChartCompactnessSupport.lean) | 37 | Comparator stub (ends in sorry) |
| S8 | [`lean/OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean`](../../../lean/OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean) | 61 | Lean proof (OAI.CartierSections.isCompact_closedChartFieldRetraction_cone, 0 sorry) |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 066 at line 206) |

[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 068](../index/algebraic-and-complex-geometry/068-anticanonical-nonvanishing-under-smooth-semipositivity.md)

# 068 — Anticanonical nonvanishing under smooth semipositivity

[Index page](../index/algebraic-and-complex-geometry/068-anticanonical-nonvanishing-under-smooth-semipositivity.md)

## Original CONTENTS.md summary

The release blurb 

> **068. Anticanonical nonvanishing in every dimension.** If *X* is a smooth connected complex projective variety and $`-K_X`$ admits a smooth Hermitian metric with nonnegative curvature, then $`H^0(X,-mK_X)\ne0`$ for some *m* > 0. Thus smooth semipositivity forces a nonzero section of a positive tensor power of the anticanonical bundle in every dimension. [S1:1695]

This is the largest family in the release so far: **seven** companion
manuscripts, each attacking the same headline from a different
technical angle. The headline (manuscript 1):

Manuscript 1, anticanonical nonvanishing from smooth semipositivity 

> Every smooth connected projective complex variety with smoothly
semipositive anticanonical bundle has a nonzero section of some positive
anticanonical power. [S2:27–31]

The six supporting manuscripts, each proving a lemma or a variant that
feeds the main argument:

Manuscript 2, invariant anticanonical indices 

> For a holomorphic action of a compact torus on a compact complex manifold,
we prove that the invariant Euler characteristic of naturally linearized
anticanonical powers is polynomial on a divisible progression, with its
actual value at exponent zero. Independently, on a smooth projective
variety with smoothly semipositive anticanonical bundle, we remove a fixed
pseudoeffective error from an unbounded sequence of effective twists.
These results convert invariant cohomology into twisted differential
forms and prove anticanonical nonvanishing on smooth projective varieties
with smoothly semipositive anticanonical bundle, by descending the forms
before conversion. [S3:50–61]

Manuscript 3, bounded anticanonical metrics on klt pairs 

> Let $`(W,D)`$ be a projective $`\mathbb Q`$-factorial klt pair with effective rational boundary. We prove that a positive Cartier multiple of $`-(K_W+D)`$ has a nonzero section if this divisor is nef, its pullback to a resolution admits a semipositive metric with locally bounded weights, and the resolution has nonzero structure-sheaf Euler characteristic. Consequently a smooth rationally connected projective variety with smoothly semipositive anticanonical bundle has a nonzero naturally invariant anticanonical plurisection for every algebraic torus action. [S4:38–40]

Manuscript 4, cohomological transfer and equivariant sections 

> Let $`X`$ be a smooth projective complex variety with smoothly semipositive anticanonical bundle. For any torus linearization of that bundle, we show that invariant sections in unbounded degrees with one fixed negative pseudoeffective error yield an invariant section in a positive untwisted degree. Combining the natural invariant index with compact-monodromy structure, we deduce that every such $`X`$ has a nonzero section of some positive anticanonical power. [S5:46–48]

Manuscript 5, metric descent and rank-preserving contractions 

> From a smooth semipositive anticanonical metric on a smooth projective
complex variety, we construct an
unweighted integrable semipositive metric on a corrected anticanonical
line of a smooth base, using a normal equidimensional toroidal model
and full generic adjoint rank one at exponent zero. The explicit
rational boundary correction pulls back to an exceptional divisor.
On varieties without positive-degree holomorphic forms, two-metric
transfer gives sections with prescribed boundary poles from a
finite-volume log-anticanonical metric and a target line with bounded
semipositive weights. In particular, a smooth projective complex
variety with a smoothly semipositive anticanonical bundle and no such
forms has a nonzero invariant section of a positive anticanonical
multiple for every torus action with its natural linearization.
On this class of varieties, generic section and adjoint-rank hypotheses
give contractions of invariant fibrations that preserve both conditions
unless an invariant global section already exists. [S6:32–49]

Manuscript 6, integrable metrics and effectivity with controlled
boundary 

> Let $`Y`$ be smooth projective and let $`C`$ be an effective integral divisor.
If $`-K_Y+C`$ admits a metric with a global strict curvature lower bound
for which the canonical section of $`C`$ is locally square integrable,
every pseudoeffective rational divisor becomes rationally effective
after an effective correction supported on $`C`$.
For a smooth projective $`X`$ with smoothly semipositive $`L=-K_X`$,
sections of $`m_jL-P`$ at unbounded positive exponents, with any fixed
pseudoeffective Cartier error $`P`$, yield a section of a positive
multiple of $`L`$. [S7:33–43]

Manuscript 7, exact orders and invariant anticanonical linear systems


> On a smooth connected projective complex variety with smoothly
semipositive anticanonical bundle, we prove that asymptotically zero valuation on the curvature-null face is attained by
an effective rational anticanonical divisor. The fixed auxiliary line
bundle is arbitrary. [S8:34–39]

## Undergraduate summary

**Anticanonical nonvanishing** asks a deceptively simple question: if
the anticanonical bundle $`-K_X`$ of a smooth projective variety carries
a metric whose curvature is everywhere nonnegative (a "smoothly
semipositive" metric), must some positive power $`m K_X`$ have a nonzero
holomorphic section? In geometric language: does smooth semipositivity
of the anticanonical curvature force the anticanonical bundle to be
"nef enough" to actually produce sections?

The answer is yes in every dimension. The seven manuscripts here build
this from component lemmas: a finite-volume theorem controlling
adjoint metrics (manuscript 1), an equivariant conversion of invariant
cohomology into twisted differential forms (manuscript 2), a
boundedness result for klt pairs with torus quotients (manuscript 3),
a transfer principle for invariant sections under torus actions
(manuscript 4), a metric-descent argument preserving the rank
hypothesis under contractions (manuscript 5), an effectivity result
with a controlled boundary correction (manuscript 6), and an exact-
order argument showing the valuation on the curvature-null face is
attained by an effective divisor (manuscript 7). Together they prove
that the smooth semipositivity assumption is strong enough to force
nonvanishing without any additional projective-genus hypothesis.

## Graduate summary

**The headline theorem** (manuscript 1) 

> **theorem**
Let $`X`$ be a smooth connected projective variety over $`\mathbb C`$.
If $`-K_X`$ admits a smooth Hermitian metric of semipositive curvature,
then $`H^0(X,-mK_X)\ne0`$ for some integer $`m>0`$. [S9:14–18]

This is the positive-multiple formulation of Yau's anticanonical
nonvanishing question. The proof proceeds by induction on dimension,
using a finite-volume theorem [S9:77–94] that controls sections of
corrected anticanonical lines on bases of smaller dimension. The
structure theory of Demailly–Peternell–Schneider and Campana–Demailly–
Peternell describes the universal cover by its flat, Ricci-flat, and
compact factors [S9:41–51]; the compact torus action on the remaining
factor is where the invariant-section machinery of manuscripts 2–7
enters.

The supporting manuscripts each prove a component: manuscript 2
establishes the polynomiality of the invariant Euler characteristic
and the conversion of invariant cohomology to twisted forms (theorem
at line 29 of its `sections/introduction.tex`); manuscript 3 proves
the boundedness for klt pairs (theorem at line 15); manuscript 4
proves the cohomological transfer (theorem at line 8); manuscript 5
proves the rank-preserving contraction (theorem at line 13 of its
`sections/contraction.tex`); manuscript 6 proves the effectivity with
controlled boundary (theorem at line 24); manuscript 7 proves the
exact-order result (theorems at lines 49 and 144).

## history of the conjecture

**Yau's anticanonical nonvanishing question** (Problem 75, p. 395 of
his 1994 problem collection) asks whether a smooth projective variety
with a smoothly semipositive anticanonical bundle must have a nonzero
section of some positive anticanonical power. This is the positive-
multiple analogue of the classical result that a smooth semipositive
Hermite-Einstein metric with vanishing first Chern class is flat. The
question is open in the general dimension: the Enriques-surface
example (where $`K_E`$ has order two and no first-power section, but the
square has sections) shows that the positive multiple is genuinely
necessary, not just a technical convenience.

The structural inputs — Yau's prescribed-Ricci theorem, the
Demailly–Peternell–Schneider structure theorem, the Campana–Demailly–
Peternell refinement, the Lazić–Matsumura–Peternell–Tsakanikas–Xie
numerical effectivity theorem, and Müller's nonvanishing in dimension
three — are all cited in manuscript 1's introduction [S9:38–55]. The
present argument adds the monodromy-invariant section construction
that closes the gap between the structural decomposition and an
actual section on the base.

## Consequences

**Anticanonical nonvanishing in every dimension:** a smooth connected
projective complex variety with a smoothly semipositive anticanonical
bundle has $`H^0(X, -mK_X) \neq 0`$ for some $`m > 0`$ [S9:14–18].

**The Enriques surface is the sharp example:** the first positive
anticanonical power has no section, the second does, and the
anticanonical bundle is not torsion [S9:21–30].

**Invariant nonvanishing under torus actions:** the nonzero section
can be chosen invariant under any algebraic torus action with its
natural linearization [S4:40, S5:48, S6:48].

**The finite-volume theorem:** the inductive engine, controlling
sections of corrected anticanonical lines on bases of smaller
dimension [S9:77–94].

## section skeleton

Seven manuscripts, all with the same layout: a single
`build/source/main.tex` root with the abstract inline and all
sections in `build/source/sections/`.

Manuscript 1 [S2:27–31] `build/source/main.tex`: abstract at [S2:27–31],
headline theorem in `sections/introduction.tex` at [S9:14], finite-
volume theorem at [S9:77], and sections for structure, slope,
transfer, induction, torus, and models.

Manuscript 2 [S3:50–61] `build/source/main.tex`: abstract at [S3:50–61],
theorems in `sections/introduction.tex` (lines 29, 98).

Manuscript 3 [S4:38–40] `build/source/main.tex`: abstract at [S4:38–40],
theorems in `sections/introduction.tex` (lines 15, 27).

Manuscript 4 [S5:46–48] `build/source/main.tex`: abstract at [S5:46–48],
theorem in `sections/introduction.tex` (line 8).

Manuscript 5 [S6:32–49] `build/source/main.tex`: abstract at [S6:32–49],
theorem in `sections/contraction.tex` (line 13).

Manuscript 6 [S7:33–43] `build/source/main.tex`: abstract at [S7:33–43],
theorem in `sections/introduction.tex` (line 24).

Manuscript 7 [S8:34–39] `build/source/main.tex`: abstract at [S8:34–39],
theorems in `sections/introduction.tex` (lines 49, 144).

## Coverage

T0: seven manuscripts, zero comparator challenges, zero
`main_results` entries, zero scope notes. The ledger reads `paps 7`,
`paps_form 0`, `mainres 0`, `chal 0`, `scope_note 0`, `verification 0`,
`trace` empty, `shapes` (empty), `resolves_named 0` — the simplest tier
in the release. The catalog entry [S10:210] names all seven PDFs. No
Lean formalization, no comparator stub, and no scope note exist for
this family.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 068 at line 1695) |
| S2 | [`preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/build/source/main.tex`](../../../preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/build/source/main.tex) | 42 | Manuscript 1: abstract, section inputs (headline nonvanishing) |
| S3 | [`preprints/Invariant-anticanonical-indices-and-conversion-of-twisted-differentials-September-26-2026/build/source/main.tex`](../../../preprints/Invariant-anticanonical-indices-and-conversion-of-twisted-differentials-September-26-2026/build/source/main.tex) | 72 | Manuscript 2: abstract, section inputs (invariant anticanonical indices) |
| S4 | [`preprints/Bounded-anticanonical-metrics-on-klt-pairs-and-torus-quotients-September-26-2026/build/source/main.tex`](../../../preprints/Bounded-anticanonical-metrics-on-klt-pairs-and-torus-quotients-September-26-2026/build/source/main.tex) | 49 | Manuscript 3: abstract, section inputs (bounded anticanonical metrics on klt pairs) |
| S5 | [`preprints/Cohomological-transfer-and-equivariant-anticanonical-sections-September-26-2026/build/source/main.tex`](../../../preprints/Cohomological-transfer-and-equivariant-anticanonical-sections-September-26-2026/build/source/main.tex) | 68 | Manuscript 4: abstract, section inputs (cohomological transfer and equivariant sections) |
| S6 | [`preprints/Metric-descent-and-rank-preserving-contractions-September-26-2026/build/source/main.tex`](../../../preprints/Metric-descent-and-rank-preserving-contractions-September-26-2026/build/source/main.tex) | 64 | Manuscript 5: abstract, section inputs (metric descent and rank-preserving contractions) |
| S7 | [`preprints/Integrable-metrics-and-effectivity-with-controlled-boundary-September-26-2026/build/source/main.tex`](../../../preprints/Integrable-metrics-and-effectivity-with-controlled-boundary-September-26-2026/build/source/main.tex) | 58 | Manuscript 6: abstract, section inputs (integrable metrics and effectivity) |
| S8 | [`preprints/Exact-orders-and-invariant-anticanonical-linear-systems-September-26-2026/build/source/main.tex`](../../../preprints/Exact-orders-and-invariant-anticanonical-linear-systems-September-26-2026/build/source/main.tex) | 58 | Manuscript 7: abstract, section inputs (exact orders and invariant anticanonical systems) |
| S9 | [`preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/build/source/sections/introduction.tex`](../../../preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/build/source/sections/introduction.tex) | 225 | Manuscript 1: headline theorem (anticanonical nonvanishing) |
| S10 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 068 at line 210) |

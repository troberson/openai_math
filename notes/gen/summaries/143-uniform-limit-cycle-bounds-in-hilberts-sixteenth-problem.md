[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 143](../index/dynamical-systems-and-ergodic-theory/143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md)

# 143 — Uniform limit-cycle bounds in Hilbert's sixteenth problem

[Index page](../index/dynamical-systems-and-ergodic-theory/143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md)

## Original CONTENTS.md summary

The release's blurb [S1:3452] and the catalog abstract [S2:367] state
the family's claim: the number of isolated periodic orbits of a real
planar polynomial vector field is bounded by a finite constant
depending only on its degree — the uniform boundedness assertion
in Hilbert's sixteenth problem — and that for classical quintic
Liénard systems the exact maximum is two limit cycles. The
headline manuscript's abstract 

> For every degree, we prove that the number of isolated periodic orbits of a
real planar polynomial vector field is bounded by a finite constant depending
only on that degree. This establishes the uniform boundedness assertion in
the second part of Hilbert's sixteenth problem. The proof uses separation
of asymptotic expansions on nested complex domains and a finite-dimensional
counting argument. [S3:25–30]

The family ships two manuscripts.

## Undergraduate summary

A *limit cycle* of a planar vector field is a closed orbit that no
other closed orbit can approach — an isolated periodic orbit.
Hilbert's sixteenth problem, in its second part, asks for a uniform
bound on how many such cycles a planar polynomial vector field of
degree $`n`$ can have, depending only on $`n`$. The headline manuscript
claims that for every degree $`n`$ such a finite bound exists, proved by
separating asymptotic expansions on nested complex domains and a
finite-dimensional counting argument [S3:25–30].

The companion manuscript addresses a specific named case. A
*Liénard system* is the planar system
$`\dot x=y-F(x)`$, $`\dot y=-x`$ for a polynomial $`F`$, and the
Lins Neto–de Melo–Pugh conjecture predicts that when
$`\deg F=5`$ the number of limit cycles is at most two. The companion
proves that bound and shows it is attained, so the exact maximum is
two [S4:28–32].

## Graduate summary

**The uniform bound (headline, unregistered).** For every degree $`n`$,
the number of isolated periodic orbits of a real planar polynomial
vector field of degree $`n`$ is bounded by a finite constant depending
only on $`n`$ [S3:25–30]. The proof uses separation of
asymptotic expansions on nested complex domains and a
finite-dimensional counting argument [S3:28–30]. This is the
family's headline claim, but it is the manuscript the release did
**not** register: it is absent from `formalization.yaml`'s
`sources:` and is not the `main_results` declaration (see the
`formalized` section).

**The quintic Liénard two-cycle bound (registered).** For the
quintic Liénard system $`\dot x=y-F(x)`$, $`\dot y=-x`$, every
real polynomial $`F`$ of degree at most five yields at most two limit
cycles, and some such $`F`$ yields exactly two [S4:28–32, S5:9].
This is the degree-five case of the
Lins Neto–de Melo–Pugh conjecture [S4:31–32], and it
is the statement the formalization registers.

## History of the conjecture

Hilbert posed the second part of his sixteenth problem in 1900, asking
for a uniform bound on the number of limit cycles of a planar
polynomial vector field in terms of its degree; it remains one of the
most open problems in qualitative ODE theory. The
Lins Neto–de Melo–Pugh conjecture is a tractable
named case, predicting at most two limit cycles for quintic
Liénard systems, and the companion manuscript resolves that
case exactly [S4:31–32].

**Prior (my training data, not this repo).** I know Hilbert's
sixteenth problem and that the uniform limit-cycle bound is open; I
know the Liénard system and the Lins Neto–de Melo–Pugh
conjecture as a named case. A proof of the *uniform* degree-dependent
bound for all planar polynomial vector fields is, to my knowledge,
not established in the literature I was trained on; the
degree-five Liénard two-cycle bound I am less sure of. I cannot
independently verify either manuscript's argument.

## Consequences

**Uniform boundedness in Hilbert's sixteenth problem (claimed).** The
number of isolated periodic orbits of a real planar polynomial vector
field is bounded by a finite constant depending only on its degree
[S3:25–30].

**Exact quintic Liénard maximum.** Every quintic
Liénard system has at most two limit cycles, and the bound is
attained, so the exact maximum is two [S4:28–32].

## Section skeleton

Two manuscripts:

- **headline (uniform bounds)** [S3:25–30] (title [S3:19], date [S3:21])
  — `main.tex` under `build/`; 17,692 lines total; one
  `.bib` file.
- **companion (quintic Liénard)** [S4] (title [S4:22], date
  [S4:24]) — `paper.tex` under `build/`; 3,248 lines total; a
  `thebibliography` block in `sections/references.tex`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalized result is the degree-five
Liénard statement: for the quintic Liénard system
$`x'=y-F(x)`$, $`y'=-x`$, every real polynomial $`F`$ of degree at most
five yields at most two limit cycles, and some such $`F`$ yields
exactly two. Limit cycles are isolated images of nonconstant periodic
solutions, and no sign, parity, hyperbolicity, or amplitude
restriction is imposed [S5:9]. The scope note links only the
companion Liénard manuscript and names one comparator
[S5:13–15].

**The partial registration.** The `main_results` entry names
`OAI.QuinticLienard.main` in
`OAI/Analysis/LienardCycles/Main.lean`, the degree-five two-cycle
bound — not the family's headline uniform-bounds claim. The
registered declaration is proven at line 20 

```lean
theorem main :
    (∀ F : Polynomial ℝ, F.degree ≤ 5 → {C : Set Plane | IsLimitCycle F C}.encard ≤ 2) ∧
    (∃ F : Polynomial ℝ, F.degree ≤ 5 ∧ {C : Set Plane | IsLimitCycle F C}.encard = 2) :=
  ⟨upper_bound,Sharpness.sharpness⟩
```
[S7:20–23]

The proof is a direct term: `upper_bound` discharges the at-most-two
claim and `Sharpness.sharpness` the existence of a two-cycle example.
Only one of the two manuscripts (the Liénard one) is in
`formalization.yaml`'s `sources:`; the 17,692-line headline
uniform-bounds manuscript is not registered, so the family's headline
claim has no Lean entry point. The OAI `LienardCycles` tree is 146
files over 16,659 lines with zero `sorry`. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library
has not been built here.

## Coverage

T3: the family is formalized, in its degree-five
Liénard case. The ledger row `fam=143` records `paps 2`,
`paps_form 1`, `tier T3`, `chal 1`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|bound|uniform`,
`resolves_named 1`, `summary 1`. The family ships two LaTeX
manuscripts (17,692 + 3,248 lines), a scope note naming one
comparator, and the registered `main_results` declaration
`OAI.QuinticLienard.main`, the degree-five two-cycle bound, proven as
a direct term in the 146-file `LienardCycles` OAI tree. Only the
companion Liénard manuscript is in the release's `sources:`; the
headline uniform-bounds manuscript, which carries the general-degree
claim, is not registered and has no Lean entry point. The family
ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 143 at [S1:3452] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{143} at [S2:367] |
| S3 | [`preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/main.tex`](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/main.tex) | 47 | headline manuscript root (uniform bounds); title [S3:19], date [S3:21], abstract [S3:25–30] |
| S4 | [`preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/build/paper.tex`](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/build/paper.tex) | 42 | companion manuscript root (quintic Liénard); title [S4:22], date [S4:24], abstract [S4:28–32] |
| S5 | [`lean/docs/143.md`](../../../lean/docs/143.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/QuinticLienard.lean`](../../../lean/ComparatorChallenges/QuinticLienard.lean) | 46 | comparator stub: the `main` theorem [S6:39–41] and the `sorry` [S6:42] |
| S7 | [`lean/OAI/Analysis/LienardCycles/Main.lean`](../../../lean/OAI/Analysis/LienardCycles/Main.lean) | 26 | the OAI proven `main` theorem [S7:20–23] |

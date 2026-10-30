[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 370](../index/partial-differential-equations/370-subcritical-lane-emden-and-henon-lane-emden-conjectures.md)

# 370 — The subcritical Lane–Emden and Hénon–Lane–Emden conjectures

[Index page](../index/partial-differential-equations/370-subcritical-lane-emden-and-henon-lane-emden-conjectures.md)

## Original CONTENTS.md summary

[S1:8954] (family entry):

> **370. The Lane–Emden and Hénon–Lane–Emden conjectures.** Resolves the subcritical Lane–Emden conjecture and its weighted Hénon extension. For <i>n</i> ≥ 2, $`p,q\gt 0`$ and real <i>A</i>, <i>B</i>, the system $`-\Delta u=|x|^A v^p`$, $`-\Delta v=|x|^B u^q`$ has no positive entire solution when $`(n+A)/(p+1)+(n+B)/(q+1)\gt n-2`$, with solutions continuous at the origin and classical elsewhere. No symmetry or growth assumption is needed. Known radial existence gives the exact existence criterion for <i>n</i> ≥ 3 and $`A,B\gt -2`$. ([Lean](lean/docs/370.md))

[S2:843] carries the `\resultentry` with a single manuscript [S3].
The scope note states the formalized result:

> The formalized result proves nonexistence of positive entire solutions to the subcritical Hénon–Lane–Emden system. For $`n\ge2`$, $`p,q>0`$, and real $`A,B`$ with $`(n+A)/(p+1)+(n+B)/(q+1)>n-2`$, there are no positive functions, continuous everywhere and $`C^2`$ off the origin, satisfying $`-\Delta u=|x|^A v^p`$ and $`-\Delta v=|x|^B u^q`$ away from the origin. It includes the globally $`C^2`$ unweighted case for $`n\ge3`$. The critical equality case is not included. [S4:9]

## Undergraduate summary

The **Lane–Emden equation** is a classical nonlinear equation that
models the density of a self-gravitating gas sphere. This family
studies its **weighted, coupled** version: two unknowns
$`u,v`$ that each solve a nonlinear Poisson equation, the other
appearing on the right-hand side with a weight:

$`-\Delta u = |x|^A\, v^p`$ \qquad $`-\Delta v = |x|^B\, u^q`$

The question is a **nonexistence** question: can this system have a
solution that is *strictly positive everywhere* on all of
$`\mathbb R^n`$ (an "entire" solution)?

The answer depends on a single number built from the dimension
$`n`$, the nonlinear exponents $`p,q`$, and the weights $`A,B`$:
the threshold
$`(n+A)/(p+1) + (n+B)/(q+1)`$ compared to $`n-2`$. When the sum is
**strictly larger** than $`n-2`$ (the "subcritical" regime), the
result says **no** such positive entire solution exists. When the
inequality **fails** (and $`n\ge3`$, with mild weights
$`A,B>-2`$), a positive radial entire solution **does** exist.

So the result draws the exact boundary between "solutions exist" and
"no solutions exist," with no symmetry assumption and no condition at
infinity [S3:71–81, S4:9].

## Graduate summary

**Main theorem (subcritical nonexistence)** [S3:71–81, S1:8954, S4:9].
For every dimension $`n\ge 2`$, positive powers $`p,q`$, and real
weights $`A,B`$, the system
$`-\Delta u=|x|^A v^p`$, $`-\Delta v=|x|^B u^q`$ for solutions that
are continuous everywhere, $`C^2`$ off the origin, and strictly
positive has **no** positive entire solution when
$`(n+A)/(p+1)+(n+B)/(q+1) > n-2`$. No symmetry assumption and no
growth condition at infinity are imposed [S3:71–81, S1:8954].

**Complementary existence (Phan's Conjecture C)** [S3:71–81].
For $`n\ge 3`$ and $`A,B>-2`$, combining the nonexistence above with
the radial existence theorem of **Bidaut-Véron and Giacomini** proves
Phan's Conjecture C in full: a positive radial entire solution exists
**exactly** when the strict inequality fails [S3:71–81].

**The formalization is T3, symmetric with the manuscript**
[S4, S5, S6, S7].
The scope note names the single manuscript [S4:5] and states the
subcritical nonexistence as the formalized result [S4:9] — the same
statement as the abstract [S3:71–81]. The comparator stub
`HenonEmden.lean` (31 lines) carries the solution/subcritical
machinery (`IsSolution`, `Subcritical` [S6:21]) and states
`theorem main_nonexistence` [S6:24] with the `sorry` at [S6:27]
(1 in this stub). The `main_results` entry [S5:1311–1313] resolves
the declaration `OAI.HenonLaneEmden.main_nonexistence` to
`lean/OAI/Analysis/HenonEmden/Main.lean` [S7] (45 lines), entry of a
96-file OAI tree carrying 0 `sorry`. The proved theorem
[S7:9–17] matches the comparator stub's statement exactly, and the
same file proves the unweighted corollary
`lane_emden_nonexistence` [S7:19–39].

**The stated exclusion.** The **critical equality case**
$`(n+A)/(p+1)+(n+B)/(q+1) = n-2`$ is **not** included
[S4:9]; the formalization covers the strict-subcritical regime only.
It does include the globally $`C^2`$ unweighted case for
$`n\ge 3`$ [S4:9].

## History of the conjecture

The **Lane–Emden equation** (Lane 1916, Emden 1907/1908) models
self-gravitating gas spheres in astrophysics, and the **Hénon** (1982)
extension adds a weight $`|x|^A`$ to the nonlinearity. The **critical
threshold** for the coupled two-unknown system is a comparison of a
weighted sum built from the dimension and the nonlinear exponents
against a dimension-dependent bound: in the regime where that sum is
large enough, no positive entire solution exists. The classical
nonexistence results for the unweighted system (the
Gidas–Spruck / Ghoussoub–Guo program) established the core cases.

The **novel contributions** are the **weighted** Hénon extension and
the **exact dichotomy** [S3:71–81, S4:9]: the subcritical
nonexistence for all real weights in dimension at least two, with the
solution regularity weakened to "continuous at the origin, classical
elsewhere" and no condition at infinity, **and** — combined with the
radial existence theorem of Bidaut-Véron and Giacomini — the full
resolution of Phan's Conjecture C (a positive radial solution exists
exactly when the strict inequality fails) [S3:71–81].

**Prior (my training data, not this repo).** As of my training cutoff,
the unweighted coupled Lane–Emden/Hénon nonexistence in the
subcritical regime was a classical result, and the weighted
Hénon–Lane–Emden extension with the weakened regularity hypothesis and
the exact weighted existence/nonexistence dichotomy was at the
frontier of the elliptic systems program. I cannot verify the
PDE analysis independently from training alone.

## Consequences

- **Subcritical nonexistence** [S3:71–81, S1:8954, S4:9]: for
  $`n\ge 2`$, $`p,q>0`$, real $`A,B`$ with
  $`(n+A)/(p+1)+(n+B)/(q+1) > n-2`$, no positive entire solution of
  the weighted Hénon–Lane–Emden system.
- **No condition at infinity** [S3:71–81, S1:8954]: solutions need
  only be continuous at the origin and $`C^2`$ elsewhere; no growth
  or symmetry hypothesis is required.
- **Exact existence criterion (Phan's Conjecture C)** [S3:71–81]:
  for $`n\ge 3`$ and $`A,B>-2`$, a positive radial entire solution
  exists exactly when the strict inequality fails.
- **Globally $``C^2`$` unweighted case included** [S4:9]: the
  formalized nonexistence covers the globally $``C^2`$` unweighted case
  for $`n\ge 3`$.
- **The critical equality case is excluded** [S4:9]: the boundary
  case $`(n+A)/(p+1)+(n+B)/(q+1) = n-2`$ is not part of the
  formalized statement.
- **The result is T3, fully formal** [S5, S6, S7]: the scope note,
  comparator stub, `main_results` entry, and a 96-file proved OAI
  tree (0 `sorry`) are all present, and the formalized statement is
  the manuscript's own theorem.

## Section skeleton

One manuscript, `build/main.tex` root (91 lines). The root declares
the theorem environments and macros inline [S3:40–50], the title at
[S3:66], the date at [S3:68], the abstract at [S3:71–81], and 6
`input` files [S3:83–88]: `01-introduction`, `02-preliminaries`,
`03-localization`, `04-intervals`, `05-pressure`,
`06-conclusion`, plus a BibTeX `references`. **No verification
bundles.**

## Coverage

The ledger row `fam=370` [S8] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=453`, `verification=0`, `trace=0`,
`companions=`. The T3 shape is "scope note, comparator stub,
`main_results` entry, and proved OAI tree (0 `sorry`)." The single
comparator stub carries 1 `sorry` [S6:27]. The shape flags are
`shapes=resolution`, `resolves_named=1`, `counterex_broad=0`,
`covmd=0` — a **resolution** of the subcritical Lane–Emden and
Hénon–Lane–Emden conjectures, with `resolves_named=1` for the named
"conjectures" in the title. No counterexample. The family has no
verification bundle and no trace. Note `paps_form=1`: the single
manuscript appears in `formalization.yaml`'s `sources:` list, and the
`main_results` entry [S5:1311–1313] resolves the declaration to the
proved OAI tree [S7] — the full T3 surface is present and the
formalized statement is the manuscript's own theorem.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8954] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 370 at [S2:843] |
| S3 | [`preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/build/main.tex`](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/build/main.tex) | 91 | the `\documentclass` root — 91 lines, theorem envs + macros [S3:40–50], title [S3:66], date [S3:68], abstract [S3:71–81], 6 `input` files [S3:83–88] |
| S4 | [`lean/docs/370.md`](../../../lean/docs/370.md) | 15 | scope note — names the single manuscript [S4:5]; Scope at [S4:9], comparator link at [S4:15] |
| S5 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry — [S5:1311–1313] |
| S6 | [`lean/ComparatorChallenges/HenonEmden.lean`](../../../lean/ComparatorChallenges/HenonEmden.lean) | 31 | comparator stub — 31 lines, `def Subcritical` [S6:21], `theorem main_nonexistence` [S6:24], `sorry` [S6:27] |
| S7 | [`lean/OAI/Analysis/HenonEmden/Main.lean`](../../../lean/OAI/Analysis/HenonEmden/Main.lean) | 45 | proved OAI declaration — 45 lines, 0 `sorry`; `theorem main_nonexistence` [S7:9–17], `theorem lane_emden_nonexistence` [S7:19–39]; 96 files under the tree |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=370`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

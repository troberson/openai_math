[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 144](../index/dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md)

# 144 — Banach's simple Lebesgue-spectrum problem

[Index page](../index/dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md)

## Original CONTENTS.md summary

The release's blurb [S1:3477] and the catalog abstract [S2:369] state
the family's claim: a smooth volume-preserving diffeomorphism of the
standard-volume three-torus has simple Lebesgue spectrum on its entire
complex mean-zero $`L^2`$ space — the bilateral iterates of one real
observable form an orthonormal basis of that space. This resolves the
probability-preserving form of Banach's simple Lebesgue-spectrum
problem within smooth dynamics. The manuscript's abstract 

> We solve the probability-preserving form of Banach's simple Lebesgue-spectrum problem in smooth dynamics. We construct a $`C^\infty`$ diffeomorphism of the three-torus that preserves standard volume and whose Koopman operator has simple Lebesgue spectrum on the entire mean-zero $`L^2`$ space. [S3:45]

## Undergraduate summary

Take a smooth, volume-preserving map of the three-torus and study how
it acts on the space of square-integrable functions
$`\{f:\mathbb T^3\to\mathbb C\}`$ with mean zero, under the
*Koopman operator* $`U f=f\circ T`$ (the function pulled back along the
map). The Koopman operator's *spectrum* describes how the dynamics
mix. *Simple Lebesgue spectrum* is the strongest mixing type: the
spectrum is a single copy of the Lebesgue measure on the unit disk,
and one single observable, together with all its iterates
$`U^nf\ (n\in\mathbb Z)`$, spans the whole space as an orthonormal
basis. Banach asked in 1932 for an example of a probability-preserving
transformation with this property; this manuscript gives one that is
smooth and volume-preserving, on the three-torus [S3:45, S4:9].

## Graduate summary

**The simple-Lebesgue-spectrum construction** [S3:45, S4:9]. The
formalization constructs a $`C^\infty`$ diffeomorphism
$`T:\mathbb T^3\to\mathbb T^3`$ preserving standard volume whose
Koopman operator has simple Lebesgue spectrum on the entire complex
mean-zero $`L^2`$ space. It gives a real-valued cyclic vector
$`\phi`$ whose integer iterates $`\{T^n\phi\}_{n\in\mathbb Z}`$
form an orthonormal basis of the mean-zero space, and an isometric
identification under which the Koopman operator becomes multiplication
by the coordinate function on the circle. The transformation is also
ergodic [S4:9].

**The mechanism.** The construction works by reducing the three-torus
dynamics to a circle model: the isometric identification makes the
Koopman operator a multiplication operator
$`(M_\zeta f)(\zeta)=\zeta f(\zeta)`$ on $`L^2(\mathbb T)`$, whose
spectrum is the single Lebesgue copy, and the cyclic vector is the
coordinate function $`\zeta`$ itself [S4:9].

## History of the conjecture

Banach raised the question of a measure-preserving transformation with
simple Lebesgue spectrum in 1932; it is one of the classical open
probes in ergodic theory, distinct from the generic existence of
mixing maps, because it asks for the *simplest possible* spectral type
(a single Lebesgue component) in a concrete setting. The
probability-preserving continuous case remained open, and this
manuscript settles it with a smooth volume-preserving example on the
three-torus [S3:45, S4:9].

**Prior (my training data, not this repo).** I know Banach's 1932
question and the spectral-type hierarchy in ergodic theory
(Lebesgue, $`K`$-automorphism, weak mixing), and I know that simple
Lebesgue spectrum is the strongest mixing type. A *smooth,
volume-preserving* diffeomorphism of the three-torus realizing simple
Lebesgue spectrum on the full mean-zero space is, to my knowledge,
not established in the literature I was trained on; the classical
examples I know are typically non-smooth or built abstractly. I cannot
independently verify this manuscript's construction.

## Consequences

**Resolution of Banach's problem (probability-preserving, smooth).**
A smooth volume-preserving diffeomorphism of the standard-volume
three-torus has simple Lebesgue spectrum on its entire mean-zero
$`L^2`$ space [S3:45, S4:9].

**A single cyclic observable.** The bilateral iterates of one real
observable form an orthonormal basis of the mean-zero space
[S2:369, S4:9].

**Circle-model isometry.** Under an isometric identification the
Koopman operator is multiplication by the circle coordinate, so the
spectrum is a single Lebesgue copy [S4:9].

## Section skeleton

One manuscript [S3:45] (title [S3:39], date [S3:41]) — `main.tex`
under `build/` plus section files; 2,183 lines total; one
`references.bib`. No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result constructs a smooth
volume-preserving diffeomorphism of the three-torus with simple
Lebesgue spectrum on the mean-zero $`L^2`$ space, a real-valued cyclic
vector whose integer iterates are an orthonormal basis, and the
isometric identification under which the Koopman operator becomes
multiplication by the circle coordinate; the transformation is also
ergodic [S4:9]. The scope note names one comparator
[S4:13–15].

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming a comparator theorem for this family, and
the manuscript is not in its `sources:` listing. The scope note and
one comparator stub exist, but the release has not registered a
single declaration as a family result. The `ThreeTorus.lean`
comparator states the conclusion as a `sorry`-terminated theorem


```lean
theorem simple_lebesgue_spectrum : MainConclusion := by
  sorry
```
[S5:82–83]

**What the OAI tree does carry.** Under the tree's
`OAI/Dynamics/` directory there is a substantial `ThreeTorus` package
(37 files over 33,818 lines, zero `sorry`) matching the comparator.
A `main_results` registration would link the scope note's comparator
to a declaration in this package, but none is registered. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
zero `sorry` in the Lean source is not a comparator pass, and the
library has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=144` records `paps 1`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes resolution`, `resolves_named 1`, `summary 1`.
The family ships one 2,183-line LaTeX manuscript, a scope note naming
one comparator, and one `sorry`-terminated comparator stub. The OAI
tree carries one unregistered formalization package
(`OAI/Dynamics/ThreeTorus`, 37 files over 33,818 lines, zero `sorry`)
matching the comparator, but no `main_results` entry links it and the
manuscript is not in `formalization.yaml`'s `sources:`. The family
ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 144 at [S1:3477] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{144} at [S2:369] |
| S3 | [`preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/main.tex`](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/main.tex) | 59 | the single manuscript root; title [S3:39], date [S3:41], abstract [S3:45] |
| S4 | [`lean/docs/144.md`](../../../lean/docs/144.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/ThreeTorus.lean`](../../../lean/ComparatorChallenges/ThreeTorus.lean) | 89 | comparator stub: the `simple_lebesgue_spectrum` theorem [S5:82] and the `sorry` [S5:83] |
| S6 | [`preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/references.bib`](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/references.bib) | 168 | the manuscript's BibTeX bibliography |

## Bibliography

- el Abdalaoui, el Houcein, Spectral ergodic Banach problem and flat polynomials (2023)
- Abdedou, Fatna, Fayad, Bassam, Kessi, Arezki, Analytic reparametrizations of translation toral flows with countable Lebesgue spectrum (2023)
- Anosov, D. V., Katok, A. B., New examples in smooth ergodic theory. Ergodic diffeomorphisms (1970)
- Fayad, Bassam R., {Partially mixing and locally rank one smooth transformations and flows on the torus {$`\mathbb T^d`$, $`d\ge3`$}} (2001)
- Fayad, Bassam, Forni, Giovanni, Kanigowski, Adam, Lebesgue spectrum of countable multiplicity for conservative flows on the torus (2021)
- Guenais, Mélanie, Morse cocycles and simple Lebesgue spectrum (1999)
- Helson, Henry, Parry, William, Cocycles and spectra (1978)
- Prikhod'ko, A. A., On ergodic flows with simple Lebesgue spectrum (2020)
- Mathew, J., Nadkarni, M. G., A measure preserving transformation whose spectrum has Lebesgue component of multiplicity two (1984)
- OpenAI, Rokhlin's multiple-mixing problem for one transformation (2026)
- Hörmander, Lars, {The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis} (2003)
- Rokhlin, V. A., Selected topics from the metric theory of dynamical systems (1949)
- Rokhlin, V. A., New progress in the theory of transformations with invariant measure (1960)
- Ulam, S. M., A Collection of Mathematical Problems (1960)
- Ma{\ n}é, Ricardo, {A proof of Pesin's formula} (1981)

[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 152](../index/dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md)

# 152 — Zero entropy does not guarantee a smooth positive-volume model

[Index page](../index/dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md)

## Original CONTENTS.md summary

The release's blurb [S1:3632] and the catalog abstract [S2:385] state
the family's claim: a zero-entropy ergodic invertible transformation of
a standard nonatomic probability space is not measurably conjugate to
any $C^\infty$ diffeomorphism preserving a strictly positive smooth
probability density on a compact finite-dimensional manifold. One
example rules out every finite dimension. The manuscript's abstract


> We construct an ergodic invertible transformation of a standard nonatomic
probability space with zero Kolmogorov–Sinai entropy that has no smooth
positive-volume model. More precisely, it is not measurably conjugate to any
$C^\infty$ diffeomorphism preserving a strictly positive smooth probability
density on a compact finite-dimensional manifold. A single example excludes
every finite dimension, including models on nonorientable manifolds and
manifolds with smooth boundary. [S3:9–15]

## Undergraduate summary

A *measure-preserving system* is a probability space with a measure-
preserving map $T$; its *entropy* (the Kolmogorov–Sinai entropy)
measures how quickly the system generates new information. A system
with *zero entropy* is the least chaotic kind — for instance, an
irrational rotation of the circle. A *smooth positive-volume model* of
such a system is a representation of it as a $C^\infty$
diffeomorphism of a compact smooth manifold $M$ that preserves some
strictly positive smooth probability density (not just the Lebesgue
measure, some smooth weight that is everywhere $>0$). The question is:
can every zero-entropy system be modelled in this geometric language?
This manuscript shows the answer is **no**: it builds one zero-entropy
ergodic system that has no such model in **any** finite dimension
[S3:9–15, S4:9].

## Graduate summary

**The obstruction (zero entropy, no smooth model)** [S3:9–15,
S4:9]. There is an ergodic invertible transformation $T$ of a standard
nonatomic probability space $(X,\mathcal B,\mu)$ with zero
Kolmogorov–Sinai entropy, such that $T$ is not measurably
conjugate (modulo null sets) to any $C^\infty$ diffeomorphism of a
compact finite-dimensional manifold preserving a strictly positive
smooth probability density. The obstruction is dimension-agnostic: the
same single example rules out models in every finite dimension,
including on nonorientable manifolds and on manifolds with smooth
boundary [S3:13–15].

**The formalized statement (finite entropy)** [S4:9, S4:11]. The
comparator `SmoothObstruction.lean` and the scope note state a related
weaker result: there is an ergodic invertible transformation of a
standard nonatomic probability space with *finite* (not necessarily
zero) Kolmogorov–Sinai entropy and no smooth positive-volume model
[S4:9, S5:90–95]. The scope note is explicit that the paper's
stronger zero-entropy conclusion is **outside** the linked statement
[S4:11]: the formalization proves the finite-entropy obstruction, not
the zero-entropy one.

**The comparison notion.** "Smooth positive-volume model" means
measurable conjugacy after discarding null sets: the system
$(X,\mathcal B,\mu,T)$ is conjugate to
$(M,\mathcal B_M,\nu,f)$ if there is a measurable
$\varphi:X\to M$ with $\varphi\circ T=f\circ\varphi$ almost
everywhere and $\varphi_\\#\mu=\nu$, where $f$ is a $C^\infty$
diffeomorphism and $\nu$ a strictly positive smooth probability
density [S5:70–89].

## History of the conjecture

The question of which measure-preserving systems admit smooth
geometric models is a central theme in ergodic theory and smooth
dynamics. For many low-entropy systems — rotations, nilflows,
Kakutani–Rokhlin towers over finite systems — one can
construct a smooth model: an irrational rotation is the linear rotation
of the circle, and certain zero-entropy systems arise as flows on
compact manifolds. The *zero-entropy* obstruction to any smooth positive-
volume model had not been established before this work; the family
asserts a construction that is ergodic, invertible, zero-entropy, and
non-modelable in every finite dimension simultaneously
[S3:9–15, S4:9].

**Prior (my training data, not this repo).** I know the
Kakutani–Rokhlin classification of zero-entropy systems, the
existence of smooth models for some zero-entropy systems (rotations,
nilflows), and the open problem of whether all zero-entropy systems
have smooth models. A *negative* answer by an explicit
construction — a single zero-entropy ergodic system with no
smooth positive-volume model in any finite dimension — is, to my
knowledge, not present in the literature I was trained on. I cannot
independently verify this manuscript's construction.

## Consequences

**Zero entropy is not sufficient for a smooth model.** There is a
zero-entropy ergodic invertible transformation with no smooth
positive-volume model in any finite dimension [S3:9–15, S4:9].

**A single example excludes all dimensions.** The same construction
rules out models on compact finite-dimensional manifolds
(orientable, nonorientable, with or without boundary) simultaneously
[S3:13–15].

**Finite entropy is the formalized foothold.** The formalization
provides the weaker finite-entropy obstruction: an ergodic invertible
transformation with finite KS entropy and no smooth positive-volume
model [S4:9, S5:90–95].

## Section skeleton

One manuscript [S3:9–15] (title [S3:3], date [S3:5]) — `main.tex`
under `build/`; 3,055 lines total; one `references.bib` plus a
`preamble.tex`. No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization constructs an ergodic
invertible transformation of a standard nonatomic probability space
with *finite* Kolmogorov–Sinai entropy that has no smooth
positive-volume model on any compact finite-dimensional manifold,
including manifolds with smooth boundary. The comparison is measurable
conjugacy after discarding null sets [S4:9]. The scope note is explicit
that the paper's stronger zero-entropy conclusion is outside the linked
statement: the formalization proves the finite-entropy obstruction, not
the zero-entropy one [S4:11]. The scope note names one comparator
[S4:15–17]: `SmoothObstruction.lean`.

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming the comparator theorem for this family, and
the manuscript is not in its `sources:` listing. The scope note and one
comparator stub exist, but the release has not registered a single
declaration as a family result. The `SmoothObstruction.lean` comparator
states the finite-entropy obstruction as a `sorry`-terminated theorem


```lean
theorem main :
    ∃ (X : Type) (_ : MeasurableSpace X) (μ : Measure X)
      (_ : IsProbabilityMeasure μ) (T : X ≃ᵐ X),
      StandardNonatomic μ ∧ Ergodic T μ ∧ FiniteKSEntropy μ T ∧
        ¬ HasSmoothPositiveVolumeModel μ T := by
  sorry
```
[S5:90–95]

The conclusion `HasSmoothPositiveVolumeModel μ T` bundles the claim
that a smooth positive-volume model exists in some finite dimension
[S5:84–89]; the comparator asserts its negation. The body is a
bare `sorry`.

**What the OAI tree does carry.** Under the tree's
`OAI/Dynamics/` directory there is a substantial `SmoothObstruction`
package (53 files over 30,090 lines, zero `sorry`) with files matching
the construction the comparison is built on (`Obstruction.lean`,
`FiniteEntropy.lean`, `Models.lean`, `ManifoldMatching.lean`,
`CoordinateTubes.lean`, `DensityBounds.lean`, `DensityLocalization.lean`,
`PhaseEntropy.lean`, `WordEntropy.lean`, `Main.lean`, `Models.lean`). A
`main_results` registration would link the scope note's comparator to a
declaration in this package, but none is registered. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=152` records `paps 1`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes density`, `resolves_named 0`, `counterex_broad 0`,
`summary 1`. The family ships one 3,055-line LaTeX manuscript, a scope
note naming one comparator (itself targeting the finite-entropy
obstruction, not the paper's stronger zero-entropy conclusion), and one
`sorry`-terminated comparator stub. The OAI tree carries one
unregistered formalization package (`OAI/Dynamics/SmoothObstruction`, 53
files over 30,090 lines, zero `sorry`) matching the comparator, but no
`main_results` entry links it and the manuscript is not in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 152 at [S1:3632] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{152} at [S2:385] |
| S3 | [`preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/build/main.tex`](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/build/main.tex) | 28 | the single manuscript root; title [S3:3], date [S3:5], abstract [S3:9–15] |
| S4 | [`lean/docs/152.md`](../../../lean/docs/152.md) | 17 | the formalization scope note: the scope paragraph [S4:9], the finite-entropy caveat [S4:11], and the comparator table [S4:15–17] |
| S5 | [`lean/ComparatorChallenges/SmoothObstruction.lean`](../../../lean/ComparatorChallenges/SmoothObstruction.lean) | 99 | comparator stub: the `main` theorem [S5:90–94] and the `sorry` [S5:95] |
| S6 | [`preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/build/references.bib`](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/build/references.bib) | 130 | the manuscript's BibTeX bibliography |

## Bibliography

- Chow, S.-N., Lin, X.-B., Palmer, K. J., A shadowing lemma with applications to semilinear parabolic equations (1989)
- Dajani, Karma, Dirksin, Sjoerd, A Simple Introduction to Ergodic Theory (2008)
- Foreman, Matthew, Weiss, Benjamin, Measure preserving diffeomorphisms of the torus are unclassifiable (2022)
- Foreman, Matthew, Rudolph, Daniel J., Weiss, Benjamin, The conjugacy problem in ergodic theory (2011)
- Gerber, Marlies, Kunde, Philipp, Non-classifiability of mixing zero-entropy diffeomorphisms up to isomorphism (2025)
- Katok, Anatole, Thouvenot, Jean-Paul, Slow entropy type invariants and smooth realization of commuting measure-preserving transformations (1997)
- Kunde, Philipp, Anti-classification results for weakly mixing diffeomorphisms (2024)
- Lind, D. A., Thouvenot, J.-P., Measure-preserving homeomorphisms of the torus represent all finite entropy ergodic transformations (1977)
- Oseledets, V. I., A multiplicative ergodic theorem. Characteristic Ljapunov exponents of dynamical systems (1968)
- Quas, Anthony, Soo, Terry, Ergodic universality of some topological dynamical systems (2016)
- Ruelle, David, An inequality for the entropy of differentiable maps (1978)
- Sason, Igal, Entropy bounds for discrete random variables via maximal coupling (2013)
- Seidel, J. J., On two-graphs, and Shult's characterization of symplectic and orthogonal geometries over GF(2) (1973)
- Smale, Stephen, Differentiable dynamical systems (1967)
- Tonchev, Vladimir D., Difference systems of sets and code synchronization (2003)

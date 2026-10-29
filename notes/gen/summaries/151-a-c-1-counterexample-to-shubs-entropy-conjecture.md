[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 151](../index/dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md)

# 151 — A $C^1$ counterexample to Shub’s entropy conjecture

[Index page](../index/dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:3616] and the catalog abstract [S2:383] state
the family's claim: a noninvertible $`C^1`$ self-map of a compact smooth
manifold has zero topological entropy but eigenvalue $`2`$ on second
homology. This disproves the homological entropy lower bound for general
$`C^1`$ self-maps — homological growth need not force positive orbit
complexity. The manuscript's abstract 

> We disprove the general $`C^1`$ self-map formulation of Shub's entropy
conjecture. We construct a noninvertible $`C^1`$ self-map of a compact
smooth manifold without boundary whose topological entropy is zero,
while its action on second real homology has eigenvalue $`2`$. Thus the
topological entropy is strictly smaller than the logarithm of the
homological spectral radius. [S3:40–45]

## Undergraduate summary

Take a smooth map $`f`$ of a compact manifold $`M`$ and study two
"complexity" numbers. The *topological entropy* measures how fast
distinct orbits of $`f`$ separate — zero entropy means the dynamics
are not actually orbit-complex, no matter how the map looks under a
lens. The *action on homology* is the linear map $`f_*`$ that $`f`$ induces
on the manifold's $`H_2(M;\mathbb R)`$: its *spectral radius* $`\rho`$
measures how quickly the map stretches cycles in the second homology
group. Shub's entropy conjecture says a smooth self-map's topological
entropy is at least $`\log \rho`$ — homological growth must force
positive orbit complexity. This manuscript shows that for general $`C^1`$
(invertible-not-required) self-maps the bound fails: one can build a
noninvertible $`C^1`$ map with zero topological entropy and eigenvalue $`2`$
on second homology, so $`\log \rho=\log 2>0`$ while the entropy is
$`s=0`$ [S3:40–45, S4:9].

## Graduate summary

**The counterexample statement** [S3:40–45, S4:9]. There exists a
compact smooth manifold without boundary $`M`$ (built from the comparator's
`CounterexampleManifold q` family, $`q\ge2`$) and a noninvertible $`C^1`$
self-map $`f:M\to M`$ with:

- Topological entropy $`h_{\mathrm{top}}(f)=0`$ (the comparator states
  this as
  `Dynamics.coverEntropy f (Set.univ) = (0 : EReal)`);
- A nonzero eigenvector $`v\in H_2(M;\mathbb R)`$ with
  $`f_*v=2 v`$ (the comparator's
  `realHomologyMap 2 f hf.1 v = (2 : ℝ) • v`);
- Hence the total-real-homology spectral radius satisfies
  $`\rho(f_*)\ge2`$, so $`\log \rho\ge\log 2>0`$;
- $`f`$ is genuinely noninvertible
  (`¬ Function.Bijective f`).

Together $`h_{\mathrm{top}}(f)=0<\log \rho(f_*)`$, disproving the
general $`C^1`$ self-map version of Shub's lower bound [S4:9]. The
comparator's theorem `exists_C1_entropy_counterexample` is a
`sorry`-terminated statement of exactly these conjuncts
[S5:65–67].

**What the bound is, and where it survives.** Shub's entropy conjecture
is a statement about the *general* $`C^1`$ self-map version; a positive
answer for homeomorphisms, or for smooth maps with some additional
hypothesis (e.g. invertibility), is a strictly stronger regime. The
counterexample shows the lower bound fails once invertibility is
dropped — the map can be topologically zero-entropy while
stretching a homology class by a factor of $`2`$ at each iteration
[S4:9].

## History of the conjecture

Shub's entropy conjecture (1970s) is one of the classical links
between the orbit complexity of a dynamical system and the linear
algebra of its action on homology. It is often quoted as
$`h_{\mathrm{top}}(f)\ge\log \rho(f_*)`$ for a smooth self-map $`f`$ of
a compact smooth manifold, and it is *known* for homeomorphisms of
finite CW complexes, for algebraic maps of projective varieties, and
for other special classes. The conjecture in its full $`C^1`$ self-map
form had resisted proof: this manuscript asserts a counterexample
[S3:40–45, S4:9].

**Prior (my training data, not this repo).** I know Shub's entropy
conjecture, the known cases (homeomorphisms, algebraic maps, maps with
finite entropy), and that the general $`C^1`$ form is where the
conjecture is often stated most strongly. A *negative* answer to the
general $`C^1`$ form by an explicit $`C^1`$ construction $`f`$ with
$`h_{\mathrm{top}}(f)=0`$ and $`\rho(f_*)\ge2`$ on $`H_2`$ is, to my
knowledge, not established in the literature I was trained on; the
known positive results go in the other direction, and I do not recall
a negative result of this shape in the $`C^1`$ self-map regime. I cannot
independently verify this manuscript's construction.

## Consequences

**Shub's lower bound fails for general $`C^1`$ self-maps.** The
topological entropy of a $`C^1`$ self-map is not in general bounded below
by the log spectral radius of its action on homology
[S3:40–45, S4:9].

**A concrete counterexample.** There is a compact smooth manifold
without boundary $`M`$ and a noninvertible $`C^1`$ self-map $`f`$ with
$`h_{\mathrm{top}}(f)=0`$ and $`\rho(f_*)\ge2`$ on $`H_2(M;\mathbb R)`$
[S4:9, S5:65–67].

**Invertibility is a genuine constraint.** The counterexample is
noninvertible; the positive cases of the conjecture (homeomorphisms,
algebraic maps) keep invertibility as a hypothesis, and the negative
result locates exactly the gap the invertibility assumption closes
[S5:65–67].

## Section skeleton

One manuscript [S3:40–45] (title [S3:33], date [S3:35]) — `main.tex`
under `build/source/`; 1,160 lines total; one `references.bib`. No
manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization gives a counterexample to the
general $`C^1`$ self-map formulation of Shub's entropy conjecture: a
noninvertible $`C^1`$ map on a compact smooth manifold without boundary
has topological entropy zero, while its action on second real homology
has a nonzero eigenvector with eigenvalue $`2`$, so the homological lower
bound
$`\log \rho(f_*)\ge\log 2>0`$ strictly exceeds
$`h_{\mathrm{top}}(f)=0`$ [S4:9]. The scope note names one comparator
[S4:13–15]: `C1EntropyCounterexample.lean`.

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming the comparator theorem for this family, and
the manuscript is not in its `sources:` listing. The scope note and one
comparator stub exist, but the release has not registered a single
declaration as a family result. The `C1EntropyCounterexample.lean`
comparator states the counterexample as a `sorry`-terminated theorem


```lean
theorem exists_C1_entropy_counterexample :
    ∃ q : ℕ, 0 < q ∧ ∃ f : CounterexampleManifold q → CounterexampleManifold q, ∃ hf : IsC1SelfMap q f, Dynamics.coverEntropy f (Set.univ : Set (CounterexampleManifold q)) = (0 : EReal) ∧ (∃ v : RealSingularHomology 2 (CounterexampleManifold q), v ≠ 0 ∧ realHomologyMap 2 f hf.1 v = (2 : ℝ) • v) ∧ 0 < Real.log (2 : ℝ) ∧ Real.log (2 : ℝ) ≤ Real.log (totalRealHomologySpectralRadius f hf.1) ∧ ¬ Function.Bijective f ∧ 5 ≤ 2 * q + 3 := by
  sorry
```
[S5:65–67]

**What the OAI tree does carry.** Under the tree's
`OAI/Dynamics/` directory there is a substantial `EntropyCounterexample`
package (184 files over 19,869 lines, zero `sorry`) with files matching
the construction the comparison is built on
(`Counterexample.lean`, `CounterexampleEntropy.lean`,
`EntropyBounds.lean`, `SpectralRadius.lean`, `EigenpairBound.lean`,
`SphereGeometry.lean`, the `Clock*` and `Map*` certificate files,
`C1Conjugacy.lean`, `C1Retraction.lean`, `MapEntropyComplete.lean`). A
`main_results` registration would link the scope note's comparator to a
declaration in this package, but none is registered. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library has
not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=151` records `paps 1`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes counterexample|bound`, `resolves_named 1`,
`counterex_broad 1`, `summary 1`. The family ships one 1,160-line LaTeX
manuscript, a scope note naming one comparator, and one
`sorry`-terminated comparator stub. The OAI tree carries one
unregistered formalization package (`OAI/Dynamics/EntropyCounterexample`,
184 files over 19,869 lines, zero `sorry`) matching the comparator, but
no `main_results` entry links it and the manuscript is not in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 151 at [S1:3616] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{151} at [S2:383] |
| S3 | [`preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/main.tex`](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/main.tex) | 171 | the single manuscript root; title [S3:33], date [S3:35], abstract [S3:40–45] |
| S4 | [`lean/docs/151.md`](../../../lean/docs/151.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/C1EntropyCounterexample.lean`](../../../lean/ComparatorChallenges/C1EntropyCounterexample.lean) | 73 | comparator stub: the `exists_C1_entropy_counterexample` theorem [S5:65–66] and the `sorry` [S5:67] |
| S6 | [`preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/references.bib`](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/references.bib) | 128 | the manuscript's BibTeX bibliography |

## Bibliography

- Gromov, M., Entropy, homology and semialgebraic geometry (1987)
- Hatcher, Allen, Algebraic Topology (2002)
- Liao, Gang, Viana, Marcelo, Yang, Jiagang, The entropy conjecture for diffeomorphisms away from tangencies (2013)
- Manning, Anthony, Topological entropy and the first homology group (1975)
- Manning, Anthony, Topological entropy and homology (1976)
- Misiurewicz, Michal, Przytycki, Feliks, Topological entropy and degree of smooth mappings (1977)
- Misiurewicz, Michal, A short proof of the variational principle for a $`\mathbb Z_+^N`$ action on a compact space (1976)
- Saghin, Radu, Xia, Zhihong, The entropy conjecture for partially hyperbolic diffeomorphisms with 1-D center (2010)
- Shub, Michael, Dynamical systems, filtrations and entropy (1974)
- Shub, Michael, All, most, some differentiable dynamical systems (2007)
- Yomdin, Y., Volume growth and entropy (1987)

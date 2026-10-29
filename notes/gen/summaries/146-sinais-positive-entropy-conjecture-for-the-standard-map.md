[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 146](../index/dynamical-systems-and-ergodic-theory/146-sinais-positive-entropy-conjecture-for-the-standard-map.md)

# 146 — Sinai's positive-entropy conjecture for the standard map

[Index page](../index/dynamical-systems-and-ergodic-theory/146-sinais-positive-entropy-conjecture-for-the-standard-map.md)

## Original CONTENTS.md summary

The release's blurb [S1:3509] and the catalog abstract [S2:373] state
the family's claim: the standard sine map on the two-dimensional torus
has positive metric entropy with respect to area for every
sufficiently large positive parameter — Sinai's
positive-parameter-measure conjecture for the original family, with the
stronger conclusion of a full parameter tail. The manuscript's abstract


> We prove that the standard sine map of the two-dimensional torus has
positive metric entropy with respect to normalized area for every
sufficiently large positive parameter. This gives a full parameter tail,
and hence answers Sinai's positive-parameter-measure conjecture
affirmatively. [S3:60–64]

## Undergraduate summary

The *standard map* is the family of area-preserving twist maps of the
two-torus
$`(x,y)\mapsto(x+y+\lambda\sin 2\pi y,\ y+\lambda\sin 2\pi y)`$
(parametrized by the strength $`\lambda`$). It is the archetypal model
for how a smooth area-preserving map develops chaos as $`\lambda`$
grows: small $`\lambda`$ is mostly regular islands, large $`\lambda`$ is
expected to be mostly chaotic. Chaos here means *positive metric
entropy* — the rate at which a typical point forgets its past.
Sinai asked (conjecturally) that for the original family, every
sufficiently large positive $`\lambda`$ gives positive entropy with
respect to area. This manuscript settles that, with the stronger
statement that the conclusion holds for the whole tail of large
parameters [S3:60–64].

## Graduate summary

**Positive metric entropy on a parameter tail** [S3:60–64,
S4:9]. For every sufficiently large positive parameter $`\lambda`$, the
standard sine map
$`T_\lambda`$ has positive metric entropy with respect to normalized
area. This is a full parameter tail, not a sparse set of parameters:
the threshold is some absolute $`\Lambda_0`$ and every
$`\lambda\ge\Lambda_0`$ works [S4:9]. No genericity assumption on the
parameter is used [S4:11].

**The hyperbolic mechanism.** The proof builds a positive-area
invariant ergodic hyperbolic component for large $`\lambda`$. That
component splits into finitely many cyclic pieces on each of which the
corresponding iterate is Bernoulli; a Bernoulli (hence positive-
entropy) invariant measure of positive area forces the area measure to
carry positive entropy [S4:11]. The companion statements carry positive
largest Lyapunov exponent with the stated derivative-growth limit
[S4:9].

## History of the conjecture

The standard map, introduced by standard-map models of Hamiltonian
dynamics, is the canonical route from regular to chaotic
area-preserving motion. Sinai's positive-entropy conjecture for the
original family — that large $`\lambda`$ forces positive metric
entropy with respect to the invariant area measure — was open.
Related results establish chaos for *generic* or *most* parameters,
and positive Lyapunov exponents on large sets, but the full-tail,
area-measure statement for the original family is what this manuscript
asserts [S3:60–64, S4:11].

**Prior (my training data, not this repo).** I know the standard map
as a model, the positive-entropy / positive-Lyapunov heuristics for
large $`\lambda`$, and that generic-parameter chaos results exist. A
*full parameter tail* result giving positive metric entropy with
respect to the invariant area measure (rather than a generic set) is,
to my knowledge, not established in the literature I was trained on;
the area-measure (not merely a positive-measure sub-set) conclusion is
the delicate part. I cannot independently verify this manuscript's
argument.

## Consequences

**Sinai's positive-entropy conjecture (original family).** The
standard sine map has positive metric entropy with respect to area for
every sufficiently large positive parameter — a full parameter
tail [S3:60–64, S4:9].

**A positive-area hyperbolic component.** The proof constructs a
positive-area invariant ergodic hyperbolic component, splitting into
finitely many cyclic Bernoulli pieces [S4:11].

**Positive Lyapunov exponent.** The largest Lyapunov exponent is
positive on a positive-area set, with the stated derivative-growth
limit [S4:9].

## Section skeleton

One manuscript [S3:60–64] (title [S3:54], date [S3:56]) — `paper.tex`
under `build/` plus section files; 3,404 lines total; a
`thebibliography` block in `references.tex`. No manuscript ships a
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result proves Sinai's
positive-entropy conjecture for the standard sine map in the stronger
full-parameter-tail form: for every sufficiently large parameter,
normalized area has positive metric entropy, and a positive-area set
has positive largest Lyapunov exponent with the stated derivative-
growth limit [S4:9]. It also constructs a positive-area invariant
ergodic hyperbolic component, splitting into finitely many cyclic
pieces on each of which the corresponding iterate is Bernoulli, with
no genericity assumption on the parameter [S4:11]. The scope note
names three comparators [S4:15–19].

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming a comparator theorem for this family, and
the manuscript is not in its `sources:` listing. The scope note and
three comparator stubs exist, but the release has not registered a
single declaration as a family result. The `StandardMapEntropy.lean`
comparator states the positive-entropy obligation as a
`sorry`-terminated theorem 

```lean
theorem main_entropy : MainObligation := by
  sorry
```
[S5:48–49]

**What the OAI tree does carry.** Under the tree's
`OAI/Dynamics/` directory there is a large `StandardMap` package (274
files over 54,864 lines, zero `sorry`), with subpackages
(`Entropy`, `Components`, `Coupling`, `Coding`, `Towers`, `Lyapunov`,
`Stable`, `Holonomy`, `Bernoulli`) matching the three comparators. A
`main_results` registration would link the scope note's three
comparators to declarations in this package, but none is registered.
The release records `scope: "Partial progress."` and
`review: status: unchecked`; zero `sorry` in the Lean source is not a
comparator pass, and the library has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=146` records `paps 1`, `paps_form 0`,
`tier T2`, `chal 3`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes uniform`, `resolves_named 1`, `summary 1`. The
family ships one 3,404-line LaTeX manuscript, a scope note naming
three comparators, and three `sorry`-terminated comparator stubs. The
OAI tree carries one unregistered formalization package
(`OAI/Dynamics/StandardMap`, 274 files over 54,864 lines, zero
`sorry`) with subpackages matching the three comparators, but no
`main_results` entry links them and the manuscript is not in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 146 at [S1:3509] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{146} at [S2:373] |
| S3 | [`preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/build/paper.tex`](../../../preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/build/paper.tex) | 75 | the single manuscript root; title [S3:54], date [S3:56], abstract [S3:60–64] |
| S4 | [`lean/docs/146.md`](../../../lean/docs/146.md) | 19 | the formalization scope note: the scope paragraph [S4:9], the component paragraph [S4:11], and the three-row comparator table [S4:15–19] |
| S5 | [`lean/ComparatorChallenges/StandardMapEntropy.lean`](../../../lean/ComparatorChallenges/StandardMapEntropy.lean) | 53 | comparator stub: the `main_entropy` theorem [S5:48] and the `sorry` [S5:49] |
| S6 | [`preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/build/references.tex`](../../../preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/build/references.tex) | 122 | the manuscript's `thebibliography` block |

## Bibliography

- M. Bestvina, _Real trees in topology, geometry, and group theory_, arXiv:math/9712210v1 (1997). arXiv:math/9712210v1.
- A. Blumenthal, _Statistical properties for compositions of standard maps with increasing coefficient_, Ergodic Theory and Dynamical Systems **41** (2021), no. 4, 981–1024. doi:10.1017/etds.2019.115.
- A. Blumenthal, J. Xue, and L.-S. Young, _Lyapunov exponents for random perturbations of some area-preserving maps including the standard map_, Annals of Mathematics **185** (2017), no. 1, 285–310. doi:10.4007/annals.2017.185.1.5.
- P. Berger and P. D. Carrasco, _Non-uniformly hyperbolic diffeomorphisms derived from the standard map_, Communications in Mathematical Physics **329** (2014), no. 1, 239–262. doi:10.1007/s00220-014-1932-1.
- B. V. Chirikov, _A universal instability of many-dimensional oscillator systems_, Physics Reports **52** (1979), no. 5, 263–379. doi:10.1016/0370-1573(79)90023-1.
- P. Duarte, _Plenty of elliptic islands for the standard family of area preserving maps_, Annales de l'Institut Henri Poincaré. Analyse non linéaire **11** (1994), no. 4, 359–409. Official article record.
- A. Gorodetski, _On stochastic sea of the standard map_, Communications in Mathematical Physics **309** (2012), no. 1, 155–192. doi:10.1007/s00220-011-1365-z.
- A. Katok, in collaboration with K. Burns, _Infinitesimal Lyapunov functions, invariant cone families and stochastic properties of smooth dynamical systems_, Ergodic Theory and Dynamical Systems **14** (1994), 757–785. doi:10.1017/S0143385700008142.
- K. Bloor and S. Luzzatto, _Some remarks on the geometry of the standard map_, International Journal of Bifurcation and Chaos **19** (2009), no. 7, 2213–2232. doi:10.1142/S0218127409024025.
- M. Holland and S. Luzzatto, _Stable manifolds under very weak hyperbolicity conditions_, Journal of Differential Equations **221** (2006), no. 2, 444–469. doi:10.1016/j.jde.2005.07.013.
- R. Ma\ né, _A proof of Pesin's formula_, Ergodic Theory and Dynamical Systems **1** (1981), no. 1, 95–102. doi:10.1017/S0143385700001188.
- R. Ma\ né, _Errata to A proof of Pesin's formula_, Ergodic Theory and Dynamical Systems **3** (1983), no. 1, 159–160. doi:10.1017/S0143385700001863.
- D. Obata, _Uniqueness of the measure of maximal entropy for the standard map_, Commentarii Mathematici Helvetici **96** (2021), no. 1, 79–111. doi:10.4171/CMH/508.
- F. Oliveira, _Positive topological entropy for the Standard Map_, arXiv:2404.02209v2 (2024). arXiv:2404.02209.
- V. I. Oseledets, _A multiplicative ergodic theorem. Lyapunov characteristic numbers for dynamical systems_, Transactions of the Moscow Mathematical Society **19** (1968), 197–231. Official bibliographic record.
- Ya. B. Pesin, _Characteristic Lyapunov exponents and smooth ergodic theory_, Russian Mathematical Surveys **32** (1977), no. 4, 55–114. doi:10.1070/RM1977v032n04ABEH001639.
- P. Berger and D. Turaev, _On Herman's positive entropy conjecture_, Advances in Mathematics **349** (2019), 1234–1288. doi:10.1016/j.aim.2019.04.002.

[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 232](../index/probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md)

# 232 — Gaussian fields and SLE interfaces for Lipschitz heights

[Index page](../index/probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md)

## Original CONTENTS.md summary

[S1:5598] (family entry):

> **232. Gaussian fields and interfaces for triangular-lattice Lipschitz heights.** Proves Gaussian free field limits on bounded smooth simply connected domains for triangular-lattice height models: uniform odd heights with increments $`0,\pm2`$ and two-arc boundary values $`\pm1`$, and zero-boundary integer Lipschitz heights weighted by fixed $`x\in[1/\sqrt2,1]`$. Uniform real Lipschitz heights also converge to a Gaussian field; at a tuned opposite-boundary amplitude, their interface converges to chordal $`\mathrm{SLE}_4`$, establishing Schramm’s real-field/interface predictions.

[S2:549] carries the `\resultentry`, so the release blurb and the overview agree.
The three manuscripts:

**Weighted integer heights** [S3:40, S3:42]:

> 1

**Integer heights with two-arc boundary** [S4:99, S4:101]:

> 2

**Uniform real Lipschitz surfaces** [S5:37, S5:39]:

> 3

## Undergraduate summary

A **Lipschitz height function** on the triangular lattice is an integer-
valued function on the faces such that neighboring faces differ by at
most one. The **Gaussian free field** (GFF) is the canonical random
field in two dimensions, analogous to Brownian motion in one
dimension. These results show that, on smooth simply connected
domains, properly scaled random height functions converge to a
multiple of the GFF. One of the three results goes further: at a
tuned boundary amplitude, the **interface** (the boundary between
positive and negative height regions) converges to a
**Schrämm–Loewner evolution** curve,
a random fractal curve that is the conformally invariant
limit of many lattice models [S3:46–55, S4:104–107,
S5:42–51, S2:549].

## Graduate summary

**Weighted integer heights**
[S3:46–55, S2:549]. On bounded smooth simply connected
domains, the zero-boundary weighted integer Lipschitz height
function with edge weight $`x`$ for each changing edge converges,
after division by a positive constant depending only on $`x`$,
to the zero-Dirichlet Gaussian free field, for every fixed
$`x\in[1/\sqrt2,1]`$. The convergence is in the sense of random
distributions under inside lattice approximations with uniformly
convergent boundary parametrizations. This includes the uniform
height model ($`x=1`$) and the predicted critical endpoint
($`x=1/\sqrt2`$).

**Integer heights with two-arc boundary**
[S4:104–107, S2:549]. The centered uniform odd integer
height function on triangular-lattice approximations of a smooth
simply connected domain, with neighboring differences zero or
two and boundary values $`+1`$ and $`-1`$ on two arcs, converges to
a universal multiple of the Dirichlet Gaussian free field. This
resolves the field part of Schramm’s Problem 2.2. An
absolutely convergent finite-volume formula for the
normalization is given. The proof combines reflection positivity,
a spectral sum rule, and boundary comparison with Gaussian
moment identities.

**Uniform real Lipschitz surfaces**
[S5:42–51, S2:549]. The centered uniformly sampled real
nearest-neighbor Lipschitz height function on the triangular
lattice converges as a random distribution to a multiple of the
Dirichlet Gaussian free field. At one tuned two-arc boundary
amplitude, the zero-height interface converges in uniform
curve distance to chordal $`\mathrm{SLE}_4`$. This resolves
Schramm’s Problem 2.3. The relation between the field
variance and the boundary height is identified in terms of an
implicit stationary tangent-flux coefficient.

## History of the conjecture

**Schramm’s Problem 2.2** asked for the Gaussian free
field limit of the uniform odd integer height model on the
triangular lattice with two-arc boundary data. The
**Schramm’s Problem 2.3** asked for the GFF and SLE
scaling limits of uniformly sampled real Lipschitz heights.
The **weighted integer** result [S3:46–55] provides
a one-parameter family of GFF limits, including the
uniform model and the critical endpoint. The
two-arc boundary result [S4:104–107]
resolves the field part of Problem 2.2. The
real Lipschitz result [S5:42–51]
resolves Problem 2.3 in full, including the SLE$`_4`$
interface convergence.

**Prior (my training data, not this repo).** The Gaussian
free field, SLE, and the general framework of height
models on lattices are well-established. The GFF limits for
the three specific height models and the SLE$`_4`$ interface
convergence are the novel contributions. I cannot confirm
these independently from training alone.

## Consequences

- **The weighted GFF limit**
  [S3:46–55]: zero-boundary weighted integer
  Lipschitz heights converge to the GFF for every
  $`x\in[1/\sqrt2,1]`$, including the uniform and
  critical cases.
- **The two-arc boundary GFF limit**
  [S4:104–107]: uniform odd integer heights with
  two-arc boundary data converge to a universal GFF
  multiple, resolving Schramm’s Problem 2.2
  (field part).
- **The real Lipschitz GFF and SLE$`_4`$ limits**
  [S5:42–51]: uniform real Lipschitz heights
  converge to the GFF, and at the tuned amplitude
  the zero-height interface converges to chordal
  SLE$`_4`$, resolving Schramm’s Problem 2.3.

## Section skeleton

Three manuscripts: [S3] (title [S3:40], date [S3:42])
— `main.tex` under `build/` with `sections/`;
[S4] (title [S4:99], date [S4:101]) —
`paper.tex` under `build/` with `sections/`;
[S5] (title [S5:37], date [S5:39]) —
`paper.tex` under `build/` with `sections/`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release does **not** formalise this family. There is
no scope note, no comparator stub, no `main_results` entry,
and no OAI tree. The ledger tier is T0. The reading is of
source text only.

## Coverage

The ledger row `fam=232` [S6] records the tier and the
counts: `tier=T0`, `paps=3`, `paps_form=0`, `chal=0`,
`mainres=0`, `scope_note=0`, `verification=0`, `trace=`.
No formalization. No verification bundle. No reasoning
trace. The shape flags are `bound|uniform`, and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5598] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 232 at [S2:549] |
| S3 | [`preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/build/main.tex`](../../../preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/build/main.tex) | 73 | manuscript 1 of 3 (weighted integer heights); title [S3:40], date [S3:42], abstract [S3:46–55] |
| S4 | [`preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/build/paper.tex`](../../../preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/build/paper.tex) | 120 | manuscript 2 of 3 (integer heights with two-arc boundary); title [S4:99], date [S4:101], abstract [S4:104–107] |
| S5 | [`preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/build/paper.tex`](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/build/paper.tex) | 374 | manuscript 3 of 3 (uniform real Lipschitz surfaces); title [S5:37], date [S5:39], abstract [S5:42–51] |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=232`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- S. Buchholz, C. Cotar and F. Schweiger, _Gradient Gibbs measures with non-convex potentials and the universality class of the Gaussian Free Field_, arXiv:2608.14526v1 (2026). .
- G. Giacomin, S. Olla and H. Spohn, _Equilibrium fluctuations for $`\nabla\varphi`$ interface model_, Annals of Probability **29** (2001), 1138–1172. .
- R. F. Bass and P. Hsu, _The semimartingale structure of reflecting Brownian motion_, Proceedings of the American Mathematical Society **108** (1990), 1007–1010, Theorem 1.
- J. Miller, _Universality for SLE(4)_, arXiv:1010.1356v1 (2010). .
- J. Miller, _Fluctuations for the Ginzburg–Landau $`\nabla\phi`$ interface model on a bounded domain_, Communications in Mathematical Physics **308** (2011), 591–639. . .
- L. Sł omiński, _On existence, uniqueness and stability of solutions of multidimensional SDE's with reflecting boundary conditions_, Annales de l'Institut Henri Poincare, Probabilites et Statistiques **29** (1993), 163–198, Section 2, Corollaries 3–4. .
- O. Cohen-Alloro and R. Peled, _Rarity of extremal edges in random surfaces and other theoretical applications of cluster algorithms_, Annals of Applied Probability **30** (2020), 2439–2464. Theorem 1.1 in arXiv:1711.00259v2. . .
- P. Mił oś and R. Peled, _Delocalization of two-dimensional random surfaces with hard-core constraints_, Communications in Mathematical Physics **340** (2015), 1–46. . .
- A. Prékopa, _On logarithmic concave measures and functions_, Acta Scientiarum Mathematicarum (Szeged) **34** (1973), 335–343, Theorems 3 and 6. .
- T. Radó, _Sur la représentation conforme de domaines variables_, Acta Scientiarum Mathematicarum (Szeged) **1** (1923), 180–186, Section 1, theorem on p. 182. .
- T. Richthammer, _Translation-invariance of two-dimensional Gibbsian point processes_, Communications in Mathematical Physics **274** (2007), 81–122. . .
- S. Rohde and O. Schramm, _Basic properties of SLE_, Annals of Mathematics **161** (2005), 883–924. . .
- O. Schramm, _Conformally invariant scaling limits (an overview and a collection of problems)_, International Congress of Mathematicians, Vol. I, European Mathematical Society (2007), 513–543, Problem 2.3, p. 528. . .
- O. Schramm and S. Sheffield, _Contour lines of the two-dimensional discrete Gaussian free field_, Acta Mathematica **202** (2009), 21–137. Detailed locators refer to arXiv:math/0605337v3 (2008). . .
- O. Schramm and S. Sheffield, _A contour line of the continuum Gaussian free field_, Probability Theory and Related Fields **157** (2013), 47–80. . .
- S. Sheffield, _Random surfaces_, Astérisque **304** (2005), vi+175 pp. .
- A. Naddaf and T. Spencer, _On homogenization and scaling limit of some gradient perturbations of a massless free field_, Communications in Mathematical Physics **183** (1997), 55–84. .
- T. J. Lyons and W. Zheng, _A crossing estimate for the canonical process on a Dirichlet space and a tightness result_, Asterisque **157–158** (1988), 249–271, Section 1, equations (1.2)–(1.5). .

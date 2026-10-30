[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 221](../index/probability-and-statistical-mechanics/221-mezard-parisi-formula-for-diluted-spin-glasses.md)

# 221 — The Mézard–Parisi formula for diluted spin glasses

[Index page](../index/probability-and-statistical-mechanics/221-mezard-parisi-formula-for-diluted-spin-glasses.md)

## Original CONTENTS.md summary

[S1:5229] (family entry):

> **221. The M\'ezard–Parisi formula for diluted spin glasses.** Proves the M\'ezard–Parisi hierarchical cavity formula for Poisson-diluted even-arity Ising models satisfying the Panchenko–Talagrand factorization and positivity assumptions, with only first-moment integrability. The limiting free energy equals the infimum over finite-depth hierarchical trial laws. This includes the Viana–Bray model, symmetric diluted even-spin models, and weighted soft even-$`K`$ satisfiability. ([Lean](../../../lean/docs/221.md))

[S2:527] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript [S3:49, S3:51]:

> We prove the Mézard–Parisi hierarchical cavity formula for diluted
even-arity Ising models in the Panchenko–Talagrand class. This resolves
the variational equality conjecture for that class: the limiting pressure
equals the infimum of the trial functional over all finite hierarchy depths
and trial laws. Only first moments of the interaction and external field
are required. [S3:54–61]

## Undergraduate summary

A **spin glass** is a disordered magnetic material where the spins (tiny
magnets) interact through a random network of couplings. The **free
energy** (or pressure) measures the thermodynamic cost of the system at
a given temperature. The **M\'ezard–Parisi formula** is a
hierarchy of nested trial distributions that, when optimized, gives the
exact free energy of a spin glass in the thermodynamic limit (infinitely
large system). The "diluted" version means the interaction network is
sparse: each spin talks to a Poisson-distributed number of neighbors
rather than all others. The paper proves this formula for the
Panchenko–Talagrand class of diluted even-arity Ising models
[S3:55–60, S2:527].

## Graduate summary

**Main theorem** (the M\'ezard–Parisi variational
equality) [S3:55–60, S2:527]. For Poisson-diluted
even-arity Ising models in the Panchenko–Talagrand class
(factorization, independence, integrability, and positivity),
the limiting pressure equals
$`\inf_{r,\zeta,m} \phi(r,\zeta,m)`$
— the infimum of the trial functional over all finite
hierarchy depths $`r`$, hierarchical trial laws $`\zeta`$, and
exponent vectors $`m`$. Only first-moment integrability of
the interaction and external field is required. The theorem
includes the Viana–Bray model, symmetric diluted
even-spin models, and weighted soft even-$`K`$ satisfiability.

The scope note [S5:9] states: "the formalization proves the
M\'ezard–Parisi hierarchical cavity formula for diluted
even-arity Ising models in the Panchenko–Talagrand class.
Under the class's factorization, independence, integrability,
and positivity assumptions, the finite-system pressure converges
to the infimum of the trial functional over all finite hierarchy
depths and trial laws. The arity is any even integer at least
two and the interaction density is positive."

## History of the conjecture

The **M\'ezard–Parisi formula** (1985, 1987) was proposed
as the solution to the Sherrington–Kirkpatrick (SK) spin
glass model. Its rigorous proof for the fully connected SK model
was completed by Parisi (2006). The **diluted** extension replaces
the fully connected interaction with a Poisson-diluted one,
yielding a sparser, more physically realistic model. The
**Panchenko–Talagrand class** (2014, 2015) identifies the
structural conditions (factorization and positivity) under which
the variational formula extends beyond the SK model to a broader
family of diluted models. This paper proves the formula for
that class with only first-moment integrability [S3:55–60,
S2:527].

**Prior (my training data, not this repo).** The M\'ezard–Parisi
formula for the SK model, the Parisi order parameter, and the
Panchenko–Talagrand characterization are standard in spin glass
theory. The extension to the full Panchenko–Talagrand class with
only first-moment integrability is the novel contribution. I cannot
confirm this result independently from training alone.

## Consequences

- **The variational equality for the Panchenko–Talagrand
  class** [S3:55–60]: the limiting pressure equals the
  infimum of the trial functional over all finite hierarchy depths
  and trial laws — the M\'ezard–Parisi formula holds
  for the full class, not just the SK model.
- **First-moment sufficiency.** No boundedness, no higher moments:
  only first-moment integrability of the interaction and field is
  required [S3:55–60].
- **Covers named models.** The Viana–Bray model, symmetric
  diluted even-spin models, and weighted soft even-$`K`$
  satisfiability all fall within the class [S2:527].

## Section skeleton

One manuscript [S3:54–61]: `main.tex` under `build/`, with sections
under `build/sections/` (introduction, model, overview, trees,
upper, cavity, perturbations). The shipped PDF [S4] is the
manuscript in the form the release distributes. The family also
ships a published reasoning trace [S7] (LaTeX source and PDF).

## Comparison with the formalized statement

The release formalises this family at tier T2 with one scope note
[S5:9] and one comparator stub [S6], but **no** `main_results`
entry and **no** OAI tree. The scope note [S5:9] describes the
target: the M\'ezard–Parisi hierarchical cavity formula
for the Panchenko–Talagrand class. The comparator stub
[S6] states the target theorem: "theorem mezard_parisi {p :
\mathbb N} (M : Model p) (hM : Admissible M) : Tendsto
(pressure M) atTop (\mathcal N (variationalValue M)) := by"
[S6:148–149] and ends in `sorry` at [S6:150]. No proved
copy exists under `lean/OAI/`. The gap is the formalization
itself: the release set the target and described the scope, but
shipped no proof. The reading is of source text only.

## Coverage

The ledger row `fam=221` [S8] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `verification=0`, `trace=mezard-parisi-formula`.
The T2 shape is "scope note and comparator stub exist, no
formalization": the release identified the target theorem,
wrote a scope note, and created a challenge stub with `sorry`,
but did not produce a `main_results` entry or an OAI proof. The
reasoning trace [S7] is the release's published record of the
formalization attempt. There is no verification bundle.
The shape flags are empty (no `resolution` tag fires), and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5229] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 221 at [S2:527] |
| S3 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex) | 75 | the manuscript; title [S3:49], date [S3:51], abstract [S3:54–60] |
| S4 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf) | 14733 | the manuscript as shipped |
| S5 | [`lean/docs/221.md`](../../../lean/docs/221.md) | 15 | scope note — the formalization's Scope at [S5:9] and its comparator link at [S5:15] |
| S6 | [`lean/ComparatorChallenges/DilutedSpin.lean`](../../../lean/ComparatorChallenges/DilutedSpin.lean) | 154 | the comparator stub — `mezard_parisi` at [S6:148–150] with its `sorry` at [S6:150] |
| S7 | [`reasoning_traces/mezard-parisi-formula.tex`](../../../reasoning_traces/mezard-parisi-formula.tex) | 211 | the published reasoning trace (LaTeX source); the PDF is `mezard-parisi-formula.pdf` |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=221`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- Dmitry Panchenko and Michel Talagrand. _Bounds for diluted mean-fields spin glass models_. Probability Theory and Related Fields **130**(3) (2004), 319–336. .
- Dmitry Panchenko. _Structure of finite-RSB asymptotic Gibbs measures in the diluted spin glass models_. Journal of Statistical Physics **162**(1) (2016), 1–42. .
- Jean-Christophe Mourrat and Dmitry Panchenko. _Extending the Parisi formula along a Hamilton–Jacobi equation_. Electronic Journal of Probability **25** (2020), paper no. 23, 1–17. .
- Jean Barbier and Dmitry Panchenko. _Strong replica symmetry in high-dimensional optimal Bayesian inference_. Communications in Mathematical Physics **393**(3) (2022), 1199–1239. .
- Jean-Christophe Mourrat. _The Parisi formula is a Hamilton–Jacobi equation in Wasserstein space_. Canadian Journal of Mathematics **74**(3) (2022), 607–629. .

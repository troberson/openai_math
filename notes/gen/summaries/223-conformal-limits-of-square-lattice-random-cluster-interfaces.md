[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 223](../index/probability-and-statistical-mechanics/223-conformal-limits-of-square-lattice-random-cluster-interfaces.md)

# 223 — Conformal limits of square-lattice random-cluster interfaces

[Index page](../index/probability-and-statistical-mechanics/223-conformal-limits-of-square-lattice-random-cluster-interfaces.md)

## Original CONTENTS.md summary

[S1:5292] (family entry):

> **223. Random-cluster interfaces: critical, disordered, thermal, and natural-time scaling.** Proves chordal SLE<sub>κ</sub> limits for critical square-lattice random-cluster interfaces for $`0<q\le4`$, with $`\kappa=4\pi/\arccos(-\sqrt q/2)`$: bounded Jordan domains are allowed for $`q \ge 1`$, and smooth Jordan domains for $`q < 1`$, under the stated marked-boundary approximations. For $`1\le q\le4`$, complete nested plane loops converge to CLE<sub>κ</sub>.

[S2:531] carries the `\resultentry`, so the release blurb and the overview agree.
The six manuscripts:

**FK interfaces and nested loops ($`1\le q<4`$)** [S3:44, S3:46]:

> 1

**Self-dual interfaces ($`q<1`$)** [S4:16, S4:18]:

> 2

**Quenched SLE universality (weakly disordered FK--Ising)** [S5:47, S5:49]:

> 3

**Thermal FK--Ising interfaces and massive SLE** [S6:46, S6:48]:

> 4

**Natural occupation measures** [S7:1–9]:

> 5

**Conformal limits ($`1\le q\le4`$)** [S8:44, S8:46]:

> 6

## Undergraduate summary

A **random-cluster model** is a way to describe phase transitions in
magnetic materials. The parameter $`q`$ controls what kind of transition:
$`q=1`$ is ordinary percolation, $`q=2`$ is the Ising model (magnetic spins
that are up or down), and $`q=4`$ is the Potts model with four colors.
A **Dobrushin interface** is the boundary between two regions with
different spin states. The **Schramm--Loewner evolution (SLE)** is a
random curve that describes the "universal" shape of such boundaries
at criticality. The parameter $`\kappa`$ tells you how wiggly the curve
is: $`\kappa=8/3`$ for percolation, $`\kappa=6`$ for Ising, up to
$`\kappa=16/3`$ for the $`q=4`$ transition. This family proves that
the lattice interfaces converge to SLE curves for the full range
$`0<q\le4`$ [S3:50–58, S4:22–30, S8:50–57, S2:531].

## Graduate summary

**Critical FK interfaces, $`1\le q<4`$**
[S3:50–58, S2:531]. The Dobrushin interface converges
to chordal $`\mathrm{SLE}_{\kappa(q)}`$ where
$`\kappa(q)=4\pi/\arccos(-\sqrt q/2)`$, in every
bounded Jordan domain under uniform marked boundary
approximation. Nested plane loop collections converge to
whole-plane $`\mathrm{CLE}_{\kappa(q)}`$ in a spherical matching
topology retaining multiplicities. At $`q=1`$ this recovers
Cardy's formula for square-lattice bond percolation.

**Self-dual interfaces, $`q<1`$**
[S4:22–30, S2:531]. The Dobrushin interface at the
self-dual parameter converges to chordal $`\mathrm{SLE}_\kappa`$
with $`\kappa\in(6,8)`$. The approximating domains are
simple closed nearest-neighbor lattice polygons with
distinct marked vertices. Convergence holds along the full
mesh sequence in the uniform metric on oriented curves
modulo increasing reparametrization.

**Quenched SLE, weakly disordered**
[S5:53–57, S2:531]. Critical FK--Ising interfaces
with sufficiently weak, symmetric, independent two-valued
bond disorder converge to chordal $`\mathrm{SLE}_{16/3}`$. The
disorder strength is fixed as the mesh tends to zero, and
convergence of the conditional curve laws holds in
probability over the environment.

**Thermal FK--Ising, massive SLE**
[S6:52–58, S2:531]. For every fixed nonzero mass of
either sign, thermal FK--Ising interfaces on uniformly
angle-bounded isoradial lattices converge to a lattice- and
domain-independent limit. Positive mass gives the unique
massive $`\mathrm{SLE}_{16/3}`$ law with locally finite-energy
drift from a massive boundary value problem; negative
mass follows by duality and reversal.

**Natural occupation measures**
[S7:2–9, S2:531]. The rescaled counting measure of
a critical square-lattice FK Dobrushin interface in the
unit square converges to the Minkowski-content measure of
its SLE limit, for every $`1\le q<4`$. A single
deterministic constant times the predicted power of the
mesh gives the normalization. Convergence is joint with
the ordered curve and includes the total mass.

**Conformal limits, $`1\le q\le4`$**
[S8:50–57, S2:531]. The full-range version: critical
Dobrushin interfaces converge to chordal
$`\mathrm{SLE}_{\kappa(q)}`$ and nested loops to whole-plane
$`\mathrm{CLE}_{\kappa(q)}`$ under uniform marked Jordan boundary
approximation, retaining loop multiplicities and
traversals.

## History of the conjecture

The **Schramm--Loewner evolution** (Schramm, 1999) was
introduced as the unique conformally invariant family of
random planar curves with the Markov property. **Cardy's
formula** (1984) predicted the crossing probability for
2D percolation, and the proof that the conformal limit
of lattice percolation interfaces is $`\mathrm{SLE}_{8/3}`$
(Smirshev, 2001) confirmed it. The **random-cluster model**
(Fortuin--Kasteleyn, 1972) generalizes percolation
($`q=1`$), the Ising model ($`q=2`$), and the 4-state Potts
model ($`q=4`$). The **SLE universality** for the full
range $`0<q\le4`$ was a long-standing open problem, with
the $`q=1,2,3,4`$ cases established through the 2010s
using domain Markov properties and observable
techniques. This family extends the range to all
$`0<q\le4`$ [S3:50–58, S4:22–30, S8:50–57],
adds the **disorder** and **massive** extensions
[S5:53–57, S6:52–58], and provides the
**natural occupation measure** result [S7:2–9].

**Prior (my training data, not this repo).** The SLE
framework, Cardy's formula, the random-cluster model,
and the $`q=1,2,3,4`$ universality results are standard.
The full-range $`0<q\le4`$ extension, the weak-disorder
and massive-SLE results, and the natural occupation
measure convergence are the novel contributions. I
cannot confirm these independently from training alone.

## Consequences

- **Full-range SLE universality**
  [S3:50–58, S4:22–30, S8:50–57]:
  chordal $`\mathrm{SLE}_{\kappa(q)}`$ convergence for every
  $`0<q\le4`$, with $`\kappa(q)=4\pi/
  \arccos(-\sqrt q/2)`$, plus $`\mathrm{CLE}_{\kappa(q)}`$
  for nested loops.
- **Disorder robustness**
  [S5:53–57]: SLE_{16/3} survives weak two-valued
  bond disorder, in probability over the environment.
- **Massive SLE**
  [S6:52–58]: the off-critical (massive) limit
  is a lattice-independent massive SLE_{16/3} law.
- **Natural occupation measures**
  [S7:2–9]: the rescaled step count converges to
  the Minkowski-content measure, giving the scaling
  limit of the interface's total length.

## Section skeleton

Six manuscripts: [S3] (title [S3:44], date [S3:46])
— `main.tex` under `build/` with `sections/`,
`figures/`, `refs.bib`; [S4] (title [S4:16],
date [S4:18]) — `main.tex` under `build/` with
`appendices/`, `figures/`, `macros.tex`; [S5]
(title [S5:47], date [S5:49]) — `main.tex`
under `build/` with `sections/`; [S6] (title [S6:46],
date [S6:48]) — `main.tex` under `build/` with
`sections/`; [S7] (abstract [S7:1–9])
— `main.tex` under `build/` with `sections/`,
`figures/`, `sources/`; [S8] (title [S8:44],
date [S8:46]) — `main.tex` under `build/` with
`sections/`. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`,
`chal 0`, and `verification 0`. There is no
scope note under `lean/docs/`, no comparator
challenge under `lean/ComparatorChallenges/`, no
`main_results` entry in `formalization.yaml`,
and no verification bundle. The result is
**entirely unformalized**: the release shipped
no Lean code, no challenge stub, and no checking
workflow for this family. The proof rests solely
on the six manuscripts.

## Coverage

The ledger row `fam=223` [S9] records the tier and
the counts: `tier=T0`, `paps=6`, `paps_form=0`,
`chal=0`, `mainres=0`, `scope_note=0`,
`verification=0`, `trace=`. No formalization of
any kind. The shape flags are `bound`, and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5292] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 223 at [S2:531] |
| S3 | [`preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/build/main.tex`](../../../preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/build/main.tex) | 73 | manuscript 1 of 6 (FK interfaces and nested loops, $1\le q<4$); title [S3:44], date [S3:46], abstract [S3:49–59] |
| S4 | [`preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/build/main.tex`](../../../preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/build/main.tex) | 53 | manuscript 2 of 6 (self-dual interfaces, $q<1$); title [S4:16], date [S4:18], abstract [S4:21–31] |
| S5 | [`preprints/Quenched-SLE-Universality-for-Weakly-Disordered-FK-Ising-Interfaces-October-5-2026/build/main.tex`](../../../preprints/Quenched-SLE-Universality-for-Weakly-Disordered-FK-Ising-Interfaces-October-5-2026/build/main.tex) | 68 | manuscript 3 of 6 (quenched SLE, weak disorder); title [S5:47], date [S5:49], abstract [S5:52–57] |
| S6 | [`preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/build/main.tex`](../../../preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/build/main.tex) | 69 | manuscript 4 of 6 (thermal FK--Ising, massive SLE); title [S6:46], date [S6:48], abstract [S6:51–58] |
| S7 | [`preprints/Natural-Occupation-Measures-for-Critical-Square-Lattice-FK-Interfaces-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Natural-Occupation-Measures-for-Critical-Square-Lattice-FK-Interfaces-October-5-2026/build/sections/01-introduction.tex) | 251 | manuscript 5 of 6 (natural occupation measures); abstract [S7:1–9] |
| S8 | [`preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/main.tex`](../../../preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/main.tex) | 73 | manuscript 6 of 6 (conformal limits, $1\le q\le4$); title [S8:44], date [S8:46], abstract [S8:49–57] |
| S9 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=223`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

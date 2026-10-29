[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 226](../index/probability-and-statistical-mechanics/226-double-dimer-cle-4-conjecture-in-the-half-plane.md)

# 226 — The double-dimer $\mathrm{CLE}_4$ conjecture in the half-plane

[Index page](../index/probability-and-statistical-mechanics/226-double-dimer-cle-4-conjecture-in-the-half-plane.md)

## Original CONTENTS.md summary

[S1:5403] (family entry):

> **226. The double-dimer loop ensemble converges to CLE<sub>4</sub>.** Resolves the half-plane Temperleyan form of the double-dimer scaling-limit conjecture: the complete loop ensemble formed by two independent dimer coverings of the Temperleyan square lattice converges to nested CLE<sub>4</sub>. Convergence matches every macroscopic loop as an unparametrized curve, upgrading convergence of loop observables to convergence of the loops themselves.

[S2:537] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript [S3:36, S3:38]:

> 1

## Undergraduate summary

A **dimer covering** is a way to tile a grid with dominoes (1-by-2 rectangles).
The **double-dimer model** takes two independent random tilings and overlays
them: at every vertex, the edges from both tilings meet, and the symmetric
difference (edges that appear in only one tiling) forms a collection of
closed loops. The **concentrated loop ensemble (CLE)** is a conformally
invariant random collection of nested loops in the plane. **CLE<sub>4</sub>**
is the member of this family that appears in the Ising model. This paper
proves that the double-dimer loops converge to CLE<sub>4</sub> in the
half-plane [S3:42–46, S2:537].

## Graduate summary

**Main theorem** [S3:42–46, S2:537]. The complete
double-dimer loop ensemble for the Temperleyan square lattice
in the upper half-plane converges to nested CLE<sub>4</sub>.
The convergence holds along the full mesh limit and matches
**every** macroscopic loop as an unparametrized curve. This
resolves the half-plane Temperleyan form of the double-dimer
CLE<sub>4</sub> scaling-limit conjecture. The statement is
stronger than convergence of loop observables: it is
convergence of the loops themselves, as random curves in the
half-plane.

## History of the conjecture

The **double-dimer model** (Kenyon, 2001) was introduced as
a way to generate random loop ensembles from dimer coverings.
Kenyon showed that the loop ensemble from two independent
dimer coverings of the square lattice converges to CLE<sub>4</sub>
in the full plane. The **half-plane** extension is harder
because the boundary breaks the translation invariance and
the Temperleyan lattice geometry interacts with the
boundary in a nontrivial way. The "Temperleyan" qualifier
refers to the specific Temperley lattice geometry (a
subgraph of the square lattice with boundary conditions
that make the dimer model integrable). This paper
resolves the half-plane Temperleyan form
[S3:42–46, S2:537].

**Prior (my training data, not this repo).** The
double-dimer model, Kenyon's full-plane CLE<sub>4</sub>
result, and the CLE framework are standard. The half-plane
Temperleyan extension with full loop convergence (not just
observable convergence) is the novel contribution. I
cannot confirm this independently from training alone.

## Consequences

- **The half-plane double-dimer CLE<sub>4</sub>
  conjecture is resolved**
  [S3:42–46, S2:537]: the complete loop ensemble
  converges to nested CLE<sub>4</sub>.
- **Curve-level convergence, not just observables.**
  Every macroscopic loop matches as an unparametrized
  curve [S3:42–46] — a stronger statement
  than the convergence of winding numbers,
  intersections, or other loop observables.

## Section skeleton

One manuscript [S3]: `main.tex` under `build/` with
`sections/`, `figures/`, `references.tex`. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`,
`chal 0`, and `verification 0`. There is no
scope note, no comparator challenge, no
`main_results` entry, and no verification bundle.
The result is **entirely unformalized**.

## Coverage

The ledger row `fam=226` [S4] records the tier and
the counts: `tier=T0`, `paps=1`, `paps_form=0`,
`chal=0`, `mainres=0`, `scope_note=0`,
`verification=0`, `trace=`. No formalization of
any kind. The shape flags are `resolution`, and
`resolves_named=1` — the blurb names the
double-dimer CLE<sub>4</sub> conjecture with a
resolve verb.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5403] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 226 at [S2:537] |
| S3 | [`preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/main.tex`](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/main.tex) | 55 | the manuscript; title [S3:36], date [S3:38], abstract [S3:41–47] |
| S4 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=226`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

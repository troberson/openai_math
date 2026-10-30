[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 233](../index/probability-and-statistical-mechanics/233-joint-critical-ashkin-teller-scaling-limit.md)

# 233 — The joint critical Ashkin–Teller scaling limit

[Index page](../index/probability-and-statistical-mechanics/233-joint-critical-ashkin-teller-scaling-limit.md)

## Original CONTENTS.md summary

[S1:5632] (family entry):

> **233. The joint critical Ashkin–Teller current limit.** Identifies the joint scaling limit of Ashkin–Teller heights and both complete current-cluster collections throughout the critical line, including the four-state Potts endpoint. In bounded Jordan domains with admissible lattice approximations and wired primal/free dual boundaries, the height converges to the predicted Gaussian free field, and the clusters to canonical recursive sets of that same field, retaining every nesting depth.

[S2:551] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**Joint Ashkin–Teller scaling limit** [S3:52, S3:54]:

> For each fixed point on the critical Ashkin–Teller line, including the
four-state Potts endpoint, we prove the conjectured joint scaling limit
of the height and both current-cluster collections in every bounded
Jordan domain, for every admissible polygonal approximation. The height
converges to a Gaussian free field with the predicted coupling constant,
and the clusters converge to canonical recursive two-valued local sets
of that same field. The joint limit includes all nesting depths and the
distinguished wired boundary cluster. [S3:57–66]

## Undergraduate summary

The **Ashkin–Teller model** is a two-dimensional statistical
mechanics model on a lattice, where each edge carries two Ising
spins that interact with each other and with their neighbors. The
**critical line** is the set of temperature and coupling values
where the model phase-transitions. The result identifies the
**joint scaling limit**: at any point on the critical line, the
height function (a derived integer-valued field) and both
current-cluster collections (nested random sets of edges)
converge, in a precisely specified sense, to a
**Gaussian free field** and its associated
**recursive local sets** [S3:57–66, S2:551].

## Graduate summary

**Joint critical Ashkin–Teller scaling limit**
[S3:57–66, S2:551]. For each fixed point on the critical
Ashkin–Teller line, including the four-state Potts
endpoint, the joint scaling limit of the height and both
current-cluster collections is identified in every bounded
Jordan domain, for every admissible polygonal approximation.
The height converges to a Gaussian free field with the
predicted coupling constant, and the clusters converge to
canonical recursive two-valued local sets of that same field.
The joint limit includes all nesting depths and the
distinguished wired boundary cluster.

## History of the conjecture

The **Ashkin–Teller model** generalizes the
Ising model by adding a four-spin interaction along each
edge. Its critical behavior on the critical line has been
studied for decades, but the joint scaling limit of the
height and both current-cluster collections had not been
identified. The result [S3:57–66] proves that,
throughout the critical line including the four-state
Potts endpoint, the height converges to a GFF and the
currents to canonical recursive local sets of that same
field. This is the full joint identification, with all
nesting depths and the wired boundary cluster retained.

**Prior (my training data, not this repo).** The Ashkin–Teller
model, its critical line, and the GFF are well-known. The
joint scaling limit identification for the height and both
current-cluster collections is the novel contribution. I
cannot confirm this independently from training alone.

## Consequences

- **The joint GFF and local-set limit**
  [S3:57–66]: the height converges to a GFF with the
  predicted coupling constant, and both current-cluster
  collections converge to canonical recursive two-valued
  local sets of that same field, at every point on the
  critical line including the four-state Potts endpoint.
- **All nesting depths retained**
  [S3:57–66]: the joint limit includes the full
  nested structure of the clusters, not just the outer
  boundary.

## Section skeleton

One manuscript: [S3:57–66] (title [S3:52], date [S3:54])
— `main.tex` under `build/` with `sections/`. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

The release does **not** formalise this family. There is
no scope note, no comparator stub, no `main_results` entry,
and no OAI tree. The ledger tier is T0. The reading is of
source text only.

## Coverage

The ledger row `fam=233` [S4] records the tier and the
counts: `tier=T0`, `paps=1`, `paps_form=0`, `chal=0`,
`mainres=0`, `scope_note=0`, `verification=0`, `trace=`.
No formalization. No verification bundle. No reasoning
trace. The shape flags are `bound`, and `resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5632] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 233 at [S2:551] |
| S3 | [`preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026/build/main.tex`](../../../preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026/build/main.tex) | 84 | manuscript 1 of 1; title [S3:52], date [S3:54], abstract [S3:57–66] |
| S4 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=233`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

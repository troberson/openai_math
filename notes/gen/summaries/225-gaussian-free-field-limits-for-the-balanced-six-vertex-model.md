[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 225](../index/probability-and-statistical-mechanics/225-gaussian-free-field-limits-for-the-balanced-six-vertex-model.md)

# 225 — Gaussian free field limits for the balanced six-vertex model

[Index page](../index/probability-and-statistical-mechanics/225-gaussian-free-field-limits-for-the-balanced-six-vertex-model.md)

## Original CONTENTS.md summary

[S1:5387] (family entry):

> **225. Gaussian free field limits throughout the balanced six-vertex regime.** The balanced square-lattice six-vertex height field with $`a=b=1`$ and $`0<c\le2`$ converges to a Gaussian free field, including at the endpoint $`c=2`$. The plane state is defined by balanced-torus limits. For unit height increments and Green kernel $`-(2\pi)^{-1}\log|x-y|`$, the exact variance multiplier is $`1/\arcsin(c/2)`$.

[S2:535] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript [S3:3, S3:5]:

> 1

## Undergraduate summary

The **six-vertex model** is a statistical mechanics model of ice
crystal structure: each vertex of a square lattice has two arrows
pointing in and two pointing out, giving six allowed configurations.
The parameter $`c`$ controls the energy of the "free" vertices. The
**height function** assigns an integer to each face, increasing by
one across each arrow. The **Gaussian free field (GFF)** is the
continuum limit of many lattice height functions: a random field
whose values at nearby points are strongly correlated, with
correlations decaying logarithmically. This paper proves that the
six-vertex height function converges to the GFF for the full range
$`0<c\le2`$, with the exact variance multiplier $`1/\arcsin(c/2)`$
[S3:9–13, S2:535].

## Graduate summary

**Main theorem** [S3:9–13, S2:535]. The height function
of the square-lattice six-vertex model with weights
$`a=b=1`$ and $`0<c\le2`$, in the plane state obtained from
balanced tori, converges to a multiple of the Gaussian free
field. For unit height jumps and Green kernel
$`-(2\pi)^{-1}\log|x-y|`$, the squared variance
multiplier is $`1/\arcsin(c/2)`$. The endpoint $`c=2`$ is
included.

## History of the conjecture

The **six-vertex model** (Bazhanov, 1973; domarck, 1973) is
one of the exactly solvable models in 2D statistical
mechanics. The **height function** approach connects it to
the GFF through the logarithmic variance of the
height field. The **GFF universality** for the six-vertex
model was established in the free-fermion case
($`c=2`$, the critical point) by earlier work; the extension
to the full regime $`0<c\le2`$ with the exact variance
multiplier $`1/\arcsin(c/2)`$ is the contribution here
[S3:9–13, S2:535].

**Prior (my training data, not this repo).** The
six-vertex model, the height function, and the GFF
limit at the free-fermion point are standard. The
full-regime extension with the exact variance formula
is the novel contribution. I cannot confirm this
independently from training alone.

## Consequences

- **GFF universality for the full balanced regime**
  [S3:9–13]: the height function converges to the
  GFF for every $`0<c\le2`$, including the critical
  endpoint.
- **The exact variance multiplier**
  [S3:9–13]: $`1/\arcsin(c/2)`$, a closed-form
  function of the ice parameter.

## Section skeleton

One manuscript [S3]: `main.tex` under `build/` with
`sections/`, `figures/`, `preamble.tex`,
`references.bib`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`,
`chal 0`, and `verification 0`. There is no
scope note, no comparator challenge, no
`main_results` entry, and no verification bundle.
The result is **entirely unformalized**.

## Coverage

The ledger row `fam=225` [S4] records the tier and
the counts: `tier=T0`, `paps=1`, `paps_form=0`,
`chal=0`, `mainres=0`, `scope_note=0`,
`verification=0`, `trace=`. No formalization of
any kind. The shape flags are empty, and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5387] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 225 at [S2:535] |
| S3 | [`preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/build/main.tex`](../../../preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/build/main.tex) | 28 | the manuscript; title [S3:3], date [S3:5], abstract [S3:8–14] |
| S4 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=225`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

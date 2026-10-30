[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 239](../index/probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md)

# 239 — Sharp singularity rates for symmetric sign matrices

[Index page](../index/probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md)

## Original CONTENTS.md summary

[S1:5962] (family entry):

> **239. Sharp singularity rates for symmetric random sign matrices.** Determines the sharp exponential singularity rate of symmetric random sign matrices with independent entries on and above the diagonal. Uniform signs give $`\Pr(\det A_n=0)=(1/2+o(1))^n`$; for fixed bias $`p\in(0,1)\setminus\{1/2\}`$, the rate is $`(p^2+(1-p)^2+o(1))^n`$. In the biased case, agreeing rows attain this rate.

[S2:563] carries the `\resultentry`, so the release blurb and the overview agree.
The two manuscripts:

**Uniform symmetric signs** [S3:49–50, S3:52]:

> Let $`A_n`$ be a symmetric $`n\times n`$ matrix whose entries on and above
the diagonal are independent uniform signs. We prove
$$\Pr(\det A_n=0)=\left(\frac12+o(1)\right)^n.$$ [S3:57–63]

**Biased symmetric signs** [S4:43, S4:45]:

> Let $`A_n`$ be a symmetric random matrix whose entries on and above the
diagonal are independent signs, equal to $`1`$ with fixed probability
$`p\in(0,1)\setminus\{1/2\}`$. We prove that
$`\mathbb P(\det A_n=0)=(p^2+(1-p)^2+o(1))^n`$.
The rate is attained by the event that two rows agree. [S4:48–54]

## Undergraduate summary

A **random sign matrix** is a square matrix filled with $`+1`$ and
$`-1`$ entries. **Singular** means the determinant is zero, which
geometrically means the rows (or columns) have some linear
dependency. The question: what is the probability that a
random symmetric sign matrix is singular, as the size $`n`$ grows?
The answer: it decays exponentially, at rate
$`(1/2)^n`$ for uniform signs and
$`(p^2+(1-p)^2)^n`$ for biased signs
[S3:57–63, S4:48–54, S2:563].

## Graduate summary

**Uniform symmetric signs**
[S3:57–63, S2:563]. Let $`A_n`$ be a symmetric
$`n	imes n`$ matrix whose entries on and
above the diagonal
are independent
uniform signs.
The singularity probability satisfies
$`\Pr(\det A_n=0)
= (1/2+o(1))^n`$.
The rate $`1/2`$ is sharp: no faster exponential decay occurs.

**Biased symmetric signs**
[S4:48–54, S2:563].
For $`A_n`$ with entries on and above the diagonal independent signs,
equal to $`+1`$ with fixed probability $`p\in(0,1)\setminus\{1/2\}`$, the
singularity probability satisfies
$`\Pr(\det A_n=0)
= (p^2+(1-p)^2+o(1))^n`$.
The rate is attained by the event that two rows agree.

## History of the conjecture

The **singularity probability** of random matrices is a classical
problem in combinatorial probability. For **asymmetric** random sign
matrices, the rate is known to be $`(1/2+o(1))^n`$ by the work of Tao, Vu,
and others. The **symmetric** case — where $`A_{ij}=A_{ji}`$ — is harder
because the off-diagonal entries appear twice, creating correlations
that the asymmetric proofs do not handle. The uniform result [S3:57–63]
and the biased result [S4:48–54] resolve the sharp rate for both the
unbiased and biased symmetric cases. In the biased case, the mechanism
for attaining the rate is identified: two rows agree.

**Prior (my training data, not this repo).** The singularity probability
for asymmetric random matrices, the Komlós– Erdös framework, and the
Tao–Vu improvements are standard. The sharp symmetric rate and the
biased extension are the novel contributions. I cannot confirm these
independently from training alone.

## Consequences

- **The uniform symmetric rate**
  [S3:57–63]:
  $`\Pr(\det A_n=0)
  = (1/2+o(1))^n`$
for uniform symmetric random sign matrices.
- **The biased symmetric rate**
  [S4:48–54]:
  $`\Pr(\det A_n=0)
  = (p^2+(1-p)^2+o(1))^n`$
for biased symmetric random sign matrices, attained by agreeing rows.

## Section skeleton

Two manuscripts. [S3:57–63] (title [S3:49–50], date [S3:52]) — `main.tex`
under `build/` with `sections/`. [S4:48–54] (title [S4:43], date [S4:45]) —
`main.tex` under `build/` with `sections/`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

The release does **not** formalise this family. There is no scope note,
no comparator stub, no `main_results` entry, and no OAI tree. The ledger
tier is T0. The reading is of source text only.

## Coverage

The ledger row `fam=239` [S5] records the tier and the counts:
`tier=T0`, `paps=2`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `verification=0`, `trace=`. No formalization. No
verification bundle. No reasoning trace. The shape flags are
`bound|partial|uniform`, and `resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5962] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 239 at [S2:563] |
| S3 | [`preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/main.tex`](../../../preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/main.tex) | 81 | manuscript 1 of 2 (uniform symmetric signs); title [S3:49–50], date [S3:52], abstract [S3:57–63] |
| S4 | [`preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/build/main.tex`](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/build/main.tex) | 63 | manuscript 2 of 2 (biased symmetric signs); title [S4:43], date [S4:45], abstract [S4:48–54] |
| S5 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=239`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

# 332 — Metric Markov cotype two for $\ell_1$ (Functional analysis, 1 manuscript, tier T0)

## Original CONTENTS.md summary

The release's blurb [S1:8104]:

> Proves that real ℓ1 has metric Markov cotype two, answering Mendel and
> Naor's question. Consequently, every Lipschitz map from an arbitrary
> subset of a real Hilbert space into ℓ1 extends to the whole space with a
> universal multiplicative loss in its Lipschitz constant, resolving Ball's
> extension problem for this target.

The manuscript's own abstract [S5:42–46] states the same result in one
sentence: "We prove that the real Banach space" ℓ1 "has metric Markov
cotype two, answering a question of Mendel and Naor. As a consequence,
every Lipschitz" map "from an arbitrary subset of a real Hilbert space
into" ℓ1 "extends to the whole Hilbert space with a universal
multiplicative loss in its Lipschitz constant, resolving Ball's extension
problem for this target." The manuscript names the target of the extension
as the whole Hilbert space. The release's blurb and the overview's
paraphrase [S2:760] both say the extension reaches "the whole space",
dropping the word "Hilbert" from the target the manuscript names.

## Undergraduate summary

Take a finite set of points in a metric space, and a Markov chain on that
set whose transition matrix is reversible with respect to a stationary
probability vector. Metric Markov cotype two asks whether you can move each
point to a new point so that the one-step movement the chain expects under
the new positions is small, while the total cost of moving the points is
paid by the original pairwise distances averaged over a longer time window.
The definition is due to Mendel and Naor, and the manuscript names the
constant it asks for: "The infimum of all such constants is denoted" by a
symbol the manuscript reserves for it. [S5:82]

The space in question is the real space of absolutely summable sequences,
with the sum of absolute values as its norm. The manuscript's main theorem
gives an explicit finite bound on the cotype constant for this space, and
the manuscript says what it is not: "No optimization of this numerical
constant is intended." [S5:97–98]

The point that makes the question hard is that the definition asks for
freedom, not for a linear average. Ball's original Markov cotype condition
for Banach spaces prescribes linear averages, and the space fails that
stronger condition. "The modified values are not prescribed linear averages.
This freedom is essential for the result proved here." [S5:56–57]

The consequence is an extension theorem. A Lipschitz map defined on an
arbitrary subset of a Hilbert space, with values in this space, extends to
the whole Hilbert space with a loss in its Lipschitz constant that is a
universal multiplicative factor — it does not depend on the subset, the
dimension, or the map. This is Ball's extension problem for this target,
and the manuscript resolves it.

## Graduate summary

The definition. A stochastic matrix is reversible with respect to a
probability vector when the detailed-balance identity holds for every pair
of indices; reversibility implies stationarity, and the manuscript notes
that "Zero coordinates of" the stationary vector "are allowed." [S5:69] The
cotype inequality compares two sums on the left — the movement cost and the
one-step variation weighted by a time parameter — against the Cesàro average
of the original pairwise distances over that time window.

The theorem. The manuscript proves an explicit finite bound for the real
space, and states what the bound is independent of: the number of points,
the number of coordinates, and the time parameter. [S5:95–98]

The mechanism. The proof is constructive, in three parts. First, a cut
representation: finitely many points in the space are replaced by binary
vectors in a weighted Hilbert space, where the squared Hilbert distance
between two binary vectors is exactly the original distance, and an affine
map back to the space is contractive for the weighted ℓ1 norm on the cut
coordinates. Second, a martingale estimate for a cubic smoothing function
whose derivative vanishes at the binary endpoints. Third, a comparison valid
in any metric space that converts the terminal geometric endpoint cost into
the Cesàro average the definition asks for.

The martingale is built by stopping a walk after an independent geometric
number of steps and attaching the expected binary vector to the current
index while the walk is alive, and the binary vector itself when it stops.
"These values form a martingale." [S5:171] Because the smoothing cubic's
derivative vanishes at the binary values, a fourth-power Hilbert potential
controls the total squared weighted ℓ1 variation after the smoothing is
applied. [S5:172–173] Centering at the starting point makes the terminal
potential the stopping cost; the stopping jump pays for the approximation,
and the expected number of preceding jumps pays for the one-step variation.
Contractivity of the reconstruction map transfers the bounds back to the
target space.

The interpretation. After the proof, the manuscript identifies the
constructed points as "the expected coordinatewise median of three
independent geometric-walk endpoints started at" the starting index.
[S5:186–188] The median is taken coordinate by coordinate, which is what
keeps the result inside the target space.

The scope of the method. The cut representation and the smoothing estimate
are stated for the real space; the comparison lemma is metric-space-valued.
The remark after the martingale section says the reversibility is used only
through the stationarity of the stationary law, so the argument extends to
any stationary Markov chain, not only to reversible ones. [S5:399–401]

## History and prior work

Ball introduced Markov type and cotype in his study of Lipschitz extension,
and his Banach-space cotype condition prescribes linear averages; the space
fails that stronger condition. "Ball also proposed a metric definition."
[S5:104] Mendel and Naor developed the Cesàro formulation the manuscript
uses, proved its equivalence to Ball's metric definition, and asked
explicitly whether the cotype constant of this space is finite. The
manuscript names the question it answers, in the sentence that closes the
history section. [S5:106–109]

For exponents between one and two, the uniformly convex theory gives bounds
that deteriorate as the exponent decreases to one, so they do not settle the
endpoint. There is a second distinction the manuscript makes: using a
construction of Kalton, Mendel and Naor found a closed linear subspace of
the space that fails metric Markov cotype at every finite exponent. That
does not contradict the main theorem, "because the points" the definition
produces "need not belong to a given subspace containing the original data.
Our construction uses this freedom." [S5:121–124]

The nonlinear cut smoothing with the same cubic also appears in the work of
Cheng, Wang, and Xiang on sharp metric cotype; the manuscript notes that
"metric cotype and metric Markov cotype are different invariants."
[S5:147–148] The cut representation is the geometry-of-cuts book of Deza
and Laurent. The bibliography carries five entries: Ball's 1992 paper,
Mendel and Naor's 2013 paper, the Deza–Laurent book, Naor and Young's
foliated corona decomposition paper, and the Cheng–Wang–Xiang 2026
preprint. [S6:1–50]

Prior (my training data, not the manuscript's record): Mendel and Naor's
2013 paper defined the invariant and asked whether the cotype constant of
the real ℓ1 is finite; the uniformly convex bounds for ℓp with p > 1 were
known, and the endpoint p = 1 was the open case. The Kalton subspace example
was the known obstruction to any subspace-stable version of the statement.
I would have recorded the question as open, with the extension consequence
for Hilbert-to-ℓ1 maps following formally once the question was answered.
The manuscript's own citations are the record; this paragraph is my prior on
the conjecture's standing, and the manuscript does not state it.

## Consequences and open directions

The extension consequence is the headline. Because the cotype constant is
finite, a Lipschitz map from any subset of a real Hilbert space into the
space extends to the whole Hilbert space with a universal multiplicative
loss. The manuscript states the loss explicitly, as a product of the
constant from the comparison lemma, the cotype constant, and the square
root of the bound on the cotype constant. [S5:411–414]

The method separates three things that are usually combined: a binary
representation of the metric data, a nonlinear smoothing of the binary
coordinates, and a metric comparison that rewrites the stopping cost as a
Cesàro average. The smoothing is the piece that is specific to this space,
because it uses the coordinate structure of the target.

Open directions the manuscript leaves: the numerical constant is not
optimized, so the bound is not claimed to be sharp; the cut representation
and the smoothing estimate are stated for the real space, so the complex
space is not treated; the subspace example shows that no subspace-stable
version of the statement can hold, so the freedom to place the new points
outside the span of the data is not a technical convenience but a necessity;
and the remark that reversibility is used only through stationarity widens
the class of chains the argument covers, which is a strengthening the
manuscript states rather than a limitation.

## What is formalized

Nothing. The ledger records tier T0 for this family, with no scope note, no
comparator challenge, no `main_results` entry, no reasoning trace, and no
verification bundle. The manuscript's LaTeX is the only source, and the
release's `formalized` flag for this manuscript is 0. The repo readme's
reasoning-summary table, "We are also releasing abridged summaries of the
model's reasoning, covering the following results:" [S3:24], lists ten
families and 332 is not among them. The claim is a nonlinear inequality for
a Markov chain on a Banach space; nothing in the Lean library reaches it,
and no certificate ships with it.

## Sources

| ID | File | Lines | What it carries |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | The release's blurb for family 332 at line 8104. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 760. |
| S3 | [`README.md`](../../../README.md) | 51 | The repo readme, which attributes no reasoning trace to this family. |
| S4 | [`preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/README.md`](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/README.md) | 18 | Citation-only manuscript readme: the result, the method, the scope, no provenance. |
| S5 | [`preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/main.tex`](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/main.tex) | 648 | The abstract, the definition, the theorem, the mechanism, the three sections, the remark, and the two corollaries. |
| S6 | [`preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/references.bib`](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/references.bib) | 50 | The bibliography: Ball, Mendel–Naor, Deza–Laurent, Naor–Young, Cheng–Wang–Xiang. |

The manuscript ships [S4:1–16] as a citation-only record: the result, the
method, the scope, and the bibliography, with no provenance, no run command,
and no verification bundle. The manuscript directory is
`preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/`, its PDF is
[S1:8104](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf),
and its main file is
[S5:1](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/build/main.tex).

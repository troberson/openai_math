[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 217](../index/probability-and-statistical-mechanics/217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md)

# 217 — The low-temperature Sherrington–Kirkpatrick fluctuation law

[Index page](../index/probability-and-statistical-mechanics/217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md)

## Original CONTENTS.md summary

The release's blurb [S1:5084] and the catalog abstract [S2:519]
state the family's claim: for every fixed inverse temperature
$`\beta > 1`$, the zero-field Gaussian Sherrington–Kirkpatrick
log partition function has variance asymptotic to
$`c_\beta n^{1/3}`$ with $`c_\beta > 0`$, confirming the
predicted $`n^{1/6}`$ standard-deviation scale. Exact
centering and standardization give full-sequence
convergence to a uniquely characterized nondegenerate
law. The family ships two manuscripts [S1:5084]:

- *The low-temperature
  Sherrington–Kirkpatrick free-energy limiting
  law* [S3:42, S3:44]
- *The low-temperature
  Sherrington–Kirkpatrick fluctuation scale*
  [S4:36, S4:38]

The free-energy limiting-law abstract


> For every fixed inverse temperature $`\beta>1`$, we prove that the zero-field Gaussian Ising Sherrington–Kirkpatrick free energy, centered by its expectation and divided by its standard deviation, converges in distribution to a nondegenerate law as the system size tends to infinity through all integers. We also prove that its variance divided by $`n^{1/3}`$ converges to a finite positive constant. [S3:47–49]

The fluctuation-scale abstract 

> For the zero-field Gaussian Sherrington–Kirkpatrick model at every fixed inverse temperature $`\beta>1`$, we prove that the standard deviation of the log partition function is $`n^{1/6+o(1)}`$. The same exponent describes its typical centered absolute fluctuations, establishing the predicted one-sixth exponent in this regime. [S4:41–43]

## Undergraduate summary

The **Sherrington–Kirkpatrick (SK) model** is a
mathematical model of a **spin glass** — a
disordered magnet where each pair of spins interacts
with a random strength. On $`n`$ sites, each spin is
$`+1`$ or $`-1`$, and the energy of a configuration is
$`H(\sigma) = \sum_{i<j} g_{ij} \sigma_i \sigma_j`$
where the $`g_{ij}`$ are i.i.d. Gaussian random numbers.
The **free energy** (log partition function)
$`F_n = \log \sum_{\sigma} e^{-\beta H(\sigma)}`$
encodes the thermodynamics. The big question: what
does $`F_n`$ look like when centered and scaled? In
the **low-temperature** regime ($`\beta > 1`$), the
fluctuations are of order $`n^{1/6}`$, not the
Gaussian $`n^{1/2}`$ — a hallmark of the spin-glass
phase. The family proves the **exact scaling** and the
**limiting law**: the variance is
$`c_\beta n^{1/3}(1+o(1))`$ and the standardized
free energy converges to a specific nondegenerate
random variable [S3:47–49, S4:41–43,
S2:519].

## Graduate summary

**The fluctuation scale** [S4:41–43, S2:519].
For the zero-field Gaussian SK model at every fixed
inverse temperature $`\beta > 1`$, the standard
deviation of the log partition function is
$`n^{1/6+o(1)}`$. The same exponent describes the
typical centered absolute fluctuations,
establishing the predicted one-sixth exponent.

**The limiting law** [S3:47–49, S2:519]. For
every fixed $`\beta > 1`$, the zero-field Gaussian
Ising SK free energy, centered by its expectation
and divided by its standard deviation, converges in
distribution to a nondegenerate law as $`n \to
\infty`$ through all integers. The variance divided
by $`n^{1/3}`$ converges to a finite positive
constant.

**The scope of the formalization.** The family is
at tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no
comparator challenge, no `main_results` entry, and
no verification bundle. The result is entirely
unformalized.

## History of the conjecture

**The SK model** was introduced by Sherrington and
Kirkpatrick (1975) as the prototype of mean-field
spin glass. The **free energy** per site exists in
thermodynamic limit by the Guerra ``interpolation''
method (Talagrand 2006, resolving a conjecture of
Sherrington and Kirkpatrick). The **fluctuation
scale** question asks: after centering, what is
the typical size of $`F_n - \mathbb{E}F_n`$? In the
high-temperature regime ($`\beta < 1`$), the
fluctuations are Gaussian of order $`n^{1/2}`$. In
the **low-temperature** regime ($`\beta > 1`$),
Bryson--Seigal (2007) and later work predicted the
$`n^{1/6}`$ scale from the replica-symmetric theory.
The two manuscripts establish this prediction
rigorously: the first determines the fluctuation
scale, the second determines the limiting law
[S3:47–49, S4:41–43, S2:519].

**Prior (my training data, not this repo).** I
know the SK model, the free-energy existence, the
replica-symmetric picture, and the predicted
$`n^{1/6}`$ low-temperature scale. The **rigorous
proof of the $`n^{1/6}`$ scale** and the
**convergence to a uniquely characterized
nondegenerate law** are results I cannot
independently verify from training alone.

## Consequences

**The low-temperature SK fluctuation scale is
$`n^{1/6}`$**: the standard deviation of the log
partition function is $`n^{1/6+o(1)}`$ for every
$`\beta > 1`$ [S4:41–43, S2:519].

**The SK free energy has a non-Gaussian limiting
law** in the low-temperature regime: after
centering and scaling by $`n^{1/6}`$, the free
energy converges to a nondegenerate distribution
[S3:47–49, S2:519].

**The variance constant is positive**:
$`\mathrm{Var}(F_n) / n^{1/3} \to c_\beta > 0`$
for every $`\beta > 1`$ [S3:47–49, S2:519].

## Section skeleton

Two manuscripts: [S3:47–49] (title [S3:42], date
[S3:44]) — `main.tex` under `build/` with
sections under `build/sections/` and a `figures/`
directory; [S4:41–43] (title [S4:36], date [S4:38])
— `paper.tex` under `build/` with sections
under `build/sections/` and a `figures/`
directory. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`,
`chal 0`, and `verification 0`. There is no
scope note under `lean/docs/`, no comparator
challenge under `lean/ComparatorChallenges/`, no
`main_results` entry in `formalization.yaml`,
and no verification bundle under the manuscript
directories. The result is **entirely
unformalized**: the release shipped no Lean
code, no challenge stub, and no checking
workflow for this family. The proof rests
solely on the two manuscripts
[S3:47–49, S4:41–43].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 217 at [S1:5084] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{217} at [S2:519] |
| S3 | [`preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/main.tex`](../../../preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/main.tex) | 72 | manuscript 1 of 2 (free-energy limiting law); title [S3:42], date [S3:44], abstract [S3:47–49] |
| S4 | [`preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/paper.tex`](../../../preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/paper.tex) | 58 | manuscript 2 of 2 (fluctuation scale); title [S4:36], date [S4:38], abstract [S4:41–43] |

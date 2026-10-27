[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 270](../index/mathematical-physics/270-threshold-and-positive-energy-bound-states-of-the-bfss-model.md)

# 270 — Threshold and positive-energy bound states of the BFSS model

[Index page](../index/mathematical-physics/270-threshold-and-positive-energy-bound-states-of-the-bfss-model.md)

## Original CONTENTS.md summary

The release's blurb [S1:6797] and the catalog abstract [S2:629] state
the family's claim: the undeformed relative $\mathrm{SU}(N)$ BFSS model
has exactly one normalizable zero-energy state for every finite
$N\ge2$, resolving the threshold-bound-state conjecture; and for
$\mathrm{SU}(2)$ a companion proves infinitely many normalizable
positive-energy eigenstates with unbounded energies, contradicting the
original BFSS paper's exclusion of additional bound states at
$N=2$. The threshold manuscript's abstract "For every finite \(N\ge2\), we prove that undeformed \(\mathrmSU(N)\) BFSS matrix
quantum mechanics has exactly one normalizable zero-energy state after
removing the center of mass. This establishes the threshold-bound-state
conjecture. [S3:66–71]" The
positive-eigenvalue manuscript's abstract "We prove that the relative $\mathrm{SU}(2)$ BFSS Hamiltonian has infinitely many
positive eigenvalues tending to infinity, with square-integrable
eigenvectors. The operator is defined by closing the gauge-invariant
supercharge form. This refutes, at $N=2$, the exclusion of normalizable
positive-energy states stated in the original BFSS paper. [S5:44–50]"

## Undergraduate summary

The BFSS model is a one-dimensional supersymmetric quantum mechanics
of $N\times N$ matrices, obtained by reducing ten-dimensional
supersymmetric Yang–Mills theory to a single time dimension. Its
quartic potential vanishes on commuting matrices, so classical
configurations can escape to infinity without paying potential
energy. The supersymmetric Hamiltonian is a square, so its spectrum
is bounded below by zero, and a zero-energy state is an unbroken
supersymmetry state. The threshold question asks how many zero-energy
states exist once the overall center of mass is removed. The
threshold manuscript answers: exactly one, for every $N\ge2$
[S4:23–81]:

> **theorem**
For every integer \(N\ge2\),
\[
\dim\mathrmker H_N=1.
\]
The kernel consists of \(\mathrmSpin(9)\)-invariant states and is even in the
fermion grading just specified. [S4:74–81]

That single state is the unique ground state of the relative model.
The positive-eigenvalue companion then asks what happens to the
positive spectrum: for $\mathrm{SU}(2)$ it exhibits an infinite
sequence of normalizable eigenvectors with energies tending to infinity
[S5:55–143]:

> **theorem**
There are an orthonormal sequence
$\Psi_j\in\mathrm{Dom}(H)$ and real numbers $E_j>0$ tending to infinity such that
\[
 H\Psi_j=E_j\Psi_j.
\]
In particular, $\sigma_{\mathrm p}(H)\cap(0,\infty)$ is infinite. [S5:135–143]

## Graduate summary

**The threshold proof's compactness mechanism.** The threshold
manuscript reduces $\dim\mathrm{ker} H_N = 1$ to a counting problem for the
massive spectrum. The analytic core is a compactness argument: after
local rescaling, any sequence with bounded energy concentrates on a
finite number of scales, and local profiles satisfy a linearized
equation. The massive count bounds how many profiles can pack into
each scale, and a capture argument shows no concentration scale is
missed, leaving only the $\mathrm{Spin}(9)$-invariant zero mode [S4:173–274].

**The positive-eigenvalue construction.** The $\mathrm{SU}(2)$
manuscript defines the Hamiltonian by closing the gauge-invariant
supercharge form on the $\mathrm{SU}(2)$-invariant part of
$L^2(\mathbb{R}^{27};\mathcal{F})$. It then selects $\mathrm{Spin}(9)$
sectors in which symmetry excludes the low transverse oscillator
levels, so the remaining oscillator energy confines those sectors and
produces an unbounded sequence of discrete positive eigenvalues with
square-integrable eigenvectors [S5:229–411].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

The BFSS model was introduced by Banks, Fischler, Shenker, and Susskind
as a nonperturbative definition of M-theory. The original paper argued
that the relative model has a single normalizable zero-energy state and
excluded additional normalizable positive-energy bound states, in
particular at $N=2$. The threshold manuscript proves that
zero-energy claim for all $N\ge2$ [S4:90–169]. The positive-eigenvalue
manuscript refutes, at $N=2$, the exclusion of positive-energy bound
states that the original paper stated, by constructing the normalizable
eigenvectors directly [S5:55–133].

## Consequences

**The threshold-bound-state conjecture is resolved.** The relative
$\mathrm{SU}(N)$ BFSS model has a unique normalizable ground state,
$\mathrm{Spin}(9)$-invariant and even in the fermion grading, for every
$N\ge2$ [S4:74–81].

**The original BFSS $N=2$ exclusion is refuted.** The relative
$\mathrm{SU}(2)$ Hamiltonian has infinitely many normalizable positive-energy
eigenvalues tending to infinity, so the positive point spectrum is
infinite. This is a direct contradiction of the bound-state exclusion
in the original paper at $N=2$ [S5:135–143].

## Section skeleton

**Threshold manuscript** [S3:66–71], 7 sections under
`build/manuscript/sections/`: 01-introduction [S4:74–81], 02-algebra,
03-massive-index, 04-fast-analysis, 05-lifts, 06-profiles,
07-counting. Plus one figure under `build/manuscript/figures/`. Its
root is `build/manuscript/main.tex`, with a `references.bib`
bibliography [S6].

**Positive-eigenvalue manuscript** [S5] is a single self-contained
`.tex` file under `build/` (title, abstract, introduction, and the
quadratic-form, confinement, and eigenvalue sections all inline), with
no separate bibliography or `sections/` tree.

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts — 9 `.tex` files in the threshold `build/manuscript/` and
1 (single-file) in the positive-eigenvalue `build/` — and no
non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 270 at line 6797. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 629. |
| S3 | [`preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/main.tex`](../../../preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/main.tex) | 86 | Threshold manuscript main file: title and abstract. |
| S4 | [`preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/sections/01-introduction.tex`](../../../preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/sections/01-introduction.tex) | 274 | Threshold manuscript introduction: the operator, the main theorem, the history, and the proof's compactness mechanism. |
| S5 | [`preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/build/positive-eigenvalues-relative-su2-bfss.tex`](../../../preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/build/positive-eigenvalues-relative-su2-bfss.tex) | 888 | Positive-eigenvalue (single-file) manuscript: title, abstract, the operator setup, the main theorem, and the quadratic-form analysis. |
| S6 | [`preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/references.bib`](../../../preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/build/manuscript/references.bib) | 290 | Threshold manuscript bibliography. |

## Bibliography

- Tom Banks, Willy Fischler, Stephen H. Shenker, and Leonard Susskind, _M theory as a matrix model: A conjecture_, Physical Review D **55** (1997), 5112–5128.  .
- Banks, T., Fischler, W., Shenker, S. H., Susskind, L., M theory as a matrix model: A conjecture (1997)
- Berenstein, David, Maldacena, Juan, Nastase, Horatiu, Strings in flat space and pp waves from $\mathcal{N}=4$ Super Yang Mills (2002)
- Boulton, Lyonell, {García del Moral}, María Pilar, Restuccia, Alvaro, Existence of a supersymmetric massless ground state of the $SU(N)$ matrix model globally on its valleys (2021)
- Chang, Chi-Ming, Witten index of BMN matrix quantum mechanics (2025)
- Ulf H. Danielsson, Gabriele Ferretti, and Bo Sundborg, _D-particle dynamics and bound states_, International Journal of Modern Physics A **11** (1996), 5463–5478.  .
- Dasgupta, Keshav, Sheikh-Jabbari, Mohammad M., Van Raamsdonk, Mark, Matrix Perturbation Theory for M-theory on a PP-Wave (2002)
- I. Ya. Aref'eva, A. S. Koshelev, and P. B. Medvedev, _On stable sector in supermembrane matrix model_, Nuclear Physics B **579** (2000), 411–436.  .
- Frank, Rupert L., Seiringer, Robert, Non-linear ground state representations and sharp Hardy inequalities (2008)
- Graf, Gian Michele, Hoppe, Jens, Asymptotic Ground State for 10 Dimensional Reduced Supersymmetric $SU(2)$ Yang–Mills Theory (1998)
- Green, Michael B., Gutperle, Michael, D-particle bound states and the D-instanton measure (1998)
- Halpern, M. B., Schwartz, C., Asymptotic Search for Ground States of $SU(2)$ Matrix Theory (1998)
- Hasler, David, Hoppe, Jens, Zero Energy States of Reduced Super Yang–Mills Theories in $d+1=4,6$ and 10 dimensions are necessarily $\mathrm{Spin}(d)$ invariant (2002)
- Hasler, David, Hoppe, Jens, Asymptotic Factorisation of the Ground-State for $SU(N)$-invariant Supersymmetric Matrix-Models (2002)
- Hitchin, Nigel, $L^2$-cohomology of hyperkähler quotients (2000)
- Fröhlich, Jürg, Graf, Gian Michele, Hasler, David, Hoppe, Jens, Yau, Shing-Tung, Asymptotic Form of Zero Energy Wave Functions in Supersymmetric Matrix Models (2000)
- Kac, Victor G., Smilga, Andrei V., Normalized Vacuum States in $N=4$ Supersymmetric Yang–Mills Quantum Mechanics with Any Gauge Group (2000)
- Kato, Tosio, Perturbation Theory for Linear Operators (1995)
- Konechny, Anatoly, On asymptotic Hamiltonian for $SU(N)$ matrix theory (1998)
- Lin, Henry W., TASI lectures on Matrix Theory from a modern viewpoint (2025)
- Lin, Henry W., TASI lectures on Matrix Theory from a modern viewpoint (2026)
- Lin, Ying-Hsuan, Yin, Xi, On the Ground State Wave Function of Matrix Theory (2015)
- Lundholm, Douglas, Zero-energy states in supersymmetric matrix models (2010)
- Martin Lüscher, _Some analytic results concerning the mass spectrum of Yang–Mills gauge theories on a torus_, Nuclear Physics B **219** (1983), 233–261.  .
- Moore, G., Nekrasov, N., Shatashvili, S., D-particle bound states and generalized instantons (2000)
- Porrati, Massimo, Rozenberg, Alexander, Bound States at Threshold in Supersymmetric Quantum Mechanics (1998)
- Sethi, Savdeep, Stern, Mark, D-brane bound states redux (1998)
- Sethi, Savdeep, Stern, Mark, Invariance theorems for supersymmetric Yang–Mills theories (2000)
- E. B. Davies and Barry Simon, _Spectral properties of Neumann Laplacian of horns_, Geometric and Functional Analysis **2** (1992), 105–117.  .
- Barry Simon, _Some quantum operators with discrete spectrum but classically continuous spectrum_, Annals of Physics **146** (1983), 209–220.  .
- Simon, Barry, Semiclassical analysis of low lying eigenvalues. I. Non-degenerate minima: asymptotic expansions (1983)
- A. V. Smilga, _Comments on thermodynamics of supersymmetric matrix models_, Nuclear Physics B **818** (2009), 101–114.  .
- Savdeep Sethi and Mark Stern, _Invariance theorems for supersymmetric Yang–Mills theories_, Advances in Theoretical and Mathematical Physics **4** (2000), 487–501.  .
- B. de Wit, M. Lüscher, and H. Nicolai, _The supermembrane is unstable_, Nuclear Physics B **320** (1989), 135–159.  .
- de Wit, Bernard, Lüscher, Martin, Nicolai, Hermann, The supermembrane is unstable (1989)
- de Wit, Bernard, Hoppe, Jens, Nicolai, Hermann, On the quantum mechanics of supermembranes (1988)
- Witten, Edward, Constraints on supersymmetry breaking (1982)
- Witten, Edward, Bound States of Strings and $p$-Branes (1996)
- Yi, Piljin, Witten index and threshold bound states of D-branes (1997)
- Elia Bisi and Nikos Zygouras, _Transition between characters of classical groups, decomposition of Gelfand–Tsetlin patterns and last passage percolation_, arXiv:1905.09756, version 5, 2022.  .

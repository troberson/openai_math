# Name: turing

15 families · subject name · 1 carried by a title or a declaration · 15 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 152 capitalized occurrences, 117 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 15 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | Hilbert's tenth problem over $\mathbb Q$ | — | — | — | — | yes | — |
| [103](../theoretical-computer-science/103-derandomization-of-logarithmic-space-l-rl-bpl.md) | Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$ | — | — | — | — | yes | — |
| [109](../theoretical-computer-science/109-integer-multiplication-below-n-n.md) | Integer multiplication below $n\log n$ | — | — | — | — | yes | — |
| [116](../theoretical-computer-science/116-uniform-identity-testing-for-noncommutative-formulas.md) | Uniform identity testing for noncommutative formulas | — | — | — | — | yes | — |
| [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | Superpolynomial lower bounds and quasipolynomial reconstruction from deletion traces | — | — | — | — | yes | — |
| [124](../theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md) | Polynomial-time scheduling on three identical machines | — | — | — | — | yes | — |
| [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | The complexity of Weisfeiler--Leman refinement | — | — | — | — | yes | — |
| [137](../theoretical-computer-science/137-one-tape-time-simulation-in-two-fifths-power-space.md) | One-tape time simulation in two-fifths-power space | — | — | — | — | yes | — |
| [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | Finite lattice representation: counterexamples and undecidability | — | — | — | — | yes | — |
| [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | Random-SAT thresholds, sharp variance and computability | — | — | — | — | yes | — |
| [241](../mathematical-logic/241-rigidity-of-the-turing-degrees.md) | Rigidity of the Turing degrees | yes | yes | — | yes | yes | — |
| [242](../mathematical-logic/242-single-fold-diophantine-representations.md) | Single-fold Diophantine representations | — | — | — | — | yes | — |
| [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | QMA-hardness of continuum Coulomb energy | — | — | — | — | yes | — |
| [279](../mathematical-physics/279-exact-quantum-factoring-over-a-fixed-finite-gate-set.md) | Exact quantum factoring over a fixed finite gate set | — | — | — | — | yes | — |
| [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | Universal computation in forced Navier--Stokes flows | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026`](../../../preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf) |
| [`A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026`](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/) | [124](../theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md) | prose | [paper.pdf](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) |
| [`Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026`](../../../preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) |
| [`Computing-the-Random-3-SAT-Threshold-September-27-2026`](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [article.pdf](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf) |
| [`Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026`](../../../preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/) | [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | prose | [Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf](../../../preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf) |
| [`Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026`](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/) | [103](../theoretical-computer-science/103-derandomization-of-logarithmic-space-l-rl-bpl.md) | prose | [paper.pdf](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf) |
| [`Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026`](../../../preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/) | [279](../mathematical-physics/279-exact-quantum-factoring-over-a-fixed-finite-gate-set.md) | prose | [main.pdf](../../../preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/main.pdf) |
| [`Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026`](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/) | [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | prose | [paper.pdf](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf) |
| [`Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026`](../../../preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf) |
| [`Geometric-Programs-for-Solenoidal-Forcing-September-27-2026`](../../../preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf) |
| [`Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/) | [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | prose | [main.pdf](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf) |
| [`Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/) | — | prose | — |
| [`Incompressible-Box-Transport-and-Finite-Computation-October-6-2026`](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf) |
| [`Incompressible-Box-Transport-and-Finite-Computation-September-27-2026`](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-September-27-2026/) | — | prose | — |
| [`Integer-multiplication-below-n-log-n-September-23-2026`](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/) | [109](../theoretical-computer-science/109-integer-multiplication-below-n-n.md) | prose | [paper.pdf](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf) |
| [`Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose | [paper.pdf](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) |
| [`Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026`](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/) | [116](../theoretical-computer-science/116-uniform-identity-testing-for-noncommutative-formulas.md) | prose | [Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf) |
| [`Prefix-Instructions-and-Incompressible-Flows-September-27-2026`](../../../preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf) |
| [`Rigidity-of-the-Turing-degrees-September-24-2026`](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/) | [241](../mathematical-logic/241-rigidity-of-the-turing-degrees.md) | prose + title | [paper.pdf](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf) |
| [`Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026`](../../../preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf) |
| [`Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/) | [137](../theoretical-computer-science/137-one-tape-time-simulation-in-two-fifths-power-space.md) | prose | [article.pdf](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf) |
| [`Single-fold-Diophantine-representations-September-24-2026`](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/) | [242](../mathematical-logic/242-single-fold-diophantine-representations.md) | prose | [paper.pdf](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf) |
| [`Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose | [paper.pdf](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) |
| [`Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026`](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/) | [116](../theoretical-computer-science/116-uniform-identity-testing-for-noncommutative-formulas.md) | prose | [uniform-matrix-hitting-points-positive-characteristic.pdf](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf) |
| [`Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026`](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/) | [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | prose | [uniform-trace-reconstruction.pdf](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf) |
| [`Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026`](../../../preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) |
| [`Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026`](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose | [paper.pdf](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf) |
| [`Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026`](../../../preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [DegreeRigidity](../../../lean/ComparatorChallenges/DegreeRigidity.json) | `OAI.TuringRigidity.ManuscriptMain.rigidity` | [Main.lean](../../../lean/OAI/Computability/DegreeRigidity/Main.lean) | [241](../mathematical-logic/241-rigidity-of-the-turing-degrees.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `turing`: accents folded, dash variants unified, possessives stripped, case lowered. `Turing` · `Turing's`


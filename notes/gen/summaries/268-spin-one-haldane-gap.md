[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 268](../index/mathematical-physics/268-spin-one-haldane-gap.md)

# 268 — The spin-one Haldane gap

[Index page](../index/mathematical-physics/268-spin-one-haldane-gap.md)

## Original CONTENTS.md summary

The release's blurb [S1:6747] and the catalog abstract [S2:625] state
the family's claim: the spin-one Haldane gap conjecture for the pure
antiferromagnetic Heisenberg chain on even periodic rings — the
spectral gap stays uniformly positive as the chain grows — together
with a companion gap for odd open chains with endpoint field
$h=3/5$ and boundary-selected infinite-volume states carrying
topological index $-1$. The periodic manuscript's abstract
 "We prove a uniform positive spectral gap for the pure antiferromagnetic
spin-one Heisenberg chain on even periodic rings, establishing the
positive even-periodic formulation of the spin-one Haldane conjecture. [S3:90–94]" The boundary-field manuscript's abstract
 "We prove a uniform spectral gap for odd open spin-one antiferromagnetic
Heisenberg chains with the same fixed magnetic field at both endpoints.
The field $h=3/5$ gives a gap greater than $\log(10)/392$ on every chain
of $2L+1$ sites with $L\ge960$. Tasaki's index theorem then gives index $-1$
for every subsequential local limit of these boundary-selected ground states. [S5:41–47]"

## Undergraduate summary

The spin-one Heisenberg chain is a model of interacting quantum spins
arranged on a ring. Each site carries a spin-1 particle (a vector in
$\mathbb{C}^3$), and neighbouring spins couple through their dot
product. The Haldane conjecture, proposed by Haldane in 1983, says
that the ground state of the antiferromagnetic chain on a ring has a
finite energy gap to the first excited state, uniformly as the number
of sites grows. This gap is the thermodynamic signature of a gapped
phase of matter. The periodic manuscript proves the conjecture for
even-periodic rings 

> **Theorem 1.1**
For the Hamiltonians  , the ground state is unique for
every even $L\ge60$, and
$$\gamma_L&>\frac4{105}\log\frac{80}{79}
     &&\text{for every even }L\ge60,\label{eq:gap60}\\
 \gamma_L&>\frac{\log20}{784}
     &&\text{for every even }L\ge2304.\label{eq:gap2304}$$
Consequently
\[
 \Delta_1\ge\frac{\log20}784>0.
\]
The spectral conclusions also hold for any simultaneously similar
spin-one realization satisfying the same commutator and Casimir
normalizations. [S4:37–53]

The boundary-field companion proves a matched statement for odd open
chains: with a fixed magnetic field $h = 3/5$ at both endpoints, the
gap is bounded below by a positive constant for all chains of
$2L+1$ sites with $L \ge 960$ 

> **theorem**
For the Hamiltonian  , with the spin normalization above,
\[
 E_1(L,3/5)-E_0(L,3/5)>\frac{\log 10}392
 \qquadfor every integer L\ge960.
\] [S5:77–83]

## Graduate summary

**The transfer-operator structure.** Both proofs reduce the spectral
gap to estimates on a transfer operator acting on a Hilbert space of
boundary data. The periodic manuscript works with a compact
self-adjoint spatial operator $X_b$ at inverse temperature $b$: the
partition function is $\mathrm{Tr}(X_b^{2L})$, and the gap follows from
dominance of the top eigenvalue at high even moments [S4:144–190].
The boundary-field manuscript works with a boundary pairing
$\langle v_b, X_b^{2L} v_b \rangle$ for the opposite-field chain, then
rotates the boundary vector to obtain the same-field Hamiltonian.
The boundary-overlap problem — the vector $v_b$ changes with
temperature — is solved by contracting residual boundary-weighted
moments while tracking the Gibbs purity of the opposite-field chain
[S5:88–135].

**The Tasaki index connection.** The boundary-field gap feeds into
Tasaki's index theorem: the uniform positivity of the gap for
boundary-selected ground states at $h = 3/5$ implies that every
subsequential local limit carries topological index $-1$. This
connects the finite-volume gap to a bulk topological invariant of
the infinite-volume state, completing the Haldane mechanism for
the open-chain case [S5:41–47].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

Haldane's 1983 conjecture was motivated by the observation that
integer-spin antiferromagnetic chains should be gapped, in contrast
to half-integer-spin chains. Affleck, Kennedy, Lieb, and Ross (AKLR)
proved the gap for a subclass of the spin-1 chain with a
complementary interaction. The present work addresses the pure
bilinear Heisenberg model, which was the remaining case [S4:68–140].
The two-manuscript structure follows Tasaki's program: the periodic
gap is the thermodynamic statement, and the boundary-field gap
supplies the topological index via his index theorem [S5:49–75].

## Consequences

**The even-periodic Haldane gap is proved.** The spectral gap
$\Delta_1$ for the pure antiferromagnetic spin-one Heisenberg chain
on even periodic rings is uniformly positive, with the quantitative
bound $\Delta_1 \ge \log 20/784$ for all even chains of length at
least 2304. The ground state is unique for every even $L \ge 60$
[S4:37–53].

**The boundary-field gap closes the open-chain case.** The
endpoint-field gap at $h = 3/5$ is uniformly positive for all odd
open chains with $L \ge 960$, and the boundary-selected
infinite-volume states carry topological index $-1$. Together with
the periodic result, this gives the full Haldane mechanism for
both even and odd chain topologies [S5:77–83].

## Section skeleton

**Periodic manuscript** [S3:90–94], 6 sections under `build/`:
introduction [S4:37–53], model, transfer, bootstrap, initialization,
assembly. Plus three appendices (thermal120, thermal72, trials).
Its root is `build/main.tex`, with a `references.bib` bibliography
[S6].

**Boundary-field manuscript** [S5], 8 sections under
`build/sections/`: history, transfer, periodic, boundary,
initialization, conclusion, topology, plus two appendices (thermal,
trials). Its introduction, Hamiltonian setup, main theorem, and
proof strategy are all inline in the root `build/main.tex`; its
bibliography is `references.bib` [S7].

Both manuscripts ship `verification/` bundles (the ledger reads
`verification 2`).

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 2`, `trace` empty. The family ships two LaTeX
manuscripts — 10 `.tex` files in the periodic `build/` and 10 in the
boundary-field `build/` — plus two finite-arithmetic certificate
bundles, and no other non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 268 at line 6747. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 625. |
| S3 | [`preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/main.tex`](../../../preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/main.tex) | 114 | Periodic manuscript main file: title and abstract. |
| S4 | [`preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/introduction.tex`](../../../preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/introduction.tex) | 190 | Periodic manuscript introduction: main theorem, historical context, and the proof structure. |
| S5 | [`preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/build/main.tex`](../../../preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/build/main.tex) | 135 | Boundary-field manuscript main file: title, abstract, Hamiltonian setup, main theorem, and proof strategy (all inline). |
| S6 | [`preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/references.bib`](../../../preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/references.bib) | 275 | Periodic manuscript bibliography. |
| S7 | [`preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/build/references.bib`](../../../preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/build/references.bib) | 219 | Boundary-field manuscript bibliography. |

## Bibliography

- Pérez-García, David, Verstraete, Frank , Wolf, Michael M., Cirac, J. Ignacio, Matrix product state representations (2007)
- Pérez-García, David, Verstraete, Frank , Wolf, Michael M., Cirac, J. Ignacio, Matrix product state representations (2007)
- Affleck, Ian, Kennedy, Tom, Lieb, Elliott H. , Tasaki, Hal, Valence bond ground states in isotropic quantum antiferromagnets (1988)
- Affleck, Ian, Lieb, Elliott H., A proof of part of Haldane's conjecture on spin chains (1986)
- Affleck, Ian, Kennedy, Tom, Lieb, Elliott H., Tasaki, Hal, Rigorous results on valence-bond ground states in antiferromagnets (1987)
- Affleck, Ian, Kennedy, Tom, Lieb, Elliott H. , Tasaki, Hal, Valence bond ground states in isotropic quantum antiferromagnets (1988)
- Affleck, Ian, Kennedy, Tom, Lieb, Elliott H., Tasaki, Hal, Rigorous results on valence-bond ground states in antiferromagnets (1987)
- Aizenman, Michael, Nachtergaele, Bruno, Geometric aspects of quantum spin states (1994)
- Aizenman, Michael, Nachtergaele, Bruno, Geometric aspects of quantum spin states (1994)
- Banerjee, Sagnik, Guo, Haoyu, Chowdhury, Debanjan, Bootstrap certification of string order in quantum spin chains (2026)
- Batista, C. D., Ortiz, G., Generalized Jordan–Wigner transformations (2001)
- Bochev, Pavel, Markov, Svetoslav, A Self-Validating Numerical Method for the Matrix Exponential (1989)
- Buyers, W. J. L., Morra, R. M., Armstrong, R. L., Hogan, M. J., Gerlach, P., Hirakawa, K., Experimental evidence for the Haldane gap in a spin-1 nearly isotropic, antiferromagnetic chain (1986)
- Fannes, M., Nachtergaele, B., Werner, R. F., Finitely correlated states on quantum spin chains (1992)
- Fannes, M., Nachtergaele, B., Werner, R. F., Finitely correlated states on quantum spin chains (1992)
- Fox, Bennett L., Glynn, Peter W., Computing Poisson Probabilities (1988)
- Fox, Bennett L., Glynn, Peter W., Computing Poisson Probabilities (1988)
- Fuji, Yohei, Pollmann, Frank, Oshikawa, Masaki, Distinct Trivial Phases Protected by a Point-Group Symmetry in Quantum Spin Chains (2015)
- Goldsztejn, Alexandre, Neumaier, Arnold, On the Exponentiation of Interval Matrices (2014)
- Gosset, David, Mozgunov, Evgeny, Local gap threshold for frustration-free spin systems (2016)
- Haldane, F. D. M., Continuum dynamics of the 1-D Heisenberg antiferromagnet: Identification with the O(3) nonlinear sigma model (1983)
- Haldane, F. D. M., Nonlinear field theory of large-spin Heisenberg antiferromagnets: Semiclassically quantized solitons of the one-dimensional easy-axis {Néel} state (1983)
- Haldane, F. D. M., Ground State Properties of Antiferromagnetic Chains with Unrestricted Spin: Integer Spin Chains as Realisations of the O(3) Non-Linear Sigma Model (1981)
- Haldane, F. D. M., Continuum dynamics of the 1-D Heisenberg antiferromagnet: Identification with the O(3) nonlinear sigma model (1983)
- Haldane, F. D. M., Nonlinear field theory of large-spin Heisenberg antiferromagnets: Semiclassically quantized solitons of the one-dimensional easy-axis {Néel} state (1983)
- Haldane, F. D. M., Ground State Properties of Antiferromagnetic Chains with Unrestricted Spin: Integer Spin Chains as Realisations of the O(3) Non-Linear Sigma Model (1981)
- Kennedy, Tom, Tasaki, Hal, Hidden $\mathbb{Z}_2\times\mathbb{Z}_2$ symmetry breaking in Haldane-gap antiferromagnets (1992)
- Knabe, Stefan, Energy gaps and elementary excitations for certain VBS-quantum antiferromagnets (1988)
- Lemm, Marius, Mozgunov, Evgeny, Spectral gaps of frustration-free spin systems with boundary (2019)
- Lieb, Elliott, Schultz, Theodore, Mattis, Daniel, Two Soluble Models of an Antiferromagnetic Chain (1961)
- Lieb, Elliott, Schultz, Theodore, Mattis, Daniel, Two soluble models of an antiferromagnetic chain (1961)
- Nachtergaele, Bruno, The spectral gap for some spin chains with discrete symmetry breaking (1996)
- Nakamura, Masaaki, Todo, Synge, Order Parameter to Characterize Valence-Bond-Solid States in Quantum Spin Chains (2002)
- den Nijs, Marcel, Rommelse, Koos, Preroughening transitions in crystal surfaces and valence-bond phases in quantum spin chains (1989)
- Ogata, Yoshiko, A $\mathbb{Z}_2$-index of Symmetry Protected Topological Phases with Reflection Symmetry for Quantum Spin Chains (2021)
- OpenAI, A boundary-field gap for the spin-one Heisenberg chain (2026)
- OpenAI, The periodic spin-one Haldane gap (2026)
- Pollmann, Frank, Turner, Ari M., Berg, Erez, Oshikawa, Masaki, Entanglement spectrum of a topological phase in one dimension (2010)
- Suzuki, Masuo, Transfer-matrix method and Monte Carlo simulation in quantum spin systems (1985)
- Tasaki, Hal, Ground state of the $S=1$ antiferromagnetic Heisenberg chain is topologically nontrivial if gapped (2025)
- Tasaki, Hal, Ground state of the $S=1$ antiferromagnetic Heisenberg chain is topologically nontrivial if gapped (2025)
- Tasaki, Hal, Topological Phase Transition and $\mathbb{Z}_2$ Index for $S=1$ Quantum Spin Chains (2018)
- White, Steven R., Huse, David A., Numerical renormalization-group study of low-lying eigenstates of the antiferromagnetic $S=1$ Heisenberg chain (1993)
- White, Steven R., Huse, David A., Numerical renormalization-group study of low-lying eigenstates of the antiferromagnetic $S=1$ Heisenberg chain (1993)
- Yarotsky, D. A., Ground states in relatively bounded quantum perturbations of classical lattice systems (2006)

[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 043](../index/algebraic-and-complex-geometry/043-p-w-for-fixed-determinant-moduli-spaces.md)

# 043 — $P=W$ for fixed-determinant moduli spaces

[Index page](../index/algebraic-and-complex-geometry/043-p-w-for-fixed-determinant-moduli-spaces.md)

## Original CONTENTS.md summary

The release's blurb "**043. P = W for fixed-determinant SL n moduli spaces.** Proves $P_k=W_{2k}=W_{2k+1}$ on the full rational cohomology of smooth coprime fixed-determinant, trace-free Higgs moduli spaces and their character varieties for composite ranks over smooth projective complex curves of genus at least two. [S1:1201]" The manuscript title is
"P=W in composite rank for fixed determinant [S3:1]" , and its abstract reads: "We prove the $P=W$ conjecture on the full rational cohomology of
fixed-determinant, trace-free Higgs moduli spaces in composite rank and
coprime degree, for smooth projective complex curves of genus at least two.
Together with the established prime-rank cases, this gives the equality in
every coprime rank. [S4:11–17]"

## Undergraduate summary

Nonabelian Hodge theory identifies the Higgs moduli space $X$ with
the character variety $X^B$. Each carries a natural filtration:
the Hitchin map's perverse Leray filtration $P$ on the Higgs side,
and the mixed Hodge weight filtration $W$ on the Betti side. The
$P=W$ conjecture asserts $P_k = W_{2k} = W_{2k+1}$ . "Nonabelian Hodge theory identifies two moduli spaces whose cohomology carries very different geometric filtrations. On the Higgs-bundle side, the Hitchin map defines the perverse Leray filtration. On the character-variety side, the mixed Hodge structure defines the weight filtration. The $P=W$ conjecture asserts that these filtrations coincide after doubling the indices of the first. [S5:3]"
The theorem 

> **theorem**
For every smooth projective complex curve $C$ of genus $g\ge2$, every composite integer $n\ge4$, every integer $d$ with $\gcd(n,d)=1$, and every $L\in\mathrm{Pic}^d(C)$, one has
$$P_kH^m(X^B,\mathbb Q)=W_{2k}H^m(X^B,\mathbb Q)
=W_{2k+1}H^m(X^B,\mathbb Q)$$
for all $m,k\ge0$. [S5:39–46]

The assertion covers the full rational cohomology, including the
variant part not captured by quotienting by the torsion-line-bundle
action [S5:48–54]. Combined with the prime-rank theorems, this
resolves $P=W$ in every coprime rank.

## Graduate summary

**The Lefschetz criterion.** The proof constructs a degree-$-2$
operator $f$ satisfying three conditions: $f$ lowers $P$ by 2,
lowers $W$ by 4, and satisfies the double commutator
$[[f,e],e]=-2e$ 

> It remains to construct one degree-$-2$ operator $f$ such that
$$fP_k\subset P_{k-2},\qquad
fW_j\subset W_{j-4},\qquad [[f,e],e]=-2e.$$
An elementary Lefschetz-module argument then identifies both filtrations as sums of eigenspaces of the same operator $[e,f]$. It also handles extensions between filtration grades. [S5:79–84]

An elementary Lefschetz-module argument then identifies both
filtrations as eigenspace sums of $[e,f]$.

**Constructing $f$.** The operator is built from a logarithmic
pole moved over a finite cover, with a flag at the pole. The
logarithmic $\lambda$-connection parameter interpolates between
Higgs bundles and connections 

> To construct $f$, allow one logarithmic pole, move it over a finite cover $S\to C$, and choose a full flag at the pole. The logarithmic $\lambda$-connection parameter interpolates between Higgs bundles at $\lambda=0$ and connections at $\lambda=1$. The underlying moduli constructions and semistable reduction come from ; the restriction argument uses the semiprojective geometry of . We verify the fixed determinant, residue, and flag conditions, as well as compatibility with the full nonabelian-Hodge identification. Write $X_\lambda$ for the fixed-pole scalar-residue moduli space, with $X_0=X$. At scalar residue, the flag space fits into a correspondence
$$X_\lambda\xleftarrow{\ \mathrm{pr}\ }S\times X_\lambda
\xleftarrow{\ \pi\ }Z_\lambda
\xrightarrow{\ \iota\ }Y_{\lambda,0}.$$
Here $Y_{\lambda,0}$ permits a flag-preserving residue with prescribed scalar diagonal, while $Z_\lambda$ requires the residue itself to be scalar. We first deform the ordered residues to distinct values and shift two residue eigenline lattices in opposite directions. Restriction isomorphisms from the total logarithmic Hodge family transport the resulting translation to a degree-zero operator $T$ on $H^*(Y_{\lambda,0})$. On the connection side, $T$ is eigenvalue monodromy. A power has unipotent action, and its logarithm $N$ lowers the diagram weights by two. [S5:86–92]

On the connection side, the translation operator is eigenvalue
monodromy; its logarithm $N$ lowers diagram weights by two. The
resulting operator $f'=\mathrm{pr}_*\pi_*\iota^*N^2\iota_*\pi^*\mathrm{pr}^*$
gives the perverse bound on the Higgs side, and a lattice
Riemann–Roch calculation gives the double commutator.

**The two fixed-determinant steps.** Beyond the
$\mathfrak{sl}_2$ pattern, the construction requires pulling
Mellit's toric stratifications through a determinant-root cover
and proving integral local constancy, plus a finite diagram of
algebraic fibers giving weight zero to the cochains [S5:66–68].
"Our argument constructs an operator on the full cohomology, before taking $\Gamma$-invariants. Its algebraic pattern follows the common $\mathfrak{sl}_2$ structure and flag-correspondence methods of Hausel, Mellit, Minets, and Schiffmann \cite[Proposition 7.9 and Section 8]HMMS2025. The fixed-determinant construction requires two further geometric steps. First, we pull Mellit's toric stratifications through a determinant-root cover and prove integral local constancy and ordinary base change. The inputs include the relative product stratification over ordered eigenvalues, including collisions \cite[Section 7.4, Theorem 7.5, and proof of Proposition 8.7]Mellit2025. This yields curious hard Lefschetz on the full fixed-determinant cohomology, rather than only its invariant part. [S5:66–68]"

## History of the conjecture

The $P=W$ conjecture arose from Hausel–Rodriguez-Villegas's
arithmetic study of character varieties, extended to generic
puncture data. De Cataldo–Hausel–Migliorini formulated the
filtration comparison and proved it in rank two [S5:58–64].
"The weight symmetries behind $P=W$ arose from the arithmetic study of character varieties by Hausel and Rodriguez-Villegas , extended to generic puncture data by Hausel, Letellier, and Rodriguez-Villegas . De Cataldo, Hausel, and Migliorini formulated the filtration comparison and established it in rank two . Their theorem relates the topology of an algebraic integrable system to the mixed Hodge theory of an affine character variety: relative hard Lefschetz on the Higgs side explains curious hard Lefschetz on the Betti side. [S5:58–64]"

For $\mathrm{GL}_n$, tautological class generation was established by
Hausel–Thaddeus (rank 2) and Markman (all ranks); Shende
determined their weights. De Cataldo–Maulik–Shen proved
$P=W$ in genus two. Maulik–Shen proved the coprime $\mathrm{GL}_n$
conjecture in all ranks . "Tautological classes have been central to the higher-rank problem. For $\mathrm{GL}_n$, generation by these classes was established in rank two by Hausel and Thaddeus and in arbitrary rank by Markman \cite[Theorem 7]Markman2002; Shende determined their Betti weights . De Cataldo, Maulik, and Shen proved $P=W$ for $\mathrm{GL}_n$ in genus two and obtained the required perversity bounds for tautological classes in arbitrary genus \cite[Theorems 0.2 and 0.4–0.6]dCMSJAMS2022. [S5:60–62]" Additional proofs
use the Hecke-algebra action and the Fourier-transform method
. "Maulik and Shen proved the coprime $\mathrm{GL}_n$ conjecture in arbitrary rank and genus . Further proofs use the Hecke-algebra action of Hausel, Mellit, Minets, and Schiffmann and the Fourier-transform method of Maulik, Shen, and Yin \cite[Theorem 0.4]MSY2025. [S5:62]"

For fixed determinant, the quotient by $\Gamma$ detects only
invariant cohomology; the variant part was handled in prime rank
by De Cataldo–Maulik–Shen. Maulik–Shen constructed endoscopic
correspondences but did not identify the full filtrations in
composite rank [S5:64].

## Consequences

**$P=W$ in every coprime rank.** The composite-rank theorem
combined with the known prime-rank cases resolves the smooth
coprime fixed-determinant trace-free $P=W$ conjecture for all
$n\ge2$ [S5:39–46].

**Full cohomology, including variant.** The theorem covers every
nontrivial $\Gamma$-character, not just the $\Gamma$-invariant
part [S5:48–54].

**Endoscopic weight equality.** Corollary combining the
all-rank equality with cover-side $\mathrm{GL}_r$ $P=W$ gives the exact
Betti-weight image equality asked in
Maulik–Shen's endoscopy paper [S5:64].

## Section skeleton

**Main file** [S4:11–17], 9 sections under `build/sections/`:

1. Introduction [S5]
2. The Lefschetz comparison criterion [S6]
3. Ordinary base change and curious hard Lefschetz [S7]
4. The diagram weights [S8]
5. The logarithmic restriction isomorphisms [S9]
6. The common operator and its weight bound [S10]
7. The perverse bound by specialization [S11]
8. The double commutator [S12]
9. The conclusion [S13]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
10 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 043 at line 1201. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 164. |
| S3 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/README.md`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/README.md) | 18 | Manuscript readme: title, author, date. |
| S4 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/main.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/main.tex) | 32 | The main file: abstract and section inputs. |
| S5 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/01-introduction.tex) | 101 | The main theorem, the setup, the operator, and the proof organization. |
| S6 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/02-lefschetz.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/02-lefschetz.tex) | 310 | The Lefschetz comparison criterion. |
| S7 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/03-betti.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/03-betti.tex) | 352 | Ordinary base change and curious hard Lefschetz for the Betti family. |
| S8 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/04-diagram.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/04-diagram.tex) | 299 | The diagram weights. |
| S9 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/05-logarithmic.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/05-logarithmic.tex) | 559 | The logarithmic restriction isomorphisms. |
| S10 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/06-translation.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/06-translation.tex) | 178 | The common operator and its weight bound. |
| S11 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/07-specialization.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/07-specialization.tex) | 305 | The perverse bound by specialization. |
| S12 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/08-commutator.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/08-commutator.tex) | 298 | The double commutator. |
| S13 | [`preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/09-conclusion.tex`](../../../preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/build/sections/09-conclusion.tex) | 111 | The conclusion. |

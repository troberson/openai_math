[Notes](../../README.md) / [Summaries](../README.md) / [Algebra](../../index/disciplines/algebra.md) / [Family 193](../../index/algebra/193-serres-intersection-multiplicity-conjecture.md)

# 193 — Serre's intersection-multiplicity conjecture

[Index page](../../index/algebra/193-serres-intersection-multiplicity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4434] and the catalog abstract [S2:467] state
the family's claim: strict positivity of Serre's intersection
multiplicity $\chi^R(M,N)$ for nonzero finitely generated modules over
any regular local ring, provided $M\otimes_R N$ has finite length and
$\dim M+\dim N=\dim R$, resolving the positivity conjecture including
ramified mixed characteristic. The manuscript's abstract
 "We prove Serre's positivity conjecture, including ramified mixed
characteristic. If two nonzero finitely generated modules over a regular local
ring have tensor product of finite length and complementary dimensions, then
their intersection multiplicity is strictly positive. [S3:41–44]"

## Undergraduate summary

For a finite $R$-module over a $d$-dimensional regular local ring
$(R,\m)$, the intersection multiplicity of two modules $M,N$ with
finite-length tensor product is the alternating sum of the Tor lengths,
$\chi^R(M,N)=\sum_{i=0}^d(-1)^i\length_R\Tor_i^R(M,N)$
[S4:4–14]. It measures the local intersection of the two supports,
accounting for the higher Tor terms, which enter with alternating signs
— so positivity is not a formal consequence of the degree-zero term.
Serre's positivity conjecture asks that, when the two modules are
nonzero, have complementary dimensions, and their tensor product has
finite length, this number is strictly positive. The manuscript proves
the full conjecture 

> **theorem**
Let $(R,\mathfrak{m})$ be a commutative Noetherian regular local ring of dimension
$d$, and let $M,N$ be nonzero finitely generated $R$-modules. If
$\mathrm{length}_R(M\otimes_R N)<\infty$ and
$\dim_R M+\dim_R N=d$, then
\[
  \chi^R(M,N)>0.
\] [S4:16–24]

Complementary dimensions means $\dim M+\dim N=d$, so the two supports
meet in dimension zero — the closed point — and the finite-length
condition makes every Tor length finite.

## Graduate summary

**Why the general case is hard.** Serre's own diagonal reduction
proves positivity in equicharacteristic and in the unramified setting,
and the same argument reaches formal power series over a complete
discrete valuation ring; Roberts and Gillet–Soulé proved vanishing when
the dimension sum is below $d$, and Gabber proved *nonnegativity* in the
remaining mixed-characteristic case using alterations. Positive
characteristic or unramified hypotheses are what the diagonal argument
needs, so ramified mixed characteristic — where the residue
characteristic $p$ lies in $\m^2$ — is the genuinely open case: the
existing routes give $\ge0$ there, and the theorem must additionally
rule out zero [S4:39–88]. Skalit's and KC–Soto Levins' partial
positivity results impose smoothness or a Serre-liftability condition
that the theorem drops [S4:39–88].

**The two comparisons.** The proof combines normalized-length methods
with algebraic $K$-theory. After reducing to two complete local domains
of complementary dimensions, each with a finite Galois extension over a
regular normalization base, the argument makes two norm comparisons.
The first is in rational $K$-theory with support at the closed point:
ordinary and normalized Euler lengths agree after summing over all
Galois conjugates, reducing the claim to showing each individual twist
is positive. The second works in a category that kills free sequences
of negligible normalized rank, where supported objects have nonnegative
homology lengths; the uniform annihilator and a positive lower bound on
the normalized number of generators of an approximating sequence force
each value strictly positive [S4:92–177]. No invariance of a
normalized-length function under a Galois group is assumed, and no
perfectoid tower on a quotient domain is needed — the proof uses
bounded complexes modulo free sequences of negligible normalized rank
[S4:92–177].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Serre introduced intersection multiplicities through the Euler
characteristic of Tor and proved positivity in the diagonal (equichar
and unramified) cases in Chapter V of his monograph. Roberts and,
independently, Gillet–Soulé proved vanishing below the complementary
dimension using local Chern characters and Adams operations, and Gabber
proved nonnegativity in the mixed-characteristic remainder via
alterations. The open ramified case then saw partial results —
Skalit's positivity for essentially smooth essentially-two-dimensional
bases, and KC–Soto Levins' liftability-restricted positivity — each
leaving a characteristic/ramification hypothesis or a smoothness
assumption in place, which the present theorem removes [S4:39–88]. The
proof's machinery descends from Faltings' normalized-length formalism,
the Gabber–Ramero and Bhatt–Scholze almost/perfected foundations, and
the Land–Tamme descent theorem for truncating invariants
[S4:92–177].

## Consequences

**Symbolic powers in the ramified case.** The Kurano–Roberts
positivity-to-symbolic-power theorem now applies in ramified mixed
characteristic: for primes $P,Q$ with
$\sqrt{P+Q}=\m$ and $\ht P+\ht Q=\dim R$,
$P\cap Q^{(r)}\subseteq\m^{r+1}$ for $r\ge1$ [S4:181–198].

**A finite strict-transform intersection inequality.** Applying
Skalit's finite-support blowup argument with the theorem as positivity
input gives, for prime ideals of complementary dimension with
$\dim T\le1$ where $T$ is the tensor product of the associated graded
rings,
$\chi^A(A/P,A/Q)\ge e_\m(A/P)e_\m(A/Q)$, with equality exactly when
$\dim T=0$ 

> **corollary**
Let $(A,\mathfrak{m})$ be a commutative Noetherian regular local ring with residue
field $k$, and let $P,Q$ be prime ideals such that $A/(P+Q)$ has finite
length and $\dim(A/P)+\dim(A/Q)=\dim A$. Write $e_\mathfrak{m}$ for Hilbert–Samuel
multiplicity and put
\[
 T=\operatornamegr(A/P)\otimes_{\operatornamegrA}\operatornamegr(A/Q),
\]
where all associated graded rings use the maximal-ideal filtrations.
If $\dim T\leq1$, then
\[
 \chi^A(A/P,A/Q)\geq e_\mathfrakm(A/P)e_\mathfrakm(A/Q),
\]
with equality if and only if $\dim T=0$. [S4:200–214]

## Section skeleton

**Manuscript** [S3:41–44], 5 sections under `build/sections/`:
introduction [S4], lengths, descent, asymptotic, positivity.

The manuscript's root is `build/paper.tex`, with a `references.tex`
bibliography (a `thebibliography` block) [S5]. It ships no
`verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 7 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 193 at line 4434. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 467. |
| S3 | [`preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/paper.tex`](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/paper.tex) | 53 | Main file: title and abstract. |
| S4 | [`preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/sections/introduction.tex`](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/sections/introduction.tex) | 261 | The main theorem, the background and significance, the proof strategy with its two comparisons, the finite strict-transform corollary, and the conventions. |
| S5 | [`preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/references.tex`](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/references.tex) | 227 | The manuscript's bibliography. |

## Bibliography

- The Stacks Project Authors, _The Stacks Project_, Tag 0815, Tag 03QH, Tag 0BRI, and Tag 0BRJ, accessed September 23, 2026.
- P. Berthelot, Altérations de variétés algébriques [d'apr\`es A. J. de Jong], _Astérisque_ **241** (1997), Exp. 815, 273–311; Section 6.1, Theorem 6.1.1 (Gabber).  .
- B. Bhatt, M. Hochster, and L. Ma, Lim Cohen–Macaulay sequences of modules, _J. Reine Angew. Math._ **835** (2026), 111–169. Numbered references follow arXiv:2410.18372v2, August 25, 2026.
- A. J. Blumberg, D. Gepner, and G. Tabuada, A universal characterization of higher algebraic $K$-theory, _Geom. Topol._ **17** (2013), 733–838. doi:10.2140/gt.2013.17.733. Numbered references follow arXiv:1001.2282v4, February 5, 2013.
- H. Cai, S. Lee, L. Ma, K. Schwede, and K. Tucker, Perfectoid signature, perfectoid Hilbert–Kunz multiplicity, and an application to local fundamental groups, _Invent. Math._ **244** (2026), 357–454. doi:10.1007/s00222-025-01399-w. Numbered references follow arXiv:2209.04046v4, July 3, 2025.
- V. Drinfeld, DG quotients of DG categories, _J. Algebra_ **272** (2004), no. 2, 643–691. doi:10.1016/j.jalgebra.2003.05.001. Numbered references follow arXiv:math/0210114v7, February 17, 2008.
- S. P. Dutta, A special case of positivity (II), _Proc. Amer. Math. Soc._ **133** (2005), no. 7, 1891–1896. doi:10.1090/S0002-9939-05-07929-3.
- G. Faltings, Almost étale extensions, _Astérisque_ **279** (2002), 185–270. Numdam: AST\_2002\_\_279\_\_185\_0.
- T. G. Goodwillie, Relative algebraic $K$-theory and cyclic homology, _Ann. of Math. (2)_ **124** (1986), no. 2, 347–402. doi:10.2307/1971283.
- U. Jannsen, Resolution of singularities for embedded curves, Appendix A to S. Saito and K. Sato, A finiteness theorem for zero-cycles over $p$-adic fields, _Ann. of Math. (2)_ **172** (2010), no. 3, 1593–1639, Proposition A.4(1).  .
- N. KC and A. J. Soto Levins, On liftings of modules of finite projective dimension, _Int. Math. Res. Not. IMRN_ **2024**, no. 24, 14729–14736. doi:10.1093/imrn/rnae257. Numbered references follow arXiv:2404.17572v2, November 5, 2024.
- L. Ma, Lech's conjecture in dimension three, _Adv. Math._ **322** (2017), 940–970. doi:10.1016/j.aim.2017.10.032. Numbered references follow arXiv:1609.00095v3, February 13, 2018.
- P. Monsky, The Hilbert–Kunz function, _Math. Ann._ **263** (1983), no. 1, 43–49. doi:10.1007/BF01457082.
- OpenAI, Lech's multiplicity conjecture, OpenAI Math Release preprint OAI:Lechs-multiplicity-conjecture-September-23-2026, 2026.
- O. Gabber and L. Ramero, _Foundations for almost ring theory—Release 7.5_, arXiv:math/0409584v13, September 29, 2018.
- K. Kurano and P. C. Roberts, The positivity of intersection multiplicities and symbolic powers of prime ideals, _Compositio Math._ **122** (2000), no. 2, 165–182. doi:10.1023/A:1001741230307.
- P. Roberts, The vanishing of intersection multiplicities of perfect complexes, _Bull. Amer. Math. Soc. (N.S.)_ **13** (1985), no. 2, 127–130. doi:10.1090/S0273-0979-1985-15394-7.
- P. Roberts, Intersection multiplicities in commutative algebra, _Publications de l'Institut de recherche mathématiques de Rennes_ (1985), fasc. 4, 25–39.  .
- P. Roberts, Intersection theorems, in _Commutative Algebra_ (Berkeley, CA, 1987), M. Hochster, C. Huneke, and J. D. Sally (eds.), Mathematical Sciences Research Institute Publications **15**, Springer, New York, 1989, 417–436. doi:10.1007/978-1-4612-3660-3\_23.
- P. Balmer and M. Schlichting, Idempotent completion of triangulated categories, _J. Algebra_ **236** (2001), 819–834. doi:10.1006/jabr.2000.8529.
- B. Bhatt and P. Scholze, Prisms and prismatic cohomology, _Ann. of Math. (2)_ **196** (2022), no. 3, 1135–1275. doi:10.4007/annals.2022.196.3.5. Numbered references follow arXiv:1905.08229v4, January 12, 2022.
- J.-P. Serre, _Local Algebra_, translated by C. W. Chin, Springer Monographs in Mathematics, Springer, Berlin, 2000, Chapter V. doi:10.1007/978-3-662-04203-8.
- S. Ishiro and K. Shimomoto, $\delta$-rings, perfectoid towers, and lim Cohen–Macaulay sequences, preprint, arXiv:2509.06527v3, May 31, 2026.
- K. Kurano and K. Shimomoto, An elementary proof of Cohen–Gabber theorem in the equal characteristic $p>0$ case, _Tohoku Math. J. (2)_ **70** (2018), no. 3, 377–389, Theorem 1.1. arXiv:1510.03573.
- C. Skalit, Positivity of intersection multiplicity over a two-dimensional base, _J. Pure Appl. Algebra_ **223** (2019), no. 4, 1801–1816. doi:10.1016/j.jpaa.2018.07.008. Numbered references follow arXiv:1510.05146v2, July 31, 2018.
- C. Skalit, Intersection multiplicity of Serre in the unramified case, _J. Algebra_ **428** (2015), 91–121. doi:10.1016/j.jalgebra.2014.12.040. Numbered references follow arXiv:1409.3616v2, December 10, 2014.
- H. Gillet and C. Soulé, Intersection theory using Adams operations, _Invent. Math._ **90** (1987), no. 2, 243–277. doi:10.1007/BF01388705.
- M. Land and G. Tamme, On the $K$-theory of pullbacks, _Ann. of Math. (2)_ **190** (2019), no. 3, 877–930. doi:10.4007/annals.2019.190.3.4. Numbered references follow arXiv:1808.05559v3, November 8, 2019.
- R. W. Thomason and T. Trobaugh, Higher algebraic $K$-theory of schemes and of derived categories, in _The Grothendieck Festschrift_, Vol. III, Progress in Mathematics **88**, Birkhäuser Boston, 1990, 247–435. Original-edition text.

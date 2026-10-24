[Notes](../../README.md) / [Summaries](../README.md) / [Number theory](../../index/disciplines/number-theory.md) / [Family 029](../../index/number-theory/029-artins-primitive-root-conjecture-infinitude-for-every-base.md)

# 029 — Artin's primitive root conjecture: infinitude for every base

[Index page](../../index/number-theory/029-artins-primitive-root-conjecture-infinitude-for-every-base.md)

## Original CONTENTS.md summary

The release's blurb "**029. Primitive roots for every admissible integer base.** Proves the infinitude assertion in Artin's primitive root conjecture [S1:698]" The catalog abstract 
expands on it: "Proves the infinitude assertion in Artin's primitive root conjecture for every integer $a$ that is neither $-1$ nor a square. For each such base, at least $c_a x/(\log x)^2$ primes in every sufficiently large interval $(x,2x)$ have primitive root $a$, with $c_a>0$. [S2:134]" The two manuscripts are
"Primitive roots for every admissible integer base [S3:1]" and "Simultaneous primitive roots: a conditional lower bound for prime bases [S4:1]" .

## Undergraduate summary

A prime $p$ has $a$ as a primitive root when the multiplicative order
$\ord_p(a)=p-1$. Artin's 1927 conjecture asserts that every "admissible"
integer (not $-1$, not a square) is a primitive root modulo infinitely
many primes. The theorem 

> **Theorem 1.1**
For every admissible integer $a$, there are constants $c_a>0$ and
$x_a\ge2$ such that, for every real $x\ge x_a$,
\[
 #\{p prime:x<p<2x,\ p\nmid a,\ \ord_p(a)=p-1\}
       \ge c_a\fracx{(\log x)^2}.
\] [S6:17–24]

The predicted scale is $x/\log x$; the theorem gives $x/(\log x)^2$ in
every dyadic interval — a square-root loss in the log, but unconditional
and base-specific . "The predicted counting scale is $x/\log x$; the theorem gives
$x/(\log x)^2$ in every sufficiently large dyadic interval. In
particular, it proves the infinitude assertion for each fixed
admissible integer, including the prescribed base $2$. The constants
and the threshold may depend on the base. [S6:26–30]"

## Graduate summary

**The analytic engine.** The proof establishes a uniform zero-free region
for Hecke $L$-functions 

> **Theorem 1.2**
Let $F$ be a cyclotomic number field containing $\mu_{12}$.
For every finite-order Hecke character $\eta$ of $F$, the meromorphic
continuation of $L_F(s,\eta)$ has no zeros in
\[
 \operatornameRe s>1-10^-6.
\] [S6:38–45]

The width $10^{-6}$ is common to all cyclotomic fields containing
$\mu_{12}$ and all finite-order Hecke characters, with no conductor
cutoff [S6:47–53]. This uniformity is what allows a single splitting
estimate to handle a growing family of Kummer fields [S14].

**The reduction.** The problem reduces to counting primes with a
controlled predecessor in a fixed arithmetic progression [S18]. The
predecessor construction uses a cubic theta input, a reflection argument
with the quadratic large sieve, and a Poisson probe whose Euler product
gives the zero-free region [S10] [S11] [S12]. The Type II estimates
control the remaining bilinear sums [S15].

**The companion manuscript.** The second paper [S21] extends the
construction to simultaneous primitive roots for a fixed finite set of
prime bases. It is an implication from four inputs taken from the first
manuscript "Our result is an implication from four statements taken from the companion
manuscript  : a uniform Hecke zero-free assertion
(Input  ), a marked Type II estimate
(Input  ), a block sieve (Input  ), and a
rough-number density estimate (Input  ).  We reproduce
these statements in the precise forms used here.  They are hypotheses of
the following theorem; their proofs in   and its cited
companion manuscripts are outside the scope of this paper. [S21:23–30]" The conditional theorem 

> **theorem**
Assume Inputs  ,  ,
 , and  .  Let \(k\ge1\) and let
\(q_1,\ldots,q_k\) be distinct positive primes.  There are constants
\(c_{\mathbf q}>0\) and \(x_{\mathbf q}>1\) such that, for every real
\(x\ge x_{\mathbf q}\), at least
\[
        c_{\mathbf q}\fracx{(\log x)^2}
\]
primes \(p\in(x,2x)\) satisfy
\[
        p\nmid q_1\cdots q_k,
        \qquad
        \ord_p(q_i)=p-1\quad(1\le i\le k).
\] [S21:32–47]

The reduction [S22] shows the four inputs suffice; the marked family
construction [S24] and the prime-reservoir extraction [S25] complete
the argument.

## History of the conjecture

Hooley proved Artin's asymptotic under the Riemann hypothesis for the
Dedekind zeta functions of the Kummer fields
$\Q(\mu_n,a^{1/n})$ . "Hooley proved Artin's predicted asymptotic under the Riemann hypothesis
for the Dedekind zeta functions of the Kummer fields
$\mathbb{Q}(\mu_n,a^{1/n})$, with $n$ squarefree  .
These fields encode the obstructions to maximal order. For a prime
$q$ and $p\nmid aq$, the conditions
\[
 p\equiv1\pmod q,\qquad a^(p-1)/q\equiv1\pmod p
\]
say that $p$ splits completely in $\mathbb{Q}(\mu_q,a^{1/q})$.
They hold precisely when $q$ divides the index
$(p-1)/\ord_p(a)$. Hooley's method counts and sums such splitting
conditions. Here a restricted factorization of $p-1$ confines the
possible index divisors to ranges where they can all be removed. [S6:57–69]" The Kummer fields encode
the obstructions: for $q|(p-1)/\ord_p(a)$, the prime $p$ splits
completely in $\Q(\mu_q,a^{1/q})$.

Unconditional results allow only a finite choice of bases [S6:71–76].
"Classical unconditional results allow a finite choice of bases.
Gupta and Murty constructed a set of thirteen integers from three
distinct primes, at least one of which is a primitive root modulo
infinitely many primes  . Heath-Brown proved that
at most two prime bases fail the infinitude assertion, so at least
one of $2,3,5$ satisfies it  . [S6:71–76]" Averaging over the base gives asymptotics for almost all
integers in a short range, but the exceptional set may depend on $x$
[S6:77–82].

## Consequences

**Simultaneous primitive roots.** Given the four analytic inputs from
the first manuscript, the second proves a positive-density lower bound
for primes $p$ where every member of a fixed set of $k$ prime bases
is simultaneously a primitive root [S21:32–47]. The bound is
$c_{\mathbf q}\,x/(\log x)^2$ in every dyadic interval, with constants
depending only on the chosen bases.

## Section skeleton

**Manuscript A** (main file [S5], 13 sections under `build/sections/`):

1. Introduction [S6]
2. Reduction to controlled predecessors and complete splitting [S7]
3. S-integers, residue symbols, and Gauss sums [S8]
4. The coefficient family and analytic comparison [S9]
5. The normalized cubic theta input and its radial profiles [S10]
6. Reflection and the quadratic large sieve [S11]
7. The Poisson probe and its Euler product [S12]
8. Zero detection and Mellin continuation [S13]
9. A uniform estimate for complete splitting [S14]
10. Marked Type II estimates and rough factors [S15]
11. The cubic theta normalization [S16]
12. Two elementary sieve facts [S17]
13. Primes with a controlled predecessor in a fixed progression [S18]

Bibliography: `references.tex` [S19].

**Manuscript B** (main file [S20], 5 sections under `build/sections/`):

1. Introduction [S21]
2. Reduction to two estimates [S22]
3. A uniform splitting estimate [S23]
4. A marked family in a fixed progression [S24]
5. Extracting primes from the marked family [S25]

Bibliography: `references.tex` [S26].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. Manuscript A ships
14 `.tex` files under `build/`; manuscript B ships 7.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 029 at line 698. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 134. |
| S3 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/README.md`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S4 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/README.md`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S5 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/main.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/main.tex) | 91 | The main file: document class, packages, and section inputs. |
| S6 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex) | 219 | The main theorem, the Hecke zero-free theorem, the historical context, and the two obstructions. |
| S7 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01a-reduction.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01a-reduction.tex) | 216 | Reduction to controlled predecessors and complete splitting. |
| S8 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/02-arithmetic.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/02-arithmetic.tex) | 625 | S-integers, residue symbols, and Gauss sums. |
| S9 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/02a-coefficient-family.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/02a-coefficient-family.tex) | 179 | The coefficient family and analytic comparison. |
| S10 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/03-theta.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/03-theta.tex) | 775 | The normalized cubic theta input and its radial profiles. |
| S11 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/04-reflection.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/04-reflection.tex) | 1228 | Reflection and the quadratic large sieve. |
| S12 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex) | 765 | The Poisson probe and its Euler product. |
| S13 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/06-zero-free.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/06-zero-free.tex) | 764 | Zero detection and Mellin continuation. |
| S14 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/07-splitting.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/07-splitting.tex) | 247 | A uniform estimate for complete splitting. |
| S15 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/08-type-ii.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/08-type-ii.tex) | 536 | Marked Type II estimates and rough factors. |
| S16 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/10-whittaker-calculation.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/10-whittaker-calculation.tex) | 495 | The cubic theta normalization. |
| S17 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/11-sieve.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/11-sieve.tex) | 277 | Two elementary sieve facts. |
| S18 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/12-construction.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/12-construction.tex) | 818 | Primes with a controlled predecessor in a fixed progression. |
| S19 | [`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/references.tex`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/references.tex) | 209 | The bibliography. |
| S20 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/paper.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/paper.tex) | 49 | The main file: document class, theorem environments, and section inputs. |
| S21 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/01-introduction.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/01-introduction.tex) | 58 | The conditional theorem, the four inputs from the companion, and the proof strategy. |
| S22 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/02-reduction.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/02-reduction.tex) | 119 | Reduction to two estimates. |
| S23 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/03-splitting.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/03-splitting.tex) | 214 | A uniform splitting estimate. |
| S24 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/04-marked-family.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/04-marked-family.tex) | 499 | A marked family in a fixed progression. |
| S25 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/05-prime-reservoir.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/05-prime-reservoir.tex) | 610 | Extracting primes from the marked family. |
| S26 | [`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/references.tex`](../../../preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/references.tex) | 84 | The bibliography. |

## Bibliography

- E. Bombieri, On the large sieve, _Mathematika_ **12** (1965), no. 2, 201–225. doi:10.1112/S0025579300005313.
- E. Bombieri, On the large sieve, _Mathematika_ **12** (1965), no. 2, 201–225. doi:10.1112/S0025579300005313.
- A. Buchstab, Asymptotische Abschätzung einer allgemeinen zahlentheoretischen Funktion, _Rec. Math. [Mat. Sbornik] N.S._ **2(44)** (1937), no. 6, 1239–1246 (Russian, with a German summary). MathNet record and original text.
- M. Goldfeld, Artin's conjecture on the average, _Mathematika_ **15** (1968), no. 2, 223–226. doi:10.1112/S0025579300002606.
- K. Ford and H. Halberstam, The Brun–Hooley sieve, _J. Number Theory_ **81** (2000), no. 2, 335–350. doi:10.1006/jnth.1999.2479.
- E. Hasanalizade, Q. Shen, and P.-J. Wong, Counting zeros of Dedekind zeta functions, _Math. Comp._ **91** (2022), no. 333, 277–293. doi:10.1090/mcom/3665.
- E. Hasanalizade, Q. Shen, and P.-J. Wong, Counting zeros of Dedekind zeta functions, _Math. Comp._ **91** (2022), no. 333, 277–293. doi:10.1090/mcom/3665.
- E. Artin and H. Hasse, _Emil Artin und Helmut Hasse: Die Korrespondenz 1923–1934_, edited and commented by G. Frei and P. Roquette, with F. Lemmermeyer, Universitätsverlag Göttingen, 2008. Publisher's edition.
- H. Hasse, _Die mathematischen Tagebücher von Helmut Hasse 1923–1935_, edited by F. Lemmermeyer and P. Roquette, Universitätsverlag Göttingen, 2012. Publisher's edition.
- D. R. Heath-Brown, Artin's conjecture for primitive roots, _Quart. J. Math. Oxford_ (2) **37** (1986), no. 1, 27–38. doi:10.1093/qmath/37.1.27.
- D. R. Heath-Brown, A mean value estimate for real character sums, _Acta Arith._ **72** (1995), no. 3, 235–275. doi:10.4064/aa-72-3-235-275.
- D. R. Heath-Brown, Artin's conjecture for primitive roots, _Quart. J. Math. Oxford_ (2) **37** (1986), no. 1, 27–38. doi:10.1093/qmath/37.1.27.
- C. Hooley, On Artin's conjecture, _J. Reine Angew. Math._ **225** (1967), 209–220. doi:10.1515/crll.1967.225.209.
- C. Hooley, On Artin's conjecture, _J. Reine Angew. Math._ **225** (1967), 209–220. doi:10.1515/crll.1967.225.209.
- A. Hoshi and K. Kanai, Davenport and Hasse's theorems and lifts of multiplication matrices of Gaussian periods, _Finite Fields Appl._ **84** (2022), article 102101. doi:10.1016/j.ffa.2022.102101.
- O. Klurman, I. E. Shparlinski, and J. Teräväinen, On Artin's conjecture on average and short character sums, _Bull. Lond. Math. Soc._ **57** (2025), no. 8, 2429–2443. doi:10.1112/blms.70103.
- T. Kubota, Topological covering of $\mathrm{SL}(2)$ over a local field, _J. Math. Soc. Japan_ **19** (1967), no. 1, 114–121. doi:10.2969/jmsj/01910114.
- L. Goldmakher and B. Louvel, A quadratic large sieve inequality over number fields, _Math. Proc. Cambridge Philos. Soc._ **154** (2013), no. 2, 193–212. doi:10.1017/S0305004112000370.
- K. Matthews, A generalisation of Artin's conjecture for primitive roots, _Acta Arith._ **29** (1976), no. 2, 113–146. doi:10.4064/aa-29-2-113-146.
- R. Gupta and M. R. Murty, A remark on Artin's conjecture, _Invent. Math._ **78** (1984), no. 1, 127–130. doi:10.1007/BF01388719.
- R. Gupta and M. Ram Murty, A remark on Artin's conjecture, _Invent. Math._ **78** (1984), no. 1, 127–130. doi:10.1007/BF01388719.
- J. Neukirch, _Algebraic Number Theory_, translated by N. Schappacher, Grundlehren der mathematischen Wissenschaften, vol. 322, Springer, Berlin, 1999. doi:10.1007/978-3-662-03983-0.
- J. Neukirch, _Algebraic Number Theory_, translated by N. Schappacher, Grundlehren der mathematischen Wissenschaften, vol. 322, Springer, Berlin, 1999. doi:10.1007/978-3-662-03983-0.
- OpenAI, Weighted dilation graphs, smooth shifted primes and totient fibers, OpenAI Math Release preprint OAI:Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026, 2026. Lemmas 2.9 and 7.4.
- OpenAI, The Poisson–Dirichlet law for prime predecessors, OpenAI Math Release preprint OAI:The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026, 2026. Theorem 3.1 and Sections 3–5.
- OpenAI, Prime Predecessors with an Even Number of Prime Factors, OpenAI Math Release preprint OAI:Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026, 2026. Section 3, especially Lemmas 3.1 and 3.3.
- OpenAI, The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\mathrm{Re}(s)>7/8$, OpenAI Math Release preprint OAI:The-Quasi-Riemann-Hypothesis-September-30-2026, 2026. Part I, Sections 5–7.
- OpenAI, Primitive roots for every admissible integer base, OpenAI Math Release preprint OAI:Primitive-roots-for-every-admissible-integer-base-October-4-2026, 2026.
- M. Anwar and F. Pappalardi, On simultaneous primitive roots, _Acta Arith._ **180** (2017), no. 1, 35–43. doi:10.4064/aa8566-3-2017.
- D. A. Kazhdan and S. J. Patterson, Metaplectic forms, _Publ. Math. Inst. Hautes Études Sci._ **59** (1984), 35–142. doi:10.1007/BF02698770.
- D. A. Kazhdan and S. J. Patterson, Corrections to _Metaplectic forms_, _Publ. Math. Inst. Hautes Études Sci._ **62** (1985), 203. doi:10.1007/BF02698809.
- S. J. Patterson, A cubic analogue of the theta series, _J. Reine Angew. Math._ **296** (1977), 125–161. doi:10.1515/crll.1977.296.125.
- S. J. Patterson, A cubic analogue of the theta series. II, _J. Reine Angew. Math._ **296** (1977), 217–220. doi:10.1515/crll.1977.296.217.
- P. J. Stephens, An average result for Artin's conjecture, _Mathematika_ **16** (1969), no. 2, 178–188. doi:10.1112/S0025579300008159.
- J. T. Tate, Fourier analysis in number fields and Hecke's zeta-functions, in _Algebraic Number Theory_, edited by J. W. S. Cassels and A. Fröhlich, Academic Press, London, 1967, 305–347. Scan of the volume.
- J. T. Tate, Fourier analysis in number fields and Hecke's zeta-functions, in _Algebraic Number Theory_, edited by J. W. S. Cassels and A. Fröhlich, Academic Press, London, 1967, 305–347. Scan of the volume.
- A. I. Vinogradov, On the density hypothesis for Dirichlet $L$-series, _Izv. Akad. Nauk SSSR Ser. Mat._ **29** (1965), no. 4, 903–934 (Russian). MathNet record and original text. Correction, _ibid._ **30** (1966), no. 3, 719–720; MathNet record and correction.
- A. I. Vinogradov, On the density hypothesis for Dirichlet $L$-series, _Izv. Akad. Nauk SSSR Ser. Mat._ **29** (1965), no. 4, 903–934 (Russian). MathNet record and original text. Correction, _ibid._ **30** (1966), no. 3, 719–720; MathNet record and correction.
- A. Weil, Sur certains groupes d'opérateurs unitaires, _Acta Math._ **111** (1964), 143–211. doi:10.1007/BF02391012.
- S. Baier and M. P. Young, Mean values with cubic characters, _J. Number Theory_ **130** (2010), no. 4, 879–903. doi:10.1016/j.jnt.2009.11.007. The cited equation numbering is that of arXiv:0804.2233v4.
- J. Thorner and A. Zaman, A unified and improved Chebotarev density theorem, _Algebra Number Theory_ **13** (2019), no. 5, 1039–1068. doi:10.2140/ant.2019.13.1039.
- A. Dunn and M. Radziwił{}ł{}, Bias in cubic Gauss sums: Patterson's conjecture, _Ann. of Math._ (2) **200** (2024), no. 3, 967–1057. doi:10.4007/annals.2024.200.3.3. Author version: arXiv:2109.07463v3.

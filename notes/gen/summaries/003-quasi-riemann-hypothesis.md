[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 003](../index/number-theory/003-quasi-riemann-hypothesis.md)

# 003 — The quasi-Riemann hypothesis

[Index page](../index/number-theory/003-quasi-riemann-hypothesis.md)

## Original CONTENTS.md summary

The release blurb 

> **003. The quasi-Riemann hypothesis.** Proves that every Dirichlet L-function, including $`\zeta(s)`$, is zero-free in $`\Re s\gt 7/8`$, resolving the quasi-Riemann hypothesis. The same half-plane is zero-free for every finite-order Hecke L-function over $`\mathbb Q(\sqrt{-3})`$. A companion gives a different proof of the zero-free half-plane $`\Re s\gt 11/12`$. [S1:66]

The headline manuscript (September 30) proves the stronger 7/8 bound


> We prove that all finite-order Hecke $L$-functions over
$\mathbb Q(\sqrt{-3})$ and all Dirichlet $L$-functions are zero-free in
the half-plane $\Re s>7/8$, with the principal pole at $s=1$ allowed.
In particular, the Riemann zeta function is zero-free in this half-plane,
proving the quasi-Riemann hypothesis. [S2:37–43]

The companion (October 5) proves a weaker 11/12 bound by a different
route — mean-square estimates for twisted Möbius sums — and draws its
own corollary for primes in arithmetic progressions [S3:84–95]. The
third manuscript (October 1) is a uniform Landau–Siegel exclusion


> We prove the uniform exclusion of Landau–Siegel zeros. There is an
absolute constant $c>0$ such that every real zero $\beta\in(0,1)$ of
every primitive nonprincipal real Dirichlet $L$-function of conductor
$q\ge3$ satisfies $(1-\beta)\log q\ge c$. [S4:41–46]

## Undergraduate summary

The quasi-Riemann hypothesis asks: is there a fixed number $\theta < 1$
such that the zeta function has no zeros in the half-plane
$\Re s > \theta$? This is weaker than the full Riemann Hypothesis
(all nontrivial zeros on $\Re s = 1/2$), but already implies the
prime number theorem with a power-saving error term.

This family provides three results. The headline paper proves
$\theta = 7/8$: every Dirichlet $L$-function and every finite-order
Hecke $L$-function over $\mathbb{Q}(\sqrt{-3})$ is zero-free in
$\Re s > 7/8$. A companion paper proves the weaker $\theta = 11/12$
by a different method (mean-square estimates), and draws a
quantitative corollary for the distribution of primes in arithmetic
progressions. A third paper proves a uniform gap for Landau–Siegel
zeros: there exists $c > 0$ such that every real zero $\beta$ of every
primitive nonprincipal real Dirichlet $L$-function of conductor $q
\ge 3$ satisfies $(1 - \beta) \log q \ge c$.

The companion's PNT corollary 

> **corollary**
Let $\pi(x;q,a)$ count the primes $p\le x$ with $p\equiv a\pmod q$.
Write $\varphi$ for Euler's totient function.
For $x\ge2$,
$$\sup_{\substack{1\le q\le x\\(a,q)=1}}
 \biggl|\pi(x;q,a)-\frac1{\varphi(q)}
                  \int_2^x\frac{\,d t}{\log t}\biggr|
 \ll x^{11/12}\log x,$$
where the implied constant is absolute and effective. [S3:84–95]

## Graduate summary

The family ships three manuscripts proving zero-free half-planes by
independent routes, plus a uniform Landau–Siegel exclusion.

**Headline (7/8).** Theorem 

> **theorem**
Every finite-order Hecke $L$-function over
$F=\mathbb Q(\sqrt{-3})$ has no zero in $\Re s>7/8$.
The same holds for every Dirichlet $L$-function, including $\zeta(s)$.
A pole at $s=1$ for a principal character is allowed. [S2:106–111]

The proof proceeds through a common-signal argument: embed the
$M$öbius sum in a family, apply Poisson summation twice, and use
cancellation in the dual mean square to obtain power saving. The
result is the first conductor-independent zero-free half-plane for
Dirichlet $L$-functions.

**Companion (11/12).** Theorem 

> **theorem**
Every finite-order Hecke $L$-function over $K$ has no zeros in the half-plane $\mathrm{Re} s>11/12$. Thus every Dirichlet $L$-function, including $\zeta(s)$, has no zeros for $\mathrm{Re} s>11/12$. [S3:73–75]

The route is mean-square estimates for twisted Möbius sums with
cube factors removed by a theta-function reflection. The manuscript
explicitly positions 11/12 as an intermediate step toward the 7/8
bound: "For simplicity, we have isolated Theorem `thm:main` and its
proof here" [S3:81].

**Landau–Siegel exclusion.** Theorem [S4:66–73]: a uniform
logarithmic gap $(1-\beta)\log q \ge c$ for real zeros of primitive
nonprincipal real Dirichlet $L$-functions of conductor $q \ge 3$.
Both character parities are included; no explicit $c$ is given.

The scope note states the formalization's reach: "The quasi-Riemann hypothesis asks for a fixed zero-free half-plane $\Re s>\theta$ with $\theta<1$. The formalization gives $\theta=7/8$ for the Riemann zeta function and every Dirichlet $L$-function, uniformly over all positive moduli and all characters. It also establishes the same bound for finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$. [S5:10]" The
formalization covers $\theta = 7/8$ for zeta, all Dirichlet
$L$-functions, and finite-order Hecke $L$-functions over
$\mathbb{Q}(\sqrt{-3})$, plus the uniform real-zero gap.

## history of the conjecture

Prior (my training data, not this repo): the quasi-Riemann
hypothesis — existence of a fixed zero-free half-plane
$\Re s > \theta < 1$ for $\zeta$ — was implicit in the work of de la
Vallee Poussin (1896), who proved zero-freeness on $\Re s = 1$.
Vinogradov (1958) and Korobov (1958) obtained the first explicit
$\theta$-type bounds, excluding zeros in $\Re s > 1 - c/(\log t)^{2/3}
(\log\log t)^{1/3}$, a region that shrinks with height $t$. The
quasi-RH is the assertion that some *fixed* $\theta < 1$ works
uniformly in $t$, which no published zero-free region or zero-density
estimate reaches.

The 11/12 companion [S3:81] positions itself explicitly as a
"simpler" intermediate step toward the 7/8 headline, and both papers
decline to feed the published zero-density ladder as input. RH
remains open.

## Consequences

**A fixed zero-free half-plane for Dirichlet and Hecke
$L$-functions.** The 7/8 bound is conductor- and height-independent.
No prior published zero-free region achieves a fixed $\theta < 1$
uniformly over all moduli.

**Quantitative PNT in arithmetic progressions.** The companion's
corollary [S3:84–95] gives
$\sup_{q \le x} |\pi(x;q,a) - \text{li}(x)/\varphi(q)| \ll
x^{11/12}\log x$ with an absolute effective constant.

**Uniform Landau–Siegel exclusion.** The logarithmic gap
$(1-\beta)\log q \ge c$ rules out zeros in
$1 - c/\log q < \beta < 1$ uniformly over all primitive nonprincipal
real Dirichlet characters of conductor $q \ge 3$.

**Least quadratic nonresidues.** The companion draws corollaries
bounding the least quadratic nonresidue modulo an odd prime $p$ by a
fixed power of $\log p$, and the least prime in an arithmetic
progression by $\log^{A} q$ for a fixed $A$ [S3:97–100].

## section skeleton

Three single-file manuscripts, no `build/sections/` directories, no
`.bib` files (all three use inline `thebibliography`).

**Headline** [S2], `paper.tex`: Introduction (line 48) with Prior
work (127) and Organization (168); Notation (184); Outline of the
argument (206) with five steps (reduction to power-saving estimates,
embedding, Poisson summation, relation, cube removal); Poisson
summation and the dual mean square (773) with subsubsections through
the transfer estimate; Proof of the completed mean-square estimate
(1632); Proof of the transfer proposition (2217).

**Companion** [S3], `paper2.tex`: Introduction (line 52) with Prior
work (127) and Organization (168); Notation (184); Outline of the
argument (206) with five steps; From the mean-square estimate to the
zero-free region (660); Poisson summation and the dual mean square
(773); Proof of the completed mean-square estimate (1632); Proof of
the transfer proposition (2217).

**Landau–Siegel** [S4:41–46], `paper.tex`: Introduction (line 49); The
argument (95); Interpolation and arithmetic context (140); The prime
bias forced by a real zero (172).

## Comparison with the formalized statement

The scope note [S5:10] covers all three manuscripts (2 of 3
formalized in the ledger: `paps_form 2`). The formalization achieves
$\theta = 7/8$ for zeta, Dirichlet, and Hecke $L$-functions, plus the
uniform real-zero gap.

Four comparator challenges [S5:20–24]:

| Result | Comparator |
|--------|-----------|
| Riemann zeta 7/8 bound | [S6] |
| Dirichlet $L$-function 7/8 bound | `DirichletSevenEighths.lean` |
| Finite-order Hecke 7/8 bound | `HeckeSevenEighths.lean` |
| Uniform real-zero gap | [S7] |

The scope note [S5:14] notes the Landau–Siegel formalization: "Both
character parities are included. No explicit value of $c$ is given.
This excludes real zeros in $1-c/\log q < \beta < 1$, but does not
rule out real zeros elsewhere in $(0,1)$."

The scope note [S5:12] states the exclusion of later applications:
"The paper's later applications are not included."

## Coverage

T3: three manuscripts, two formalized, four comparator challenges,
four `main_results` entries, one scope note. The ledger reads `paps
3`, `paps_form 2`, `mainres 4`, `chal 4`, `scope_note 1`,
`verification 0`, `trace` empty, `companions 1`, `companion_word 2`.
The `companions 1` flags the October-5 paper as a companion to the
September-30 headline; the `companion_word 2` fires on both papers
that use the word "companion" in their abstracts. The catalog entry
[S8:82] names all three PDFs [S9] [S10] [S11]. No `verification/`
bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 003 at line 66) |
| S2 | [`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) | 16677 | Headline manuscript: 7/8 zero-free half-plane |
| S3 | [`preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) | 3988 | Companion manuscript: 11/12 zero-free half-plane |
| S4 | [`preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex`](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex) | 773 | Landau–Siegel uniform exclusion |
| S5 | [`lean/docs/003.md`](../../../lean/docs/003.md) | 25 | Scope note |
| S6 | [`lean/ComparatorChallenges/QuasiRiemannHypothesis.lean`](../../../lean/ComparatorChallenges/QuasiRiemannHypothesis.lean) | 9 | Challenge stub: zeta 7/8 bound |
| S7 | [`lean/ComparatorChallenges/SiegelZeros.lean`](../../../lean/ComparatorChallenges/SiegelZeros.lean) | 30 | Challenge stub: uniform real-zero gap |
| S8 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 003 at line 82) |
| S9 | [`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf`](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) | 45960 | Compiled headline manuscript |
| S10 | [`preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) | 22322 | Compiled companion manuscript |
| S11 | [`preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf`](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) | 11299 | Compiled Landau–Siegel manuscript |

## Bibliography

- M. Agrawal, N. Kayal, and N. Saxena, PRIMES is in P, _Ann. of Math._ (2) **160** (2004), no. 2, 781–793.
- S. Baier and A. Bansal, _The large sieve with power moduli for $\mathbb Z[i]$_, International Journal of Number Theory **14** (2018), no. 10, 2737–2756. doi:10.1142/S1793042118501658; arXiv:1802.08964.
- K. Benli, S. Goel, H. Twiss, and A. Zaman, _Explicit Deuring–Heilbronn phenomenon for Dirichlet $L$-functions_, Proc. Amer. Math. Soc. **154** (2026), no. 2, 509–525. doi:10.1090/proc/17450.
- V. Bhargava, G. Ivanyos, R. Mittal, and N. Saxena, _Irreducibility and deterministic $r$-th root finding over finite fields_, Proceedings of the 2017 ACM International Symposium on Symbolic and Algebraic Computation (ISSAC 2017), ACM, 2017, 37–44. doi:10.1145/3087604.3087620; author manuscript.
- V. Bhargava, G. Ivanyos, R. Mittal, and N. Saxena, Irreducibility and deterministic $r$-th root finding over finite fields, in _Proceedings of ISSAC 2017_, ACM, 2017, 37–44.
- K. Billington, M. Cheng, J. Schettler, and A. I. Suriajaya, _The average number of Goldbach representations and zero-free regions of the Riemann zeta-function_, International Journal of Number Theory **21** (2025), no. 2, 289–316. doi:10.1142/S1793042125500150; arXiv:2306.09102.
- V. Blomer, L. Goldmakher, and B. Louvel, _$L$-functions with $n$-th-order twists_, International Mathematics Research Notices **2014** (2014), no. 7, 1925–1955. doi:10.1093/imrn/rns257; arXiv:1112.1650.
- V. Blomer, L. Goldmakher, and B. Louvel, $L$-functions with $n$-th-order twists, _Int. Math. Res. Not._ (2014), no. 7, 1925–1955. doi:10.1093/imrn/rns257.
- J.-B. Bost, _Algebraic leaves of algebraic foliations over number fields_, Publ. Math. Inst. Hautes Études Sci. **93** (2001), 161–221. doi:10.1007/s10240-001-8191-3.
- H. Davenport, _Multiplicative Number Theory_, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics **74**, Springer, New York, 2000.
- H. Davenport, _Multiplicative number theory_, 2nd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics, vol. 74, Springer-Verlag, New York, 1980.
- C. David, A. de Faveri, A. Dunn, and J. Stucky, _Non-vanishing for cubic Hecke $L$-functions_, preprint, arXiv:2410.03048v2 (2026). arXiv:2410.03048.
- P. G. L. Dirichlet, _Beweis des Satzes, daß{} jede unbegrenzte arithmetische Progression, deren erstes Glied und Differenz ganze Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele Primzahlen enthält_, Abhandlungen der Königlichen Preussischen Akademie der Wissenschaften zu Berlin (1837), 45–81. English translation by R. Stephan, arXiv:0808.1408.
- A.-S. Elsenhans, J. Klüners, and F. Nicolae, Imaginary quadratic number fields with class groups of small exponent, _Acta Arith._ **193** (2020), no. 3, 217–233.
- S. Fischler, _Interpolation on algebraic groups_, Compos. Math. **141** (2005), no. 4, 907–925. doi:10.1112/S0010437X05001351.
- K. Ford, Zero-free regions for the Riemann zeta function, in _Number Theory for the Millennium, II_ (Urbana, IL, 2000), A K Peters, Natick, MA, 2002, 25–56. Corrected version: arXiv:1910.08205.
- E. Frenkel, R. Langlands, and B. C. Ng\^o, Formule des traces et fonctorialité: le début d'un programme, _Ann. Sci. Math. Québec_ **34** (2010), no. 2, 199–243. arXiv:1003.4578.
- { NIST Digital Library of Mathematical Functions, \S10.43, equation (10.43.19). https://dlmf.nist.gov/10.43.E19. }
- S. D. Galbraith, _Mathematics of Public Key Cryptography_, Cambridge University Press, 2012. doi:10.1017/CBO9781139012843. Section and algorithm references use the author's extended and corrected version 2.0, Chapter 2.
- S. D. Galbraith, _Mathematics of Public Key Cryptography_, Cambridge University Press, 2012.
- J. B. Friedlander and D. A. Goldston, _Sums of three or more primes_, Transactions of the American Mathematical Society **349** (1997), no. 1, 287–310. doi:10.1090/S0002-9947-97-01652-8.
- S. Bettin and S. M. Gonek, The $\theta=\infty$ conjecture implies the Riemann hypothesis, _Mathematika_ **63** (2017), no. 1, 29–33. doi:10.1112/S0025579316000139.
- F. Grube, Ueber einige Euler'sche Sätze aus der Theorie der quadratischen Formen, _Z. Math. Phys._ **19** (1874), 492–519.
- T. H. Grönwall, Sur les séries de Dirichlet correspondant \`a des caract\`eres complexes, _Rend. Circ. Mat. Palermo_ **35** (1913), 145–159. doi:10.1007/BF03015596.
- J. Hadamard, _Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques_, Bulletin de la Société Mathématique de France **24** (1896), 199–220. doi:10.24033/bsmf.545.
- J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques, _Bull. Soc. Math. France_ **24** (1896), 199–220. doi:10.24033/bsmf.545.
- H. Hasse, _Vorlesungen über Zahlentheorie_, Grundlehren der mathematischen Wissenschaften **59**, Springer, Berlin, 1950. doi:10.1007/978-3-642-52795-1.
- D. R. Heath-Brown, _A mean value estimate for real character sums_, Acta Arithmetica **72** (1995), no. 3, 235–275. doi:10.4064/aa-72-3-235-275.
- D. R. Heath-Brown, _Kummer's conjecture for cubic Gauss sums_, Israel Journal of Mathematics **120**, part A (2000), 97–124. doi:10.1007/s11856-000-1273-y.
- D. R. Heath-Brown, A mean value estimate for real character sums, _Acta Arith._ **72** (1995), no. 3, 235–275.
- D. R. Heath-Brown, Kummer's conjecture for cubic Gauss sums, _Israel J. Math._ **120** (2000), 97–124. doi:10.1007/s11856-000-1273-y.
- D. R. Heath-Brown, _Zero-free regions for Dirichlet $L$-functions, and the least prime in an arithmetic progression_, Proc. London Math. Soc. (3) **64** (1992), no. 2, 265–338. doi:10.1112/plms/s3-64.2.265.
- E. Hecke, _Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen. Erste Mitteilung_, Mathematische Zeitschrift **1** (1918), 357–376; _Zweite Mitteilung_, Mathematische Zeitschrift **6** (1920), 11–51. doi:10.1007/BF01465095 (first paper).
- E. Hecke, Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen, I, II, _Math. Z._ **1** (1918), 357–376; **6** (1920), 11–51.
- M. N. Huxley, _The large sieve inequality for algebraic number fields_, Mathematika **15** (1968), no. 2, 178–187. doi:10.1112/S0025579300002540.
- Clay Mathematics Institute, _Riemann Hypothesis_, Millennium Prize Problems, .
- J. B. Friedlander and H. Iwaniec, _A note on Dirichlet $L$-functions_, Expo. Math. **36** (2018), nos. 3–4, 343–350. doi:10.1016/j.exmath.2018.06.003.
- E. Kani, Idoneal numbers and some generalizations, _Ann. Sci. Math. Québec_ **35** (2011), no. 2, 197–227.
- N. M. Korobov, Estimates of trigonometric sums and their applications, _Uspekhi Mat. Nauk_ **13** (1958), no. 4(82), 185–192 (Russian). Math-Net.Ru: rm7458.
- H. Iwaniec and E. Kowalski, _Analytic Number Theory_, American Mathematical Society Colloquium Publications **53**, American Mathematical Society, Providence, RI, 2004. doi:10.1090/coll/053.
- E. Kowalski, Y. Lin, Ph. Michel, and W. Sawin, Periodic twists of $\mathrm{GL}_3$-automorphic forms, _Forum Math. Sigma_ **8** (2020), e15. doi:10.1017/fms.2020.7. Author version.
- T. Kubota, _On automorphic functions and the reciprocity law in a number field_, Lectures in Mathematics, Department of Mathematics, Kyoto University, no. 2, Kinokuniya Book-Store, Tokyo, 1969. .
- T. Kubota, _On automorphic functions and the reciprocity law in a number field_, Lectures in Mathematics, Department of Mathematics, Kyoto University, No. 2, Kinokuniya Book-Store, Tokyo, 1969. Kyoto University repository.
- E. Landau, Neuer Beweis des Primzahlsatzes und Beweis des Primidealsatzes, _Math. Ann._ **56** (1903), 645–670. doi:10.1007/BF01444310.
- M. Laurent, _Sur quelques résultats récents de transcendance_, Astérisque **198–199–200** (1991), 209–230. .
- U. V. Linnik, _On the least prime in an arithmetic progression. II. The Deuring–Heilbronn phenomenon_, Rec. Math. [Mat. Sbornik] N.S. **15(57)** (1944), no. 3, 347–368. .
- J. E. Littlewood, Quelques conséquences de l'hypoth\`ese que la fonction $\zeta(s)$ de Riemann n'a pas de zéros dans le demi-plan $\mathrm{R}(s)>1/2$, _C. R. Acad. Sci. Paris_ **154** (1912), 263–266.
- J. E. Littlewood, On the class-number of the corpus $P(\sqrt{-k})$, _Proc. London Math. Soc._ (2) **27** (1928), no. 1, 358–372.
- L. Goldmakher and B. Louvel, _A quadratic large sieve inequality over number fields_, Mathematical Proceedings of the Cambridge Philosophical Society **154** (2013), no. 2, 193–212. doi:10.1017/S0305004112000370; arXiv:1112.1642.
- L. Goldmakher and B. Louvel, A quadratic large sieve inequality over number fields, _Math. Proc. Cambridge Philos. Soc._ **154** (2013), no. 2, 193–212. doi:10.1017/S0305004112000370.
- R. F. Lu, A. Zaman, and H. Zhao, Numerical computations concerning Landau–Siegel zeros, preprint, 2026. arXiv:2602.03626.
- L. Guth and J. Maynard, _New large value estimates for Dirichlet polynomials_, Annals of Mathematics **203** (2026), no. 2, 623–675. doi:10.4007/annals.2026.203.2.6; arXiv:2405.20552.
- G. L. Miller, Riemann's hypothesis and tests for primality, _J. Comput. System Sci._ **13** (1976), no. 3, 300–317.
- J. S. Milne, _Class Field Theory_, course notes, version 4.03, 6 August 2020. .
- H. Maier and H. L. Montgomery, The sum of the Möbius function, _Bull. London Math. Soc._ **41** (2009), no. 2, 213–226. doi:10.1112/blms/bdn119.
- OpenAI, _An unconditional first moment for cubic Gauss sums_, OpenAI Math Release preprint OAI:An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026, 2026.
- OpenAI, The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\mathrm{Re}(s)>7/8$, OpenAI Math Release preprint OAI:The-Quasi-Riemann-Hypothesis-September-30-2026, 2026.
- A. Page, On the number of primes in an arithmetic progression, _Proc. London Math. Soc._ (2) **39** (1935), 116–141. doi:10.1112/plms/s2-39.1.116.
- A. Page, _On the number of primes in an arithmetic progression_, Proc. London Math. Soc. (2) **39** (1935), 116–141. doi:10.1112/plms/s2-39.1.116.
- S. J. Patterson, _A cubic analogue of the theta series_, Journal für die reine und angewandte Mathematik **296** (1977), 125–161. doi:10.1515/crll.1977.296.125.
- D. R. Heath-Brown and S. J. Patterson, The distribution of Kummer sums at prime arguments, _J. Reine Angew. Math._ **310** (1979), 111–130. doi:10.1515/crll.1979.310.111.
- S. J. Patterson, A cubic analogue of the theta series, _J. Reine Angew. Math._ **296** (1977), 125–161. doi:10.1515/crll.1977.296.125.
- P. Philippon, _Lemmes de zéros dans les groupes algébriques commutatifs_, Bull. Soc. Math. France **114** (1986), 355–383; errata et addenda, **115** (1987), 397–398. doi:10.24033/bsmf.2060; doi:10.24033/bsmf.2084.
- C.-J. de la Vallée Poussin, _Recherches analytiques sur la théorie des nombres premiers. Premi\`ere partie: La fonction $\zeta(s)$ de Riemann et les nombres premiers en général_, Annales de la Société scientifique de Bruxelles **20**, deuxi\`eme partie (1896), 183–256. Reprinted in _Recherches analytiques sur la théorie des nombres premiers_, Hayez, Brussels, 1897, .
- C.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers. Premi\`ere partie: La fonction $\zeta(s)$ de Riemann et les nombres premiers en général, _Ann. Soc. Sci. Bruxelles_, deuxi\`eme partie, **20** (1896), 183–256.
- C.-J. de la Vallée Poussin, Sur la fonction $\zeta(s)$ de Riemann et le nombre des nombres premiers inférieurs \`a une limite donnée, _Mém. Couronnés Autres Mém. Acad. Roy. Sci. Lettres Beaux-Arts Belgique_, collection in-$8^\circ$, **59** (1899), 1–74. doi:10.3406/marb.1899.2449.
- J. Maynard and K. Pratt, _Half-isolated zeros and zero-density estimates_, International Mathematics Research Notices **2024** (2024), no. 19, 12978–13014. doi:10.1093/imrn/rnae191; arXiv:2206.11729.
- A. Dunn and M. Radziwiłł, _Bias in cubic Gauss sums: Patterson's conjecture_, Annals of Mathematics **200** (2024), no. 3, 967–1057. doi:10.4007/annals.2024.200.3.3; arXiv:2109.07463.
- A. Dunn and M. Radziwiłł, Bias in cubic Gauss sums: Patterson's conjecture, _Ann. of Math._ (2) **200** (2024), no. 3, 967–1057. doi:10.4007/annals.2024.200.3.3.
- B. Riemann, _Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse_, Monatsberichte der Königlichen Preussischen Akademie der Wissenschaften zu Berlin (1859), 671–680. Manuscript, transcription, and translation at .
- B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, _Monatsber. Königl. Preuss. Akad. Wiss. Berlin_ (1859), 671–680. Original text and English translation.
- G. Bhowmik and I. Z. Ruzsa, Average Goldbach and the quasi-Riemann hypothesis, _Anal. Math._ **44** (2018), no. 1, 51–56.
- M. Ram Murty and A. Sankaranarayanan, Averages of exponential twists of the Liouville function, _Forum Math._ **14** (2002), no. 2, 273–291.
- C. L. Siegel, Über die Classenzahl quadratischer Zahlkörper, _Acta Arith._ **1** (1935), 83–86. doi:10.4064/aa-1-1-83-86.
- C. L. Siegel, _Über die Classenzahl quadratischer Zahlkörper_, Acta Arith. **1** (1935), 83–86. doi:10.4064/aa-1-1-83-86.
- T. Tao, _The Elliott–Halberstam conjecture implies the Vinogradov least quadratic nonresidue conjecture_, Algebra & Number Theory **9** (2015), no. 4, 1005–1034. doi:10.2140/ant.2015.9.1005; publisher PDF.
- { T. Tatuzawa, On a theorem of Siegel, _Japan. J. Math._ **21** (1951), 163–178. doi:10.4099/jjm1924.21.0\_163. }
- E. C. Titchmarsh, A divisor problem, _Rend. Circ. Mat. Palermo_ **54** (1930), 414–429; correction, **57** (1933), 478–479. doi:10.1007/BF03021203; correction.
- K. A. Rodosski\uı, On non-residues and zeros of $L$-functions, _Izv. Akad. Nauk SSSR Ser. Mat._ **20** (1956), no. 3, 303–306 (Russian).
- H. L. Montgomery and R. C. Vaughan, _Multiplicative Number Theory I: Classical Theory_, Cambridge Studies in Advanced Mathematics **97**, Cambridge University Press, 2007.
- I. M. Vinogradov, A new estimate of the function $\zeta(1+it)$, _Izv. Akad. Nauk SSSR Ser. Mat._ **22** (1958), no. 2, 161–164 (Russian). Math-Net.Ru: im3962.
- I. M. Vinogradov, _Selected Works_, edited by L. D. Faddeev et al., Springer, Berlin, 1985.
- P. J. Weinberger, Exponents of the class groups of complex quadratic fields, _Acta Arith._ **22** (1973), 117–124. doi:10.4064/aa-22-2-117-124.
- A. Yoshimoto, On the cubic theta function, _Nagoya Math. J._ **105** (1987), 153–167.
- I. Petrow and M. P. Young, A generalized cubic moment and the Petersson formula for newforms, _Math. Ann._ **373** (2019), nos. 1–2, 287–353.
- I. Petrow and M. P. Young, The Weyl bound for Dirichlet $L$-functions of cube-free conductor, _Ann. of Math._ (2) **192** (2020), no. 2, 437–486. doi:10.4007/annals.2020.192.2.3.
- J. Thorner and A. Zaman, _A unified and improved Chebotarev density theorem_, Algebra & Number Theory **13** (2019), no. 5, 1039–1068. doi:10.2140/ant.2019.13.1039; arXiv:1803.02823.
- P. Gao and L. Zhao, _Moments of quadratic Hecke $L$-functions of imaginary quadratic number fields_, Journal of Number Theory **209** (2020), 359–377. doi:10.1016/j.jnt.2019.09.002; arXiv:1707.00091.
- P. Gao and L. Zhao, _Moments and one level density of sextic Hecke $L$-functions_, Functiones et Approximatio Commentarii Mathematici **70** (2024), no. 1, 7–28. doi:10.7169/facm/2057; arXiv:2201.01885.
- P. Gao and L. Zhao, Mean squares of quadratic twists of the Möbius function, _J. Number Theory_ **247** (2023), 1–14. doi:10.1016/j.jnt.2022.12.007.

[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 037](../../index/algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md)

# 037 — The sharp ordinary-double-point volume gap

[Index page](../../index/algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md)

## Original CONTENTS.md summary

The release's blurb [S1:1060]: "**037. The ordinary-double-point volume gap.** Proves the ordinary-double-point volume-gap conjecture: every singular complex algebraic klt germ of dimension $n$ ≥ 2, with zero boundary, has normalized volume at most $2(n-1)^n$. Equality holds precisely for an analytic ordinary double point." The two manuscripts
are "The ordinary-double-point gap in every dimension" [S3:1] and the fourfold companion [S6:1].

## Undergraduate summary

Normalized volume measures the size of a klt singularity: for an
$n$-dimensional klt germ $(X,x)$ with zero boundary,
$\nvol(x,X)=\inf_v A_X(v)^n \vol(v)$, where the infimum runs over
centered valuations [S5:3–24]. "Normalized volume, introduced by Chi Li  , measures the" The largest value is $n^n$,
attained exactly at smooth points. The ordinary double point gap
conjecture predicts the next largest: $2(n-1)^n$, characterizing the
ordinary double point. The theorem [S5:33–46]:

> **theorem**


The point need not be isolated in the singular locus, and no
structural assumption is implicit [S5:48–53].

## Graduate summary

**The induction.** The proof uses the fourfold theorem of the
companion as its sole external input [S5:55–62]. The companion
proves $\nvol\le162$ in dimension four [S7:74–83]:

> **theorem**


The induction from $n=4$ to all $n\ge5$ proceeds by cone
reduction, small-stabilizer analysis, jet interiority, adjoint
semigroup construction, filtration comparison, and a bootstrap
argument [S8]–[S14]. The key principle: after stable degeneration
to a K-semistable cone, a sufficiently large volume forces
algebraic structure (Gorenstein, canonical) that is absent from
the hypotheses [S5:84–98].

**The global application.** Combining the local gap with
Li–Miao's smooth classification gives global volume bounds for
K-semistable $\mathbb{Q}$-Fano varieties [S5:64–75]:

> **corollary**


The singular bound $2((n^2-1)/n)^n$ is strictly below $2n^n$,
improving the smooth classification for singular Fano varieties.

## History of the conjecture

The gap conjecture arose from singular Kähler–Einstein limits,
where volume density measures the size of a metric tangent cone.
Donaldson–Sun established algebraicity and uniqueness of these
cones; Spotti–Sun formulated the conjecture and observed that
density above $1/2$ forces Gorenstein canonical structure [S5:84–98].
"The gap conjecture arose from the study of singular noncollapsed"

The low-dimensional cases precede the present work: Li–Liu for
surfaces, Liu–Xu for threefolds, Liu for local complete
intersections in all dimensions, and Moragá–Süss for toric
germs [S5:100–116]. "The unrestricted low-dimensional cases precede the present induction." The fourfold companion supplies the
remaining base case.

The cone reduction to K-semistable cones uses the variational
theory of normalized volume: Martelli–Sparks–Yau, Li–Liu,
Li–Xu, Blum, Xu, Xu–Zhuang, and Li–Wang–Xu [S5:136–151].
"The passage from metric cones to arbitrary klt singularities rests"

## Consequences

**The full ODP gap conjecture.** Every singular klt germ of
dimension $n\ge2$ with zero boundary has normalized volume at
most $2(n-1)^n$, with equality precisely for the ordinary double
point [S5:33–46]. This resolves the Spotti–Sun conjecture in all
dimensions simultaneously.

**Sharp global Fano bounds.** The local gap gives a strict
improvement of the volume bound for singular K-semistable
$\mathbb{Q}$-Fano varieties, reducing the equality case at
$2n^n$ to the smooth classification of Li–Miao [S5:64–75].

## Section skeleton

**Main manuscript** (8 sections under `build/sections/`):

1. Introduction [S5]
2. Cone reduction and the base case [S8]
3. Small-stabilizer structure [S9]
4. Jet interiority [S10]
5. Adjoint semigroup construction [S11]
6. Filtrations [S12]
7. Bootstrap argument [S13]
8. Conclusion [S14]

Main file: `paper.tex` [S4].

**Companion manuscript** (single file `paper.tex` [S7]):
the fourfold theorem and its proof.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The main manuscript
ships 9 `.tex` files under `build/`; the companion ships 1.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 037 at line 1060. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 152. |
| S3 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/README.md`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/README.md) | 18 | Main manuscript readme: title, author, date. |
| S4 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/paper.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/paper.tex) | 32 | Main manuscript main file. |
| S5 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/01-introduction.tex) | 291 | The main theorem, the global corollary, the historical context, and the proof strategy. |
| S6 | [`preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/README.md`](../../../preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/README.md) | 17 | Companion manuscript readme: title, author, date. |
| S7 | [`preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/build/paper.tex`](../../../preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/build/paper.tex) | 963 | Companion manuscript: the fourfold theorem and its proof. |
| S8 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/02-cone-reduction.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/02-cone-reduction.tex) | 501 | Cone reduction and the base case. |
| S9 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/03-small-stabilizers.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/03-small-stabilizers.tex) | 515 | Small-stabilizer structure. |
| S10 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/04-jet-interiority.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/04-jet-interiority.tex) | 798 | Jet interiority. |
| S11 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/05-adjoint-semigroup.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/05-adjoint-semigroup.tex) | 557 | Adjoint semigroup construction. |
| S12 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/06-filtrations.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/06-filtrations.tex) | 578 | Filtrations. |
| S13 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/07-bootstrap.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/07-bootstrap.tex) | 678 | Bootstrap argument. |
| S14 | [`preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/08-conclusion.tex`](../../../preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/08-conclusion.tex) | 203 | Conclusion. |

## Bibliography

- The Stacks Project Authors, _The Stacks Project_. Section 48.14 (Tag 0B4A), Lemma 31.13.12 (Tag 0EBJ), and regular local rings are UFDs (Tag 0AG0).
- Harold Blum, _Existence of valuations with smallest normalized volume_, Compositio Mathematica **154** (2018), no. 4, 820–849. doi:10.1112/S0010437X17008016. arXiv:1606.08894v3.
- Anita Buckley, Miles Reid, and Shengtian Zhou, _Ice cream and orbifold Riemann–Roch_, Izvestiya: Mathematics **77** (2013), no. 3, 461–486. doi:10.1070/IM2013v077n03ABEH002644. arXiv:1208.0457v1.
- Henry Cohn and Noam Elkies, _New upper bounds on sphere packings I_, Annals of Mathematics (2) **157** (2003), no. 2, 689–714. doi:10.4007/annals.2003.157.689. arXiv:math/0110009.
- Osamu Fujino and Yoshinori Gongyo, _On canonical bundle formulas and subadjunctions_, Michigan Mathematical Journal **61** (2012), no. 2, 255–264. doi:10.1307/mmj/1339011526. arXiv:1009.3996v1. Affine Theorem 7.2 is cited from the author preprint, internal version 1.17, 12 September 2010.
- Tommaso de Fernex and Christopher D. Hacon, _Singularities on normal varieties_, Compositio Mathematica **145** (2009), no. 2, 393–414. doi:10.1112/S0010437X09003996. arXiv:0805.1767v2.
- János Kollár, _Resolution of Singularities—Seattle Lecture_, Preprint (2007). arXiv:math/0508332v3. Theorems 26–27 are cited with this preprint's numbering.
- János Kollár, _Canonical models_, author-hosted draft chapter, 1 June 2010. Section 4, written in collaboration with Sándor J. Kovács, contains the cited Theorem 120. Author chapter.
- Chi Li, _Minimizing normalized volumes of valuations_, Mathematische Zeitschrift **289** (2018), no. 1–2, 491–513. doi:10.1007/s00209-017-1963-3. arXiv:1511.08164v4.
- Chi Li and Yuchen Liu, _Kähler–Einstein metrics and volume minimization_, Advances in Mathematics **341** (2019), 440–492. doi:10.1016/j.aim.2018.10.038.
- Yuchen Liu, _K-stability of cubic fourfolds_, Journal für die reine und angewandte Mathematik **786** (2022), 55–77. doi:10.1515/crelle-2022-0002. arXiv:2007.14320v2.
- Yuchen Liu, _Optimal bounds for local volumes of threefold singularities_, Preprint (2025; revised 2026). arXiv:2512.05429v2.
- Dario Martelli, James Sparks, and Shing-Tung Yau, _Sasaki–Einstein manifolds and volume minimisation_, Communications in Mathematical Physics **280** (2008), 611–673. doi:10.1007/s00220-008-0479-4. arXiv:hep-th/0603021v5.
- Chi Li and Minghao Miao, _On the volume of K-semistable Fano manifolds_, Preprint (2025; revised 2026). arXiv:2506.17420v3.
- Miles Reid, _Minimal models of canonical 3-folds_, in _Algebraic Varieties and Analytic Varieties (Tokyo, 1981)_, Shigeru Iitaka (ed.), Advanced Studies in Pure Mathematics 1, Kinokuniya, Tokyo, and North-Holland, Amsterdam, 1983, 131–180. Original paper scan.
- Joaquín Moraga and Hendrik Sü\ss{}, _Bounding toric singularities with normalized volume_, Bulletin of the London Mathematical Society **56** (2024), no. 6, 2212–2229. doi:10.1112/blms.13052.
- Richard P. Stanley, _Hilbert functions of graded algebras_, Advances in Mathematics **28** (1978), no. 1, 57–83. doi:10.1016/0001-8708(78)90045-2. Author copy.
- Cristiano Spotti and Song Sun, _Explicit Gromov–Hausdorff compactifications of moduli spaces of Kähler–Einstein Fano manifolds_, Pure and Applied Mathematics Quarterly **13** (2017), no. 3, 477–515. doi:10.4310/PAMQ.2017.v13.n3.a5. arXiv:1705.00377v1.
- Chi Li and Chenyang Xu, _Stability of valuations: higher rational rank_, Peking Mathematical Journal **1** (2018), no. 1, 1–79. doi:10.1007/s42543-018-0001-7. arXiv:1707.05561v2.
- Yuchen Liu and Chenyang Xu, _K-stability of cubic threefolds_, Duke Mathematical Journal **168** (2019), no. 11, 2029–2073. doi:10.1215/00127094-2019-0006. arXiv:1706.01933v3.
- Chenyang Xu, _A minimizing valuation is quasi-monomial_, Annals of Mathematics **191** (2020), no. 3, 1003–1030. doi:10.4007/annals.2020.191.3.6. arXiv:1907.01114.
- Chi Li and Zhengyi Zhou, _Minimal log discrepancy and orbifold curves_, Journal of Mathematical Study **59** (2026), no. 1, 1–15. doi:10.4208/jms.v59n1.26.01. arXiv:2502.11847v1.
- Chenyang Xu and Ziquan Zhuang, _Uniqueness of the minimizer of the normalized volume function_, Cambridge Journal of Mathematics **9** (2021), no. 1, 149–176. doi:10.4310/CJM.2021.v9.n1.a2. arXiv:2005.08303v1.
- Chenyang Xu and Ziquan Zhuang, _Stable degenerations of singularities_, Journal of the American Mathematical Society **38** (2025), no. 3, 585–626. doi:10.1090/jams/1055. arXiv:2205.10915v2.
- Chenyang Xu and Ziquan Zhuang, _Open problems in K-stability of Fano varieties_, Preprint (2026). arXiv:2601.15576v2.

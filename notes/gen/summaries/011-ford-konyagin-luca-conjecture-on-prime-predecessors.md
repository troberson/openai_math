[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 011](../index/number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md)

# 011 — The Ford–Konyagin–Luca conjecture on prime predecessors

[Index page](../index/number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md)

## Original CONTENTS.md summary

The release's own entry for this family reads 

> **011. Prime-factor statistics of $`p-1`$.** Proves that the normalized ordered logarithms of the prime factors of $`p-1`$, counted with multiplicity, converge jointly to the Poisson–Dirichlet law $`\mathrm{PD}(1)`$ as *p* ranges uniformly over primes up to *x* and $`x\to\infty`$. This resolves the Ford–Konyagin–Luca conjecture. [S1:266]

The release describes three manuscripts. Manuscript A's blurb is the totient-fiber claim 

> We prove Erdős's conjecture on the largest fibers of Euler's totient function: [S1:275]

Manuscript B's blurb is the family headline 

> For a prime *p* chosen uniformly from $`3\le p\le x`$, list the prime factors of $`p-1`$ in decreasing order, with multiplicity. As $`x\to\infty`$, their logarithms, divided by $`\log(p-1)`$, converge in every finite joint distribution to the Poisson–Dirichlet distribution with parameter one. This proves the conjecture of Ford, Konyagin and Luca. [S1:284]

Manuscript C's blurb is the parity claim, which the family blurb does not mention 

> We prove that there are infinitely many primes *p* for which $`p-1`$ is squarefree and has an even number of prime factors. Equivalently, there are infinitely many primes *p* with $`\mu(p-1)=1`$. [S1:293]

The third manuscript is not named in the family blurb. Its theorem is a separate claim about the parity of the prime-factor count of $p-1$, and it is the manuscript with the earlier date — September 17, 2026, against September 24 for the other two [S3:5] [S9:5] [S15:5].

## Undergraduate summary

Euler's totient function $\varphi(m)$ counts the integers at most $m$ that are coprime to $m$, and asking how often a given value $n$ is hit is a question with a long history. Manuscript A settles its extreme end. Write $g(n)$ for the number of solutions of $\varphi(m)=n$; the theorem says that for every $\varepsilon>0$ there are infinitely many $n$ with $g(n)>n^{1-\varepsilon}$, and no larger exponent of $n$ is possible. The companion statement is about primes $p$ whose predecessor $p-1$ has only small prime factors, and the two are joined by a classical construction that turns many smooth predecessors into many products with the same totient.

Manuscript B asks a statistical question about the same predecessor. Break $p-1$ into primes, take the logarithms of those primes, and divide by $\log(p-1)$, so the pieces add up to one. The theorem says that as $p$ ranges uniformly over the primes, these normalized pieces behave exactly like the fragments of a stick broken by the Poisson–Dirichlet rule with parameter one. That is the conjecture Ford, Konyagin and Luca posed, and it is the family's headline.

Manuscript C asks which parity the number of prime factors of $p-1$ takes. It proves that infinitely many primes have a squarefree predecessor with an even number of prime factors, which is the parity class that sieve theory has historically had the least purchase on.

**The proof sketch runs in one direction, from smooth predecessors outward.** Manuscript A fixes a smoothness exponent, builds a dilation-graph transference together with an ideal-kernel weighted sieve, extracts many primes $p$ in $2x<p\le5x$ whose predecessor has no prime factor above $x^\delta$, and then forms products of many of those primes. Distinct products land on the same totient value, so one totient fiber is large; a pigeonhole count plus the elementary upper bound $g(n)\ll_\eta n^{1+\eta}$ turns a lower bound that grows with $X$ into the required infinitely many $n$. Manuscript B takes that graph machinery as a black box and adds the analytic work the full joint law needs: a marked Type II estimate in which only the predecessor side carries divisor marks, a two-sided version of it, an extraction that removes the marks, and a size-biased probability argument that turns interior factorial measures into densities of total mass one. Manuscript C takes the same machinery and proves the two extensions its parity weight needs.

## Graduate summary

Manuscript A proves two theorems, and the family's totient claim is the first of them [S5:10–16]:

> \begin{theorem}\label{thm:totient}
> For every real $\varepsilon>0$, there are infinitely many positive integers
> $n$ such that
> \[
>  g(n)>n^{1-\eps}.
> \]
> \end{theorem}

The theorem it is derived from is the smooth-predecessor count [S5:38–46]:

> \begin{theorem}\label{thm:smooth}
> For every fixed $0<\delta<1/4$, as $x\to\infty$,
> \begin{equation}\label{eq:main-smooth}
>  \#\{p:\ p\text{ prime},\ 2x<p\le5x,
>                    \ P^+(p-1)\le x^\delta\}
>  \ge x^{1-o(1)}.
> \end{equation}
> The quantity $o(1)$ may depend on $\delta$.
> \end{theorem}

The named resolution is stated by the manuscript itself: the conjecture is Pomerance's formulation with $C=1$, attributed to Erdős, and the upper bound makes the exponent sharp — "Thus the power exponent of $n$ in the theorem is optimal [S5:24–25]" . The smooth-predecessor corollary is claimed as a second resolution, "In particular, for every $\varepsilon>0$ there are infinitely many primes $p$ with $P^+(p-1)\le p^\varepsilon$. This resolves the smooth-predecessor conjecture positively as well [S5:48–50]" . The strength of the count is quoted against the fixed-exponent literature: "Our unconditional bound $x^{1-o(1)}$ gives the full power exponent of the count for every fixed positive smoothness exponent. A positive limiting proportion is a stronger conclusion [S5:78–80]" .

The moves in manuscript A are:

1. Transfer the weighted-sieve problem onto a dilation graph and prove the operator theorems, so that a lower bound for smooth predecessors comes out of a signed correlation estimate.
2. Prove the marked Type II estimate on the graph side, with the long factor slot occupied by a rough integer.
3. Extract primes from the resulting correlation, giving "In particular, for every $\varepsilon>0$ there are infinitely many primes $p$ with $P^+(p-1)\le p^\varepsilon$ [S5:48–49]" as a corollary of the dyadic count .
4. Pass from smooth predecessors to totient fibers by the classical product-and-pigeonhole argument: "We finish by deriving   from  . This product-and-pigeonhole passage is the classical connection between smooth shifted primes and large totient fibers; see \cite[Theorem B and its proof]Pomerance1980 [S6:3–6]" .
5. Close the infiniteness argument: "These lower bounds for $g(n)$ tend to infinity with $X$. By  , the resulting values $n$ cannot belong to a fixed finite set. They are therefore unbounded, which proves the required assertion for infinitely many $n$ [S6:84–87]" .

Manuscript B's headline is the joint limiting law [S11:30–41]:

> \begin{theorem}\label{thm:main}
> For every fixed $k\ge1$ and every bounded continuous function
> $F:[0,1]^k\to\mathbb{R}$,
> \begin{equation}\label{eq:main-law}
>  \lim_{x\to\infty}\frac1{\pi(x)-1}
>      \sum_{\substack{3\le p\le x\\p\text{ prime}}}
>        F\bigl(V_1(p),\ldots,V_k(p)\bigr)
>  =\E F(L_1,\ldots,L_k).
> \end{equation}
> The limit holds through all real $x$ and uses ordinary equal
> weighting of the primes.
> \end{theorem}

The named resolution is asserted in the same words: "Theorem   resolves positively the conjecture of Ford, Konyagin and Luca \cite[Section 6, Conjecture 5]FordKonyaginLuca2010. Their formulation uses the same multiplicity convention, normalization, and ordinary counting distribution on primes. The assertion includes all finite joint distributions, strengthening the largest-factor prediction alone [S11:43–48]" . The fixed-threshold form of the conjecture is resolved with it: "Theorem   resolves this fixed-$u$ conjecture positively and proves the complete joint limiting law [S11:87–88]" .

The moves in manuscript B are:

1. Prove the marked Type II estimate with marks on the predecessor side only: "The main new estimate is Theorem  : a marked Type II estimate in which only the predecessor side carries divisor marks, namely weights recording selected small prime divisors [S11:143–145]" . Cauchy's inequality after dividing out one tuple of marks produces a small-determinant relation between primitive lattice vectors, and an exact memory expansion charges each recurring prime once.
2. Pass to marks on both endpoints: "The second estimate, Theorem  , uses marks on both endpoints. We apply the general graph inputs of S to a centered long-prime divisor statistic and prove the required new endpoint Fourier estimates. A small mark restricts difficult frequencies to a sparse set; a long-prime polynomial controls the positive tuple term there, and a finite divisor model controls the constant term [S11:187–193]" .
3. Remove the marks: a first-moment presieve replaces composite slots by rough slots, marking groups bring the composite terms within the two-sided estimate, and averaging over disjoint fixed marking arrays yields interior factorial-moment asymptotics for ordinary prime dyads.
4. Convert moments into a law: "Finally, sequential size-biased sampling turns the interior factorial measures into probability densities of total mass one. This excludes escape to the boundary and yields the stick fragments in [S11:202–205]" [S11:202–209]. Section 8 is where that passage is carried out, and it is explicit about what it does not need: "We now pass from Theorem   to ordinary prime averages of every finite collection of ranked factors. The argument also shows why no additional assertion about very small factors or the boundary of a simplex is needed [S12:4–7]" , with the probability input named as "the size-biased viewpoint of Donnelly and Grimmett \cite[Section 2]DonnellyGrimmett and the factorial-measure characterization of Arratia, Kochman and Miller \cite[Lemma 2 and Section 3.3]ArratiaKochmanMiller2014 [S12:8–11]" [S12:8–12], on the setup "Choose a prime $p$ uniformly from $x<p\leq 2x$, and regard the prime factors of $p-1$, with their multiplicities, as distinct labelled balls [S12:16–17]" .

Manuscript C's theorem is the parity statement [S16:53–57]:

> \begin{theorem}\label{thm:main}
> There are infinitely many primes $p$ such that $p-1$ is squarefree
> and $\Omega(p-1)$ is even. In particular, there are infinitely many
> such primes under either convention for counting prime factors.
> \end{theorem}

Its claim is deliberately narrow, and the manuscript says so. Squarefreeness is what removes the $\Omega$/$\omega$ ambiguity: "The squarefreeness condition is useful rather than cosmetic: it removes the ambiguity between the two counting conventions. Writing $p=2u+1$, we will construct nonnegative weights on odd integers $u$ for which $\Omega(u)$ is odd. These weights have enough bilinear distribution to detect prime values of $2u+1$, and their nonsquarefree part is negligible at the scale of the detected prime mass [S16:59–64]" . The obstruction it is working against is stated as classical: "Prime-factor parity is a classical obstruction in sieve theory: congruence information alone need not distinguish the two Liouville signs [S16:67–69]" . Its dependence on manuscript A is declared, and the gap it must fill is named: "Our structural inputs are the dilation-graph transference, ideal-kernel, weighted-sieve, and proxy estimates of the companion paper _Weighted dilation graphs, smooth shifted primes and totient fibers_  , hereafter S. Their hypotheses and the conclusions needed here are stated where they enter the proof. We do not reprove those results [S16:78–83]" , and "S's shifted-correlation argument uses a rough integer in a designated long factor slot and unsigned marked weights. Neither smoothness of the predecessor nor that unsigned statement gives the parity conclusion of Theorem  . The new work is to permit a prime in the long slot and the same group-supported Liouville sign at both endpoints. We prove both extensions here [S16:85–90]" . The second extension is a cancellation: "Second, the sign of a shared dilation occurs twice in a lifted correlation and cancels by complete multiplicativity. This observation allows the graph reduction to retain a parity-sensitive weight [S16:100–102]" .

What this family does not say. Manuscript A asserts no uniformity in the smoothness exponent — "No uniformity as $\delta\to0$ is asserted in   or needed for [S5:52–53]" — and its $x^{1-o(1)}$ count is explicitly weaker than a positive limiting proportion, which the manuscript concedes . Manuscript B's law is a statement about every finite joint distribution of ranked factors under ordinary equal weighting; it does not claim a rate, and it does not assert the recursive independence assumptions that the prime-chain model needs beyond the root . Manuscript C proves existence of infinitely many parity-even squarefree predecessors; it does not claim a positive proportion, and it does not deduce its parity condition from smoothness . The family's three manuscripts are three separate claims, and the family blurb names only two of them.

Formalization status. The ledger records 3 manuscripts, 0 formalized, no scope note, no comparator challenge, no `main_results` config, no verification directory, and no reasoning trace, with claim shapes resolution and uniform and `resolves_named` set [S20:12]. Nothing about this family is machine-checked. Absence of formalization is not a red flag here: 560 of the release's 722 manuscripts are unformalized, and this family's evidence is its three manuscripts and nothing else.

## History of the conjecture

The two named conjectures are recorded by the manuscripts that resolve them. For the totient-fiber side, manuscript A gives the attribution and the form: "The final passage from plentiful smooth shifted primes to large totient fibers belongs to the method of Erdős and Pomerance; Pomerance states the relevant transfer explicitly in \cite[Theorem B]Pomerance1980. We give the needed product-and-pigeonhole proof in full [S5:81–85]" , after stating that Pomerance formulates the conjecture as $C=1$ and attributes it to Erdős [S5:18–22]. For the Poisson–Dirichlet side, manuscript B gives the setting the conjecture was posed in: "Ford, Konyagin and Luca formulated their conjecture in studying prime chains and Pratt trees. Theorem   supplies the factorization law at the root of their probabilistic model; the recursive independence assumptions used for later generations are additional hypotheses. Smooth predecessors also underlie the Carmichael-number construction of Alford, Granville and Pomerance  , together with a separate progression-distribution input [S11:121–128]" . Manuscript A records the same Carmichael connection from its own side: "Smooth predecessors also enter the construction of Carmichael numbers by Alford, Granville and Pomerance  , where their supply is combined with a separate distribution theorem for primes in arithmetic progressions. This is one reason that estimates for shifted smoothness have applications beyond the factorization problem itself. The contribution here includes the general graph and kernel theorems that produce the arithmetic lower bound, as well as the optimal exponent for totient fibers [S5:87–94]" .

The fixed-exponent history is the measure of what was known before. Manuscript A's introduction records Baker and Harman's exponent $0.2961$ for shifted primes with the corresponding totient multiplicity exponent $0.7039$, Friedlander's threshold $1/(2\sqrt e)+\varepsilon$, and the Elliott–Halberstam prediction with distribution level one half obtained unconditionally [S5:55–80]. Manuscript B records the Dickman-function form of the fixed-$u$ conjecture and the Granville threshold, together with the closest general distribution theorem, Bharadwaj and Rodgers' [S11:84–97]. The parity question is older than any of these: manuscript C calls it "a classical obstruction in sieve theory [S16:67]" and points to the Friedlander–Iwaniec asymptotic sieve as the illustration of what bilinear information buys .

Prior (my training data, not this repo). The Poisson–Dirichlet law PD(1) is the Kingman stick-breaking distribution, and the size-biased and factorial-measure tools manuscript B uses are the standard machinery for proving that a sequence of integer factorizations converges to it — the Donnelly–Grimmett and Arratia–Kochman–Miller results the manuscript cites are the two it needs. The Ford–Konyagin–Luca conjecture sat in their 2010 paper on prime chains, and the totient-fiber conjecture with $C=1$ is Pomerance's 1980 formulation of an Erdős problem; both were open in my training data, and the smooth-shifted-prime exponents manuscript A lists are the pre-existing record. Nothing in this paragraph comes from the repository.

## Consequences

The family's strongest structure is a mutual citation between two of its own manuscripts. Manuscript A declares its output as an input to manuscript B: "These graph and ideal-kernel estimates also serve as inputs to the companion paper \cite[Theorem 1.1]PrimePredecessors, where a separate determinant-graph estimate and prime-extraction argument yield the full Poisson–Dirichlet law for prime predecessors [S5:96–99]" , and its bibliography carries the release copy of that companion under the key `PrimePredecessors` with the title line "title = The Poisson–Dirichlet law for prime predecessors, [S7:230]" . Manuscript B cites back, naming manuscript A as S and using its operator theorems: "The companion article _Weighted dilation graphs, smooth shifted primes and totient fibers_ \cite[Theorem 1.2]SmoothShifted, denoted S, proves that, for every fixed positive smoothness exponent, there are $x^{1-o(1)}$ primes in its stated interval with smooth predecessors [S11:130–133]" , with the release copy under the key `SmoothShifted` and the title line "title = {Weighted dilation graphs, smooth shifted primes and totient fibers}, [S13:266]" . Manuscript C cites manuscript A one-directionally, in an inline bibliography rather than a `.bib` file: the entry is "_Weighted dilation graphs, smooth shifted primes and totient fibers_, [S17:27]" and it is cited as S in the passage quoted above . So the chain is A ↔ B and C → A, and every link is inside the family: the family's headline result rests on machinery its own first manuscript supplies, and its third manuscript rests on the same machinery.

What the family gives the rest of the release is a smooth-shifted-prime count with the full power exponent, an optimal totient-fiber exponent, the complete joint factorization law for prime predecessors, and a parity-existence theorem that extends the shared graph reduction to a parity-sensitive weight. The corpus contains no formalization in which any of these is used, so the downstream consequences are the ones the manuscripts themselves record. The triage record lists this family in the T0 opening [S19:125]. Related T0 number-theory pages: [002 — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one](002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md), [004 — Hilbert's tenth problem over ℚ](004-hilberts-tenth-problem-over-q.md), [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md), [010 — Fontaine–Mazur modularity at the prime 2](010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md), [018 — The Margulis–Platonov conjecture over global fields](018-margulis-platonov-conjecture-over-global-fields.md) and [019 — The $p$-adic section conjecture](019-p-adic-section-conjecture.md).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Family 011 entry at 266; manuscript blurbs at 275, 284 and 293 |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 011 `\resultentry` at 98 |
| S3 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/README.md`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S4 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/paper.tex`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/paper.tex) | 27 | Title at 3, date at 5, abstract at 9, section inputs at 11–19 |
| S5 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/00-introduction.tex) | 245 | `thm:totient` at 10–16, attribution at 18–25, `thm:smooth` at 38–46, literature at 55–94, companion link at 96–99 |
| S6 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/07-totient-conclusion.tex`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/07-totient-conclusion.tex) | 90 | Transfer to totient fibers at 3–6, `lem:finite-totient-fibers` at 10–12, infiniteness close at 84–89 |
| S7 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/references.bib`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/references.bib) | 245 | Release entry `PrimePredecessors` at 228–234 |
| S8 | [`preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) | 22511 | Typeset manuscript, 802,390 bytes |
| S9 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/README.md`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S10 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/paper.tex`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/paper.tex) | 30 | Title at 3, date at 5, abstract at 9, section inputs at 12–21 |
| S11 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/01-introduction.tex) | 214 | Stick fragments at 19–28, `thm:main` at 30–41, named resolution at 43–48, fixed-$u$ form at 84–100, history at 118–140, method at 142–213 |
| S12 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/08-poisson-dirichlet.tex`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/08-poisson-dirichlet.tex) | 254 | Passage from interior statistics at 4–7, probability inputs at 8–12, labelled-ball setup at 16–17 |
| S13 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/references.bib`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/references.bib) | 291 | Release entry `SmoothShifted` at 264–270 |
| S14 | [`preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) | 22437 | Typeset manuscript, 795,971 bytes |
| S15 | [`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/README.md`](../../../preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S16 | [`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/main.tex`](../../../preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/main.tex) | 141 | Title at 33, date at 35, abstract at 41–43, `thm:main` at 53–57, scope at 59–64, relation to earlier work at 66–76, companion link at 78–90, extensions at 92–108 |
| S17 | [`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/references.tex`](../../../preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/references.tex) | 39 | Inline `thebibliography`; release entry `SmoothShifted` at 25–30 |
| S18 | [`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf`](../../../preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf) | 16893 | Typeset manuscript, 599,500 bytes |
| S19 | [`notes/gen/reports/t0-triage.md`](../../../notes/gen/reports/t0-triage.md) | 897 | Family 011 entry at 125–126 |
| S20 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Ledger row for family 011 at 12 |

## Bibliography

- Alford, W. R., Granville, Andrew, Pomerance, Carl, There are infinitely many Carmichael numbers (1994)
- Alford, W. R., Granville, Andrew, Pomerance, Carl, There are infinitely many Carmichael numbers (1994)
- Arratia, Richard, Kochman, Fred, Miller, Victor S., Extensions of Billingsley's theorem via multi-intensities (2014)
- Baker, R. C., Harman, Glyn, Shifted primes without large prime factors (1998)
- Baker, R. C., Harman, Glyn, Shifted primes without large prime factors (1998)
- Bharadwaj, Abhishek, Rodgers, Brad, Large prime factors of well-distributed sequences (2026)
- Bharadwaj, Abhishek, Rodgers, Brad, Large prime factors of well-distributed sequences (2026)
- Billingsley, Patrick, On the distribution of large prime divisors (1972)
- de Bruijn, N. G., On the number of positive integers $\le x$ and free of prime factors $>y$ (1951)
- Buchstab, A., Asymptotische Abschätzung einer allgemeinen zahlentheoretischen Funktion (1937)
- Dickman, K., On the frequency of numbers containing prime factors of a certain relative magnitude (1930)
- Donnelly, Peter, Grimmett, Geoffrey, On the asymptotic distribution of large prime factors (1993)
- Efron, Bradley, Stein, Charles, The jackknife estimate of variance (1981)
- Ford, Kevin, Halberstam, Heini, The Brun–Hooley sieve (2000)
- Ford, Kevin, Konyagin, Sergei V., Luca, Florian, Prime chains and Pratt trees (2010)
- Ford, Kevin, Poisson approximation of prime divisors of shifted primes (2025)
- Ford, Kevin, Vinogradov's integral and bounds for the Riemann zeta function (2002)
- Friedlander, John, Iwaniec, Henryk, Asymptotic sieve for primes (1998)
- Gorodetsky, Ofir, A Kubilius model for sieve-theoretic sequences (2026)
- Granville, Andrew, Smooth numbers: computational number theory and beyond (2008)
- Granville, Andrew, Smooth numbers: computational number theory and beyond (2008)
- R. C. Baker and G. Harman, _Shifted primes without large prime factors_, Acta Arith. **83** (1998), no. 4, 331–361. doi:10.4064/aa-83-4-331-361.
- Helfgott, Harald Andrés, Radziwiłł, Maksym, Expansion, divisibility and parity (2021)
- Helfgott, Harald Andrés, Radziwiłł, Maksym, Expansion, divisibility and parity (2021)
- J. Friedlander and H. Iwaniec, _Asymptotic sieve for primes_, Ann. of Math. (2) **148** (1998), no. 3, 1041–1065. doi:10.2307/121035; arXiv:math/9811186v1.
- Khale, Tanmay, An explicit Vinogradov–Korobov zero-free region for Dirichlet $L$-functions (2024)
- Matomäki, Kaisa, Radziwiłł, Maksym, Multiplicative functions in short intervals (2016)
- Matomäki, Kaisa, Radziwiłł, Maksym, Tao, Terence, Sign patterns of the Liouville and {Möbius} functions (2016)
- Matomäki, Kaisa, Radziwiłł, Maksym, Multiplicative functions in short intervals (2017)
- Lichtman, Jared Duker, Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors (2022)
- Lichtman, Jared Duker, Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors (2022)
- J. D. Lichtman, _Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors_, arXiv:2211.09641v1, 14 November 2022.
- Montgomery, Hugh L., Vaughan, Robert C., Multiplicative Number Theory II: Primes and Sieves
- Montgomery, Hugh L., Vaughan, Robert C., Hilbert's inequality (1974)
- Montgomery, Hugh L., Vaughan, Robert C., Hilbert's inequality (1974)
- OpenAI, The Poisson–Dirichlet law for prime predecessors (2026)
- OpenAI, Weighted dilation graphs, smooth shifted primes and totient fibers (2026)
- OpenAI, _Weighted dilation graphs, smooth shifted primes and totient fibers_, OpenAI Math Release preprint OAI:Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026, 2026.
- Pilatte, Cédric, Improved bounds for the two-point logarithmic Chowla conjecture (2026)
- Pilatte, Cédric, Improved bounds for the two-point logarithmic Chowla conjecture (2026)
- Pomerance, Carl, Popular values of Euler's function (1980)
- Pomerance, Carl, Popular values of Euler's function (1980)
- Erdős, Paul, On the normal number of prime factors of $p-1$ and some related problems concerning Euler's $\varphi$-function (1935)
- Erdős, Paul, On pseudoprimes and Carmichael numbers (1956)
- Erdős, Paul, On the normal number of prime factors of $p-1$ and some related problems concerning Euler's $\varphi$-function (1935)
- Erdős, Paul, On pseudoprimes and Carmichael numbers (1956)
- Soundararajan, Kannan, Moments of the Riemann zeta function (2009)
- Soundararajan, Kannan, Moments of the Riemann zeta function (2009)
- Stechkin, S. B., Mean values of the modulus of a trigonometric sum (1975)
- Tao, Terence, 254A, Notes 2: Complex-analytic multiplicative number theory (2014)
- Tao, Terence, 254A, Notes 1: Elementary multiplicative number theory (2014)
- Tao, Terence, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations (2016)
- Tao, Terence, 254A, Notes 2: Complex-analytic multiplicative number theory (2014)
- Tao, Terence, 254A, Notes 1: Elementary multiplicative number theory (2014)
- Wooley, Trevor D., Vinogradov's mean value theorem via efficient congruencing (2012)
- T. D. Wooley, _Vinogradov's mean value theorem via efficient congruencing_, Ann. of Math. (2) **175** (2012), 1575–1627. doi:10.4007/annals.2012.175.3.12.

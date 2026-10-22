Notes / Summaries / Convex and metric geometry / [Family 098](../../index/convex-and-metric-geometry/098-a-negative-answer-to-the-lang-plaut-problem.md)

# 098 — A negative answer to the Lang--Plaut problem

## Original CONTENTS.md summary

[S1:272] carries the family entry:

> Every infinite-dimensional real Banach space contains a compact doubling set that admits no bi-Lipschitz embedding into any finite-dimensional normed space. The doubling constant is universal. This answers the Lang--Plaut problem negatively, even for compact subsets of Hilbert space.

The entry names the manuscript "A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding" [S1:272].

The README title is `A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding` [S2:1].

The README dates it September 25, 2026 [S2:5].

## Undergraduate summary

A metric space is doubling when every ball meeting it can be covered by a bounded number of half-radius balls, with centers inside the set. Lang and Plaut asked whether a doubling subset of Hilbert space must sit, up to bi-Lipschitz distortion, inside some finite-dimensional Euclidean space.

The manuscript's abstract states the negative answer. [S3:28] states it: "Every infinite-dimensional real Banach space contains a compact doubling subset that admits no bi-Lipschitz embedding into any finite-dimensional real normed space. The doubling constant has a universal bound, independent of the ambient Banach space. This answers the Lang--Plaut problem negatively, even for compact subsets of Hilbert space."

The main theorem names the set and its constant. [S3:48] gives it: "There is a fixed subset $S$ of real $\ell_2$, equipped with its induced Hilbert distance, whose doubling constant is at most $76800$ and which admits no bi-Lipschitz embedding into $\mathbb R^k$ for any positive integer $k$, at any finite distortion."

The set is a plane plus countably many finite-dimensional layers, at scales shrinking by a factor of 1000. A point's base position decides which basis vector of each layer may be added to it, so the set is sparse at every scale. The proof assumes an embedding exists, extracts a compact pair of derivative bounds from all the resulting sheets, and uses crossings of colored strips to pack more points in a Euclidean ball than the target dimension allows.

## Graduate summary

The doubling notion and the distortion bound are defined. [S3:33] defines them: "A metric space $(X,d)$ is \emph{doubling with constant at most $\lambda$} if every ball in $X$ is covered by at most $\lambda$ balls of half its radius, with centers in $X$. A map $f:X\to\mathbb R^k$ is a \emph{bi-Lipschitz embedding with distortion at most $D$} if there is a scale $a>0$ such that"

and by [S3:38]: "Both the target dimension $k$ and the distortion $D$ are required to be finite."

The question is placed. [S3:40] places it: "Every subset of a finite-dimensional Euclidean space is doubling. Lang and Plaut asked whether every doubling subset of Hilbert space admits a bi-Lipschitz embedding into some finite-dimensional Euclidean space"

The positive snowflake result is recorded. [S3:42] records it: "Assouad's theorem gives a positive result after changing the metric: every doubling metric space admits such an embedding for the distance $d^\alpha$, where $0<\alpha<1$  . This operation is called _snowflaking_."

The dimension-independent snowflake bound is recorded. [S3:42] records it: "Naor and Neiman proved that, when $\alpha$ is close to $1$, the target dimension can be bounded in terms of the doubling constant alone, independently of $\alpha$"

and by [S3:42]: "The distortion bound still depends on the snowflake exponent."

The finite Hilbert case is recorded. [S3:42] records it: "For finite Hilbert subsets, Gottlieb and Krauthgamer obtained embeddings of snowflakes with distortion arbitrarily close to one, with dimension depending on the doubling constant, exponent, and permitted distortion"

and by [S3:42]: "The Lang--Plaut question concerns the original distance $d$, even when arbitrary finite dimension and distortion are allowed."

The exponents above two are recorded. [S3:44] records them: "For exponents $p>2$, Lafforgue and Naor constructed doubling subsets of $L_p$ admitting no bi-Lipschitz embedding into any finite-dimensional Euclidean space"

and by [S3:44]: "Independently, Bartal, Gottlieb, and Neiman obtained dimension-reduction obstructions for doubling subsets of $\ell_p$ using thin Laakso configurations  ."

and by [S3:44]: "Baudier, Święcicki, and Swift later gave an elementary proof of the corresponding fixed-set theorem for $\ell_q$, $q>2$"

and by [S3:44]: "These results concern ambient exponents strictly greater than two and do not settle the Hilbert case."

The withdrawn preprint is recorded. [S3:44] records it: "Schioppa announced a negative answer in  , but withdrew the preprint after reporting a possible issue with its duality argument."

The method is named. [S3:55] names it: "The proof couples a covering argument with a derivative obstruction."

The differentiation lineage is recorded. [S3:55] records it: "Differentiation has a substantial history as a method for ruling out Euclidean embeddings: Cheeger's framework gives such obstructions under doubling-measure and Poincaré-inequality hypotheses"

and by [S3:55]: "Laakso's nonembedding argument gives a related separation-versus-stretch principle: separated branches force an increase in stretch along a subsegment"

The analytic step is stated. [S3:55] states it: "Here the analytic step uses ordinary Euclidean differentiation of Lipschitz maps on open subsets of $\mathbb R^2$ and a quadratic variance identity. A lexicographic extremum treats the two derivative columns successively, and crossings turn their small variation into a packing obstruction."

The strip coloring is described. [S3:58] describes it: "At each scale $r_j=1000^{-j}$, we color horizontal strips of width $r_j$ and vertical strips of width $W_jr_j$ periodically with $N_j$ colors. Here $N_j,W_j$ are positive integers, fixed in advance so that every pair occurs infinitely often. Choose unit vectors $e_{j,i}$, one for each level and color, mutually orthogonal and orthogonal to the base plane. For a base point $p\in\mathbb R^2$, color $i$ permits a displacement $r_je_{j,i}$ whenever $p$ is in a horizontal or a vertical strip of that color. Points of $S$ carry finitely many such displacements."

The set is built independently of any proposed embedding. [S3:83] states this: "We first construct the set independently of any target map. The rapid separation of the displacement scales will give a uniform covering bound even though the number of colors is unbounded."

The ambient space is a Hilbert sum. [S3:89] states it: "be the Hilbert direct sum. This is isometric to real $\ell_2$. Let $e_{j,i}$, $1\le i\le N_j$, denote the coordinate vectors in its $j$th summand."

The zero choice is always allowed. [S3:113] states this: "The zero choice is always allowed, including on strip boundaries. Neither $S$ nor its defining parameters will subsequently depend on a proposed embedding."

The doubling bound is proved. [S3:116] gives it: "The doubling constant of $S$ is at most $300\cdot16^2=76800$."

The covering argument is given. [S3:119] gives it: "Fix a ball of radius $t>0$ centered at a point of $S$. Distinct choices of $w_j$ have distance at least $r_j$. Thus at every level with $r_j>t$, all points of the ball have the same coordinate as its center."

and by [S3:121]: "There is at most one intermediate level satisfying $t/64<r_j\le t$, since consecutive radii have ratio $1000$. The projection of the ball onto each base coordinate lies in an interval of length $2t$. Such an interval meets at most $\lfloor2t/r_j\rfloor+2\le129$ strips of width $r_j$, and the same upper bound applies to strips of width $W_jr_j\ge r_j$. Consequently, at the intermediate level there are fewer than $300$ available labels, including zero."

The proof assumes an embedding and extracts derivative data. [S3:139] states this: "We now assume an embedding exists and extract one compact set of derivative data from all its sheets. Maximizing the two coordinates in order will constrain variation in the two directions separately."

Rademacher's theorem is cited for the derivative. [S3:160] cites it: "Rademacher's theorem gives differentiability almost everywhere on each sheet domain"

The lexicographic maximum is fixed. [S3:175] fixes it: "Thus $(A,B)\in K$. This single compact set and these two numbers remain fixed throughout the argument. The next lemma explains the benefit of maximizing the coordinates in this order: if the mean deficit from $A$ tends to zero, then the mean second coordinate cannot exceed $B$ in the limit."

The compactness lemma is stated. [S3:178–185] states it: "Let $D>0$, let $K\subseteq[0,D^2]^2$ be nonempty and compact, and define $A=\max\{s:(s,t)\in K\}$ and $B=\max\{t:(A,t)\in K\}$. For every $\varepsilon>0$ there is $\delta>0$ such that \[ (s,t)\in K,\quad s>A-\delta\quad\Longrightarrow\quad t\le B+\varepsilon. \] Consequently, if measurable pairs $(s_n,t_n)$ take values in $K$ on probability spaces and $\mathbb E(A-s_n)\to0$, then $\limsup_n\mathbb E t_n\le B$."

The energy estimates are stated. [S3:208] states them: "The output of this section is small variation of the added-sheet offsets: a horizontal estimate strong enough for increasingly long rows, and a vertical estimate for columns of fixed normalized height. The compact set $K$ and the embedding are already fixed."

The vertical selection is explained. [S3:278] explains it: "For the vertical selection, we first average the horizontal derivative over strips of width $nr$. Dividing the same endpoint error $2Dr$ by this wider strip width makes the selected horizontal mean approach $u$. The selected derivative has squared norm at most $A$ almost everywhere, so its mean squared norm must then approach $A$. Lemma~  will control the mean vertical squared norm without requiring a rate."

The variance limit is closed. [S3:309] closes it: "The upper bound has limsup at most zero, so the nonnegative variance tends to zero. In particular, convergence of the vectors $v$ themselves is unnecessary. Combining this with   proves  ."

The crossing section states its plan. [S3:314] states it: "We use the two energy estimates to find one line of every color in each direction on a common period block. Their intersections will supply the separated vectors needed for the Euclidean packing bound."

The period block is chosen. [S3:320] chooses it: "is no greater than its mean on $Q$. Denote its mean on $P$ by $\varepsilon_n$. Proposition~  gives $\varepsilon_n\to0$. The block has width $Nnr$ and height $Nr$, and contains exactly one row and one column of each color."

The crossing separation is obtained. [S3:369] obtains it: "For $i\ne m$, both added labels $re_{j,i}$ and $re_{j,m}$ are permitted at $(x_m,y_i)$: the first by row $i$, the second by column $m$. The corresponding source points have distance exactly $\sqrt2\,r$, so   gives"

The packing bound closes the proof. [S3:379] closes it: "We have obtained $N$ points in the radius-$D$ ball of $\mathbb R^k$ with pairwise distances greater than one. Their open radius-$1/2$ balls are disjoint and contained in the radius-$(D+1/2)$ ball. Comparing Euclidean volumes gives"

and by [S3:383]: "contrary to  . No map satisfying   exists. Together with Proposition~ , this proves Theorem~ ."

The $L_p$ consequence is stated. [S3:390] states it: "For every real $1\le p<\infty$, the fixed metric space $S$ of Theorem~  is isometric to a subset $S_p$ of $L_p([0,1];\mathbb R)$, where $[0,1]$ carries Lebesgue measure. With its induced $L_p$ metric, $S_p$ has doubling constant at most $76800$ and admits no bi-Lipschitz embedding into any finite-dimensional real normed space at any finite distortion."

The relation to the earlier $L_p$ work is recorded. [S3:408] records it: "Lafforgue and Naor proved the qualitative fixed-set obstruction with Euclidean targets for $p>2$ and, in the paragraph following their Theorem~1.1, recorded the corresponding question for $1<p\le2$ as open at that time, while noting stronger known results for $p=1$ \cite[Theorem 1.1 and the following paragraph]{LN}. Theorem~  treats $p=2$, and Corollary~  answers that qualitative fixed-set question with finite-dimensional Euclidean targets when $1<p<2$. This transfer adds no new metric construction."

The finite-set contrast is recorded. [S3:410–411] records it: "Finite-set dimension reduction in $L_p$, for $1<p<\infty$ and $p\ne2$, allows the target dimension to depend on cardinality"

and by [S3:412]: "unlike the fixed infinite-set obstruction of Corollary~ ."

The Banach reduction is described. [S3:416] describes it: "Finite witnesses to Theorem~  can be placed in any infinite-dimensional real Banach space by the classical Dvoretzky theorem. A geometrically shrinking union of these finite clusters, with its limit point adjoined, is compact and retains a uniform doubling bound."

The compact Banach consequence is stated. [S3:419] states it: "There is a universal constant $\Lambda$ such that every infinite-dimensional real Banach space $B$ contains a compact subset $K_B$ whose doubling constant is at most $\Lambda$ and which admits no bi-Lipschitz embedding into any finite-dimensional real normed space at any finite distortion. The subset $K_B$ may depend on $B$, but is chosen independently of the target dimension and distortion."

The finite witnesses are chosen. [S3:435] chooses them: "Choose, for each $j\in\mathbb N$, a finite $X_j\subset S$ that admits no embedding into $\mathbb R^j$ with distortion at most $j$. Each $X_j$ has at least two points. These choices are made before any target for $K_B$ is considered."

The Dvoretzky form used is bounded. [S3:443] bounds it: "Only this qualitative finite-dimensional form of Dvoretzky is used."

The universal constant is given. [S3:487] gives it: "balls, all centered in $K_B$. This proves a universal doubling bound; one may take $\Lambda=1+6\lambda^8$."

The final obstruction is closed. [S3:490] closes it: "Suppose $K_B$ admitted a finite-distortion bi-Lipschitz embedding into a finite-dimensional real normed space. The zero-dimensional case is impossible because $K_B$ has more than one point. Otherwise, choose a linear isomorphism from the target onto $\mathbb R^k$. Equivalence of finite-dimensional norms makes this isomorphism bi-Lipschitz, so composition gives an embedding $f:K_B\to\mathbb R^k$ with some finite distortion $D$. Choose an integer $j\ge k$ with $j\ge2D$. Composing the distortion-below-two placement of $X_j$ onto $C_j$, the restriction of $f$, and the isometric inclusion $\mathbb R^k\hookrightarrow\mathbb R^j$ gives an embedding of $X_j$ into $\mathbb R^j$ with distortion strictly below $2D\le j$. This contradicts the choice of $X_j$."

## Section skeleton

- `build/main.tex` [S3]
  - Introduction (line 31)
  - The construction and proof strategy (line 54)
  - Conventions (line 74)
  - The subset and its doubling bound (line 81)
  - Sheets and extremal derivatives (line 137)
  - Near-extremal rectangles and two energy estimates (line 206)
  - Crossings force a packing contradiction (line 312)
  - A consequence for finite-$p$ function spaces (line 385)
  - Compact obstructions in infinite-dimensional Banach spaces (line 414)

## Comparison with the formalized statement

The scope note states the formalized claim. [S4:9] says: "The formalized result gives a doubling subset of real $\ell_2$, with doubling constant at most $76800$, that admits no bi-Lipschitz embedding into any finite-dimensional Euclidean space at any finite distortion. A companion gives one universal doubling constant such that every infinite-dimensional real Banach space contains a compact doubling subset with no bi-Lipschitz embedding into any finite-dimensional normed space."

The declaration is `OAI.DoublingHilbert.main` at `lean/OAI/Geometry/DoublingHilbert/Main.lean:57` [S5:57]. The second declaration is `OAI.CompactBanach.main` at `lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean:21` [S6:20].

The comparator stubs carry `sorry` at `lean/ComparatorChallenges/DoublingHilbert.lean:27` [S7:26] and `lean/ComparatorChallenges/CompactBanach.lean:31` [S8:30].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 272 |
| S2 | [`preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/README.md`](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/README.md) | 20 | Title, date |
| S3 | [`preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/build/main.tex`](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/build/main.tex) | 560 | Abstract, theorem, construction, proof, consequences |
| S4 | [`lean/docs/098.md`](../../../lean/docs/098.md) | 16 | Scope |
| S5 | [`lean/OAI/Geometry/DoublingHilbert/Main.lean`](../../../lean/OAI/Geometry/DoublingHilbert/Main.lean) | 69 | Declaration |
| S6 | [`lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean`](../../../lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean) | 94 | Declaration |
| S7 | [`lean/ComparatorChallenges/DoublingHilbert.lean`](../../../lean/ComparatorChallenges/DoublingHilbert.lean) | 30 | Comparator stub |
| S8 | [`lean/ComparatorChallenges/CompactBanach.lean`](../../../lean/ComparatorChallenges/CompactBanach.lean) | 34 | Comparator stub |

## Bibliography

**16 entries** from `main.tex`:
- [Assouad] P. Assouad, \emph{Plongements lipschitziens dans $\R^n$}, Bulletin de la Soci\'et\'e Math\'ematique de France \textbf{11…
- [BGN] Y. Bartal, L.-A. Gottlieb, and O. Neiman, \emph{On the impossibility of dimension reduction for doubling subsets of $\el…
- [BSS] F. P. Baudier, K. \'Swi\k{e}cicki, and A. Swift, \emph{No dimension reduction for doubling subsets of $\ell_q$ when $q>2…
- [COO] F. Catrina, S. Ostrovska, and M. I. Ostrovskii, \emph{Dvoretzky-type theorem for locally finite subsets of a Hilbert spa…
- [Cheeger] J. Cheeger, \emph{Differentiability of Lipschitz functions on metric measure spaces}, Geometric and Functional Analysis …
- [Dvoretzky] A. Dvoretzky, \emph{Some results on convex bodies and Banach spaces}, in Proceedings of the International Symposium on L…
- [GK] L.-A. Gottlieb and R. Krauthgamer, \emph{A nonlinear approach to dimension reduction}, Discrete \& Computational Geometr…
- [GKL] A. Gupta, R. Krauthgamer, and J. R. Lee, \emph{Bounded geometries, fractals, and low-distortion embeddings}, Proceedings…
- [Heinonen] J. Heinonen, \emph{Lectures on Lipschitz Analysis}, Report 100, Department of Mathematics and Statistics, University of …
- [Laakso] T. J. Laakso, \emph{Ahlfors $Q$-regular spaces with arbitrary $Q>1$ admitting weak Poincar\'e inequality}, Geometric and…
- … and 6 more

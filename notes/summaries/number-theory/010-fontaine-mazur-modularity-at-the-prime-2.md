# 010 — Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity (Number theory, 3 manuscripts, tier T0)

## Original CONTENTS.md summary

[S1:232]

> **010. Unrestricted pro-modularity at the prime two.** Every continuous odd absolutely irreducible two-dimensional 2-adic representation of $`G_{\mathbb Q}`$ unramified outside finitely many primes occurs in a completed Hecke algebra at some odd tame level. Also proves classical modularity up to Tate twist for irreducible odd representations with these finiteness conditions that are de Rham at 2 with distinct Hodge–Tate weights, resolving the dyadic Fontaine–Mazur case without residual restrictions.

The release lists three manuscripts under this family, and the three blurbs state three different claims:

[S1:241]

> Every continuous, odd, absolutely irreducible two-dimensional 2-adic representation of $`G_{\mathbb Q}`$ that is unramified outside finitely many finite primes occurs in the full completed Hecke algebra at some odd tame level. The level may contain auxiliary tame primes, and scalar and reducible residual representations are included. This is a completed-Hecke occurrence result, with no de Rham hypothesis; it does not assert classical modularity.

[S1:250]

> For every odd positive integer *N*, every irreducible component of the full two-adic Hecke algebra of level $`\Gamma_1(N)`$ has Krull dimension four. This proves the *p* = 2 case of Emerton's dimension conjecture, including all residual components.

[S1:259]

> We prove that every continuous, irreducible, odd two-dimensional 2-adic representation of $`G_{\mathbb Q}`$, unramified outside finitely many primes and de Rham at 2 with distinct Hodge–Tate weights, is modular up to Tate twist. This resolves the odd, regular two-dimensional Fontaine–Mazur conjecture over ℚ at 2, including all residual representations.

## Undergraduate summary

Prior (my training data, not this repo). The Fontaine–Mazur conjecture predicts which $p$-adic Galois representations come from geometry: an odd representation of $G_{\mathbb Q}$, unramified outside finitely many primes and de Rham at $p$ with two distinct Hodge–Tate weights, should be the $p$-adic cohomology of a classical modular form, up to a Tate twist. The case $p=2$ is the awkward one. The modularity-lifting theorems that settled the odd-prime cases lean on hypotheses about the reduction of the representation modulo $p$ — it must stay irreducible, or at least be large — and at $2$ those hypotheses fail easily, because a $2$-adic lattice reduced modulo $2$ is so often scalar or reducible.

The family attacks that gap from three directions, and its three manuscripts prove three genuinely different things. The first proves *occurrence*: the representation shows up in the full $2$-adic Hecke algebra assembled from all weights at a fixed odd tame level. Its own abstract is explicit about the limit of that claim [S4:60–63] “scalar and reducible residual representations are included. This is a completed-Hecke occurrence result, with no de Rham hypothesis; it does not assert classical modularity.”

The second proves a theorem about the size of that algebra: every irreducible component of its spectrum has Krull dimension exactly four, and the manuscript stresses that [S14:96–97] “the theorem does not require a residual Galois representation to be irreducible, nonscalar, or distinguished at $2$.” The third proves the classical modularity statement at $2$ itself, with no residual hypothesis at all.

Read together: the representation lives in the completed Hecke algebra (manuscript A); that algebra is exactly the right size, component by component (manuscript B); and under the dyadic de Rham hypothesis it is a modular form up to Tate twist (manuscript C). The dimension theorem is not decoration — manuscript A uses it as the input that closes its proof [S5:122–124] “The final passage uses the dimension theorem of \cite[Theorem~1.1]{Dim} and the adjoint Selmer vanishing theorem of Newton and Thorne \cite[Theorem~5.4]{NewtonThorne2023}.”

**Proof sketch (the pro-modularity manuscript).** Twist the target representation by a continuous cyclotomic family and place it inside a fixed-determinant trace family of dimension at least three. Choose the base-change field so that it splits completely at $2$; then all dyadic restrictions of the family share one local Galois parameter, and a local comparison builds a one-factor object out of an admissible representation of the product of dyadic groups. Force maximal growth along a chain of prime specializations to obtain a point that is regular and de Rham, hence classical by the regular Fontaine--Mazur theorem. At that point the global deformation ring with determinant allowed to vary has tangent dimension at most three, while a dimension-four integral Hecke component has local dimension three; equality makes the ambient local ring regular, its Hecke kernel vanishes at the point, and since the trace family is a domain through it, the kernel vanishes everywhere on the family. The original representation is therefore on Hecke support.

## Graduate summary

**Occurrence (manuscript A).**

[S5:33–49]

> \begin{theorem}\label{thm:main}
> Let $E/\Q_2$ be finite, with ring of integers $\OO_E$, and let
> $r:G_{\Q}\longrightarrow\GL_2(E)$
> be continuous and absolutely irreducible. Suppose that $r$ is
> unramified outside finitely many finite primes and is odd:
> $\det r(c)=-1$ for complex conjugation $c$.
> Then there exist an odd positive integer $N$, divisible by every odd
> prime where $r$ ramifies, and a continuous $\Z_2$-algebra homomorphism
> \[
>  \lambda:\mathbb T_2(N)\longrightarrow\OO_E
> \]
> such that, for every prime $\ell\nmid2N$,
> \[
>  \lambda(T_\ell)=\tr r(\operatorname{Frob}_\ell),\qquad
>  \lambda(\ell S_\ell)=\det r(\operatorname{Frob}_\ell).
> \]
> \end{theorem}

The conclusion gets its name in the next paragraph [S5:51–54] “We call this conclusion *pro-modularity*. No condition on the semisimplified reduction of $r$ is imposed. In particular, the theorem includes scalar residual representations.” The tame level is not pinned to the ramification set: auxiliary odd primes are allowed, which is the point on which the manuscript distinguishes its theorem from the formulation it cites [S5:65–68] “That formulation prescribes the allowed tame primes. Theorem~\ref{thm:main} proves dyadic occurrence for absolutely irreducible representations while allowing auxiliary primes in the tame level.”

**Dimension (manuscript B).**

[S14:88–91]

> \begin{theorem}\label{thm:main}
> For every odd positive integer $N$, every irreducible component of
> $\Spec T_2(N)$ has dimension exactly $4$.
> \end{theorem}

The algebra is the inverse limit over all weights, Eisenstein series included [S14:93–95] “This is the $p=2$ case of Emerton's Conjecture~2.9 \cite{Emerton11}. The algebra in \eqref{eq:algebra} retains all weights, all Eisenstein systems, and all residual systems of eigenvalues.”

**Classicality (manuscript C).**

[S19:20–30]

> \begin{theorem}\label{thm:main}
> Let
> \[
>  r:G_{\mathbb Q}\longrightarrow\GL_2(\overline{\mathbb Q}_2)
> \]
> be continuous and irreducible. Suppose that \(r\) is odd, is
> unramified outside finitely many primes, and is de Rham at \(2\)
> with distinct Hodge--Tate weights. Then \(r\) is isomorphic to
> a Tate twist of the \(2\)-adic Galois representation associated
> with a classical cuspidal eigenform.
> \end{theorem}

The manuscript states the scope of that statement itself [S19:32–35] “Thus Theorem~\ref{thm:main} resolves the odd, regular two-dimensional Fontaine--Mazur conjecture over \(\mathbb Q\) at \(2\). Its scope includes every semisimple residual representation, including scalar and reducible ones.” The abstract of the same manuscript states the same conclusion in one sentence [S18:66–71] “We prove that every continuous, irreducible, odd two-dimensional \(2\)-adic representation of \(G_{\mathbb Q}\), unramified outside finitely many primes and de Rham at \(2\) with distinct Hodge--Tate weights, is modular up to Tate twist.”

**The moves.**

1. **Trace family.** Manuscript A begins [S5:95–97] “After a continuous cyclotomic twist, we place the original representation in a fixed-determinant trace family $D$ of dimension at least three.” The base-change and connectedness machinery that puts such a family on Hecke support sits in `sections/family.tex` [S6].
2. **Diagonal block equivalence.** [S5:103–106] “We choose the base-change field to split completely at $2$, so that all dyadic restrictions of the family have the same local Galois parameter.” The block-equivalence comparison is `sections/diagonal.tex` [S7], and the manuscript notes [S5:112] “This comparison includes scalar residual blocks.”
3. **A regular de Rham point.** [S5:113–117] “Section~\ref{sec:regular-point} then uses a chain of prime specializations in $D$ to force maximal growth, and hence positive Iwasawa rank, for the one-factor object. Polynomial approximation detects a locally algebraic depth-zero supercuspidal type, yielding a regular de Rham point $x$.” The construction is `sections/regular-point.tex` [S8].
4. **Classicality of the auxiliary point.** [S5:117–120] “The regular Fontaine--Mazur theorem \cite[Theorem~1.1]{FM2} makes $x$ classical up to Tate twist, and Section~\ref{sec:hecke} puts its classical packet and continuous cyclotomic twists in the precise algebra \eqref{eq:full-hecke}.” The Hecke-algebra bookkeeping is `sections/hecke.tex` [S9].
5. **Tangent bound at the classical point.** The closing section proves the adjoint Selmer bound and its deformation-ring consequence, and states what the bound tolerates [S10:31–32] “Both assertions permit scalar or reducible semisimplified residual data and finite extension of the coefficient ring.” The global input is the Selmer vanishing theorem quoted where it is used [S10:55–58] “Newton--Thorne's theorem \cite[Theorem~5.4]{NewtonThorne2023}, specialized to $\GL_2/\Q$, states that for a regular algebraic cuspidal automorphic representation $\pi$ and any prime $p$,”.
6. **Kernel vanishing on the whole domain.** [S5:125–130] “At $x$, the global deformation problem with varying determinant has tangent dimension at most three, while a dimension-four integral Hecke component has local dimension three. Equality makes the ambient local ring regular and forces its Hecke kernel to vanish there. Since $D$ is a domain through $x$, the same kernel vanishes on all of $D$.”
7. **How the dimension theorem is proved.** Manuscript B works at characteristic-zero points [S14:131–132] “The proof works at characteristic-zero points, even on components whose residual systems are reducible or scalar.” Its tangent step is [S14:139–142] “the tangent space at such a point has dimension at most $3$: the Newton--Thorne theorem annihilates the global finite Selmer group, and the only nonzero local quotient has dimension $3$ at $2$.” Two passages are advertised as reusable, and the manuscript is explicit that [S14:151–152] “Neither passage assumes residual irreducibility.”
8. **The dyadic local input.** Manuscript C's local ingredient is [S19:113–115] “The local input is the \(p\)-adic Langlands correspondence of Colmez~\cite{Colmez2010}, in the all-prime form of Colmez, Dospinescu and Pa\v{s}k\=unas~\cite{CDP2014}.” The obstacle it leaves is stated plainly [S19:119–120] “a trace does not record a residual extension class, and globally reducible families can be too large for a direct connectedness argument.”
9. **Classical vectors, then descent.** Manuscript C's locally reducible branch ends [S19:183–184] “This last step avoids assuming that algebraic vectors commute with specialization.”, and its final stage is [S19:191–192] “Descent is applied only after classicality has been established; no descent statement for pro-modular loci is needed.” The eight sections of that manuscript are preliminaries [S20], the deformation problem [S21], completed definite forms [S22], patching [S23], controlled fields [S24], transverse connectedness [S25], and classicality [S26].

**What the family does not say.** Manuscript A's theorem is an occurrence statement and its abstract refuses the stronger reading [S4:61–63] “This is a completed-Hecke occurrence result, with no de Rham hypothesis; it does not assert classical modularity.” Manuscript B says nothing about Galois representations being modular; it bounds the Krull dimension of a Hecke algebra. Manuscript C's theorem is stated for irreducible representations with the dyadic de Rham hypothesis imposed, and it is that hypothesis manuscript A drops. The release blurb's phrase *resolving the dyadic Fontaine–Mazur case* is keyed to the family-level paraphrase in `overview.tex` [S2:96], which merges the three manuscripts into one sentence; the ledger records the family as claim shape `resolution` with `resolves_named` 0, so the page states a resolution of the dyadic case as the manuscripts state it, not as a named-conjecture resolution beyond their own wording.

**Formalization status.** The ledger row for family 010 [S30:11] records 3 manuscripts, 0 formalized, tier T0, 0 comparator challenges, 0 `main_results` configs, no scope note, no verification directory, and no reasoning trace. Nothing about this family is machine-checked.

## History of the conjecture

Prior (my training data, not this repo). Fontaine and Mazur formulated their conjecture in the mid-1990s, in a volume in honour of Jean-Pierre Serre; the odd two-dimensional case over $\mathbb Q$ is the form that modularity-lifting attacks. The long run of results before this release runs through Wiles and Taylor–Wiles patching, the residual-irreducibility and odd-prime hypotheses of the classical lifting theorems, the potential modularity arguments of Harris, Shepherd-Barron, Taylor and Thorne, and the $p$-adic Langlands correspondence at $p=2$ of Colmez, extended by Colmez–Dospinescu–Paškus. The dyadic case is where the residual hypotheses are hardest to remove.

The manuscripts give the corpus-side record. Manuscript C opens with the conjecture itself [S19:3–5] “The Fontaine--Mazur conjecture predicts that irreducible \(p\)-adic Galois representations satisfying suitable finiteness and local conditions arise from algebraic geometry \cite{FM1995}.” Manuscript A records the pro-modularity expectation it is answering [S5:64–65] “Emerton records this expectation for the full varying-weight algebra in \cite[Conjecture~2.12]{Emerton2011Families}.”, and the shape of the earlier theorems [S5:70–76] “Skinner and Wiles developed pro-modularity arguments through ordinary families in the residually reducible setting \cite[Introduction and Section~4.1]{SkinnerWiles1999}. Emerton's local--global compatibility work separates pro-modularity from the production of classical vectors \cite[Section~1.2]{Emerton2011}; the pro-modularity theorem recorded there assumes $p>2$, residual irreducibility, and local residual restrictions.”

The odd-prime route is described in both manuscripts. Manuscript A: [S5:77–81] “Pan extends the family method to the residually reducible nonordinary setting at odd primes: ordinary loci supply modular points, and patching at one-dimensional primes propagates Hecke support \cite[Introduction and Theorem~4.1.7]{Pan2022}. His classical modularity theorems retain regular de Rham hypotheses.” Manuscript C gives the sequence of removals [S19:75–77] “At odd primes, Pan's work treats the residually reducible case and, together with preceding modularity lifting theorems, establishes the regular conjecture apart from one local residual configuration at~$3$” and [S19:78–83] “Zhang removes that configuration, obtaining the stated odd, regular theorem for every odd prime \cite[Theorem~1.0.2]{Zhang2025}. At~$2$, Tung removes the remaining local restriction in a modularity lifting theorem whose global residual image is nonsolvable \cite[Theorem~A]{Tung2021Dyadic}.”, drawing the distinction the family turns on [S19:83–86] “Thus local scalar residual behavior and a globally scalar residual representation must be distinguished: a local theorem covering the former does not by itself settle the latter.”

The two inputs the dyadic proofs lean on are named where they are used. Manuscript C: [S19:100–103] “Thorne's theorem supplies an essential set of classical points: ordinary, potentially crystalline representations of weights $\{0,1\}$ are modular at every prime, without a residual irreducibility hypothesis \cite[Theorem~D]{Thorne2026}.” Manuscript B, on the Selmer input: [S14:119–121] “proved the vanishing theorem used here without the residual restrictions that would obstruct its application to all components at $2$.”

## Consequences now that the proof has been found

The family has one edge that leaves it, and it points at family 004. Manuscript C states the dependency [S19:40–44] “Theorem~\ref{thm:main}, in particular its absence of a residual-image hypothesis, supplies the weight-two modularity input in the height argument of *Hilbert's tenth problem over the rational numbers* \cite[Section~4]{OpenAIH10Q2026}, whose undecidability proof also uses substantial additional arithmetic and logical constructions.” The bibliography entry is a release entry [S27:723–730], whose title line reads [S27:725] “title = {{Hilbert's tenth problem over the rational numbers}},” and whose note field is [S27:729] “note = {Section~4}”, pointing at `Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/`. So the consequence runs 010 → 004: the dyadic modularity theorem is an input to the undecidability proof, and family 004 is T0 as well, so the edge is a reading dependency between two unformalized families, not a machine-checked one. See [004 — Hilbert's tenth problem over ℚ](004-hilberts-tenth-problem-over-q.md).

The other two edges are inside the family. Manuscript A cites both of its siblings as release preprints: the key `FM2` is the manuscript C entry [S11:230–236], titled [S11:232] “title = {{Fontaine--Mazur modularity at the prime 2}},”, and the key `Dim` is the manuscript B entry [S11:238–244], titled [S11:240] “title = {{The Dimension of the Two-Adic Hecke Algebra at Odd Level}},”. Manuscript B cites nothing in the corpus: its 19-entry bibliography carries no release key [S15]. The dependency structure inside the family is therefore one-directional — manuscript A is the consumer, citing the regular theorem of C and the dimension theorem of B — which is why the three manuscripts read as one result with two supporting theorems rather than as three independent papers.

What the family gives the rest of the release is a dyadic modularity theorem with no residual hypothesis, and a dimension theorem for the full two-adic Hecke algebra. Both are stated at $\mathbb Q$; neither is stated for a general totally real field, and the corpus contains no formalization in which either is used, so the downstream consequences are the ones the manuscripts themselves record. The triage record lists this family in the T0 opening [S29:121–124]. Related T0 number-theory pages: [002 — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one](002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md), [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md), [018 — The Margulis–Platonov conjecture over global fields](018-margulis-platonov-conjecture-over-global-fields.md) and [019 — The $p$-adic section conjecture](019-p-adic-section-conjecture.md).

## Sources

The three manuscript roots are `preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/` (8 LaTeX and bibliography files, 2,530 lines), `preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/` (2 files, 1,040 lines) and `preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/` (10 files, 6,278 lines). Manuscripts A and C keep their LaTeX in `build/source/` and `build/sections/`; manuscript B is a single 806-line `build/main.tex` with no section files. Every manuscript file below sits under the manuscript's `build/` directory, which is where this release puts its LaTeX.

| ID | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Family 010 entry at 232; manuscript blurbs at 241, 250 and 259 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 010 `\resultentry` at 96 |
| S3 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/README.md`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/README.md) | 21 | Author at 3, date at 5, citation block at 9–17, version note at 19–21 |
| S4 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/main.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/main.tex) | 75 | Title at 51, date at 53, abstract at 56–64, section inputs at 66–71 |
| S5 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/introduction.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/introduction.tex) | 162 | `thm:main` at 33–49, pro-modularity naming at 51–54, context at 56–132, conventions from 134 |
| S6 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/family.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/family.tex) | 562 | Trace family and base-change support transfer |
| S7 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/diagonal.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/diagonal.tex) | 418 | Dyadic block equivalences and the one-factor object |
| S8 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/regular-point.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/regular-point.tex) | 404 | Prime specializations, Iwasawa rank, the regular de Rham point |
| S9 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/hecke.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/hecke.tex) | 296 | Classical packet and cyclotomic twists inside the full Hecke algebra |
| S10 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/conclusion.tex`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/sections/conclusion.tex) | 267 | Adjoint tangent bound at 14–33, Newton–Thorne input at 55–60, kernel transfer to the domain |
| S11 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/refs.bib`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/build/source/refs.bib) | 346 | Release entries `FM2` at 230–236 and `Dim` at 238–244 |
| S12 | [`preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/two-adic-promodularity.pdf`](../../../preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/two-adic-promodularity.pdf) | — | Typeset manuscript, 454,918 bytes |
| S13 | [`preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/README.md`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S14 | [`preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/build/main.tex`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/build/main.tex) | 806 | Abstract at 51–56, algebra at 68–86, `thm:main` at 88–91, Emerton Conjecture 2.9 at 93–97, method at 130–158 |
| S15 | [`preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/build/references.bib`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/build/references.bib) | 234 | 19 entries, no release key |
| S16 | [`preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf) | — | Typeset manuscript, 347,687 bytes |
| S17 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/README.md`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/README.md) | 21 | Author at 3, date at 5, citation block at 9–17, version note at 19–21 |
| S18 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/main.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/main.tex) | 91 | Title at 57, date at 59, abstract at 65–72, section inputs at 74–87 |
| S19 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/introduction.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/introduction.tex) | 280 | Conjecture at 3–18, `thm:main` at 20–30, scope at 32–38, family-004 dependency at 40–44, history at 48–124, proof route at 126–192 |
| S20 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/preliminaries.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/preliminaries.tex) | 268 | Conventions and local setup |
| S21 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/deformation.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/deformation.tex) | 1074 | Deformation problem and unrestricted propagation |
| S22 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/completed_forms.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/completed_forms.tex) | 786 | Completed definite forms and the pro-modular locus |
| S23 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/patching.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/patching.tex) | 896 | Patching in scalar residual blocks |
| S24 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/fields.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/fields.tex) | 789 | Controlled base-change fields |
| S25 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/connectedness.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/connectedness.tex) | 583 | Transverse connectedness and the dimension loss |
| S26 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/classicality.tex`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/sections/classicality.tex) | 758 | Classical vectors, polynomial orbit, cyclic descent |
| S27 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/references.bib`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/build/references.bib) | 753 | Release entry `OpenAIH10Q2026` at 723–730 |
| S28 | [`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf) | — | Typeset manuscript, 767,547 bytes |
| S29 | [`notes/t0-triage.md`](../../t0-triage.md) | 897 | Family 010 entry at 121–124 |
| S30 | [`notes/catalog.tsv`](../../catalog.tsv) | 373 | Ledger row for family 010 at 11 |

The PDF rows are the typeset form of each manuscript; the page quotes the LaTeX source, which is what the release ships alongside them [S12] [S16] [S28]. The three PDFs are 454,918, 347,687 and 767,547 bytes, and the three READMEs are 21, 18 and 21 lines, carrying the release citation block for each manuscript [S3] [S13] [S17].

Two of the three manuscripts are re-issues, and each says so in its own README. `Unrestricted-pro-modularity-at-the-prime-two-October-4-2026/` is the superseded copy of manuscript A [S3:19–21] and `Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/` the superseded copy of manuscript C [S17:19–21]; both stay tracked in the repository, and the catalog names only the October-6 editions. The supersession is citation-only. In manuscript A the section files are byte-identical between the two copies, `build/source/main.tex` differs in its date line alone, and `build/source/refs.bib` differs in one `\href`, which repoints the bibliography entry for manuscript C from the September-23 copy to the October-6 copy. In manuscript C the section files are again byte-identical, `build/main.tex` differs in its date line alone, and `build/references.bib` differs in one `\href` — the release entry quoted above [S27:723–730], whose link line is [S27:727], now points at the October-6 copy of family 004's Hilbert's-tenth manuscript. No file in either pair adds or removes a line, so every line anchor on this page resolves in both editions. Manuscript B is a first edition: its README carries no version note [S13].

Links are relative to this page's directory: `../../../` is the repository root and `../../` is `notes/`. Family pages cross-linked here: [002 — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one](002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md), [004 — Hilbert's tenth problem over ℚ](004-hilberts-tenth-problem-over-q.md), [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md), [018 — The Margulis–Platonov conjecture over global fields](018-margulis-platonov-conjecture-over-global-fields.md) and [019 — The $p$-adic section conjecture](019-p-adic-section-conjecture.md), the T0 number-theory pages already written. The upstream copies are [CONTENTS.md](../../../CONTENTS.md) and [overview.tex](../../../overview.tex); the triage record is [notes/t0-triage.md](../../t0-triage.md) and the ledger is [notes/catalog.tsv](../../catalog.tsv).

This page is checked by [notes/scripts/verify_summaries.py](../../scripts/verify_summaries.py), which resolves every `[Sn:line]` marker against the shipped file, checks every quotation verbatim against the lines it cites, counts a File cell that resolves under both roots as a problem, and writes nothing. `python3 notes/scripts/verify_summaries.py --mutant` injects one mutant in each form this page uses — an altered inline quotation, a block quote attributed to the wrong source, a manuscript retargeted to its superseded directory, a locator cite moved outside the family's block, and a fabricated quotation — and all five are flagged. The wrapped-inline form is not exercised here: no inline quotation on this page is wrapped across page lines.

Absent by construction (T0): `lean/docs/010.md`, any `lean/OAI/**` file, any `lean/ComparatorChallenges/` entry, any `main_results` config, any verification directory, any reasoning trace.

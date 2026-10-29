[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 031](../index/number-theory/031-uchidas-conjecture-for-open-galois-homomorphisms.md)

# 031 — Uchida's conjecture for open Galois homomorphisms

[Index page](../index/number-theory/031-uchidas-conjecture-for-open-galois-homomorphisms.md)

## Original CONTENTS.md summary

The release's blurb "**031. Uchida's conjecture for open homomorphisms of Galois groups.** Proves Uchida's conjecture: every continuous open homomorphism between Galois groups of possibly infinite solvably closed Galois extensions of number fields comes from a unique equivariant field embedding in the opposite direction. No restriction on the kernel or separate cyclotomic-compatibility assumption is needed. [S1:739]" The catalog abstract 
restates it: "Proves Uchida's conjecture: every continuous open homomorphism between Galois groups of possibly infinite solvably closed Galois extensions of number fields comes from a unique equivariant field embedding in the opposite direction. No restriction on the kernel or separate cyclotomic-compatibility assumption is needed. [S2:138]" The manuscript's title is "Open Homomorphisms of Global Solvably Closed Galois Groups [S3:1]" , and
its abstract reads: "We prove Uchida's conjecture on open homomorphisms of Galois groups. Every continuous open homomorphism between Galois groups of solvably closed Galois extensions of number fields is induced by a unique equivariant field embedding in the opposite direction. No restriction on the kernel or additional compatibility hypothesis is required. [S4:41]"

## Undergraduate summary

A "solvably closed" number field is one with no nontrivial abelian
algebraic extension — algebraic closures and maximal prosolvable
extensions are examples. The isomorphism theorems of Neukirch and Uchida
show that the Galois group of such a field determines the field up to
isomorphism. Uchida asked the corresponding question for homomorphisms:
does every continuous open homomorphism between such Galois groups come
from a field embedding? The theorem 

> **Theorem 1.1**
Let $`F_1,F_2`$ be number fields, and let $`E_i/F_i`$ be possibly infinite solvably closed Galois extensions. Every continuous open homomorphism
$$\alpha:\mathrm{Gal}(E_1/F_1)\longrightarrow\mathrm{Gal}(E_2/F_2)$$
is induced by a unique field embedding $`j:E_2\hookrightarrow E_1`$. [S5:11–17]

The setup [S5:5–9] makes the contravariance explicit: a field embedding
$`E_2 \hookrightarrow E_1`$ induces a group homomorphism
$`\mathrm{Gal}(E_1/F_1) \to \mathrm{Gal}(E_2/F_2)`$ by conjugation, and the theorem says
every open homomorphism arises this way, uniquely.

> Let $`E_i/F_i`$ be Galois extensions of number fields, with each $`E_i`$ solvably closed, and write $`G_i=\mathrm{Gal}(E_i/F_i)`$. A field embedding $`j:E_2\hookrightarrow E_1`$ _induces_ a homomorphism $`\alpha:G_1\to G_2`$ if
$$g\circ j=j\circ\alpha(g)\qquad(g\in G_1).$$
In particular, such an embedding sends $`F_2`$ into $`F_1`$. Uchida conjectured that every continuous homomorphism with open image arises in this way \cite[p. 595]uchida1981. We prove the conjecture in its full form. [S5:5–9]

The kernel is unrestricted [S5:19]. No cyclotomic-compatibility
assumption is needed; the proof derives it from openness itself.

## Graduate summary

**Two main ingredients.** The proof uses two arguments that are stated
as useful beyond the final reduction 

> Two arguments used below are useful beyond the final reduction. First, an additive $`\ell`$-adic character of the absolute Galois group of a number field is determined by its values on any infinite set of primes of absolute residue degree one. More precisely, a character vanishing at all those primes is zero. The logarithmic-rank input is a special case of the $`\ell`$-adic Waldschmidt–Masser theorem . We give a complete proof using Laurent's interpolation-determinant method and a translate-and-degree zero estimate on a torus. Its variants for Frobenius averages and corestriction permit us to treat primes of arbitrary residue degree as well. These statements concern the actual unit-logarithm image and require no hypothesis on its rank. [S5:29]

The second refines Uchida's own Kummer argument 

> Second, we refine the Kummer argument in Uchida's proof of cofinite target coverage \cite[Proposition 1]uchida1981. After logarithmic cyclotomic compatibility has been established, the number of target primes missed by the partial correspondence can be bounded independently of $`\ell`$. A missed prime supplies a Kummer class. On killing a finite cyclotomic twist, these classes lie in one character component of an $`S`$-unit representation. The full extension degree may grow with $`\ell`$, but the multiplicity of that character is bounded by the number of orbits of $`S`$, hence by the degree of the fixed source field. This uniformity allows us to choose $`\ell`$ by simultaneous Kummer conditions and force enough corresponding primes to have the same rational residue characteristic. [S5:31]

**The route.** The reduction goes through $`P = \mathrm{Gal}(\mathbb Q^s/\mathbb Q)`$, the
maximal prosolvable extension of $`\mathbb Q`$: it suffices to identify every
continuous open homomorphism $`G_F \to P`$ with ordinary restriction up to
conjugation [S5:33]. The regular-module construction enlarges finite
quotients of $`P`$ by elementary abelian kernels of regular
representations, and comparing Frobenius averages proves surjectivity and
logarithmic cyclotomic compatibility for an infinite congruence class of
auxiliary primes [S5:35]. A sign character and the uniform Kummer bound
then force residue-characteristic matching for almost every split target
prime [S5:37]. Rational primes split completely in suitable finite
extensions identify the two character pullbacks, and compactness supplies
a single conjugation [S5:37].

**The endpoint.** The proof uses Hoshi's cyclotomic criterion at its
endpoint [S5:26]: an open homomorphism is induced by a field embedding
if and only if it preserves the full cyclotomic character. The main task
is to derive that criterion from the partial local correspondences,
whose domains and exceptional sets initially depend on the auxiliary
prime $`\ell`$.

## History of the conjecture

The reconstruction of number fields from their Galois groups begins with
Neukirch's work on normal number fields and decomposition groups,
continued by Uchida, Iwasawa, and Ikeda . "The reconstruction of number fields from their Galois groups begins with Neukirch's work on normal number fields and decomposition groups . The passage to arbitrary number fields and prescribed group isomorphisms involved Uchida, Iwasawa, and Ikeda; their contributions are recorded in the contemporary accounts . Uchida subsequently established the isomorphism theorem for arbitrary solvably closed Galois extensions of number fields . [S5:22]" Uchida
established the isomorphism theorem for arbitrary solvably closed
extensions [S5:22].

In the 1981 paper formulating the homomorphism conjecture, Uchida proved
it for source field $`\mathbb Q`$, proved uniqueness in general, and established
existence under a local condition on decomposition groups [S5:24].
"In the paper formulating the homomorphism conjecture, Uchida proved it when the source number field is $`\mathbb Q`$, proved uniqueness in general, and established existence under a suitable local condition on decomposition groups \cite[Theorem 1, Proposition 2, and Theorem 2]uchida1981. His local analysis also associates primes to one another whenever a chosen pro-$`\ell`$ inertia group survives under the homomorphism, for an odd auxiliary prime $`\ell`$. For each fixed auxiliary prime $`\ell`$, this partial correspondence reaches all but finitely many target primes \cite[Proposition 1]uchida1981. [S5:24]" His partial correspondence reaches all but finitely many target
primes for each fixed auxiliary prime $`\ell`$, but the exceptional set
depends on $`\ell`$.

Hoshi's 2025 reduction identifies the exact arithmetic condition:
cyclotomic-character preservation . "A later reduction of Hoshi identifies an exact arithmetic condition for existence: an open homomorphism is induced by a field embedding if and only if it preserves the full cyclotomic character \cite[Theorem 3.4]hoshi2025. Hoshi's subsequent work reformulates the unrestricted conjecture in terms of radicals and normality of the field fixed by a kernel \cite[Theorem B]hoshi2026. Related work on finite solvable quotients includes the isomorphism theorem of Saïdi and Tamagawa and the cyclotomic-compatible homomorphism theorem of Mao and Saïdi . Our proof uses the cyclotomic criterion at its endpoint. The main task is to derive that criterion from the partial local correspondences, even though their domains and exceptional sets initially depend on $`\ell`$. [S5:26]" The present proof
derives that criterion from the partial correspondences without assuming
it.

## Consequences

**Full Uchida, no restrictions.** Every continuous open homomorphism
between Galois groups of solvably closed extensions is induced by a
unique field embedding, with no restriction on the kernel and no
separate cyclotomic-compatibility hypothesis [S5:11–17]. This completes
the picture started by Neukirch's isomorphism theorem and Uchida's 1981
partial result.

**Reusable analytic input.** The character-determination theorem
(S5:29) — an additive $`\ell`$-adic character vanishing on an infinite set
of degree-one primes is zero — is a new proof of a special case of the
$`\ell`$-adic Waldschmidt–Masser theorem, using Laurent's
interpolation-determinant method, with no rank hypothesis on the
unit-logarithm image. The uniform Kummer bound (S5:31) bounds the
number of target primes missed by the partial correspondence
independently of $`\ell`$.

## Section skeleton

**Main file** [S4:41], 5 sections under `build/sections/`:

1. Introduction [S5]
2. Anabelian inputs and the local norm identity [S6]
3. The character tests [S7]
4. Surjectivity and logarithmic cyclotomic compatibility [S8]
5. The uniform bound and residue-characteristic matching [S9]
6. Identification of the map to $`P`$ [S10]

Bibliography: `references.tex` [S11].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
7 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 031 at line 739. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 138. |
| S3 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/README.md`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S4 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/main.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/main.tex) | 50 | The main file: the abstract, packages, and section inputs. |
| S5 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/introduction.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/introduction.tex) | 39 | The main theorem, the historical context, the two main ideas, and the proof route. |
| S6 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/preliminaries.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/preliminaries.tex) | 92 | Anabelian inputs and the local norm identity. |
| S7 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/characters.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/characters.tex) | 420 | The character tests and the Waldschmidt-Masser input. |
| S8 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/generation.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/generation.tex) | 425 | Surjectivity and logarithmic cyclotomic compatibility. |
| S9 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/matching.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/matching.tex) | 180 | The uniform Kummer bound and residue-characteristic matching. |
| S10 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/identification.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/identification.tex) | 102 | Identification of the map to P and the proof of the theorem. |
| S11 | [`preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/references.tex`](../../../preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/references.tex) | 101 | The bibliography. |

## Bibliography

- Hyman Bass, _Generators and relations for cyclotomic units_, Nagoya Math. J. **27** (1966), no. 2, 401–407. doi:10.1017/S0027763000026258.
- Samit Dasgupta, _Ranks of matrices of logarithms of algebraic numbers. I: The theorems of Baker and Waldschmidt–Masser_, Essential Number Theory **2** (2023), no. 1, 93–138. doi:10.2140/ent.2023.2.93.
- Yuichiro Hoshi, _Homomorphisms of global solvably closed Galois groups compatible with cyclotomic characters_, Tohoku Math. J. (2) **77** (2025), no. 1, 17–32. doi:10.2748/tmj.20230414.
- Yuichiro Hoshi, _A note on open homomorphisms between global solvably closed Galois groups_, Kodai Math. J. **49** (2026), no. 1, 63–79. doi:10.2996/kmj49104.
- Michel Laurent, _Sur quelques résultats récents de transcendance_, Astérisque **198–199–200** (1991), 209–230. doi:10.24033/ast.93.
- D. W. Masser, _On polynomials and exponential polynomials in several complex variables_, Invent. Math. **63** (1981), no. 1, 81–95. doi:10.1007/BF01389194.
- Jürgen Neukirch, _Kennzeichnung der $`p`$-adischen und der endlichen algebraischen Zahlkörper_, Invent. Math. **6** (1969), 296–314. doi:10.1007/BF01425420.
- Jürgen Neukirch, _Kennzeichnung der endlich-algebraischen Zahlkörper durch die Galoisgruppe der maximal auflösbaren Erweiterungen_, J. reine angew. Math. **238** (1969), 135–147. doi:10.1515/crll.1969.238.135.
- Jürgen Neukirch, _Über die absoluten Galoisgruppen algebraischer Zahlkörper_, Astérisque **41–42** (1977), 67–79. .
- Jürgen Neukirch, _Algebraic Number Theory_, translated by Norbert Schappacher, Grundlehren der mathematischen Wissenschaften, vol. 322, Springer-Verlag, Berlin, 1999. doi:10.1007/978-3-662-03983-0.
- Yu Mao and Mohamed Saïdi, _Open homomorphisms between $`m`$-step solvable Galois groups compatible with the cyclotomic characters_, preprint, 2025. arXiv:2512.13312.
- Mohamed Saïdi and Akio Tamagawa, _The $`m`$-step solvable anabelian geometry of number fields_, J. reine angew. Math. **789** (2022), 153–186. doi:10.1515/crelle-2022-0025.
- K\^oji Uchida, _Isomorphisms of Galois groups_, J. Math. Soc. Japan **28** (1976), no. 4, 617–620. doi:10.2969/jmsj/02840617.
- K\^oji Uchida, _Isomorphisms of Galois groups of solvably closed Galois extensions_, Tohoku Math. J. (2) **31** (1979), no. 3, 359–362. doi:10.2748/tmj/1178229803.
- K\^oji Uchida, _Homomorphisms of Galois groups of solvably closed Galois extensions_, J. Math. Soc. Japan **33** (1981), no. 4, 595–604. doi:10.2969/jmsj/03340595.
- Michel Waldschmidt, _Transcendance et exponentielles en plusieurs variables_, Invent. Math. **63** (1981), no. 1, 97–127. doi:10.1007/BF01389195.

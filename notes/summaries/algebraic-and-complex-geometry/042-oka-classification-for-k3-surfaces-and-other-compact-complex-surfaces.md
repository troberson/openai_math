# 042 - Oka classification for K3 surfaces and other compact complex surfaces

## Original CONTENTS.md summary

[S1:162] carries the family entry and the manuscript entry:

> Proves that every complex K3 surface is Oka, including nonprojective surfaces. More
> generally, every connected minimal compact complex surface of Kodaira dimension zero is Oka; a
> connected minimal compact complex surface of class VII is Oka exactly when it is a Hopf or Enoki
> surface.

[S1:162] carries the manuscript entry as link text:

> Every complex K3 surface is Oka

## Undergraduate summary

A complex manifold is called **Oka** when holomorphic maps into it are as flexible as the target allows: any holomorphic map defined near a compact convex set in some $\mathbb{C}^m$ can be uniformly approximated on that set by a map defined on all of $\mathbb{C}^m$. The name comes from the Oka principle, the idea that on flexible targets, topological problems have holomorphic solutions. The paper proves that every complex K3 surface is Oka, which settles a conjecture listed among the problems in Forstneric's book. [S2:47–50]

The paper's main theorem states the approximation directly: fix a K3 surface with any smooth Hermitian distance, a compact convex set, a holomorphic map near it, and a tolerance. Then an entire map from $\mathbb{C}^m$ to the surface approximates the given map to within the tolerance. [S3:20–29] A corollary turns this into a statement about curves drawn on the surface: through every point and every tangent direction there passes a holomorphic map from the plane whose image is dense in the surface, and when the surface is projective the image is Zariski dense. [S3:43–52]

The release's blurb is broader than the manuscript's title. The paper proves the K3 case; the classification of the other Kodaira-zero and class-VII surfaces is assembled from the K3 result plus cases already established, and the classification is explicitly restricted to minimal surfaces. [S4:108–114]

**Proof sketch.** [S3:54–58]

1. The paper reduces the Oka property to the **convex approximation property** (CAP), which Forstneric proved characterizes Oka manifolds. [S3:11–18]
2. A local operation $L$ is defined on a complex surface, and the paper proves that if $L$ holds at every point, the manifold has CAP in every source dimension. [S5:24–26]
3. For a K3 surface, $L$ is built from two ingredients: a local-to-global approximation lemma, and a **sewing theorem** that glues annular chains of convex sets into one spray. [S6:24–28]
4. The K3 lattice structure supplies the genus-one curves whose self-intersection grows, which is what makes the sewing work on a K3 surface. [S3:54–58]
5. The Enriques case follows from the K3 case: an Enriques surface has an unramified K3 double cover, and the Oka property descends through holomorphic covering maps. [S4:116–125]

## Graduate summary

**The theorem.** For a complex K3 surface $X$ with any smooth Hermitian distance $d_X$, every integer $m \ge 1$, every nonempty compact convex $K \subset \mathbb{C}^m$, every neighborhood $U$ of $K$, every holomorphic $f : U \to X$ and every $\epsilon > 0$, there is a holomorphic $F : \mathbb{C}^m \to X$ with $\sup_{z \in K} d_X(F(z), f(z)) < \epsilon$. [S3:20–29]

**The moves.** CAP is the operative property, and the paper's architecture is a chain of implications: the local operation $L$ at every point of a manifold implies CAP in every source dimension [S5:24–26]; CAP characterizes the Oka property, in the Stein-source formulation that includes deforming continuous maps to holomorphic ones with approximation and interpolation [S3:11–18]. The geometric side supplies $L$ for a K3 surface: the annular-chain sewing theorem takes a chain of annuli indexed by the integers, with a nowhere-zero holomorphic two-form fixed on the surface, and produces the spray the approximation needs. [S6:24–28]

**What the paper does not say.** The manuscript's own classification corollary states the class-VII case as a biconditional: "A connected minimal compact complex surface of class VII is Oka if and only if it is a Hopf surface or an Enoki surface." [S4:108–114]

The paragraph after the corollary is explicit about its own scope: "The classification assertion is restricted to minimal surfaces; no claim is made here for arbitrary blowups or for properly elliptic surfaces." [S4:138–140]

The class-VII half leans on the global spherical shell theorem, cited to a manuscript in this same release: the paper cites `OpenAIGSS`, which is the preprint `Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026`, family 060, titled The Global Spherical Shell conjecture, tier T0 and unformalized. The release records no cross-family edge between 042 and 060 — the ledger's `companions` column is empty for both — so the dependency is a citation choice the release records, not a consequence it states. [S7:42–47]

**Formalization status.** The ledger records family 042 at tier T0: 1 manuscript, 0 formalized, 0 scope notes, 0 comparator challenges, 0 reasoning traces, 0 verification bundles. Nothing in `lean/` corresponds to this result, and there is no scope note saying what the formalization leaves out. The absence is not a red flag — 547 of 719 listed manuscripts are unformalized — and the manuscript's LaTeX is the only source here.

## History of the conjecture

The K3 Oka conjecture is listed among the problems in Forstneric's book, which the manuscript cites as `ForstnericBook`. [S7:11–14] The Oka-property machinery the paper uses is Forstneric's: CAP as the characterization of Oka manifolds, cited to `ForstnericCAP` and `Forstneric`. [S3:11–18] The class-VII classification rests on the global spherical shell theorem, which the release itself supplies as family 060. [S7:42–47] The Zariski-density conclusion for projective K3 surfaces confirms the K3 case of Campana's prediction of Zariski-dense entire curves on special projective manifolds, cited as `Campana`. [S3:54–58]

## Consequences now that the proof has been found

The dense-entire-curve corollary is the consequence the manuscript states for itself: through every point and every nonzero tangent vector of a K3 surface there is a holomorphic immersion of the plane whose image is dense in the surface, and for a projective K3 surface the image is Zariski dense, which is the K3 case of Campana's prediction. [S3:43–52] The classification corollary extends the Oka property across the Kodaira-zero class by covering the Enriques case through the K3 double cover, and settles the class-VII case as a biconditional. [S4:108–114]

The consequence for the catalog is a citation edge, not a recorded dependency: the class-VII half of the classification depends on family 060's global spherical shell theorem, and the release records no `result (NNN)` clause linking the two families. The release records 2 cross-family edges over 372 families, and this pair is not one of them.

## Sources

| # | File | Lines | Role |
|---|---|---|---|
| S1 | `overview.tex` | 859 | The release's family entry and manuscript entry, line 162 |
| S2 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/paper.tex` | 68 | Manuscript abstract, lines 47–50 |
| S3 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/introduction.tex` | 229 | Main theorem 20–29, dense corollary 43–52, CAP 11–18, organization 54–58 |
| S4 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/dense.tex` | 164 | Surface classification 108–114, Enriques cover and minimality restriction 116–128 |
| S5 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/gluing.tex` | 549 | CAP from the local operation, lines 24–26 |
| S6 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/sewing.tex` | 436 | Annular-chain sewing theorem, lines 24–28 |
| S7 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/references.bib` | 181 | `ForstnericBook` 11–14, `OpenAIGSS` 42–47 |
| S8 | `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/README.md` | 18 | The manuscript's own build and run note |

The manuscript root is `preprints/Every-complex-K3-surface-is-Oka-September-23-2026/`, enumerated on disk: `README.md`, `paper.pdf`, and `build/` carrying `figures/`, `paper.tex`, `references.bib` and `sections/`. Every File cell above is the repo-relative path; the links below are relative to this page.

- [S1](../../../overview.tex)
- [S2](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/paper.tex)
- [S3](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/introduction.tex)
- [S4](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/dense.tex)
- [S5](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/gluing.tex)
- [S6](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/sections/sewing.tex)
- [S7](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/build/references.bib)
- [S8](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/README.md)

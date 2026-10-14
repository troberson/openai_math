# Family summary pages

Twenty-nine extended summaries, one per family, each built from the manuscript's own LaTeX and verified
by script. The pages are hand-written; the checker measures them and writes nothing.

## Coverage, as four layers

The release's own formalization surface is four separate counts, and one percentage over them says
nothing. The numbers are the ledger's, quoted with the rule that yields each:

| Layer | Count | What the count is |
| --- | --- | --- |
| Formalized manuscripts | **172** of **719** listed manuscript directories | The per-manuscript formalized flag, counting only listed manuscripts. `formalization.yaml` names **173** paths; the extra one is the superseded `Taming-implies-compatibility-on-four-manifolds-September-23-2026`, which family 342's overview entry does not list. |
| Scope notes | **242** of **372** families | `lean/docs/NNN.md`, each with a `## Scope` section. **121** of the 242 sections state no exclusion at all. |
| Comparator challenges | **416** distinct configs | `lean/ComparatorChallenges/*.lean` files, each a challenge **stub**: 539 `sorry` occurrences, 415 files with at least one, the zero-`sorry` exception being `HarmonicGrowth.lean`. The scope notes link **426** occurrences; the 10-gap is one config linked twice inside each of 7 docs. |
| `main_results` entries | **200** entries over **189** unique configs, reaching **136** of 372 families | `lean/formalization.yaml`'s `main_results:` list. The yaml carries no family key, so family-to-config comes only from the scope notes' links. |

The summaries are a fifth layer, and it is the thinnest: **29** of **372** families have a page.

## The summaries layer

**29** family pages, **6,028** lines, over **67** manuscript directories carrying **13.2 MB** of
LaTeX source. The checker measures **4,414** `[Sn:line]` marker positions and **1,243** quoted spans
across the **30** pages it reads (the 29 family pages and this link-only index page), and reports
**0** problems.

The cost model is the reading pass, not a build. Each page cites the files it read, so the cost per page
is the manuscript LaTeX its Sources table names: the median page cites **21** declared sources and the
largest cites **63**. The checker runs over all 30 pages in **1.14 s** — it walks the cited files and
compares each marker and each quotation against the bytes the file carries, and it runs nothing.

The pages are not a build target: no Lean, no lake, no comparator runs here. A page states what the
manuscript says and where it sits, with a `file:line` anchor the checker resolves.

## The pages

- [197 — Nonsofic groups and group-ring counterexamples](algebra/197-nonsofic-groups-and-group-ring-counterexamples.md)
- [032 — The rational Hodge conjecture for CM abelian varieties](algebraic-and-complex-geometry/032-the-rational-hodge-conjecture-for-cm-abelian-varieties.md)
- [159 — Quasipolynomial bounds for arithmetic progressions](combinatorics/159-quasipolynomial-bounds-for-arithmetic-progressions.md)
- [087 — The Mahler conjectures and symplectic width](convex-and-metric-geometry/087-the-mahler-conjectures-and-symplectic-width.md)
- [101 — The sharp simplex conjecture for isotropic constants](convex-and-metric-geometry/101-the-sharp-simplex-conjecture-for-isotropic-constants.md)
- [147 — The near-boundary Birkhoff conjecture](dynamical-systems-and-ergodic-theory/147-the-near-boundary-birkhoff-conjecture.md)
- [332 — Metric Markov cotype two for $\ell_1$](functional-analysis/332-metric-markov-cotype-two-for-l1.md)
- [258 — Gersten's conjecture for one-relator groups](group-theory/258-gerstens-conjecture-for-one-relator-groups.md)
- [259 — A group without fixed price](group-theory/259-a-group-without-fixed-price.md)
- [271 — Bloch's law and spontaneous ferromagnetic order](mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md)
- [001 — Milne's rationality conjecture](number-theory/001-milnes-rationality-conjecture.md)
- [002 — Full Birch–Swinnerton-Dyer formula from low Selmer corank](number-theory/002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md)
- [004 — Hilbert's tenth problem over Q](number-theory/004-hilberts-tenth-problem-over-q.md)
- [006 — Goldfeld's conjecture](number-theory/006-goldfelds-conjecture.md)
- [007 — Two-point Chowla and the corrected binary Elliott conjecture](number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md)
- [010 — Fontaine–Mazur modularity at the prime 2](number-theory/010-fontaine-mazur-modularity-at-the-prime-2.md)
- [011 — The Ford–Konyagin–Luca conjecture on prime predecessors](number-theory/011-the-ford-konyagin-luca-conjecture-on-prime-predecessors.md)
- [014 — Restricted geometric Langlands, generic Ramanujan and Arthur parameters](number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md)
- [016 — Zilber–Pink in abelian varieties and the Siegel threefold](number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md)
- [017 — The irrationality exponent of pi is 2](number-theory/017-the-irrationality-exponent-of-pi-is-2.md)
- [018 — Margulis–Platonov conjecture over global fields](number-theory/018-margulis-platonov-conjecture-over-global-fields.md)
- [019 — p-adic section conjecture](number-theory/019-p-adic-section-conjecture.md)
- [287 — All nonabelian free group factors are isomorphic](operator-algebras/287-all-nonabelian-free-group-factors-are-isomorphic.md)
- [362 — Global smoothness for relativistic Vlasov–Maxwell](partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md)
- [221 — Mézard–Parisi formula for diluted spin glasses](probability-and-statistical-mechanics/221-mezard-parisi-formula-for-diluted-spin-glasses.md)
- [226 — The curve scaling limit of half-plane double dimers](probability-and-statistical-mechanics/226-the-curve-scaling-limit-of-half-plane-double-dimers.md)
- [102 — Unique games conjecture and optimal approximation thresholds](theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md)
- [109 — Integer multiplication below $n\log n$](theoretical-computer-science/109-integer-multiplication-below-n-n.md)
- [136 — The quasilinear PCP-for-PPAD conjecture](theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md)

## The checker

```
python3 notes/scripts/verify_summaries.py
```

It resolves every `[Sn:line]` marker against the shipped file, checks every quotation against the lines
it cites, counts a Sources-table `File` cell that resolves under both roots as a problem, and writes
nothing. Its self-tests are in `notes/scripts/tests/test_summaries.py`, run by
`python3 notes/scripts/run_tests.py notes/scripts/tests/test_summaries.py -q`: a real quotation
corrupted in each form the page uses, one fabricated quotation, a manuscript root retargeted to a
superseded sibling, and a bare locator citation moved above the family's own block.

Two more tools read the pages: `check_summary_manuscripts.py` reports which manuscripts each page reads
and whether the release still names them, and `refresh_summary_line_counts.py` rewrites each page's
`Lines` column after a manuscript changes. `read_manuscript.py` takes a `preprints/` directory name and
prints the abstract, the section skeleton and the titled statement environments with anchors. All three
write nothing.

This page is link-only: it names no manuscript directory and cites no family-keyed file, so the
checker's manuscript-directory pass and its family-citation pass skip it. Its links are checked.

## Not checked

- **343 families have no summary page.** The 29 pages cover 29 of 372 families; the rest are recorded in
  the ledger and the index, not summarized.
- **The coverage counts are the release's own.** The yaml's `scope`, `automation` and `review` fields
  state partial progress, the agent method, and an unchecked review — those are the release's claims, not
  verified results. Zero `sorry` in a formalized file is not a comparator pass, and it does not mean the
  library elaborates.
- **No page was checked by running Lean.** Nothing in this repo builds, and a Lean run would prove the
  formalized statement, not the manuscript's theorem.
- **The cost model is the reading pass, measured as bytes cited and checker wall.** It is not a build
  cost, and it is not a per-family estimate of the time a reader spends.

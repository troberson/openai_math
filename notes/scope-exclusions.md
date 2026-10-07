# Scope exclusions: what each Lean formalization leaves out

One entry per family with a scope note. Each entry quotes what the note's `## Scope` section says the
Lean formalization does **not** cover, with the `file:line` it comes from. The notes are the release's
own description of its formalization, so this is a record of source-level claims: `formalization.yaml`
states `automation: methods: [agent]` and `review: status: unchecked`, so what a note says the
formalization excludes is what the release asserts, not what a build has confirmed.

## How this was read

All 235 scope notes were read in full, section by section. Each note has exactly two `## `
sections — `## Scope` and `## Comparator links` — so the section boundaries are unambiguous, and every
citation below points inside the `## Scope` section. An entry records:

- a paper result the note says is outside the selected formalized statement;
- a missing explicit constant, threshold, rate, or algorithm;
- a hypothesis the formalized statement keeps as a condition rather than proving;
- a definitional exclusion inside the statement's own wording.

Clauses that only say an assumption is *not imposed* — “No nuclearity, simplicity, trace, or
comparison hypothesis is imposed” — widen the formalized claim instead of bounding it, so they are not
entries. A family whose section states no exclusion gets an explicit **None stated.** row; that is a
finding about the notes, not a claim that the formalization covers the whole paper.

115 of 235 sections state at least one exclusion, carrying 137 exclusion
statements; 120 state none.

## Measurements

From `python3 notes/scripts/extract_scope_notes.py` (report-only, writes nothing). Quote each number
with the rule that yields it.

| Measure | Value |
| --- | --- |
| Scope notes | 235 |
| Docs with both `## Scope` and `## Comparator links` | 235 |
| `## Scope` section lines | 1459 |
| Scope-note lines, all files | 4319 |
| Lines per section (min / median / max) | 4 / 6 / 32 |
| Docs hit by the 5-phrase narrow list | 5 |
| Docs hit by the 24-phrase broad list | 44 |

The narrow list is the five phrases an earlier reading pass recorded: `not formalized`, `excluded`,
`out of scope`, `does not cover`, `not covered`. It hits 5 of 235 — families 003, 020, 049, 173, 360,
with per-phrase hits 0 / 3 / 0 / 1 / 1. The broad list adds `not included`, `not part of`,
`no explicit`, `omitted`, `not asserted`, `excludes`, `excluded`, `exclusion`, `exclude`,
`not supplied`, `not treated`, `not addressed`, `not proved`, `not established`, `not discussed`,
`not modelled`, `not modeled`, `not formalised`, `not formalized`, `not included in the scope`,
`not in scope`, `out of scope`, `does not cover`, `not covered`; it hits 44 of 235.

So 5 is a floor under a narrow rule, not a census. A keyword filter finds 5 sections; the reading pass
finds exclusions in 115. The gap is the reason this page is a reading record and not a tag.

## Entries

One row per family. A quotation is verbatim from the cited line, markup aside.

| Family | What `## Scope` says the formalization leaves out |
| --- | --- |
| 003 | “The principal-character poles at $s=1$ are excluded in the Dirichlet and Hecke statements. The paper's later applications are not included.” `lean/docs/003.md:12` · “No explicit value of $c$ is given. This excludes real zeros in $1-c/\log q<\beta<1$, but does not rule out real zeros elsewhere in $(0,1)$.” `lean/docs/003.md:16` |
| 005 | **None stated.** |
| 007 | “These are ordinary averages, with no logarithmic averaging.” `lean/docs/007.md:11` |
| 008 | “The regularized-transport proposition and graph-complex consequences are not included.” `lean/docs/008.md:11` |
| 009 | “existence of a field isomorphism for every admissible Galois-data isomorphism is outside it.” `lean/docs/009.md:11` |
| 012 | **None stated.** |
| 013 | **None stated.** |
| 015 | **None stated.** |
| 017 | “The paper's convergence consequence for the Flint–Hills series is outside this selected statement.” `lean/docs/017.md:11` |
| 020 | “Negative values are allowed and zero is excluded. No monicity, primitivity, or coefficient-height restriction is imposed.” `lean/docs/020.md:9` |
| 021 | “the optimal order of growth is not determined.” `lean/docs/021.md:9` |
| 023 | **None stated.** |
| 024 | **None stated.** |
| 025 | **None stated.** |
| 026 | **None stated.** |
| 028 | “No explicit function of $D$ is supplied.” `lean/docs/028.md:9` |
| 033 | “The finite-dimension and negative-base branches of the paper's additivity theorem are outside this selected statement.” `lean/docs/033.md:11` |
| 039 | “The threshold is not explicit or uniform over all surfaces.” `lean/docs/039.md:16` |
| 047 | “The separate stable-coordinate and general line-bundle lifting consequences are not included.” `lean/docs/047.md:11` |
| 049 | “The three-variable case is not covered.” `lean/docs/049.md:11` |
| 050 | “The separate very-ampleness result for all admissible even exponents is not included.” `lean/docs/050.md:11` |
| 052 | “Automatic integrability and the paper's additional corollaries are not included.” `lean/docs/052.md:12` · “The paper's compatible product decomposition is a separate consequence, outside this selected statement.” `lean/docs/052.md:14` |
| 058 | **None stated.** |
| 071 | **None stated.** |
| 072 | “no numerical value of $\varepsilon$ is specified.” `lean/docs/072.md:16` |
| 073 | **None stated.** |
| 076 | “The results are existential and do not give an effective convergence rate or a signing algorithm.” `lean/docs/076.md:11` |
| 081 | “The variation and principal-value corollary is not included.” `lean/docs/081.md:9` |
| 082 | **None stated.** |
| 083 | **None stated.** |
| 084 | **None stated.** |
| 085 | “a BV extension is outside these statements.” `lean/docs/085.md:11` |
| 087 | “The nonsymmetric Mahler conjecture and the functional inequalities are not included.” `lean/docs/087.md:13` · “The paper's functional inequality is outside this selected statement.” `lean/docs/087.md:17` · “No boundary smoothness or strict convexity is assumed. An embedding at capacity exactly $4$ is not asserted.” `lean/docs/087.md:21` |
| 088 | “Other inequalities in the projection-body family are not included.” `lean/docs/088.md:16` · “The paper's exponential-factor result for every sufficiently large dimension is not included.” `lean/docs/088.md:22` |
| 089 | **None stated.** |
| 090 | “The separate uniqueness statement for periodic equality cases is outside this selected theorem.” `lean/docs/090.md:14` |
| 091 | **None stated.** |
| 092 | **None stated.** |
| 094 | **None stated.** |
| 095 | **None stated.** |
| 096 | “The separate Gaussian-maxima and kernel-clustering consequences are not included.” `lean/docs/096.md:9` |
| 097 | “The result is existential and does not supply an online algorithm.” `lean/docs/097.md:9` |
| 098 | **None stated.** |
| 099 | “The selected statements are the binary lower bounds. The paper's constant-distortion binary conversion and the companion upper embedding theorem are outside them.” `lean/docs/099.md:19` |
| 100 | “The affine extension of the directionwise conclusion to every nondegenerate tetrahedron is outside the selected regular-tetrahedron statements.” `lean/docs/100.md:22` |
| 102 | **None stated.** |
| 104 | **None stated.** |
| 105 | **None stated.** |
| 106 | **None stated.** |
| 107 | “The result concerns arithmetic complexity, rather than bit complexity or practical crossover sizes.” `lean/docs/107.md:12` |
| 108 | “The paper's algebraic-branching-program consequences are outside these statements.” `lean/docs/108.md:11` |
| 110 | “The additive movement constant is not claimed to be polynomially bounded.” `lean/docs/110.md:16` |
| 111 | **None stated.** |
| 112 | “The result does not assert a fixed exponent $n^{1/2+\varepsilon}$ or a lower bound for unrestricted depth.” `lean/docs/112.md:9` |
| 113 | “The paper's sharp global face-dimension bound is not part of that selected statement.” `lean/docs/113.md:16` |
| 114 | **None stated.** |
| 115 | **None stated.** |
| 116 | “The selected theorem states this universal hitting property. The paper's deterministic polynomial bit-construction bound and matrix-dimension bound $O(ns^2)$ are not separately asserted in it.” `lean/docs/116.md:12` |
| 117 | “The result is an existential sequence, not a bound for every size or a computational hardness theorem.” `lean/docs/117.md:9` |
| 118 | **None stated.** |
| 119 | **None stated.** |
| 121 | **None stated.** |
| 122 | **None stated.** |
| 124 | **None stated.** |
| 125 | **None stated.** |
| 126 | “These selected statements give superpolynomial growth. They do not state the paper's exponential bound for every fixed positive shift.” `lean/docs/126.md:11` |
| 127 | “This establishes the stated asymptotic bound, rather than the separate conjecture identifying exact extremizers.” `lean/docs/127.md:9` |
| 128 | **None stated.** |
| 129 | “The separate results about one-way liveness and the Sakoda–Sipser problem are outside this scope.” `lean/docs/129.md:12` |
| 130 | “The result is subsequential, with no all-length, bounded-coefficient, conditioning, or bit-complexity claim.” `lean/docs/130.md:9` |
| 131 | “The paper's exactly uniform sampling algorithm is outside these selected chain estimates.” `lean/docs/131.md:11` |
| 132 | **None stated.** |
| 133 | “The paper's conditional running-time exclusions are outside these selected construction statements.” `lean/docs/133.md:14` |
| 134 | “The selected statement asserts the uniform expression bound, without separately encoding every construction step of that paper.” `lean/docs/134.md:11` |
| 135 | **None stated.** |
| 139 | **None stated.** |
| 140 | “the stronger $3/5$ variant is outside this scope.” `lean/docs/140.md:20` · “with the auxiliary dimension-two case outside this scope.” `lean/docs/140.md:28` · “The separate streaming consequences and several intermediate comparison constructions are outside this selection.” `lean/docs/140.md:32` |
| 143 | **None stated.** |
| 144 | **None stated.** |
| 145 | **None stated.** |
| 146 | **None stated.** |
| 148 | “Absolute continuity is outside these statements.” `lean/docs/148.md:11` |
| 149 | **None stated.** |
| 150 | **None stated.** |
| 151 | **None stated.** |
| 152 | “The linked statement gives finite entropy; the paper's stronger zero-entropy conclusion is outside this statement.” `lean/docs/152.md:11` |
| 155 | **None stated.** |
| 156 | **None stated.** |
| 157 | **None stated.** |
| 158 | **None stated.** |
| 159 | “The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement.” `lean/docs/159.md:11` |
| 160 | “The sharper intermediate estimates used in the paper are not part of the described formalization.” `lean/docs/160.md:9` |
| 161 | “The separate forcing-conjecture consequence in the paper is outside this statement.” `lean/docs/161.md:9` |
| 162 | “Equal part sizes and numerical thresholds are not asserted.” `lean/docs/162.md:12` |
| 165 | **None stated.** |
| 167 | “The separate unit-distance power-saving theorem is not included.” `lean/docs/167.md:10` |
| 168 | **None stated.** |
| 169 | **None stated.** |
| 170 | **None stated.** |
| 172 | **None stated.** |
| 173 | “The initial vertex and first neighbors are excluded from that count, and sinks are included.” `lean/docs/173.md:9` |
| 174 | “No numerical value of $C$ or construction algorithm is asserted.” `lean/docs/174.md:10` |
| 175 | **None stated.** |
| 176 | **None stated.** |
| 177 | “The graph and two-dimensional cases used for the paper's all-positive-dimensions conclusion are separate.” `lean/docs/177.md:9` |
| 179 | “The paper's classification of odd Barker lengths is outside this selected additional statement.” `lean/docs/179.md:11` |
| 180 | **None stated.** |
| 181 | “The optimal value of $C$ is not determined.” `lean/docs/181.md:9` |
| 182 | **None stated.** |
| 183 | **None stated.** |
| 184 | **None stated.** |
| 185 | **None stated.** |
| 186 | **None stated.** |
| 187 | “it does not impose the paper's smaller finite-board restriction.” `lean/docs/187.md:9` |
| 188 | **None stated.** |
| 189 | **None stated.** |
| 190 | **None stated.** |
| 191 | “The linked construction is for an unbounded sequence of sizes; the paper's statement for every sufficiently large $n$ is broader.” `lean/docs/191.md:9` |
| 192 | **None stated.** |
| 194 | “This selected statement is the complete-domain Dutta comparison. The paper's full flat-local result in arbitrary characteristic is outside it.” `lean/docs/194.md:11` |
| 196 | **None stated.** |
| 197 | “The further conclusion that the group is nonsofic is outside these statements.” `lean/docs/197.md:13` · “The paper's additional spectral-measure integral conclusion is not included.” `lean/docs/197.md:23` |
| 198 | **None stated.** |
| 199 | “The later field-extension, endomorphism-algebra, and related homological consequences are not included.” `lean/docs/199.md:16` |
| 205 | “The stronger claim that every constituent appears in the orbit span of one prescribed tensor is not included.” `lean/docs/205.md:14` |
| 206 | “This selected theorem is the equivalence with the graph criterion; the paper's undecidability and subgroup-interval conclusions are outside it.” `lean/docs/206.md:9` |
| 207 | **None stated.** |
| 210 | “the companion's full range $b\ge6$ is not included.” `lean/docs/210.md:9` |
| 211 | **None stated.** |
| 212 | “Strict convexity is outside these selected differentiability statements.” `lean/docs/212.md:11` |
| 213 | **None stated.** |
| 214 | **None stated.** |
| 215 | “The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included.” `lean/docs/215.md:9` |
| 218 | “The paper's finite stopping-band approximation theorem is outside this selected statement.” `lean/docs/218.md:9` |
| 220 | **None stated.** |
| 221 | **None stated.** |
| 222 | “It does not assert convergence of the finite-system pressure or the paper's extension to all bounded Borel log-potentials.” `lean/docs/222.md:12` |
| 227 | “The paper's full range $\beta<1$, explicit cutoff location, and continuous-time conclusion are outside this selected statement.” `lean/docs/227.md:16` · “The covariance result does not give an upper bound for the full inverse spectral gap.” `lean/docs/227.md:20` |
| 228 | **None stated.** |
| 229 | “Non-reconstruction at or below the threshold and the stochastic-block-model consequences in the paper are outside them.” `lean/docs/229.md:11` |
| 230 | **None stated.** |
| 231 | **None stated.** |
| 234 | **None stated.** |
| 235 | “The statement makes no assertion at the threshold itself.” `lean/docs/235.md:11` · “They do not show that the logarithmic factor in the $k=3$ variance bound is necessary.” `lean/docs/235.md:15` |
| 236 | “Finitary coding and coding-radius bounds are not included.” `lean/docs/236.md:9` |
| 237 | “The paper's $h^{4/3+o(1)}$ mean-length law and its central-visit and hexagonal-chord exponents are outside them.” `lean/docs/237.md:13` · “It does not state the paper's small-force exponent, near-critical correlation scale, or the $3/4$ spatial and moment laws.” `lean/docs/237.md:17` |
| 238 | “The paper's asymptotic conclusion about the product of two random permutations is outside this selected finite estimate.” `lean/docs/238.md:24` · “its changed later statements and six other result blocks are outside this scope.” `lean/docs/238.md:30` · “The paper's full physical-mixing conclusion is outside these selected representation estimates.” `lean/docs/238.md:34` · “the full $L^2$ and total-variation mixing conclusion is outside them.” `lean/docs/238.md:42` · “Physical-shuffle law identification is not included.” `lean/docs/238.md:44` · “The Thorp mixing consequence is outside this selected statement.” `lean/docs/238.md:46` |
| 240 | “The later canonical-point obstruction and the separate eventual-categoricity theorem are not included.” `lean/docs/240.md:11` |
| 241 | “The additional representation corollaries are not included.” `lean/docs/241.md:9` |
| 242 | “The consequence that solvability remains undecidable under an at-most-one-solution promise is not separately formalized.” `lean/docs/242.md:11` |
| 243 | “The separate witnessed-symmetric-choice result is not included.” `lean/docs/243.md:10` |
| 244 | “The paper's stronger transitive-model preservation assertions are outside that selected construction.” `lean/docs/244.md:11` |
| 245 | **None stated.** |
| 246 | **None stated.** |
| 247 | “The paper's separate nil-algebra and radical-algebra conclusions are outside these selected statements.” `lean/docs/247.md:9` |
| 248 | “No explicit boundary constant or prescribed generating set is given.” `lean/docs/248.md:9` |
| 249 | **None stated.** |
| 250 | “The paper's converse about recursively presented subgroups is not included.” `lean/docs/250.md:17` |
| 251 | **None stated.** |
| 252 | “Nonlinearity over every field is not a separate conclusion of the statement linked below.” `lean/docs/252.md:11` |
| 253 | “The later general claims about central kernels and enlargements across families are not included.” `lean/docs/253.md:11` |
| 254 | “Later corollaries in the manuscript are not included.” `lean/docs/254.md:13` |
| 255 | **None stated.** |
| 256 | **None stated.** |
| 257 | “The stronger claims that the witness is two-dimensional and that those models admit no locally $\mathrm{CAT}(0)$ metric are not included.” `lean/docs/257.md:9` |
| 260 | “The paper's general Bondi–Penrose inequality for possibly disconnected weakly trapped boundaries remains unformalized.” `lean/docs/260.md:11` · “This supporting result is not selected as a substitute for the paper's main inequality.” `lean/docs/260.md:13` |
| 261 | “It does not assert the pure-point spectral type claimed in the accompanying paper.” `lean/docs/261.md:11` |
| 262 | **None stated.** |
| 263 | “fixed-$m$ convergence and ground-state attainment are outside this statement.” `lean/docs/263.md:10` · “Ground states are inputs to the statement; their existence is not asserted separately.” `lean/docs/263.md:13` |
| 266 | “The selected statement does not establish the paper's upper bound of three or its computer-assisted exclusion of four arbitrary bases.” `lean/docs/266.md:12` · “The paper's full character-sum vanishing theorem and its mutually unbiased bases bound are outside this selected statement.” `lean/docs/266.md:16` |
| 267 | “It is uniform in the gas parameter within this range and concerns ground states, without a positive-temperature assertion.” `lean/docs/267.md:11` |
| 269 | “This selected statement is the unperturbed Fock-space inequality. Stability under projected one-body potentials and uniqueness of the perturbed ground state are outside it.” `lean/docs/269.md:12` |
| 271 | **None stated.** |
| 272 | “The paper's zero-distillable-secret-key statement is outside these two selected Comparator statements.” `lean/docs/272.md:11` |
| 273 | “The thermal-attenuator minimum-output-entropy and broadcast-capacity consequences in the paper are outside this selected inequality.” `lean/docs/273.md:11` |
| 274 | “regular-trajectory propagation and pruning are not separate formalized statements here.” `lean/docs/274.md:12` |
| 275 | **None stated.** |
| 276 | “Additivity with an arbitrary different partner channel and decoding by separate measurements are not included.” `lean/docs/276.md:9` |
| 277 | “The separate distribution-dependent cubic bound is outside this scope.” `lean/docs/277.md:9` |
| 279 | **None stated.** |
| 280 | “The selected statement does not include complete rationality of the net, unitarizability of all simple modules, the braided tensor equivalence, or the classification of local extensions described in the paper.” `lean/docs/280.md:11` |
| 281 | “The selected statement covers these value and approximation results; it does not itself assert convergence of QAOA circuit energies.” `lean/docs/281.md:12` · “It is conditional on the order parameter being a minimizer and does not separately assert existence of a minimizer.” `lean/docs/281.md:16` |
| 287 | “The paper's fundamental-group conclusion is a further consequence rather than a separate selected statement here.” `lean/docs/287.md:9` |
| 288 | **None stated.** |
| 289 | **None stated.** |
| 290 | “The absolute bicentralizer conjecture is not included.” `lean/docs/290.md:9` |
| 291 | **None stated.** |
| 292 | **None stated.** |
| 293 | **None stated.** |
| 294 | **None stated.** |
| 295 | “The degree-one inner-derivation theorem is outside this selected statement.” `lean/docs/295.md:9` |
| 296 | **None stated.** |
| 297 | **None stated.** |
| 298 | **None stated.** |
| 299 | **None stated.** |
| 303 | **None stated.** |
| 307 | **None stated.** |
| 312 | “The later semi-model structure and full comparison with the homotopy theory of spaces are not included.” `lean/docs/312.md:11` |
| 317 | **None stated.** |
| 322 | **None stated.** |
| 323 | “This is the conditional counterexample direction. The positive consistency direction and the paper's full relative-independence conclusions are outside the selected statement.” `lean/docs/323.md:11` |
| 324 | **None stated.** |
| 325 | **None stated.** |
| 326 | **None stated.** |
| 327 | **None stated.** |
| 328 | **None stated.** |
| 329 | **None stated.** |
| 330 | **None stated.** |
| 331 | “they do not identify that span with the full dual or assert reflexivity for every forest.” `lean/docs/331.md:17` · “This scope concerns the segment-space results; the companion results on diamond energies remain separate.” `lean/docs/331.md:21` · “the remaining auxiliary assertions of the paper are outside this scope.” `lean/docs/331.md:33` |
| 333 | **None stated.** |
| 334 | **None stated.** |
| 337 | **None stated.** |
| 342 | **None stated.** |
| 343 | **None stated.** |
| 347 | “The separate nondegenerate Morse-number construction is not included.” `lean/docs/347.md:9` |
| 348 | **None stated.** |
| 350 | “The known lower bound is not part of this selected statement.” `lean/docs/350.md:11` |
| 353 | “The paper's extension to immersed hypersurfaces without an initial graph assumption is outside this selected statement.” `lean/docs/353.md:11` |
| 354 | **None stated.** |
| 356 | **None stated.** |
| 358 | “The separate no-focal-points and CAT(0) consequences are not included.” `lean/docs/358.md:9` |
| 359 | “This is the negatively pinched construction; the different companion with only one-sided curvature control is separate.” `lean/docs/359.md:9` |
| 360 | “The latter finite-family result does not cover the paper's arbitrary-potential local-injectivity assertion.” `lean/docs/360.md:10` |
| 361 | “Separate tangent-cone and cone-spectrum conclusions are not included.” `lean/docs/361.md:9` |
| 362 | **None stated.** |
| 363 | “These are the conditions of the selected periodic result; later local-conservation refinements are outside it.” `lean/docs/363.md:11` |
| 365 | **None stated.** |
| 367 | “The flatness classification in dimensions at most six and the resulting regularity and singular-set bounds are outside this selected statement.” `lean/docs/367.md:11` |
| 369 | **None stated.** |
| 370 | “The critical equality case is not included.” `lean/docs/370.md:9` |
| 371 | “The selected quantifier gives arbitrarily large odd powers, rather than every sufficiently large odd power.” `lean/docs/371.md:9` |
| 372 | “The selected statement is uniqueness; it does not supply a reconstruction algorithm.” `lean/docs/372.md:9` |
| 373 | “This is the three-dimensional Coulomb result; the paper's inverse-power extensions in every dimension are outside this statement.” `lean/docs/373.md:11` |
| 374 | **None stated.** |
| 376 | “This selected statement covers the sheet programs. The paper's fixed-particle halting detector and its reciprocal maps on solid boxes are outside its scope.” `lean/docs/376.md:14` |

## Not checked

- No Lean build. Nothing here confirms that a formalized statement elaborates, or that an exclusion
  the note names is genuinely absent from the source; the notes are prose written by the release's
  agent-generated pipeline with `review: status: unchecked`.
- Whether a section states an exclusion using none of the measured vocabulary. The reading pass is
  the only guard against that, and it is a human read of 1459 lines, not a rule.
- The `## Comparator links` sections. They name configs, not exclusions; the config inventory lives
  in `notes/links.tsv`.
- The 137 families with no scope note at all (372 families, 235 notes): absence of a note is not
  recorded here, because there is no `## Scope` section to read for them.


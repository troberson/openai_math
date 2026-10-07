# What the `verification` column counts

Measured 2026-10-06 by reading the files each bundle ships. No `lake`, `lean`, or comparator run, and
**no verification program was executed** — see "Not checked".

The ledger's `verification` column counts `preprints/<slug>/verification/` directories: **30 dirs over
22 families** (059, 067, 087, 090, 101, 107, 119, 153, 187, 189, 205, 210, 229, 266, 268, 269, 272,
348, 352, 361, 367, 371). `inputs` counts 4 `INPUTS.md` (057, 157, 251, 259); `covmd` counts 2
`verification/COVERAGE.md`, both in family 348.

A verification bundle is a **finite-arithmetic certificate**, not a proof check. The bundles that
document themselves say so:

| Fam | Bundle | Scope limit, verbatim |
|---|---|---|
| 348 | `manifest.json` (both dirs) | "Supporting exact arithmetic package only; no theorem certification claim" |
| 348 | `COVERAGE.md` (both dirs, byte-identical) | "The verifier checks finite polynomial, coefficient, and rational-integral claims, not the manuscript's geometric or analytic reductions." |
| 268 | `README.md` | "They verify finite scalar, thermal, and trial calculations, not the analytic proof." · "The programs embed their finite inputs and do not read the stored JSON files as premises." |
| 361 | `README.md` | "This optional check performs exact integer spectral-selection comparisons for ambient dimension `n=16` and cutoff `k=50000`. It does not construct the metric or verify the complete counterexample." |
| 090 | `An-atomic-certificate…/README.md` | "The checker verifies the finite blocks, parameter-polytope bounds, envelope comparisons, and Bernstein tables, not the article's analytic propagation and energy-transfer arguments." · "`CERTIFICATE.json` identifies the checker and documented command; it is static metadata, not an execution receipt." |
| 090 | `A-sharp-Fourier-certificate…/README.md` | "The main command checks the finite matrix, residual, Bernstein, and scalar comparisons. The analytic quadrature, continuum, and infinite-tail arguments remain in the article." |
| 090 | `Universal-optimality…/README.md` | "These commands check finite arithmetic, not the manuscript's analytic reductions." · "They do not execute the separate floor-rounded matrix construction." |
| 090 | `Triangular-minimality…/README.md` | "`data/certificate-record.txt` … is evidence for readers, not an input to the runner." · "The wrapper does not read the manuscript." |
| 107 | `README.md` | "This command does not run the numerical checks." (the inventory check verifies byte counts and SHA-256 only) |

So a `verification` value of 1 is evidence that a family ships a reproducible **finite computation**,
and the bundle's own text states that the analytic/geometric reductions are outside it. It is not
evidence that the theorem was checked.

## How documented the bundles are

- **12 of 30** ship a `README.md` with a run command and success criteria: 087, 090 (×4), 107, 119,
  229, 268, 348 (×2), 361. **18 ship no README** — a command is not recoverable from the bundle.
- **2 of 30** ship `manifest.json` (both 348 dirs) with `scope`, `main_command`, `network_required`,
  `third_party_dependencies`, and per-file sha256. The other 28 have no manifest.
- **2 of 30** ship `COVERAGE.md` (both 348 dirs).
- Success criteria are bundle-specific and deliberately narrow: exit status 0 **plus** a printed
  marker (`PASS`, `"all_passed": true`, `"status": "pass"`, `passed: true` with a stated record
  count). Two READMEs warn that files on disk prove nothing: "A failed run may leave older or partial
  result files; those files do not establish success for that run" (090) and "file presence alone is
  not success" (090).
- **8 of the 12** READMEs insist Python assertions stay enabled (`-O`, `-OO`, `PYTHONOPTIMIZE`
  forbidden): 087, 090 (×2), 119, 229, 268, 361. **2** reject `NDEBUG` in the C++ programs (090
  `Triangular-minimality`, 229). The checks live inside `assert` statements, so an optimized run is a
  no-op. The two 348 bundles are the only ones that say the opposite — "Checks remain active under
  Python `-O`" — because their verifier compares output rather than asserting.

## What the 348 bundle checks, and what it omits (read 2026-10-07)

Every count here comes from `python3 notes/scripts/extract_verification_348.py`, which reads the two
bundles as text and runs nothing. `python3 notes/scripts/verify_verification_dirs.py` re-derives those
counts independently, resolves every anchor in this section, and checks every quotation against the
lines it cites; it writes nothing.

**The two dirs are one bundle shipped twice.** Of the 9 files they share, **7 are byte-identical** —
`verify.py` (28,511 B), `polynomial.py`, `results.json` (447,073 B), `COVERAGE.md`,
`dependencies.json`, `portability_check.py`, `portability-results.json` — and **2 differ**:
`README.md` (768 B vs 855 B, the extra bullet naming the scalar script) and `manifest.json`, which
hashes `README.md`. The Zero-Plane dir carries one extra file, `check_scalar_certificates.py`. So the
ledger's `verification` value of 2 for family 348 counts two copies of one arithmetic check, not two
independent checks.

**What the check is.** `verify.py` is 504 lines with 6 `check_*` functions (at lines 157, 170, 271,
334, 373, 397). `--check` recomputes everything and compares the serialized JSON against the shipped
file (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:496`):

```
        require(RESULTS_FILE.read_text(encoding="utf-8") == encoded,
                "Recomputed exact results differ from bundled results.json")
```

A passing run therefore shows that the shipped numbers are reproducible from the shipped code. It does
not compare any number with the manuscript. Shipped counts, from `results.json` in both dirs:
**53** identities, **21** interval certificate rows (**15** reported + **6** supplementary),
**12** triangle certificate rows (**9** carrying a determinant floor), **24** exact-value assertions,
over **41** subinterval records.

**Four things it does not cover.**

1. **The reductions.** `COVERAGE.md` says the verifier checks "finite polynomial, coefficient, and
   rational-integral claims, not the manuscript's geometric or analytic reductions", and the
   manuscript defers to it: *"Its coverage record distinguishes those executed reconstructions from
   the collection identities and geometric reductions proved in the text."*
   (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/07-certificates.tex:14`).
   The optional scalar script is explicit about the split: *"The accompanying mathematical proof
   supplies the compactness, separation, calculus, Jacobi comparison, and Sobolev arguments."*
   (`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/check_scalar_certificates.py:14`).
2. **The manuscript-to-literal link.** **9** `scalar_claim` keys name a printed value
   (`eq9.printed_minimum`, `eq9.printed_minimum.endpoint_lower`, `eq22.printed_CBE.8.0`, …) and each
   compares a computed minimum against a rational literal written into `verify.py`. Nothing in the
   bundle parses the manuscript, so the mapping from a printed number in the PDF to that literal is
   made by hand and is not re-checked by the command.
3. **`all_passed` is not an aggregation.** It is assigned unconditionally at the end of `compute()`
   (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:477`):

   ```
           "all_passed": True,
   ```

   Every check aborts through `require` (13 occurrences) on the
   first failure, and each record is appended with `"passed": True` only after its check passes —
   **151** such occurrences in `results.json`, and no negative record anywhere. `results.json` is a
   transcript of a completed run, not a table of independent verdicts.
4. **The reference is regenerable.** `dependencies.json` ships `regenerate_command:
   python -B verify.py --write`, which overwrites `results.json` beside the script. The file
   `--check` compares against is not fixed by anything outside the bundle.

**Manifest gaps.** Both `manifest.json` files list 8 files, and every listed sha256 and byte count
matches what is on disk (0 mismatches). Neither hashes `manifest.json` itself, and the Zero-Plane
manifest omits `check_scalar_certificates.py` — the only file unique to that directory. That file
imports `sympy` while `dependencies.json` declares `"third_party_dependencies": []`, so the one
undeclared third-party import in family 348 is in the one file the manifest does not list.

**The coverage file names only shipped artifacts.** `COVERAGE.md` points at `results.json`, `verify.py`,
`polynomial.py`, and `README.md`; all four are present in both directories. The family-318 pattern — a
coverage document naming files that do not exist — does not fire here, which is what makes 348's scope
statement safe to quote.

**The method is sufficient, not necessary.** An interval certificate requires every Bernstein
coefficient of the polynomial, on each subinterval, to be at or above a stated floor; a triangle
certificate additionally requires the exact zero pattern to match (`actual_zeros == expected_zeros`).
A Bernstein bound is a sufficient condition for a lower bound, so a bound the bundle cannot certify is
not evidence that the bound is false — and the bundle records only the bounds it chose to certify.

**The bundle self-tests.** `portability-results.json` ships **11** checks, **8** of them negative
tests naming a rejection: **7** whose names end in `rejected` (`altered_saved_results`,
`incorrect_zero_locations`, `violated_coefficient_floor`, `univariate_degree_truncation`,
`triangle_degree_truncation`, `inexact_polynomial_division`, `floating_point_coefficient`) plus
`incorrect_printed_triple_rejected_under_O`, which appends the flag it tests. The other three are
`relocated_run_from_different_cwd`, `optimized_python_checks_remain_active`, and
`original_runtime_files_unchanged`. This is the only bundle among the 30 that demonstrates its own
checks fail on bad input; the report is a shipped artifact, not a run this session performed.

## Requirements, for anyone who wants to run them

Python only, standard library: 348 (×2, Python ≥ 3.10), 361, 090 `An-atomic-certificate`, 268
(scalar + trial programs). Pinned third-party: 090 `A-sharp-Fourier-certificate` and
`Universal-optimality` (`python-flint==0.9.0`); 087 and 119 (SymPy 1.14.0); 268 thermal program
(NumPy + SciPy). C++ toolchain: 119 (C++17 with signed `__int128`), 229 (g++ C++17, `__int128`,
UBSan), 090 `Triangular-minimality` (g++ C++17, OpenMP, Boost.Multiprecision). 107's inventory check
is Python ≥ 3.9 stdlib. `network_required` is false where stated; 090 and 348 need the full paper
source tree present because manifests hash `build/` sources.

## Not checked

- **Nothing was executed.** No `verify.py`, `reproduce.py`, or certificate program was run, so no
  family here has a passing run in this record. Running them needs a virtualenv (system Python is
  PEP 668 externally managed) and, for four bundles, a C++17 toolchain.
- The 18 undocumented bundles were counted, not read for scope; their limits are unstated, not known
  to be absent.
- Certificate *contents* were not audited: no check that a bundle's finite claims are the ones the
  manuscript uses, and no recomputation of any bound.
- `results.json`/`CERTIFICATE.json`-style stored outputs were not compared with freshly generated
  output. Several READMEs state the stored files are not premises; that was taken at face value.
- Family 318's `SUPPORT-COVERAGE.md` is a different case: it names a `support/r-ce/` bundle,
  `BUILDING.md`, and `SUPPORT-COVERAGE.json` that do not exist on disk.

Specific to the 348 section above:

- The shipped `portability-results.json` is the release's own report. Its 11 checks, including the 8
  negative tests, were **read, not executed** here, so "the bundle demonstrates its checks fail on bad
  input" is a claim about the artifact, not an observation made in this session.
- The 9 printed-value literals in `verify.py` were **not** compared with the numbers printed in the two
  manuscripts. The hand-transcription gap is described from the code's shape; no mismatch was looked
  for, so none is recorded.
- Manuscript references to the bundle were found by matching `verify.py` or `COVERAGE.md` in
  `build/**/*.tex` — 3 hits. A reference phrased without either token would not have been found.
- `check_scalar_certificates.py` was read for its imports and its scope sentence, not audited line by
  line; its SymPy use is reported from the import, not from what it computes.

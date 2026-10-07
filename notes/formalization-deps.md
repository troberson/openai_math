# The upstream library graph

Measured 2026-10-07 by `python3 notes/scripts/extract_formalization_deps.py`, which writes
`notes/formalization-deps.tsv` — **31 rows, 8 fields**. No `lake`, `lean`, `lake exe cache get`, or
comparator run, and **no build was attempted**, so every pin below is a declared pin, not a verified
buildable pin. The generator report is the test; quote a number below with the rule that yields it.

## The four layers, and what each one says

| Layer | What it declares | Measured |
|---|---|---|
| `lean/lakefile.lean` | `require … from git "url" @ "commit"` | **30** declarations, every one pinned to a **40-char** commit |
| `lean/formalization.yaml` | `related_formalizations:` → `id:` + `relationship:` | **30** entries, all `relationship: builds-on` |
| `lean/OAI/**/*.lean` | `import` statements | **276,599** OAI-rooted, **56,196** Mathlib-rooted, **3** `all`-prefixed |
| `lean/patches/` | `*-lean4341.patch` | **23** patches, **160,187** lines (plus `README.md`) |

The 30 lakefile declarations and the 30 yaml entries cross-match exactly — 30 declared in both
layers, 0 declared in the lakefile only. The row set is the union of the declared libraries and the
import roots that are imported but undeclared, so **31 rows = 30 declared + 1 undeclared**.

## A fifth layer the spec does not name: `lean/lake-manifest.json`

`lean/lake-manifest.json` is tracked (426 lines, `"version": "1.2.0"`, `"packagesDir":
".lake/packages"`, `"fixedToolchain": true`) and lists **42 resolved git packages**, every `rev`
40 chars. It reconciles with the declared set with no residue:

- **30 of 42** are the declared libraries, and **all 30 manifest revs equal the lakefile pins** — 0
  mismatches, and 0 declared libraries absent from the manifest.
- **12 of 42** are transitive-only: `BibtexQuery`, `Cli`, `LeanSearchClient`, `MD4Lean`, `Qq`,
  `UnicodeBasic`, `aesop`, `batteries`, `importGraph`, `leansqlite`, `plausible`, `proofwidgets`.
  These are the Mathlib-ecosystem closure; none is declared in `lakefile.lean` and none is an import
  root in `lean/OAI/`.

**Decision point (recorded, provisional).** The spec names four sources and fixes 8 columns, so the
manifest is *not* a column — it is recorded here. Revisit condition: if a later bead needs resolved
pins machine-readably (a per-library pin table, or `math-el4.2`'s link graph), add a `manifest_rev`
column then; the change is additive and provable by diffing the TSV column by column.

The manifest is a **generated** artifact — Lake wrote it, so a `lake update`/`lake resolve` happened
somewhere. It is evidence of a resolution event, not of a build in this repo: `.lake/packages` is
absent, so no upstream source is vendored.

One hunk of the AINTLIB patch corroborates the mathlib pin directly: it rewrites AINTLIB's own
`[[require]] name = "mathlib"` from `rev = "e4b72ca0d01c"` to
`rev = "d13f23b723b8a846827a245b89c10fc7d3f11612"`, annotated `# Zauner compatibility:
Lean/Mathlib v4.34.1` — the same 40-char commit OAI pins and the manifest resolves. The patches are
what make the pins agree on one mathlib.

## The import rule, and the scope it is measured over

Root = the first dotted token after `^\s*import\s+`. `import all Mathlib` is rooted at `all`, not at
Mathlib, so it contributes 3 to `all` and 0 to Mathlib. Comments are not stripped; stripping `--` and
`/- -/` changes no count, because no import statement is commented out.

The counts above are over **`lean/OAI/**/*.lean` (121,734 files)**, which is what the acceptance line
reproduces. Over the whole tree `lean/**/*.lean` (122,141 files) the same rule yields **OAI 277,501 /
Mathlib 56,715** — the difference is `lean/ComparatorChallenges/`, whose 405 files import Mathlib
**519** times and import OAI **zero** times. Quote the scope with the number.

Upstream sources are **not vendored** (there is no `lean/.lake`), so import roots are the only
in-repo evidence that a library is used. There are **12 external import roots** carrying **56,482**
import statements; 11 are aliased to a declared URL, 1 is not.

## The join key is a trap

The lakefile writes `https://github.com/leanprover-community/mathlib4.git` and `formalization.yaml`
writes the same repo **without** `.git`; `schoenflies-lean` in the lakefile has no `.git` either. A
naive normalization keys mathlib as `mathlib4git` and every join fails — the first run of the
extractor printed 90 `PROBLEM` lines and refused to write the TSV. `url_key()` strips `.git` from the
last path segment before normalizing.

The three layers also name one library three ways: lakefile `«fixed-point-theorems»`, yaml
`harfe/fixed-point-theorems-lean4`, source `import FixedPointTheorems…`. The alias map in the
extractor is hand-written for that reason, and every alias is asserted to resolve to a declared URL,
so a stale alias fails loudly rather than silently zeroing an import count.

## `formalization.yaml` claims an ordering it does not satisfy

The comment above `related_formalizations:` reads, verbatim:

> `  # Imported libraries, ordered by direct import count in project Lean sources.`

Measured against the import counts, **5 entries are out of order** — each has a measured count
*greater* than the entry directly above it:

| Position | Entry | Imports | Above it | Imports |
|---|---|---|---|---|
| 5 | `strongpnt` | 12 | `AINTLIB` | 0 |
| 8 | `TauCeti` | 5 | `fixed-point-theorems-lean4` | 4 |
| 11 | `gromov` | 2 | `heights` | 0 |
| 13 | `schoenflies-lean` | 2 | `iut` | 0 |
| 16 | `AbsorptionCutoff` | 1 | `zeta_3_irrational` | 0 |

The extractor prints these five lines in the report, so the count is reproducible.

The claim is recorded, not asserted true. The obvious rescue — that the list is ordered by
*transitive* use, so a library can sit high in it while importing nothing directly — is not supported
by the manifest: the transitive closure is 12 packages (`Qq`, `aesop`, `batteries`, …) and **none of
them is one of the 19 zero-import declared libraries**. The 19 are declared by OAI itself, so their
zero counts are not a transitivity artifact at the direct-import level; they are simply libraries
that OAI pins and never imports.

## 19 declared libraries import nothing directly

`AINTLIB`, `LeanArchitect`, `PrimeCert`, `Zeta3Irrational`, `belyi`, `carleson`, `checkdecls`,
`doc-gen4`, `elliptic-curves`, `formal-schemes`, `genl`, `heights`, `iut`, `leancert`, `oka`,
`orbicurve-cores`, `pi1`, `tate-curves-theta`, `tempered-fundamental-groups` — recorded with
`direct_imports=0`, not dropped.

Only **12 of 31** rows have any direct import: mathlib 56,196, then PrimeNumberTheoremAnd 244,
StrongPNT 12, rellich-kondrachov 9, TauCeti 5, ClassFieldTheory 4, fixed-point-theorems 4,
SphereEversion 2, gromov 2, schoenflies-lean 2, AbsorptionCutoff 1, BernoulliRegular 1. Mathlib is
56,196 of the 56,482 external statements — **99.5%** — so the OAI tree is a Mathlib project with a
thin layer of specialist libraries on top.

**7 declared libraries ship no patch**: mathlib, TauCeti, LeanArchitect, PrimeCert, checkdecls,
doc-gen4, leancert. The last four are tooling, not mathematics. Patch size tracks how much upstream
surgery was needed, not how much a library is used: PrimeNumberTheoremAnd 39,904 lines,
ClassFieldTheory 31,757, StrongPNT 26,284, AINTLIB 23,288, gromov 18,638 — while TauCeti, with 5
direct imports, needs no patch at all.

## BernoulliRegular: imported, declared nowhere

`lean/OAI/NumberTheory/Ostmann/Quadratic/QuadraticGaussSign.lean:2` is the only import:

> `import BernoulliRegular.GaussSum.QuadraticEndpoint`

`BernoulliRegular` appears **zero** times in `lean/lakefile.lean` and **zero** times in
`lean/formalization.yaml`. It is recorded as a row with `lakefile_declared=n`, `repo_url=none`,
`pinned_commit=none` — a row, not a dropped count, and not a silent alias.

Where it comes from is recoverable from the patches: `lean/patches/AINTLIB-lean4341.patch` touches
`projects/FltRegularBernoulli/BernoulliRegular/BernoulliGeneralized.lean` (patch line 4055),
`Characters.lean` (4131), `GaussSum/Basic.lean` (4165), and
`GaussSum/SignInvariant/BlockDeterminant.lean` (4287). So **BernoulliRegular ships inside the AINTLIB
repo** as one project in a multi-project tree — the same patch touches 158 files, of which
`projects/HasseWeil` (118), `projects/DedekindResidue` (15), `projects/Chebotarev` (14), and
`projects/FltRegularBernoulli` (9), plus `lakefile.toml` and `lean-toolchain`. The patch's
`lakefile.toml` hunk shows AINTLIB declaring `[[lean_lib]]` blocks with globs such as
`CebotarevDensity`, which is the mechanism by which a project inside a dependency becomes a top-level
import root reachable from OAI without appearing in OAI's lakefile. The specific imported module
`BernoulliRegular.GaussSum.QuadraticEndpoint` is **not** touched by the patch, so it exists upstream
unpatched.

`BernoulliRegular` is also **absent from `lean/lake-manifest.json`**. That is consistent with the
subproject explanation and proves nothing on its own: the manifest lists *packages*, not the
`lean_lib`s inside them, and AINTLIB is present as a package. So the absence is not evidence that the
import fails to resolve, and this record does not claim it is.

What the divergence does establish: this is the one library in the release with **no pin of its own**.
Every other library is pinned to a 40-char commit by OAI; `QuadraticGaussSign.lean` resolves
BernoulliRegular from AINTLIB's tree at whatever revision *AINTLIB's* declaration selects, so OAI's
pin list does not pin it.

## Not checked

- **No build was run**, so no pin is verified as buildable and no patch is verified as applicable.
  Patch applicability is asserted by the release, not by this record.
- Upstream repos were not fetched: no commit was checked to exist, and no URL was checked to resolve.
- Import counts are **direct statements only**, not the transitive closure. The 19 zero-import rows
  are evidence of *no direct import*, not of non-use — that is precisely the gap the yaml ordering
  comment is about.
- The BernoulliRegular → AINTLIB link is read from patch file paths. No AINTLIB `lakefile.toml`
  `[[lean_lib]]` entry naming `BernoulliRegular` appears in the patch hunks — the patch carries only
  two `lakefile.toml` hunks, not the file — so the mechanism is inferred from the sibling
  `CebotarevDensity` block, not observed. AINTLIB's full `lakefile.toml` is not shipped here.
- The manifest's 42 revs were compared with the 30 declared pins; they were **not** checked against
  upstream, so a rev that matches its declaration is a matching string, not a commit that was shown
  to exist.
- The 12 transitive-only packages were identified by set difference. Which declared library pulls in
  each one is not recorded — the manifest does not carry the dependency edges that produced them.
- `lean/docs/` ships 0 `.lean` files, so it contributes nothing to the import counts; it was not
  checked for dependency prose.
- Whether each declared library is *needed* is not measured — 30 declarations, 12 with direct
  imports, and no build to say which are load-bearing.

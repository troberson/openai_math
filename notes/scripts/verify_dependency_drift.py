#!/usr/bin/env python3
"""Verify notes/dependency-drift.md against the shipped dependency record.

Report-only; writes nothing. Five passes:

1. Anchors. Every `path:line` anchor must name a file that exists and a line inside it;
   every bare `:NN` anchor resolves against the last explicit path that precedes it.
2. Blockquotes. Every `> `path:line: text`` line must match that file's line, with
   whitespace runs collapsed on both sides — the page wraps, the source does not.
3. Code spans. Every backticked span long enough to be code, and code-shaped, must occur
   verbatim in lakefile ∪ yaml ∪ patches ∪ TSV. A span containing `…` is the page's own
   elision and is exempt; so is anything path-shaped.
4. Counts, table, name lists. Every number the page quotes is re-derived from the files —
   declarations and arrays from `lean/lakefile.lean`, hunks and toolchain rewrites from
   `lean/patches/`, imports and patch lines from `notes/formalization-deps.tsv` — and must
   appear in the page. The patch-size table must equal the TSV row by row, and every name
   list the page prints must equal the computed set.
5. Sync. The page is compared with notes/scripts/render_reports.py's render of it, so prose that
   no count phrase covers cannot drift from the writer's template. The count pass proves the
   numbers are measured; it proves nothing about the sentences around them.

`lean/OAI/**/*.lean` is never scanned here: import counts are read from the TSV, which
`extract_formalization_deps.py` measured. The 122,458-file figure is reconciled against
`notes/formalization-deps.md`, which records it.

--mutant runs the built-in mutations and fails if any goes uncaught, the last of them a prose
row count outside every count phrase -- visible only to pass 5.
"""
import csv
import pathlib
import re
import statistics
import sys
import collections

from catlib import render as RD, yaml as Y
from catlib.paths import LAKEFILE, LAKE_MANIFEST as MANIFEST

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "dependency-drift.md"
TSV = ROOT / "notes" / "formalization-deps.tsv"
PATCHDIR = ROOT / "lean" / "patches"
TOOLCHAIN = ROOT / "lean" / "lean-toolchain"
DEPSMD = ROOT / "notes" / "formalization-deps.md"

SUFFIX = "-lean4341.patch"

ANCHOR = re.compile(r"`([\w./+-]+):(\d+)`")
BARE = re.compile(r"`:(\d+)`")
BLOCKQUOTE = re.compile(r"^> `([\w./+-]+\.\w+):(\d+): (.*)`\s*$")
SPAN = re.compile(r"`([^`\n]+)`")
REQUIRE = re.compile(
    r'^require\s+(?:«(?P<l1>[^»]+)»|(?P<l2>[A-Za-z0-9_.\-]+))\s+from\s+git\s*\n'
    r'\s*"(?P<url>[^"]+)"\s*@\s*"(?P<commit>[0-9a-f]+)"',
    re.M,
)
CODEISH = ('s!"', '=>', ':=', '--', '(', ')', '#', '"', '<|', '{', '}')
PATHISH = re.compile(r"(\.lean|\.md|\.yaml|\.tsv|\.json|\.patch|\.toml|\.txt)$")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def strip(s):
    """Lakefile labels are written «doc-gen4»; the TSV key is doc-gen4."""
    return s.strip("«»")


def n(x):
    return f"{x:,}"


def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def tsv_rows():
    with TSV.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def requires():
    text = read(LAKEFILE)
    out = []
    for m in REQUIRE.finditer(text):
        line = text[: m.start()].count("\n") + 1
        out.append({
            "label": strip(m.group("l1") or m.group("l2")),
            "url": m.group("url"),
            "commit": m.group("commit"),
            "line": line,
        })
    return out


def array_after(marker, text):
    """Backticked names in the `#[ ... ]` array that starts at `marker`.

    Lean writes a name as `iut with one leading backtick and no closing one, so the
    closing delimiter is whitespace, a comma, or the array's `]`.
    """
    i = text.index(marker)
    j = text.index("]", i)
    names = [strip(s) for s in re.findall(r"`([^\s`,\]]+)", text[i:j])]
    start = text[:i].count("\n") + 1
    end = text[:j].count("\n") + 1
    return names, start, end


def patch_info():
    out = {}
    for p in sorted(PATCHDIR.glob("*.patch")):
        lines = read(p).split("\n")
        heads = [i for i, ln in enumerate(lines) if ln.startswith("diff --git ")]
        files = []
        for i in heads:
            tail = lines[i].split()[-1]
            files.append(tail[2:] if tail.startswith("b/") else tail)
        froms, tos = [], []
        for k, i in enumerate(heads):
            end = heads[k + 1] if k + 1 < len(heads) else len(lines)
            if not files[k].endswith("lean-toolchain"):
                continue
            for ln in lines[i:end]:
                if "leanprover/lean4:" not in ln:
                    continue
                ver = ln.split("leanprover/lean4:")[-1].strip()
                if ln.startswith("-"):
                    froms.append(ver)
                elif ln.startswith("+"):
                    tos.append(ver)
        out[p.name] = {
            "lines": len(read(p).splitlines()),
            "hunks": len(heads),
            "files": files,
            "toolchain": any(f.endswith("lean-toolchain") for f in files),
            "lakefile": any(re.search(r"(^|/)lakefile\.\w+$", f) for f in files),
            "froms": froms,
            "tos": tos,
        }
    return out


def yaml_order_violations(imports_by_key):
    """Positions where formalization.yaml's stated ordering fails.

    The comment above related_formalizations: claims the list is ordered by direct import
    count; a violation is an entry whose measured count exceeds the entry above it. Same
    rule as extract_formalization_deps.yaml_order_violations, fed from the TSV.
    """
    lines = Y.yaml_lines(tolerant=True)
    start = lines.index("related_formalizations:")
    urls = []
    for ln in lines[start + 1:]:
        if ln and not ln.startswith(" "):
            break
        m = re.match(r"\s+-\s+id:\s*(\S+)", ln)
        if m:
            urls.append(m.group(1))
    out, prev = [], None
    for i, url in enumerate(urls, start=1):
        last = url.rstrip("/").split("/")[-1]
        if last.endswith(".git"):
            last = last[: -len(".git")]
        key = re.sub(r"[0-9]+$", "", re.sub(r"[^a-z0-9]", "", last.lower()))
        for suffix in ("lean4", "lean"):
            if key.endswith(suffix) and len(key) > len(suffix):
                key = key[: -len(suffix)]
                key = re.sub(r"[0-9]+$", "", key)
                break
        cnt = imports_by_key.get(key)
        if cnt is None:
            continue
        if prev is not None and cnt > prev[1]:
            out.append((i, last, cnt, prev[2], prev[1]))
        prev = (i, cnt, last)
    return out


def measure():
    rows = tsv_rows()
    declared = [r for r in rows if r["lakefile_declared"] == "y"]
    for r in declared:
        r["imports"] = int(r["direct_imports"])
        r["plines"] = int(r["patch_lines"])
        r["name"] = strip(r["library"])
    lake = requires()
    patches = patch_info()
    lake_text = read(LAKEFILE)
    pre, pre_start, pre_end = array_after("preResolutionPatchNames : Array Lean.Name := #[", lake_text)
    post, post_start, post_end = array_after("for name in #[", lake_text)
    by_name = {r["name"]: r for r in declared}
    zero = sorted(r["name"] for r in declared if r["imports"] == 0)
    patched = sorted(r["name"] for r in declared if r["patch_file"] != "none")
    froms = collections.Counter()
    for info in patches.values():
        froms.update(info["froms"])
    imports_by_key = {}
    for r in declared:
        last = r["repo_url"].rstrip("/").split("/")[-1]
        if last.endswith(".git"):
            last = last[: -len(".git")]
        key = re.sub(r"[0-9]+$", "", re.sub(r"[^a-z0-9]", "", last.lower()))
        for suffix in ("lean4", "lean"):
            if key.endswith(suffix) and len(key) > len(suffix):
                key = key[: -len(suffix)]
                key = re.sub(r"[0-9]+$", "", key)
                break
        imports_by_key[key] = r["imports"]
    import json
    manifest = json.loads(read(MANIFEST))
    names = {p["name"].strip("«»") for p in manifest["packages"]}
    return {
        "rows": rows,
        "declared": declared,
        "lake": lake,
        "patches": patches,
        "pre": pre,
        "pre_span": (pre_start, pre_end),
        "post": post,
        "post_span": (post_start, post_end),
        "by_name": by_name,
        "zero": zero,
        "patched": patched,
        "zero_nopatch": sorted(r["name"] for r in declared if r["imports"] == 0 and r["patch_file"] == "none"),
        "nopatch": sorted(r["name"] for r in declared if r["patch_file"] == "none"),
        "lana": sorted(r["name"] for r in declared if "lana-agents/" in r["repo_url"]),
        "last_block": [r["label"] for r in lake if r["line"] >= 73],
        "total_lines": sum(p["lines"] for p in patches.values()),
        "total_hunks": sum(p["hunks"] for p in patches.values()),
        "tc_patches": sum(1 for p in patches.values() if p["toolchain"]),
        "lake_patches": sum(1 for p in patches.values() if p["lakefile"]),
        "froms": froms,
        "tos": {v for p in patches.values() for v in p["tos"]},
        "median_import": statistics.median([r["plines"] for r in declared if r["imports"] > 0]),
        "median_zero": statistics.median([r["plines"] for r in declared if r["imports"] == 0]),
        "violations": yaml_order_violations(imports_by_key),
        "manifest_pkgs": len(names),
        "transitive": sorted(names - {r["name"] for r in declared}),
        "lake_lines": len(read(LAKEFILE).splitlines()),
        "toolchain": read(TOOLCHAIN).splitlines()[0],
    }


def table_rows(text):
    """(name, imports, patch lines) for the patch-size table."""
    rows = []
    for _m in re.finditer(r"^\| ([\w.-]+) \| (\*?\*?)(\d+)\2? \| (\*?\*?)([\d,]+)\2? \|$", text, re.M):
        pass
    for ln in text.split("\n"):
        if not ln.startswith("| ") or ln.startswith("|---"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != 3:
            continue
        if not re.fullmatch(r"\**\d+\**", cells[1]) or not re.fullmatch(r"\**[\d,]+\**", cells[2]):
            continue
        rows.append((cells[0], int(cells[1].strip("*")), int(cells[2].strip("*").replace(",", ""))))
    return rows


def name_list(text, start_marker, end_marker):
    i = text.index(start_marker) + len(start_marker)
    j = text.index(end_marker, i)
    return [strip(s) for s in SPAN.findall(text[i:j])]


def check(text):
    """-> (problems, summary)"""
    m = measure()
    problems = []
    flat = norm(text)
    lines = text.split("\n")

    # 1. anchors
    tokens = sorted(
        [(t.start(), t.group(1), int(t.group(2))) for t in ANCHOR.finditer(text)]
        + [(t.start(), None, int(t.group(1))) for t in BARE.finditer(text)]
    )
    last_path, n_anchor = None, 0
    for pos, path, line in tokens:
        if path:
            last_path = path
        rel = path or last_path
        n_anchor += 1
        if rel is None:
            problems.append(f"page:{text[:pos].count(chr(10)) + 1}: bare anchor :{line} has no preceding path")
            continue
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist (citing :{line})")
            continue
        total = len(read(f).splitlines())
        if not 1 <= line <= total:
            problems.append(f"anchor {rel}:{line} out of range ({total} lines)")

    # 2. blockquotes
    n_quote = 0
    for i, ln in enumerate(lines):
        q = BLOCKQUOTE.match(ln)
        if not q:
            continue
        rel, at, want_q = q.group(1), int(q.group(2)), q.group(3)
        f = ROOT / rel
        if not f.exists():
            problems.append(f"page:{i + 1}: blockquote file {rel} does not exist")
            continue
        src = read(f).split("\n")
        n_quote += 1
        got = src[at - 1] if 1 <= at <= len(src) else "<past end of file>"
        if norm(got) != norm(want_q):
            problems.append(
                f"page:{i + 1}: blockquote != {rel}:{at}\n"
                f"    want {want_q!r}\n    got  {got!r}")

    # 3. code spans
    corpus = None
    n_span = 0
    for i, ln in enumerate(lines):
        if ln.startswith("> "):
            continue
        for span in SPAN.findall(ln):
            if "…" in span or len(span) < 12 or PATHISH.search(span) or "/" in span:
                continue
            if ANCHOR.fullmatch(span) or BARE.fullmatch(span):
                continue
            if not any(c in span for c in CODEISH) and not (span.endswith(".") and len(span) >= 25):
                continue
            if corpus is None:
                corpus = norm(
                    read(LAKEFILE) + "\n" + "\n".join(Y.yaml_lines(tolerant=True)) + "\n" + read(TSV)
                    + "".join("\n" + read(p) for p in sorted(PATCHDIR.glob("*.patch"))))
            n_span += 1
            if norm(span) not in corpus:
                problems.append(f"page:{i + 1}: code span not found in source: {span[:70]!r}")

    # 4. counts
    def want(label, needle):
        if needle not in flat:
            problems.append(f"count missing from page: {label} -> {needle!r}")

    want("require declarations", f"**{len(m['lake'])}**")
    want("pinned commit length", "**40-char**")
    want("patch files", f"**{len(m['patches'])}**")
    want("patch lines", n(m["total_lines"]))
    want("diff hunks", f"**{m['total_hunks']}**")
    want("declared with no patch", f"**{len(m['nopatch'])}**")
    want("toolchain rewrites", f"**{m['tc_patches']} of {len(m['patches'])}**")
    want("lakefile rewrites", f"**{m['lake_patches']} of {len(m['patches'])}**")
    want("from-versions", f"**{len(m['froms'])}**")
    want("release toolchain", m["toolchain"])
    want("lakefile lines", f"({m['lake_lines']} lines)")
    want("pre-resolution libraries", f"**{len(m['pre'])}**")
    want("post_update libraries", f"**{len(m['post'])}**")
    want("pre-resolution patch lines",
         n(sum(m["by_name"][x]["plines"] for x in m["pre"])))
    want("post_update patch lines",
         n(sum(m["by_name"][x]["plines"] for x in m["post"])))
    want("last-block requires", f"**{len(m['last_block'])}** requires")
    want("last-block unpached",
         f"{len([x for x in m['last_block'] if m['by_name'][x]['patch_file'] == 'none'])} of those {len(m['last_block'])}")
    want("zero-import libraries", f"**{len(m['zero'])} of the {len(m['declared'])}**")
    want("zero-import patched", f"**{len([x for x in m['zero'] if m['by_name'][x]['patch_file'] != 'none'])} of those {len(m['zero'])}")
    want("zero-import unpached", f"the {len(m['zero_nopatch'])} that do not are")
    want("pre ∩ zero", f"All {len(m['pre'])} pre-resolution libraries are in the zero-import set")
    want("post ∩ zero", f"and {len(set(m['post']) & set(m['zero']))} of the {len(m['post'])}")
    want("median patched+imported", n(int(m["median_import"])))
    want("median zero-import", n(int(m["median_zero"])))
    want("yaml ordering violations", f"{len(m['violations'])} entries violate")
    want("manifest packages", f"({m['manifest_pkgs']} resolved packages)")
    want("transitive-only packages", f"{len(m['transitive'])} transitive-only")
    want("declared with imports", f"{len(m['declared']) - len(m['zero'])} with direct imports")
    singletons = [v for v, c in m["froms"].items() if c == 1]
    for ver, cnt in sorted(m["froms"].items(), key=lambda kv: -kv[1]):
        want(f"from-version {ver}", f"`{ver}` ×{cnt}" if cnt > 1 else f"`{ver}`")
    if singletons:
        want("singleton from-versions", "and one each of")
    for name, needle in [("largest patch", "PrimeNumberTheoremAnd at 39,904 lines"),
                         ("mathlib imports", "mathlib at 56,416"),
                         ("largest unused patch", "AINTLIB at 23,288 lines"),
                         ("source files", "122,458-file"),
                         ("patch lines per source file", "1.3 lines of patch")]:
        want(name, needle)

    # 4b. figures the page takes from the deps record, not from these files
    depsmd = norm(read(DEPSMD))
    for needle in ["122,458", "56,416"]:
        if needle not in depsmd:
            problems.append(f"deps record does not record {needle}")

    # 4c. arithmetic the page asserts — the denominator is read from the deps record,
    # so a re-measured source-file count moves the bar instead of desyncing from it.
    m_src = re.search(r"OAI/\*\*/\*\.lean` \((\d[\d,]*) files\)", depsmd)
    if not m_src:
        problems.append("PROBLEM deps record does not state its source-file count")
        src_files = 0
    else:
        src_files = int(m_src.group(1).replace(",", ""))
    ratio = round(m["total_lines"] / src_files, 1) if src_files else -1
    if f"{ratio} lines of patch" not in flat:
        problems.append(f"patch-per-source ratio is {ratio}, page says otherwise")

    # 5. patch-size table
    tbl = table_rows(text)
    want("patch-size table rows", "| Library | Direct imports | Patch lines |")
    if len(tbl) != len(m["patched"]):
        problems.append(f"patch-size table has {len(tbl)} rows, TSV has {len(m['patched'])} patched libraries")
    seen = {r[0] for r in tbl}
    for name in m["patched"]:
        if name not in seen:
            problems.append(f"patch-size table omits {name}")
    for name in seen:
        if name not in set(m["patched"]):
            problems.append(f"patch-size table names {name}, which ships no patch")
    for name, imports, plines in tbl:
        row = m["by_name"].get(name)
        if row is None:
            continue
        if imports != row["imports"]:
            problems.append(f"table {name}: imports {imports} != TSV {row['imports']}")
        if plines != row["plines"]:
            problems.append(f"table {name}: patch lines {plines} != TSV {row['plines']}")
    ordered = [p for _, _, p in tbl]
    if ordered != sorted(ordered, reverse=True):
        problems.append("patch-size table is not ordered by descending patch lines")

    # 6. name lists
    lists = [
        ("zero-import list", "`direct_imports = 0`:", "ship a patch", m["zero"]),
        ("zero-import unpached list", f"the {len(m['zero_nopatch'])} that do not",
         ".", m["zero_nopatch"]),
    ]
    for label, a, b, computed in lists:
        try:
            got = name_list(text, a, b)
        except ValueError:
            problems.append(f"name list {label}: markers not found")
            continue
        if sorted(got) != sorted(computed):
            problems.append(
                f"name list {label} != computed: missing {sorted(set(computed) - set(got))} "
                f"extra {sorted(set(got) - set(computed))}")
    for label, names in [
        ("post ∩ zero", sorted(set(m["post"]) & set(m["zero"]))),
        ("last-block requires", m["last_block"]),
        ("from-versions", sorted(m["froms"])),
        ("yaml ordering violations", [v[1] for v in m["violations"]]),
    ]:
        missing = [x for x in names if x not in text]
        if missing:
            problems.append(f"{label} not named in page: {missing}")

    # 7. prose tied to structure
    checks = len([ln for ln in lines if ln.startswith("| The ") and ln.count("|") == 4])
    if "six checks" not in flat:
        problems.append("prose does not say 'six checks'")
    if checks != 6:
        problems.append(f"drift table has {checks} check rows, prose says six")
    if "no build was attempted" not in flat:
        problems.append("page does not state that no build was attempted")
    if "unmeasurable without" not in flat:
        problems.append("page does not mark transitive imports unmeasurable without lake")

    sync = RD.sync_problems(PAGE, text)
    problems.extend(sync)
    return problems, (len(tokens), n_quote, n_span, len(tbl), len(sync))


MUTANTS = {
    "blockquote paraphrased as a quote": lambda t: t.replace(
        "compatibility patch was lost during dependency resolution.",
        "compatibility patch was lost by dependency resolution.", 1),
    "anchor out of range": lambda t: t.replace(
        "`lean/lakefile.lean:10`–`:86`", "`lean/lakefile.lean:10`–`:486`", 1),
    "table row count shifted": lambda t: t.replace(
        "| PrimeNumberTheoremAnd | 244 | 39,904 |", "| PrimeNumberTheoremAnd | 244 | 39,905 |", 1),
    "name dropped from the zero-import list": lambda t: t.replace(
        "`oka`, `orbicurve-cores`,", "`oka`,", 1),
    "patch-line total shifted": lambda t: t.replace("160,187", "160,186"),
    "phase count shifted": lambda t: t.replace(
        "| **11** | **6,658** |", "| **10** | **6,658** |", 1),
    "ordering-violation count shifted": lambda t: t.replace(
        "and 5 entries violate it", "and 6 entries violate it", 1),
    "code span paraphrased": lambda t: t.replace(
        "`s!\".{plan.label}-bootstrap-{pid}-{stamp}\"`",
        "`s!\".{label}-bootstrap-{pid}-{stamp}\"`", 1),
    "table row dropped": lambda t: t.replace(
        "| orbicurve-cores | **0** | 695 |\n", "", 1),
    # Prose no count phrase reads: the deps-record row count in the opening sources sentence.
    # Only the render diff can see it.
    "prose row count": lambda t: t.replace("`notes/formalization-deps.tsv` (31 rows, 8 fields)",
                                            "`notes/formalization-deps.tsv` (32 rows, 8 fields)", 1),
}


def main():
    text = PAGE.read_text(encoding="utf-8", errors="replace")

    if "--mutant" in sys.argv:
        uncaught = []
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"mutant target absent: {name}")
                uncaught.append(name)
                continue
            problems, _ = check(mutated)
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}")
        raise SystemExit(1 if uncaught else 0)

    problems, (n_anchor, n_quote, n_span, n_table, n_sync) = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    m = measure()
    print(f"\nanchors {n_anchor}  blockquotes {n_quote}  checked code spans {n_span}"
          f"  table rows {n_table}  sync problems {n_sync}  problems {len(problems)}")
    print(f"declared {len(m['declared'])}  patched {len(m['patched'])}"
          f"  patch lines {n(m['total_lines'])}  hunks {m['total_hunks']}"
          f"  toolchain patches {m['tc_patches']}  from-versions {len(m['froms'])}")
    print(f"pre {len(m['pre'])}  post {len(m['post'])}  disjoint {set(m['pre']).isdisjoint(m['post'])}"
          f"  union==patched {set(m['pre']) | set(m['post']) == set(m['patched'])}"
          f"  lana==pre {set(m['lana']) == set(m['pre'])}")
    print(f"zero-import {len(m['zero'])}  zero unpached {len(m['zero_nopatch'])}"
          f"  median imported {n(int(m['median_import']))}  median zero {n(int(m['median_zero']))}"
          f"  yaml violations {len(m['violations'])}")
    raise SystemExit(1 if problems else 0)


main()

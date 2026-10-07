#!/usr/bin/env python3
"""Verify notes/index-design.md against the tree it describes.

Report-only; writes nothing. Three passes over the page:

1. Anchors. Every `path:line` anchor must name a file that exists and a line inside it. Any
   backticked path:line shape is checked, not just the extensions this page happens to use, so a
   mistyped extension fails instead of being skipped. A fenced block is attributed to the nearest
   preceding anchor (scanning back up to 8 lines) and every block line must match that file at
   consecutive line numbers.
2. Counts. Every bold count on the page is checked by matching the exact phrase the page must
   contain, built from notes/scripts/measure_index_sizes.population(). A count the page states in
   prose, not in a phrase listed here, is not verified by this script.
3. Byte sizes. The five measured TSV sizes are re-read from disk and compared with the values the
   page's SIZES-derived phrases quote.

Whitespace runs are collapsed on both sides of every comparison: line-wrapping in the page is
markup, not part of the text (see the ruling recorded for the summaries pages).

--mutant runs the built-in mutations and fails if any goes uncaught.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import measure_index_sizes as M  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "index-design.md"

ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json|tsv|yaml)):(\d+)`")
# Any backticked path:line shape, so a mistyped extension is a failure and not a skip.
ANCHOR_SHAPE = re.compile(r"`([\w./+-]+?\.[A-Za-z][A-Za-z0-9]{0,4}):(\d+)`")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def count_phrases(p):
    """Exact phrases the page must contain for each bold count to be honest."""
    n, e, rb = f"{p['nodes']:,}", f"{p['edges_resolved']:,}", f"{p['edges_rawbib']:,}"
    lf, be = f"{p['lean_files']:,}", f"{p['bib_entries']:,}"
    sf, tex = f"{p['sf_rows']:,}", f"{p['tex_files']:,}"
    setb, rawkib = f"{p['ledger_set_bytes']:,}", f"{p['rawbib_kib']:,}"
    fam, man, disc = p["families"], p["manuscripts"], p["disciplines"]
    return [
        # node table
        (f"| Families | **{fam}** |", "families node count"),
        (f"| Manuscripts | **{man}** |", "manuscripts node count"),
        (f"| Catalog disciplines | **{disc}** |", "catalog discipline count"),
        (f"| Preprint dirs | **{p['preprint_dirs']}** |", "preprint dir count"),
        (f"| `.tex` files under `preprints/` | **{tex}** |", "tex file count"),
        (f"| `.bib` files / entries | **{p['bib_files']}** / **{be}** |", "bib file/entry counts"),
        (f"| Lean discipline dirs | **{p['lean_disc']}** |", "lean discipline dir count"),
        (f"| Lean module dirs | **{p['lean_mods']}** |", "lean module dir count"),
        (f"| `.lean` files | **{lf}** |", "lean file count"),
        (f"| Comparator configs | **{p['chal_json']}** | "
         f"`lean/ComparatorChallenges/*.json`, matched by **{p['chal_lean']}** `.lean` |",
         "comparator config counts"),
        (f"| Scope notes | **{p['scope_notes']}** |", "scope note count"),
        (f"| `main_results` entries / configs | **{p['mr_entries']}** / **{p['mr_configs']}** |",
         "main_results entry/config counts"),
        (f"| Lean files / dirs named by the yaml | **{p['mr_files']}** / **{p['mr_dirs']}** |",
         "yaml-named file/dir counts"),
        (f"| Reasoning traces | **{p['traces']}** in **{p['trace_files']}** files |",
         "trace file/trace counts"),
        (f"| Verification dirs | **{p['ver_dirs']}** over **{p['ver_fams']}** families |",
         "verification dir/family counts"),
        # edge table
        (f"| family → manuscript | **{p['e_fam_man']}** |", "family-manuscript edge count"),
        (f"| family → discipline | **{p['e_fam_disc']}** |", "family-discipline edge count"),
        (f"| manuscript → formalized | **{p['formalized']}** |", "formalized manuscript count"),
        (f"| family → config | **{p['fam_cfg_occ']}** occurrences over **{p['fam_cfg_distinct']}** "
         f"distinct configs in **{p['fam_cfg_fams']}** families |", "family-config edge counts"),
        (f"| config → declaration | **{p['mr_entries']}** |", "config-declaration edge count"),
        (f"| family → Lean file | **{p['reach']}** families |", "family-lean reach count"),
        (f"| manuscript → corpus manuscript | **{p['resolved']}** resolved "
         f"(**{p['cross']}** cross-family) | from **{p['bib_hrefs']}** bib hrefs |",
         "citation edge counts"),
        (f"| subfindings rows | **{sf}** = **{p['sf_man']}** manuscript + "
         f"**{p['sf_comp']}** comparator |", "subfindings row counts"),
        # totals
        (f"Totals: **{n}** index nodes (excluding the **{lf}** `.lean` files) and "
         f"**{e}** edges, or **{rb}**", "population totals"),
        (f"The measured population is **{n}** nodes and **{e}** edges", "store-section totals"),
        (f"carries **{sf}** rows at **{p['sf_bpr']:.1f}** B/row", "subfindings bytes per row"),
        (f"the whole ledger set is **{setb}** B", "ledger set byte total"),
        (f"(**{p['builds_on']}** `builds-on` declarations at `lean/formalization.yaml:822`)",
         "builds-on declaration count"),
        # granularity
        (f"**{fam}** family pages, and no per-manuscript pages", "page count decision"),
        (f"a family carries a maximum of **{p['max_paps']}** manuscripts, **{p['fams_1']}** "
         f"families carry exactly **1**, and **{p['fams_2']}** carry two or more",
         "manuscripts-per-family distribution"),
        (f"a table of at most {p['max_paps']} rows", "table row bound"),
        (f"keyed by manuscript (**{p['sf_man']}** rows) and comparator link "
         f"(**{p['sf_comp']}** rows)", "subfindings key counts"),
        # topic vocabulary
        (f"family → MSC code **{p['msc_hits']}** hits over **{p['msc_scanned']:,}** files scanned",
         "MSC hit count"),
        (f"bibliography entry → `keywords` field **{p['bib_kw']}** over **{be}** entries",
         "bib keywords count"),
        (f"manuscript → `\\keywords` macro **{p['kw_dirs']}** of **{man}** "
         f"(**{p['kw_pct']:.1f}%**)", "keywords macro share"),
        (f"**{disc}** catalog disciplines against **{p['lean_disc']}** Lean discipline dirs",
         "grouping counts"),
        (f"the triples name **{p['mr_dirs']}** module dirs, and the declaration namespace equals "
         f"the file's module dir in only **{p['ns_agree']}** of **{p['mr_entries']}** entries",
         "namespace agreement count"),
        (f"A name-based guess is wrong **{p['mr_entries'] - p['ns_agree']}** times out of "
         f"**{p['mr_entries']}**", "namespace disagreement count"),
        (f"with **{p['msc_hits']}** MSC codes and **{p['bib_kw']}** `keywords` fields",
         "derived-vocabulary rejection basis"),
        # schema tables
        (f"`families.tsv` | **{fam}**", "families.tsv rows"),
        (f"`manuscripts.tsv` | **{man}**", "manuscripts.tsv rows"),
        (f"`configs.tsv` | **{p['chal_json']}**", "configs.tsv rows"),
        (f"`lean-dirs.tsv` | **{p['lean_mods']}**", "lean-dirs.tsv rows"),
        (f"`scope-notes.tsv` | **{p['scope_notes']}**", "scope-notes.tsv rows"),
        (f"`traces.tsv` | **{p['traces']}**", "traces.tsv rows"),
        (f"`family-manuscript.tsv` | **{man}**", "family-manuscript.tsv rows"),
        (f"`family-config.tsv` | **{p['chal_json']}**", "family-config.tsv rows"),
        (f"`config-declaration.tsv` | **{p['mr_entries']}**", "config-declaration.tsv rows"),
        (f"`family-lean.tsv` | **{p['reach']}**", "family-lean.tsv rows"),
        (f"`citation.tsv` | **{p['resolved']}** | manuscript → corpus manuscript, "
         f"**{p['cross']}** cross-family", "citation.tsv rows"),
        (f"`family-trace.tsv` | **{p['traces']}**", "family-trace.tsv rows"),
        (f"`family-topic.tsv` | **{fam}**", "family-topic.tsv rows"),
        (f"Pages: `notes/index/<discipline>/<NNN>-<name>.md`, **{fam}** of them", "page count"),
        (f"**{be}** rows at the measured **150** B/row is **{rawkib}** KiB",
         "raw-bib projection"),
        (f"subset is **{p['resolved']}** rows (**{p['res_kib']}** KiB)", "resolved-edge projection"),
        # edges the release does not ship
        (f"scope notes: **{p['fam_cfg_occ']}** occurrences, **{p['fam_cfg_distinct']}** distinct "
         f"configs, **{p['fam_cfg_fams']}** families", "scope-note config counts"),
        (f"config → file (yaml: **{p['mr_configs']}** configs, all **{p['cfg_in_both']}** of them "
         f"also named by a scope note), which reaches **{p['reach']}** families",
         "derivable lean reach"),
        (f"The index carries family → Lean file for **{p['reach']}** families; the "
         f"**{p['formalized']}** is a manuscript-level flag", "lean edge scope"),
        (f"**{p['e_fam_disc']}** edges, one per family", "family-discipline join count"),
        # counting traps
        (f"so a substring count of the command name reads {p['substr_disc']} and "
         f"{p['substr_res']}. The brace-qualified substring reads **{p['brace_disc']}** and "
         f"**{p['brace_res']}** only because each definition writes `}}[n]{{` after the name. "
         f"The rule is the command at line start: **{disc}** and **{fam}**",
         "substring vs line-start counts"),
        (f"Traces: **{p['trace_files']}** files, **{p['traces']}** traces", "trace file/trace trap"),
        (f"**{p['sf_comp']}** scope-note link occurrences against **{p['chal_json']}** distinct "
         f"configs: {p['dup_docs']} scope notes link one config twice", "link occurrence gap"),
        # not checked
        (f"projections at **150** B/row", "projection basis"),
        (f"The **{be}** bib entries are counted", "bib entry caveat"),
        (f"The **{p['reach']}**-family Lean reach", "lean reach caveat"),
        (f"The **{p['ns_agree']}** of **{p['mr_entries']}** namespace agreement",
         "namespace caveat"),
        (f"Whether the **{p['lean_disc']}** Lean discipline dirs align with the **{disc}** catalog "
         f"disciplines", "grouping caveat"),
        (f"superseded by the measured **{n}** and **{rb}**", "superseded estimate"),
    ]


def size_phrases(p):
    """The measured TSV sizes the page's byte figures are projections from."""
    out = []
    for name, (size, rows) in p["sizes"].items():
        out.append((f"| `{name}` | **{size}** | **{rows}** |", f"{name} measured size"))
    return out


def check(text):
    problems = []
    lines = text.split("\n")
    flat = norm(text)
    n_anchor = n_block_lines = 0

    for m in ANCHOR_SHAPE.finditer(text):
        rel, at = m.group(1), int(m.group(2))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist")
            continue
        src = f.read_text(encoding="utf-8", errors="replace").split("\n")
        n_anchor += 1
        if not 1 <= at <= len(src):
            problems.append(f"anchor {rel}:{at} is outside the file ({len(src)} lines)")

    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            j = i + 1
            blk = []
            while j < len(lines) and not lines[j].lstrip().startswith("```"):
                ln = lines[j]
                blk.append(ln[len(indent):] if ln.startswith(indent) and ln.strip() else ln)
                j += 1
            anchor = None
            for k in range(i - 1, max(i - 9, -1), -1):
                found = ANCHOR.findall(lines[k])
                if found:
                    anchor = (found[-1][0], int(found[-1][1]))
                    break
            if anchor is None:
                problems.append(f"page line {i + 1}: fenced block has no preceding file:line anchor")
            elif not (ROOT / anchor[0]).exists():
                problems.append(f"page line {i + 1}: anchor file {anchor[0]} does not exist")
            else:
                rel, at = anchor
                src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                for k, want in enumerate(blk):
                    got = src[at - 1 + k] if at - 1 + k < len(src) else "<past end of file>"
                    n_block_lines += 1
                    if got != want:
                        problems.append(
                            f"page line {i + 2}: block line {k} != {rel}:{at + k}\n"
                            f"    want {want!r}\n    got  {got!r}")
            i = j + 1
        else:
            i += 1

    p = M.population()
    for phrase, label in count_phrases(p):
        if norm(phrase) not in flat:
            problems.append(f"count mismatch ({label}): page does not contain {phrase!r}")
    for phrase, label in size_phrases(p):
        if norm(phrase) not in flat:
            problems.append(f"size mismatch ({label}): page does not contain {phrase!r}")

    return problems, n_anchor, n_block_lines, len(count_phrases(p)) + len(size_phrases(p))


MUTANTS = {
    "anchor line shifted": lambda t: t.replace("`lean/formalization.yaml:922`",
                                              "`lean/formalization.yaml:921`", 1),
    "anchor file renamed": lambda t: t.replace("`lean/formalization.yaml:927`",
                                               "`lean/formalization.yml:927`", 1),
    "block line altered": lambda t: t.replace("      declaration: OAI.GAD.main",
                                              "      declaration: OAI.AmplitudeDamping.main", 1),
    "count altered": lambda t: t.replace("**2,529** index nodes", "**2,700** index nodes", 1),
    "derived count altered": lambda t: t.replace("is wrong **139** times", "is wrong **138** times",
                                                 1),
    "links value altered": lambda t: t.replace("**396** resolved", "**397** resolved", 1),
    "abbreviated anchor": lambda t: t.replace("`overview.tex:28`", "`.../overview.tex:28`", 1),
    "substring-rule count altered": lambda t: t.replace("of the command name reads 18 and",
                                                        "of the command name reads 17 and", 1),
    "projected size altered": lambda t: t.replace("**1,893** KiB", "**1,800** KiB", 1),
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
            problems, _, _, _ = check(mutated)
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}")
        raise SystemExit(1 if uncaught else 0)

    problems, n_anchor, n_block_lines, n_phrases = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"\nanchors {n_anchor}  block lines {n_block_lines}  count phrases {n_phrases}"
          f"  problems {len(problems)}")
    raise SystemExit(1 if problems else 0)


main()

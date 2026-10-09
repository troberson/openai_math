#!/usr/bin/env python3
"""Verify every count and quotation in notes/findings.md. Writes nothing.

The page is a synthesis, so its claims arrive in three kinds and each needs a different check:

  Pass A (sources)   - the Sources table names files that exist, declares the line count they have,
                       every row is cited, and the body's [Sn] markers are contiguous and in
                       first-use order.
  Pass B (quotes)    - every quotation adjacent to a line anchor must appear, markup aside, on the
                       lines it cites. An anchor proves a line exists; it proves nothing about text.
  Pass C (ledger)    - the ledger counts are re-derived by importing build_catalog's parse functions
                       and rebuilding every row. main() is never called: it writes notes/catalog.tsv.
  Pass D (tables)    - the TSV and on-disk counts are re-measured from the shipped files.
  Pass E (reports)   - the fast extractors run as subprocesses; each report line the page quotes must
                       read the same in the report and in the page.
  Pass F (records)   - a count quoted from a record must appear in that record. This proves the page
                       cites the measurement, not that the measurement is right.
  Pass G (closing)   - the page closes with a "Not checked" section and carries no preamble, per the
                       repo rules.

--mutant corrupts one real quotation, cites a real quotation to a neighbouring line, invents a
quotation, changes a ledger count, deletes a Sources row, and ages a Sources line count, asserting
each is flagged while the real page stays clean.

Usage: python3 notes/scripts/verify_findings.py
       python3 notes/scripts/verify_findings.py --mutant
"""
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

from catlib import yaml as Y
from catlib.ledger import counterex_broad, resolves_named, shapes_of, tier_of, versions_of
from catlib.overview import parse_contents, parse_overview
from catlib.paths import (COMPARATOR_DIR, INDEX_DIR, NOTES, PREPRINTS, REASONING_TRACES, ROOT,
                          SCRIPTS, SUMMARIES_DIR)
from catlib.text import strip_markup
from catlib.tsv import read_rows

PAGE = NOTES / "findings.md"
TRACES = REASONING_TRACES
INDEX = INDEX_DIR

SRCROW = re.compile(r"^\|\s*(S\d+)\s*\|\s*\[`([^`]+)`\]\(([^)]+)\)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*$")
MARKER = re.compile(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]")
# A quotation is a typographic/straight-quoted run or a backticked code span.
SPAN = re.compile(r"[“\"]([^”\"]{8,})[”\"]|`([^`]{8,})`")
# Scanned separately in Pass B: a code-span match can swallow a quotation that opens inside it
# (`` `sorry` … "zero of … `lean/OAI/` …" ``), so the two forms cannot share one alternation.
QUOTE = re.compile(r"[“\"]([^”\"]{8,})[”\"]")
CODE = re.compile(r"`([^`]{8,})`")
PRE_GAP, POST_GAP = 2, 12  # adjacency windows around a marker

# Counts the page takes from a record rather than re-measuring. Each must appear in that record.
RECORD = {
    "S5": ["121 of 242 sections state at least one exclusion", "143 exclusion", "121 state none"],
    "S6": ["233", "94", "144"],
    "S7": ["74", "44", "30", "348", "339", "355", "004"],
    "S8": ["Five families are genuinely conditional", "122,458"],
    "S9": ["0.236", "283", "89", "127", "153"],
    "S11": ["| C | 16 | 29 |", "| R | 46 | 85 |", "| B | 27 | 54 |", "| K | 8 | 20 |",
            "| U | 12 | 17 |", "| O | 2 | 5 |", "| N | 19 | 34 |", "**130** | **244**",
            "86 of these 130", "21 of these 130", "547 of 719", "44 families",
            "134 manuscripts", "93 families, 121 manuscripts", "21 families",
            "34 manuscripts", "the whole body of evidence"],
    "S12": ["**26** of the 27", "`verification = 2`", "**27** families carrying **54** manuscripts"],
    "S13": ["393", "391", "156", "104", "417", "500", "14", "426", "416", "not** typed"],
    "S14": ["**30 dirs over 22 families**", "**12 of 30**", "**18 ship no README**",
            "finite-arithmetic certificate", "counts 4 `INPUTS.md`",
            "counts 2 `verification/COVERAGE.md`"],
    "S16": ["**28**", "**19**", "**9**"],
    "S18": ["30.0", "168.2", "0.965", "0.973", "No ledger column"],
    "S20": ["2,410", "1,609", "271", "101", "**17**"],
    "S21": ["6 of 419", "0 of 197", "225"],
    "S23": ["5,842", "551", "5,291", "9,819", "232"],
    "S24": ["92", "978"],
    "S25": ["109", "94", "62", "47", "18", "51", "49", "203", "10"],
    "S26": ["724", "719", "749", "20,341", "21,288", "21,203", "717", "5"],
    "S27": ["1,033", "66,107"],
    "S28": ["160,187", "734", "v4.34.1", "1.3"],
    "S29": ["277,607", "56,416", "278,523", "56,944", "122,458", "56,702"],
    "S31": ["139", "60", "64", "11", "42", "84", "13", "145",
            "the assistant's training-data prior, not a literature survey"],
}

# (script, report line the page relies on, the page's rendering of it)
REPORTS = [
    ("extract_scope_notes.py", "narrow list: 5 phrases, 5 of 242 docs hit",
     "the 5-phrase narrow list hits **5** of 242"),
    ("extract_scope_notes.py", "broad list: 24 phrases, 44 of 242 docs hit",
     "the 24-phrase broad list hits **44**"),
    ("extract_subfinding_pairs.py", "POPULATION 49 families, 203 manuscripts",
     "**49 families over 203 manuscripts**"),
    ("measure_proof_density.py",
     "proofs per manuscript    counterex_broad  n= 74 AUC=0.356 p=1.22e-04",
     "AUC **0.356**, p **1.22e-04**"),
    ("extract_citations.py", "pairs sharing >=5 titles: 419  same-family 296  cross-discipline 6",
     "6 of 419 pairs at ≥5 shared titles cross a discipline boundary"),
    ("extract_citations.py", "pairs sharing >=10 titles: 197  same-family 173  cross-discipline 0",
     "0 of 197 at ≥10"),
    ("extract_citations.py",
     "listed manuscripts with no .bib: 225 of 719, of which 225 carry an inline thebibliography and 0 carry neither",
     "blind to **225** of 719 manuscripts"),
    ("check_index_links.py", "links extracted        66107", "**66,107** links with **0** broken"),
]


def tsv(rel):
    return read_rows(ROOT / rel)


def run(script):
    """One extractor's stdout. cwd is notes/scripts so its sibling imports resolve."""
    r = subprocess.run([sys.executable, str(SCRIPTS / script)], cwd=SCRIPTS,
                       capture_output=True, text=True, timeout=300, check=False)  # nonzero exits are the finding
    return r.stdout


def ledger():
    """Every catalog.tsv row rebuilt from the shipped files, exactly as build_catalog builds it.

    main() is never called because it writes notes/catalog.tsv; the row construction below is a
    copy of it, so a page count is checked against the generator's own rules, not against a
    paraphrase of them — the rules being catlib's, which the generator itself uses.
    """
    _order, fams = parse_overview()
    fam_paps = parse_contents()
    sources, main_results = Y.parse_yaml()
    docs = Y.parse_docs()
    trace_by_fam, trace_unlisted = Y.parse_traces()
    ver_dirs = {p.parent.name for p in PREPRINTS.glob("*/verification")}
    inputs_dirs = {p.parent.name for p in PREPRINTS.glob("*/INPUTS.md")}
    covmd_dirs = {p.parent.parent.name for p in PREPRINTS.glob("*/verification/COVERAGE.md")}
    summary_fams = {p.name[:3] for p in SUMMARIES_DIR.glob("*/*.md")
                    if re.match(r"^\d{3}-", p.name)}
    rows = {}
    for fam in sorted(fams):
        info = fams[fam]
        all_paths = sorted(set(fam_paps.get(fam, [])) | set(info["tex_paps"]))
        d = docs.get(fam)
        cfgs = d["configs"] if d else []
        in_main = [c for c in cfgs if c in main_results]
        shapes = shapes_of(info["abstract"])
        dirs = {Path(p).parts[-2] for p in all_paths}
        rows[fam] = {
            "tier": tier_of(bool(in_main), bool(cfgs), bool(d)),
            "paps": len(all_paths),
            "paps_form": sum(1 for p in all_paths if p in sources),
            "chal": len(cfgs),
            "mainres": len(in_main),
            "scope": 1 if d else 0,
            "verification": sum(1 for x in dirs if x in ver_dirs),
            "inputs": sum(1 for x in dirs if x in inputs_dirs),
            "covmd": sum(1 for x in dirs if x in covmd_dirs),
            "trace": bool(trace_by_fam.get(fam)),
            "shapes": shapes,
            "conditional": 1 if "conditional" in shapes else 0,
            "named": resolves_named(info["title"], info["abstract"]),
            "cxbroad": counterex_broad(info["title"], info["abstract"]),
            "companion": 1 if re.search(r"\bcompanion", info["abstract"], re.I) else 0,
            "versions": versions_of(all_paths),
            "summary": 1 if fam in summary_fams else 0,
            "paths": all_paths,
        }
    traces = sum(len(v) for v in trace_by_fam.values())
    return rows, traces, set(main_results), ver_dirs, len(inputs_dirs), len(covmd_dirs), \
        len(trace_unlisted), sum(main_results.values()), len(main_results)


def measured():
    """Every number the page states that this repo can re-measure right now."""
    (rows, trace_count, configs, ver_dirs, vinputs, vcov, _trace_extra,
     mainres_entries, mainres_configs) = ledger()
    fams = len(rows)
    tier = Counter(r["tier"] for r in rows.values())
    shapes = Counter(s for r in rows.values() for s in r["shapes"])
    t0 = {f: r for f, r in rows.items() if r["tier"] == "T0"}
    named = {f for f, r in rows.items() if r["named"]}
    res = {f for f, r in rows.items() if "resolution" in r["shapes"]}
    cx = {f for f, r in rows.items() if r["cxbroad"]}
    cxtag = {f for f, r in rows.items() if "counterexample" in r["shapes"]}
    def by_tier(s):
        return Counter(rows[f]["tier"] for f in s)

    sub = tsv("notes/subfindings.tsv")
    mss_rows = [r for r in sub if r["kind"] == "manuscript"]
    comp_rows = [r for r in sub if r["kind"] == "comparator-link"]
    src, links = tsv("notes/sources.tsv"), tsv("notes/links.tsv")
    topics, deps = tsv("notes/topics.tsv"), tsv("notes/formalization-deps.tsv")
    standing = tsv("notes/conjecture-standing.tsv")
    lk = {r["edge"]: r for r in links}
    bib = lk["manuscript->corpus manuscript (bib href)"]["detail"]

    files = sorted(COMPARATOR_DIR.glob("*.lean"))
    sorries = [p.read_text(encoding="utf-8", errors="replace").count("sorry") for p in files]
    bundles = sorted(d for d in (ROOT / "preprints").glob("*/verification"))
    topic_edges = tsv("notes/index/edges/family-topic.tsv")

    # The disk link scan is the source of the page's index-link figure, so it is measured here
    # rather than written as a literal the page has to stay in step with by hand.
    ci = run("check_index_links.py")
    disk_links = int(re.search(r"links extracted\s+(\d+)", ci).group(1))
    disk_broken = int(re.search(r"broken links\s+(\d+)", ci).group(1))

    # The yaml `sources:` list is the only place the release names a formalized manuscript, so the
    # gap between it and the overview's own manuscript list is measured, not quoted.
    yaml_paths = Y.parse_yaml()[0]
    listed = {p for r in rows.values() for p in r["paths"]}
    yaml_extra = sorted(p for p in yaml_paths if p not in listed)

    # Cross-family citation count comes from the links table's own detail field.
    bib_cross = int(re.search(r"(\d+) cross-family", bib).group(1))

    return {
        "fams": fams,
        "cols": len(tsv("notes/catalog.tsv")[0]),
        "tier": tier,
        "shapes": shapes,
        "ge3": sum(1 for r in rows.values() if len(r["shapes"]) >= 3),
        "noshape": sum(1 for r in rows.values() if not r["shapes"]),
        "named": len(named),
        "named_tier": by_tier(named),
        "cx": len(cx),
        "cx_tier": by_tier(cx),
        "cx_mss": sum(1 for r in mss_rows if r["fam"] in cx),
        "union": len(named | res),
        "inter": len(named & res),
        "tagonly": sorted(res - named),
        "colonly": sorted(named - res),
        "cx_tagonly": len(cxtag - cx),
        "cx_flagonly": len(cx - cxtag),
        "cond": sorted(f for f, r in rows.items() if r["conditional"]),
        "mss": sum(r["paps"] for r in rows.values()),
        "form": sum(r["paps_form"] for r in rows.values()),
        "scope": sum(1 for r in rows.values() if r["scope"]),
        "chal": sum(r["chal"] for r in rows.values()),
        "mainres": sum(r["mainres"] for r in rows.values()),
        "configs": len(configs),
        "mainres_fams": sum(1 for r in rows.values() if r["mainres"]),
        "mainres_entries": mainres_entries,
        "mainres_configs": mainres_configs,
        "form_fams": sum(1 for r in rows.values() if r["paps_form"]),
        "fam_diff": sorted({f for f, r in rows.items() if r["mainres"]} -
                           {f for f, r in rows.items() if r["paps_form"]}),
        "yaml_paths": len(yaml_paths),
        "yaml_extra": len(yaml_extra),
        "yaml_extra_name": " ".join(Path(p).parent.name for p in yaml_extra),
        "traces": trace_count,
        "sumfam": sum(1 for r in rows.values() if r["summary"]),
        "summss": sum(r["paps"] for r in rows.values() if r["summary"]),
        "t0": len(t0),
        "t0_mss": sum(r["paps"] for r in t0.values()),
        "t0_named": sum(1 for r in t0.values() if r["named"]),
        "t0_cx": sum(1 for r in t0.values() if r["cxbroad"]),
        "t0_two": sum(1 for r in t0.values() if r["paps"] == 2),
        "unform": sum(r["paps"] - r["paps_form"] for r in rows.values()),
        "companion": sum(1 for r in rows.values() if r["companion"]),
        "versions": sum(1 for r in rows.values() if r["versions"]),
        "proofs": sum(int(r["proofs"]) for r in src),
        "thms": sum(int(r["thms"]) for r in src),
        "comp_rows": len(comp_rows),
        "standing": len(standing),
        "terms": len(topics),
        "assign": sum(int(r["fams"]) for r in topics),
        "nohit": sum(1 for r in topics if int(r["fams"]) == 0),
        "uncovered": fams - len({r["fam"] for r in topic_edges}),
        "pins": sum(1 for r in deps if r["lakefile_declared"] == "y"),
        "patches": sum(1 for r in deps if r["patch_file"] not in ("", "none")),
        "patch_lines": sum(int(r["patch_lines"]) for r in deps if r["patch_lines"]),
        "scope_configs": int(re.search(r"(\d+) distinct configs",
                                       lk["scope note->comparator statement"]["detail"]).group(1)),
        "bib_edges": int(re.search(r"(\d+) resolved edges", bib).group(1)),
        "bib_fams": int(re.search(r"over (\d+) of \d+ families", bib).group(1)),
        "bib_cross": bib_cross,
        "chal_files": len(files),
        "sorry_total": sum(sorries),
        "sorry_files": sum(1 for c in sorries if c),
        "vdirs": len(bundles),
        "vfams": sum(1 for r in rows.values()
                     if {Path(p).parts[-2] for p in r["paths"]} & ver_dirs),
        "vinputs": vinputs,
        "vcov": vcov,
        "trace_files": len([p for p in TRACES.iterdir() if p.is_file()]),
        "index_pages": len(list(INDEX.rglob("*.md"))),
        "disk_links": disk_links,
        "disk_broken": disk_broken,
    }


def needles(m):
    """Every count phrase the page must carry, built from the re-measured values."""
    t, sh, nt, ct = m["tier"], m["shapes"], m["named_tier"], m["cx_tier"]
    return [
        f"{m['fams']} rows over {m['cols']} columns",
        f"T3 {t['T3']} · T2 {t['T2']} · T1 {t['T1']} · T0 {t['T0']}.",
        ("uniform {uniform} · resolution {resolution} · bound {bound} · counterexample "
         "{counterexample} · partial {partial} · classification {classification} · density {density}"
         " · conditional {conditional} · undecidability {undecidability}").format(**sh),
        f"**{m['ge3']} families match ≥3 shapes and {m['noshape']} match none**",
        (f"flags **{m['named']}** families (T3 {nt['T3']} · T2 {nt['T2']} · T1 {nt['T1']} "
         f"· T0 {nt['T0']})"),
        (f"flags **{m['cx']}** (T3 {ct['T3']} · T2 {ct['T2']} · T1 {ct['T1']} · T0 {ct['T0']}) "
         f"over **{m['cx_mss']}** manuscripts"),
        (f"the union is **{m['union']}**, the intersection **{m['inter']}**, the tag-only set "
         f"**{len(m['tagonly'])}** (`{' '.join(m['tagonly'])}`), and the column-only set "
         f"**{len(m['colonly'])}**"),
        f"the tag-only set is **{m['cx_tagonly']}** and the flag-only set is **{m['cx_flagonly']}**",
        " — " + ", ".join(m["cond"]) + ".",
        (f"**{m['form']}** of {m['mss']} manuscripts formalized, **{m['scope']}** scope notes, "
         f"**{m['chal']}** comparator challenges, **{m['mainres_entries']}** `main_results` entries over "
         f"**{m['mainres_configs']}** unique configs reaching **{m['mainres_fams']}** families"),
        f"all {m['scope']} scope notes link at least one config",
        (f"**{m['form_fams']}** families have a formalized manuscript and **{m['mainres_fams']}** "
         f"have a `main_results` entry; the difference is **{len(m['fam_diff'])}** family "
         f"(`{' '.join(m['fam_diff'])}`)"),
        (f"the yaml `sources:` list carries **{m['yaml_paths']}** paths, **{m['yaml_extra']}** of "
         f"them not listed by any family (`{m['yaml_extra_name']}`)"),
        f"The {m['t0']} T0 families carry **{m['t0_mss']}** manuscripts",
        f"flags **{m['t0_named']} of {m['t0']}**",
        f"`counterex_broad` **{m['t0_cx']} of {m['t0']}**",
        f"{m['unform']} of {m['mss']} manuscripts are unformalized",
        f"Within T0, **{m['t0_two']}** families ship exactly two manuscripts",
        (f"The {m['chal_files']} `lean/ComparatorChallenges/*.lean` files carry "
         f"**{m['sorry_total']}** `sorry` occurrences, {m['sorry_files']} of them at least one"),
        (f"**{m['vdirs']}** bundles over **{m['vfams']}** families; **{m['vinputs']}** ship "
         f"`INPUTS.md`, **{m['vcov']}** ship `COVERAGE.md`"),
        f"**{m['traces']}** reasoning traces",
        f"shipping in {m['trace_files']} files",
        (f"**{m['sumfam']}** of {m['fams']} families have a summary page, covering "
         f"**{m['summss']}** manuscripts"),
        (f"**{m['terms']}** terms carry **{m['assign']}** assignments over the {m['fams']} families, "
         f"**{m['uncovered']}** families are uncovered, and **{m['nohit']}** terms have no hit"),
        f"Proof environments total **{m['proofs']:,}**; statement environments total **{m['thms']:,}**",
        f"the comparator-table figure **{m['comp_rows']}**",
        f"carries **{m['standing']}** rows",
        (f"**{m['pins']}** declared library pins, **{m['patches']}** patches over "
         f"**{m['patch_lines']:,}** lines"),
        f"**{m['index_pages']:,}** pages carry **{m['disk_links']:,}** links with "
        f"**{m['disk_broken']}** broken",
        f"the 10-gap against **{m['scope_configs']}**",
        (f"**{m['bib_edges']}** manuscript→manuscript edges over **{m['bib_fams']}** of "
         f"{m['fams']} families, **{m['bib_cross']}** crossing"),
    ]


def sources_rows(lines):
    table = {}
    for ln in lines:
        m = SRCROW.match(ln)
        if m:
            table[m.group(1)] = (m.group(2), m.group(3), int(m.group(4)))
    return table


def check(page):
    """Every problem found in the page. Empty list means the page is clean."""
    problems = []
    lines = page.splitlines()
    flat = re.sub(r"\s+", " ", page)
    body = page.split("## Sources")[0]

    # Pass A - the Sources table.
    table = sources_rows(lines)
    if not table:
        problems.append("no Sources table rows parsed")
    ids = sorted(int(k[1:]) for k in table)
    if ids and ids != list(range(1, len(ids) + 1)):
        problems.append(f"Sources ids are not contiguous S1..S{len(ids)}")
    first_use = []
    for m in MARKER.finditer(body):
        sid = f"S{m.group(1)}"
        if sid not in first_use:
            first_use.append(sid)
    if [int(s[1:]) for s in first_use] != sorted(int(s[1:]) for s in first_use):
        problems.append(f"markers are not in first-use order: {' '.join(first_use)}")
    problems.extend(f"marker {s} cites no Sources row" for s in sorted(set(first_use) - set(table)))
    problems.extend(f"Sources row {s} is never cited in the body" for s in sorted(set(table) - set(first_use)))
    for sid, (shown, link, declared) in sorted(table.items()):
        path = ROOT / shown
        if not path.is_file():
            problems.append(f"{sid}: {shown} does not exist")
            continue
        real = len(path.read_text(encoding="utf-8", errors="replace").splitlines())
        if real != declared:
            problems.append(f"{sid}: declares {declared} lines, {shown} has {real}")
        rel = (PAGE.parent / link).resolve()
        if not rel.is_file():
            problems.append(f"{sid}: link {link} does not resolve to a file")

    # Pass B - anchored quotations. A quotation is attributed to a marker only when it is adjacent:
    # ending just before it (any form) or starting just after it (code span only, the yaml form).
    checked = 0
    for m in MARKER.finditer(flat):
        if not m.group(2):
            continue
        sid, a = f"S{m.group(1)}", int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        if sid not in table:
            continue
        path = ROOT / table[sid][0]
        if not path.is_file():
            continue
        src = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if a < 1 or b > len(src):
            problems.append(f"{sid}:{a}-{b} is outside {table[sid][0]} ({len(src)} lines)")
            continue
        target = strip_markup(" ".join(src[a - 1:b]))
        cand = []
        window = flat[max(0, m.start() - 400):m.start()]
        for sp in QUOTE.finditer(window):
            if len(window) - sp.end() <= PRE_GAP:
                cand.append(sp.group(1))
        if not cand:
            for sp in CODE.finditer(flat[m.end():m.end() + 60]):
                if sp.start() <= POST_GAP:
                    cand.append(sp.group(1))
        if not cand:
            continue  # a prose citation, not a quotation
        checked += 1
        if not any(strip_markup(c) in target for c in cand):
            problems.append(f"{sid}:{a}-{b} carries no quotation found on those lines: "
                            f"{cand[-1][:60]}")
    if checked < 12:
        problems.append(f"only {checked} anchored quotations verified")

    # Passes C, D - re-measured counts must be stated as measured.
    m = measured()
    for n in needles(m):
        if n not in flat:
            problems.append(f"count not stated as measured: {n[:80]}")

    # Pass E - the extractors' own reports.
    outs = {s: run(s) for s in {s for s, _, _ in REPORTS}}
    for script, report, shown in REPORTS:
        if report not in outs[script]:
            problems.append(f"{script} report no longer reads: {report[:60]}")
        if shown not in flat:
            problems.append(f"page does not carry the {script} figure: {shown[:60]}")

    # Pass F - record-quoted counts.
    for sid, ns in RECORD.items():
        if sid not in table:
            problems.append(f"{sid} is not a Sources row")
            continue
        path = ROOT / table[sid][0]
        if not path.is_file():
            continue
        text = re.sub(r"\s+", " ", path.read_text(encoding="utf-8", errors="replace"))
        problems.extend(f"{sid} record does not contain {n!r}" for n in ns if n not in text)

    # Pass G - the closing section and the no-preamble rule.
    headings = [l for l in lines if l.startswith("## ")]
    if not headings or headings[-1].strip() != "## Not checked":
        problems.append("page does not close with a `## Not checked` section")
    after = [l for l in lines[1:] if l.strip()]
    if after and not after[0].startswith("## "):
        problems.append(f"text sits between the title and the first heading: {after[0][:50]}")

    return problems, m, len(table), checked


def main():
    mutant = "--mutant" in sys.argv
    page = PAGE.read_text(encoding="utf-8")
    problems, m, table, quotes = check(page)
    t = m["tier"]
    summary = mutants(page) if mutant else None
    if summary is not None:
        undetected = int(summary.rsplit("undetected mutants:", 1)[1])
        if undetected:
            problems.append(f"{undetected} injected mutants went undetected")
    print(f"page: {PAGE.relative_to(ROOT)}")
    print(f"sources rows {table}, anchored quotations verified {quotes}")
    print(f"families {m['fams']} over {m['cols']} columns | manuscripts {m['mss']} | "
          f"formalized {m['form']} | tiers T3:{t['T3']} T2:{t['T2']} T1:{t['T1']} T0:{t['T0']}")
    print(f"resolves_named {m['named']} | counterex_broad {m['cx']} over {m['cx_mss']} manuscripts | "
          f"conditional {' '.join(m['cond'])} | companion {m['companion']} | versions {m['versions']}")
    print(f"scope notes {m['scope']} | challenges {m['chal']} | main_results "
          f"{m['mainres_entries']} entries over {m['mainres_configs']} configs reaching "
          f"{m['mainres_fams']} families")
    print(f"proofs {m['proofs']} | statements {m['thms']} | comparator rows {m['comp_rows']} | "
          f"index pages {m['index_pages']} | problems {len(problems)}")
    for p in problems:
        print(f"  {p}")
    if summary is not None:
        print()
        print("mutants:")
        print(summary)
    return 0 if not problems else 1


def mutants(page):
    """Six corruptions; each must be flagged, and the real page must stay clean."""
    cases = [
        ("corrupted quotation",
         lambda p: p.replace("Five families are genuinely conditional",
                             "Five families are genuinely conditional-ish", 1), "no quotation"),
        ("quotation cited to the neighbouring line",
         lambda p: p.replace("[S8:7]", "[S8:8]", 1), "no quotation"),
        ("fabricated quotation",
         lambda p: p.replace('"121 of 242 sections state at', '"121 of 242 scope notes state at'),
         "no quotation"),
        ("changed ledger count", lambda p: p.replace("T3 136 · T2 106", "T3 137 · T2 105", 1),
         "count not stated as measured"),
        ("deleted Sources row",
         lambda p: "\n".join(l for l in p.splitlines() if not l.startswith("| S14 |")),
         "cites no Sources row"),
        ("aged Sources line count", lambda p: p.replace("| 897 |", "| 896 |", 1), "declares"),
    ]
    out, undetected = [], 0
    for name, fn, expect in cases:
        got, _, _, _ = check(fn(page))
        hit = [p for p in got if expect in p]
        undetected += 0 if hit else 1
        out.append(f"  {name}: {'detected' if hit else 'UNDETECTED'} ({len(got)} problems)")
    base, _, _, _ = check(page)
    out.append(f"  clean page: {'clean' if not base else 'PROBLEMS'} ({len(base)} problems)")
    out.append(f"undetected mutants: {undetected}")
    return "\n".join(out)


if __name__ == "__main__":
    sys.exit(main())

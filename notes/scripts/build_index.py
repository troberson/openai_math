#!/usr/bin/env python3
"""Render notes/index/: the entry point, one page per family, one per discipline, and the node
and edge tables the pages are rendered from.

Stdlib only. Reads text that ships in this repo plus two generated ledgers; writes only under
notes/index/; never invokes lean, lake, or comparator.

The joins are imported from build_catalog.py, not re-derived: family -> manuscript from
parse_contents() (CONTENTS.md) unioned with the overview.tex links, manuscript -> formalized from
parse_yaml() `sources:`, family -> config from parse_docs() (scope-note links), config ->
declaration + file from the formalization.yaml triples, family -> trace from parse_traces()
(the README.md trace table). The ledger supplies the derived claim-shape columns.

Rules this generator encodes, all of them stated in notes/index-design.md:

- **No manuscript -> Lean edge exists.** `sources:` is a flat list of manuscript paths and
  `main_results:` is a flat list of config/declaration/file triples; nothing joins them. The
  derivable chain is family -> config -> file, which reaches 127 families over 185 triples. The
  162 formalized manuscripts stay a per-manuscript flag, and a family with configs but no
  `main_results` entry renders as *absent*, not as zero.
- **405 configs, 415 link occurrences.** The edge table is keyed per family as a set, so it carries
  405; 7 scope notes link one config twice.
- **10 traces over 11 files.** The Mézard–Parisi trace ships as both `.pdf` and `.tex`.
- **Manuscript ownership is the path component after `preprints`**, never `parts[-2]`.
- **`mainres` counts configs, not declarations**, matching the ledger column; 185 declarations over
  178 configs, so the two differ for 7 configs and the page renders declarations separately.
- **Page filenames are a mechanical slug of the title**, not the hand-shortened names used under
  notes/summaries/. Index pages pair with summary pages by family number, never by filename.
- **Topics come from the curated vocabulary at `notes/topics.tsv`**, measured by
  measure_topics.py, never derived here. A topic is multi-label — a family carries zero or more —
  so it is an added label, not a partition: the 17 catalog disciplines stay the partition.
- **Names come from measure_names.py, and only subject names get a page.** A name is a subject
  when it hits a title layer (family title, manuscript directory, theorem-environment title) or a
  `main_results` declaration name; a name that only appears in prose or as a `.bib` author surname
  is a citation and stays a row in `names.tsv` with no page. Every name page states, per source,
  which layer produced the hit, because a name in a body paragraph is a citation, not a subject.

Slug rule: NFKD-normalize and drop combining marks; rewrite a one- or two-letter accent macro
`\\H{o}` as its argument; drop `$`, apostrophes, and any remaining command name; lowercase; replace
each run of non-alphanumerics with `-`; strip a leading `the-`.
"""
import collections
import csv
import pathlib
import posixpath
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_catalog as B  # noqa: E402
import measure_topics as MT  # noqa: E402
import measure_names as MN  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRE = ROOT / "preprints"
OAI = ROOT / "lean" / "OAI"
CHAL = ROOT / "lean" / "ComparatorChallenges"
DOCS = ROOT / "lean" / "docs"
TRACES = ROOT / "reasoning_traces"
IDX = ROOT / "notes" / "index"
LEDGER = ROOT / "notes" / "catalog.tsv"
SRC = ROOT / "notes" / "sources.tsv"

UP = "../../../"     # notes/index/<discipline>/<page>.md -> repo root

TRIPLE = re.compile(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json\s*\n"
                    r"\s*declaration:\s*(\S+)\s*\n\s*file:\s*(\S+)")
HREF = re.compile(r"\\href\{(https?://[^}]+)\}")
PREPRINT_URL = re.compile(r"/preprints/([^/\\]+)/([A-Za-z0-9_.\-]+\.pdf)")
BIB_ENTRY = re.compile(r"@[A-Za-z]+\s*\{([^,]*),")

FAMILY_COLS = ["fam", "discipline", "disc_slug", "title", "slug", "page", "tier", "paps",
               "paps_form", "chal", "mainres", "decl_count", "scope_note", "scope_chars",
               "verification", "inputs", "covmd", "trace", "shapes", "conditional",
               "resolves_named", "counterex_broad", "companions", "summary", "lean_files",
               "cite_out", "cite_in", "topics"]
MANUSCRIPT_COLS = ["dir", "fam", "pdf", "formalized", "main_tex", "build", "readme",
                   "verification", "inputs", "covmd", "tex", "bib", "proofs", "thms", "page"]
CONFIG_COLS = ["config", "fam", "json", "lean", "theorems", "definitions", "nanoda",
               "decl_count", "declarations", "files", "page"]
LEANDIR_COLS = ["dir", "discipline", "module", "lean_files", "named_by_yaml", "declarations"]
SCOPE_COLS = ["fam", "configs", "paps", "scope_chars", "path", "page"]
TRACE_COLS = ["stem", "fam", "files", "page"]
TOPIC_COLS = ["term", "pattern", "fams", "title", "abstract", "scope", "path", "status", "page"]
NAME_COLS = ["name", "role", "fams", "fam_title_fams", "ms_title_dirs", "env_title_fams",
             "decl", "body_fams", "bib_fams", "cap", "mid", "low", "variants", "page"]
EDGE_TABLES = [
    ("edges/family-manuscript.tsv", ["fam", "dir", "pdf", "formalized"]),
    ("edges/family-config.tsv", ["fam", "config"]),
    ("edges/config-declaration.tsv", ["config", "fam", "declaration", "file", "module_dir"]),
    ("edges/family-lean.tsv", ["fam", "config", "declaration", "file"]),
    ("edges/citation.tsv", ["citing_dir", "citing_fam", "target_dir", "target_fam", "cross"]),
    ("edges/family-trace.tsv", ["fam", "stem", "files"]),
    ("edges/family-topic.tsv", ["fam", "topic", "layers"]),
    ("edges/family-name.tsv", ["fam", "name", "layers"]),
]


def tsv(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def slug(title):
    t = unicodedata.normalize("NFKD", title)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"\\[A-Za-z]{1,2}\{([^{}]*)\}", r"\1", t)
    t = t.replace("$", "").replace("'", "").replace("\u2019", "")
    t = re.sub(r"\\[A-Za-z]+\*?", "", t)
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t[4:] if t.startswith("the-") else t


def disc_slug(discipline):
    return re.sub(r"[^a-z0-9]+", "-", discipline.lower()).strip("-")


def owner(p):
    parts = p.parts
    return parts[parts.index("preprints") + 1]


def base(path):
    return posixpath.basename(path)


def citation_edges(dir2fam, report):
    """manuscript -> corpus manuscript, the rule recorded in notes/links.tsv.

    A `.bib` entry that carries the release marker `OpenAI Math Release` and an `\\href` whose
    `/preprints/<dir>/<file>.pdf` target exists on disk. Deduplicated to a set of dir pairs.
    """
    out = set()
    for p in sorted(PRE.rglob("*.bib")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        d = owner(p)
        for m in BIB_ENTRY.finditer(txt):
            nxt = txt.find("@", m.end())
            body = txt[m.start(): nxt if nxt > 0 else len(txt)]
            if "OpenAI Math Release" not in body:
                continue
            for u in HREF.findall(body):
                mm = PREPRINT_URL.search(u)
                if not mm:
                    continue
                if not (PRE / mm.group(1) / mm.group(2)).exists():
                    report["citation_unresolved"] += 1
                    continue
                if mm.group(1) not in dir2fam or d not in dir2fam:
                    report["citation_unowned"] += 1
                    continue
                out.add((d, mm.group(1)))
    return sorted((a, dir2fam[a], b, dir2fam[b]) for a, b in out)


def write(relpath, text):
    f = IDX / relpath
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def write_tsv(relpath, cols, rows):
    lines = ["\t".join(cols)]
    for r in rows:
        lines.append("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols))
    write(relpath, "\n".join(lines) + "\n")


def row(cells):
    return "| " + " | ".join(str(c).replace("|", "\\|") for c in cells) + " |"


def family_page(r, mans, cfgs, decls, tfiles, challenges, main_results, summary_href,
                summary_label, companions, abstract, topics):
    L = [f"# {r['fam']} — {r['title']}", ""]
    L.append(row(["", ""]))
    L.append("|---|---|")
    L.append(row(["Discipline", f"[{r['discipline']}](../disciplines/{r['disc_slug']}.md)"]))
    L.append(row(["Tier", r["tier"]]))
    L.append(row(["Manuscripts", f"{r['paps']} ({r['paps_form']} formalized at source level)"]))
    L.append(row(["Scope note",
                  f"[`lean/docs/{r['fam']}.md`]({UP}lean/docs/{r['fam']}.md)"
                  if r["scope_note"] == "1" else "—"]))
    L.append(row(["Comparator configs",
                  f"{r['chal']} ({r['mainres']} with a `main_results` declaration)"]))
    L.append(row(["Reasoning trace",
                  " · ".join(f"[{s}]({UP}reasoning_traces/{s}.pdf)" for s in tfiles)
                  if tfiles else "—"]))
    L.append(row(["Verification bundles", r["verification"]]))
    L.append(row(["Cited by / cites", f"{r['cite_in']} in · {r['cite_out']} out"]))
    L.append(row(["Claim shapes", r["shapes"].replace("|", ", ") or "—"]))
    L.append(row(["Topics", " · ".join(f"[{t}](../topics/{t}.md)" for t in topics)
                  if topics else "—"]))
    L.append(row(["Companion families", " · ".join(companions) if companions else "—"]))
    L.append(row(["Summary page",
                  f"[{summary_label}]({UP}{summary_href})" if summary_href else "—"]))
    L.append("")

    L.append("## Manuscripts")
    L.append("")
    L.append(row(["Dir", "PDF", "LaTeX tree", "README", "Formalized", "Main file", "Verification"]))
    L.append("|---|---|---|---|---|---|---|")
    for m in mans:
        L.append(row([
            f"[`{m['dir']}`]({UP}preprints/{m['dir']}/)",
            f"[{base(m['pdf'])}]({UP}{m['pdf']})",
            f"[build/]({UP}preprints/{m['dir']}/build/)",
            f"[README.md]({UP}preprints/{m['dir']}/README.md)",
            "yes" if m["formalized"] == "1" else "no",
            f"[{base(m['main_tex'])}]({UP}preprints/{m['main_tex']})" if m["main_tex"] else "—",
            f"[verification/]({UP}preprints/{m['dir']}/verification/)"
            if m["verification"] == "1" else "—",
        ]))
    L.append("")

    L.append("## Lean")
    L.append("")
    if decls:
        L.append(row(["Config", "Declaration", "File", "Module dir"]))
        L.append("|---|---|---|---|")
        for c, d, f in decls:
            mod = posixpath.dirname(f)
            L.append(row([f"[{c}]({UP}lean/ComparatorChallenges/{c}.json)", f"`{d}`",
                          f"[{base(f)}]({UP}lean/{f})", f"[`{mod}`]({UP}lean/{mod}/)"]))
        L.append("")
        L.append("The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` "
                 "and `main_results:` are two flat lists that nothing joins, so the table above is "
                 "a family-level link and the formalized count above is a manuscript-level flag.")
    else:
        L.append("No `main_results` declaration reaches this family"
                 + (f": its scope note links {r['chal']} comparator "
                    f"config{'' if r['chal'] == 1 else 's'}, none of them in `main_results`."
                    if r["chal"] else ", and no scope note links a comparator config."))
    L.append("")

    L.append("## Comparator configs")
    L.append("")
    if cfgs:
        L.append(row(["Config", "Statement", "Solution", "Theorems", "Definitions", "nanoda",
                      "In `main_results`"]))
        L.append("|---|---|---|---|---|---|---|")
        for c in cfgs:
            L.append(row([f"`{c}`", f"[.json]({UP}lean/ComparatorChallenges/{c}.json)",
                          f"[.lean]({UP}lean/ComparatorChallenges/{c}.lean)",
                          challenges[c]["theorems"], challenges[c]["definitions"],
                          "yes" if challenges[c]["nanoda"] else "no",
                          "yes" if c in main_results else "no"]))
    else:
        L.append("No scope note links a comparator config for this family.")
    L.append("")

    L.append("## Verification bundles")
    L.append("")
    if any(m["verification"] == "1" for m in mans):
        L.append(row(["Dir", "Bundle", "INPUTS.md", "COVERAGE.md"]))
        L.append("|---|---|---|---|")
        for m in mans:
            if m["verification"] == "1":
                L.append(row([f"`{m['dir']}`",
                              f"[verification/]({UP}preprints/{m['dir']}/verification/)",
                              "yes" if m["inputs"] == "1" else "no",
                              "yes" if m["covmd"] == "1" else "no"]))
    else:
        L.append("No `verification/` bundle ships with this family's manuscripts.")
    L.append("")

    L.append("## Abstract (`overview.tex`, verbatim)")
    L.append("")
    L.append(abstract)
    L.append("")
    return "\n".join(L) + "\n"


def discipline_page(discipline, rows):
    tier = collections.Counter(r["tier"] for r in rows)
    L = [f"# {discipline}", ""]
    L.append(f"{len(rows)} families · {sum(r['paps'] for r in rows)} manuscripts · "
             f"{sum(r['paps_form'] for r in rows)} formalized at source level · "
             f"{sum(1 for r in rows if r['scope_note'] == '1')} scope notes · "
             f"{sum(r['chal'] for r in rows)} comparator configs · "
             f"{sum(1 for r in rows if r['trace'])} reasoning traces · "
             f"{sum(r['verification'] for r in rows)} verification bundles")
    L.append("")
    L.append("Tier: " + " · ".join(f"{t} {tier.get(t, 0)}" for t in ("T3", "T2", "T1", "T0")))
    L.append("")
    L.append(row(["Family", "Title", "Tier", "Mss", "Form.", "Scope", "Configs", "Trace"]))
    L.append("|---|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: x["fam"]):
        L.append(row([f"[{r['fam']}](../{r['page']})", r["title"], r["tier"], r["paps"],
                      r["paps_form"], "yes" if r["scope_note"] == "1" else "—", r["chal"],
                      "yes" if r["trace"] else "—"]))
    L.append("")
    return "\n".join(L) + "\n"


def topic_page(term, rec, fams, page_of):
    """One page per vocabulary term: the pattern, its yield by layer, and its families."""
    L = [f"# Topic: {term}", ""]
    L.append(f"{len(rec['families'])} families · pattern `{rec['pattern']}` · hits by layer: "
             f"title {len(rec['title'])} · abstract {len(rec['abstract'])} · "
             f"scope {len(rec['scope'])} · path {len(rec['path'])}")
    L.append("")
    if not rec["families"]:
        L.append("No family matches this pattern. That is a measured statement about the corpus, "
                 "not a defect: the term was proposed, matched, and returned nothing.")
        L.append("")
        return "\n".join(L) + "\n"
    L.append("A family is listed when the pattern hits its title, its abstract, its scope note, "
             "or the Lean file paths reached from its comparator configs. The match is a keyword "
             "floor, not a judgement: read the family page before treating a listing as a claim "
             "about what the result is about.")
    L.append("")
    L.append(row(["Family", "Title", "T", "A", "S", "P"]))
    L.append("|---|---|---|---|---|---|")
    for f in sorted(rec["families"]):
        L.append(row([f"[{f}](../{page_of[f]})", fams[f]["title"],
                      *["yes" if f in rec[k] else "—" for k in ("title", "abstract",
                                                                 "scope", "path")]]))
    L.append("")
    return "\n".join(L) + "\n"


# The six layers a name can hit, and the provenance each one carries. The bead's point:
# a name in a body paragraph is a citation, not a subject, so the four title/declaration
# layers make a page and the two body layers are listed as evidence.
NAME_SOURCES = [
    ("F", "Family title", "title",
     "The release named the family after it — the strongest subject evidence there is."),
    ("M", "Manuscript title", "title",
     "A manuscript directory is named after it, so a manuscript takes it as its subject."),
    ("E", "Theorem title", "title",
     "A statement environment carries it in its optional title, so a theorem is named for it."),
    ("D", "Declaration", "declaration",
     "A `main_results` declaration name contains it, so a formalized statement is named for it."),
    ("b", "Body prose", "body",
     "A capitalized occurrence in manuscript prose — a citation, not a statement of subject."),
    ("B", "Bib author", "body",
     "An author surname in a shipped `.bib` — a citation, not a statement of subject."),
]


def name_page(r, fams, page_of, dir2fam, dir2pdf, cfg2fams):
    """One page per subject name: families by layer, manuscripts, declarations, spellings."""
    name = r["name"]
    ms_fams = {f for f, _ in r["ms_title"]}
    decl_fams = sorted({f for stem, _, _ in r["decl"] for f in cfg2fams.get(stem, ())})
    title_fams = set(r["fam_title_fams"]) | ms_fams | set(r["env_title_fams"]) | set(decl_fams)
    counts = {"F": len(r["fam_title_fams"]), "M": len(ms_fams), "E": len(r["env_title_fams"]),
              "D": len(decl_fams), "b": len(r["body_fams"]), "B": len(r["bib_fams"])}
    L = [f"# Name: {name}", ""]
    L.append(f"{len(r['fams'])} families · subject name · {len(title_fams)} carried by a title "
             f"or a declaration · {len(r['body_fams'])} by prose · {len(r['bib_fams'])} by "
             f"bibliography author")
    L.append("")
    L.append("A name page exists because a **title** layer (a family title in `overview.tex`, a "
             "manuscript directory name, the optional title of a statement environment) or a "
             "`main_results` **declaration** name carries this name. Those hits make it a subject. "
             "The prose and bibliography columns are listed as citation evidence: a body paragraph "
             "that mentions a name says the manuscript cites it, not that the result is about it. "
             "A name that never reaches a title layer has no page — it is a row in "
             "[`../names.tsv`](../names.tsv) with `role = citation`.")
    L.append("")
    L.append(f"Prose counts: {r['cap']} capitalized occurrences, {r['mid']} of them mid-sentence, "
             f"{r['low']} lowercase. The mid-sentence count is what separates a surname from an "
             f"English word; the rule and its measurements live in "
             f"[`notes/names.md`](../../names.md).")
    L.append("")
    L.append("## Provenance by source")
    L.append("")
    L.append(row(["Source", "Layer", "Families", "What a hit means here"]))
    L.append("|---|---|---|---|")
    for flag, src, layer, meaning in NAME_SOURCES:
        L.append(row([f"`{flag}` — {src}", layer, counts[flag], meaning]))
    L.append("")
    L.append("## Families")
    L.append("")
    L.append(row(["Family", "Title", "F", "M", "E", "D", "b", "B"]))
    L.append("|---|---|---|---|---|---|---|---|")
    for f in r["fams"]:
        flags = (f in r["fam_title_fams"], f in ms_fams, f in r["env_title_fams"],
                 f in decl_fams, f in r["body_fams"], f in r["bib_fams"])
        L.append(row([f"[{f}](../{page_of[f]})" if f in page_of else f, fams[f]["title"]]
                     + ["yes" if c else "—" for c in flags]))
    L.append("")

    ms = {}
    for f, d in r["ms_title"]:
        ms.setdefault(d, set()).add("title")
    for d in r["body_ms"]:
        ms.setdefault(d, set()).add("prose")
    L.append("## Manuscripts")
    L.append("")
    if ms:
        L.append(row(["Dir", "Family", "Where the name appears", "PDF"]))
        L.append("|---|---|---|---|")
        for d in sorted(ms):
            f = dir2fam.get(d, "")
            L.append(row([f"[`{d}`]({UP}preprints/{d}/)",
                          f"[{f}](../{page_of[f]})" if f in page_of else "—",
                          " + ".join(sorted(ms[d])),
                          f"[{base(dir2pdf[d])}]({UP}{dir2pdf[d]})" if dir2pdf.get(d) else "—"]))
        L.append("")
        L.append("`title` means the name is in the manuscript directory name; `prose` means it "
                 "appears capitalized in that manuscript's body text with its bibliography "
                 "stripped. A `prose`-only row is a citation.")
    else:
        L.append("No manuscript directory name and no manuscript body paragraph carries this "
                 "name; its hits are the family title, the theorem-environment titles, the "
                 "declaration names, and the bibliography.")
    L.append("")

    L.append("## Lean declarations")
    L.append("")
    if r["decl"]:
        L.append(row(["Config", "Declaration", "File", "Family"]))
        L.append("|---|---|---|---|")
        for stem, d, fp in r["decl"]:
            L.append(row([f"[{stem}]({UP}lean/ComparatorChallenges/{stem}.json)", f"`{d}`",
                          f"[{base(fp)}]({UP}lean/{fp})",
                          " · ".join(f"[{x}](../{page_of[x]})" for x in cfg2fams.get(stem, ()))
                          or "—"]))
    else:
        L.append("No `main_results` declaration name contains this name.")
    L.append("")

    L.append("## Theorem-environment titles")
    L.append("")
    if r["env_hits"]:
        L.append("Up to 8 of the statement-environment titles that carry the name, verbatim with "
                 "accents folded.")
        L.append("")
        L.append(row(["Family", "Environment title"]))
        L.append("|---|---|")
        for f, t in r["env_hits"]:
            L.append(row([f"[{f}](../{page_of[f]})" if f in page_of else "—", t]))
    else:
        L.append("No statement environment carries this name in its optional title.")
    L.append("")

    L.append("## Spelling variants")
    L.append("")
    if len(r["variants"]) > 1:
        L.append("Every form below normalizes to the key `%s`: accents folded, dash variants "
                 "unified, possessives stripped, case lowered. " % name
                 + " · ".join(f"`{v}`" for v in r["variants"]))
    elif r["variants"]:
        L.append("One surface form in prose: `%s`. The normalized key is `%s`."
                 % (r["variants"][0], name))
    else:
        L.append("No capitalized prose occurrence; the key `%s` comes from a title, a "
                 "declaration, or a bibliography author." % name)
    L.append("")
    return "\n".join(L) + "\n"


def main():
    order, fams = B.parse_overview()
    fam_paps = B.parse_contents()
    sources, main_results = B.parse_yaml()
    challenges = B.parse_challenges()
    docs = B.parse_docs()
    trace_by_fam, trace_unlisted = B.parse_traces()
    ledger = {r["fam"]: r for r in tsv(LEDGER)}
    srcrows = {r["dir"]: r for r in tsv(SRC)}
    report = collections.Counter()

    ver_dirs = {p.parent.name for p in PRE.glob("*/verification")}
    inputs_dirs = {p.parent.name for p in PRE.glob("*/INPUTS.md")}
    covmd_dirs = {p.parent.parent.name for p in PRE.glob("*/verification/COVERAGE.md")}
    summary_by_fam = {}
    for p in sorted((ROOT / "notes" / "summaries").glob("*/*.md")):
        if re.match(r"^\d{3}-", p.name):
            summary_by_fam.setdefault(p.name[:3], p)

    triples = sorted(TRIPLE.findall((ROOT / "lean" / "formalization.yaml").read_text(encoding="utf-8")))
    cfg2decls = collections.defaultdict(list)
    for c, d, f in triples:
        cfg2decls[c].append((d, f))
    cfg2fams = collections.defaultdict(set)
    for fam in sorted(docs):
        for c in docs[fam]["configs"]:
            cfg2fams[c].add(fam)

    # family -> manuscript: the same union build_catalog.py writes to the ledger.
    fam_paths = {f: sorted(set(fam_paps.get(f, [])) | set(v["tex_paps"])) for f, v in fams.items()}
    dir2fam = {pathlib.PurePosixPath(p).parts[1]: f for f, ps in fam_paths.items() for p in ps}
    cites_out, cites_in = collections.Counter(), collections.Counter()
    citations = citation_edges(dir2fam, report)
    for _, ff, _, ft in citations:
        cites_out[ff] += 1
        cites_in[ft] += 1

    lean_files_by_fam = collections.defaultdict(set)
    for c, famset in cfg2fams.items():
        for fam in famset:
            for _, f in cfg2decls.get(c, []):
                lean_files_by_fam[fam].add(f)

    mod_dirs = sorted(f"OAI/{d.name}/{m.name}"
                      for d in (p for p in OAI.iterdir() if p.is_dir())
                      for m in (p for p in d.iterdir() if p.is_dir()))
    mod_lean = collections.Counter()
    for p in OAI.rglob("*.lean"):
        rel = p.relative_to(OAI).parts
        if len(rel) >= 2:
            mod_lean[f"OAI/{rel[0]}/{rel[1]}"] += 1
    mod_decls = collections.defaultdict(set)
    for _, d, f in triples:
        mod_decls[posixpath.dirname(f)].add(d)

    page_of = {f: f"{disc_slug(v['discipline'])}/{f}-{slug(v['title'])}.md" for f, v in fams.items()}
    topic_rows = MT.measure()[0]
    topic_by_term = {r["term"]: r for r in topic_rows}
    fam2topics = {f: [r["term"] for r in topic_rows if f in r["families"]] for f in fams}
    pages, links = [], []
    family_rows, manuscript_rows, config_rows, lean_dir_rows, scope_rows, trace_rows = [], [], [], [], [], []
    edges = {name: [] for name, _ in EDGE_TABLES}
    for d1, ff, d2, ft in citations:
        edges["edges/citation.tsv"].append(
            {"citing_dir": d1, "citing_fam": ff, "target_dir": d2, "target_fam": ft,
             "cross": "1" if ff != ft else "0"})

    for fam in sorted(fams):
        info = fams[fam]
        led = ledger[fam]
        ds = disc_slug(info["discipline"])
        page = page_of[fam]
        pages.append(page)
        mans = []
        for p in fam_paths[fam]:
            d = pathlib.PurePosixPath(p).parts[1]
            s = srcrows[d]
            mans.append({
                "dir": d, "fam": fam, "pdf": p,
                "formalized": "1" if p in sources else "0",
                "main_tex": s["main_tex"],
                "build": "1" if (PRE / d / "build").is_dir() else "0",
                "readme": "1" if (PRE / d / "README.md").exists() else "0",
                "verification": "1" if d in ver_dirs else "0",
                "inputs": "1" if d in inputs_dirs else "0",
                "covmd": "1" if d in covmd_dirs else "0",
                "tex": s["tex"], "bib": s["bib"], "proofs": s["proofs"], "thms": s["thms"],
                "page": page,
            })
            edges["edges/family-manuscript.tsv"].append(
                {"fam": fam, "dir": d, "pdf": p, "formalized": mans[-1]["formalized"]})
        manuscript_rows.extend(mans)
        cfgs = docs[fam]["configs"] if fam in docs else []
        decls = [(c, d, f) for c in cfgs for d, f in cfg2decls.get(c, [])]
        for c in cfgs:
            edges["edges/family-config.tsv"].append({"fam": fam, "config": c})
        for c, d, f in decls:
            edges["edges/family-lean.tsv"].append(
                {"fam": fam, "config": c, "declaration": d, "file": f})
        tfiles = sorted(trace_by_fam.get(fam, []))
        for s in tfiles:
            edges["edges/family-trace.tsv"].append(
                {"fam": fam, "stem": s, "files": "|".join(x.name for x in sorted(TRACES.glob(f"{s}.*")))})
        sp = summary_by_fam.get(fam)
        summary_href = f"notes/summaries/{sp.relative_to(ROOT / 'notes' / 'summaries')}" if sp else ""
        companions = [f"[{c}](../{page_of[c]})" for c in led["companions"].split("|")
                      if c and c in fams]
        tier = ("T3" if any(c in main_results for c in cfgs) else
                "T2" if cfgs else "T1" if fam in docs else "T0")
        family_rows.append({
            "fam": fam, "discipline": info["discipline"], "disc_slug": ds,
            "title": info["title"], "slug": slug(info["title"]), "page": page, "tier": tier,
            "paps": len(fam_paths[fam]),
            "paps_form": sum(1 for p in fam_paths[fam] if p in sources),
            "chal": len(cfgs), "mainres": sum(1 for c in cfgs if c in main_results),
            "decl_count": len(decls),
            "scope_note": "1" if fam in docs else "0",
            "scope_chars": docs[fam]["scope_chars"] if fam in docs else 0,
            "verification": sum(1 for m in mans if m["verification"] == "1"),
            "inputs": sum(1 for m in mans if m["inputs"] == "1"),
            "covmd": sum(1 for m in mans if m["covmd"] == "1"),
            "trace": "|".join(tfiles), "shapes": led["shapes"],
            "conditional": led["conditional"], "resolves_named": led["resolves_named"],
            "counterex_broad": led["counterex_broad"], "companions": led["companions"],
            "summary": "1" if sp else "0",
            "lean_files": len(lean_files_by_fam.get(fam, ())),
            "cite_out": cites_out[fam], "cite_in": cites_in[fam],
            "topics": len(fam2topics[fam]),
        })
        write(page, family_page(
            family_rows[-1], mans, cfgs, decls, tfiles, challenges, main_results,
            summary_href, sp.name if sp else "", companions, info["abstract"],
            fam2topics[fam]))
        links.append((page, f"../disciplines/{ds}.md"))
        for t in fam2topics[fam]:
            links.append((page, f"../topics/{t}.md"))
        for m in mans:
            links += [(page, f"{UP}{m['pdf']}"),
                      (page, f"{UP}preprints/{m['dir']}/build/"),
                      (page, f"{UP}preprints/{m['dir']}/README.md")]
            if m["main_tex"]:
                links.append((page, f"{UP}preprints/{m['main_tex']}"))
            if m["verification"] == "1":
                links.append((page, f"{UP}preprints/{m['dir']}/verification/"))
        if fam in docs:
            links.append((page, f"{UP}lean/docs/{fam}.md"))
        for c in cfgs:
            links += [(page, f"{UP}lean/ComparatorChallenges/{c}.json"),
                      (page, f"{UP}lean/ComparatorChallenges/{c}.lean")]
        for _, _, f in decls:
            links += [(page, f"{UP}lean/{f}"), (page, f"{UP}lean/{posixpath.dirname(f)}/")]
        for s in tfiles:
            links.append((page, f"{UP}reasoning_traces/{s}.pdf"))
        if summary_href:
            links.append((page, f"{UP}{summary_href}"))
        for c in companions:
            links.append((page, c.split("](")[1][:-1]))

    for c in sorted(cfg2fams):
        famset = sorted(cfg2fams[c])
        config_rows.append({
            "config": c, "fam": "|".join(famset),
            "json": "1" if (CHAL / f"{c}.json").exists() else "0",
            "lean": "1" if (CHAL / f"{c}.lean").exists() else "0",
            "theorems": challenges[c]["theorems"], "definitions": challenges[c]["definitions"],
            "nanoda": "1" if challenges[c]["nanoda"] else "0",
            "decl_count": len(cfg2decls.get(c, [])),
            "declarations": "|".join(x[0] for x in cfg2decls.get(c, [])),
            "files": "|".join(x[1] for x in cfg2decls.get(c, [])),
            "page": page_of[famset[0]],
        })
    for c, d, f in triples:
        edges["edges/config-declaration.tsv"].append(
            {"config": c, "fam": "|".join(sorted(cfg2fams.get(c, ()))), "declaration": d,
             "file": f, "module_dir": posixpath.dirname(f)})
    for m in mod_dirs:
        _, disc, mod = m.split("/")
        lean_dir_rows.append({"dir": m, "discipline": disc, "module": mod,
                              "lean_files": mod_lean[m],
                              "named_by_yaml": len(mod_decls.get(m, ())),
                              "declarations": "|".join(sorted(mod_decls.get(m, ())))})
    for fam in sorted(docs):
        scope_rows.append({"fam": fam, "configs": len(docs[fam]["configs"]),
                           "paps": len(docs[fam]["paps"]),
                           "scope_chars": docs[fam]["scope_chars"],
                           "path": f"lean/docs/{fam}.md", "page": page_of[fam]})
    stem_fam = {}
    for fam in sorted(trace_by_fam):
        for s in trace_by_fam[fam]:
            stem_fam[s] = fam
    for s in sorted(stem_fam):
        fam = stem_fam[s]
        trace_rows.append({"stem": s, "fam": fam,
                           "files": "|".join(x.name for x in sorted(TRACES.glob(f"{s}.*"))),
                           "page": page_of[fam]})

    by_disc = collections.defaultdict(list)
    for r in family_rows:
        by_disc[r["discipline"]].append(r)
    disc_pages = []
    for discipline in sorted(by_disc):
        ds = disc_slug(discipline)
        write(f"disciplines/{ds}.md", discipline_page(discipline, by_disc[discipline]))
        disc_pages.append(f"disciplines/{ds}.md")
        for r in by_disc[discipline]:
            links.append((f"disciplines/{ds}.md", f"../{r['page']}"))

    topic_pages = []
    topic_table_rows = []
    for r in sorted(topic_rows, key=lambda r: r["term"]):
        page = f"topics/{r['term']}.md"
        write(page, topic_page(r["term"], r, fams, page_of))
        topic_pages.append(page)
        for f in sorted(r["families"]):
            links.append((page, f"../{page_of[f]}"))
        topic_table_rows.append({
            "term": r["term"], "pattern": r["pattern"], "fams": len(r["families"]),
            "title": len(r["title"]), "abstract": len(r["abstract"]),
            "scope": len(r["scope"]), "path": len(r["path"]),
            "status": "assigned" if r["families"] else "negative", "page": page})
    for fam in sorted(fams):
        for t in fam2topics[fam]:
            r = topic_by_term[t]
            edges["edges/family-topic.tsv"].append(
                {"fam": fam, "topic": t, "layers": "".join(
                    c for c, k in (("T", "title"), ("A", "abstract"), ("S", "scope"),
                                   ("P", "path")) if fam in r[k])})

    # ---- names: measured by measure_names.py; only subject names get a page ----
    name_rows, name_meta = MN.measure()
    subject_rows = [r for r in name_rows if r["role"] == "subject"]
    citation_rows = [r for r in name_rows if r["role"] == "citation"]
    name_covered = {f for r in subject_rows for f in r["fams"]}
    trace_fams = set(trace_by_fam)
    dir2pdf = {r["dir"]: r["pdf"] for r in manuscript_rows}
    name_pages = []
    name_table_rows = []
    for r in sorted(name_rows, key=lambda r: r["name"]):
        page = f"names/{r['name']}.md" if r["role"] == "subject" else ""
        if page:
            write(page, name_page(r, fams, page_of, dir2fam, dir2pdf, cfg2fams))
            name_pages.append(page)
            for f in r["fams"]:
                links.append((page, f"../{page_of[f]}"))
            for d in sorted(set([d for _, d in r["ms_title"]] + r["body_ms"])):
                links.append((page, f"{UP}preprints/{d}/"))
                if dir2pdf.get(d):
                    links.append((page, f"{UP}{dir2pdf[d]}"))
            for stem, _, fp in r["decl"]:
                links.append((page, f"{UP}lean/ComparatorChallenges/{stem}.json"))
                links.append((page, f"{UP}lean/{fp}"))
        name_table_rows.append({
            "name": r["name"], "role": r["role"], "fams": len(r["fams"]),
            "fam_title_fams": "|".join(r["fam_title_fams"]),
            "ms_title_dirs": "|".join(d for _, d in r["ms_title"]),
            "env_title_fams": "|".join(r["env_title_fams"]),
            "decl": "|".join(d for _, d, _ in r["decl"]),
            "body_fams": len(r["body_fams"]), "bib_fams": len(r["bib_fams"]),
            "cap": r["cap"], "mid": r["mid"], "low": r["low"],
            "variants": "|".join(r["variants"]), "page": page})
    for r in sorted(name_rows, key=lambda r: r["name"]):
        if r["role"] != "subject":
            continue
        ms_fams = {f for f, _ in r["ms_title"]}
        decl_fams = {f for stem, _, _ in r["decl"] for f in cfg2fams.get(stem, ())}
        for f in r["fams"]:
            edges["edges/family-name.tsv"].append({
                "fam": f, "name": r["name"],
                "layers": "".join(c for c, cond in (
                    ("F", f in r["fam_title_fams"]), ("M", f in ms_fams),
                    ("E", f in r["env_title_fams"]), ("D", f in decl_fams),
                    ("b", f in r["body_fams"]), ("B", f in r["bib_fams"])) if cond)})

    write_tsv("families.tsv", FAMILY_COLS, family_rows)
    write_tsv("manuscripts.tsv", MANUSCRIPT_COLS, manuscript_rows)
    write_tsv("configs.tsv", CONFIG_COLS, config_rows)
    write_tsv("lean-dirs.tsv", LEANDIR_COLS, lean_dir_rows)
    write_tsv("scope-notes.tsv", SCOPE_COLS, scope_rows)
    write_tsv("traces.tsv", TRACE_COLS, trace_rows)
    write_tsv("topics.tsv", TOPIC_COLS, topic_table_rows)
    write_tsv("names.tsv", NAME_COLS, name_table_rows)
    for name, cols in EDGE_TABLES:
        write_tsv(name, cols, edges[name])

    paps_all = [p for f in fams for p in set(fam_paps.get(f, [])) | set(fams[f]["tex_paps"])]
    canon = {"families": len(fams), "manuscripts": len(set(paps_all)), "formalized": len(sources),
             "scope_notes": len(docs), "challenges": len(challenges),
             "traces": len({s for v in trace_by_fam.values() for s in v}), "ver_dirs": len(ver_dirs)}
    rendered = {
        "families": len(family_rows), "manuscripts": len(manuscript_rows),
        "formalized": sum(1 for r in manuscript_rows if r["formalized"] == "1"),
        "scope_notes": len(scope_rows), "challenges": len(config_rows),
        "traces": len(trace_rows),
        "ver_dirs": sum(1 for r in manuscript_rows if r["verification"] == "1"),
    }
    L = ["# The family index", ""]
    L.append(f"Generated by `python3 notes/scripts/build_index.py` — {len(pages)} family pages, "
             f"{len(disc_pages)} discipline pages, {len(topic_pages)} topic pages, this entry "
             f"point, and the node and edge tables the pages are rendered from. Nothing here is "
             f"hand-written: regenerate and diff.")
    L.append("")
    L.append("The schema is decided in [notes/index-design.md](../index-design.md): generated "
             "markdown plus TSV in git, family pages with no manuscript pages, `notes/index/` as "
             "the location, and the curated vocabulary at `notes/topics.tsv` as the topic source.")
    L.append("")
    L.append("## Disciplines")
    L.append("")
    L.append(row(["Discipline", "Families", "Manuscripts", "Formalized", "Scope notes",
                  "Configs", "Traces", "Verification"]))
    L.append("|---|---|---|---|---|---|---|---|")
    for discipline in sorted(by_disc):
        rows = by_disc[discipline]
        L.append(row([f"[{discipline}](disciplines/{disc_slug(discipline)}.md)", len(rows),
                      sum(r["paps"] for r in rows), sum(r["paps_form"] for r in rows),
                      sum(1 for r in rows if r["scope_note"] == "1"),
                      sum(r["chal"] for r in rows), sum(1 for r in rows if r["trace"]),
                      sum(r["verification"] for r in rows)]))
    L.append("")
    L.append("## Topics")
    L.append("")
    L.append(f"Topics are a curated keyword vocabulary in [`notes/topics.tsv`](../topics.tsv) "
             f"(the hand-written source of truth, with the reading verdict for each term in "
             f"[`notes/topics.md`](../topics.md)), measured over four texts per family: title, "
             f"abstract, scope note, and the derived Lean file paths. A family carries zero or "
             f"more topics, so this is a label on top of the discipline partition, not a "
             f"replacement for it. {len(topic_pages)} terms, "
             f"{len(edges['edges/family-topic.tsv'])} assignments, "
             f"{len([r for r in topic_rows if not r['families']])} terms with no hit.")
    L.append("")
    L.append(row(["Topic", "Families", "Title", "Abstract", "Scope", "Path"]))
    L.append("|---|---|---|---|---|---|")
    for r in sorted(topic_rows, key=lambda r: (-len(r["families"]), r["term"])):
        L.append(row([f"[{r['term']}](topics/{r['term']}.md)", len(r["families"]),
                      len(r["title"]), len(r["abstract"]), len(r["scope"]), len(r["path"])]))
    L.append("")
    L.append("## Names")
    L.append("")
    L.append(f"Names are measured over six layers by "
             f"[`notes/scripts/measure_names.py`](../scripts/measure_names.py) and recorded in "
             f"[`notes/names.md`](../names.md): four title layers (family titles, manuscript "
             f"directory names, the optional titles of statement environments, the `main_results` "
             f"declaration names) and two body layers (manuscript prose with the bibliography "
             f"stripped, and the author fields of the shipped `.bib` files). A name is a "
             f"**subject** when a title layer or a declaration carries it and a **citation** when "
             f"only prose or a bibliography does, so only subject names get a page: "
             f"{len(name_pages)} pages in [`names/`](names/) over {len(name_rows)} measured names. "
             f"The other {len(citation_rows)} are bibliography surnames that never reach a title "
             f"layer — rows in [`names.tsv`](names.tsv) with `role = citation`, not pages. "
             f"{len(edges['edges/family-name.tsv'])} family-name edges cover {len(name_covered)} "
             f"of {len(ledger)} families; "
             f"{len(name_rows) - len([r for r in name_rows if r['fams']])} names resolve to no "
             f"family. Each page states, per source, which layer produced the hit: a name in a "
             f"body paragraph is a citation, not a subject.")
    L.append("")
    L.append(row(["Name", "Families", "F", "M", "E", "D", "b", "B"]))
    L.append("|---|---|---|---|---|---|---|---|")
    for r in sorted(subject_rows, key=lambda r: (-len(r["fams"]), r["name"]))[:40]:
        L.append(row([f"[{r['name']}](names/{r['name']}.md)", len(r["fams"]),
                      len(r["fam_title_fams"]), len({f for f, _ in r["ms_title"]}),
                      len(r["env_title_fams"]), len(r["decl"]),
                      len(r["body_fams"]), len(r["bib_fams"])]))
    L.append("")
    L.append("The 40 subject names that reach the most families; "
             "[`names.tsv`](names.tsv) carries all "
             f"{len(name_table_rows)}. Column letters are the layers of the name pages: "
             "`F` family title, `M` manuscript directory, `E` theorem-environment title, "
             "`D` declaration, `b` prose, `B` bib author.")
    L.append("")
    L.append("## Tables")
    L.append("")
    L.append(row(["Table", "Rows", "Key", "What it carries"]))
    L.append("|---|---|---|---|")
    for name, rows_, key, what in (
        ("`families.tsv`", family_rows, "`fam`",
         "One row per catalogued family, with its page path and claim-shape columns."),
        ("`manuscripts.tsv`", manuscript_rows, "preprint dir slug",
         "One row per manuscript: PDF, main file, formalized flag, bundle flags, source counts."),
        ("`configs.tsv`", config_rows, "config stem",
         "One row per comparator config, its family, and its `main_results` declarations."),
        ("`lean-dirs.tsv`", lean_dir_rows, "`OAI/<discipline>/<module>`",
         "One row per Lean module dir, with its `.lean` count and the declarations named there."),
        ("`scope-notes.tsv`", scope_rows, "`fam`",
         "One row per scope note: configs linked, manuscripts linked, `## Scope` length."),
        ("`traces.tsv`", trace_rows, "trace stem",
         "One row per published reasoning trace and the family README.md attributes it to."),
        ("`topics.tsv`", topic_table_rows, "term",
         "One row per curated vocabulary term: its pattern, its yield, its yield by layer, and "
         "its page. The patterns live in `notes/topics.tsv`; this table is the measured copy."),
        ("`names.tsv`", name_table_rows, "name",
         "One row per measured name — subject or citation-only — with its layer counts, prose "
         "counts, surface spellings, and its page (empty for a citation-only name)."),
        ("`edges/family-manuscript.tsv`", edges["edges/family-manuscript.tsv"], "`fam` + dir",
         "The release's own family→manuscript links."),
        ("`edges/family-config.tsv`", edges["edges/family-config.tsv"], "`fam` + config",
         "Scope-note links keyed per family as a set: 405, not the 415 link occurrences."),
        ("`edges/config-declaration.tsv`", edges["edges/config-declaration.tsv"],
         "config + declaration", "The `main_results` triples, with the family that links each config."),
        ("`edges/family-lean.tsv`", edges["edges/family-lean.tsv"], "`fam` + config",
         "The derived family→Lean-file reach: 185 declarations over 127 families. There is no "
         "manuscript→Lean edge to carry."),
        ("`edges/citation.tsv`", edges["edges/citation.tsv"], "citing dir + target dir",
         "manuscript→corpus manuscript from release-marked `.bib` hrefs; untyped."),
        ("`edges/family-trace.tsv`", edges["edges/family-trace.tsv"], "`fam` + stem",
         "Family→trace attribution as README.md tabulates it."),
        ("`edges/family-topic.tsv`", edges["edges/family-topic.tsv"], "`fam` + topic",
         "Family→topic assignments from the curated vocabulary, with the layers that hit "
         "(T/A/S/P). Multi-label: a family appears once per topic it carries."),
        ("`edges/family-name.tsv`", edges["edges/family-name.tsv"], "`fam` + name",
         "Family→subject-name edges, with the layers that hit (F/M/E/D/b/B). Subject names only: "
         "a citation-only name has no family edge, only a `names.tsv` row."),
    ):
        L.append(row([name, len(rows_), key, what]))
    L.append("")
    L.append("## Reconciliation")
    L.append("")
    L.append(row(["Quantity", "Canonical (build_catalog joins)", "Rendered here"]))
    L.append("|---|---|---|")
    for k in ("families", "manuscripts", "formalized", "scope_notes", "challenges", "traces",
              "ver_dirs"):
        L.append(row([k.replace("_", " "), canon[k], rendered[k]]))
    L.append(row(["family pages", canon["families"], len(pages)]))
    L.append(row(["discipline pages", len(by_disc), len(disc_pages)]))
    L.append(row(["topic pages", len(topic_rows), len(topic_pages)]))
    L.append(row(["topic assignments", sum(len(r["families"]) for r in topic_rows),
                  len(edges["edges/family-topic.tsv"])]))
    L.append(row(["families with a topic", len({f for r in topic_rows for f in r["families"]}),
                  sum(1 for r in family_rows if r["topics"])]))
    L.append(row(["name pages", name_meta["subject"], len(name_pages)]))
    L.append(row(["names measured", len(name_rows), len(name_table_rows)]))
    L.append(row(["name→family edges", sum(len(r["fams"]) for r in subject_rows),
                  len(edges["edges/family-name.tsv"])]))
    L.append(row(["families with a name hit", len(name_covered), len({r["fam"] for r in family_rows})]))
    L.append(row(["trace families with a subject name", len(trace_fams & name_covered),
                  len(trace_fams)]))
    L.append("")
    L.append("## Not checked")
    L.append("")
    L.append("- Nothing here says a proof is correct. `formalized` is the yaml `sources:` flag at "
             "source level; `review: status: unchecked` and `automation: methods: [agent]` apply.")
    L.append("- No `.lean` file was opened and nothing was built, so a Lean link says the yaml "
             "names a file that exists on disk, not that it elaborates.")
    L.append("- Citation edges are untyped: the release records no builds-on / contrasts-with "
             "relation, so an edge is a citation choice, not consequence.")
    L.append("- The family→Lean reach is derived through scope-note config links. The release "
             "ships no manuscript→Lean edge, so the formalized manuscripts are not individually "
             "linked to a Lean file.")
    L.append("- Claim shapes are keyword floors carried from `notes/catalog.tsv`, not a census: "
             "families match three or more shapes and others match none.")
    L.append("- Topics are a curated keyword floor, not a classification: a family is listed under "
             "a term because the term's pattern hit its title, abstract, scope note, or derived "
             "Lean paths. `notes/topics.md` records the incidental matches each term was measured "
             "to carry, and the path layer is derived, not shipped.")
    L.append("- Link targets were checked for existence at render time, not for content: a link "
             "resolving to a file says the file is there, not that it says what the page claims.")
    L.append("- Names are a keyword floor, not a census. The name-vs-word test is corpus-internal "
             "(mid-sentence capitalization counts measured in this corpus); no external name "
             "dictionary was consulted, so a surname that never reaches a title layer is invisible "
             "as a subject.")
    L.append("- A `b`/`B` hit is a citation, not a subject: prose hits are counted with the "
             "bibliography and the cite/cross-reference braces stripped, and a name page lists "
             "them as evidence of where the name is cited, never as the scope of a result.")
    L.append("- Citation-only names carry no page, so a name search that finds no page is not "
             "evidence the corpus never mentions the name — check `names.tsv` for the "
             "`role = citation` rows.")
    L.append("- Family pages do not link name pages: the average family carries 27 subject names, "
             "which is a table, not a header row. The name→family direction is the one the index "
             "carries.")
    L.append("")
    write("README.md", "\n".join(L) + "\n")

    # ---- report: every count the entry point prints, plus the reconciliation ----
    broken = [f"{p} -> {h}" for p, h in links
              if not (IDX / p).parent.joinpath(h).exists()]
    tier_diff = sum(1 for r in family_rows if r["tier"] != ledger[r["fam"]]["tier"])
    mr_diff = sum(1 for r in family_rows if r["mainres"] != int(ledger[r["fam"]]["mainres"]))
    chal_diff = sum(1 for r in family_rows if r["chal"] != int(ledger[r["fam"]]["chal"]))
    paps_diff = sum(1 for r in family_rows if r["paps"] != int(ledger[r["fam"]]["paps"]))
    form_diff = sum(1 for r in family_rows if r["paps_form"] != int(ledger[r["fam"]]["paps_form"]))
    print(f"pages               family {len(pages)}  discipline {len(disc_pages)}  "
          f"topic {len(topic_pages)}  name {len(name_pages)}  entry 1")
    print(f"node tables         families {len(family_rows)}  manuscripts {len(manuscript_rows)}  "
          f"configs {len(config_rows)}  lean-dirs {len(lean_dir_rows)}  "
          f"scope-notes {len(scope_rows)}  traces {len(trace_rows)}  topics {len(topic_table_rows)}  "
          f"names {len(name_table_rows)}")
    print(f"edge tables         " + "  ".join(
        f"{name.split('/')[-1][:-4]} {len(edges[name])}" for name, _ in EDGE_TABLES))
    print(f"links checked       {len(links)}  broken {len(broken)}")
    for b in broken[:10]:
        print(f"  BROKEN {b}")
    print(f"canonical           " + "  ".join(f"{k} {canon[k]}" for k in canon))
    print(f"rendered            " + "  ".join(f"{k} {rendered[k]}" for k in rendered))
    missing_pages = [f for f in sorted(ledger)
                     if not (IDX / page_of.get(f, "")).is_file()]
    print(f"vs ledger         tier {tier_diff}  mainres {mr_diff}  chal {chal_diff}  "
          f"paps {paps_diff}  paps_form {form_diff}")
    print(f"ledger join         fams {len(fams)}  ledger rows {len(ledger)}  "
          f"ledger-only {sorted(set(ledger) - set(fams))}  overview-only {sorted(set(fams) - set(ledger))}  "
          f"pages {len(set(pages))}  pages absent on disk {len(missing_pages)}")
    print(f"trace files         {len([p for p in TRACES.iterdir() if p.is_file()])} on disk  "
          f"{len(trace_rows)} stems attributed  {len(trace_unlisted)} unattributed")
    print(f"citation            {len(citations)} edges  "
          f"{sum(1 for a, b, c, d in citations if b != d)} cross-family  "
          f"{len({b for _, b, _, _ in citations})} citing families  "
          f"{len({d for _, _, _, d in citations})} target families  "
          f"unresolved {report['citation_unresolved']}  unowned {report['citation_unowned']}")
    fl = edges["edges/family-lean.tsv"]
    print(f"family-lean         {len(fl)} rows over {len({r['fam'] for r in fl})} families  "
          f"{len({r['file'] for r in fl})} files  "
          f"{len({posixpath.dirname(r['file']) for r in fl})} module dirs")
    rec = {r["term"]: r for r in tsv(MT.TSV)}
    drift = [r["term"] for r in topic_table_rows
             if r["term"] not in rec
             or any(int(rec[r["term"]][c]) != r[c] for c in
                    ("fams", "title", "abstract", "scope", "path"))]
    print(f"topics              {len(topic_rows)} terms  "
          f"{len(edges['edges/family-topic.tsv'])} assignments over "
          f"{len({r['fam'] for r in edges['edges/family-topic.tsv']})} families  "
          f"negative {len([r for r in topic_rows if not r['families']])}  "
          f"max {max(topic_rows, key=lambda r: len(r['families']))['term']} "
          f"{max(len(r['families']) for r in topic_rows)}  "
          f"drift vs notes/topics.tsv {len(drift)} {drift[:5]}")
    ne = edges["edges/family-name.tsv"]
    print(f"names               {len(name_rows)} measured  subject {len(subject_rows)} "
          f"(pages {len(name_pages)})  citation-only {len(citation_rows)}  "
          f"edges {len(ne)} over {len({r['fam'] for r in ne})} families  "
          f"no-family names {len([r for r in name_rows if not r['fams']])}  "
          f"singletons {sum(1 for r in subject_rows if len(r['fams']) == 1)}  "
          f"max {max(((len(r['fams']), r['name']) for r in subject_rows))}  "
          f"variants {sum(1 for r in subject_rows if len(r['variants']) > 1)}  "
          f"trace families {len(trace_fams & name_covered)} of {len(trace_fams)}")
    print(f"configs             {len(config_rows)}  json {sum(1 for r in config_rows if r['json'] == '1')}  "
          f"lean {sum(1 for r in config_rows if r['lean'] == '1')}  "
          f"with a declaration {sum(1 for r in config_rows if r['decl_count'] > 0)}  "
          f"declarations {sum(r['decl_count'] for r in config_rows)}  "
          f"linked by >1 family {sum(1 for v in cfg2fams.values() if len(v) > 1)}")
    named = len(mod_decls)
    print(f"lean module dirs    {len(lean_dir_rows)}  named by the yaml "
          f"{sum(1 for r in lean_dir_rows if r['named_by_yaml'] > 0)} of {named} named dirs "
          f"(`{named - sum(1 for r in lean_dir_rows if r['named_by_yaml'] > 0)}` deeper than depth 2)  "
          f"`.lean` files inside them {sum(r['lean_files'] for r in lean_dir_rows)} of "
          f"{len(list(OAI.rglob('*.lean')))}")
    print(f"summary pairing     {sum(1 for r in family_rows if r['summary'] == '1')} of "
          f"{len(family_rows)} families have a notes/summaries page")
    dupes = collections.Counter(r["page"] for r in family_rows)
    print(f"page collisions     {sum(1 for c in dupes.values() if c > 1)}  "
          f"max slug length {max(len(r['slug']) for r in family_rows)}")
    print(f"manuscript links    main file {sum(1 for r in manuscript_rows if r['main_tex'])} of "
          f"{len(manuscript_rows)}  build/ {sum(1 for r in manuscript_rows if r['build'] == '1')}  "
          f"README.md {sum(1 for r in manuscript_rows if r['readme'] == '1')}")
    print(f"written             {len(pages) + len(disc_pages) + len(topic_pages) + len(name_pages) + 1} "
          f"pages + {8 + len(EDGE_TABLES)} tables -> {IDX.relative_to(ROOT)}/")


main()

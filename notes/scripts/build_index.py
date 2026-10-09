#!/usr/bin/env python3
"""Render notes/index/: the entry point, one page per family, one per discipline, and the node
and edge tables the pages are rendered from.

Stdlib plus jinja2. Reads text that ships in this repo plus two generated ledgers; writes only
under notes/index/; never invokes lean, lake, or comparator. Page text lives in
notes/templates/*.j2, so a page's wording is edited in the template, never in this file.

The joins are imported from build_catalog.py, not re-derived: family -> manuscript from
parse_contents() (CONTENTS.md) unioned with the overview.tex links, manuscript -> formalized from
parse_yaml() `sources:`, family -> config from parse_docs() (scope-note links), config ->
declaration + file from the formalization.yaml triples, family -> trace from parse_traces()
(the README.md trace table). The ledger supplies the derived claim-shape columns.

Rules this generator encodes, all of them stated in notes/index-design.md:

- **No manuscript -> Lean edge exists.** `sources:` is a flat list of manuscript paths and
  `main_results:` is a flat list of config/declaration/file triples; nothing joins them. The
  derivable chain is family -> config -> file, which reaches 136 families over 200 triples. The
  173 formalized manuscripts stay a per-manuscript flag, and a family with configs but no
  `main_results` entry renders as *absent*, not as zero.
- **416 configs, 426 link occurrences.** The edge table is keyed per family as a set, so it carries
  416; 7 scope notes link a config more than once (family 100 links `CylinderCovering` four
  times), which is the 10-occurrence gap.
- **10 traces over 11 files.** The Mézard–Parisi trace ships as both `.pdf` and `.tex`.
- **Manuscript ownership is the path component after `preprints`**, never `parts[-2]`.
- **`mainres` counts configs, not declarations**, matching the ledger column; 200 declarations over
  189 configs, so 8 configs carry more than one declaration and the page renders declarations
  separately.
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
import unicodedata

from jinja2 import Environment, FileSystemLoader

import build_catalog as B
import measure_topics as MT
import measure_names as MN
import check_index_links as CL  # report-only: the checker runs nothing at import

from catlib import yaml as Y
from catlib.paths import (
    COMPARATOR_DIR as CHAL,
    FORMALIZATION_YAML,
    OAI_DIR as OAI,
    PREPRINTS as PRE,
    REASONING_TRACES as TRACES,
    read_text,
)

ROOT = pathlib.Path(__file__).resolve().parents[2]
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


WRITTEN: set = set()


def write(relpath, text):
    f = IDX / relpath
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")
    WRITTEN.add(f)


def write_tsv(relpath, cols, rows):
    lines = ["\t".join(cols)]
    for r in rows:
        lines.append("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols))
    write(relpath, "\n".join(lines) + "\n")


def row(cells):
    return "| " + " | ".join(str(c).replace("|", "\\|") for c in cells) + " |"


def dirname(path):
    return posixpath.dirname(path)


def trace_links(stems):
    return " · ".join(f"[{s}]({UP}reasoning_traces/{s}.pdf)" for s in stems)


def topic_links(terms):
    return " · ".join(f"[{t}](../topics/{t}.md)" for t in terms)


TPL = ROOT / "notes" / "templates"
ENV = Environment(loader=FileSystemLoader(str(TPL)), keep_trailing_newline=True,
                  trim_blocks=True, lstrip_blocks=True, autoescape=False)
ENV.filters.update(row=row, base=base, dirname=dirname, trace_links=trace_links,
                   topic_links=topic_links)


def family_page(r, mans, cfgs, decls, tfiles, challenges, main_results, summary_href,
                summary_label, companions, abstract, topics):
    return ENV.get_template("family.md.j2").render(
        r=r, mans=mans, cfgs=cfgs, decls=decls, tfiles=tfiles, challenges=challenges,
        main_results=main_results, summary_href=summary_href, summary_label=summary_label,
        companions=companions, abstract=abstract, topics=topics, UP=UP)



def discipline_page(discipline, rows):
    tier = collections.Counter(r["tier"] for r in rows)
    return ENV.get_template("discipline.md.j2").render(
        discipline=discipline, rows=rows, UP=UP,
        tier_line=" · ".join(f"{t} {tier.get(t, 0)}" for t in ("T3", "T2", "T1", "T0")))


def topic_page(term, rec, fams, page_of):
    """One page per vocabulary term: the pattern, its yield by layer, and its families."""
    return ENV.get_template("topic.md.j2").render(term=term, rec=rec, fams=fams,
                                                  page_of=page_of)


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
    ms_fams = {f for f, _ in r["ms_title"]}
    decl_fams = sorted({f for stem, _, _ in r["decl"] for f in cfg2fams.get(stem, ())})
    title_fams = set(r["fam_title_fams"]) | ms_fams | set(r["env_title_fams"]) | set(decl_fams)
    counts = {"F": len(r["fam_title_fams"]), "M": len(ms_fams), "E": len(r["env_title_fams"]),
              "D": len(decl_fams), "b": len(r["body_fams"]), "B": len(r["bib_fams"])}
    fam_rows = [(f, ["yes" if c else "—" for c in
                     (f in r["fam_title_fams"], f in ms_fams, f in r["env_title_fams"],
                      f in decl_fams, f in r["body_fams"], f in r["bib_fams"])])
                for f in r["fams"]]
    ms = {}
    for _f, d in r["ms_title"]:
        ms.setdefault(d, set()).add("title")
    for d in r["body_ms"]:
        ms.setdefault(d, set()).add("prose")
    ms_rows = [(d, dir2fam.get(d, ""), " + ".join(sorted(ms[d])), dir2pdf.get(d, ""))
               for d in sorted(ms)]
    decl_rows = [(stem, d, fp,
                  " · ".join(f"[{x}](../{page_of[x]})" for x in cfg2fams.get(stem, ())) or "—")
                 for stem, d, fp in r["decl"]]
    return ENV.get_template("name.md.j2").render(
        r=r, fams=fams, page_of=page_of, NAME_SOURCES=NAME_SOURCES, counts=counts,
        fam_rows=fam_rows, ms_rows=ms_rows, decl_rows=decl_rows, title_fams=title_fams,
        variants_join=" · ".join(f"`{v}`" for v in r["variants"]), name=r["name"], UP=UP)


def index_readme_page(disc_rows, topic_tbl, name_tbl, table_rows, recon_rows, counts):
    """The entry point: tables arrive as cell lists, every prose count is passed in."""
    return ENV.get_template("index-readme.md.j2").render(
        disc_rows=disc_rows, topic_tbl=topic_tbl, name_tbl=name_tbl,
        table_rows=table_rows, recon_rows=recon_rows, **counts)


def main():
    _order, fams = B.parse_overview()
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

    triples = sorted(TRIPLE.findall(read_text(FORMALIZATION_YAML)))
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
    for p in Y.oai_lean_files():
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
    write_tsv("topics-rendered.tsv", TOPIC_COLS, topic_table_rows)
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
    disc_rows = []
    for discipline in sorted(by_disc):
        rows = by_disc[discipline]
        disc_rows.append([f"[{discipline}](disciplines/{disc_slug(discipline)}.md)", len(rows),
                          sum(r["paps"] for r in rows), sum(r["paps_form"] for r in rows),
                          sum(1 for r in rows if r["scope_note"] == "1"),
                          sum(r["chal"] for r in rows), sum(1 for r in rows if r["trace"]),
                          sum(r["verification"] for r in rows)])
    topic_tbl = [[f"[{r['term']}](topics/{r['term']}.md)", len(r["families"]),
                  len(r["title"]), len(r["abstract"]), len(r["scope"]), len(r["path"])]
                 for r in sorted(topic_rows, key=lambda r: (-len(r["families"]), r["term"]))]
    name_tbl = [[f"[{r['name']}](names/{r['name']}.md)", len(r["fams"]),
                 len(r["fam_title_fams"]), len({f for f, _ in r["ms_title"]}),
                 len(r["env_title_fams"]), len(r["decl"]),
                 len(r["body_fams"]), len(r["bib_fams"])]
                for r in sorted(subject_rows, key=lambda r: (-len(r["fams"]), r["name"]))[:40]]
    table_rows = [[name, len(rows_), key, what] for name, rows_, key, what in (
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
        ("`topics-rendered.tsv`", topic_table_rows, "term",
         "One row per curated vocabulary term: its pattern, its yield, its yield by layer, and "
         "its page. The patterns live in `notes/topics.tsv`; this table is the measured copy."),
        ("`names.tsv`", name_table_rows, "name",
         "One row per measured name — subject or citation-only — with its layer counts, prose "
         "counts, surface spellings, and its page (empty for a citation-only name)."),
        ("`edges/family-manuscript.tsv`", edges["edges/family-manuscript.tsv"], "`fam` + dir",
         "The release's own family→manuscript links."),
        ("`edges/family-config.tsv`", edges["edges/family-config.tsv"], "`fam` + config",
         "Scope-note links keyed per family as a set: 416, not the 426 link occurrences."),
        ("`edges/config-declaration.tsv`", edges["edges/config-declaration.tsv"],
         "config + declaration", "The `main_results` triples, with the family that links each config."),
        ("`edges/family-lean.tsv`", edges["edges/family-lean.tsv"], "`fam` + config",
         "The derived family→Lean-file reach: 200 declarations over 136 families. There is no "
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
    )]
    recon_rows = [[k.replace("_", " "), canon[k], rendered[k]]
                  for k in ("families", "manuscripts", "formalized", "scope_notes", "challenges",
                            "traces", "ver_dirs")]
    recon_rows += [
        ["family pages", canon["families"], len(pages)],
        ["discipline pages", len(by_disc), len(disc_pages)],
        ["topic pages", len(topic_rows), len(topic_pages)],
        ["topic assignments", sum(len(r["families"]) for r in topic_rows),
         len(edges["edges/family-topic.tsv"])],
        ["families with a topic", len({f for r in topic_rows for f in r["families"]}),
         sum(1 for r in family_rows if r["topics"])],
        ["name pages", name_meta["subject"], len(name_pages)],
        ["names measured", len(name_rows), len(name_table_rows)],
        ["name→family edges", sum(len(r["fams"]) for r in subject_rows),
         len(edges["edges/family-name.tsv"])],
        ["families with a name hit", len(name_covered), len({r["fam"] for r in family_rows})],
        ["trace families with a subject name", len(trace_fams & name_covered), len(trace_fams)],
    ]
    counts = {
        "n_pages": len(pages),
        "n_disc": len(disc_pages),
        "n_topic": len(topic_pages),
        "n_assign": len(edges["edges/family-topic.tsv"]),
        "n_nohit": len([r for r in topic_rows if not r["families"]]),
        "n_name_pages": len(name_pages),
        "n_name_rows": len(name_rows),
        "n_cite": len(citation_rows),
        "n_name_edges": len(edges["edges/family-name.tsv"]),
        "n_name_covered": len(name_covered),
        "n_ledger": len(ledger),
        "n_nofam": len(name_rows) - len([r for r in name_rows if r["fams"]]),
        "n_name_table": len(name_table_rows),
    }
    write("README.md", index_readme_page(disc_rows, topic_tbl, name_tbl, table_rows,
                                         recon_rows, counts))

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
    print("edge tables         " + "  ".join(
        f"{name.rsplit('/', 1)[-1][:-4]} {len(edges[name])}" for name, _ in EDGE_TABLES))
    print(f"links checked       {len(links)}  broken {len(broken)}")
    for b in broken[:10]:
        print(f"  BROKEN {b}")
    # Registered links per page group, the same grouping check_index_links.py reports for the
    # scanned set, so the coverage gap in notes/index-links.md is measurable per group.
    reg = collections.Counter(
        {"names": "name pages", "topics": "topic pages",
         "disciplines": "discipline pages"}.get(p.split("/")[0],
                                                "entry point" if p == "README.md"
                                                else "family pages")
        for p, _ in links)
    print("registered by group " + "  ".join(
        f"{g} {reg[g]}" for g in ("name pages", "family pages", "topic pages",
                                  "discipline pages", "entry point")))
    # Registered links per category, classified by the checker's own rule (importing it is safe:
    # check_index_links.py has no module-scope work), so notes/index-links.md can state the
    # scanned-minus-registered gap per category from two reports rather than from prose.
    regcat = collections.Counter(CL.category(CL.resolve(p, h)) for p, h in links)
    print("registered by category " + "  ".join(
        f"{c} {regcat[c]}" for c in sorted(regcat, key=lambda k: (-regcat[k], k))))
    print("canonical           " + "  ".join(f"{k} {canon[k]}" for k in canon))
    print("rendered            " + "  ".join(f"{k} {rendered[k]}" for k in rendered))
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
          f"max {max((len(r['fams']), r['name']) for r in subject_rows)}  "
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
          f"{Y.oai_lean_count()}")
    print(f"summary pairing     {sum(1 for r in family_rows if r['summary'] == '1')} of "
          f"{len(family_rows)} families have a notes/summaries page")
    dupes = collections.Counter(r["page"] for r in family_rows)
    print(f"page collisions     {sum(1 for c in dupes.values() if c > 1)}  "
          f"max slug length {max(len(r['slug']) for r in family_rows)}")
    print(f"manuscript links    main file {sum(1 for r in manuscript_rows if r['main_tex'])} of "
          f"{len(manuscript_rows)}  build/ {sum(1 for r in manuscript_rows if r['build'] == '1')}  "
          f"README.md {sum(1 for r in manuscript_rows if r['readme'] == '1')}")
    # A page whose family title changed is written under a new slug, so the old page survives on
    # disk and its manuscript table links the editions the merge superseded. The tree is generated,
    # so anything this build did not write is stale and is removed.
    stale = sorted(p for p in IDX.rglob("*")
                   if p.is_file() and p.suffix in (".md", ".tsv") and p not in WRITTEN)
    for p in stale:
        p.unlink()
    empty_dirs = 0
    for d in sorted((x for x in IDX.rglob("*") if x.is_dir()), key=lambda x: -len(x.parts)):
        if not any(d.iterdir()):
            d.rmdir()
            empty_dirs += 1
    print(f"stale swept         {len(stale)} files {sorted(p.relative_to(IDX).as_posix() for p in stale)}  "
          f"empty dirs removed {empty_dirs}")
    print(f"written             {len(pages) + len(disc_pages) + len(topic_pages) + len(name_pages) + 1} "
          f"pages + {8 + len(EDGE_TABLES)} tables -> {IDX.relative_to(ROOT)}/")


main()

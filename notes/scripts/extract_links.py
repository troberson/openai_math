#!/usr/bin/env python3
"""Extract notes/links.tsv: the typed-edge inventory of the release.

One row per relation type. Every count is computed here, so the command column
names this script and re-running it reproduces every number in the file.

Edges are read from the text that ships in the repo:

  CONTENTS.md / overview.tex        family -> manuscript links
  lean/formalization.yaml           manuscript -> formalized; family -> main_results
  lean/docs/*.md                    scope note -> comparator statement
  lean/ComparatorChallenges/        statement/solution config pairs
  lean/lakefile.lean                formalization -> declared upstream library
  lean/OAI/**/*.lean                observed import roots
  preprints/**/*.bib                manuscript -> bibliography entries; corpus citations
  preprints/**/*.tex                manuscript -> corpus manuscript (body href); body mentions
  README.md                         family -> reasoning trace

The family->manuscript mapping is imported from build_catalog.py so the paren-aware
path regex lives in exactly one place.

The three name relations (named-in-title, cited-in-bib, mentioned-in-body) are three
separate rows: they measure three different things and the repo has previously quoted
one number for all three.

Scope: every preprints/ scan is restricted to the manuscript directories the release
lists (CONTENTS.md), not to every directory under preprints/. Upstream keeps a superseded
edition of a revised manuscript on disk beside its replacement, and a withdrawn manuscript's
directory beside its notice, so a directory walk is 749 dirs, not 719 manuscripts, and a
superseded edition's bibliography would count its edges twice. The whole-tree counts and the
superseded-target citation counts are printed in the report, not written to the TSV.

Sync pass: notes/links.md is compared with notes/scripts/render_reports.py's render of it.
The report proves the numbers are measured; it proves nothing about the sentences around them,
and the page's tables are prose in the template, not report output. render_reports.py runs this
script as a child to compute that page's slots, and marks the child with RENDER_REPORTS_CHILD,
where the pass is inert by design — the writer rendering the page this pass asks for would
recurse. The gate's plain run is where the pass does its work.
"""
import bisect
import collections
import csv
import re
import sys
from pathlib import Path

import build_catalog as bc

from catlib import render as RD
from catlib import yaml as Y
from catlib.paths import (
    COMPARATOR_DIR as CHALLENGES,
    LAKEFILE,
    LEDGER_TSV as LEDGER,
    OAI_DIR as SOURCE,
    PREPRINTS,
    README_MD as README,
)

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "notes" / "links.tsv"
PAGE = REPO / "notes" / "links.md"

FIELDS = ["edge", "source", "pattern", "count", "detail", "command", "not_meaning"]
CMD = "python3 notes/scripts/extract_links.py"

# Title-phrase normalization for the three name relations.
NOUN = re.compile(r"\b(conjecture|conjectures|problem|problems|question|questions|hypothesis)\b", re.I)
# MSC classification statements, written as a rule rather than a stem search: a bare
# \bMSC\b / "primary class" scan hits prose ("MSc thesis", "2-primary class groups").
MSC = re.compile(
    r"MSC\s?-?\s?20\d\d|MSC\s*:|\\msc\b|mscclass|Mathematics Subject Classification"
    r"|Primary\s*:?\s*\d{2}\s?[A-Z]\s?xx",
    re.I,
)
HREF = re.compile(r"\\href\{(https?://[^}]+)\}")
PREPRINT_URL = re.compile(r"/preprints/([^/\\]+)/([A-Za-z0-9_.\-]+\.pdf)")


def norm(s):
    """Lowercase alphanumerics, single-spaced, leading 'the' dropped, possessives stripped."""
    s = s.lower().replace("\u2019", "'").replace("\u2018", "'")
    s = re.sub(r"'s\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\bthe\b", " ", s)
    return " ".join(s.split())


def ledger_rows():
    with LEDGER.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def owner(p):
    """Manuscript directory that owns a file: the component after 'preprints'."""
    parts = p.parts
    return parts[parts.index("preprints") + 1]


def listed_dirs():
    """The manuscript directories the release lists, per CONTENTS.md.

    Not a walk of preprints/: upstream keeps superseded editions and withdrawal notices on disk.
    """
    return {Path(p).parts[1] for ps in bc.parse_contents().values() for p in ps}


def read_group(paths):
    """dir -> normalized text, over a file list."""
    norm_text = {}
    for p in paths:
        t = p.read_text(encoding="utf-8", errors="replace")
        d = owner(p)
        norm_text[d] = norm_text.get(d, "") + " " + norm(t)
    return norm_text


class Blob:
    """One concatenated normalized corpus, searched once per phrase.

    Building the blob per phrase is O(phrases x corpus); 372 phrases over 128 MB of
    .tex is minutes that way, so the blob and its offset index are built once.
    """

    def __init__(self, norm_text):
        self.order = sorted(norm_text)
        self.blob = "\x00".join(norm_text[d] for d in self.order)
        self.starts = []
        off = 0
        for d in self.order:
            self.starts.append(off)
            off += len(norm_text[d]) + 1

    def find(self, phrase):
        found = set()
        i = self.blob.find(phrase)
        while i != -1:
            found.add(self.order[bisect.bisect_right(self.starts, i) - 1])
            i = self.blob.find(phrase, i + 1)
        return found



def bib_entries(scope):
    """(owning dir, entry body) for every @-entry in a .bib file owned by a listed manuscript."""
    out = []
    for p in sorted(PREPRINTS.glob("**/*.bib")):
        if owner(p) not in scope:
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"@[A-Za-z]+\s*\{([^,]*),", txt):
            nxt = txt.find("@", m.end())
            out.append((owner(p), txt[m.start() : nxt if nxt > 0 else len(txt)]))
    return out


def prefix6(title):
    """The title rule the surprise-ranking skill used: first 6 whitespace tokens, lowercased."""
    return " ".join(re.split(r"\s+", title.lower())[:6])


def legacy_title_proxy(titles, fam_dirs, scope):
    """Reproduce the recorded "14 of 372 family titles appear in the corpus's .bib files".

    The rule is the one written in the corpus-finding-surprise-ranking skill: a 6-token lowercased
    title prefix searched in the concatenation of `preprints/*/*.bib` + `preprints/*/*/*.bib`, with
    the corpus lowercased (not normalized) and own-family bibliographies included. It scans 417 of
    the 500 listed-manuscript .bib files, so the 83 at depth 4 are outside its scope.
    """
    shallow = sorted(p for p in PREPRINTS.glob("**/*.bib")
                     if len(p.relative_to(PREPRINTS).parts) <= 3 and owner(p) in scope)
    deep = sorted(p for p in PREPRINTS.glob("**/*.bib") if owner(p) in scope)
    out = {}
    for label, paths in (("depth<=3", shallow), ("all", deep)):
        per = {}
        for p in paths:
            d = owner(p)
            per[d] = per.get(d, "") + " " + p.read_text(encoding="utf-8", errors="replace").lower()
        anyf, cross = [], []
        for fam, title in sorted(titles.items()):
            ph = prefix6(title)
            hits = {d for d, txt in per.items() if ph in txt}
            if hits:
                anyf.append(fam)
            if hits - fam_dirs.get(fam, set()):
                cross.append(fam)
        out[label] = (len(paths), len(anyf), len(cross), anyf)
    return out


def main():
    rows = ledger_rows()
    fam_paps = bc.parse_contents()
    dir2fam = {Path(p).parts[1]: f for f, ps in fam_paps.items() for p in ps}
    fam_dirs = {f: {Path(p).parts[1] for p in ps} for f, ps in fam_paps.items()}
    titles = {r["fam"]: r["title"] for r in rows}
    mainres_fams = {r["fam"] for r in rows if int(r["mainres"]) > 0}
    form_fams = {r["fam"] for r in rows if int(r["paps_form"]) > 0}
    listed = set(dir2fam)
    n_manuscripts = len(listed)
    n_families = len(rows)
    n_docs = len(Y.doc_files())

    # Scope: the listed manuscripts only. A superseded edition on disk is not a manuscript row, and
    # its bibliography would count the same edges a second time.
    bib_files = [p for p in sorted(PREPRINTS.glob("**/*.bib")) if owner(p) in listed]
    tex_files = [p for p in sorted(PREPRINTS.glob("**/*.tex")) if owner(p) in listed]
    bib_tree = sorted(PREPRINTS.glob("**/*.bib"))
    tex_tree = sorted(PREPRINTS.glob("**/*.tex"))
    disk_dirs = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
    unlisted_dirs = [p.name for p in disk_dirs if p.name not in listed]
    notice_dirs = [n for n in unlisted_dirs
                   if "Withdrawal notice" in (PREPRINTS / n / "README.md")
                   .read_text(encoding="utf-8", errors="replace")]
    entries = bib_entries(listed)
    bib_blob = Blob(read_group(bib_files))
    tex_blob = Blob(read_group(tex_files))

    report = []

    def row(edge, source, pattern, count, detail, not_meaning):
        rows_out.append(
            {
                "edge": edge,
                "source": source,
                "pattern": pattern,
                "count": count,
                "detail": detail,
                "command": CMD,
                "not_meaning": not_meaning,
            }
        )
        report.append(f"{edge}: {count}  {detail}")

    rows_out = []

    # --- catalog structure -------------------------------------------------
    _, fams = bc.parse_overview()
    tex_only = sum(len(set(v["tex_paps"]) - set(fam_paps.get(f, []))) for f, v in fams.items())
    md_only = sum(len(set(fam_paps.get(f, [])) - set(v["tex_paps"])) for f, v in fams.items())
    row(
        "family->manuscript",
        "CONTENTS.md, overview.tex",
        "parse_contents(): `**NNN.` header + PAP link",
        sum(int(r["paps"]) for r in rows),
        f"{len(rows)} families; overview.tex-only links {tex_only}; CONTENTS.md-only links {md_only}",
        "A link the release publishes. It does not say the manuscript is formalized, "
        "read, or correct.",
    )
    row(
        "manuscript->formalized",
        "lean/formalization.yaml",
        "`sources:` -> `id: ../<PAP>`",
        sum(int(r["paps_form"]) for r in rows),
        f"of {n_manuscripts} manuscripts; {len(form_fams)} families",
        "A source-level declaration. `review: status: unchecked` and "
        "`automation: methods: [agent]` apply, so it is not a checked proof.",
    )
    row(
        "family->scope note",
        "lean/docs/<NNN>.md",
        "file exists",
        sum(1 for r in rows if r["scope_note"].strip() == "1"),
        f"of {n_families} families",
        "A note the release wrote. It states exclusions; it does not certify the proof.",
    )

    # --- comparator layer --------------------------------------------------
    link_files = collections.Counter()
    docs_with_links = 0
    raw_links = 0
    docs_with_intra_dupes = []
    for p in Y.doc_files():
        hits = re.findall(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean", p.read_text(encoding="utf-8"))
        if hits:
            docs_with_links += 1
        if len(hits) != len(set(hits)):
            docs_with_intra_dupes.append(p.stem)
        raw_links += len(hits)
        link_files.update(set(hits))
    total_links = sum(link_files.values())
    dupes = sum(1 for v in link_files.values() if v > 1)
    json_files = sorted(CHALLENGES.glob("*.json"))
    lean_files = sorted(CHALLENGES.glob("*.lean"))
    row(
        "scope note->comparator statement",
        "lean/docs/*.md",
        "`](../ComparatorChallenges/<name>.lean)`",
        raw_links,
        f"{total_links} distinct configs; {raw_links - total_links} duplicate links inside "
        f"{len(docs_with_intra_dupes)} docs ({', '.join(docs_with_intra_dupes)}); "
        f"{dupes} configs linked by >1 family; {docs_with_links} of {n_docs} docs",
        f"A link to a statement file. It is not a pass. The {raw_links}/{total_links} gap is link "
        "occurrences vs distinct configs — the same config linked twice in one doc — "
        "not a missing file, and no config is shared between families.",
    )
    row(
        "comparator config->statement+solution",
        "lean/ComparatorChallenges/",
        "`<name>.json` paired with `<name>.lean`",
        len(json_files),
        f"{len(lean_files)} .lean files; {len(json_files) - len(set(link_files))} never linked from a doc",
        "A statement/solution pair on disk. Nothing here says the comparator was run.",
    )
    yaml_lines = Y.yaml_lines()
    i = next(k for k, ln in enumerate(yaml_lines) if ln.strip() == "main_results:")
    cfgs = []
    for ln in yaml_lines[i + 1 :]:
        if ln and not ln.startswith("    "):
            break
        m = re.match(r"\s+-\s+comparator_config:\s*(\S+)", ln)
        if m:
            cfgs.append(m.group(1))
    row(
        "family->main_results declaration",
        "lean/formalization.yaml",
        "`status.main_results` -> `comparator_config:`",
        len(cfgs),
        f"{len(set(cfgs))} unique configs ({len(cfgs) - len(set(cfgs))} repeated entries); "
        f"{sum(1 for r in rows if int(r['mainres']) > 0)} families",
        "The release's own list of catalogued main results. It is a declaration, not a "
        "verification, and it is not the same set as the formalized-manuscript layer.",
    )

    # --- upstream libraries ------------------------------------------------
    lake_pairs = re.findall(
        r'^require\s+(?:«(?P<name>[^»]+)»|(?P<plain>[A-Za-z0-9_.\-]+))\s+from\s+git\s*\n\s*"(?P<url>[^"]+)"',
        LAKEFILE.read_text(encoding="utf-8"),
        re.M,
    )
    lake = [u for _n, _p, u in lake_pairs]
    # A declared library is reached by an import root whose name matches the require name, with
    # guillemets and hyphens folded out of both sides; `Schoenflies` reaches «schoenflies-lean».
    declared_slugs = [re.sub(r"[^a-z0-9]", "", (n or p).lower()) for n, p, _u in lake_pairs]
    CORE = {"OAI", "Lean", "Std", "Init", "Lake", "all"}
    imports = collections.Counter()
    for p in sorted(SOURCE.glob("**/*.lean")):
        for root in re.findall(r"^\s*import\s+([A-Za-z_][A-Za-z0-9_.]*)", p.read_text(encoding="utf-8", errors="replace"), re.M):
            imports[root.split(".")[0]] += 1
    external = {r: c for r, c in imports.items() if r not in CORE}
    reached = {r for r in external if re.sub(r"[^a-z0-9]", "", r.lower()) in declared_slugs
               or any(r.lower() in s for s in declared_slugs)}
    undeclared = sorted(set(external) - reached)
    aliased = {r for r in reached if re.sub(r"[^a-z0-9]", "", r.lower()) not in declared_slugs}
    row(
        "formalization->declared library",
        "lean/lakefile.lean",
        "`require ... from git \"url\" @ \"commit\"`",
        len(lake),
        "each pinned to a 40-char commit; see notes/formalization-deps.tsv",
        "A declared pin. No lake run happened here, so no pin is verified buildable.",
    )
    row(
        "formalization->observed import root",
        "lean/OAI/**/*.lean",
        "`^\\s*import\\s+<root>`",
        len(external),
        f"{sum(external.values())} statements; {len(reached)} reached by a declared URL "
        f"({len(aliased)} by name-alias, e.g. Mathlib for mathlib), "
        f"{len(undeclared)} declared nowhere ({', '.join(undeclared)})",
        "A direct import statement over lean/OAI only. Not the transitive closure, and "
        "a zero count is not non-use.",
    )

    # --- bibliographies ----------------------------------------------------
    ent = sum(len(re.findall(r"^@[A-Za-z]+", p.read_text(encoding="utf-8", errors="replace"), re.M)) for p in bib_files)
    row(
        "manuscript->bibliography entry",
        "preprints/**/*.bib",
        "`^@[A-Za-z]+`",
        ent,
        f"{len(bib_files)} .bib files in {len({owner(p) for p in bib_files})} of "
        f"{n_manuscripts} manuscript dirs",
        "An entry the manuscript ships. It is not a checked reference and not a claim "
        "that the cited work exists.",
    )

    # --- corpus-internal citations (the real manuscript->manuscript edge) --
    oai_entries = [(d, b) for d, b in entries if "OpenAI Math Release" in b]
    edges = set()
    target_dirs, citing_dirs = set(), set()
    target_fams, citing_fams = set(), set()
    target_fam_counts = collections.Counter()
    stale_targets, stale_hrefs = set(), 0
    self_family = 0
    unresolved = 0
    for d, btxt in oai_entries:
        for u in HREF.findall(btxt):
            m = PREPRINT_URL.search(u)
            if not m or not (PREPRINTS / m.group(1) / m.group(2)).exists():
                unresolved += 1
                continue
            dd = m.group(1)
            if dd not in dir2fam:
                # A citation whose target is a superseded edition: on disk, not a listed manuscript.
                stale_targets.add(dd)
                stale_hrefs += 1
                continue
            edges.add((d, dd))
            target_dirs.add(dd)
            citing_dirs.add(d)
            target_fams.add(dir2fam[dd])
            target_fam_counts[dir2fam[dd]] += 1
            citing_fams.add(dir2fam[d])
            if dir2fam[d] == dir2fam[dd]:
                self_family += 1
    cross = sum(1 for a, b in edges if dir2fam[a] != dir2fam[b])
    row(
        "manuscript->corpus manuscript (bib href)",
        "preprints/**/*.bib",
        "entry contains `OpenAI Math Release` + `\\href{.../preprints/<dir>/<f>.pdf}`",
        len(oai_entries),
        f"{len(edges)} resolved edges; {len(target_dirs)} target dirs over {len(target_fams)} of "
        f"{n_families} families; {len(citing_dirs)} citing dirs; {self_family} same-family; "
        f"{cross} cross-family; {unresolved} unresolved; {stale_hrefs} hrefs point at "
        f"{len(stale_targets)} superseded editions",
        "A citation of one release preprint by another. It measures what the release "
        "chose to cite, not importance, and it is not a citation graph of the wider literature.",
    )
    # Whole-tree census: the same href scan over every .bib on disk, superseded editions included.
    tree_stale = collections.Counter()
    tree_hrefs = 0
    for p in bib_tree:
        for u in HREF.findall(p.read_text(encoding="utf-8", errors="replace")):
            m = PREPRINT_URL.search(u)
            if m and (PREPRINTS / m.group(1) / m.group(2)).exists():
                tree_hrefs += 1
                if m.group(1) not in dir2fam:
                    tree_stale[m.group(1)] += 1
    tex_edges = collections.Counter()
    tex_target, tex_citing = set(), set()
    for p in tex_files:
        t = p.read_text(encoding="utf-8", errors="replace")
        for u in HREF.findall(t):
            m = PREPRINT_URL.search(u)
            if m and (PREPRINTS / m.group(1) / m.group(2)).exists():
                tex_edges[owner(p)] += 1
                tex_target.add(m.group(1))
                tex_citing.add(owner(p))
    row(
        "manuscript->corpus manuscript (body href)",
        "preprints/**/*.tex",
        "`\\href{.../preprints/<dir>/<f>.pdf}` in body text",
        sum(tex_edges.values()),
        f"{len(tex_target)} target dirs over "
        f"{len({dir2fam[d] for d in tex_target if d in dir2fam})} families; {len(tex_citing)} citing dirs",
        "An in-text link to a release preprint. Not a citation count and not a "
        "dependency; a link can be a courtesy pointer.",
    )

    # --- abstract cross-references ----------------------------------------
    edges_ab = [(r["fam"], r["companions"]) for r in rows if r["companions"].strip()]
    n_ab_edges = sum(len(c.split("|")) for _, c in edges_ab)
    companion_edge_fams = {a for a, c in edges_ab}
    row(
        "abstract->companion family",
        "overview.tex abstracts",
        "`result (\\d{3})` (build_catalog.py:106)",
        n_ab_edges,
        f"{len(edges_ab)} families: " + ", ".join(f"{a}->{b}" for a, b in edges_ab),
        f"The abstract names a sibling result. It is not a citation, not a dependency, "
        f"and {n_ab_edges} edges over {n_families} families is the whole intra-catalog "
        f"cross-reference layer.",
    )
    companion_word_fams = {r["fam"] for r in rows if int(r["companion_word"]) > 0}
    row(
        "abstract->'companion' wording",
        "overview.tex abstracts",
        "`\\bcompanion` (build_catalog.py:128)",
        len(companion_word_fams),
        f"families; {len(companion_word_fams & companion_edge_fams)} of them carry a "
        f"`result NNN` edge",
        "A word in an abstract. It does not create an edge and does not pair families.",
    )

    # --- reasoning traces --------------------------------------------------
    tr = re.findall(r"^\|\s*(\d{3})\s*\|\s*\[[^\]]*\]\(reasoning_traces/([^)]+?)\.(?:pdf|tex)\)", README.read_text(encoding="utf-8"), re.M)
    fams_tr = {f for f, _ in tr}
    stems = {s for _, s in tr}
    trace_files = sorted(p for p in (REPO / "reasoning_traces").rglob("*") if p.is_file())
    row(
        "family->reasoning trace",
        "README.md",
        "trace table row `| NNN | [..](reasoning_traces/<stem>.pdf)`",
        len(fams_tr),
        f"{len(stems)} distinct stems; {len(trace_files)} files on disk "
        f"({', '.join(sorted(s for s in stems if len([p for p in trace_files if p.stem == s]) > 1))}) "
        "ships .pdf and .tex",
        "The release published a trace for these families. It is attribution by the "
        "release table, not evidence the trace is the proof.",
    )

    # --- the three name relations -----------------------------------------
    named = [f for f, t in titles.items() if NOUN.search(t)]
    row(
        "named-in-title",
        "overview.tex `\\resultentry` arg 2 (via notes/catalog.tsv `title`)",
        "title contains conjecture|problem|question|hypothesis",
        len(named),
        f"of {n_families} families",
        "The title names a target. It says nothing about resolution, and it is not a "
        "citation — this is a property of the catalog's prose, not of the literature.",
    )
    cited, any_bib = [], []
    for fam, title in sorted(titles.items()):
        ph = norm(title)
        if not ph:
            continue
        hits = bib_blob.find(ph)
        if hits:
            any_bib.append(fam)
        if hits - fam_dirs.get(fam, set()):
            cited.append(fam)
    row(
        "cited-in-bib",
        "preprints/**/*.bib",
        "normalized family title (possessives and 'the' dropped) in a .bib owned by a **different** family",
        len(cited),
        f"of {n_families} families; {len(any_bib)} families when the family's own .bib files are included",
        "A title-phrase match in a bibliography. It is a proxy: the release's real "
        f"citation edges are the href rows above, which reach {len(target_fams)} families. "
        "A miss here is not evidence of no impact.",
    )
    body, any_body = [], []
    for fam, title in sorted(titles.items()):
        ph = norm(title)
        if not ph:
            continue
        hits = tex_blob.find(ph)
        if hits:
            any_body.append(fam)
        if hits - fam_dirs.get(fam, set()):
            body.append(fam)
    row(
        "mentioned-in-body",
        "preprints/**/*.tex",
        "normalized family title in a .tex owned by a **different** family",
        len(body),
        f"of {n_families} families; {len(any_body)} families including own-family text",
        "A phrase appearing in another manuscript's source. It can be a shared term, "
        "not a reference to this family, and it is not a citation count.",
    )

    # --- negatives ---------------------------------------------------------
    legacy = legacy_title_proxy(titles, fam_dirs, listed)
    msc_hits = 0
    for p in tex_files + bib_files + [REPO / "overview.tex"]:
        msc_hits += len(MSC.findall(p.read_text(encoding="utf-8", errors="replace")))
    row(
        "family->MSC code",
        "preprints/**/*.tex, **/*.bib, overview.tex",
        "MSC 20xx | `\\msc` | mscclass | 'Mathematics Subject Classification' | Primary nnXxx",
        msc_hits,
        "files scanned: " + str(len(tex_files) + len(bib_files) + 1),
        "Negative: the release carries no MSC classification anywhere, so topic "
        "grouping cannot be read from classification codes. A bare `\\bMSC\\b` scan is not "
        "this rule — it hits 'MSc thesis' and '2-primary class groups'.",
    )
    kw_bib = sum(len(re.findall(r"^\s*keywords\s*=", p.read_text(encoding="utf-8", errors="replace"), re.M | re.I)) for p in bib_files)
    row(
        "bibliography entry->keywords field",
        "preprints/**/*.bib",
        "`^\\s*keywords\\s*=`",
        kw_bib,
        f"{ent} entries scanned",
        "Negative: no entry carries a keywords field, so the bibliographies carry no "
        "topic vocabulary — only titles, authors, and the release hrefs.",
    )
    kw_tex = {owner(p) for p in tex_files if re.search(r"\\keywords\b", p.read_text(encoding="utf-8", errors="replace"))}
    row(
        "manuscript->\\keywords macro",
        "preprints/**/*.tex",
        "`\\keywords`",
        len(kw_tex),
        f"of {n_manuscripts} manuscript dirs ({len(kw_tex) / n_manuscripts:.1%})",
        "Negative-weighted: 98% of manuscripts define no keyword list, so a topic query "
        "cannot be answered from manuscript metadata at scale.",
    )
    row(
        "manuscript->verification bundle",
        "preprints/*/verification, INPUTS.md, verification/COVERAGE.md",
        "directory / file exists",
        sum(int(r["verification"]) for r in rows),
        f"{len({p.parent.name for p in PREPRINTS.glob('*/verification')})} dirs over "
        f"{sum(1 for r in rows if int(r['verification']) > 0)} families; INPUTS.md "
        f"{sum(int(r['inputs']) for r in rows)}; COVERAGE.md {sum(int(r['covmd']) for r in rows)}",
        "A certificate bundle the manuscript ships. It is not a theorem check, and "
        "family 318's SUPPORT-COVERAGE.md names artifacts that do not exist on disk.",
    )
    summary_rows = [r for r in rows if r["summary"].strip() == "1"]
    row(
        "family->notes summary page",
        "notes/summaries/<discipline>/<NNN>-*.md",
        "file exists",
        len(summary_rows),
        f"of {n_families} families; {sum(int(r['paps']) for r in summary_rows)} manuscripts behind them",
        "Our own reading artifact. It is not part of the release and carries no "
        "authority about the result.",
    )

    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(FIELDS) + "\n")
        for r in rows_out:
            fh.write("\t".join(str(r[f]).replace("\t", " ") for f in FIELDS) + "\n")

    for line in report:
        print(line)
    print(f"rows: {len(rows_out)}  fields: {len(FIELDS)}")
    print(f"bib entries: {ent}  bib files: {len(bib_files)}  tex files: {len(tex_files)}")
    print(f"preprint dirs on disk: {len(disk_dirs)}  listed manuscripts: {n_manuscripts}  unlisted: "
          f"{len(unlisted_dirs)} = {len(unlisted_dirs) - len(notice_dirs)} superseded editions + "
          f"{len(notice_dirs)} withdrawal notices")
    print(f"whole-tree .bib: {len(bib_tree)}  whole-tree .tex: {len(tex_tree)}  "
          f"(listed-scope: {len(bib_files)} / {len(tex_files)})")
    print(f"bib hrefs pointing at superseded editions: listed-scope {stale_hrefs} over "
          f"{len(stale_targets)} dirs; whole-tree {sum(tree_stale.values())} over {len(tree_stale)} "
          f"of {tree_hrefs} tree hrefs (report only; not counted in the TSV)")
    print(f"cited-in-bib families: {len(cited)}  named-in-title: {len(named)}  mentioned-in-body: {len(body)}")
    print(f"cited list: {cited}")
    print(f"mentioned list: {body}")
    print(f"cited∩mentioned: {sorted(set(cited) & set(body))}  "
          f"mentioned-only: {sorted(set(body) - set(cited))}  cited-only: {sorted(set(cited) - set(body))}")
    print(f"named list: {named}")
    s_n, s_any, s_cross, s_list = legacy["depth<=3"]
    d_n, d_any, d_cross, _ = legacy["all"]
    print(f"legacy title proxy (6-token prefix, lowercased corpus, .bib at depth<=3): "
          f"files={s_n} any={s_any} cross={s_cross}  <- the recorded '14 of 372'")
    print(f"legacy proxy list: {s_list}")
    print(f"same title rule over all .bib: files={d_n} any={d_any} cross={d_cross}")
    print(f"corpus citation edges: {len(edges)}  target families: {len(target_fams)}  citing dirs: {len(citing_dirs)}")
    print(f"top bib target families: {target_fam_counts.most_common(10)}")
    print(f"mainres families: {len(mainres_fams)}  formalized families: {len(form_fams)}  "
          f"mainres-only: {len(mainres_fams - form_fams)}  formalized-only: {len(form_fams - mainres_fams)}")
    print(f"body href edges: {sum(tex_edges.values())}  target dirs: {len(tex_target)}")
    print(f"MSC hits: {msc_hits}  bib keywords fields: {kw_bib}  \\keywords dirs: {len(kw_tex)}")
    print(f"written: {OUT.relative_to(REPO)}")
    sync = RD.sync_problems(PAGE, PAGE.read_text(encoding="utf-8"))
    print(f"sync problems (notes/links.md) {len(sync)}")
    for p in sync:
        print("  " + p)
    return len(sync)


if __name__ == "__main__":
    sys.exit(main())

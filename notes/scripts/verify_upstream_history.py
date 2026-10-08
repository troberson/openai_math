#!/usr/bin/env python3
"""Verify the upstream_history/ pages against git, the release files, and disk.

Report-only: writes nothing. Run twice and diff — the report must be identical.

What each check measures, and the rule behind it:

  anchors      every `path:line` (or `path:a-b`) span resolves; `…suffix` anchors resolve
               against the nearest preceding explicit path, bare `:N` against that path too
  quotations   every *"…"* matches the anchored lines verbatim modulo whitespace, and the
               anchor sits in the same paragraph as the quotation
  fenced       every fenced block is matched against the nearest preceding anchor's lines
               (a block with no preceding anchor is skipped — the fd4aeeb page has no anchors)
  slugs        every backticked date-suffixed token exists as a preprints/ directory
  links        every markdown link resolves, quotations excluded (a quote may contain one)
  needles      per-anchor content checks: the seven noncomputable lines, the stale yaml id,
               the overview pdfsubject line, family 032's resultentry line
  counts       every count phrase on the page is re-derived from git + disk, not from the page
  tables       the fixes table and the config table are checked row by row against disk

Run with --mutant to corrupt one real claim per form the page uses and prove each fires.
"""

import csv
import io
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_catalog as bc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PAGES = [
    "upstream_history/README.md",
    "upstream_history/2026-10-07_3014888.md",
    "upstream_history/2026-10-07_fd4aeeb.md",
]
PAGE_301 = "upstream_history/2026-10-07_3014888.md"
PAGE_FD = "upstream_history/2026-10-07_fd4aeeb.md"
BASE = "adc7f1241"  # merge-base: the release as we mirrored it
UP = "301488868"  # the upstream commit the 3014888 page discusses
PRE = "9b68bc538"  # our last pre-merge commit: the "Before" column of the ledger table

ANCHOR = re.compile(r"`([^`\n]*?)?:([0-9]+)(?:-([0-9]+))?`")
QUOTE = re.compile(r'\*"([^"]*?)"\*', re.S)
LINK = re.compile(r"\]\(([^)\s]+)\)")
SLUG = re.compile(r"`([A-Za-z0-9][A-Za-z0-9-]*-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{1,2}-\d{4})/`")
# Citation-only = the note says only that citations were updated. The Exact BSD note ("removes an
# obsolete supporting citation and updates citations…") is a repair: history.md lists it under Fixes.
CITATION_ONLY = re.compile(r"^This version updates (?:a citation to a revised manuscript|citations to revised manuscripts)")
VERSION_NOTE = re.compile(r"## Version note\s*\n+(.+)")


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT)] + list(args), capture_output=True,
                          text=True, check=True).stdout


def ws(text):
    """Whitespace-folded, markup-normalized comparison form.

    Verbatim covers the words, not the markup: a markdown link URL the page elides to `(…)`
    is markup, so every `(https://…)` on the source side is folded to the same `(…)`, and
    typographic quotes are folded to ASCII — the same fold the `overview.tex` text layer
    already applies, since the release ships both `'` and `’`.
    """
    text = (text.replace("\u2019", "'").replace("\u2018", "'")
                .replace("\u201c", '"').replace("\u201d", '"'))
    text = re.sub(r"\((?:https?|ftp)://[^)]*\)", "(…)", text)
    return re.sub(r"\s+", " ", text).strip()


def overview_text(text):
    """bc.parse_overview() over an arbitrary overview.tex string."""
    start = text.index("\\begin{document}")
    discipline, fams, order, i = None, {}, [], start
    while True:
        ns, nr = text.find("\\cataloguesection{", i), text.find("\\resultentry{", i)
        if nr == -1:
            break
        if ns != -1 and ns < nr:
            args, i = bc.read_args(text, ns + len("\\cataloguesection"))
            discipline = args[0]
            continue
        args, i = bc.read_args(text, nr + len("\\resultentry"))
        fams[args[0]] = {"discipline": discipline, "title": args[1].strip(),
                         "abstract": args[2].strip(), "tex_paps": re.findall(bc.PAP, args[3])}
        order.append(args[0])
    return order, fams


def ledger(rev=None):
    text = git("show", f"{rev}:notes/catalog.tsv") if rev else (ROOT / "notes/catalog.tsv").read_text(encoding="utf-8")
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def yaml_text(rev=None):
    return git("show", f"{rev}:lean/formalization.yaml") if rev else (ROOT / "lean/formalization.yaml").read_text(encoding="utf-8")


def yaml_parse(text):
    sources = set(re.findall(r"^\s*id:\s*\.\./(" + bc.PAP + r")", text, re.M))
    main = Counter(re.findall(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json", text))
    return sources, main


def ls_leaf(rev, prefix, suffix):
    """Count files under `prefix` named `<digits><suffix>` (the lean/docs/ family notes)."""
    n = len(suffix)
    return sum(1 for f in git("ls-tree", "-r", "--name-only", rev, "--", prefix).split("\n")
               if f.endswith(suffix) and f.split("/")[-1][:-n].isdigit())


def measure():
    p = {}
    status = git("diff", "--name-status", BASE, UP).splitlines()
    p["added"] = sum(1 for l in status if l.startswith("A"))
    p["deleted"] = sum(1 for l in status if l.startswith("D"))
    p["modified"] = sum(1 for l in status if l.startswith("M"))
    p["top_level"] = sorted({l.split("\t")[-1] for l in status if "/" not in l.split("\t")[-1]})

    pre, post = ledger(PRE), ledger()
    p["ledger_rows"] = (len(pre), len(post))
    for col in ("paps", "paps_form", "scope_note", "chal", "mainres", "verification", "inputs",
                "covmd", "versions", "summary"):
        p["sum_" + col] = (sum(int(r[col]) for r in pre), sum(int(r[col]) for r in post))
    # `trace` is a pipe-joined stem list, not a number: the figure is the row count.
    p["sum_trace"] = (sum(1 for r in pre if r["trace"]), sum(1 for r in post if r["trace"]))
    p["tier"] = (Counter(r["tier"] for r in pre), Counter(r["tier"] for r in post))
    p["fam_form"] = (sum(1 for r in pre if int(r["paps_form"]) > 0),
                     sum(1 for r in post if int(r["paps_form"]) > 0))
    p["tier_moves"] = {r["fam"]: (pre[i]["tier"], r["tier"]) for i, r in enumerate(post)
                       if r["tier"] != pre[i]["tier"]}
    p["paps_moves"] = {r["fam"]: (int(pre[i]["paps"]), int(r["paps"])) for i, r in enumerate(post)
                       if int(pre[i]["paps"]) != int(r["paps"])}
    p["form_moves"] = {r["fam"]: (int(pre[i]["paps_form"]), int(r["paps_form"])) for i, r in enumerate(post)
                       if int(pre[i]["paps_form"]) != int(r["paps_form"])}
    p["companion_pre"] = sum(1 for r in pre if r["companion_word"] == "1")
    p["companion_post"] = sum(1 for r in post if r["companion_word"] == "1")

    src_pre, main_pre = yaml_parse(yaml_text(BASE))
    src_post, main_post = yaml_parse(yaml_text())
    p["sources"] = (len(src_pre), len(src_post))
    p["entries"] = (sum(main_pre.values()), sum(main_post.values()))
    p["configs"] = (len(main_pre), len(main_post))
    p["new_configs"] = sorted(set(main_post) - set(main_pre))
    p["new_entries"] = sum(main_post[c] for c in p["new_configs"])
    p["main_post"] = main_post

    contents = bc.parse_contents()
    listed = {q for paths in contents.values() for q in paths}
    p["listed"] = sum(len(v) for v in contents.values())
    p["listed_form"] = len(src_post & listed)
    p["stale_ids"] = sorted(src_post - listed)

    dirs = sorted(d.name for d in (ROOT / "preprints").iterdir() if d.is_dir())
    p["dirs"] = len(dirs)
    p["pdfs"] = sum(1 for _ in (ROOT / "preprints").rglob("*.pdf"))
    p["notices"] = sorted(d for d in dirs
                          if (ROOT / "preprints" / d / "README.md").is_file()
                          and "Withdrawal notice" in (ROOT / "preprints" / d / "README.md").read_text(encoding="utf-8"))
    owner = {}
    for fam, paths in contents.items():
        for q in paths:
            owner[q.split("/")[1]] = fam
    # Superseded = on disk, not listed in CONTENTS.md, and not one of the withdrawal notices.
    p["superseded"] = len([d for d in dirs if d not in owner and d not in p["notices"]])

    versioned = {}
    for d in dirs:
        rd = ROOT / "preprints" / d / "README.md"
        if rd.is_file():
            m = VERSION_NOTE.search(rd.read_text(encoding="utf-8"))
            if m:
                versioned[d] = m.group(1)
    p["versioned"] = len(versioned)
    p["repairs"] = sorted(d for d, note in versioned.items() if not CITATION_ONLY.match(note))
    cites = Counter(owner.get(d, "?") for d, note in versioned.items() if CITATION_ONLY.match(note))
    p["citation_only"] = dict(cites)

    p["scope_notes"] = (ls_leaf(BASE, "lean/docs/", ".md"), ls_leaf("HEAD", "lean/docs/", ".md"))
    p["challenges"] = (sum(1 for f in git("ls-tree", "-r", "--name-only", BASE, "lean/ComparatorChallenges/").split("\n") if f.endswith(".lean")),
                       sum(1 for f in git("ls-tree", "-r", "--name-only", "HEAD", "lean/ComparatorChallenges/").split("\n") if f.endswith(".lean")))
    p["oai_files"] = (sum(1 for f in git("ls-tree", "-r", "--name-only", BASE, "lean/OAI/").split("\n") if f.endswith(".lean")),
                      sum(1 for _ in (ROOT / "lean/OAI").rglob("*.lean")))
    p["oai_imports"] = sum(1 for l in git("diff", BASE, UP, "--", "lean/OAI.lean").splitlines() if l.startswith("+import "))
    # Only files the diff *modifies*: the 1135 added paths ship whole new formalization trees whose
    # `noncomputable def` lines are not edits, and counting them reads 170 over 45 files.
    modified = {l.split("\t")[-1] for l in git("diff", "--name-status", BASE, UP, "--", "lean/OAI/").splitlines()
                if l.startswith("M")}
    files, hits, cur = set(), 0, None
    for line in git("diff", BASE, UP, "--", "lean/OAI/").splitlines():
        if line.startswith("+++ b/"):
            cur = line[6:] if line[6:] in modified else None
        elif line.startswith("+") and cur and re.match(r"^\+noncomputable def ", line):
            hits += 1
            files.add(cur)
    p["noncomputable"] = (hits, sorted(files))

    _, fams_pre = overview_text(git("show", f"{BASE}:overview.tex"))
    _, fams_post = overview_text((ROOT / "overview.tex").read_text(encoding="utf-8"))
    changed = [f for f in fams_post if fams_pre[f] != fams_post[f]]
    p["resultentry_changed"] = changed
    p["path_only"] = [f for f in changed if fams_pre[f]["title"] == fams_post[f]["title"]
                      and fams_pre[f]["abstract"] == fams_post[f]["abstract"]]
    p["text_changed"] = [f for f in changed if f not in p["path_only"]]
    p["fam032"] = {"title_pre": fams_pre["032"]["title"], "title_post": fams_post["032"]["title"],
                   "abs_pre": len(fams_pre["032"]["abstract"]), "abs_post": len(fams_post["032"]["abstract"]),
                   "links_pre": len(fams_pre["032"]["tex_paps"]), "links_post": len(fams_post["032"]["tex_paps"])}

    p["config_fam"] = {}
    for fam, d in bc.parse_docs().items():
        for cfg in d["configs"]:
            p["config_fam"][cfg] = fam
    p["owner"] = owner
    return p


# ---------------------------------------------------------------- page parsing

def split_blocks(lines):
    """-> [('para'|'code', start0, end0)] over the page."""
    out, i, fence = [], 0, None
    while i < len(lines):
        if lines[i].startswith("```"):
            if fence is None:
                fence = i
            else:
                out.append(("code", fence, i))
                fence = None
            i += 1
            continue
        if not lines[i].strip():
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip() and not lines[j].startswith("```"):
            j += 1
        out.append(("para", i, j - 1))
        i = j
    return out


def resolve_anchor(path, last_explicit, pool, problems, where):
    if path == "":
        if last_explicit is None:
            problems.append(f"{where}: bare line anchor with no preceding path")
            return None
        return last_explicit
    if path.startswith("…"):
        suffix = path[1:]
        if last_explicit and last_explicit.endswith(suffix):
            return last_explicit
        cand = [q for q in pool if q.endswith(suffix)]
        if len(cand) == 1:
            return cand[0]
        problems.append(f"{where}: suffix anchor {path!r} resolves to {len(cand)} files")
        return None
    rel = path[3:] if path.startswith("../") else path
    if not (ROOT / rel).is_file():
        problems.append(f"{where}: anchor path {path!r} is not a file")
        return None
    return rel


def check_page(name, text, p, problems):
    lines = text.split("\n")
    pool = [f"preprints/{d}/README.md" for d in sorted(x.name for x in (ROOT / "preprints").iterdir() if x.is_dir())]
    pool += [f"lean/docs/{x.name}" for x in (ROOT / "lean/docs").glob("*.md")]
    last_explicit = None
    anchors = []  # (para_start, relpath, start, end, source_text)

    def src(rel, a, b):
        fl = (ROOT / rel).read_text(encoding="utf-8").split("\n")
        return ws(" ".join(fl[a - 1:b])), len(fl)

    for kind, a, b in split_blocks(lines):
        body = "\n".join(lines[a:b + 1])
        if kind == "para":
            for m in ANCHOR.finditer(body):
                path, start = m.group(1) or "", int(m.group(2))
                end = int(m.group(3)) if m.group(3) else start
                where = f"{name}:{a + 1 + body[:m.start()].count(chr(10))}"
                rel = resolve_anchor(path, last_explicit, pool, problems, where)
                if rel is None:
                    continue
                if not path.startswith("…"):
                    last_explicit = rel
                text_src, n = src(rel, start, end)
                if start < 1 or end > n:
                    problems.append(f"{where}: anchor {rel}:{start}-{end} is outside the file ({n} lines)")
                    continue
                anchors.append((a, rel, start, end, text_src))
            for m in QUOTE.finditer(body):
                quote = ws(m.group(1))
                para = [x for x in anchors if x[0] == a]
                if not para:
                    problems.append(f"{name}:{a + 1}: quotation has no anchor in its paragraph: {quote[:60]!r}")
                    continue
                # A quotation is pinned to one anchor's own lines, not to the union of the
                # paragraph's anchors: a union span lets a shifted anchor keep matching, which
                # is exactly the corruption this mutant injects. A quote that spans more source
                # than one anchor names must widen that anchor.
                if not any(quote in t for (_, _, _, _, t) in para):
                    problems.append(f"{name}:{a + 1}: quotation is not verbatim in its anchored lines: {quote[:60]!r}")
            for m in LINK.finditer(QUOTE.sub("", body)):
                target = m.group(1)
                if target.startswith(("http://", "https://", "#")):
                    continue
                if not (ROOT / "upstream_history" / target).resolve().is_file():
                    problems.append(f"{name}:{a + 1}: link target {target!r} does not exist")
        else:
            prev = [x for x in anchors if x[0] < a]
            if not prev:
                continue
            _, rel, start, end, _ = prev[-1]
            block = [l for l in lines[a + 1:b] if l.strip()]
            text_src, _ = src(rel, start, start + max(len(block), end - start + 1) - 1)
            if ws(" ".join(block)) not in text_src:
                problems.append(f"{name}:{a + 1}: fenced block does not match {rel}:{start}")
    for m in SLUG.finditer(text):
        if not (ROOT / "preprints" / m.group(1)).is_dir():
            problems.append(f"{name}: slug {m.group(1)!r} is not a preprints/ directory")
    return anchors


# ---------------------------------------------------------------- needles

def check_needles(p, problems):
    def line(rel, n):
        return (ROOT / rel).read_text(encoding="utf-8").split("\n")[n - 1]

    for ln, decl in [(184, "representationEquivalence"), (208, "finiteRepresentationEquivalence")]:
        l = line("lean/OAI/CategoryTheory/Thomason/Representation.lean", ln)
        if "noncomputable def" not in l or decl not in l:
            problems.append(f"needle: Representation.lean:{ln} is not the expected noncomputable def ({l!r})")
    for ln, decl in [(142, "loopMap"), (150, "groupMap"), (154, "componentsMap"),
                     (287, "loopHomeomorphEquiv"), (462, "componentsFunctor")]:
        l = line("lean/OAI/CategoryTheory/Thomason/Simplicial/LoopDimensionShift.lean", ln)
        if "noncomputable def" not in l or decl not in l:
            problems.append(f"needle: LoopDimensionShift.lean:{ln} is not the expected noncomputable def ({l!r})")
    l = line("lean/formalization.yaml", 684)
    if "Taming-implies-compatibility-on-four-manifolds-September-23-2026/paper.pdf" not in l:
        problems.append(f"needle: formalization.yaml:684 does not name the September-23 edition ({l!r})")
    l = line("overview.tex", 12)
    if "pdfsubject={372 result families in 719 manuscripts}" not in l:
        problems.append(f"needle: overview.tex:12 is not the pdfsubject line ({l!r})")
    l = line("overview.tex", 142)
    if not l.startswith("\\resultentry{032}"):
        problems.append(f"needle: overview.tex:142 is not family 032's resultentry ({l[:40]!r})")
    for fam, ln in [("157", 10), ("157", 11), ("157", 12), ("075", 9), ("103", 9), ("137", 9),
                    ("049", 10), ("130", 12), ("237", 23), ("301", 9), ("027", 9), ("066", 9),
                    ("195", 9), ("195", 11)]:
        if not line(f"lean/docs/{fam}.md", ln).strip():
            problems.append(f"needle: lean/docs/{fam}.md:{ln} is an empty line")


# ---------------------------------------------------------------- counts

def check_counts(name, text, p, problems):
    if name != PAGE_301:
        return
    flat = ws(text)
    nrep, ncite = len(p["repairs"]), sum(p["citation_only"].values())

    def want(phrase):
        if phrase not in flat:
            problems.append(f"count: phrase absent from page: {phrase!r}")

    t0, t2 = p["tier"][0], p["tier"][1]
    gain = sorted(f for f, (a, b) in p["form_moves"].items() if b > a)
    lose = sorted(f for f, (a, b) in p["form_moves"].items() if b < a)
    t0m = sorted(f for f, (a, b) in p["tier_moves"].items() if a == "T0")
    t2m = sorted(f for f, (a, b) in p["tier_moves"].items() if a == "T2")
    cite = ", ".join(f"**{f}** ({n})" for f, n in sorted(p["citation_only"].items()))
    for phrase in [
        f"**{p['added']} files added, {p['deleted']} deleted, {p['modified']} modified**",
        f"repaired {nrep} manuscripts, re-issued {ncite} more for citations alone, and added "
        f"{len(p['new_configs'])} formalizations",
        f"The manuscript count moves **{p['sum_paps'][0]} → {p['sum_paps'][1]}** and the family count "
        f"holds at **{p['ledger_rows'][1]}**",
        f"reads {p['listed_form']} formalized manuscripts of the {p['listed']} listed",
        f"Fixes: {nrep} manuscripts, {nrep - 1} of them proof repairs",
        f"so **{nrep - 1}** of the {nrep} carry mathematical repair",
        f"Citation-only re-issues: {ncite} manuscripts",
        cite,
        f"Additional formalizations: {len(p['new_configs'])} configs, {p['new_entries']} declarations",
        f"grows from {p['entries'][0]} `main_results` entries over {p['configs'][0]} configs to "
        f"**{p['entries'][1]} entries over {p['configs'][1]} configs**",
        f"grows **{p['challenges'][0]} → {p['challenges'][1]}** configs",
        f"the only such change, {p['companion_pre']} families carry it then **{p['companion_post']}**",
        f"**{len(p['resultentry_changed'])}** `\\resultentry` lines are rewritten",
        f"**{len(p['path_only'])}** of them change manuscript paths only",
        f"only **{p['text_changed'][0]}** changes text",
        f"`lean/OAI.lean` gains {p['oai_imports']} imports",
        f"go {p['oai_files'][0]:,} → {p['oai_files'][1]:,}",
        f"its abstract shrinks **{p['fam032']['abs_pre']} → {p['fam032']['abs_post']}** characters",
        f"manuscript links go **{p['fam032']['links_pre']} → {p['fam032']['links_post']}**",
        f"Its manuscript count drops **{p['fam032']['links_pre']} → {p['fam032']['links_post']}**",
        f"now holds **{p['dirs']}** directories",
        f"**{p['listed']}** listed in",
        f"**{p['superseded']}** superseded editions",
        f"**{len(p['notices'])}** withdrawal notices",
        f"{p['pdfs']} PDFs sit under",
        f"| Families | {p['ledger_rows'][0]} | {p['ledger_rows'][1]} |",
        f"| Manuscripts | {p['sum_paps'][0]} | {p['sum_paps'][1]} |",
        f"| Formalized manuscripts (`sources:` ids) | {p['sources'][0]} | {p['sources'][1]} |",
        f"| Families with a formalized manuscript | {p['fam_form'][0]} | {p['fam_form'][1]} |",
        f"| Scope notes | {p['scope_notes'][0]} | {p['scope_notes'][1]} |",
        f"| Comparator challenges | {p['challenges'][0]} | {p['challenges'][1]} |",
        f"| `main_results` entries / configs | {p['entries'][0]} / {p['configs'][0]} | "
        f"{p['entries'][1]} / {p['configs'][1]} |",
        f"| T3 / T2 / T1 / T0 | {t0['T3']} / {t0['T2']} / {t0['T1']} / {t0['T0']} | "
        f"{t2['T3']} / {t2['T2']} / {t2['T1']} / {t2['T0']} |",
        f"**T0 → T3** for {' '.join(t0m)}, **T2 → T3** for {' '.join(t2m)}",
        f"{' '.join(lose)}** loses its formalization flag",
        f"Verification bundles ({p['sum_verification'][1]}), `INPUTS.md` ({p['sum_inputs'][1]}), "
        f"`COVERAGE.md` ({p['sum_covmd'][1]}), reasoning traces ({p['sum_trace'][1]})",
        f"formalization is **{p['listed_form']}**, not {p['sources'][1]}",
        f"One of the {p['sources'][1]} `sources:` ids",
        f"All {p['sources'][1]} ids resolve",
    ]:
        want(phrase)
    if len(gain) != len(p["new_configs"]):
        problems.append(f"count: {len(gain)} families gain a formalization, {len(p['new_configs'])} new configs")
    gain_cfg = sorted({p["config_fam"][c] for c in p["new_configs"]})
    if gain != gain_cfg:
        problems.append(f"count: families gaining a formalization {gain} != families of the new configs {gain_cfg}")
    if list(p["paps_moves"]) != ["032"]:
        problems.append(f"count: manuscript-count changes are {p['paps_moves']}, not 032 alone")
    if sorted(p["top_level"]) != ["CONTENTS.md", "README.md", "history.md", "overview.pdf", "overview.tex"]:
        problems.append(f"count: top-level files touched are {p['top_level']}")
    if p["versioned"] != nrep + ncite:
        problems.append(f"count: {p['versioned']} version notes != {nrep} repairs + {ncite} citation-only")
    if p["dirs"] != p["listed"] + p["superseded"] + len(p["notices"]):
        problems.append(f"count: {p['dirs']} dirs != {p['listed']} listed + {p['superseded']} superseded + "
                        f"{len(p['notices'])} notices")
    if p["noncomputable"][0] != 7 or len(p["noncomputable"][1]) != 2:
        problems.append(f"count: {p['noncomputable'][0]} noncomputable additions over "
                        f"{len(p['noncomputable'][1])} modified files, not 7 over 2")


def check_tables(name, text, p, problems):
    if name != PAGE_301:
        return
    lines = text.split("\n")
    rows = [l for l in lines if re.match(r"^\| \d{3} \| `[^`]+-2026` \| \*\"", l)]
    if len(rows) != len(p["repairs"]):
        problems.append(f"table: {len(rows)} fixes rows, {len(p['repairs'])} repair directories on disk")
    for l in rows:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        fam, slug = cells[0], cells[1].strip("`")
        if not (ROOT / "preprints" / slug).is_dir():
            problems.append(f"table: {slug!r} is not a preprints/ directory")
        if p["owner"].get(slug) != fam:
            problems.append(f"table: {slug} is listed under {p['owner'].get(slug)}, row says {fam}")
        m = re.search(r"`([^`]+/README\.md:\d+)`", cells[2])
        if not m:
            problems.append(f"table: row {fam} {slug} carries no full anchor")
            continue
        rel, ln = m.group(1).rsplit(":", 1)
        if rel != f"preprints/{slug}/README.md":
            problems.append(f"table: row {fam} anchor path {rel} != its own directory")
            continue
        note = (ROOT / rel).read_text(encoding="utf-8").split("\n")[int(ln) - 1]
        quote = ws(re.search(r'\*"([^"]*?)"\*', cells[2]).group(1))
        if quote not in ws(note):
            problems.append(f"table: row {fam} quotation is not on {rel}:{ln}")
    cfg_rows = [l for l in lines if re.match(r"^\| \d{3} \| `[A-Za-z0-9]+` \| \d+ \|", l)]
    cfgs = [l.strip().strip("|").split("|")[1].strip().strip("`") for l in cfg_rows]
    if sorted(cfgs) != p["new_configs"]:
        problems.append(f"table: configs in the table {sorted(cfgs)} != the {len(p['new_configs'])} new configs")
    for l in cfg_rows:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        fam, cfg, n = cells[0], cells[1].strip("`"), int(cells[2])
        if p["config_fam"].get(cfg) != fam:
            problems.append(f"table: {cfg} is linked by scope note {p['config_fam'].get(cfg)}, row says {fam}")
        if p["main_post"][cfg] != n:
            problems.append(f"table: {cfg} has {p['main_post'][cfg]} main_results entries, row says {n}")


# ---------------------------------------------------------------- mutants

def mutants(p):
    base = (ROOT / PAGE_301).read_text(encoding="utf-8")
    fd = (ROOT / PAGE_FD).read_text(encoding="utf-8")
    cases = [
        ("diff triple", PAGE_301, base.replace("**1135 files added, 31 deleted, 19 modified**",
                                               "**1134 files added, 31 deleted, 19 modified**"), "phrase absent from page"),
        ("deleted row", PAGE_301, "\n".join(l for l in base.split("\n")
                                            if not l.startswith("| 376 | `Incompressible-Box-Transport")), "fixes rows"),
        ("quote word", PAGE_301, base.replace("supplies the annulus proof of the circuit estimate",
                                              "supplies the annulus proof of the bound estimate"), "not verbatim in its anchored lines"),
        ("paraphrase", PAGE_301, base.replace('The resulting count is therefore"*',
                                              'so the count is therefore nonzero"*'), "not verbatim in its anchored lines"),
        ("anchor shift", PAGE_301, base.replace("`history.md:19`", "`history.md:18`"), "not verbatim in its anchored lines"),
        ("dead path", PAGE_301, base.replace("preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md:21",
                                             "preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-8-2026/README.md:21"), "is not a file"),
        ("tier list", PAGE_301, base.replace("for 027 066 075 103 137 195 301", "for 027 066 075 103 137 301"), "phrase absent from page"),
        ("config name", PAGE_301, base.replace("`FourierLLogL`", "`FourierLLogL2`"), "new configs"),
        ("count phrase", PAGE_301, base.replace("**749** directories", "**748** directories"), "phrase absent from page"),
        ("entry count", PAGE_301, base.replace("| 137 | `OneTapeSpace` | 2 |", "| 137 | `OneTapeSpace` | 1 |"), "main_results entries"),
        ("unanchored quote", PAGE_FD, fd.replace("Nothing. `git diff", 'Nothing. *"a quotation with no anchor at all"* `git diff'), "no anchor in its paragraph"),
        ("dead link", PAGE_301, base.replace("[`history.md`](../history.md)", "[`history.md`](../historyx.md)"), "does not exist"),
    ]
    fired = 0
    for label, page, text, needle in cases:
        original = (ROOT / page).read_text(encoding="utf-8")
        if text == original:
            # A mutation whose search string is absent from the page is a silent no-op: the
            # mutant reports "MISSED" for the same reason a real fault goes unreported.
            problems = [f"mutation {label} changed nothing — its search string is not in {page}"]
        else:
            problems = []
            check_page(page, text, p, problems)
            check_counts(page, text, p, problems)
            check_tables(page, text, p, problems)
        hit = [x for x in problems if needle in x]
        fired += bool(hit)
        print(f"  mutant {label:<18} {'FIRED ' if hit else 'MISSED'}  {(hit or problems or ['no problem'])[0][:88]}")
    return fired, len(cases)


def main():
    mutant = "--mutant" in sys.argv
    p = measure()
    problems = []
    for name in PAGES:
        text = (ROOT / name).read_text(encoding="utf-8")
        check_page(name, text, p, problems)
        check_counts(name, text, p, problems)
        check_tables(name, text, p, problems)
    check_needles(p, problems)

    print("== population ==")
    print(f"diff {BASE}..{UP}: {p['added']} added / {p['deleted']} deleted / {p['modified']} modified")
    print(f"top-level touched: {' '.join(p['top_level'])}")
    print(f"preprints: {p['dirs']} dirs = {p['listed']} listed + {p['superseded']} superseded + "
          f"{len(p['notices'])} notices; {p['pdfs']} pdfs")
    print(f"version notes: {p['versioned']} = {len(p['repairs'])} repairs + {sum(p['citation_only'].values())} citation-only")
    print(f"citation-only families: {' '.join(f'{k}:{v}' for k, v in sorted(p['citation_only'].items()))}")
    print(f"ledger rows {p['ledger_rows'][0]} -> {p['ledger_rows'][1]}; paps {p['sum_paps'][0]} -> {p['sum_paps'][1]}; "
          f"sources {p['sources'][0]} -> {p['sources'][1]}")
    print(f"listed-formalized {p['listed_form']}; stale ids: {p['stale_ids']}")
    print(f"entries {p['entries'][0]} -> {p['entries'][1]} over configs {p['configs'][0]} -> {p['configs'][1]}; "
          f"challenges {p['challenges'][0]} -> {p['challenges'][1]}; scope notes {p['scope_notes'][0]} -> {p['scope_notes'][1]}")
    print(f"new configs {len(p['new_configs'])} carrying {p['new_entries']} entries: {' '.join(p['new_configs'])}")
    print(f"tiers {dict(sorted(p['tier'][0].items()))} -> {dict(sorted(p['tier'][1].items()))}")
    print(f"tier moves {len(p['tier_moves'])}: {' '.join(sorted(p['tier_moves']))}")
    print(f"formalization gain {' '.join(sorted(f for f, (a, b) in p['form_moves'].items() if b > a))} / "
          f"lose {' '.join(sorted(f for f, (a, b) in p['form_moves'].items() if b < a))}")
    print(f"paps moves: {p['paps_moves']}; companion word {p['companion_pre']} -> {p['companion_post']}")
    print(f"resultentry changed {len(p['resultentry_changed'])} ({' '.join(p['resultentry_changed'])}); "
          f"path-only {len(p['path_only'])}; text {p['text_changed']}")
    print(f"032: abstract {p['fam032']['abs_pre']} -> {p['fam032']['abs_post']}, links "
          f"{p['fam032']['links_pre']} -> {p['fam032']['links_post']}")
    print(f"lean/OAI *.lean {p['oai_files'][0]} -> {p['oai_files'][1]}; OAI.lean +{p['oai_imports']} imports; "
          f"noncomputable {p['noncomputable'][0]} over {len(p['noncomputable'][1])} files")
    print()
    print("== checks ==")
    print(f"pages checked: {len(PAGES)}")
    print(f"problems: {len(problems)}")
    for x in problems:
        print(f"  ! {x}")
    if mutant:
        print()
        print("== mutants ==")
        fired, total = mutants(p)
        print(f"fired {fired} of {total}")
        if fired < total:
            problems.append("a mutant did not fire")
    ok = not problems
    print()
    print("RESULT:", "green" if ok else f"{len(problems)} problems")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

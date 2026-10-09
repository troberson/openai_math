#!/usr/bin/env python3
"""Measure the name signal in the release, report-only.

math-u41.4. Names sit in four sources; this script extracts candidate names from
all four, plus the two body layers that tell a subject from a citation, normalizes
the spelling variants the sources disagree on, classifies each candidate, and prints
the report every count in notes/names.md and notes/index/names/ comes from. With
--json it dumps the records notes/scripts/build_index.py renders into name pages. It
writes no file in the repo.

Sources, and the provenance each yields:
  title-family   family titles in overview.tex             - title, a subject
  title-manuscript  manuscript directory names             - title, a subject
  title-theorem  optional titles of statement environments - title, a subject
  declaration    main_results declaration names            - declaration, a subject
  body           manuscript prose, bibliography stripped   - body, a citation
  bib-author     author fields of the bibliography         - body, a citation

The subject/citation split is the bead's point: a name in a body paragraph is a
citation, not a subject, so only title-layer and declaration-layer hits make a page.

Name-vs-word test, measured against this corpus (no external dictionary). A surname
is written capitalized mid-sentence and almost never lowercase. Sentence-initial
capitalization is what makes English words look capitalized, so the counter that
matters is mid-sentence capitalization: a token is name-like when mid >= 3 and
low <= max(1, mid // 2), and word-like when low >= 20 and low >= 5 * max(1, mid).
Measured on the tokens a plain capitalized count cannot separate: `all` mid=1426
low=43916, `the` mid=23736 low=856520, `games` mid=57 low=100, `lane` mid=16 low=48
— all word-like; `catalan` mid=33 low=7, `koebe` mid=39 low=14, `saxl` mid=21 low=9,
`pixton` mid=14 low=6 — all name-like. The report prints these as its `probe tokens`
line (PROBE_TOKENS below), because a rejected candidate carries no row in the JSON.
Cite keys are lowercase name fragments
(`catalan2012`), so the bibliography and the cite/cross-reference braces are stripped
before any count.

Family-title escape. A name the release put in a family title is a subject even when
the manuscripts barely mention it, so a family-title candidate with no prose evidence
is accepted when it is also an author surname in the bibliography. The bibliography is
the corpus's own surname gazetteer; the escape adds 16 names: Bochner, Campana, Curtis,
Elliott, Etingof, Green, Jacobsthal, Kraetzer, Mahler, Ostmann, Pop, Riesz, Ryser, Shub,
Swinnerton-Dyer, Wilson.

Rejection ladder, in the order applied: a key that is not a lowercase word, a
cross-reference label word, a maths word (the Hom and Quot functors and four heading
words), a key containing a digit, an acronym (dominant surface all capitals: CAT, ADM),
a LaTeX macro (dominant surface with an internal capital: OpenAIWidth), a prose word,
then the name-like test. A candidate that is name-like from any title source is a
subject; one that is not name-like is accepted only through the family-title escape.

Run: python3 notes/scripts/measure_names.py [--json]
"""
from __future__ import annotations

import collections
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notes" / "scripts"))
import build_catalog as B  # noqa: E402

import csv

LEDGER = {}
with open(ROOT / "notes" / "catalog.tsv", newline="") as _fh:
    for _r in csv.DictReader(_fh, delimiter="\t"):
        LEDGER[_r["fam"]] = _r

PRE = ROOT / "preprints"
YAML = ROOT / "lean" / "formalization.yaml"

# Statement environments whose optional argument is a name the release chose.
STATEMENT_ENV = ("theorem", "lemma", "proposition", "corollary", "conjecture",
                 "claim", "definition", "example", "remark", "question",
                 "convention", "thm")
STATEMENT = re.compile(
    r"\\begin\{(?:%s)\}\s*\[([^\]]{1,140})\]" % "|".join(STATEMENT_ENV))
# A capitalized token, allowing dash-linked compounds (Mezard-Parisi) and possessives.
NAME = re.compile(r"[A-ZÀ-Þ][A-Za-zÀ-ÿ]*(?:[-‐‑‒–—][A-ZÀ-Þ][A-Za-zÀ-ÿ]*)*(?:'[sS])?")
CAPTOK = re.compile(r"[A-ZÀ-Þ][A-Za-zÀ-ÿ]*(?:'[sS])?")
LOWTOK = re.compile(r"\b[a-zà-ÿ]+(?:'s)?")
OKKEY = re.compile(r"^[a-z][a-z]*(?:-[a-z][a-z]*)*$")
# Characters that end a sentence or open a display: a capital after one is not evidence
# that the token names a person.
NONMID = set(".!?;:}~%&$\\{}[]()#")
# Cross-reference and inclusion commands whose braces hold keys, not prose. Cite keys
# are lowercase name fragments and would poison the lowercase count.
CITE = re.compile(r"\\(?:no)?cite[a-zA-Z]*\*(?:\[[^\]]*\])?\{[^}]*\}")
XREF = re.compile(r"\\(?:label|ref|eqref|autoref|cref|Cref|nameref|labelcref|index|url|"
                  r"href|includegraphics|input|include|usepackage|bibliographystyle|"
                  r"hypertarget)\*?(?:\[[^\]]*\])?\{[^}]*\}")

# Tokens that are capitalized in prose for structural reasons, not because they name
# a person: cross-reference labels, the months that end every manuscript directory
# name, and the prover itself.
LABEL_WORDS = {
    "theorem", "theorems", "lemma", "lemmas", "proposition", "propositions",
    "corollary", "corollaries", "conjecture", "conjectures", "definition",
    "definitions", "example", "examples", "remark", "remarks", "claim",
    "claims", "notation", "exercise", "exercises", "problem", "problems",
    "question", "questions", "convention", "conventions", "case", "cases",
    "step", "steps", "proof", "proofs", "answer", "answers", "equation",
    "equations", "figure", "figures", "table", "tables", "section",
    "sections", "appendix", "appendices", "chapter", "chapters",
    "introduction", "abstract", "reference", "references", "remarkbox",
    "january", "february", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday", "springer", "elsevier", "cambridge", "oxford", "princeton",
    "chicago", "berlin", "heidelberg", "newyork", "london", "american",
    "mathematics", "mathematicae", "society", "press", "lean", "openai",
}

# Tokens that pass the mid-sentence capitalization test and appear in a title layer,
# but name a mathematical object or an English adjective, not a person. Each was
# traced to the title that produced it; the trace is recorded in notes/names.md.
# Names that look like this and are kept: eccles ("Eccles's conjecture for spheres"),
# street ("Street nerves of two-piece covers"), villain (the Villain field),
# sebastiani ("Thom--Sebastiani--Sakamoto"), saint ("Saint--Venant"), solitar
# (Baumslag--Solitar), maker and snaky (family 187's own game roles).
JUNK_WORDS = {
    "hom",         # "The orbit Hom calculation" - the Hom functor
    "quot",        # "The open Quot enhancement" - the Quot functor
    "combinatorics",  # "Combinatorics of shapes"
    "computer",    # "Computer-assisted"
    "beaver",      # "The Busy Beaver cutoff"
    "stablest",    # "Majority Is Stablest with a degree cutoff"
}

# The tokens notes/names.md tabulates to show the gate separating names from words.
# Rejected candidates carry no row in the JSON, so the gate's evidence for them lives
# only here: the report prints cap/mid/low for each token in this list.
PROBE_TOKENS = ("the", "all", "games", "lane", "hom", "quot", "cat", "adm",
               "boolean", "catalan", "koebe", "saxl", "pixton", "wang", "cauchy")


def fold(s: str) -> str:
    """Strip LaTeX accent escapes and Unicode diacritics so spellings join."""
    s = s.replace("\u2019", "'")
    s = re.sub(r"\\[Hh]\{([a-zA-Z])\}", r"\1", s)
    s = re.sub(r"\\['`^~\"]([a-zA-Z])", r"\1", s)
    s = s.replace("{", "").replace("}", "")
    d = unicodedata.normalize("NFD", s)
    return "".join(c for c in d if not unicodedata.combining(c))


def key(s: str) -> str:
    """Canonical form: folded, dash-unified, possessive-stripped, lowercase."""
    s = fold(s)
    s = re.sub(r"\s+", " ", s).strip()
    for d in ("‐", "‑", "‒", "–", "—"):
        s = s.replace(d, "-")
    s = s.strip("\"'`$ ").strip()
    if s.endswith("'s"):
        s = s[:-2]
    elif s.endswith("'"):
        s = s[:-1]
    return s.strip("-").lower()


def macro_shaped(surface: str) -> bool:
    """A surface form with a second internal capital is a LaTeX macro, not a name.

    Tested per dash-component so Mezard-Parisi survives and OpenAI-Scalar does not.
    """
    return any(re.search(r"[A-ZÀ-Þ]", c[1:]) for c in surface.split("-") if c)


def all_caps(surface: str) -> bool:
    letters = [c for c in surface if c.isalpha()]
    return len(letters) >= 2 and all(c.upper() == c for c in letters)


def tex_files():
    """Every manuscript .tex at depth 1-3, in path order.

    Sorted: glob order is directory order, and the per-name evidence lists
    (theorem-environment titles, body manuscript dirs) are recorded in scan order.
    """
    for depth in (1, 2, 3):
        for p in sorted(PRE.glob("/".join(["*"] * depth) + "/*.tex")):
            yield p


def strip_bibliography(t: str) -> str:
    t = re.sub(r"\\begin\{thebibliography\}.*?(\\end\{thebibliography\}|$)", " ", t,
               flags=re.S)
    return re.sub(r"\\bibliography\{[^}]*\}|\\printbibliography|\\addbibresource\{[^}]*\}",
                  " ", t)


def prose(t: str) -> str:
    """Body text with the bibliography and the cite/cross-reference braces removed."""
    t = strip_bibliography(fold(t))
    return XREF.sub(" ", CITE.sub(" ", t))


def dir_of(path) -> str:
    """The manuscript a path belongs to: the component after `preprints`."""
    parts = pathlib.PurePosixPath(str(path)).parts
    if "preprints" in parts:
        return parts[parts.index("preprints") + 1]
    return ""


def measure():
    order, fams = B.parse_overview()
    dir2fam = {}
    for f in order:
        for p in fams[f]["tex_paps"]:
            d = dir_of(p)
            if d:
                dir2fam[d] = f

    fam_title = collections.defaultdict(set)
    ms_title = collections.defaultdict(list)
    env_title = collections.defaultdict(set)
    env_hits = collections.defaultdict(list)
    surfaces = collections.defaultdict(collections.Counter)
    env_count = 0
    for f in order:
        for m in NAME.finditer(fold(fams[f]["title"])):
            fam_title[key(m.group(0))].add(f)
            surfaces[key(m.group(0))][m.group(0)] += 1
    for d, f in sorted(dir2fam.items()):
        for m in NAME.finditer(fold(d.replace("-", " "))):
            k = key(m.group(0))
            surfaces[k][m.group(0)] += 1
            if (f, d) not in ms_title[k]:
                ms_title[k].append((f, d))

    cap = collections.Counter()
    mid = collections.Counter()
    low = collections.Counter()
    body = collections.defaultdict(set)
    variants = collections.defaultdict(collections.Counter)
    for p in tex_files():
        fam = dir2fam.get(dir_of(p))
        raw = p.read_text(encoding="utf-8", errors="replace")
        for m in STATEMENT.finditer(raw):
            env_count += 1
            for tk in NAME.finditer(fold(m.group(1))):
                k = key(tk.group(0))
                env_title[k].add(fam)
                surfaces[k][tk.group(0)] += 1
                if len(env_hits[k]) < 8:
                    env_hits[k].append((fam, fold(m.group(1))))
        t = prose(raw)
        for m in CAPTOK.finditer(t):
            k = key(m.group(0))
            if len(k) < 3:
                continue
            cap[k] += 1
            i = m.start() - 1
            while i >= 0 and t[i] in " \t\n":
                i -= 1
            prev = t[i] if i >= 0 else ""
            if prev and prev not in NONMID and "\n\n" not in t[max(0, i - 40):i + 1]:
                mid[k] += 1
            body[k].add(fam)
            variants[k][m.group(0)] += 1
            surfaces[k][m.group(0)] += 1
        for m in LOWTOK.finditer(t):
            k = key(m.group(0))
            if len(k) >= 3:
                low[k] += 1

    decl = collections.defaultdict(list)
    for m in re.finditer(r"comparator_config:\s*(\S+)\s*\n\s*declaration:\s*(\S+)\s*\n\s*file:\s*(\S+)",
                         YAML.read_text()):
        stem = pathlib.PurePosixPath(m.group(1)).stem
        for seg in m.group(2).split("."):
            for tk in re.findall(r"[A-Z][a-z0-9]+", seg):
                decl[key(tk)].append((stem, m.group(2), m.group(3)))
                surfaces[key(tk)][tk] += 1

    bib = collections.defaultdict(set)
    bib_entries = 0
    for p in sorted(PRE.glob("**/*.bib")):
        fam = dir2fam.get(dir_of(p))
        t = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"^\s*@\w+\s*\{([^,]*),\s*(.*?)^\s*\}", t, re.S | re.M):
            bib_entries += 1
            am = re.search(r"^\s*author\s*=\s*[{\"]?(.*?)[}\"]?\s*,?\s*$",
                           m.group(2), re.M | re.S)
            if not am:
                continue
            a = re.sub(r"\$[^$]*\$", " ", re.sub(r"\s+", " ", am.group(1)))
            for part in re.split(r"\s+and\s+", a):
                part = part.strip().strip("{}\"").strip()
                if not part:
                    continue
                last = part.split(",")[0] if "," in part else part.split()[-1]
                k = key(last)
                if len(k) >= 3 and OKKEY.match(k):
                    bib[k].add(fam)

    def name_like(k):
        return mid[k] >= 3 and low[k] <= max(1, mid[k] // 2)

    def word_like(k):
        return low[k] >= 20 and low[k] >= 5 * max(1, mid[k])

    def acronym(k):
        """The way the corpus most often writes the token is all capitals."""
        v = surfaces[k]
        return bool(v) and all_caps(v.most_common(1)[0][0])

    def macro(k):
        r"""The way the corpus most often writes the token is macro-shaped.

        Judged on the dominant surface form over every layer, not on prose alone: a
        cite key that leaks into a theorem-environment title ("\cite{OpenAIWidth}")
        never appears as prose, so a prose-only view of surface forms cannot see it.
        """
        v = surfaces[k]
        return bool(v) and macro_shaped(v.most_common(1)[0][0])

    title_cands = set(fam_title) | set(ms_title) | set(env_title) | set(decl)
    subject, rejected = set(), collections.Counter()
    escape_names = []
    for k in title_cands:
        if len(k) < 3 or not OKKEY.match(k):
            rejected["not-a-word-key"] += 1
        elif k in LABEL_WORDS:
            rejected["label-word"] += 1
        elif k in JUNK_WORDS:
            rejected["maths-word"] += 1
        elif any(c.isdigit() for c in k):
            rejected["contains-digit"] += 1
        elif acronym(k):
            rejected["acronym"] += 1
        elif macro(k):
            rejected["latex-macro"] += 1
        elif word_like(k):
            rejected["prose-word"] += 1
        elif name_like(k):
            subject.add(k)
        elif k in fam_title and k in bib:
            subject.add(k)
            escape_names.append(k)
            rejected["family-title-via-bib"] += 1
        else:
            rejected["no-prose-evidence"] += 1

    # A plural of an attested subject name is the same name. Measured: hamiltonians,
    # hessians, jacobians, lagrangians, laplacians.
    merged = []
    for k in sorted(subject):
        if k.endswith("s") and k[:-1] in subject and k not in fam_title:
            subject.discard(k)
            merged.append(k)
    # Plural forms the release itself put in a title layer, and how many of them are
    # name-like enough to reach the merge step above.
    tl = set(fam_title) | set(ms_title) | set(env_title)
    plural_title = sorted(k for k in tl if k.endswith("s") and k[:-1] in tl)

    citation = {k for k in bib if k not in subject and k not in LABEL_WORDS
                and k not in JUNK_WORDS
                and not word_like(k) and not acronym(k) and not macro(k)
                and not any(c.isdigit() for c in k)}

    body_ms = collections.defaultdict(set)
    for p in tex_files():
        d = dir_of(p)
        t = prose(p.read_text(encoding="utf-8", errors="replace"))
        for m in CAPTOK.finditer(t):
            k = key(m.group(0))
            if k in subject:
                body_ms[k].add(d)

    def famset(k):
        s = set(fam_title.get(k, ())) | {f for f, _ in ms_title.get(k, ())}
        s |= set(env_title.get(k, ())) | body.get(k, set()) | bib.get(k, set())
        for stem, d, fp in decl.get(k, ()):
            s |= {f for f, r in LEDGER.items() if stem in r["chal"].split("|")}
        return {f for f in s if f}

    rows = []
    for k in sorted(subject | citation):
        role = "subject" if k in subject else "citation"
        rows.append({
            "name": k,
            "role": role,
            "fams": sorted(famset(k)),
            "fam_title_fams": sorted(fam_title.get(k, ())),
            "ms_title": ms_title.get(k, []),
            "env_title_fams": sorted(f for f in env_title.get(k, ()) if f),
            "env_hits": env_hits.get(k, []),
            "body_fams": sorted(f for f in body.get(k, ()) if f),
            "body_ms": sorted(body_ms.get(k, ())) if role == "subject" else [],
            "decl": sorted(set(decl.get(k, ()))),
            "bib_fams": sorted(f for f in bib.get(k, ()) if f),
            "cap": cap[k],
            "mid": mid[k],
            "low": low[k],
            "variants": [v for v, _ in variants[k].most_common(8)],
        })
    meta = {
        "tex_files": sum(1 for _ in tex_files()),
        "env_count": env_count,
        "bib_entries": bib_entries,
        "bib_author_keys": len(bib),
        "title_cands": len(title_cands),
        # Sorted: Counter insertion order follows set iteration order over the
        # candidates, which is not stable across runs.
        "rejected": dict(sorted(rejected.items())),
        "subject": len(subject),
        "citation": len(citation),
        "decl_tokens": len(decl),
        "decl_entries": len({(stem, d) for v in decl.values() for stem, d, _ in v}),
        "decl_top": sorted(((len({(stem, d) for stem, d, _ in v}), k)
                            for k, v in decl.items()), key=lambda t: (-t[0], t[1]))[:8],
        "probe": [(k, cap[k], mid[k], low[k]) for k in PROBE_TOKENS],
        "merged": merged,
        "plural_title": len(plural_title),
        "plural_name_like": sum(1 for k in plural_title if name_like(k)),
        "escape_names": sorted(escape_names),
    }
    return rows, meta


def main(argv):
    rows, meta = measure()
    if "--json" in argv:
        json.dump({"rows": rows, "meta": meta}, sys.stdout, indent=1)
        return 0
    subject = [r for r in rows if r["role"] == "subject"]
    citation = [r for r in rows if r["role"] == "citation"]
    covered, subj_cov = set(), set()
    for r in rows:
        covered |= set(r["fams"])
    for r in subject:
        subj_cov |= set(r["fams"])
    order, _ = B.parse_overview()
    trace_by_fam, unlisted = B.parse_traces()
    tf = set(trace_by_fam)
    edges = sum(len(r["fams"]) for r in subject)
    multi = [r for r in subject if len(r["variants"]) > 1]
    hard = sorted((n, v) for n, v in meta["rejected"].items() if n != "family-title-via-bib")
    print(f"tex files scanned        {meta['tex_files']}")
    print(f"statement envs w/ title  {meta['env_count']}")
    print(f"bib entries parsed       {meta['bib_entries']}  author keys {meta['bib_author_keys']}")
    print(f"title candidates         {meta['title_cands']}  rejected {sum(v for _, v in hard)} {hard}")
    print(f"  via family title+bib   {meta['rejected'].get('family-title-via-bib', 0)}  "
          + " ".join(meta["escape_names"]))
    print(f"declarations             {meta['decl_entries']} entries  {meta['decl_tokens']} tokens  "
          + " ".join("%s:%d" % (k, n) for n, k in meta["decl_top"]))
    print("probe tokens             " + " ".join(
        "%s=%d/%d" % (k, m, l) for k, c, m, l in meta["probe"]))
    print(f"plural merge             {len(meta['merged'])} merged "
          f"({' '.join(meta['merged'])})  {meta['plural_title']} plural forms in a title "
          f"layer, {meta['plural_name_like']} name-like")
    print(f"names                    {len(rows)}  subject {len(subject)}  citation-only {len(citation)}")
    print(f"subject edges            {edges} family-name edges over {len(subj_cov)} families")
    print(f"subject singletons       {sum(1 for r in subject if len(r['fams']) == 1)}")
    print(f"subject max              {max(((len(r['fams']), r['name']) for r in subject))}")
    print(f"spelling variants        {len(multi)} subject names with >1 surface form in prose")
    print(f"names with no family     {sum(1 for r in rows if not r['fams'])}")
    print(f"families with a hit      {len(covered)} of {len(order)}  no-hit {len(set(order) - covered)}")
    print(f"trace families covered   {len(tf & subj_cov)} of {len(tf)} by subject  all {len(tf & covered)}")
    print(f"trace families           {' '.join(sorted(tf))}")
    print(f"unlisted traces          {' '.join(sorted(unlisted)) if unlisted else 'none'}")
    top = sorted(subject, key=lambda r: (-len(r["fams"]), r["name"]))[:12]
    print("top subject names        " + " ".join(
        "%s:%d" % (r["name"], len(r["fams"])) for r in top))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Measure the shared-bibliography graph over the .bib files under preprints/.

Report-only: writes nothing. Every count in notes/citations.md comes from this report.

Method, stated once so the page can quote it:

  Population.  Every `preprints/**/*.bib` file, owned by the path component after `preprints`
  (never `parts[-2]` -- the files sit at depths 4, 5, 6 and 9). Manuscripts are the unit; a
  manuscript maps to a family through notes/subfindings.tsv, and a family to a discipline through
  notes/catalog.tsv.

  Entries.  `@type{key,` at line start; the body runs to the next line-start `@`.

  Work identity.  Two entries are the same work when their titles normalize equal: LaTeX accent
  macros folded to their base letter, `\\& \\% \\_ \\-` unescaped, remaining `\\command` removed,
  braces and math delimiters dropped, U+2019/U+2018 folded to ASCII apostrophe, NFKD with combining
  marks dropped, lowercased, every non-alphanumeric run collapsed to one space.

  Sharing.  A manuscript carries the *set* of its normalized titles. A work is shared when its set
  of owning manuscripts has size >= 2. A pair edge exists when two manuscripts share >= k titles;
  a cluster is a connected component of that pair graph. k is quoted with every count.

  Cited, not just listed.  A key counts as cited when it appears in a `\\cite...{...}` locator
  anywhere in the manuscript's own `.tex` tree.

  Release-internal works.  An entry is release-labelled when its body contains `OpenAI Math
  Release`; its target is the `preprints/<dir>/` component of the `\\href{...pdf}` in the body. This
  is the rule notes/links.tsv records for its 397-entry / 396-edge row.

Static reading only: never run lake, lean, or comparator. Run twice and diff -- the report must be
identical.

Usage:
    python3 notes/scripts/extract_citations.py
"""

import collections
import csv
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PREPRINTS = os.path.join(ROOT, "preprints")
LEDGER = os.path.join(ROOT, "notes", "catalog.tsv")
SUBFINDINGS = os.path.join(ROOT, "notes", "subfindings.tsv")

ENTRY = re.compile(r"^\s*@\s*(\w+)\s*\{\s*([^,]*)\s*,", re.M)
ATLINE = re.compile(r"^\s*@", re.M)
ACCENT = re.compile(r"\\(?:['`^~=\".](?![a-zA-Z])|c|v|u|H|k|r|d|b|t|o)\{?([a-zA-Z])\}?")
CITE = re.compile(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])?\{([^}]*)\}")
RELEASE_HREF = re.compile(r"\\href\{[^}]*/preprints/([^/]+)/[^}]*\.pdf\}")
THRESHOLDS = (1, 2, 3, 5, 10)
CLUSTER_K = (1, 5, 10)
TOP_N = 20


def ranked(counter, n=None):
    """most_common with ties broken by key, so the report is byte-stable."""
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return items if n is None else items[:n]



def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def bib_files():
    out = []
    for dirpath, dirs, files in os.walk(PREPRINTS):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".bib"):
                out.append(os.path.join(dirpath, f))
    return sorted(out, key=rel)


def owner(path):
    return rel(path).split("/")[1]


def read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def field(body, name):
    """Raw value of `name = {...}` (or `name = "..."`) in an entry body, or None."""
    m = re.search(r"\b%s\s*=\s*([{\"\"])" % name, body, re.I)
    if not m:
        return None
    j = m.end()
    depth = 1
    k = j
    while k < len(body) and depth:
        c = body[k]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                break
        k += 1
    return body[j:k]


def norm_title(s):
    s = ACCENT.sub(r"\1", s)
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_").replace("\\-", "")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)


def entries(text):
    """(type, key, body, start_line) for every @-entry, body cut at the next line-start @."""
    heads = list(ENTRY.finditer(text))
    bounds = [m.start() for m in ATLINE.finditer(text)]
    out = []
    for i, m in enumerate(heads):
        nxt = len(text)
        for b in bounds:
            if b > m.end():
                nxt = b
                break
        out.append((m.group(1).lower(), m.group(2).strip(), text[m.end():nxt],
                    text.count("\n", 0, m.start()) + 1 + m.group(0).count("\n")))
    return out


def ledger_rows():
    with open(LEDGER, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def manuscript_map():
    man2fam = {}
    with open(SUBFINDINGS, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r.get("kind") == "manuscript":
                man2fam[r["path"].split("/")[1]] = r["fam"]
    return man2fam


def tex_tree(man):
    base = os.path.join(PREPRINTS, man)
    for dirpath, dirs, files in os.walk(base):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".tex"):
                yield os.path.join(dirpath, f)


def cite_keys(man):
    out = set()
    for p in tex_tree(man):
        for m in CITE.finditer(read(p)):
            for k in m.group(1).split(","):
                if k.strip():
                    out.add(k.strip())
    return out


def main():
    files = bib_files()
    rows = ledger_rows()
    led = {r["fam"]: r for r in rows}
    man2fam = manuscript_map()

    # ---- population -------------------------------------------------------
    owners = collections.Counter(owner(p) for p in files)
    types = collections.Counter()
    keys = collections.Counter()
    titles = collections.defaultdict(set)          # manuscript -> {norm title}
    verbatim = collections.defaultdict(collections.Counter)  # norm title -> Counter(verbatim form)
    where = collections.defaultdict(dict)  # norm title -> {verbatim form: (path, line) first seen}
    entry_keys = collections.defaultdict(set)      # manuscript -> {bib keys}
    release = collections.defaultdict(set)         # manuscript -> {release dirs cited}
    release_count = collections.Counter()          # manuscript -> release-labelled entry count
    n_entries = 0
    release_entries = 0
    for p in files:
        man = owner(p)
        text = read(p)
        for ty, key, body, line in entries(text):
            n_entries += 1
            types[ty] += 1
            keys[key] += 1
            entry_keys[man].add(key)
            ti = field(body, "title")
            if ti:
                nt = norm_title(ti)
                if nt:
                    titles[man].add(nt)
                    verbatim[nt][ti.strip()] += 1
                    where[nt].setdefault(ti.strip(), (rel(p), line))
            if "OpenAI Math Release" in body:
                release_entries += 1
                release_count[man] += 1
                for m in RELEASE_HREF.finditer(body):
                    release[man].add(m.group(1))

    men = sorted(titles)
    # A .bib can sit in a superseded manuscript dir that the ledger does not list; those owners
    # carry no family, so they are reported and excluded from every family/discipline join.
    unowned = [m for m in men if m not in man2fam]
    men = [m for m in men if m in man2fam]
    n_man = sum(int(r["paps"]) for r in rows)
    print("bib files: %d  owner manuscripts: %d  of %d listed manuscript dirs"
          % (len(files), len(owners), n_man))
    print("owners with >1 .bib: %d (max %d)"
          % (sum(1 for v in owners.values() if v > 1), max(owners.values())))
    depth = collections.Counter(len(rel(p).split("/")) for p in files)
    print("path depth histogram: " + " ".join("%d:%d" % (d, n) for d, n in sorted(depth.items())))
    print("families covered: %d  disciplines covered: %d  owners outside the ledger: %d"
          % (len({man2fam[m] for m in men}), len({led[man2fam[m]]["discipline"] for m in men}),
             len(unowned)))
    print("entries: %d  types: %s"
          % (n_entries, " ".join("%s %d" % (t, n) for t, n in ranked(types))))
    print("distinct keys: %d  keys used by more than one manuscript: %d"
          % (len(keys), sum(1 for v in keys.values() if v > 1)))
    keymen = collections.defaultdict(set)
    for p2 in files:
        for ty, key, body, line in entries(read(p2)):
            keymen[key].add(owner(p2))
    print("top keys by owning manuscripts:")
    for k, s2 in ranked({k: len(v) for k, v in keymen.items() if len(v) > 1}, 10):
        print("  %2d  %s" % (len(keymen[k]), k))

    # ---- cited, not just listed -------------------------------------------
    all_keys = sum(len(v) for v in entry_keys.values())
    cited = sum(len(v & cite_keys(m)) for m, v in entry_keys.items())
    fracs = sorted(len(v & cite_keys(m)) / len(v) for m, v in entry_keys.items() if v)
    print("cited keys: %d of %d manuscript-key pairs appear in a \\cite locator" % (cited, all_keys))
    print("per-manuscript cited fraction: min %.3f median %.3f max %.3f; manuscripts at 0: %d; at >=0.9: %d"
          % (fracs[0], fracs[len(fracs) // 2], fracs[-1],
             sum(1 for x in fracs if x == 0), sum(1 for x in fracs if x >= 0.9)))

    # ---- sharing ----------------------------------------------------------
    inv = collections.defaultdict(set)
    for m in men:
        for nt in titles[m]:
            inv[nt].add(m)
    shared = {nt: s for nt, s in inv.items() if len(s) >= 2}
    print("distinct works: %d  shared by >=2 manuscripts: %d  by >=3: %d  by >=5: %d  by >=10: %d"
          % (len(inv), len(shared),
             sum(1 for s in shared.values() if len(s) >= 3),
             sum(1 for s in shared.values() if len(s) >= 5),
             sum(1 for s in shared.values() if len(s) >= 10)))
    print("manuscripts sharing nothing: %d"
          % sum(1 for m in men if not any(m in s for s in shared.values())))
    print("shared works crossing a family boundary: %d  crossing a discipline boundary: %d"
          % (sum(1 for s in shared.values() if len({man2fam[m] for m in s}) > 1),
             sum(1 for s in shared.values()
                 if len({led[man2fam[m]]["discipline"] for m in s}) > 1)))

    def rep(nt):
        """Most frequent verbatim form (ties: lexicographically first) and the first entry
        carrying *that* form, so a quoted title sits at its own anchor."""
        best = ranked(verbatim[nt])[0][0]
        path, line = where[nt][best]
        return best, path, line

    print("top shared works (manuscripts owning the work):")
    for nt, s in sorted(shared.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:TOP_N]:
        t, path, line = rep(nt)
        print("  %3d  %s  [%s:%d]" % (len(s), t, path, line))

    # ---- pairs ------------------------------------------------------------
    pairs = collections.Counter()
    for nt, s in shared.items():
        ms = sorted(s)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                pairs[(ms[i], ms[j])] += 1
    disc = {m: led[man2fam[m]]["discipline"] for m in men}
    fam = {m: man2fam[m] for m in men}
    for k in THRESHOLDS:
        ps = [(a, b, v) for (a, b), v in pairs.items() if v >= k]
        print("pairs sharing >=%d titles: %d  same-family %d  cross-discipline %d"
              % (k, len(ps), sum(1 for a, b, v in ps if fam[a] == fam[b]),
                 sum(1 for a, b, v in ps if disc[a] != disc[b])))
    print("max pair overlap: %d shared titles" % max(pairs.values()))
    print("manuscripts sharing >=1 title with a manuscript of another family: %d of %d"
          % (len({m for (a, b) in pairs if fam[a] != fam[b] for m in (a, b)}), len(men)))
    print("top pairs by shared titles:")
    for (a, b), v in sorted(pairs.items(), key=lambda kv: (-kv[1], kv[0][0], kv[0][1]))[:12]:
        print("  %2d  %s(%s) x %s(%s) %s"
              % (v, fam[a], disc[a][:28], fam[b], disc[b][:28],
                 "same-family" if fam[a] == fam[b] else "cross-family"))
    cross = [(a, b, v) for (a, b), v in pairs.items() if v >= 5 and disc[a] != disc[b]]
    print("cross-discipline pairs at >=5 shared titles: %d over %d families"
          % (len(cross), len({fam[a] for a, b, v in cross} | {fam[b] for a, b, v in cross})))
    for a, b, v in sorted(cross, key=lambda t: (-t[2], t[0], t[1])):
        print("  %2d  %s(%s) x %s(%s)" % (v, fam[a], disc[a], fam[b], disc[b]))
    hist = collections.Counter(tuple(sorted((disc[a], disc[b])))
                               for (a, b), v in pairs.items() if v >= 1)
    print("discipline pairs for >=1 shared title (top 10):")
    for (x, y), n in ranked(hist, 10):
        print("  %4d  %s x %s" % (n, x, y))

    # ---- clusters ---------------------------------------------------------
    for k in CLUSTER_K:
        adj = collections.defaultdict(set)
        for (a, b), v in pairs.items():
            if v >= k:
                adj[a].add(b)
                adj[b].add(a)
        seen = set()
        comps = []
        for n0 in sorted(adj):
            if n0 in seen:
                continue
            stack = [n0]
            comp = set()
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                seen.add(x)
                stack.extend(adj[x] - comp)
            comps.append(comp)
        comps.sort(key=lambda c: (-len(c), sorted(c)[0]))
        multi = [c for c in comps if len(c) > 1]
        print("clusters at pair threshold >=%d: %d components, %d with more than one manuscript, "
              "largest %d, spanning >=2 disciplines: %d"
              % (k, len(comps), len(multi), max((len(c) for c in multi), default=0),
                 sum(1 for c in multi if len({disc[m] for m in c}) > 1)))
        for c in multi[:12]:
            fams = sorted({fam[m] for m in c})
            ds = collections.Counter(disc[m] for m in c)
            print("  n=%2d fams=%2d disciplines=%d  %s  |  %s"
                  % (len(c), len(fams), len(ds), " ".join(fams),
                     ", ".join("%s %d" % (d, n) for d, n in ranked(ds))))

    # ---- release-internal layer -------------------------------------------
    rinv = collections.defaultdict(set)
    for m, s in release.items():
        if m not in fam:
            continue
        for d in s:
            rinv[d].add(m)
    rpairs = collections.Counter()
    for d, s in rinv.items():
        ms = sorted(s)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                rpairs[(ms[i], ms[j])] += 1
    rel_owned = sum(v for m, v in release_count.items() if m in fam)
    print("release-labelled entries: %d (%d in ledger-listed manuscripts)  "
          "manuscripts citing >=1 release work: %d  "
          "distinct release targets: %d  targets cited by >=2 manuscripts: %d"
          % (release_entries, rel_owned, sum(1 for s in release.values() if s), len(rinv),
             sum(1 for s in rinv.values() if len(s) >= 2)))
    print("pairs sharing a cited release work: %d  sharing >=2: %d  cross-family: %d"
          % (len(rpairs), sum(1 for v in rpairs.values() if v >= 2),
             sum(1 for (a, b) in rpairs if fam[a] != fam[b])))
    print("top release targets by citing manuscripts:")
    for d, s in sorted(rinv.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:10]:
        print("  %2d  %s" % (len(s), d))

    # ---- coverage caveat --------------------------------------------------
    inline = {}
    for d in sorted(os.listdir(PREPRINTS)):
        if not os.path.isdir(os.path.join(PREPRINTS, d)):
            continue
        n = 0
        for p in tex_tree(d):
            n += len(re.findall(r"\\begin\{thebibliography\}", read(p)))
        inline[d] = n
    listed = set(man2fam)
    no_bib = [d for d in listed if d not in owners]
    print("listed manuscripts with no .bib: %d of %d, of which %d carry an inline thebibliography "
          "and %d carry neither"
          % (len(no_bib), len(listed), sum(1 for d in no_bib if inline[d] > 0),
             sum(1 for d in no_bib if inline[d] == 0)))
    print("manuscripts with both a .bib and an inline thebibliography: %d"
          % sum(1 for d in owners if inline.get(d, 0) > 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())

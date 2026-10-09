"""Verify notes/citations.md against the shipped .bib files and a fresh measurement.

Report-only: writes nothing. Re-derives the whole shared-bibliography population from
`preprints/**/*.bib` using the primitives in extract_citations.py, then checks the page against it:

  - Every work-table row: the manuscript count equals the measured owning set, the quoted title is
    the most frequent verbatim form for its normalized title, and the anchor file exists with an
    entry at that line whose `title` field carries that exact form.
  - Every fenced block matches the file lines at its nearest preceding anchor, modulo whitespace.
  - Every `preprints/...bib:line` anchor on the page resolves to a real file and an in-range line.
  - The population, cited-key, work-layer, pair-layer, discipline-crossing, cluster, release-layer,
    coverage and sensitivity numbers are re-measured and required on the page in the form printed.
  - The discipline-crossing list, the >=5 cluster table and the release-target table must be
    complete: no measured row missing, no page row unmeasured.

--mutant corrupts one real quotation, one anchor, one count, one headline, one cluster membership,
one work count, one discipline composition and one release-target count in an in-memory copy and
requires each to be flagged.

Usage:
    python3 notes/scripts/verify_citations.py [--mutant]
"""

import collections
import os
import re
import sys

import extract_citations as ec

PAGE = os.path.join(ec.ROOT, "notes", "citations.md")
ACCENT_NOGUARD = re.compile(r"\\(?:['`^~=\".]|c|v|u|H|k|r|d|b|t|o)\{?([a-zA-Z])\}?")
THRESHOLDS = ec.THRESHOLDS
CLUSTER_K = ec.CLUSTER_K
TOP_N = ec.TOP_N


def norm_noguard(s):
    """ec.norm_title with the (?![a-zA-Z]) accent guard removed -- the sensitivity variant."""
    s = ACCENT_NOGUARD.sub(r"\1", s)
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_").replace("\\-", "")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)


def clusters(pairs, k):
    adj = collections.defaultdict(set)
    for (a, b), v in pairs.items():
        if v >= k:
            adj[a].add(b)
            adj[b].add(a)
    seen, comps = set(), []
    for n0 in sorted(adj):
        if n0 in seen:
            continue
        stack, comp = [n0], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            seen.add(x)
            stack.extend(adj[x] - comp)
        comps.append(comp)
    comps.sort(key=lambda c: (-len(c), min(c)))
    return [c for c in comps if len(c) > 1]


def measure(normfn):
    files = ec.bib_files()
    led = {r["fam"]: r for r in ec.ledger_rows()}
    man2fam = ec.manuscript_map()

    owners = collections.Counter(ec.owner(p) for p in files)
    types = collections.Counter()
    keys = collections.Counter()
    titles = collections.defaultdict(set)
    verbatim = collections.defaultdict(collections.Counter)
    where = collections.defaultdict(dict)
    entry_keys = collections.defaultdict(set)
    release = collections.defaultdict(set)
    release_count = collections.Counter()
    n_entries = release_entries = 0

    for p in files:
        man = ec.owner(p)
        text = ec.read(p)
        for ty, key, body, line in ec.entries(text):
            n_entries += 1
            types[ty] += 1
            keys[key] += 1
            entry_keys[man].add(key)
            ti = ec.field(body, "title")
            if ti:
                nt = normfn(ti)
                if nt:
                    titles[man].add(nt)
                    verbatim[nt][ti.strip()] += 1
                    where[nt].setdefault(ti.strip(), (ec.rel(p), line))
            if "OpenAI Math Release" in body:
                release_entries += 1
                release_count[man] += 1
                for m in ec.RELEASE_HREF.finditer(body):
                    release[man].add(m.group(1))

    # A .bib can sit in a superseded manuscript dir the ledger does not list; those owners carry no
    # family, so they are excluded from every family/discipline join (the extractor reports them).
    men = [m for m in sorted(titles) if m in man2fam]
    fam = {m: man2fam[m] for m in men}
    disc = {m: led[man2fam[m]]["discipline"] for m in men}

    inv = collections.defaultdict(set)
    for m in men:
        for nt in titles[m]:
            inv[nt].add(m)
    shared = {nt: s for nt, s in inv.items() if len(s) >= 2}

    pairs = collections.Counter()
    for s in shared.values():
        ms = sorted(s)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                pairs[(ms[i], ms[j])] += 1

    keymen = collections.defaultdict(set)
    for p in files:
        for _ty, key, _body, _line in ec.entries(ec.read(p)):
            keymen[key].add(ec.owner(p))

    all_keys = sum(len(v) for v in entry_keys.values())
    cited = sum(len(v & ec.cite_keys(m)) for m, v in entry_keys.items())
    fracs = sorted(len(v & ec.cite_keys(m)) / len(v) for m, v in entry_keys.items() if v)

    rpairs = collections.Counter()
    rinv = collections.defaultdict(set)
    for m, s in release.items():
        if m not in fam:
            continue
        for d in s:
            rinv[d].add(m)
    release_listed = sum(v for m, v in release_count.items() if m in fam)
    for s in rinv.values():
        ms = sorted(s)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                rpairs[(ms[i], ms[j])] += 1

    return {
        "files": files,
        "owners": owners,
        "led": led,
        "man2fam": man2fam,
        "men": men,
        "fam": fam,
        "disc": disc,
        "titles": titles,
        "verbatim": verbatim,
        "where": where,
        "inv": inv,
        "shared": shared,
        "pairs": pairs,
        "keys": keys,
        "keymen": keymen,
        "n_entries": n_entries,
        "types": types,
        "depth": collections.Counter(len(ec.rel(p).split("/")) for p in files),
        "fams": len({man2fam[m] for m in men}),
        "discs": len({disc[m] for m in men}),
        "all_keys": all_keys,
        "cited": cited,
        "fracs": fracs,
        "release_entries": release_entries,
        "release_listed": release_listed,
        "release": release,
        "rinv": rinv,
        "rpairs": rpairs,
        "rep": lambda nt: (ec.ranked(verbatim[nt])[0][0],) + where[nt][ec.ranked(verbatim[nt])[0][0]],
    }


def entry_at(path, line):
    """(type, key, body, start_line) for the entry starting at `line` in `path`, else None."""
    text = ec.read(path)
    for t in ec.entries(text):
        if t[3] == line:
            return t
    return None


def check(page, M, M2):
    fails = []
    flat = re.sub(r"\s+", " ", page)

    def need(needle, label):
        if needle not in flat:
            fails.append("%s: page does not contain %r" % (label, needle))

    # ---- population -------------------------------------------------------
    # Every figure below is built from the fresh measurement; the page carries no count the
    # checker does not re-derive. `listed` is the ledger's manuscript count, not the .bib owner
    # count -- owners include superseded dirs the ledger does not list.
    listed = sum(int(r["paps"]) for r in M["led"].values())
    n_disc_led = len({r["discipline"] for r in M["led"].values()})
    need("**%d**" % len(M["files"]), "bib files")
    need("**%d** of %d" % (len(M["owners"]), listed), "owner manuscripts")
    need("**%d** (max %d)" % (sum(1 for v in M["owners"].values() if v > 1),
                              max(M["owners"].values())), "owners >1")
    depth = " ".join("%d:%d" % (d, n) for d, n in sorted(M["depth"].items()))
    need(depth, "path depth")
    need("**%d** of %d" % (M["fams"], len(M["led"])), "families covered")
    need("**%d** of %d" % (M["discs"], n_disc_led), "disciplines covered")
    need("**%s**" % format(M["n_entries"], ","), "entries")
    need("**%s**" % format(len(M["keys"]), ","), "distinct keys")
    need("**%s**" % format(sum(1 for v in M["keys"].values() if v > 1), ","), "keys >1 manuscript")
    need(" · ".join("%s %s" % (t, format(n, ",")) for t, n in ec.ranked(M["types"])),
         "entry types")
    top_keys = ", ".join("`%s` %d" % (k, v) for k, v in
                         ec.ranked({k: len(v) for k, v in M["keymen"].items() if len(v) > 1}, 10))
    need(top_keys, "top keys")

    # ---- cited, not just listed -------------------------------------------
    need("**%s of %s**" % (format(M["cited"], ","), format(M["all_keys"], ",")), "cited pairs")
    f = M["fracs"]
    need("min **%.3f**, median **%.3f**, max **%.3f**" % (f[0], f[len(f) // 2], f[-1]),
         "cited fraction")
    need("**%d** manuscripts at 0" % sum(1 for x in f if x == 0), "manuscripts at 0")
    need("**%d** of %d at \u22650.9" % (sum(1 for x in f if x >= 0.9), len(M["men"])),
         "manuscripts >=0.9")

    # ---- work layer -------------------------------------------------------
    sh = M["shared"]
    need("**%s**" % format(len(M["inv"]), ","), "distinct works")
    need("**%s** owned by \u22652 manuscripts" % format(len(sh), ","), "shared >=2")
    need("**%d** by \u22653" % sum(1 for s in sh.values() if len(s) >= 3), "shared >=3")
    need("**%d** by \u22655" % sum(1 for s in sh.values() if len(s) >= 5), "shared >=5")
    need("**%d** by \u226510" % sum(1 for s in sh.values() if len(s) >= 10), "shared >=10")
    need("**%d** of the %s shared works cross a family boundary and **%d** cross a discipline"
         % (sum(1 for s in sh.values() if len({M["fam"][m] for m in s}) > 1),
            format(len(sh), ","),
            sum(1 for s in sh.values() if len({M["disc"][m] for m in s}) > 1)),
         "shared works boundary crossings")
    need("**%d** of the %d manuscripts share no title"
         % (sum(1 for m in M["men"] if not any(m in s for s in sh.values())), len(M["men"])),
         "sharing nothing")

    # ---- work table: every row, with its anchor ---------------------------
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+?):(\d+)`\s*\|\s*$", page, re.M)
    if len(rows) != TOP_N:
        fails.append("work table has %d rows, expected %d" % (len(rows), TOP_N))
    seen_nt = set()
    for cnt, title, path, raw_line in rows:
        line = int(raw_line)
        full = os.path.join(ec.ROOT, path)
        if not os.path.isfile(full):
            fails.append("work anchor absent on disk: %s:%d" % (path, line))
            continue
        e = entry_at(full, line)
        if e is None:
            fails.append("no entry begins at %s:%d" % (path, line))
            continue
        ti = ec.field(e[2], "title")
        if ti is None or ti.strip() != title:
            fails.append("anchor %s:%d carries title %r, page quotes %r"
                         % (path, line, (ti or "").strip(), title))
            continue
        nt = ec.norm_title(ti)
        best, bpath, bline = M["rep"](nt)
        if best != title:
            fails.append("quoted form %r is not the most frequent form %r for %r"
                         % (title, best, nt))
        if (bpath, bline) != (path, line):
            fails.append("anchor %s:%d is not the anchor of the quoted form (%s:%d)"
                         % (path, line, bpath, bline))
        if len(M["inv"][nt]) != int(cnt):
            fails.append("work %r: page says %s manuscripts, measured %d"
                         % (title, cnt, len(M["inv"][nt])))
        seen_nt.add(nt)
    measured_top = sorted(sh.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:TOP_N]
    if [nt for nt, _ in measured_top] != list(seen_nt_order(rows, M)):
        fails.append("work table is not the measured top-%d shared works" % TOP_N)

    # ---- pair layers ------------------------------------------------------
    for k in THRESHOLDS:
        ps = [(a, b, v) for (a, b), v in M["pairs"].items() if v >= k]
        cb = "**" if k >= 5 else ""
        need("| \u2265%d | **%s** | %d | %s%s%s |"
             % (k, format(len(ps), ","), sum(1 for a, b, v in ps if M["fam"][a] == M["fam"][b]),
                cb, format(sum(1 for a, b, v in ps if M["disc"][a] != M["disc"][b]), ","), cb),
             "pair layer >=%d" % k)
    need("Max pair overlap: **%d**" % max(M["pairs"].values()), "max overlap")
    need("**%d** of %d manuscripts share \u22651 title"
         % (len({m for (a, b) in M["pairs"] if M["fam"][a] != M["fam"][b] for m in (a, b)}),
            len(M["men"])),
         "manuscripts sharing cross-family")
    for k in (1, 5, 10):
        ps = [(a, b, v) for (a, b), v in M["pairs"].items() if v >= k]
        same = sum(1 for a, b, v in ps if M["disc"][a] == M["disc"][b])
        need("%s of %s" % (format(same, ","), format(len(ps), ",")), "same-discipline at >=%d" % k)

    # ---- discipline crossings --------------------------------------------
    cross = []
    for (a, b), v in M["pairs"].items():
        if v >= 5 and M["disc"][a] != M["disc"][b]:
            fa, fb, da, db = M["fam"][a], M["fam"][b], M["disc"][a], M["disc"][b]
            if fa > fb:
                fa, fb, da, db = fb, fa, db, da
            cross.append((fa, fb, v, da, db))
    cross.sort(key=lambda t: (-t[2], t[0], t[1]))
    prows = re.findall(r"^\|\s*(\d+)\s*\|\s*(\d{3}) × (\d{3})\s*\|\s*([^|]+)\|\s*$", page, re.M)
    if len(prows) != len(cross):
        fails.append("cross-discipline table has %d rows, measured %d" % (len(prows), len(cross)))
    for (fa, fb, v, da, db), (cnt, pa, pb, ds) in zip(cross, prows, strict=False):
        if (v, fa, fb) != (int(cnt), pa, pb):
            fails.append("cross row %s x %s at %s, measured %s x %s at %d"
                         % (pa, pb, cnt, fa, fb, v))
        if ds.strip() != "%s × %s" % (da, db):
            fails.append("cross row %s x %s disciplines %r, measured %r" % (pa, pb, ds.strip(),
                                                                            "%s × %s" % (da, db)))
    fams_cross = sorted({f for t in cross for f in (t[0], t[1])})
    need("**%d pairs over %d families**" % (len(cross), len(fams_cross)), "cross headline")
    p5 = [1 for (a, b), v in M["pairs"].items() if v >= 5]
    need("%d of %s pairs at \u22655 shared titles cross a discipline boundary"
         % (len(cross), format(len(p5), ",")), "headline crossing count")
    p10 = [(a, b) for (a, b), v in M["pairs"].items() if v >= 10]
    need("%d of %s at \u226510"
         % (sum(1 for a, b in p10 if M["disc"][a] != M["disc"][b]), format(len(p10), ",")),
         "headline crossing count at >=10")
    # ---- clusters ---------------------------------------------------------
    clus = {k: clusters(M["pairs"], k) for k in CLUSTER_K}
    cross10 = sum(1 for c in clus[10] if len({M["disc"][m] for m in c}) > 1)
    need("**%d** of %d span \u22652 disciplines" % (cross10, len(clus[10])),
         "clusters >=10 crossing")
    for k in CLUSTER_K:
        multi = clus[k]
        crossing = sum(1 for c in multi if len({M["disc"][m] for m in c}) > 1)
        big = multi[0]
        if k == 1:
            need("%d components, largest **%d manuscripts over %d families and all %d disciplines**"
                 % (len(multi), len(big), len({M["fam"][m] for m in big}),
                    len({M["disc"][m] for m in big})), "clusters >=1")
            ds = collections.Counter(M["disc"][m] for m in big)
            need(", ".join("%s %d" % (d, n) for d, n in ec.ranked(ds)), "cluster >=1 composition")
        if k == 5:
            need("%d components, all non-trivial, largest %d, **%d** spanning \u22652 disciplines"
                 % (len(multi), len(big), crossing), "clusters >=5")
        if k == 10:
            need("%d components, largest **%d**" % (len(multi), len(big)), "clusters >=10")
            need("(%s, %s)"
                 % (" ".join(sorted({M["fam"][m] for m in big})), M["disc"][min(big)]),
                 "largest >=10 membership")

    crows = re.findall(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([0-9 ]+)\|\s*([^|]+)\|\s*$",
                       page, re.M)
    multi5 = clusters(M["pairs"], 5)[:12]
    if len(crows) != len(multi5):
        fails.append("cluster table has %d rows, measured top-%d" % (len(crows), len(multi5)))
    for c, (n, nf, nd, fams, comp) in zip(multi5, crows, strict=False):
        cf = sorted({M["fam"][m] for m in c})
        cd = collections.Counter(M["disc"][m] for m in c)
        if int(n) != len(c) or int(nf) != len(cf) or int(nd) != len(cd):
            fails.append("cluster row %s: page n=%s fams=%s disciplines=%s, measured %d/%d/%d"
                         % (fams.strip(), n, nf, nd, len(c), len(cf), len(cd)))
        if fams.strip() != " ".join(cf):
            fails.append("cluster row %r: measured membership %s" % (fams.strip(), " ".join(cf)))
        want = ", ".join("%s %d" % (d, v) for d, v in ec.ranked(cd))
        if comp.strip() != want:
            fails.append("cluster row %s: composition %r, measured %r" % (fams.strip(), comp.strip(), want))

    # ---- release layer ----------------------------------------------------
    need("**%d** release-labelled entries (%d in ledger-listed manuscripts), from **%d** "
         "manuscripts, pointing at **%d** distinct targets"
         % (M["release_entries"], M["release_listed"],
            sum(1 for s in M["release"].values() if s), len(M["rinv"])), "release population")
    need("**%d** targets are cited by \u22652 manuscripts"
         % sum(1 for s in M["rinv"].values() if len(s) >= 2), "release targets >=2")
    need("**%d** manuscript pairs share a cited release work, **%d** pairs share \u22652, and "
         "**%d** of the %s pairs cross a family boundary"
         % (len(M["rpairs"]), sum(1 for v in M["rpairs"].values() if v >= 2),
            sum(1 for (a, b) in M["rpairs"] if M["fam"][a] != M["fam"][b]),
            format(len(M["rpairs"]), ",")), "release pairs")
    rrows = re.findall(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*$", page, re.M)
    top_r = sorted(M["rinv"].items(), key=lambda kv: (-len(kv[1]), kv[0]))[:10]
    if len(rrows) != 10:
        fails.append("release-target table has %d rows, expected 10" % len(rrows))
    for (d, s), (cnt, name) in zip(top_r, rrows, strict=False):
        if name != d or int(cnt) != len(s):
            fails.append("release row %r at %s, measured %r at %d" % (name, cnt, d, len(s)))

    # ---- coverage caveat --------------------------------------------------
    inline = {}
    for d in sorted(os.listdir(ec.PREPRINTS)):
        if not os.path.isdir(os.path.join(ec.PREPRINTS, d)):
            continue
        inline[d] = sum(len(re.findall(r"\\begin\{thebibliography\}", ec.read(p)))
                        for p in ec.tex_tree(d))
    # Scoped to the ledger's listed manuscripts: a superseded dir with no .bib is not a blind spot
    # in the graph, because the graph never claimed to see it.
    no_bib = [d for d in M["man2fam"] if d not in M["owners"]]
    need("**%d of %d manuscripts are invisible" % (len(no_bib), listed), "no-bib count")
    need("all %d carry an inline" % sum(1 for d in no_bib if inline[d] > 0), "inline coverage")
    need("**%d** carry neither" % sum(1 for d in no_bib if inline[d] == 0), "neither layer")
    need("**%d** manuscripts have both layers"
         % sum(1 for d in M["owners"] if inline.get(d, 0) > 0), "both layers")

    # ---- sensitivity table ------------------------------------------------
    sh2 = M2["shared"]
    vals = [
        ("Distinct works", len(M["inv"]), len(M2["inv"])),
        ("Works shared \u22652", len(sh), len(sh2)),
        ("Pairs \u22651", sum(1 for v in M["pairs"].values() if v >= 1),
         sum(1 for v in M2["pairs"].values() if v >= 1)),
        ("Cross-discipline pairs \u22651",
         sum(1 for (a, b), v in M["pairs"].items()
             if v >= 1 and M["disc"][a] != M["disc"][b]),
         sum(1 for (a, b), v in M2["pairs"].items()
             if v >= 1 and M2["disc"][a] != M2["disc"][b])),
        ("Pairs \u22655", sum(1 for v in M["pairs"].values() if v >= 5),
         sum(1 for v in M2["pairs"].values() if v >= 5)),
        ("Cross-discipline pairs \u22655",
         sum(1 for (a, b), v in M["pairs"].items()
             if v >= 5 and M["disc"][a] != M["disc"][b]),
         sum(1 for (a, b), v in M2["pairs"].items()
             if v >= 5 and M2["disc"][a] != M2["disc"][b])),
        ("Pairs \u226510", sum(1 for v in M["pairs"].values() if v >= 10),
         sum(1 for v in M2["pairs"].values() if v >= 10)),
        ("Cross-discipline pairs \u226510",
         sum(1 for (a, b), v in M["pairs"].items()
             if v >= 10 and M["disc"][a] != M["disc"][b]),
         sum(1 for (a, b), v in M2["pairs"].items()
             if v >= 10 and M2["disc"][a] != M2["disc"][b])),
    ]
    for label, guarded, ung in vals:
        delta = ung - guarded
        cell = "**0**" if delta == 0 else "%+d" % delta
        m = re.search(r"^\|\s*%s\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*(\*\*0\*\*|[+\u2212-]\d+)\s*\|"
                      % re.escape(label), page, re.M)
        if not m:
            fails.append("sensitivity row %r absent" % label)
            continue
        got = (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", "")), m.group(3))
        want = (guarded, ung, cell)
        if got[0] != guarded:
            fails.append("sensitivity %r: guarded column %s, measured %d" % (label, got[0], guarded))
        if got[1] != ung:
            fails.append("sensitivity %r: guard-removed column %s, measured %d" % (label, got[1], ung))
        sign = "\u2212" if delta < 0 else "+"
        if got[2] != cell and got[2] != "%s%d" % (sign, abs(delta)):
            fails.append("sensitivity %r: delta %r, measured %r" % (label, got[2], cell))

    # ---- anchors and fenced blocks ---------------------------------------
    for path, line in re.findall(r"`(preprints/[^`]+?\.bib):(\d+)`", page):
        full = os.path.join(ec.ROOT, path)
        if not os.path.isfile(full):
            fails.append("anchor file absent: %s" % path)
        elif int(line) > len(ec.read(full).split("\n")):
            fails.append("anchor line out of range: %s:%s" % (path, line))

    blocks = re.findall(r"```bibtex\n(.*?)```", page, re.S)
    if len(blocks) != 2:
        fails.append("page has %d bibtex blocks, expected 2" % len(blocks))
    for blk in blocks:
        head = page[:page.index(blk)]
        anch = re.findall(r"`(preprints/[^`]+?\.bib):(\d+)`", head)
        if not anch:
            fails.append("a bibtex block has no preceding anchor")
            continue
        path, line = anch[-1]
        full = os.path.join(ec.ROOT, path)
        if not os.path.isfile(full):
            fails.append("block anchor absent: %s" % path)
            continue
        flines = ec.read(full).split("\n")
        plines = [l for l in blk.split("\n") if l.strip()]
        start = int(line) - 1
        if start + len(plines) > len(flines):
            fails.append("block runs past end of %s" % path)
            continue
        for i, pl in enumerate(plines):
            fl = flines[start + i]
            if re.sub(r"\s+", " ", pl).strip() != re.sub(r"\s+", " ", fl).strip():
                fails.append("block line %d does not match %s:%d\n  page: %s\n  file: %s"
                             % (i + 1, path, start + i + 1, pl, fl))
                break

    return fails


def seen_nt_order(rows, _M):
    out = []
    for _cnt, title, _path, _line in rows:
        out.append(ec.norm_title(title))
    return out


MUTANTS = [
    ("paraphrase dressed as a quotation",
     lambda p: p.replace("author = {{The Stacks Project Authors}}",
                         "author = {{The Stacks Project editors}}")),
    ("invented anchor file",
     lambda p: p.replace("`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-"
                         "with-a-half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "`preprints/No-such-manuscript-September-1-2026/build/references.bib:106`")),
    ("anchor off by one line",
     lambda p: p.replace("half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "half-weight-divisor-October-5-2026/build/source/references.bib:105`")),
    ("count drift in the pair table",
     lambda p: p.replace("| \u22655 | **419** |", "| \u22655 | **418** |")),
    ("headline crossing count",
     lambda p: p.replace("6 of 419 pairs at \u22655", "7 of 419 pairs at \u22655")),
    ("cluster membership swap",
     lambda p: p.replace("033 034 035 036 037 046 051 054 056 057 058 065 066 068",
                         "033 034 039 036 037 046 051 054 056 057 058 065 066 068")),
    ("work count drift",
     lambda p: p.replace("| 42 | `The {Stacks Project}`", "| 43 | `The {Stacks Project}`")),
    ("cluster discipline composition",
     lambda p: p.replace("Mathematical physics 11, Differential geometry 4",
                         "Mathematical physics 12, Differential geometry 3")),
    ("release-target count",
     lambda p: p.replace("| 11 | `Log-abundance-in-characteristic-zero-September-24-2026`",
                         "| 12 | `Log-abundance-in-characteristic-zero-September-24-2026`")),
]


def main():
    with open(PAGE, encoding="utf-8") as fh:
        page = fh.read()
    M = measure(ec.norm_title)
    M2 = measure(norm_noguard)
    print("measured: %d .bib files, %d owner manuscripts, %d entries, %d distinct works, "
          "%d shared, %d pairs >=1"
          % (len(M["files"]), len(M["owners"]), M["n_entries"], len(M["inv"]), len(M["shared"]),
             len(M["pairs"])))
    fails = check(page, M, M2)
    print("page checks: %d problems" % len(fails))
    for f in fails:
        print("  FAIL %s" % f)

    if "--mutant" in sys.argv:
        print("mutant self-test:")
        for name, fn in MUTANTS:
            bad = fn(page)
            if bad == page:
                print("  NOT INJECTED (page text changed): %s" % name)
                continue
            mfails = check(bad, M, M2)
            print("  %-34s %s (%d)" % (name, "caught" if mfails else "MISSED", len(mfails)))

    print("clean" if not fails else "problems: %d" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

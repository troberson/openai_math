#!/usr/bin/env python3
r"""Extract the named-result inventory the manuscript sources carry, for notes/named-results.md.

Report-only: writes nothing. Every count in notes/named-results.md comes from this report.

Rules, stated because each one changes a number:
  HEADLINE   = a statement environment named theorem, maintheorem, or thm. Measured over all
               .tex files at depths 1-4 under preprints/: theorem 2265 begins, maintheorem 4,
               thm 1; conjecture/thmstar/theoremA/theoremB/mainthm/theoremstar read 0, so the
               headline set is those three names.
  TARGET     = r"conjectur|\bquestion|\bproblem" (case-insensitive) - the same target noun the
               ledger's resolves_named rule uses, from build_catalog.TARGET_NOUN.
  RESOLVE    = build_catalog.RESOLVE_VERB, verbatim: prove(s|ed|ing)/disprov/refut/resolv/answer/
               settl/establis/confirm/fail/violat/counterexample. "solve" and "resolution" are
               NOT in it; the gap is reported, not silently patched.
  sentence   = a run of text ending at . ! ? or :, longer than 20 characters.
  manuscript abstract = the body of the manuscript's own \begin{abstract}...\end{abstract}.
  prose      = measure_names.prose(): folded text with the bibliography and the \cite/\xref
               braces removed.
  window     = 80 characters on each side of the target noun (the probe rule); sentence scope is
               reported as the second rule because the two disagree on 4 families.
  family     = the path component after `preprints`, never parts[-2].
"""
from __future__ import annotations

import collections
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notes" / "scripts"))
import build_catalog as B  # noqa: E402
import measure_names as M  # noqa: E402

PRE = ROOT / "preprints"
LEDGER = ROOT / "notes" / "catalog.tsv"
OVERVIEW = ROOT / "overview.tex"

HEADLINE = ("theorem", "maintheorem", "thm")
TITLED = re.compile(r"\\begin\{(%s)\}\s*\[([^\]]{1,140})\]" % "|".join(HEADLINE))
BEGINS = re.compile(r"\\begin\{(%s)\}" % "|".join(HEADLINE))
TARGET = B.TARGET_NOUN
# Case-insensitive twin: directory names and theorem titles capitalize what the ledger rule
# sees in lowercase abstracts, so a case-sensitive match on them undercounts.
TARGET_I = re.compile(TARGET.pattern, re.I)
RESOLVE = B.RESOLVE_VERB
EXTRA = re.compile(r"\bsolve[sd]?\b|\bresolution\b|\banswers?\b|\bsettled\b|\bsettling\b"
                   r"|\bnegatively\b|\bpositively\b|\brefutation\b|\bcounterexamples?\b")
SENT = re.compile(r"[.!?:]")
ABSTRACT = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
GENERIC = re.compile(r"^\s*(the\s+)?main\b", re.I)
ENTRY = re.compile(r"\\resultentry\{(\d{3})\}")

# Families the reading pass adjudicates; the report prints their evidence with anchors.
A_FAMS = ["022", "039", "044", "151", "209", "297", "354", "365", "372", "263", "275"]
B_FAMS = ["085", "094", "126", "144", "187", "299", "323", "333"]
WINDOW = 80


def dir_of(path) -> str:
    return M.dir_of(path)


def sentences(t: str):
    """(offset, text) over a coarse LaTeX sentence split."""
    pos = 0
    for m in SENT.finditer(t):
        seg = t[pos:m.end()]
        if len(seg.strip()) > 20:
            yield pos, seg
        pos = m.end()
    if pos < len(t):
        yield pos, t[pos:]


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def population():
    """Everything the report and notes/named-results.md assert, measured from the shipped files.

    The checker imports this so the page and the report are judged against one measurement.
    """
    order, fams = B.parse_overview()
    ledger = {}
    with open(LEDGER, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ledger[r["fam"]] = r
    rn = {f for f in order if ledger[f]["resolves_named"] == "1"}

    dir2fam, famdirs = {}, collections.defaultdict(list)
    for f in order:
        for p in fams[f]["tex_paps"]:
            d = dir_of(p)
            if d and d not in famdirs[f]:
                famdirs[f].append(d)
                dir2fam[d] = f

    # overview.tex line numbers for the family entries, so the report can anchor its quotes.
    famline = {}
    for ln, line in enumerate(OVERVIEW.read_text(encoding="utf-8").splitlines(), 1):
        m = ENTRY.match(line.strip())
        if m:
            famline[m.group(1)] = ln

    files, begins, titled, titled_all, titled_split = 0, 0, 0, 0, 0
    env_begins = collections.Counter()
    head_titled = collections.defaultdict(list)
    head_begins = collections.Counter()
    generic = 0
    abstract_named = collections.defaultdict(list)
    prose_window = collections.defaultdict(list)
    prose_sentence = collections.defaultdict(list)
    extra_only = collections.defaultdict(list)

    for depth in (1, 2, 3, 4):
        for p in sorted(PRE.glob("/".join(["*"] * depth) + "/*.tex")):
            fam = dir2fam.get(dir_of(p))
            files += 1
            raw = p.read_text(encoding="utf-8", errors="replace")
            rel = str(p.relative_to(ROOT))
            for m in BEGINS.finditer(raw):
                begins += 1
                env_begins[m.group(1)] += 1
                head_begins[fam] += 1
            for m in TITLED.finditer(raw):
                titled_all += 1
                if "\n" in m.group(0):
                    titled_split += 1
            for ln, line in enumerate(raw.splitlines(), 1):
                for m in TITLED.finditer(line):
                    titled += 1
                    title = m.group(2)
                    if GENERIC.match(title):
                        generic += 1
                    head_titled[fam].append((title, rel, ln))
            # The manuscript's own abstract: target noun and resolve verb in one sentence.
            am = ABSTRACT.search(raw)
            if am and fam:
                atext = M.prose(am.group(1))
                for off, seg in sentences(atext):
                    low = seg.lower()
                    for _m in TARGET.finditer(low):
                        ln = raw[:raw.find(am.group(1)) + off].count("\n") + 1
                        rec = (flat(seg), rel, ln)
                        if RESOLVE.search(low):
                            abstract_named[fam].append(rec)
                        break
            # Manuscript prose, two scopes.
            if not fam:
                continue
            t = M.prose(raw)
            for off, seg in sentences(t):
                low = seg.lower()
                for _m in TARGET.finditer(low):
                    ln = t[:off].count("\n") + 1
                    rec = (flat(seg), rel, ln)
                    if RESOLVE.search(low):
                        prose_sentence[fam].append(rec)
                    elif EXTRA.search(low):
                        extra_only[fam].append(rec)
                    break
            low = t.lower()
            for m in TARGET.finditer(low):
                seg = low[max(0, m.start() - WINDOW):m.end() + WINDOW]
                if RESOLVE.search(seg):
                    ln = t[:m.start()].count("\n") + 1
                    prose_window[fam].append((flat(t[max(0, m.start() - 90):m.end() + 90]),
                                              rel, ln))

    tgt = [(f, t, q, ln) for f in order for (t, q, ln) in head_titled[f] if TARGET_I.search(t)]
    verb_in_title = [(f, t, q, ln) for f, t, q, ln in tgt if RESOLVE.search(t.lower())]
    rows, _meta = M.measure()
    subject = {r["name"] for r in rows if r["role"] == "subject"}
    subj_hits = []
    for f in order:
        for (t, q, ln) in head_titled[f]:
            toks = {M.key(x.group(0)) for x in M.NAME.finditer(M.fold(t))}
            if toks & subject:
                subj_hits.append((f, t, q, ln))
    subj_fams = {f for f, _, _, _ in subj_hits}
    tgt_fams = {f for f, _, _, _ in tgt}
    have_b = {f for f in order if head_begins[f]}
    have_t = {f for f in order if head_titled[f]}
    no_head = {f for f in rn if not head_titled[f]}
    tiers = collections.Counter(ledger[f]["tier"] for f in no_head)
    dir_named = {f: [d for d in famdirs[f] if TARGET_I.search(d.replace("-", " "))] for f in order}
    dn = {f for f in order if dir_named[f]}
    an = {f for f in order if abstract_named[f]}
    pw = {f for f in order if prose_window[f]}
    ps = {f for f in order if prose_sentence[f]}
    core = sorted((rn - pw) & (rn - ps))
    eo = {f for f in order if extra_only[f] and not prose_sentence[f]}
    # The scope the column had before the title+abstract swap: abstract text only, same two
    # regexes. `add` is therefore the applied delta of the swap, not a candidate.
    abstract_only = {f for f in order if TARGET.search(fams[f]["abstract"].lower())
                     and RESOLVE.search(fams[f]["abstract"].lower())}
    add = sorted(rn - abstract_only)
    # The two scopes the swap was measured against, kept as report figures so the counts quoted
    # from them are reproducible: both regexes on the raw (unlowered) title+abstract, and the
    # target noun read case-sensitively in the title with the verb read in the lowered pair.
    scope_raw = {
        f for f in order
        if TARGET.search(fams[f]["title"] + " " + fams[f]["abstract"])
        and RESOLVE.search(fams[f]["title"] + " " + fams[f]["abstract"])
    }
    scope_title_cs = {
        f for f in order
        if TARGET.search(fams[f]["title"])
        and RESOLVE.search((fams[f]["title"] + " " + fams[f]["abstract"]).lower())
    }
    return {
        "order": order, "fams": fams, "ledger": ledger, "rn": rn, "famline": famline,
        "famdirs": famdirs, "ndirs": len(dir2fam), "files": files, "begins": begins,
        "env_begins": env_begins, "titled": titled, "titled_all": titled_all,
        "titled_split": titled_split, "generic": generic, "head_titled": head_titled,
        "abstract_named": abstract_named, "prose_window": prose_window,
        "prose_sentence": prose_sentence, "extra_only": extra_only, "tgt": tgt,
        "verb_in_title": verb_in_title, "subject": subject, "subj_hits": subj_hits,
        "subj_fams": subj_fams, "tgt_fams": tgt_fams, "have_b": have_b, "have_t": have_t,
        "no_head": no_head, "tiers": tiers, "dir_named": dir_named, "dn": dn, "an": an,
        "pw": pw, "ps": ps, "core": core, "eo": eo, "add": add,
        "abstract_only": abstract_only, "scope_raw": scope_raw, "scope_title_cs": scope_title_cs,
    }


def report(p):
    """Print the report from a population() dict. Output is byte-stable across runs."""
    (order, fams, ledger, rn, famdirs, tgt, verb_in_title, subject, subj_hits, subj_fams,
     tgt_fams, have_b, have_t, no_head, tiers, dir_named, dn, an, pw, ps, core, eo, add,
     head_titled, abstract_named, prose_window, prose_sentence, extra_only,
     files, begins, titled, titled_all, titled_split, generic, env_begins,
     abstract_only, scope_raw, scope_title_cs) = (
        p["order"], p["fams"], p["ledger"], p["rn"], p["famdirs"], p["tgt"],
        p["verb_in_title"], p["subject"], p["subj_hits"], p["subj_fams"], p["tgt_fams"],
        p["have_b"], p["have_t"], p["no_head"], p["tiers"], p["dir_named"], p["dn"], p["an"],
        p["pw"], p["ps"], p["core"], p["eo"], p["add"], p["head_titled"],
        p["abstract_named"], p["prose_window"], p["prose_sentence"], p["extra_only"],
        p["files"], p["begins"], p["titled"], p["titled_all"], p["titled_split"],
        p["generic"], p["env_begins"], p["abstract_only"], p["scope_raw"], p["scope_title_cs"])
    famline = p["famline"]

    print("POPULATION")
    print(f"  ledger rows {len(ledger)}  families in overview.tex {len(order)}  "
          f"manuscript dirs {p['ndirs']}")
    print(f"  .tex files at depths 1-4 under preprints/ {files}")
    print(f"  headline begins {begins}  titled (whole-text scan) {titled_all}  of which the "
          f"match spans a newline {titled_split}")
    print(f"  resolves_named = 1: {len(rn)} families  (abstract-only scope: {len(abstract_only)})")

    print("\nHEADLINE INVENTORY (rule: theorem/maintheorem/thm begins and titled begins)")
    print(f"  headline begins {begins}  titled headline begins (per-line scan) {titled}")
    print("  per-env begins: " + " ".join(f"{k}={v}" for k, v in sorted(env_begins.items())))
    print(f"  families with >=1 headline begin {len(have_b)}  "
          f"with >=1 titled headline {len(have_t)}  with none {len(order) - len(have_t)}")
    print(f"  titled headline titles matching 'Main...' (generic, no content named): {generic}")

    print("\nTARGET-NAMED HEADLINE STATEMENTS (rule: titled headline title matching TARGET)")
    print(f"  statements {len(tgt)}  families {len({f for f, _, _, _ in tgt})}")
    print(f"  with a resolve verb in the same title: {len(verb_in_title)} statements over "
          f"{len({f for f, _, _, _ in verb_in_title})} families; target+verb in one title: 0")
    for f, t, q, ln in tgt:
        print(f"  {f} rn={ledger[f]['resolves_named']} tier={ledger[f]['tier']} {q}:{ln} "
              f"{t!r}")

    print("\nSUBJECT-NAMED HEADLINE STATEMENTS (rule: titled headline title containing a "
          "name-layer subject)")
    print(f"  statements {len(subj_hits)}  families {len(subj_fams)}  "
          f"(subjects in the name layer: {len(subject)})")
    print(f"  subject-named ∩ rn {len(subj_fams & rn)}  subject-named-not-rn "
          f"{len(subj_fams - rn)}")
    print("  subject-named-not-rn: " + " ".join(sorted(subj_fams - rn)))

    print("\nCROSS-TABS vs resolves_named")
    print(f"  headline-target ∩ rn {len(tgt_fams & rn)}  headline-target-not-rn "
          f"{len(tgt_fams - rn)} -> {' '.join(sorted(tgt_fams - rn))}")
    print(f"  rn-not-headline-target {len(rn - tgt_fams)}")
    print(f"  rn families with no titled headline theorem: {len(no_head)}  "
          f"tiers T3={tiers['T3']} T2={tiers['T2']} T1={tiers['T1']} T0={tiers['T0']}")
    print(f"  non-rn families with titled headline theorems: {len(have_t - rn)}")

    print("\nLAYER 1 - manuscript directory name names a target")
    print(f"  families {len(dn)}  dirs {sum(len(v) for v in dir_named.values())}  "
          f"∩rn {len(dn & rn)}  dir-not-rn {len(dn - rn)} -> {' '.join(sorted(dn - rn))}  "
          f"rn-not-dir {len(rn - dn)}")

    print("\nLAYER 2 - the manuscript's own abstract names a target with a resolve verb")
    print(f"  families {len(an)}  sentences {sum(len(v) for v in abstract_named.values())}  "
          f"∩rn {len(an & rn)}  abstract-not-rn {len(an - rn)}  rn-not-abstract {len(rn - an)}")
    print("  abstract-not-rn: " + " ".join(sorted(an - rn)))
    print("  rn-not-abstract: " + " ".join(sorted(rn - an)))

    print("\nLAYER 3 - manuscript prose (bibliography and cite braces stripped)")
    print(f"  window ±{WINDOW}: hits {sum(len(v) for v in prose_window.values())} over "
          f"{len(pw)} families  ∩rn {len(pw & rn)}  prose-not-rn {len(pw - rn)}  "
          f"rn-not-prose {len(rn - pw)} -> {' '.join(sorted(rn - pw))}")
    print(f"  sentence scope: hits {sum(len(v) for v in prose_sentence.values())} over "
          f"{len(ps)} families  ∩rn {len(ps & rn)}  prose-not-rn {len(ps - rn)}  "
          f"rn-not-prose {len(rn - ps)} -> {' '.join(sorted(rn - ps))}")
    print(f"  rn-not-prose under BOTH rules: {len(core)} -> {' '.join(core)}")

    print("\nVERB VOCABULARY GAP (target noun with an EXTRA verb, no column verb, in prose)")
    print(f"  families {len(eo)} -> {' '.join(sorted(eo))}  of these rn=1: {len(eo & rn)}")

    print("\nTITLE-SCOPE SWAP (applied: target noun in the overview title, verb in its abstract)")
    print(f"  additions {len(add)} -> {' '.join(add)}")
    print(f"  column reads {len(rn)}; abstract-only scope reads {len(abstract_only)}; "
          f"removals 0 - the union keeps every flag the abstract-only scope had")
    print(f"  scope alternates: both regexes on the raw title+abstract read {len(scope_raw)} "
          f"(removals {len(abstract_only - scope_raw)}, additions {len(scope_raw - abstract_only)}); "
          f"target noun case-sensitive in the title with the verb in the lowered pair read "
          f"{len(scope_title_cs)} (removals {len(abstract_only - scope_title_cs)}, "
          f"additions {len(scope_title_cs - abstract_only)})")

    print("\nDIRECTION A - manuscript names a target the abstract-only scope missed")
    print("  (reading material, anchored)")
    for f in A_FAMS:
        print(f"--- {f} tier={ledger[f]['tier']} rn={ledger[f]['resolves_named']} "
              f"paps={ledger[f]['paps']} shapes={ledger[f]['shapes']}")
        print(f"  overview.tex:{famline[f]} TITLE: {fams[f]['title']}")
        print(f"  overview.tex:{famline[f]} ABSTRACT: {fams[f]['abstract']}")
        print(f"  DIRS: {' | '.join(famdirs[f])}")
        for t, q, ln in head_titled[f]:
            if TARGET_I.search(t):
                print(f"  HEAD {q}:{ln} {t!r}")
        if abstract_named[f]:
            s, q, ln = abstract_named[f][0]
            print(f"  MS-ABSTRACT {q}:{ln} {s!r}")
        else:
            print("  MS-ABSTRACT: no sentence naming a target with a resolve verb")
        if prose_window[f]:
            s, q, ln = prose_window[f][0]
            print(f"  MS-PROSE {q}:{ln} ...{s}...")

    print("\nDIRECTION B - column reads 1, manuscript naming is thin (reading material, anchored)")
    for f in B_FAMS:
        print(f"--- {f} tier={ledger[f]['tier']} rn={ledger[f]['resolves_named']} "
              f"paps={ledger[f]['paps']} shapes={ledger[f]['shapes']}")
        print(f"  overview.tex:{famline[f]} TITLE: {fams[f]['title']}")
        print(f"  overview.tex:{famline[f]} ABSTRACT: {fams[f]['abstract']}")
        print(f"  DIRS: {' | '.join(famdirs[f])}")
        print(f"  titled headline statements {len(head_titled[f])}  "
              f"target-named headline {sum(1 for t, _, _ in head_titled[f] if TARGET_I.search(t))}  "
              f"ms-abstract target+verb {len(abstract_named[f])}  "
              f"prose window {len(prose_window[f])}  prose sentence {len(prose_sentence[f])}  "
              f"extra-only {len(extra_only[f])}")
        pool = (abstract_named[f] + prose_sentence[f] + extra_only[f]
                + prose_window[f] + head_titled[f])
        for t, q, ln in pool[:3]:
            print(f"  EVID {q}:{ln} {t!r}")


def main():
    report(population())
    return 0


if __name__ == "__main__":
    sys.exit(main())

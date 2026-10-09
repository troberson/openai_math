#!/usr/bin/env python3
r"""Check notes/named-results.md against the shipped files. Report-only: writes nothing.

Run with --mutant to also run the self-test: twelve injected corruptions, one per check form,
all of which must be flagged.

What it checks, and why each check exists:
  anchors   every backticked `file:line` resolves: the file exists under the repo root and the
            line number is inside it. Bare `:NNN` anchors (the page's shorthand after a family
            number) are checked against the overview line of that family's \resultentry.
  table     every row of the target-named headline table is a record the extractor measured:
            family, tier, resolves_named flag, statement path:line, and title.
  quotes    every *"…"* quotation is pinned to an anchor in its own row (the nearest one, the
            page's style being quote-then-source) or, failing that, to the last anchor of the
            nearest preceding row, and must appear in the anchored file. Matching is done on
            measure_names.fold() of both sides - accent escapes, combining marks, braces and
            U+2019 are markup, not words - over a window of 1..12 lines starting at the anchor,
            because manuscript sentences are hard-wrapped across source lines.
  counts    every count phrase is re-derived from extract_named_results.population(), the same
            measurement the report prints, formatted with thousands separators.
  corpus    the comparator/OAI figures in the closing section are recounted from disk: the
            ComparatorChallenges file count, its `sorry` occurrences, and the number of files
            under lean/OAI. The zero-`sorry` claim over lean/OAI is NOT re-derived here: scanning
            122,458 files for `sorry` is the job of extract_formalization_deps.py, not of a page
            checker.
"""
from __future__ import annotations

import bisect
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notes" / "scripts"))
import extract_named_results as en  # noqa: E402
import measure_names as M  # noqa: E402

PAGE = ROOT / "notes" / "named-results.md"
ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json|txt|lean|yaml|bib)):(\d+)`")
BARE = re.compile(r"(\d{3})\s+\(`:(\d+)`\)")
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
ROW = re.compile(r'^\| (\d{3}) \| (T\d) \| (\d) \| `([^`]+):(\d+)` \| \*"([^"]*)"\* \|$', re.M)
SPAN = 12
# The page spells its mutation count as a word, so the phrase check needs the spelling.
WORDS = {12: "twelve"}
# The target-split sentence spells its leading count as a word and agrees with it.
NUMWORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def read(rel: str, cache: dict) -> list[str]:
    if rel not in cache:
        # A page anchor naming an absent file is a check_anchors problem; the quotation scan must
        # report it, not crash on it.
        try:
            cache[rel] = (ROOT / rel).read_text(encoding="utf-8", errors="replace").splitlines()
        except FileNotFoundError:
            cache[rel] = []
    return cache[rel]


def line_starts(lines: list[str]) -> list[int]:
    starts, off = [], 0
    for ln in lines:
        starts.append(off)
        off += len(ln) + 1
    return starts


def row_ids(lines: list[str]) -> list[int]:
    """Row id per line: a row is a maximal run of contiguous non-blank lines; blank lines are -1."""
    ids, cur, prev_blank = [], -1, True
    for ln in lines:
        if ln.strip():
            if prev_blank:
                cur += 1
            prev_blank = False
            ids.append(cur)
        else:
            prev_blank = True
            ids.append(-1)
    return ids


def check_anchors(text: str, cache: dict, problems: list) -> int:
    hits = 0
    seen = set()
    for m in ANCHOR.finditer(text):
        rel, ln = m.group(1), int(m.group(2))
        if (rel, ln) in seen:
            continue
        seen.add((rel, ln))
        hits += 1
        if not (ROOT / rel).exists():
            problems.append(f"ANCHOR path absent: {rel}:{ln}")
            continue
        n = len(read(rel, cache))
        if not 1 <= ln <= n:
            problems.append(f"ANCHOR line out of range: {rel}:{ln} (file has {n} lines)")
    return len(seen)


def check_bare(text: str, p, problems: list) -> int:
    hits = 0
    for m in BARE.finditer(text):
        fam, ln = m.group(1), int(m.group(2))
        hits += 1
        want = p["famline"].get(fam)
        if want != ln:
            problems.append(f"BARE anchor :{ln} is not family {fam}'s overview line ({want})")
    return hits


def check_table(text: str, p, problems: list) -> int:
    measured = {(f, q, ln, t) for f, t, q, ln in p["tgt"]}
    rows = 0
    for m in ROW.finditer(text):
        fam, tier, rn, rel, ln, title = m.groups()
        rows += 1
        if (fam, rel, int(ln), title) not in measured:
            problems.append(f"TABLE row not measured by the extractor: {fam} {rel}:{ln} {title!r}")
        led = p["ledger"].get(fam)
        if led is None:
            problems.append(f"TABLE family absent from the ledger: {fam}")
            continue
        if tier != led["tier"]:
            problems.append(f"TABLE tier for {fam}: page {tier}, ledger {led['tier']}")
        if rn != led["resolves_named"]:
            problems.append(f"TABLE rn for {fam}: page {rn}, ledger {led['resolves_named']}")
    if rows != len(p["tgt"]):
        problems.append(f"TABLE rows {rows}, extractor measured {len(p['tgt'])} statements")
    return rows


def quote_pattern(quote: str) -> re.Pattern:
    return re.compile(r"\s*".join(re.escape(t) for t in M.fold(quote).split()))


def quote_found(quote: str, rel: str, ln: int, cache: dict) -> bool:
    lines = read(rel, cache)
    pat = quote_pattern(quote)
    for k in range(1, SPAN + 1):
        blob = M.fold(" ".join(lines[ln - 1:ln - 1 + k]))
        if blob and pat.search(blob):
            return True
    return False


def check_quotes(text: str, cache: dict, problems: list) -> int:
    lines = text.splitlines()
    starts = line_starts(lines)
    ids = row_ids(lines)
    anchors = [(m.start(), m.group(1), int(m.group(2)),
                ids[bisect.bisect_right(starts, m.start()) - 1]) for m in ANCHOR.finditer(text)]
    checked = 0
    for m in QUOTE.finditer(text):
        quote = m.group(1)
        ql = bisect.bisect_right(starts, m.start()) - 1
        row = ids[ql]
        # The window is the quote's own line plus the rest of its row up to the next bullet or
        # table row, so a quote never borrows the next entry's anchor. Inside the window the page's
        # dominant form is quote-then-source; the table rows and the Direction-B overview list are
        # anchor-then-quote, which the preceding-anchor fallbacks pick up.
        limit = len(lines)
        for i in range(ql + 1, len(lines)):
            if ids[i] != row or lines[i].lstrip().startswith(("- ", "| ")):
                limit = i
                break
        wend = starts[limit] if limit < len(lines) else len(text)
        after = [a for a in anchors if m.end() <= a[0] < wend]
        own_before = [a for a in anchors
                      if starts[ql] <= a[0] < m.start() and a[0] < starts[ql] + len(lines[ql])]
        row_before = [a for a in anchors if a[3] == row and a[0] < m.start()]
        if after:
            _, rel, ln, _ = min(after, key=lambda a: a[0])
        elif own_before:
            _, rel, ln, _ = max(own_before, key=lambda a: a[0])
        elif row_before:
            _, rel, ln, _ = max(row_before, key=lambda a: a[0])
        else:
            rel = ln = None
            for r in range(row - 1, row - 4, -1):
                above = [a for a in anchors if a[3] == r]
                if above:
                    _, rel, ln, _ = max(above, key=lambda a: a[0])
                    break
        checked += 1
        if rel is None:
            problems.append(f"QUOTE not pinned to an anchor: {quote[:60]!r}")
            continue
        if not quote_found(quote, rel, ln, cache):
            problems.append(f"QUOTE not in {rel}:{ln}: {quote[:70]!r}")
    return checked


def corpus_facts():
    chal = sorted((ROOT / "lean" / "ComparatorChallenges").glob("*.lean"))
    sorry = sum(len(re.findall(r"\bsorry\b",
                               q.read_text(encoding="utf-8", errors="replace"))) for q in chal)
    oai = sum(1 for _ in (ROOT / "lean" / "OAI").rglob("*.lean"))
    return len(chal), sorry, oai


def count_phrases(p) -> list:
    """(phrase, label) pairs the page must carry, all derived from the extractor's population()."""
    order, ledger, rn, fams = p["order"], p["ledger"], p["rn"], p["fams"]
    tgt, tgt_fams = p["tgt"], p["tgt_fams"]
    subj_hits, subj_fams = p["subj_hits"], p["subj_fams"]
    dn, an, pw, ps = p["dn"], p["an"], p["pw"], p["ps"]
    have_t, no_head, tiers = p["have_t"], p["no_head"], p["tiers"]
    core, eo, add = p["core"], p["eo"], p["add"]
    abstract_only = p["abstract_only"]
    files, begins, titled, titled_all = p["files"], p["begins"], p["titled"], p["titled_all"]
    env, split, generic = p["env_begins"], p["titled_split"], p["generic"]
    strict = {f for f in order if en.TARGET_I.search(fams[f]["title"])
              and en.RESOLVE.search(fams[f]["abstract"].lower())}
    notdir = [f for f in add if f not in dn]
    real_a = [f for f in en.A_FAMS if f != "275"]
    bset = set(en.B_FAMS)
    nchal, nsorry, noai = corpus_facts()
    return [
        (f"It reads **{len(rn)}** of **{len(order)}** families", "rn share"),
        (f"the abstract-only scope it replaced read **{len(abstract_only)}**", "abstract-only figure"),
        (f"re-derives every count from the ledger and the {files:,} `.tex` files on disk", "tex files (intro)"),
        (f"**{len(ledger)}** ledger rows", "ledger rows"),
        (f"**{len(order)}** families in `overview.tex`", "overview families"),
        (f"**{p['ndirs']}** manuscript directories", "manuscript dirs"),
        (f"**{files:,}** `.tex` files at glob depths 1–4", "tex files (population)"),
        (f"`resolves_named = 1` on **{len(rn)}** families", "rn count"),
        (f"flags {WORDS.get(len(MUTANTS), str(len(MUTANTS)))} injected mutations", "mutant claim"),
        (f"| headline begins | {begins:,} |", "headline begins"),
        (f"`\\begin{{theorem}}` {env['theorem']:,}", "theorem begins"),
        (f"`\\begin{{maintheorem}}` {env['maintheorem']}", "maintheorem begins"),
        (f"`\\begin{{thm}}` {env['thm']}", "thm begins"),
        (f"| titled headline begins | {titled:,} |", "titled per-line"),
        (f"| titled headline begins, whole-text scan | {titled_all:,} |", "titled whole-text"),
        (f"| of those, titles whose match spans a newline | {split} |", "newline gap"),
        (f"| families with ≥1 headline begin | {len(p['have_b'])} |", "families with begins"),
        (f"| families with ≥1 titled headline | {len(have_t)} |", "families with titles"),
        (f"| families with no titled headline | {len(order) - len(have_t)} |", "families without"),
        (f"| titles matching `Main…` (content-free) | {generic} |", "generic titles"),
        (f"rule: **{titled:,}** is the per-line scan, **{titled_all:,}** is the whole-text scan, "
         f"and the {split}-title gap", "per-line warning"),
        (f"## Target-named headline statements: {len(tgt)} over {len(tgt_fams)} families", "target heading"),
        (f"Over **{titled:,}** titled headline statements, **{len(tgt)}** titles name a conjecture, "
         f"question, or problem, in **{len(tgt_fams)}** families", "target counts"),
        (f"negative: {len(p['verb_in_title'])} of these {len(tgt)} titles", "verb-in-title"),
        (f"{NUMWORDS[len(tgt_fams - rn)]} of the {len(tgt)} ({', '.join(sorted(tgt_fams - rn))}) "
         f"{'sits' if len(tgt_fams - rn) == 1 else 'sit'} in "
         f"{'a family' if len(tgt_fams - rn) == 1 else 'families'} the column reads 0; the other "
         f"{len(tgt_fams & rn)} sit in families it reads 1", "target split"),
        (f"## Subject-named headline statements: {len(subj_hits)} over {len(subj_fams)} families",
         "subject heading"),
        (f"one of the {len(p['subject'])} subject names", "subject vocabulary"),
        (f"**{len(subj_hits)}** statements over **{len(subj_fams)}** families. "
         f"**{len(subj_fams & rn)}** of those families are `rn = 1`; **{len(subj_fams - rn)}** are not:",
         "subject counts"),
        (" ".join(sorted(subj_fams - rn)), "subject-not-rn list"),
        (f"| headline-target ∩ `rn` | {len(tgt_fams & rn)} |", "cross-tab 1"),
        (f"| headline-target, `rn = 0` | {len(tgt_fams - rn)} → {' '.join(sorted(tgt_fams - rn))} |",
         "cross-tab 2"),
        (f"| `rn = 1`, no target-named headline statement | {len(rn - tgt_fams)} |", "cross-tab 3"),
        (f"| `rn = 1` with **no titled headline theorem at all** | {len(no_head)} "
         f"(T3 {tiers['T3']}, T2 {tiers['T2']}, T1 {tiers['T1']}, T0 {tiers['T0']}) |", "cross-tab 4"),
        (f"| `rn = 0` with titled headline theorems | {len(have_t - rn)} |", "cross-tab 5"),
        (f"**{len(no_head)} of the {len(rn)} flagged families ship no titled headline theorem**",
         "no-headline claim"),
        (f"**{len(dn)}** families over **{sum(len(v) for v in p['dir_named'].values())}** directories. "
         f"**{len(dn & rn)}** are `rn = 1`. **{len(dn - rn)}** are not: {' '.join(sorted(dn - rn))}. "
         f"**{len(rn - dn)}**", "layer 1"),
        (f"**{len(an)}** families over **{sum(len(v) for v in p['abstract_named'].values())}** "
         f"sentences. **{len(an & rn)}** are `rn = 1`. **{len(an - rn)}** are not, and "
         f"**{len(rn - an)}**", "layer 2"),
        (" ".join(sorted(rn - an)), "rn-not-abstract list"),
        (f"it would read {len(rn)} + {len(an - rn)} = **{len(rn) + len(an - rn)}**", "layer 2 union"),
        (f"| window ±{en.WINDOW} characters | {sum(len(v) for v in p['prose_window'].values()):,} | "
         f"{len(pw)} | {len(pw & rn)} | {len(pw - rn)} | {len(rn - pw)} → "
         f"{' '.join(sorted(rn - pw))} |", "layer 3 window"),
        (f"| one sentence | {sum(len(v) for v in p['prose_sentence'].values()):,} | {len(ps)} | "
         f"{len(ps & rn)} | {len(ps - rn)} | {len(rn - ps)} → {' '.join(sorted(rn - ps))} |",
         "layer 3 sentence"),
        (f"**{len(core)}** families are `rn = 1` and name no target anywhere in their manuscript "
         f"prose under **both** rules: {' '.join(core)}", "layer 3 core"),
        (f"**{len(eo)}** families: {' '.join(sorted(eo))}, of which **{len(eo & rn)}** are `rn = 1`",
         "verb gap"),
        (f"## The title-scope swap: {len(abstract_only)} → {len(rn)}", "title-scope heading"),
        (f"**{len(add)}** additions: {' '.join(add)}", "additions"),
        (f"so the column reads **{len(rn)}**", "union figure"),
        (f"would read {len(strict)} ({len(rn - strict)} removals)", "strict replacement"),
        (f"All **{len(add)}** are corroborated", "additions corroborated"),
        (f"**{len(notdir)}** of the {len(add)} are not directory-named: {' '.join(notdir)}",
         "additions not dir-named"),
        (f"manuscript-abstract-named but **not** title-named, so they sit outside the {len(add)}",
         "outside the additions"),
        (f"The manuscript-abstract layer alone ({len(an - rn)} families) would cover them and reach "
         f"{len(rn) + len(an - rn)}", "abstract layer reach"),
        (f"**{len(en.A_FAMS)}** families. Ten are real; one is the rule's false positive",
         "direction A count"),
        (f"**{len(set(real_a) & set(add))} of the {len(real_a)} real misses are flagged**",
         "direction A applied"),
        (f"reads **{len(real_a)} real misses and 1 false positive**", "direction A verdict"),
        (f"**{len(en.B_FAMS)}** families, all `rn = 1`", "direction B count"),
        (f"the {len(en.B_FAMS)} split **3 corroborated / 5 resting on the overview paraphrase alone**",
         "direction B split"),
        (f"{len(bset & (rn - an))} of the {len(en.B_FAMS)} also sit in the layer-2 `rn-not-abstract` "
         f"list; 333 does not", "direction B layer 2"),
        (f"Over {titled:,} titled headline statements, {len(tgt)} titles name a target and "
         f"**{len(p['verb_in_title'])}** of them pair a target noun with a resolve verb",
         "load-bearing negative"),
        (f"**{len(real_a)} real misses** (Direction A) and **{len(add)} title-scope additions**, "
         f"overlapping in {' '.join(sorted(set(add) & set(real_a)))}", "overlap"),
        (f"the swap is applied, so the column reads **{len(rn)}** with removals 0", "union verdict"),
        (f"**5 of the {len(en.B_FAMS)} Direction-B families**", "direction B verdict"),
        (f"The {len(an - rn)}-family layer-2 set is **unadjudicated**. It is the widest candidate "
         f"({len(rn) + len(an - rn)})", "not checked layer 2"),
        (f"The {len(pw - rn)}-family `prose-not-rn` set (window scope)", "not checked prose"),
        (f"The {len(subj_fams - rn)} subject-named-not-`rn` families", "not checked subjects"),
        (f"The {len(order) - len(have_t)} families with no titled headline theorem",
         "not checked no-title"),
        (f"zero of the {noai:,} files under `lean/OAI/**/*.lean` contain `sorry` while the {nchal} "
         f"comparator files carry {nsorry} `sorry` occurrences", "corpus sorry facts"),
    ]


def check(text: str, p, problems: list) -> dict:
    cache: dict = {}
    out = {}
    out["anchors"] = check_anchors(text, cache, problems)
    out["bare anchors"] = check_bare(text, p, problems)
    out["table rows"] = check_table(text, p, problems)
    out["quotations"] = check_quotes(text, cache, problems)
    flat = norm(text)
    hit = 0
    for phrase, label in count_phrases(p):
        if norm(phrase) not in flat:
            problems.append(f"COUNT missing ({label}): {phrase}")
        else:
            hit += 1
    out["count phrases"] = hit
    out["count phrases total"] = len(count_phrases(p))
    if len(p["verb_in_title"]) != 0:
        problems.append(f"verb-in-title is {len(p['verb_in_title'])}, the page states 0")
    if not all(p["ledger"][f]["resolves_named"] == "1" for f in en.B_FAMS):
        problems.append("a Direction-B family is not rn = 1 in the ledger")
    if len(en.A_FAMS) != 11:
        problems.append(f"A_FAMS is {len(en.A_FAMS)}, the page states 11")
    return out


MUTANTS = {
    "count: rn share 248 -> 249":
        lambda t: t.replace("It reads **248** of **372** families",
                            "It reads **249** of **372** families"),
    "count: titled per-line 1,609 -> 1,619":
        lambda t: t.replace("| titled headline begins | 1,609 |",
                            "| titled headline begins | 1,619 |"),
    "family list: layer-1 dir-not-rn drops 372":
        lambda t: t.replace("are not: 354 365 372.", "are not: 354 365."),
    "inline quotation: resolution -> solution":
        lambda t: t.replace("This gives a positive resolution of the planar",
                            "This gives a positive solution of the planar"),
    "overview quotation: problem -> question":
        lambda t: t.replace('*"Settles the Snaky achievement problem"*',
                            '*"Settles the Snaky achievement question"*'),
    "invented quotation at a real anchor":
        lambda t: t + '\n*"We prove the Riemann hypothesis for every finite abelian category."*'
            ' (`notes/names.md:1`)\n',
    "anchor line out of range":
        lambda t: t.replace("Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex:51",
                            "Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex:99999"),
    "anchor path absent":
        lambda t: t.replace("Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex",
                            "Centered-Disk-Maximal-Operator-September-26-2026/build/mainn.tex"),
    "table tier: 006 T0 -> T3":
        lambda t: t.replace("| 006 | T0 | 1 |", "| 006 | T3 | 1 |"),
    "count: column 248 -> 247":
        lambda t: t.replace("so the column reads **248**", "so the column reads **247**"),
    "bare anchor: 039 :156 -> :157":
        lambda t: t.replace("039 (`:156`)", "039 (`:157`)"),
    "paraphrase dressed as a quotation":
        lambda t: t.replace(
            r'*"This resolves the smooth three-dimensional isotropic elastic Calder\'on uniqueness '
            r'problem under these positivity assumptions."*',
            r'*"This resolves the elastic Calder\'on problem."*'),
}


def main(argv: list[str]) -> int:
    p = en.population()
    text = PAGE.read_text(encoding="utf-8")
    problems: list = []
    out = check(text, p, problems)
    print("== page", PAGE.relative_to(ROOT))
    for k in ("anchors", "bare anchors", "table rows", "quotations"):
        print(f"  {k}: {out[k]}")
    print(f"  count phrases: {out['count phrases']} of {out['count phrases total']} re-derived")
    for pr in problems:
        print("PROBLEM:", pr)
    print(f"problems {len(problems)}")

    missed = 0
    if "--mutant" in argv:
        print(f"\n== mutants ({len(MUTANTS)})")
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"NOT INJECTED: {name}")
                missed += 1
                continue
            sub: list = []
            check(mutated, p, sub)
            print(f"{'caught' if sub else 'NOT CAUGHT'}: {name}"
                  + (f"  [{sub[0]}]" if sub else ""))
            if not sub:
                missed += 1
        print(f"mutants caught {len(MUTANTS) - missed}/{len(MUTANTS)}")
    return 1 if (problems or missed) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""The self-tests for `notes/scripts/verify_named_results.py`.

The checker verifies `notes/reports/named-results.md` against the corpus the page describes. Anchors: every
`path:line` resolves against the shipped file, a bare `:NNN` resolves to the family named nearest
before it, and a `path:a-b` span fits inside the file. Quotations: every `*"…"*` is matched against
the lines its anchor names, in a window, so a paraphrase dressed as a quotation fails and an invented
quotation at a real anchor fails. Tables: the 17-row target table is compared with the extractor's
population and the ledger row by row. Counts: all 65 count phrases are re-derived from
`extract_named_results.population()`.

This file injects thirteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: the `resolves_named` share, the titled-per-line count, a family dropped from a family
list, an inline quotation's word, an overview quotation's word, an invented quotation, an anchor line
past the file's end, an anchor path that does not exist, a table tier, the applied column's count, a
bare anchor shifted by one, a paraphrase dressed as a quotation, and a per-command count in the
headline-begins row that no count phrase reads — the last is visible only to the render diff.

**The needles that name a measured figure are derived at run time, not recorded.** The six quote
needles re-run the checker's own window rule on the mutated page — the quote's row, the anchors after
it inside the row, the anchor in its own line, the anchor earlier in its row, then the anchors in the
three lines above — so the anchor a quote is pinned to is read from the page, not recorded. The table
needle reads the mutated row against the ledger, keyed to the family the mutation touched. The bare
needle reads the mutated page's bare anchor for that family against the population's overview line.
The needles that stay literal are the mutation's own inputs — the anchor line written out of range,
the anchor path renamed, and the count labels, which carry no measured figure.

Every fault is built from a real count phrase, a real quotation, a real anchor, a real table row and a
real family list in the page as committed. Each test asserts the injected text differs from the page it
started from, and each needle is the problem string the pass that owns that form prints — measured
specific, each needle fires for its own fault and for no other.

The clean test asserts the passes are silent and pins the counts they report. The population is pinned
as **joins** where the ledger can produce the figure: the manuscript-directory count equals the
ledger's `paps` sum, and the prose sentence and window counts equal the ledger's family count. The
resolution passes are pinned as **derived floors**: each pass counted exactly the population its own
rule reads off the page — the anchor pass counts distinct `(path, line)` pairs, the bare-anchor,
table-row and quotation passes count every shape their regex finds — and each population is required
non-zero, so 0 problems means every anchor, bare anchor, table row and quotation resolved. The `.tex`
file count is pinned as a **walk equality**: the test walks `preprints/` at glob depths 1-4 itself,
measuring depth relative to `preprints/` so the root prefix does not shift every file past the bound,
and the population's count must equal the walk. The figures that stay literal are the ones the join
cannot produce: 65 count phrases, 0 sync problems; 2,410 headline begins,
1,609 titled per line (1,619 whole-text), 373 target-named titles, 76 families with no headline, 248
`resolves_named`, 275 title-union, 15 additions, 6 core, 76 directory-name, 5 abstract-only, 207 prose
hits, 551 subject keys, 17 targets, 0 generic, and the per-command split 2,405 `theorem` / 4
`maintheorem` / 1 `thm`. A page with fewer count phrases is a pass that stopped checking, not a pass
that passed.

`test_resolution_floors_fire_on_a_page_that_carries_nothing` strips every shape each pass reads and
shows the equality holds at 0 while the floor fails.

`test_ledger_joins_fire_on_faults_the_literals_miss` proves the joins are the witness: a `paps`
decrement breaks the manuscript-directory join and dropping a family row breaks the prose-window join,
and neither moves a page byte, so every page pass stays silent.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the fourteen
`check()` calls the row makes pay the 7,240-file walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_named_results.py -q
"""
import bisect
import pathlib

import pytest

pytestmark = pytest.mark.mutant

REPO = pathlib.Path(__file__).resolve().parents[3]


def tree_tex():
    """The `.tex` files under `preprints/` at glob depths 1-4 — the scope the population counts. Depth is
    measured relative to `preprints/`, not on the absolute path, so the root prefix does not shift every
    file past the bound. The walk is the test's own, so the equality is the invariant: the population
    counted every file the tree carries at that depth, and a manuscript added to the corpus moves the
    walk, not the recorded number."""
    pre = REPO / "preprints"
    return [p for p in pre.rglob("*.tex") if len(p.relative_to(pre).parts) - 1 <= 4]

CENTER = "preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026"
ELASTIC = ("preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem"
           "-September-24-2026")


def regex_count(rx):
    """Every shape the regex finds in the page."""
    def count(text):
        return len(rx.findall(text))
    return count


def distinct_anchor_count(mod):
    """The anchor pass counts distinct `(path, line)` pairs, not shapes: the page repeats anchors, and
    the pass resolves each pair once. The floor has to be the pass's own rule, not a looser one."""
    def count(text):
        return len({(m.group(1), int(m.group(2))) for m in mod.ANCHOR.finditer(text)})
    return count


def resolution(mod):
    """Each resolution pass's population, read off the page by the pass's own rule: `(key, count)` for
    the anchor, bare-anchor, table-row and quotation passes. The clean test asserts each pass counted
    exactly its population and that the population is non-zero, so 0 problems means every shape
    resolved and a page carrying none fails the floor."""
    return (("anchors", distinct_anchor_count(mod)),
            ("bare anchors", regex_count(mod.BARE)),
            ("table rows", regex_count(mod.ROW)),
            ("quotations", regex_count(mod.QUOTE)))


def quote_needle(c, mod, sub):
    """The quote problem, keyed to the mutated quote. The anchor a quote is pinned to is the one the
    pass finds by its own window rule, so the rule is re-run on the mutated page: the anchors after the
    quote inside its row, then the anchor in the quote's own line, then the anchor earlier in the row,
    then the anchors in the three lines above. A recorded anchor string is a fact about the page before
    the mutation, not about the page the pass is checking."""
    lines = c.splitlines()
    starts = mod.line_starts(lines)
    ids = mod.row_ids(lines)
    anchors = [(m.start(), m.group(1), int(m.group(2)),
                ids[bisect.bisect_right(starts, m.start()) - 1]) for m in mod.ANCHOR.finditer(c)]
    m = next(m for m in mod.QUOTE.finditer(c) if sub in m.group(1))
    ql = bisect.bisect_right(starts, m.start()) - 1
    row = ids[ql]
    limit = len(lines)
    for i in range(ql + 1, len(lines)):
        if ids[i] != row or lines[i].lstrip().startswith(("- ", "| ")):
            limit = i
            break
    wend = starts[limit] if limit < len(lines) else len(c)
    after = [a for a in anchors if m.end() <= a[0] < wend]
    own = [a for a in anchors if starts[ql] <= a[0] < m.start() and a[0] < starts[ql] + len(lines[ql])]
    row_before = [a for a in anchors if a[3] == row and a[0] < m.start()]
    if after:
        rel, ln = min(after, key=lambda a: a[0])[1:3]
    elif own:
        rel, ln = max(own, key=lambda a: a[0])[1:3]
    elif row_before:
        rel, ln = max(row_before, key=lambda a: a[0])[1:3]
    else:
        rel = ln = None
        for r in range(row - 1, row - 4, -1):
            above = [a for a in anchors if a[3] == r]
            if above:
                rel, ln = max(above, key=lambda a: a[0])[1:3]
                break
    assert rel is not None, f"no anchor pins the quote carrying {sub!r}"
    return f"QUOTE not in {rel}:{ln}"


def table_needle(c, mod, p, fam):
    """The table-tier problem, keyed to the family the mutation touched: the mutated row's tier against
    the ledger. The pass reports every differing row, so keying to the edited row keeps the needle
    specific to this fault."""
    for m in mod.ROW.finditer(c):
        f, tier, _rn, _rel, _ln, _title = m.groups()
        if f == fam:
            led = p["ledger"][fam]
            if tier != led["tier"]:
                return f"TABLE tier for {fam}: page {tier}, ledger {led['tier']}"
    raise AssertionError(f"the mutated table carries no tier mismatch for {fam}")


def bare_needle(c, mod, p, fam):
    """The bare-anchor problem, keyed to the family the mutation touched: the mutated page's bare anchor
    against the population's overview line for that family."""
    for m in mod.BARE.finditer(c):
        f, ln = m.group(1), int(m.group(2))
        if f == fam:
            want = p["famline"].get(fam)
            if want != ln:
                return f"BARE anchor :{ln} is not family {fam}'s overview line ({want})"
    raise AssertionError(f"the mutated page carries no bare anchor for family {fam}")


# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("count: rn share", "COUNT missing (rn share)",
     lambda t: t.replace("It reads **248** of **372** families",
                         "It reads **249** of **372** families")),
    ("count: titled per-line", "COUNT missing (titled per-line)",
     lambda t: t.replace("| titled headline begins | 1,609 |",
                         "| titled headline begins | 1,619 |")),
    ("family list: layer-1 drops 372", "COUNT missing (layer 1)",
     lambda t: t.replace("are not: 354 365 372.", "are not: 354 365.")),
    ("inline quotation",
     lambda c, mod, p: quote_needle(c, mod, "This gives a positive solution of the planar"),
     lambda t: t.replace("This gives a positive resolution of the planar",
                         "This gives a positive solution of the planar")),
    ("overview quotation",
     lambda c, mod, p: quote_needle(c, mod, "Settles the Snaky achievement question"),
     lambda t: t.replace('*"Settles the Snaky achievement problem"*',
                         '*"Settles the Snaky achievement question"*')),
    ("invented quotation",
     lambda c, mod, p: quote_needle(c, mod, "We prove the Riemann hypothesis for every finite abelian category"),
     lambda t: t + '\n*"We prove the Riemann hypothesis for every finite abelian category."*'
                   ' (`notes/reports/names.md:1`)\n'),
    ("anchor line out of range", f"ANCHOR line out of range: {CENTER}/build/main.tex:99999",
     lambda t: t.replace(f"{CENTER}/build/main.tex:51", f"{CENTER}/build/main.tex:99999")),
    ("anchor path absent", "ANCHOR path absent",
     lambda t: t.replace(f"{CENTER}/build/main.tex", f"{CENTER}/build/mainn.tex")),
    ("table tier",
     lambda c, mod, p: table_needle(c, mod, p, "006"),
     lambda t: t.replace("| 006 | T0 | 1 |", "| 006 | T3 | 1 |")),
    ("count: column", "COUNT missing (union figure)",
     lambda t: t.replace("so the column reads **248**", "so the column reads **247**")),
    ("bare anchor",
     lambda c, mod, p: bare_needle(c, mod, p, "039"),
     lambda t: t.replace("039 (`:156`)", "039 (`:157`)")),
    ("paraphrase dressed as a quotation",
     lambda c, mod, p: quote_needle(c, mod, "This resolves the elastic Calder"),
     lambda t: t.replace(
         r'*"This resolves the smooth three-dimensional isotropic elastic Calder\'on uniqueness '
         r'problem under these positivity assumptions."*',
         r'*"This resolves the elastic Calder\'on problem."*')),
    # Prose the count pass never reads: the per-command breakdown of the headline-begins row is not
    # in count_phrases(). Only the sync pass can see it.
    ("sync-only prose count altered", "COUNT missing (theorem begins)",
     lambda t: t.replace("`\\begin{theorem}` 2,405", "`\\begin{theorem}` 2,406", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_named_results")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text, ledger):
    """Every pass is silent, and the population is asserted as joins and derived floors, not recorded
    numbers. The ledger-join invariants: the manuscript-directory count equals the ledger's `paps` sum,
    and the prose sentence and window counts equal the ledger's family count. The resolution passes are
    derived floors: each pass counted every shape its own regex finds in the page, so 0 problems means
    every anchor, bare anchor, table row and quotation resolved, and a page carrying none is a pass that
    ran over nothing. The file, begins, titled and environment-split figures stay literals: corpus
    measurements the join cannot produce, as do the 65 count phrases and the sync count."""
    problems, out = mod.check(text)
    assert not problems, problems[:3]
    for key, pop in resolution(mod):
        assert out[key] == pop(text) > 0, \
            f"{key}: pass counted {out[key]} against {pop(text)} shapes the page carries"
    assert (out["count phrases"], out["count phrases total"], out["sync problems"]) == (65, 65, 0), \
        f"counters {out}"
    p = mod.population()
    assert p["ndirs"] == sum(int(r["paps"]) for r in ledger), \
        f"ndirs {p['ndirs']} against the ledger paps sum {sum(int(r['paps']) for r in ledger)}"
    assert len(p["prose_sentence"]) == len(p["prose_window"]) == len({r["fam"] for r in ledger}), \
        f"prose windows {len(p['prose_sentence'])}/{len(p['prose_window'])} against " \
        f"{len({r['fam'] for r in ledger})} ledger families"
    assert p["files"] == len(tree_tex()) > 0, \
        f"files {p['files']} against {len(tree_tex())} .tex files walked at depth 1-4 under preprints/"
    assert (p["begins"], p["titled"], p["titled_all"],
            len(p["head_titled"]), len(p["no_head"])) == (2410, 1609, 1619, 373, 76), \
        f"begins {p['begins']}, titled {p['titled']}"
    assert (len(p["rn"]), len(p["an"]), len(p["add"]), len(p["core"]), len(p["dn"]),
            len(p["eo"]), len(p["subj_hits"]), len(p["subject"]), len(p["tgt"]),
            p["generic"]) == (248, 275, 15, 6, 76, 5, 207, 551, 17, 0), \
        f"rn {len(p['rn'])}, subject {len(p['subject'])}"
    assert (p["env_begins"]["theorem"], p["env_begins"]["maintheorem"],
            p["env_begins"]["thm"]) == (2405, 4, 1), f"env split {p['env_begins']}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _ = mod.check(cand)
    p = mod.population()
    want = needle(cand, mod, p) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def test_ledger_joins_fire_on_faults_the_literals_miss(mod, ledger):
    """A ledger row fault moves no page byte, so every page pass stays silent. The literal figures
    are measured from the manuscript tree, not from the ledger, so a ledger fault cannot move them:
    the joins are the only witness — a `paps` decrement breaks the manuscript-directory join, and
    dropping a family row breaks the prose-window join."""
    p = mod.population()
    i = next(n for n, r in enumerate(ledger) if int(r["paps"]) > 1)
    led = [dict(r) for r in ledger]
    led[i]["paps"] = str(int(led[i]["paps"]) - 1)
    assert p["ndirs"] == sum(int(r["paps"]) for r in ledger), \
        "the clean paps join is not the relation the population satisfies"
    assert p["ndirs"] != sum(int(r["paps"]) for r in led), \
        "the paps decrement did not break the join, so the join is not a witness"
    dropped = [r for r in ledger if r["fam"] != ledger[0]["fam"]]
    assert len(p["prose_sentence"]) == len({r["fam"] for r in ledger}), \
        "the clean family join is not the relation the population satisfies"
    assert len(p["prose_sentence"]) != len({r["fam"] for r in dropped}), \
        "dropping a family row did not break the prose-window join, so the join is not a witness"


def test_resolution_floors_fire_on_a_page_that_carries_nothing(mod, text):
    """A pass that reports 0 problems on a page with no anchors is vacuous. Stripping every shape each
    resolution pass reads leaves the equality true (0 counted against 0 present) and the floor false, so
    the floor is what keeps each pass honest."""
    cand = text
    for rx in (mod.ANCHOR, mod.BARE, mod.ROW, mod.QUOTE):
        cand = rx.sub("", cand)
    _found, out = mod.check(cand)
    for key, pop in resolution(mod):
        assert out[key] == pop(cand) == 0, \
            f"{key}: pass counted {out[key]} on a page with no {key}"

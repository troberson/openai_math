"""The self-tests for `notes/scripts/verify_named_results.py`.

The checker verifies `notes/named-results.md` against the corpus the page describes. Anchors: every
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

Every fault is built from a real count phrase, a real quotation, a real anchor, a real table row and a
real family list in the page as committed. Each test asserts the injected text differs from the page it
started from, and each needle is the problem string the pass that owns that form prints — measured
specific, each needle fires for its own fault and for no other.

The clean test asserts the passes are silent and pins the counts they report: 61 anchors, 15 bare
anchors, 17 table rows, 61 quotations, 65 count phrases, 0 sync problems; and the population at 7,679
`.tex` files, 719 manuscript dirs, 2,410 headline begins, 1,609 titled per line (1,619 whole-text),
373 target-named titles, 76 families with no headline, 248 `resolves_named`, 275 title-union, 15
additions, 6 core, 76 directory-name, 5 abstract-only, 207 prose hits, 551 subject keys, 17 targets,
0 generic, 372 prose sentences and windows, and the per-command split 2,405 `theorem` / 4
`maintheorem` / 1 `thm`. A page with fewer anchors, quotations, table rows or phrases is a pass that
stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the fourteen
`check()` calls the row makes pay the 7,240-file walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_named_results.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

CENTER = "preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026"
ELASTIC = ("preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem"
           "-September-24-2026")

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
    ("inline quotation", f"QUOTE not in {CENTER}/build/main.tex:51: 'This gives a positive s",
     lambda t: t.replace("This gives a positive resolution of the planar",
                         "This gives a positive solution of the planar")),
    ("overview quotation", "QUOTE not in overview.tex:453: 'Settles the Snaky achievement question'",
     lambda t: t.replace('*"Settles the Snaky achievement problem"*',
                         '*"Settles the Snaky achievement question"*')),
    ("invented quotation", "QUOTE not in notes/names.md:1",
     lambda t: t + '\n*"We prove the Riemann hypothesis for every finite abelian category."*'
                   ' (`notes/names.md:1`)\n'),
    ("anchor line out of range", f"ANCHOR line out of range: {CENTER}/build/main.tex:99999",
     lambda t: t.replace(f"{CENTER}/build/main.tex:51", f"{CENTER}/build/main.tex:99999")),
    ("anchor path absent", "ANCHOR path absent",
     lambda t: t.replace(f"{CENTER}/build/main.tex", f"{CENTER}/build/mainn.tex")),
    ("table tier", "TABLE tier for 006: page T3, ledger T0",
     lambda t: t.replace("| 006 | T0 | 1 |", "| 006 | T3 | 1 |")),
    ("count: column", "COUNT missing (union figure)",
     lambda t: t.replace("so the column reads **248**", "so the column reads **247**")),
    ("bare anchor", "BARE anchor :157 is not family 039's overview line (156)",
     lambda t: t.replace("039 (`:156`)", "039 (`:157`)")),
    ("paraphrase dressed as a quotation", f"QUOTE not in {ELASTIC}/build/main.tex:46",
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


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, out = mod.check(text)
    assert not problems, problems[:3]
    assert (out["anchors"], out["bare anchors"], out["table rows"], out["quotations"],
            out["count phrases"], out["count phrases total"], out["sync problems"]) == \
        (61, 15, 17, 61, 65, 65, 0), f"counters {out}"
    p = mod.population()
    assert (p["files"], p["ndirs"], p["begins"], p["titled"], p["titled_all"],
            len(p["head_titled"]), len(p["no_head"])) == (7679, 719, 2410, 1609, 1619, 373, 76), \
        f"files {p['files']}, begins {p['begins']}"
    assert (len(p["rn"]), len(p["an"]), len(p["add"]), len(p["core"]), len(p["dn"]),
            len(p["eo"]), len(p["subj_hits"]), len(p["subject"]), len(p["tgt"]),
            p["generic"]) == (248, 275, 15, 6, 76, 5, 207, 551, 17, 0), \
        f"rn {len(p['rn'])}, subject {len(p['subject'])}"
    assert (len(p["prose_sentence"]), len(p["prose_window"])) == (372, 372), "prose windows"
    assert (p["env_begins"]["theorem"], p["env_begins"]["maintheorem"],
            p["env_begins"]["thm"]) == (2405, 4, 1), f"env split {p['env_begins']}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _ = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"

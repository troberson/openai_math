"""The extracted self-tests for `notes/scripts/verify_conjecture_standing.py`.

The checker measures `notes/data/conjecture-standing.tsv` against the ledger and `overview.tex`;
this file injects the six defects the page records into the table text in memory and asserts the
pass that owns each one reports it. The injections are targeted from the parsed rows, so they
follow the table when a row's anchor or name changes; an injection that finds no target fails the
test, so a mutant cannot pass by quietly stopping applying.
"""

import re

import pytest

pytestmark = pytest.mark.mutant


def _row(text, fam):
    """The single table line for fam, and its index in the line list."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith(f"{fam}\t"):
            return lines, i
    return lines, None


def _set_field(text, fam, idx, value):
    lines, i = _row(text, fam)
    assert i is not None, f"no row for {fam} — the target is gone from the table"
    fields = lines[i].split("\t")
    fields[idx] = value
    lines[i] = "\t".join(fields)
    return "\n".join(lines)


def _append_field(text, fam):
    lines, i = _row(text, fam)
    assert i is not None, f"no row for {fam} — the target is gone from the table"
    lines[i] = lines[i] + "\textra field"
    return "\n".join(lines)


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_conjecture_standing")


@pytest.fixture(scope="module")
def targets(mod):
    """The measurement, the table text, and the row each injection targets."""
    led, want, entries = mod.selection()
    text = mod.STANDING_TSV.read_text(encoding="utf-8")
    rows = mod.tsv.read_rows_from_text(text)
    anchored = [r for r in rows if re.fullmatch(r"overview\.tex:\d+", r["abstract_line"])]
    named = [r for r in rows if mod.surname_tokens(r["conjecture"])]
    return {
        "led": led,
        "want": want,
        "entries": entries,
        "text": text,
        "anchor_fam": anchored[0]["fam"],
        "anchor_line": int(anchored[0]["abstract_line"].split(":")[1]),
        "conf_fam": rows[0]["fam"],
        "gap_fam": rows[1]["fam"],
        "gap_text": rows[1]["gap"],
        "name_fam": named[0]["fam"],
        "wide_fam": rows[0]["fam"],
        "outside": min(set(led) - want - {r["fam"] for r in rows}),
    }


def problems(mod, t, targets):
    return mod.check(t, targets["led"], targets["want"], targets["entries"])[0]


def flagged(mod, t, targets, needle):
    return [p for p in problems(mod, t, targets) if needle in p]


def test_clean_table(mod, targets):
    rows = mod.tsv.read_rows_from_text(targets["text"])
    assert rows
    assert problems(mod, targets["text"], targets) == []


def test_anchor_shifted_by_two_lines(mod, targets):
    cand = _set_field(targets["text"], targets["anchor_fam"], 9,
                      f"overview.tex:{targets['anchor_line'] + 2}")
    assert cand != targets["text"]
    hits = flagged(mod, cand, targets, "cites line")
    assert hits, "the anchor pass did not flag the shifted anchor"
    assert hits[0].startswith(targets["anchor_fam"])


def test_blanked_prior_confidence(mod, targets):
    cand = _set_field(targets["text"], targets["conf_fam"], 5, "")
    assert cand != targets["text"]
    hits = flagged(mod, cand, targets, "prior_confidence")
    assert hits, "the vocabulary pass did not flag the blanked prior_confidence"


def test_family_added_outside_the_selection(mod, targets):
    t = targets["text"]
    led = targets["led"]
    outside = targets["outside"]
    cand = t.rstrip("\n") + "\n" + "\t".join(
        [outside, led[outside]["discipline"], led[outside]["tier"],
         "an added row outside the selection", "not a prior judgment", "low",
         "a synthetic release claim", "synthetic gap", "1", "overview.tex:1"])
    assert cand != t
    hits = flagged(mod, cand, targets, "outside the selection")
    assert hits, "the population pass did not flag the added row"


def test_consequence_assertion_in_a_gap_field(mod, targets):
    cand = _set_field(targets["text"], targets["gap_fam"], 7,
                      targets["gap_text"] + "; it opens the door to the general case")
    assert cand != targets["text"]
    hits = flagged(mod, cand, targets, "asserts consequence")
    assert hits, "the consequence pass did not flag the gap field"


def test_conjecture_renamed_to_a_name_absent_from_its_abstract(mod, targets):
    cand = _set_field(targets["text"], targets["name_fam"], 3,
                      "Zauner dimension-six mutually unbiased bases conjecture")
    assert cand != targets["text"]
    hits = flagged(mod, cand, targets, "absent from the cited abstract")
    assert hits, "the naming pass did not flag the renamed conjecture"


def test_row_widened_to_eleven_fields(mod, targets):
    cand = _append_field(targets["text"], targets["wide_fam"])
    assert cand != targets["text"]
    hits = flagged(mod, cand, targets, "11 fields")
    assert hits, "the field-count pass did not flag the widened row"

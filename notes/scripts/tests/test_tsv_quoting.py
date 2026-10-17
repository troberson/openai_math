"""The extracted self-tests for `notes/scripts/verify_tsv_quoting.py`.

The checker applies GitHub's TSV quoting rule: a `"` is legal only at a field start, and a quoted
field must close inside the field with every interior quote doubled. Python's csv reader is lenient,
so this class is invisible to every other checker in the repo — GitHub is the only witness.

The faults are injected into table text in memory; the checker reads no argv and writes nothing, so
no tracked file is touched. Each fault is asserted against the pass that owns it, and the needles are
checked to be specific: a quote fault must not report a row-length problem.

Run: python3 notes/scripts/run_tests.py notes/scripts/tests/test_tsv_quoting.py -q
"""
import pytest
from catlib.paths import TABLES

pytestmark = pytest.mark.mutant

NEEDLES = {
    "MID-FIELD QUOTE": "not at the field start",
    "UNCLOSED QUOTED FIELD": "does not close",
    "UNDOUBLED INTERIOR QUOTE": "undoubled interior quote",
    "EXTRA FIELD": "fields, header has",
}


def _rows(text):
    lines = text.split("\n")
    return lines[:-1] if lines and lines[-1] == "" else lines


def _set_field(text, row_idx, col, value):
    lines = _rows(text)
    fields = lines[row_idx].split("\t")
    assert 0 <= col < len(fields), f"col {col} is outside the row's {len(fields)} fields"
    fields[col] = value
    lines[row_idx] = "\t".join(fields)
    return "\n".join(lines) + "\n"


def _append_field(text, row_idx, value):
    lines = _rows(text)
    lines[row_idx] = lines[row_idx] + "\t" + value
    return "\n".join(lines) + "\n"


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_tsv_quoting")


@pytest.fixture(scope="module")
def targets():
    """The row each injection targets: a legal quoted field, and a quote-free field."""
    topics = (TABLES / "topics.tsv").read_text(encoding="utf-8")
    q = None
    for i, row in enumerate(_rows(topics)):
        fields = row.split("\t")
        for j, f in enumerate(fields):
            if f.startswith('"'):
                q = (i, j)
                break
        if q:
            break
    conj = (TABLES / "conjecture-standing.tsv").read_text(encoding="utf-8")
    gap = None
    for i, row in enumerate(_rows(conj)):
        fields = row.split("\t")
        for j, f in enumerate(fields):
            if '"' not in f and len(f) > 20:
                gap = (i, j)
                break
        if gap:
            break
    assert q is not None, "topics.tsv carries no legal quoted field to mutate"
    assert gap is not None, "conjecture-standing.tsv carries no field to inject a quote into"
    return {"topics": topics, "q": q, "conj": conj, "gap": gap}


def faults(targets):
    topics, q = targets["topics"], targets["q"]
    conj, gap = targets["conj"], targets["gap"]
    out = []

    # 1. a quote mid-field: GitHub flags this as illegal quoting
    f = _rows(conj)[gap[0]].split("\t")[gap[1]]
    out.append(("MID-FIELD QUOTE", "conjecture-standing.tsv",
                _set_field(conj, gap[0], gap[1], f[:10] + '"' + f[10:])))

    # 2. a quoted field that does not close
    f = _rows(topics)[q[0]].split("\t")[q[1]]
    out.append(("UNCLOSED QUOTED FIELD", "topics.tsv", _set_field(topics, q[0], q[1], f[:-1])))

    # 3. an interior quote that is not doubled
    f = _rows(topics)[q[0]].split("\t")[q[1]]
    assert '""' in f, f"the target field carries no doubled interior quote: {f[:60]}"
    out.append(("UNDOUBLED INTERIOR QUOTE", "topics.tsv",
                _set_field(topics, q[0], q[1], f.replace('""', '"', 1))))

    # 4. a row widened to an extra field
    out.append(("EXTRA FIELD", "conjecture-standing.tsv",
                _append_field(conj, gap[0], "extra field")))

    return out


def needle(kind, problems):
    return [p for p in problems if NEEDLES[kind] in p]


def test_clean(mod):
    problems = []
    rows = 0
    quoted = 0
    files = sorted(TABLES.glob("*.tsv"))
    for p in files:
        pr, n, q = mod.check(p.read_text(encoding="utf-8"), p.name)
        problems.extend(pr)
        rows += n
        quoted += q
    assert not problems, problems[:6]
    assert len(files) == 26, len(files)
    assert rows == 26809, rows
    assert quoted == 23, quoted


def test_mid_field_quote(mod, targets):
    kind, name, text = faults(targets)[0]
    pr, _, _ = mod.check(text, name)
    assert needle(kind, pr), pr[:4]


def test_unclosed_quoted_field(mod, targets):
    kind, name, text = faults(targets)[1]
    pr, _, _ = mod.check(text, name)
    assert needle(kind, pr), pr[:4]


def test_undoubled_interior_quote(mod, targets):
    kind, name, text = faults(targets)[2]
    pr, _, _ = mod.check(text, name)
    assert needle(kind, pr), pr[:4]


def test_extra_field(mod, targets):
    kind, name, text = faults(targets)[3]
    pr, _, _ = mod.check(text, name)
    assert needle(kind, pr), pr[:4]


def test_needles_are_specific(mod, targets):
    """Each fault fires its own needle. The extra-field fault widens a row, so the row-length
    needle fires for it alone; a quote fault must not report a row-length problem."""
    for kind, name, text in faults(targets):
        pr, _, _ = mod.check(text, name)
        assert needle(kind, pr), (kind, pr[:4])
        if kind != "EXTRA FIELD":
            assert not needle("EXTRA FIELD", pr), (kind, needle("EXTRA FIELD", pr)[:2])

"""notes/catalog.tsv and the claim-shape rules keyed to its abstracts.

The shape/tag rules live here because they are keyed to the overview.tex paraphrase, not to
the manuscripts: compare_abstracts.py measures 0 of 719 manuscript comparisons and 0 of 372
family best matches reading identical or abridged, so a tag is a claim about the summary.

`resolves_named` and `counterex_broad` are deliberately NOT SHAPES entries. triage_t0.py
assigns T0 buckets by first match over `shapes`, so widening `resolution` or `counterexample`
there moves families out of the counterexample/bound/classification/undecidability/density
buckets — a taxonomy change disguised as a tag tweak. As separate columns they discriminate
without touching that partition.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path
from typing import Any

from catlib.paths import LEDGER_TSV

SHAPES = {
    "resolution": r"resolv|proves the .{0,60}conjecture|answers .{0,30}question|settles",
    "counterexample": r"counterexample|disprove|refut|fails|violation",
    "bound": r"\bbound|sharp|power-saving|improv|inequalit",
    "classification": r"\bif and only if|classified|classification|characteri[sz]",
    "undecidability": r"no algorithm|undecidable|unsolvable|negative answer",
    "density": r"density",
    "conditional": r"[Aa]ssuming|we assume|under the .{0,40}hypothes|provided that|conditional",
    "partial": r"\bat most\b|\brestricted\b|\bunramified part|\bin coranks|for fixed|partial",
    "uniform": r"\buniform(ly|ly)?\b|\bfor every\b|\barbitrary\b",
}

ASSUME = re.compile(
    r"\bassuming\b|\bwe assume\b|\bprovided that\b|\bconditioned on\b|\bconditional\b"
    r"|under the [^.]{0,60}?(?:hypothes|conjecture|assumption)")
NEG_BEFORE = re.compile(r"(?:without|no)\s*$")
TECH_AFTER = re.compile(
    r"^[^.]{0,60}?(?:expectation|law|laws|probability|probabilities|measure|distribution|density)")

# Named-target resolution, measured in notes/resolution-tag.md.
TARGET_NOUN = re.compile(r"conjectur|\bquestion|\bproblem")
RESOLVE_VERB = re.compile(
    r"\bprov(?:e|es|ed|ing)\b|\bdisprov|\brefut|\bresolv|\banswer|\bsettl|\bestablis"
    r"|\bconfirm|\bfail|\bviolat|\bcounterexample")

# Counterexample language, measured in notes/counterexample-tag.md. Phrase rule, not stem rule:
# an unbounded `negativ` stem flags 90 families, most of them adjectival.
COUNTEREX_PHRASE = re.compile(
    r"\bcounterexample|\bdisprov|\brefut|\bviolat|\bfails?\b"
    r"|negative (?:answer|resolution)"
    r"|(?:answer|resolv|settl|conclud|establish)[a-z]*[^.]{0,80}negatively"
    r"|negatively[^.]{0,40}(?:answer|resolv|settl)"
    r"|does not (?:imply|hold|satisfy)")

TIERS = ("T3", "T2", "T1", "T0")


def read_ledger(path: Path = LEDGER_TSV) -> list[dict[str, str]]:
    """The 372 ledger rows as dicts. Parse with DictReader(delimiter='\\t'), never split(',')."""
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def ledger_by_fam(path: Path = LEDGER_TSV) -> dict[str, dict[str, str]]:
    """{fam: row}, the join every family-keyed reader wants."""
    return {r["fam"]: r for r in read_ledger(path)}


def conditional_hits(low: str) -> list[str]:
    """Assumption phrases only.

    Drops two false-positive families found by reading all nine flagged abstracts:
    "conditional expectation/law" (a technical term) and "without assuming" (a negation
    that is often the point of the result). "unconditionally" never matches, since
    \\bconditional\\b has no word boundary inside it.
    """
    hits = []
    for m in ASSUME.finditer(low):
        if m.group() == "conditional" and TECH_AFTER.match(low[m.end():m.end() + 60]):
            continue
        if NEG_BEFORE.search(low[max(0, m.start() - 12):m.start()]):
            continue
        hits.append(m.group())
    return hits


def shapes_of(abstract: str) -> list[str]:
    low = abstract.lower()
    out = [n for n, pat in SHAPES.items() if n != "conditional" and re.search(pat, low)]
    if conditional_hits(low):
        out.append("conditional")
    return out


def resolves_named(title: str, abstract: str) -> int:
    """1 when the title or abstract names a conjecture/question/problem and uses a resolution verb.

    `\\bprov(?:e|es|ed|ing)\\b` needs both boundaries: without the leading one, "improved"
    matches through the "proved" inside it.

    Input scope is title + abstract, stated because it changes the count: abstract only yields
    233, the union yields 248, and the union is a strict superset -- 0 removals. The 15 additions
    are recorded in notes/named-results.md. Lowering the whole input is what makes the union a
    superset: a case-sensitive title read drops 100 of the 233 (capitalised "Conjecture" at title
    start) and yields 148, which is why the scope is stated with the case rule.
    """
    low = (title + " " + abstract).lower()
    return 1 if TARGET_NOUN.search(low) and RESOLVE_VERB.search(low) else 0


def counterex_broad(title: str, abstract: str) -> int:
    """1 when the title or abstract uses counterexample language, judged by phrase.

    A keyword floor: it says the family *uses* the language, not that the manuscript contains a
    counterexample. The 30 families this flags beyond the `counterexample` tag were each read at
    the matched sentence and recorded in notes/counterexample-tag.md.

    Input scope is title + abstract, stated because it changes the count: abstract only yields 72,
    and the two title-only additions (088, 293) are families whose titles literally say
    "counterexamples".
    """
    return 1 if COUNTEREX_PHRASE.search((title + " " + abstract).lower()) else 0


def versions_of(paths: list[str]) -> int:
    """Manuscripts whose date-stripped directory slug repeats (same paper, new date)."""
    from catlib.paths import owner

    c = Counter(DATE_SLUG.sub("", owner(p)) for p in paths)
    return sum(n for n in c.values() if n > 1)


DATE_SLUG = re.compile(
    r"-(?:January|February|March|April|May|June|July|August|September|October|November|December)"
    r"-\d{1,2}-\d{4}$")


def tier_of(has_main_results: bool, has_configs: bool, has_scope_note: bool) -> str:
    """The ledger's tier ladder, spelled out so a reader cannot re-derive it differently.

    T3: a scope note links a config that formalization.yaml's main_results names.
    T2: a scope note links configs, none of them in main_results.
    T1: a scope note, no config links.  T0: no scope note.
    """
    if has_main_results:
        return "T3"
    if has_configs:
        return "T2"
    if has_scope_note:
        return "T1"
    return "T0"


def shapes_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    """{shape: families carrying it}, the report line every shapes figure comes from."""
    out: dict[str, int] = {}
    for name in SHAPES:
        out[name] = sum(1 for r in rows if name in r["shapes"].split("|"))
    return out

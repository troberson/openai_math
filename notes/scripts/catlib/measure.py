"""The measured population as data, not as prints.

`population()` returns the corpus-wide ledger aggregates `build_catalog.py`'s report prints and
the report-fed pages quote; `release()` returns the counts that come from the parse functions
rather than from the ledger rows; `evidence_dirs()` returns the three non-Lean evidence sets.
They exist so a generator, a report, and a template read one figure off one rule instead of
each carrying its own copy of the sum.

Checkers deliberately do NOT import this module. A checker that re-derives a count through the
same code as the page it checks proves nothing, so the checkers keep their own recomputation and
this module stays on the writer side of that line.

Figures are returned as ints, sets, and lists -- never as formatted strings. A page that quotes
"200 entries over 189 configs" quotes two ints from here; the wording is the page's, the numbers
are measured here.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from catlib.ledger import SHAPES, TIERS, read_ledger
from catlib.paths import ROOT


def _n(row: dict[str, Any], key: str) -> int:
    """Ledger cell as an int. Works on the TSV read (str) and on generated rows (int)."""
    return int(row[key])


def evidence_dirs() -> tuple[set[str], set[str], set[str]]:
    """(verification dirs, INPUTS.md dirs, COVERAGE.md dirs), keyed by manuscript directory name."""
    preprints = ROOT / "preprints"
    ver = {p.parent.name for p in preprints.glob("*/verification")}
    inputs = {p.parent.name for p in preprints.glob("*/INPUTS.md")}
    covmd = {p.parent.parent.name for p in preprints.glob("*/verification/COVERAGE.md")}
    return ver, inputs, covmd


def shape_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    """{shape: families carrying it}, read off the ledger `shapes` column."""
    return {name: sum(1 for r in rows if name in str(r["shapes"]).split("|")) for name in SHAPES}


def tier_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    """{tier: families}, in the T3/T2/T1/T0 order the report prints."""
    c = Counter(str(r["tier"]) for r in rows)
    return {t: c[t] for t in TIERS}


def discipline_table(rows: list[dict[str, Any]]) -> dict[str, tuple[int, int, int, int]]:
    """{discipline: (families, scope notes, manuscripts, formalized manuscripts)}."""
    acc: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        c = acc[str(r["discipline"])]
        c[0] += 1
        c[1] += _n(r, "scope_note")
        c[2] += _n(r, "paps")
        c[3] += _n(r, "paps_form")
    return {k: (v[0], v[1], v[2], v[3]) for k, v in acc.items()}


def population(rows: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Every corpus-wide figure the generator report prints from ledger rows.

    `rows` accepts generated rows or the TSV read; passing the generated rows keeps the
    generator from re-reading the file it just wrote.
    """
    rows = read_ledger() if rows is None else rows
    tiers = tier_counts(rows)
    shapes = shape_counts(rows)
    rn = {str(r["fam"]) for r in rows if _n(r, "resolves_named")}
    res = {str(r["fam"]) for r in rows if "resolution" in str(r["shapes"]).split("|")}
    cb = {str(r["fam"]) for r in rows if _n(r, "counterex_broad")}
    ct = {str(r["fam"]) for r in rows if "counterexample" in str(r["shapes"]).split("|")}
    return {
        "families": len(rows),
        "manuscripts": sum(_n(r, "paps") for r in rows),
        "manuscripts_form": sum(_n(r, "paps_form") for r in rows),
        "tiers": tiers,
        "shapes": shapes,
        "shapes_ge3": sum(1 for r in rows if len([s for s in str(r["shapes"]).split("|") if s]) >= 3),
        "shapes_none": sum(1 for r in rows if not str(r["shapes"])),
        "conditional": [str(r["fam"]) for r in rows if _n(r, "conditional")],
        "resolves_named": rn,
        "resolution_tag": res,
        "rn_union": len(rn | res),
        "rn_both": len(rn & res),
        "rn_tag_only": sorted(res - rn),
        "rn_column_only": sorted(rn - res),
        "resolves_named_by_tier": {
            t: sum(1 for r in rows if str(r["tier"]) == t and _n(r, "resolves_named")) for t in TIERS
        },
        "counterex_broad": len(cb),
        "counterex_tag": len(ct),
        "counterex_tag_only": len(ct - cb),
        "counterex_flag_only": len(cb - ct),
        "counterex_by_tier": {
            t: sum(1 for r in rows if str(r["tier"]) == t and _n(r, "counterex_broad")) for t in TIERS
        },
        "counterex_manuscripts": sum(_n(r, "paps") for r in rows if _n(r, "counterex_broad")),
        "versions_families": sum(1 for r in rows if _n(r, "versions")),
        "versions_reissues": sum(_n(r, "versions") for r in rows),
        "companion_word": sum(_n(r, "companion_word") for r in rows),
        "summary_families": sum(1 for r in rows if _n(r, "summary")),
        "summary_manuscripts": sum(_n(r, "paps") for r in rows if _n(r, "summary")),
        "disciplines": discipline_table(rows),
    }


def release() -> dict[str, Any]:
    """The release-level counts: what the shipped files say, independent of the ledger rows."""
    from catlib import overview, yaml

    _order, fams = overview.parse_overview()
    fam_paps = overview.parse_contents()
    sources, main_results = yaml.parse_yaml()
    challenges = yaml.parse_challenges()
    docs = yaml.parse_docs()
    trace_by_fam, trace_unlisted = yaml.parse_traces()
    ver, inputs, covmd = evidence_dirs()
    paps_all = {p for fam in fams for p in set(fam_paps.get(fam, [])) | set(fams[fam]["tex_paps"])}
    # The two family -> manuscript mappings are independent (overview.tex links vs CONTENTS.md
    # links); kept as per-family diffs so a report can name the families that disagree.
    tex_only = [(f, sorted(set(fams[f]["tex_paps"]) - set(fam_paps.get(f, [])))) for f in sorted(fams)]
    md_only = [(f, sorted(set(fam_paps.get(f, [])) - set(fams[f]["tex_paps"]))) for f in sorted(fams)]
    return {
        "families": len(fams),
        "manuscripts": len(paps_all),
        "formalized": len(sources),
        "challenges": len(challenges),
        "main_results_entries": sum(main_results.values()),
        "main_results_configs": len(main_results),
        "scope_notes": len(docs),
        "verification_dirs": len(ver),
        "inputs_dirs": len(inputs),
        "covmd_dirs": len(covmd),
        "traces_attributed": sum(len(v) for v in trace_by_fam.values()),
        "traces_unattributed": len(trace_unlisted),
        "traces_unattributed_names": list(trace_unlisted),
        "overview_only": [(f, x) for f, x in tex_only if x],
        "contents_only": [(f, x) for f, x in md_only if x],
        "no_contents": [f for f in sorted(fams) if not fam_paps.get(f)],
    }

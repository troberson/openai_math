#!/usr/bin/env python3
"""Measure the formalized statement surface against the manuscripts it is paired with; report-only.

Writes nothing and runs nothing. Lean files are read as text — lake, lean, and comparator are never
invoked here, so nothing measured can mean "a statement was compiled" or "a proof was checked". The
release's own review status is `unchecked` at lean/formalization.yaml:1774-1778.

Three measurements, in the order the page quotes them:

1. The declaration surface. Every `main_results` entry's declaration is resolved in the file the yaml
   names, and each statement is classified: opaque (its type is a name that must be opened) or a
   formula. An opaque statement's carrier is resolved through the declaration file's import closure,
   and the carrier body is measured — lines, integer literals.
2. The numeric pairing. config → family comes from the `../ComparatorChallenges/(X).lean` links inside
   `lean/docs/<NNN>.md`; family → manuscripts from the overview's `tex_paps`. The manuscript side is
   the integer and fraction literals inside its `theorem`/`maintheorem`/`thm` environments, with
   `\frac43` and `\frac{4}{3}` normalized to exact rationals; the Lean side is the same over the
   carrier body. Signs are dropped on both sides, so `m+4` and `m+5` compare as 4 and 5. A pair is
   exact, a Lean subset, an overlap, or disjoint. The manuscript side reads theorem environments only,
   so a constant in a supporting lemma is counted: an "extra" Lean literal is weak evidence.
3. The `a.e.` surface. Over the 719 listed manuscripts, every `theorem`/`maintheorem`/`thm` environment
   is scanned for an `a.e.`-style phrase (`a.e.`, `almost every`, `almost all`, `a.s.`, `measure zero`,
   `null set`), and the families that carry one are intersected with the families whose scope note links
   a config that has a `main_results` entry.

Run it twice and diff: the report must be identical.
"""
import collections
import re
from fractions import Fraction

import build_catalog
import extract_counterexample_crosscheck as cx

from catlib.paths import DOCS_DIR, PREPRINTS

LIT = re.compile(r"(?<![\w.])\d+(?:\s*/\s*\d+)?(?![\w.])")
FRAC = re.compile(r"\\frac\s*\{?(\d+)\}?\s*\{?(\d+)\}?")
STMT_ENV = re.compile(r"\\begin\{(theorem|maintheorem|thm)\}")
END_ENV = re.compile(r"\\end\{(theorem|maintheorem|thm)\}")
AE_PHRASE = re.compile(r"a\.e\.|almost every|almost all|a\.s\.|measure zero|null set", re.I)
LINK = re.compile(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean")


def norm(tok: str) -> Fraction | None:
    t = tok.replace(" ", "")
    if "/" in t:
        a, b = t.split("/", 1)
        return Fraction(int(a), int(b)) if int(b) else None
    return Fraction(int(t))


def literals(text: str, tex: bool = False) -> set:
    out = {v for v in (norm(t) for t in LIT.findall(text)) if v is not None}
    if tex:
        out |= {Fraction(int(a), int(b)) for a, b in FRAC.findall(text) if int(b)}
    return out


def env_bodies(dirpath: str) -> list[str]:
    """Every theorem-environment body in a manuscript's .tex files, as shipped text."""
    base = PREPRINTS / dirpath
    out = []
    for p in sorted(base.rglob("*.tex")):
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in STMT_ENV.finditer(text):
            close = END_ENV.search(text, m.end())
            if close:
                out.append(text[m.end():close.start()])
    return out


def cfg_to_fam(fams: list[str]) -> dict[str, set[str]]:
    """config stem -> the families whose scope note links it, from the ComparatorChallenges links."""
    out: dict[str, set[str]] = collections.defaultdict(set)
    for f in fams:
        p = DOCS_DIR / f"{f}.md"
        if not p.is_file():
            continue
        for ln in p.read_text(encoding="utf-8", errors="replace").splitlines():
            for c in LINK.findall(ln):
                out[c].add(f)
    return out


def population() -> dict:
    mr, entries = cx.main_results()
    order, fams = build_catalog.parse_overview()
    cfg2fam = cfg_to_fam(order)

    bodies: dict[str, tuple[str, int, list[str]]] = {}
    unresolved, carrier_missing = [], []
    carrier_typed = 0
    for c in sorted(set(entries)):
        decl, rel, _ = mr[c]
        at, block = cx.declaration_statement(decl, rel)
        if at is None:
            unresolved.append((c, decl, rel))
            continue
        t = re.search(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=", " ".join(block))
        if not t:
            continue
        carrier_typed += 1
        cfile, cline, cbody = cx.carrier(t.group(1).split(".{")[0].split(".")[-1], rel)
        if cfile is None:
            carrier_missing.append((c, t.group(1)))
            continue
        bodies[c] = (str(cfile), cline, cbody)

    sizes = sorted(len(b[2]) for b in bodies.values())
    lit_hist: collections.Counter[int] = collections.Counter()
    with_lit = 0
    lit_total = 0
    for body in bodies.values():
        n = len(literals("\n".join(body[2])))
        lit_hist[n] += 1
        if n:
            with_lit += 1
            lit_total += n

    pair: dict[str, int] = collections.Counter()
    disjoint, exact, overlap_extra = [], [], []
    for c, body in sorted(bodies.items()):
        b = body[2]
        clits = literals("\n".join(b))
        fams_c = sorted(cfg2fam[c])
        if not fams_c:
            pair["no_family"] += 1
            continue
        if not clits:
            pair["carrier_no_literal"] += 1
            continue
        mlits, envs = set(), 0
        for f in fams_c:
            for path in fams[f]["tex_paps"]:
                d = path.split("/")[1]
                for env in env_bodies(d):
                    mlits |= literals(env, tex=True)
                    envs += 1
        if not mlits:
            pair["no_headline_literal"] += 1
            continue
        if clits == mlits:
            pair["exact"] += 1
            exact.append((c, fams_c, sorted(clits), envs))
        elif clits <= mlits:
            pair["subset"] += 1
        elif not clits & mlits:
            pair["disjoint"] += 1
            disjoint.append((c, fams_c, sorted(clits)))
        else:
            pair["overlap"] += 1
            extra = sorted(clits - mlits)
            if extra:
                overlap_extra.append((c, fams_c, extra, sorted(clits & mlits)))

    env_total = 0
    ae_envs = collections.defaultdict(list)
    for f in order:
        for path in fams[f]["tex_paps"]:
            d = path.split("/")[1]
            for env in env_bodies(d):
                env_total += 1
                if AE_PHRASE.search(env):
                    ae_envs[f].append(d)
    ae_fams = sorted(ae_envs)
    linked_fams = {f for fs in cfg2fam.values() for f in fs}
    inter = sorted(set(ae_fams) & linked_fams)
    ae_cfgs = sorted(c for c, fs in cfg2fam.items() if fs & set(ae_fams))
    ae_with = sorted(c for c in ae_cfgs if c in mr)
    ae_without = sorted(c for c in ae_cfgs if c not in mr)

    ae_table = []
    for f in ae_fams:
        cs = sorted(c for c, fs in cfg2fam.items() if f in fs)
        ae_table.append((f, len(ae_envs[f]), len(cs),
                         len([c for c in cs if c in mr]), len([c for c in cs if c not in mr])))

    return {
        "entries": len(entries), "unique": len(set(entries)),
        "resolved": len(set(entries)) - len(unresolved), "unresolved": unresolved,
        "carrier_typed": carrier_typed, "carriers_ok": len(bodies),
        "carrier_missing": carrier_missing,
        "bodies": bodies, "sizes": sizes,
        "size_min": sizes[0], "size_med": sizes[len(sizes) // 2],
        "size_max": sizes[-1], "size_sum": sum(sizes),
        "with_literal": with_lit, "lit_total": lit_total, "lit_hist": lit_hist,
        "pair": pair, "disjoint": disjoint, "exact": exact, "overlap_extra": overlap_extra,
        "cfg2fam": cfg2fam,
        "env_total": env_total, "ae_envs": sum(len(v) for v in ae_envs.values()),
        "ae_fams": ae_fams, "ae_inter": inter, "ae_cfgs": ae_cfgs,
        "ae_with": ae_with, "ae_without": ae_without, "ae_table": ae_table,
        "mr": mr,
    }


def report(v: dict) -> None:
    print("== declaration surface")
    print(f"main_results entries {v['entries']}  unique configs {v['unique']}")
    print(f"statements resolved {v['resolved']}  NOT FOUND {len(v['unresolved'])} {v['unresolved']}")
    print(f"carrier-typed {v['carrier_typed']}  carriers resolved {v['carriers_ok']}  "
          f"carrier definitions not found {len(v['carrier_missing'])} {v['carrier_missing']}")
    print(f"carrier bodies {len(v['bodies'])}  lines min {v['size_min']} median {v['size_med']} "
          f"max {v['size_max']} sum {v['size_sum']}")
    print(f"carriers with an integer literal {v['with_literal']} of {len(v['bodies'])}  "
          f"literals {v['lit_total']}")
    print("literal-count histogram " + " ".join(f"{k}:{n}" for k, n in sorted(v["lit_hist"].items())))

    print("\n== numeric pairing against the manuscript headline environments")
    p = v["pair"]
    print(f"exact {p['exact']}  lean-subset {p['subset']}  overlap {p['overlap']}  disjoint {p['disjoint']}  "
          f"carrier-no-literal {p['carrier_no_literal']}  no-headline-literal {p['no_headline_literal']}  "
          f"no-family-link {p['no_family']}")
    print(f"disjoint pairs {len(v['disjoint'])}")
    for c, fs, lits in v["disjoint"]:
        print(f"  {c} fam {'/'.join(fs)} carrier literals {lits}")
    print(f"exact pairs {len(v['exact'])}")
    for c, fs, lits, envs in v["exact"]:
        print(f"  {c} fam {'/'.join(fs)} literals {lits} envs {envs}")
    print(f"overlap pairs carrying a literal the headline does not: {len(v['overlap_extra'])}")
    for c, fs, extra, shared in v["overlap_extra"]:
        print(f"  {c} fam {'/'.join(fs)} extra {extra} shared {shared}")

    print("\n== a.e. surface")
    print(f"theorem environments over the 719 listed manuscripts {v['env_total']}")
    print(f"environments carrying an a.e.-style phrase {v['ae_envs']}  over {len(v['ae_fams'])} families")
    print(f"of those, families whose scope note links a config {len(v['ae_inter'])} "
          f"{v['ae_inter']}")
    print(f"configs those families link {len(v['ae_cfgs'])}  with a main_results entry {len(v['ae_with'])}  "
          f"without {len(v['ae_without'])}")


def main() -> int:
    report(population())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

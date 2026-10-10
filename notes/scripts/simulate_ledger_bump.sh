#!/bin/bash
# Simulate a ledger bump in a hardlink copy: prove the generated pages move by themselves.
#
# The question this answers is the one a template change cannot answer on its own — does a page's
# count come from the corpus, or from a number someone typed? Edit one manuscript path in a copy's
# overview.tex, re-run the writers inside the copy, and diff the copy's own pages before/after.
# Pages move with no page edit; the repo tree is untouched.
#
# cp -al shares INODES: a file in the copy IS the file in the repo, so every path a writer will
# overwrite must be unlinked and re-copied first, or the writer edits the real tree through the
# link. The unlink-and-recopy set is exactly: the edited file, every notes/*.tsv, the generated
# report pages, and the whole generated notes/index tree. preprints/, lean/, notes/summaries/ and
# notes/templates/ stay hardlinked (read-only here), which is what makes the copy cheap.
#
# Usage: bash notes/scripts/simulate_ledger_bump.sh '<sed program>'
#   e.g. '782s|Taming implies compatibility on four-manifolds}}|...\\href{...}{(September 23 edition)}}|'
# In a sed replacement every backslash the LaTeX needs must be doubled: sed eats \e and \t, so
# \enspace arrives as "enspace" and \href as "href".
# The repo root comes from git, not from the script's own depth: a script that resolves its root as
# "$(dirname "$0")/../.." is correct only at exactly two levels below the root, and the same file run
# from a staging directory resolves to the wrong tree and silently copies nothing.
REPO="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)" || exit 1
cd "$REPO" || exit 1
COPY="$REPO/.qwen/tmp/ledger_bump_copy"
R="$REPO/.qwen/tmp/reports"
# The page a template renders is its basename minus the .j2 suffix: links.md.j2 renders notes/links.md.
# Keep the suffix and the unlink-and-recopy loop names files that do not exist, every cp fails, and the
# copy's pages stay HARDLINKED to the repo's — render_reports.py then writes the real tree.
PAGES=""
for t in notes/templates/report/*.j2; do p="${t##*/}"; PAGES="$PAGES notes/${p%.j2}"; done
SED="$1"
[ -n "$SED" ] || { echo "usage: $0 '<sed program>'"; exit 2; }

writers() {  # writers <dir> <tag> — the writers whose output the demo claims moves, in gate order
  local d="$1" tag="$2" s args
  for s in build_catalog.py build_sources.py build_index.py extract_links.py \
           extract_subfindings.py compare_abstracts.py; do
    args=""
    [ "$s" = "compare_abstracts.py" ] && args="--tsv"
    ( cd "$d" && python3 "notes/scripts/$s" $args > "$R/bump_${tag}_${s%.py}.txt" 2>&1 )
    printf 'writer exit %s :: %s %s\n' "$?" "$s" "$args"
  done
  # extract_formalization_deps.py is skipped: it reads all 122,458 files under lean/OAI/, its TSV
  # is copied real, and nothing on this path reads it.
  #
  # The chain runs a second time because the TSVs form a chain, not a DAG that converges in one
  # pass: build_sources.py takes its row set from notes/subfindings.tsv, which
  # extract_subfindings.py writes AFTER it in gate order. One pass leaves sources.tsv one
  # generation behind the edited overview.tex, and build_index.py then dies with
  # KeyError on the new manuscript directory. The repo sits at a fixed point, so this is
  # invisible there; a bumped copy exposes it.
  for s in build_sources.py extract_subfindings.py build_index.py; do
    ( cd "$d" && python3 "notes/scripts/$s" > "$R/bump_${tag}_2_${s%.py}.txt" 2>&1 )
    printf 'writer exit %s :: %s (pass 2)\n' "$?" "$s"
  done
  # render_reports.py runs last. In a bumped copy it exits NONZERO by design: its page-vs-render
  # sync pass compares the copy's corpus with the copy's pages, and a corpus change makes those
  # pages stale. It writes the pages before reporting, so the bytes still move.
  ( cd "$d" && python3 notes/scripts/render_reports.py > "$R/bump_${tag}_render_reports.txt" 2>&1 )
  printf 'writer exit %s :: render_reports.py\n' "$?"
}

probe() {  # probe <dir> <tag> — every count the demo claims moves
  local d="$1" tag="$2"
  echo "--- $tag ---"
  grep -E "^(families|manuscripts|formalized|challenges|main_results|scope notes|tier)" \
    "$R/bump_${tag}_build_catalog.txt"
  awk -F'\t' '$1=="342"{printf "ledger 342: paps=%s paps_form=%s tier=%s chal=%s mainres=%s\n", $4,$5,$6,$7,$8}' \
    "$d/notes/catalog.tsv"
  printf "subfindings manuscript rows: %s\n" \
    "$(awk -F'\t' 'NR>1 && $1=="manuscript"' "$d/notes/subfindings.tsv" | wc -l)"
  printf "sources.tsv rows: %s\n" "$(( $(wc -l < "$d/notes/sources.tsv") - 1 ))"
  printf "index pages: %s\n" "$(find "$d/notes/index" -type f 2>/dev/null | wc -l)"
}

rm -rf "$COPY"
mkdir -p "$COPY"
cp -al overview.tex CONTENTS.md README.md notes lean preprints reasoning_traces "$COPY"/
rm -f "$COPY/overview.tex" && cp overview.tex "$COPY/overview.tex"
for f in notes/*.tsv $PAGES; do rm -f "$COPY/$f" && cp "$f" "$COPY/$f"; done
rm -rf "$COPY/notes/index" && cp -a notes/index "$COPY/notes/index"
rm -rf "$COPY/notes/scripts/__pycache__" "$COPY/notes/scripts/catlib/__pycache__"
# Hardlink guard: a writer writes through a shared inode, so any copy file with links > 1 is the repo's
# file. Abort before the first writer runs rather than editing the real tree.
shared=""
for f in "$COPY/overview.tex" "$COPY"/notes/*.tsv; do
  [ "$(stat -c %h "$f")" = "1" ] || shared="$shared ${f#$COPY/}"
done
for p in $PAGES; do
  [ "$(stat -c %h "$COPY/$p")" = "1" ] || shared="$shared $p"
done
if [ -n "$shared" ]; then
  echo "ABORT: copy files still share an inode with the repo:$shared" >&2
  exit 3
fi
echo "hardlink guard: overview.tex, notes/*.tsv and all $(echo $PAGES | wc -w) pages are links=1"
echo "=== inode sharing (1 = unlinked real file, 2 = shared with the repo) ==="
for f in "$COPY/overview.tex" "$COPY/notes/catalog.tsv" "$COPY/notes/README.md" \
         "$COPY/notes/index/differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md" \
         "$COPY/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf"; do
  printf '%-84s links=%s\n' "${f#$REPO/}" "$(stat -c %h "$f")"
done

echo "=== BEFORE: writers run in the copy, unedited overview.tex ==="
writers "$COPY" before
probe "$COPY" before
: > "$R/bump_before_md5.txt"
for p in $PAGES; do printf '%s  %s\n' "$(md5sum "$COPY/$p" | cut -d' ' -f1)" "$p" >> "$R/bump_before_md5.txt"; done
( cd "$COPY/notes/index" && find . -type f -print0 | xargs -0 md5sum | sort -k2 ) > "$R/bump_before_idx.md5"

echo "=== applying the edit to the copy's overview.tex ==="
sed -i "$SED" "$COPY/overview.tex"
stat -c '%n links=%h' "$COPY/overview.tex"
printf 'overview.tex lines changed: %s\n' "$(diff <(git show HEAD:overview.tex) "$COPY/overview.tex" | grep -c '^[<>]')"

echo "=== AFTER: same writers, edited overview.tex ==="
writers "$COPY" after
probe "$COPY" after
echo "--- build_catalog report diff (before vs after) ---"
diff "$R/bump_before_build_catalog.txt" "$R/bump_after_build_catalog.txt"
echo "=== report pages whose bytes moved inside the copy ==="
for p in $PAGES; do
  a=$(awk -v p="$p" '$2==p{print $1; exit}' "$R/bump_before_md5.txt")
  b=$(md5sum "$COPY/$p" | cut -d' ' -f1)
  [ "$a" = "$b" ] && echo "same   $p" || echo "MOVED  $p"
done
echo "=== index pages that moved (copy before vs copy after) ==="
( cd "$COPY/notes/index" && find . -type f -print0 | xargs -0 md5sum | sort -k2 ) > "$R/bump_after_idx.md5"
printf 'index md5 lines changed: %s\n' "$(diff "$R/bump_before_idx.md5" "$R/bump_after_idx.md5" | grep -c '^[<>]')"
diff "$R/bump_before_idx.md5" "$R/bump_after_idx.md5" | grep '^[<>]' | cut -c3- | awk '{print $2}' | sort -u | head -12
echo "=== repo tree untouched? ==="
git status --porcelain
git diff --stat HEAD -- overview.tex
echo "BUMP_DONE"

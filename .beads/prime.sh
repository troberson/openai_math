#!/usr/bin/env bash
# bd prime, followed by the repo rules that outrank its generic session guidance.
# Wired into .claude/settings.json (SessionStart, PreCompact).
bd prime
cat <<'EOF'

## Repo overrides — these outrank the beads context above

- Do not commit or push unless the user asks. There is no session-end `git push`. `origin` is the
  fork `github.com/troberson/openai_math`; `upstream` (`github.com/openai/math`) is read-only.
- No Dolt in this repo: bd runs in no-db mode and `.beads/issues.jsonl` is the tracked issue store.
  Never run `bd dolt push`.
- Findings are recorded in tracked files under `notes/`, one entry per family. `bd remember` is not
  the record of record, and memory files are kept.
- Never run `lake`, `lean`, `lake exe cache get`, or the comparator.
EOF

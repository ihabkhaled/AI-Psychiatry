# Standards

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### Languages

| Detected | Where |
|---|---|
| Python (23 files) | `scripts/__init__.py`, `scripts/build_all_the_medicine.py`, `scripts/build_release_manifests.py` (+20 more) |
| Shell (3 files) | `hooks/prompt-reminder.sh`, `hooks/session-start.sh`, `install.sh` |
| PowerShell (1 file) | `install.ps1` |

### Linters, formatters and type checkers

Nothing detected.

### Pre-commit and git hooks

Nothing detected.

### Test frameworks

Nothing detected.

### CI

| Detected | Where |
|---|---|
| GitHub Actions workflows | `.github/workflows/ci.yml` |

### Ownership

Nothing detected.

### Import conventions

| Detected | Where |
|---|---|
| Python flat package `scripts` | `scripts/__init__.py` |

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: languages, code standards, lint, hooks, imports, QA gates.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which code standards, lint rules, hooks, import rules and QA gates apply, and which are enforced by a tool?

Enforced by a tool: `scripts/validate_framework.py` (links, JSON, manifests, versions, README counts, one-skill rule), `scripts/build_all_the_medicine.py --check` (generated references fresh), `scripts/psychiatry_version.py check` ([rule 58](../../../.ai/rules/58-version-discipline.md)), and the tests in `tests/`, all run by `.github/workflows/ci.yml`. The skill must stay under 8,000 bytes (a Codex limit; tested). No linter or formatter is configured, and there are no git hooks. Rules live in `.ai/rules/`; generated files are never edited by hand.

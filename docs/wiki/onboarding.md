# Onboarding

What this answers: how a newcomer, or a fresh agent, gets productive.

Part of the [project wiki](index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## How does a newcomer, or a fresh agent, get from clone to a verified first change?

1. Clone, then run `python -m unittest discover -s tests` and `python scripts/validate_framework.py`.
2. Read `CLAUDE.md`, then `.ai/rules/58-version-discipline.md` and the [ADR](../adr/0001-loud-always-on-hooks-and-version-discipline.md).
3. Edit canonical files only; regenerate with `python scripts/build_all_the_medicine.py`.
4. For a shipped change: `python scripts/psychiatry_version.py next`, `bump ... --date YYYY-MM-DD`, write the CHANGELOG entry, `check --base <ref>`.
5. Try it live: `claude --plugin-dir .`.

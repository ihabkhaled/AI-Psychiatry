# decisions

Use skills-only packaging; no MCP server or app is required.

- 2026-10-03: two local hooks keep the one skill always followed - `SessionStart` (the contract) and `UserPromptSubmit` (a three-line loud reminder). Both only print and exit 0. See `docs/adr/0001-loud-always-on-hooks-and-version-discipline.md`.
- 2026-10-03: a shipped change must raise the version and add a CHANGELOG section (rule 58, `scripts/psychiatry_version.py`, CI).


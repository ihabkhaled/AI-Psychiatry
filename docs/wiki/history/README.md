# History

<!-- akinator:generated:begin -->
<!-- Facts read from manifests, CHANGELOG.md, docs/changes, docs/adr and
     .ai/ledger. Rewritten on every run; write outside this block. -->

## Versions

| Manifest | Version |
|---|---|
| `.claude-plugin/plugin.json` | `0.7.0` |
| `.claude-plugin/marketplace.json` | `0.7.0` |
| `.codex-plugin/plugin.json` | `0.7.0` |

## Releases

| Version | Date | Summary |
|---|---|---|
| `0.7.0` | 2026-10-03 | **Always followed, on every prompt.** A second hook, `UserPromptSubmit` (`hooks/prompt-reminder.sh`, exec form), prints a three-line loud reminder with every prompt: apply the one applicable control,... |
| `0.6.0` | 2026-09-19 | **One skill, one command, always on.** `all-the-medicine` is now AI-Psychiatry's only skill and its only command on every platform (`/ai-psychiatry:all-the-medicine`, `$all-the-medicine`, `/all-the-me... |
| `0.5.0` | 2026-08-15 | Added `direct-communication` for assertive, succinct answers, essential evidence, and single non-looping blocker questions. |
| `0.4.0` | 2026-08-15 | Added `never-stop`, an explicit-invocation "superpower" for maximum autonomous execution: a question-suppression gate, a routine/material/hard-gate decision hierarchy, an eight-level recovery ladder,... |
| `0.3.0` | 2026-08-14 | Added semantic anti-gaming across retry, nesting, WIP, critic, verification, delegation, scope, completion, blocker, memory, and context controls. |
| `0.2.0` | 2026-08-14 | Replaced the canonical reference with the user-reattached 71 KB master prompt. |
| `0.1.0` | 2026-08-14 | Added shared Claude and Codex plugin packaging. |

## Change records

| Date | Change | Path |
|---|---|---|
| 2026-10-03 | Change - Always followed (loud), version discipline, uninstall cleanup (0.7.0) | `docs/changes/2026-10-03-always-followed-version-discipline.md` |

## Decisions

| Decision | Status | Path |
|---|---|---|
| ADR 0001 - Loud always-on hooks and version discipline | accepted | `docs/adr/0001-loud-always-on-hooks-and-version-discipline.md` |

## Ledger

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_history.py --write`
<!-- akinator:generated:end -->

What this answers: every version and revision, what shipped when.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which versions and revisions exist, and what shipped in each?

Every release and what shipped in it: [CHANGELOG](../../../CHANGELOG.md). Per-change records: `docs/changes/`. Decisions: `docs/adr/`.

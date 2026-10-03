# ADR 0001 - Loud always-on hooks and version discipline

- **Status:** accepted
- **Date:** 2026-10-03
- **Deciders:** Ihab Khaled (owner)

## Context

Agents skip an installed plugin unless it is shouted at (incident of 2026-10-03: an agent ignored AI-Psychiatry until the owner yelled, then complied). The owner also requires that the version always moves with a shipped change and that it is documented. Everything must stay inside the one skill and the one command.

## Options

### Option A - keep the polite contract and the SessionStart hook only
- **Cost:** the contract is read once, early, and forgotten. The incident recurs.
- **Why it lost:** it is the state that failed.

### Option B - add a loud UserPromptSubmit reminder and loud contract text; enforce versions with a tool and CI
- **Cost:** a few tokens per prompt (three short lines); a stricter release flow.
- **Why it won:** repetition at the point of attention is the one lever a plugin has on Claude Code; Codex and Cursor get the same text from the always-on contract.

### Option C - a second skill or command for releases
- **Why it lost:** the owner wants one skill and one command; a second entry would show in menus.

## Decision

Option B. The `UserPromptSubmit` hook prints static text, decides nothing and exits 0; `SessionStart` has no matcher. The tone is loud and aimed only at the AI, with no profanity. `scripts/psychiatry_version.py`, rule 58 and a CI job make a shipped change without a version bump and CHANGELOG entry a failing build. A test fails if the marker phrase `NOT OPTIONAL` leaves any output.

## Consequences

- Positive: the contract is present on every prompt; releases cannot silently skip a version.
- Negative: a few extra tokens per prompt; a loud register some readers may dislike.
- Revisit when: Claude Code offers a stronger always-on mechanism, or the reminder is observed to be ignored.

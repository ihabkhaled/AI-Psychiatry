# Roadmap

What this answers: what is planned, in what order, and why.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## What is planned next, in what order, and why that order?

Proposals only, nothing here is committed or scheduled (owner decides order):

1. A `psychiatry_version.py release` step that also rebuilds the `dist/` archive, so the zip cannot lag the version.
2. Generate the Codex block, Cursor rule and session output from one command and diff them against the installed copies (`doctor`), to catch a stale install.
3. Measure the per-prompt reminder: record whether agents still skip the contract with and without it.
4. Stop `.ai/skills/all-the-medicine/SKILL.md` (7,972 bytes, near the Codex limit, wording older than the canonical skill) from drifting: derive it from the canonical skill.
5. Replace the hand-edited rule entry flow with a safe `add-rule` command so `build_release_manifests.py` can be retired.

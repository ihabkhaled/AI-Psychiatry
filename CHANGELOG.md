# Changelog

## [0.7.0] - 2026-10-03

- **Always followed, on every prompt.** A second hook, `UserPromptSubmit` (`hooks/prompt-reminder.sh`, exec form), prints a three-line loud reminder with every prompt: apply the one applicable control, prove completion. It prints static text, decides nothing and exits 0. `SessionStart` keeps no matcher, so the contract is injected on startup, resume, clear and compact. Verified live on Claude Code: both hooks respond, and the plugin adds exactly one `/` entry, `ai-psychiatry:all-the-medicine`.
- **Version discipline** (rule 58, same one skill). `scripts/psychiatry_version.py` has `show`, `check [--base REF]`, `next`, `bump` and `set`: it edits only version strings (formatting and line endings kept), fails when manifests disagree, and fails when a shipped path changed without a higher version and a CHANGELOG section. A new CI workflow runs it, with a mutation test per invariant in `tests/test_version_discipline.py`.
- **Fix:** `install.sh --uninstall` and `install.ps1 -Uninstall` now remove the download cache an install created (`~/.ai-psychiatry/src`) and the empty directory above it; a directory that is not an AI-Psychiatry checkout is left alone.
- `scripts/build_release_manifests.py` keeps every rule (it used to cut the list at rule 55).
- CHANGELOG headings now use the `## [x.y.z] - date` form the version tool checks.
- Docs: wiki, change record, ADR 0001 and memory entry; README rewritten short and install-first.

## [0.6.0] - 2026-09-19

- **One skill, one command, always on.** `all-the-medicine` is now AI-Psychiatry's only skill and its only command on every platform (`/ai-psychiatry:all-the-medicine`, `$all-the-medicine`, `/all-the-medicine`). The other 30 public skills moved to `skills/all-the-medicine/references/skills/<name>/<name>.md` and are applied one at a time from there, so no platform lists 31 entries any more (verified live on Claude Code 2.1.154: one `/` entry). Their per-skill Codex `agents/openai.yaml` files were removed.
- **Always on.** A SessionStart hook (exec form) injects the contract on Claude Code; the installer writes the same contract as a marked `AGENTS.md` block for Codex and an `alwaysApply` rule for Cursor. One source: `skills/all-the-medicine/references/always-on.md`. `never-stop` relentless execution stays explicit-invocation only.
- **One-line installer** for Claude Code, Codex and Cursor: `install.sh` / `install.ps1` (re-run to update, `--repo`, `--uninstall` restores edited files byte for byte).
- `all-the-medicine/SKILL.md` trimmed under Codex's 8,000-byte explicit-invocation limit; the execution-phase table moved to `references/execution-phases.md`.
- Build scripts, the validator and tests resolve public skills through one rule (`public_skill_path`); the validator and a new test fail if a second plugin skill appears.

## [0.5.0] - 2026-08-15

- Added `direct-communication` for assertive, succinct answers, essential evidence, and single non-looping blocker questions.
- Renamed the installed `communicate-briefly` control to `direct-communication` and registered it for Claude and Codex.
- Added the skill to `all-the-medicine`, enforced Codex's three-prompt and 128-character limits, and refreshed package metadata.

## [0.4.0] - 2026-08-15

- Added `never-stop`, an explicit-invocation "superpower" for maximum autonomous execution: a question-suppression gate, a routine/material/hard-gate decision hierarchy, an eight-level recovery ladder, blocker validation, and a proven-completion stop condition.
- Added `all-the-medicine`, a "god-mode" meta-superpower that dynamically loads every registered public skill from the manifest, evaluates each against observable state, activates only applicable controls one at a time, resolves conflicts deterministically, and excludes itself from its own inventory.
- Added a deterministic build/check generator (`scripts/build_all_the_medicine.py`) that compiles every public skill and canonical rule into `skills/all-the-medicine/references/`, rewrites embedded links so they resolve from the compiled location, hashes every source file, and fails on staleness, duplicates, missing files, or self-recursion.
- Added background-process streaming discipline: never claim asynchronous execution without a real mechanism behind it, and keep emitting observable progress while genuine background work is in flight.
- Extended `scripts/executive_control.py` with deterministic question, decision, hard-gate, and skill-orchestration assessors (`classify_question`, `classify_decision`, `validate_hard_gate`, `next_relentless_action`, `build_skill_status_map`, `select_all_the_medicine_control`, `validate_streaming_liveness`).
- Added rules 56–57, guides, policies (`autonomy-contract`, `question-suppression`, `approval-gates`, `all-the-medicine`), and state/schema extensions for autonomy mode, decision classification, hard gates, and skill-status tracking.
- Extended `scripts/validate_framework.py` to check manifest/version consistency, README count accuracy, generated-artifact markers, and AllTheMedicine compiled-reference freshness.

## [0.3.0] - 2026-08-14

- Added semantic anti-gaming across retry, nesting, WIP, critic, verification, delegation, scope, completion, blocker, memory, and context controls.
- Added a deterministic observable-state policy engine, append-only semantic action ledger, completion evidence, reasoning balance, and audited executive overrides.
- Added 19 public skills, 19 installed controls, 15 rules, seven guides, a 24-loophole catalog, and underthinking/loophole regression suites.
- Added a complementary underthinking layer that enforces investigation, architecture, security, evidence, review, and verification floors without weakening anti-overthinking.
- Prepared portable Claude and OpenAI/Codex publication materials for the skills-only release.

## [0.2.0] - 2026-08-14

- Replaced the canonical reference with the user-reattached 71 KB master prompt.
- Added eight directly callable executive-control intervention skills for Claude and Codex.
- Added ten substantive behavioral guides and a 25-mode failure catalog.
- Replaced 28 generic installable skill bodies with distinct operational procedures.
- Added mandatory high-risk rules, deterministic policy assessment, exact 0–189 traceability, and regression validation.

## [0.1.0] - 2026-08-14

- Added shared Claude and Codex plugin packaging.
- Added full executive-control runtime, rules, skills, context, memory, adapters, tests, and traceability.

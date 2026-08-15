# Changelog

## 0.4.0 - 2026-08-15

- Added `never-stop`, an explicit-invocation "superpower" for maximum autonomous execution: a question-suppression gate, a routine/material/hard-gate decision hierarchy, an eight-level recovery ladder, blocker validation, and a proven-completion stop condition.
- Added `all-the-medicine`, a "god-mode" meta-superpower that dynamically loads every registered public skill from the manifest, evaluates each against observable state, activates only applicable controls one at a time, resolves conflicts deterministically, and excludes itself from its own inventory.
- Added a deterministic build/check generator (`scripts/build_all_the_medicine.py`) that compiles every public skill and canonical rule into `skills/all-the-medicine/references/`, rewrites embedded links so they resolve from the compiled location, hashes every source file, and fails on staleness, duplicates, missing files, or self-recursion.
- Added background-process streaming discipline: never claim asynchronous execution without a real mechanism behind it, and keep emitting observable progress while genuine background work is in flight.
- Extended `scripts/executive_control.py` with deterministic question, decision, hard-gate, and skill-orchestration assessors (`classify_question`, `classify_decision`, `validate_hard_gate`, `next_relentless_action`, `build_skill_status_map`, `select_all_the_medicine_control`, `validate_streaming_liveness`).
- Added rules 56–57, guides, policies (`autonomy-contract`, `question-suppression`, `approval-gates`, `all-the-medicine`), and state/schema extensions for autonomy mode, decision classification, hard gates, and skill-status tracking.
- Extended `scripts/validate_framework.py` to check manifest/version consistency, README count accuracy, generated-artifact markers, and AllTheMedicine compiled-reference freshness.

## 0.3.0 - 2026-08-14

- Added semantic anti-gaming across retry, nesting, WIP, critic, verification, delegation, scope, completion, blocker, memory, and context controls.
- Added a deterministic observable-state policy engine, append-only semantic action ledger, completion evidence, reasoning balance, and audited executive overrides.
- Added 19 public skills, 19 installed controls, 15 rules, seven guides, a 24-loophole catalog, and underthinking/loophole regression suites.
- Added a complementary underthinking layer that enforces investigation, architecture, security, evidence, review, and verification floors without weakening anti-overthinking.
- Prepared portable Claude and OpenAI/Codex publication materials for the skills-only release.

## 0.2.0 - 2026-08-14

- Replaced the canonical reference with the user-reattached 71 KB master prompt.
- Added eight directly callable executive-control intervention skills for Claude and Codex.
- Added ten substantive behavioral guides and a 25-mode failure catalog.
- Replaced 28 generic installable skill bodies with distinct operational procedures.
- Added mandatory high-risk rules, deterministic policy assessment, exact 0–189 traceability, and regression validation.

## 0.1.0 - 2026-08-14

- Added shared Claude and Codex plugin packaging.
- Added full executive-control runtime, rules, skills, context, memory, adapters, tests, and traceability.

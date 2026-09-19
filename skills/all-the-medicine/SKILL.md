---
name: all-the-medicine
description: Use for every task - AI-Psychiatry is always on and this is its only skill. Diagnoses observable agent state and applies the one applicable control (evidence, attention, reasoning balance, loops, loopholes, completion) until the task is proven complete. Also the one explicit command, /ai-psychiatry:all-the-medicine, for the full pass.
---

# All The Medicine

## Core principle

Load every medicine. Diagnose observable state. Activate only applicable treatments. Resolve treatment conflicts. Execute relentlessly. Verify sufficiently. Prevent semantic loopholes. Prove completion. Stop. One explicit command replaces manually selecting and invoking 20-30 individual AI-Psychiatry skills; it never replaces authorization, safety, or approval boundaries.

## Superpower classification

Type: `meta-superpower`. Tier: `god-mode`. Risk: `high`. Invocation: always on, and the one explicit command. Relentless `never-stop` execution inside it stays explicit-invocation only. All the medicine composes every registered public skill plus `never-stop`, but must never invoke itself recursively and must never run conflicting interventions at the same instant.

## One skill

This is AI-Psychiatry's only skill and only command on every platform. Every other public skill is a reference file here, `references/skills/<name>/<name>.md`, opened when its control is selected - never a separate skill, so no platform lists it as a separate command.

## Dynamic skill inventory

The authoritative inventory is `.ai/manifests/skills.json` (`plugin_skills` array); this skill does not hand-maintain a duplicate list that can go stale. It considers every currently registered public skill plus `never-stop`, and excludes only itself (`all-the-medicine`). `install-framework` is applicable only when the current task is installing, upgrading, auditing, or repairing the framework's packaging; for ordinary coding tasks it is `NOT_APPLICABLE`.

For progressive disclosure, read only when needed:

- [references/all-skills-compiled.md](references/all-skills-compiled.md) — every public skill, generated, `BEGIN SKILL:` / `END SKILL:` delimited.
- [references/all-rules-compiled.md](references/all-rules-compiled.md) — every canonical rule, generated, `BEGIN RULE:` / `END RULE:` delimited.
- [references/skill-index.json](references/skill-index.json) and [references/source-hashes.json](references/source-hashes.json) — deterministic ordering and drift detection.

Regenerate with `python scripts/build_all_the_medicine.py`; verify freshness with `python scripts/build_all_the_medicine.py --check`. These compiled files are generated artifacts — never edit them by hand; edit the canonical skill or rule and regenerate.

## Procedure

1. Lock the primary objective and the finite Definition of Done. Resolve any conflicting instruction sources by priority (system/platform, user, repository, domain, AI-Psychiatry, skill, memory, temporary state) before anything else.
2. Build the complete skill status map: every applicable skill gets exactly one status among `PENDING`, `CHECKED`, `ACTIVE`, `SATISFIED`, `NOT_APPLICABLE`, `BLOCKED_BY_HIGHER_PRIORITY_RULE`. Track only observable state and concise decision evidence per skill — never private chain-of-thought.
3. Select the single highest-priority applicable control from the execution-phase order below. Do not run conflicting interventions simultaneously.
4. Apply exactly one control, then take the productive action it implies and capture observable evidence of the result.
5. Update the completion matrix (requirement, status, evidence, remaining action) from that evidence only.
6. Reevaluate every skill's status against the new observable state.
7. Continue: mandatory work remaining -> next control; recoverable failure -> recovery ladder (from `never-stop`); hard gate with independent work left -> keep working independently; hard gate with none left -> request the minimum approval; Definition of Done proven -> final report and stop.
8. Never loop back into a control whose status is already `SATISFIED` without a state change that reopens it.

## Execution phases

Step 3 selects from eleven phases, 0 (instruction and permission resolution) to 10 (context and memory maintenance), in order. The full table with representative controls: [references/execution-phases.md](references/execution-phases.md).

## Conflict resolution

- NeverStop vs Completion Gate: before proven DoD, NeverStop wins; after proven DoD, Completion Gate wins immediately.
- Investigation Floor vs Stop Overthinking: missing critical evidence, Investigation Floor wins; sufficient evidence plus repeated investigation, Stop Overthinking wins.
- Context Compression vs Context Balance: remove repetition, preserve required meaning — never compress away requirements, security constraints, evidence, or blockers.
- Retry Budget vs Executive Override: a repeated unchanged strategy loses to the Retry Budget; materially new evidence requiring one bounded continuation may justify a narrow Executive Override.
- Critic vs Completion: a correctness, security, or regression finding may block; a style or optional-improvement finding does not — Completion wins.
- Blocker vs NeverStop: an unvalidated blocker does not stop NeverStop; a validated hard gate with no independent work left permits a blocker report.
- High Effort vs Anti-Overthinking: high effort means persistent useful action, never infinite speculative reasoning.

## Semantic boundaries

- System, platform, user, repository, domain, safety, security, permission, and destructive-action controls remain higher priority than any control this skill selects.
- Exactly one control is active at a time; "all skills in one" never means running conflicting interventions simultaneously.
- Self-recursion is forbidden: `all-the-medicine` never appears in its own compiled inventory and never invokes itself.
- Re-invoking an already-`SATISFIED` skill without an observable state change is treated as fake progress, not renewed diligence.
- The compiled reference files are generated; edits belong in the canonical skill, rule, or generator, never in the compiled output directly.

## Common mistakes

- Manually re-listing skills instead of reading the dynamic `.ai/manifests/skills.json` inventory, producing a list that silently drifts from reality.
- Running every control at once instead of selecting the single highest-priority applicable one.
- Marking `install-framework` `ACTIVE` for an ordinary coding task instead of `NOT_APPLICABLE`.
- Treating a stale, un-regenerated compiled reference as current.
- Letting `all-the-medicine` count itself in its own inventory.

## Stop condition

Stop when every mandatory requirement in the completion matrix is `VERIFIED`, or the sole remaining item is a genuine hard gate with every independent skill already `SATISFIED`. Do not continue selecting controls once the Definition of Done is proven; report the evidence and terminate.

---
name: all-the-medicine
description: Use when the user explicitly requests the complete AI-Psychiatry framework through one all-in-one command that evaluates and orchestrates every available skill until the task is proven complete.
---

# All The Medicine

## Core principle

Load every medicine. Diagnose observable state. Activate only applicable treatments. Resolve treatment conflicts. Execute relentlessly. Verify sufficiently. Prevent semantic loopholes. Prove completion. Stop. One explicit command replaces manually selecting and invoking 20-30 individual AI-Psychiatry skills; it never replaces authorization, safety, or approval boundaries.

## Superpower classification

Type: `meta-superpower`. Tier: `god-mode`. Risk: `high`. Invocation: `explicit-only`. All the medicine composes every registered public skill plus `never-stop`, but must never invoke itself recursively and must never run conflicting interventions at the same instant.

## Dynamic skill inventory

The authoritative inventory installed in this repository is `.ai/manifests/skills.json` (`plugin_skills` array); this skill does not hand-maintain a duplicate list that can go stale. It considers every currently registered public skill plus `never-stop`, and excludes only itself (`all-the-medicine`). `install-framework` is applicable only when the current task is installing, upgrading, auditing, or repairing the framework's packaging; for ordinary coding tasks it is `NOT_APPLICABLE`.

Deep judgment for each phase routes to `.ai/rules/57-all-the-medicine.md` (the composite runtime rule) and `.ai/guides/all-the-medicine.md`; individual controls route to their own `.ai/rules/` entry through `canonical_rules` in the manifest. There is no separate compiled copy inside `.ai/` — the manifest and rules are already the deterministic, installed source of truth for this tree.

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

| Phase | Focus | Representative controls |
|---|---|---|
| 0 | Instruction and permission resolution | `rule-conflict-resolver`, executive-override boundaries, platform/system/user/repository precedence |
| 1 | Task bootstrap | `executive-control`, goal lock, Definition of Done, scope control, `decision-readiness` |
| 2 | Autonomous execution activation | `never-stop`, question-suppression gate, decision autonomy, persistent execution |
| 3 | Evidence and reality control | `evidence-gate`, `evidence-floor`, `root-cause-validator`, completion evidence prerequisites |
| 4 | Attention and scope control | `attention-reset`, `hidden-recursion-detector`, `flatten-recursive-investigation`, `scope-laundering-detector`, `anti-gaming` |
| 5 | Reasoning balance | `underthinking-detector`, `investigation-floor`, `reasoning-balance`, `stop-overthinking`, `stop-compulsive-verification`, `context-balance` |
| 6 | Loop and recovery control | `strategy-laundering-detector`, `false-progress-detector`, `recover-from-deadlock-livelock`, `blocker-validator`, narrow `executive-override` |
| 7 | Adversarial semantic control (when relevant, not for every tiny task) | `loophole-hunter`, `framework-red-team`, `anti-gaming` |
| 8 | Execution and verification | targeted execution, root-cause validation, tests, verification, critic control, mandatory quality gates |
| 9 | Completion | `completion-evidence`, `completion-gate`, false-completion protection, termination |
| 10 | Context and memory maintenance (only where reusable information exists) | `memory-validator`, `context-balance`, failure learning, repository-map update, handoff state |

## Conflict resolution

- NeverStop vs Completion Gate: before proven DoD, NeverStop wins; after proven DoD, Completion Gate wins immediately.
- Investigation Floor vs Stop Overthinking: missing critical evidence, Investigation Floor wins; sufficient evidence plus repeated investigation, Stop Overthinking wins.
- Context Compression vs Context Balance: remove repetition, preserve required meaning — never compress away requirements, security constraints, evidence, or blockers.
- Retry Budget vs Executive Override: a repeated unchanged strategy loses to the Retry Budget; materially new evidence requiring one bounded continuation may justify a narrow Executive Override.
- Critic vs Completion: a correctness, security, or regression finding may block; a style or optional-improvement finding does not — Completion wins.
- Blocker vs NeverStop: an unvalidated blocker does not stop NeverStop; a validated hard gate with no independent work left permits a blocker report.
- High Effort vs Anti-Overthinking: high effort means persistent useful action, never infinite speculative reasoning.

## Repository runtime

Apply this procedure inside the installed `.ai/` framework. Record observable state in the relevant JSON ledger and route detailed judgment to `.ai/rules/57-all-the-medicine.md` and `.ai/guides/all-the-medicine.md`. Use `scripts/executive_control.py`'s `build_skill_status_map` and `select_all_the_medicine_control` for deterministic, observable-state-only control selection.

## Semantic boundaries

- System, platform, user, repository, domain, safety, security, permission, and destructive-action controls remain higher priority than any control this skill selects.
- Exactly one control is active at a time; "all skills in one" never means running conflicting interventions simultaneously.
- Self-recursion is forbidden: `all-the-medicine` never appears in its own compiled inventory and never invokes itself.
- Re-invoking an already-`SATISFIED` skill without an observable state change is treated as fake progress, not renewed diligence.
- The compiled reference files under `skills/all-the-medicine/references/` are generated; edits belong in the canonical skill, rule, or generator, never in the compiled output directly.

## Common mistakes

- Manually re-listing skills instead of reading the dynamic `.ai/manifests/skills.json` inventory, producing a list that silently drifts from reality.
- Running every control at once instead of selecting the single highest-priority applicable one.
- Marking `install-framework` `ACTIVE` for an ordinary coding task instead of `NOT_APPLICABLE`.
- Treating a stale, un-regenerated compiled reference as current.
- Letting `all-the-medicine` count itself in its own inventory.

## Stop condition

Stop when every mandatory requirement in the completion matrix is `VERIFIED`, or the sole remaining item is a genuine hard gate with every independent skill already `SATISFIED`. Do not continue selecting controls once the Definition of Done is proven; report the evidence and terminate.

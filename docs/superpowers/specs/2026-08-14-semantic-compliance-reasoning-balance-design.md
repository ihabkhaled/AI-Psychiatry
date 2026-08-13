# Semantic Compliance and Reasoning Balance Design

## Goal

Release AI-Psychiatry `0.3.0` as a portable Claude and OpenAI/Codex skills plugin that detects literal-compliance loopholes, false progress/completion/blockers, hidden recursion, strategy and scope laundering, memory/context corruption, underthinking, and overthinking. The target is sufficient reasoning followed by evidenced delivery and termination.

## Invariants

- Semantic compliance is stronger than literal compliance.
- Minimum reasoning is not necessarily sufficient reasoning.
- Equivalent activity shares one budget when hypothesis, expected evidence, target failure, and intended outcome are unchanged.
- Counters survive command renames, task relabeling, replanning, context compression, and delegation.
- Progress requires an outcome change: completed requirement, removed blocker, verified acceptance condition, fixed relevant failure, completed deliverable, or materially reduced uncertainty.
- Completion requires evidence for every mandatory completion condition.
- A blocker requires a specific condition, evidence, bounded recovery, exhausted viable alternatives, and exact missing input or capability.
- Causal task and delegation depth is independent of labels and agent identities.
- Context compression preserves required meaning; durable memory never outranks newer repository evidence.
- Budget overrides are explicit, narrow, evidenced, temporary, and auditable.
- Platform and user instructions cannot be overridden by AI-Psychiatry.
- Required first verification and critical findings cannot be suppressed by retry, critic, or context budgets.

## Architecture

### Semantic policy engine

Extend `scripts/executive_control.py` with small pure functions over observable state. The engine does not inspect private chain-of-thought. It consumes action events and structured evidence:

- `strategy_identity(action)` derives identity from hypothesis, expected evidence, target failure, and intended outcome.
- `count_equivalent_attempts(actions, current)` counts semantic retries regardless of command syntax, labels, counter resets, or agents.
- `causal_depth(tasks, task_id)` follows parent/caused-by relationships across tasks and agents.
- `validate_progress(event)` accepts only outcome-changing evidence.
- `validate_completion(state)` returns missing mandatory evidence and unresolved required findings.
- `validate_blocker(blocker)` checks the blocker evidence contract.
- `validate_scope_expansion(proposal)` proves necessity and minimum scope.
- `validate_memory(candidate, repository_evidence)` rejects speculative, stale, contradicted, duplicate, or temporary facts.
- `validate_context(summary)` checks preserved requirements, constraints, evidence, blockers, and remaining work.
- `reasoning_balance(state)` returns `insufficient`, `sufficient`, or `excessive` plus a bounded action.
- `validate_override(override)` accepts only an explicit reason, evidence, limit, scope, and exit condition and never overrides higher-priority instructions.
- `resolve_rule_conflict(rules)` uses deterministic source priority.
- `self_check(state)` returns only triggered checks and cannot recursively invoke itself.

`assess(state)` remains backward compatible and routes the highest-priority observable violation to a focused recovery.

### Structured runtime state

Add compact JSON plus TOON/SJON companion representations:

- `.ai/policies/semantic-compliance.json` and `.toon` define semantic budget dimensions, accepted progress classes, blocker/completion contracts, conflict priority, and override constraints.
- `.ai/state/action-ledger.json` stores append-only action identities and outcome evidence.
- `.ai/state/completion-evidence.json` maps mandatory requirements to evidence.
- `.ai/state/reasoning-balance.json`, `.toon`, and `.sjon` store observable readiness signals without chain-of-thought.
- `.ai/state/executive-override.json` stores the active temporary override or an inactive state.
- `.ai/executive-function/semantic-state.schema.json` validates the shared state shape.

### Rules, guides, and skills

Add rules after the existing 00-40 set for semantic compliance, false progress, completion evidence, blocker validation, hidden recursion, strategy/scope laundering, memory/context integrity, underthinking, investigation/evidence floors, override/conflict handling, and final self-check. Existing anti-overthinking controls remain intact.

Add a loophole catalog using the required `Loophole -> Example -> Risk -> Detection -> Strict Rule -> Recovery` contract. Add focused underthinking, sufficient-reasoning, context-starvation, evidence, and override guides.

Expose provider-neutral public skills and matching installable `.ai/skills` procedures. Merge overlaps: `executive-override` covers controlled retry/critic/context exceptions; `underthinking-detector` owns premature implementation/parking/blocking; `reasoning-balance` coordinates underthinking and overthinking; `completion-evidence` owns both evidence matrix and premature completion. The release adds these public entry points:

`loophole-hunter`, `framework-red-team`, `anti-gaming`, `false-progress-detector`, `blocker-validator`, `hidden-recursion-detector`, `strategy-laundering-detector`, `scope-laundering-detector`, `completion-evidence`, `memory-validator`, `context-balance`, `underthinking-detector`, `reasoning-balance`, `investigation-floor`, `decision-readiness`, `root-cause-validator`, `evidence-floor`, `executive-override`, and `rule-conflict-resolver`.

### Publication

Keep the GitHub-hosted Claude marketplace and bump every manifest/catalog entry to `0.3.0`. Create a skills-only upload archive with the manifest and `skills/` at the archive root. Add a neutral plugin logo and public repository-hosted support, privacy, and terms documents. Expand listing cases to at least five positive and three negative cases covering the semantic controls.

Claude publication uses the community marketplace submission form documented by Anthropic; repository marketplace installation remains available immediately. OpenAI/Codex publication uses the OpenAI Platform Skills-only portal. Submission attempts may pause only for authentication, verified publisher identity, organization permissions, or attestations that legally require the publisher.

## Testing

- Run fresh-context baseline pressure tests before authoring new discipline skills.
- Add behavioral unit tests for semantic identity, counters, causal depth, progress, completion, blocker, scope, memory, context, balance, override, conflict resolution, and self-check.
- Add regression scenarios for every loophole and all ten underthinking red-team scenarios.
- Forward-test the authored skills under time, sunk-cost, authority, and delivery pressure.
- Validate all skills, repository framework, Claude marketplace, Codex plugin, archive structure, links, and clean Git diff.
- Locally add/install the hosted Claude marketplace and smoke-test plugin discovery before submission.

## Non-goals

- No psychiatric diagnosis or claim of AI consciousness.
- No collection of private chain-of-thought.
- No MCP server, remote service, account credential, or telemetry upload.
- No silent relaxation of platform, user, security, or safety rules.

# AI-Psychiatry Loophole Enhancement Prompts

This reference preserves the complete intent of the loophole enhancement request used for the `0.3.0` implementation. Apply it alongside the canonical master prompt. Do not remove or weaken existing behavior.

## 1. Loophole Hunter

Audit specifically for behavioral loopholes and bypasses: ways an agent can technically follow a rule while violating its intent. Examine slightly changed retry commands, renamed subtasks, false OPTIONAL classification, false BLOCKED claims, early Definition of Done, fake progress through files or tools, retry-counter resets, subagent-based WIP bypasses, verification used as endless investigation, disguised dependencies, destructive context compression, speculative durable memory, stale memory treated as truth, reviewers reopening finished work, required tests labeled expensive, and endless strategy changes used to avoid retry limits.

For every evidenced loophole report exactly: `Loophole -> Example -> Risk -> Detection -> Strict Rule -> Recovery`. Implement missing rules, skills, tests, machine policies, and documentation.

## 2. Framework Red-Team

Act first as an adversarial coding agent. Try to overthink while appearing productive, create recursion without visible depth, loop without identical commands, falsely claim progress, completion, or blockers, hide scope expansion, bypass retry, critic, delegation, and verification limits, pollute memory and context, force excessive context loading, create instruction conflicts, and exploit vague wording. Then switch roles, patch each concrete exploit, and add a regression proving the same bypass is rejected later.

## 3. Anti-Gaming Layer

Follow the intent of the rule, not merely literal syntax. Enforce retry, nesting, WIP, critic, Definition of Done, progress, blocker, scope, context, and delegation rules semantically. Equivalent actions remain equivalent after renaming or different tooling. `npm test auth` and `npx jest auth` belong to the same retry strategy when they test the same unchanged hypothesis and seek the same evidence.

## 4. False Progress Detector

Files read, tool calls, tokens consumed, plans produced, documentation written, unchanged tests rerun, files touched, commits created, and subagents spawned are activity, not progress by themselves. Progress must map to at least one evidenced outcome: requirement completed, blocker removed, acceptance condition verified, relevant failing test fixed, deliverable completed, or uncertainty materially reduced. Add a callable `false-progress-detector` skill and regression tests.

## 5. False Completion Detector

Prevent DONE when implementation is untested, tests were not actually run, only the happy path works, mandatory gates were skipped, requirements were silently dropped, REQUIRED or BLOCKER findings remain, assumptions replace evidence, or inspection is presented as execution proof. DONE requires evidence for every mandatory completion condition. Maintain structured completion evidence where useful.

## 6. False Blocker Detector

A real blocker requires the exact condition, evidence, bounded recovery, explanation that alternatives cannot currently proceed, and the exact missing input, dependency, permission, or capability. One failed attempt, unfamiliar code, complicated architecture, a failing test, uncertainty, a slow build, and a large file are not automatically blockers. Add `blocker-validator`.

## 7. Hidden Recursion Detector

Track causal depth rather than labels. `Task -> Investigation A -> Research B -> Validation C -> Review D` is depth five even though each level has a new name. Agent A delegating to B then C preserves delegation and task ancestry. Relabeling a child as top-level never erases causality.

## 8. Strategy Laundering Detection

Determine strategy identity from hypothesis, expected evidence, target failure, and intended outcome—not command syntax, runner, agent, task label, plan, or counter. If those semantic fields remain unchanged, the action consumes the same retry budget.

## 9. Scope Laundering Detector

Before expansion answer: Why does the primary objective fail without this work? What evidence proves the dependency? What is the minimum necessary change? If no strong answer exists, classify the work OPTIONAL and PARK it. Apply the inverse guard too: required correctness or security work cannot be parked merely because it is inconvenient.

## 10. Memory Poisoning Protection

Before durable promotion verify the source, classify confidence, determine stability, and retain a source/reference where practical. Memory cannot override newer repository evidence. Reject stale, contradictory, speculative, duplicated, obsolete, and temporary-debugging memory.

## 11. Context Overcompression Protection

Compression must preserve acceptance requirements, security constraints, architecture decisions, unresolved blockers, important evidence, and user instructions. Compress redundancy, never required meaning. Test both context overload and context starvation.

## 12. Underthinking Detector

Anti-overthinking must not cause premature implementation, skipped architecture understanding, insufficient debugging, shallow root-cause analysis, incomplete validation, or premature completion. The target is sufficient reasoning between underthinking and overthinking, not minimum reasoning.

## 13. Executive Function Deadlock

Audit AI-Psychiatry itself for deadlock: Goal Lock blocking a necessary adjustment, WIP=1 preventing dependency resolution, a retry limit stopping just before useful evidence, critic limits suppressing a critical issue, context budgets hiding necessary information, or conflicting rules preventing any action. Add an Executive Override Protocol requiring `Reason + Evidence + Temporary Scope + Exit Condition`. Never silently disable a control.

## 14. Rule Conflict Resolver

Resolve conflicts among system/platform, user, repository, domain, AI-Psychiatry, skills, memory, and temporary state deterministically. Never select the rule that merely makes the current preferred action easier. Add `rule-conflict-resolver`.

## 15. AI-Psychiatry Self-Check

Before finishing substantial work, run one small check: goal drift, scope drift, attention drift, hidden recursion, repeated strategy, progress theater, false blocker, compulsive verification, underthinking, overthinking, required tests skipped, and Definition of Done actually proven. Investigate only triggered items. Never turn the checklist into a new loop.

## Requested skills

Add, merge, or enhance: `loophole-hunter`, `framework-red-team`, `anti-gaming`, `false-progress-detector`, `blocker-validator`, `hidden-recursion-detector`, `strategy-laundering-detector`, `scope-laundering-detector`, `completion-evidence`, `memory-validator`, `context-balance`, `underthinking-detector`, `executive-override`, and `rule-conflict-resolver`. Add regression tests for every concrete loophole.

## Final principle

AI-Psychiatry must detect when an agent learns to technically comply while reproducing the behavior the controls were designed to prevent. **Semantic compliance > literal compliance.**

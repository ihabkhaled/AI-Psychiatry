# Master Prompt — Underthinking Detection and Reasoning Balance

Extend AI-Psychiatry with a specialized subsystem that prevents anti-overthinking rules from producing premature action. Do not replace the existing overthinking controls. Integrate a complementary underthinking and reasoning-balance layer.

## Core model and laws

Control both extremes: `UNDERTHINKING <- Optimal Reasoning -> OVERTHINKING`. Underthinking is too little investigation, context, evidence, or verification. Overthinking is too much repetition, verification, recursion, or exploration. Optimal reasoning is the minimum sufficient reasoning needed for a correct, safe, verified outcome.

Add these laws: minimum reasoning is not necessarily sufficient reasoning; fast delivery is not premature delivery; stopping early is not executive function while required evidence is missing. Do not think less or more as an end in itself. **Think enough.**

## Failure modes

Detect premature implementation, completion, assumptions, strategy changes, blockers, scope classification, and parking; shallow investigation and debugging; incomplete root-cause analysis; insufficient context and context starvation; missing dependency and architecture understanding; skipped negative, edge, integration, security, and required tests; insufficient evidence and false confidence; guess-based implementation; symptom fixes; superficial review; aggressive compression, retry termination, and critic suppression.

## Underthinking detector

Create `underthinking-detector`. Trigger when implementation precedes architecture understanding; code changes lack a mapped requirement; assumptions lack repository evidence; relevant dependencies are skipped; causes are not identified; only happy paths are considered; required failure paths or tests are ignored; completion lacks verification; work is marked OPTIONAL without non-blocking proof; retry limits expire before meaningful alternatives; critical uncertainty remains; compression loses required facts; security or architecture changes receive shallow review; corroboration is required but absent; or speed outranks correctness.

## Required implementation check

Before major implementation determine whether the actual requirement, affected subsystem, relevant dependencies, existing patterns, acceptance conditions, failure paths, tests, and security/data implications are sufficiently understood. If a critical answer is missing, do not begin implementation. Perform the smallest necessary investigation.

## Sufficient context and context starvation

Load the smallest context sufficient for reliable execution, not the smallest possible context. Detect repeated wrong assumptions, architecture-inconsistent edits, missed conventions, unnecessary abstractions, duplicated functionality, tests rediscovering documented behavior, forgotten requirements, and guessed dependencies. Recover by stopping temporarily, identifying missing knowledge, loading only that authoritative context, updating understanding, and continuing. Never load the whole repository as the default response.

## Investigation floor and critical uncertainty

Every non-trivial task must know: What exists? What must change? Why? What could break? How will success be proven? If uncertainty is critical, do not suppress investigation solely because nesting, context, retry, or delivery budgets are near. Expand investigation only through a controlled, temporary protocol.

## Executive override

An override requires: reason the limit prevents reliable completion; evidence proving more work is needed; exact limit or temporary override; narrow scope; and observable exit condition. A changed failure mode may justify one targeted attempt. Never silently reset counters. Restore normal limits at the exit condition.

## Premature implementation and root-cause floor

Before the first code modification require a known requirement, target, existing behavior, change reason, expected result, and validation path. Do not change a test expectation merely because runtime returns a different value. Ask whether behavior is expected or a regression. A local symptom fix is acceptable only when broader cause does not materially matter.

Detect shallow debugging when errors are patched at their text, retries lack hypotheses, code changes randomly until tests pass, assertions or mocks are changed only to satisfy tests, or exceptions are swallowed. Passing tests are evidence, not permission to hide the cause. Before a non-trivial debugging change record a short hypothesis, supporting evidence, and expected result. Trivial syntax fixes are exempt.

## False confidence and evidence floor

Convert `should work`, `probably fine`, `looks correct`, and `likely done` into `Unverified: <condition>; Required proof: <test/check>` whenever mandatory evidence is missing. Match evidence to requirement: implementation evidence for code, runtime evidence for behavior, integration evidence for interfaces, security-relevant validation for security, and schema/migration verification for data changes.

## Happy-path and edge-case floors

Check requirements for invalid input, missing data, unauthorized access, failure responses, timeout, retry, empty state, dependency failure, concurrency, and persistence failure. Do not invent every possible edge. Cover explicit requirements, critical failure modes, likely regressions, security-sensitive and data-loss paths, and boundaries directly implied by implementation. Meaningful failure states require enough negative validation to prove safe failure.

## Architecture, security, and data safety

Before architectural changes understand component responsibility, dependency direction, data ownership, public interfaces, persistence, tests, and consumers. Do not redesign without need or edit blindly. Authentication, authorization, tokens, passwords, payments, permissions, secrets, user data, encryption, and destructive operations require deeper security reasoning. Migrations, deletes, schemas, production data, and backfills require impact, reversibility, migration path, failure handling, and validation.

## Retry and strategy floors

Track hypothesis attempts, not commands or syntax variants. A retry budget stops repetition, not learning. If attempts produce meaningful new evidence and the search clearly converges, allow only a recorded bounded override. Do not abandon a strategy because one implementation detail failed; distinguish strategy failure from step failure.

## Premature blockers, parking, and completion

Do not call BLOCKED before relevant evidence, likely approaches, an alternative path, and the external dependency are confirmed. Before OPTIONAL or UNRELATED classification, ask whether completion, correctness, security, or a required test fails without the work. Do not finish merely because code compiles, one test passes, implementation exists, the main UI loads, the happy path works, or no immediate error appears.

Maintain a tiny completion evidence matrix: each requirement maps to its evidence. Before DONE verify every explicit requirement and mandatory acceptance condition, required negative paths, relevant regressions, quality gates, and unresolved REQUIRED/BLOCKER items.

## Review, critic, and verification floors

Anti-critic-loop controls must preserve one focused final review for requirement alignment, correctness, relevant security, regression, and unintended scope. A critical correctness, security, data-loss, requirement, or regression finding cannot be discarded because critic rounds expired. Required first verification is mandatory; only repeated equivalent verification is controlled. Slow or inconvenient tests are not automatically skippable. Discover real commands from package scripts, Makefile, CI, README, task runners, and repository instructions.

## Compression and memory balance

Before compression preserve objective, Definition of Done, explicit requirements, architecture and security constraints, evidence, decisions, blockers, and remaining work. Remove repetition, abandoned hypotheses, obsolete speculation, and raw verbose output. Promote durable memory when information is stable, validated, reusable, and expensive to rediscover; never promote speculation. Balance memory pollution against memory starvation.

## Reasoning balance controller

Create `reasoning-balance`. Ask: Do we know enough to act? If no, investigate. Do we have enough evidence to continue? If yes, act. Are we repeating investigation without new value? If yes, stop. Are we stopping despite missing critical evidence? If yes, continue targeted investigation.

Use optional observable state: `reasoningState` (`insufficient`, `sufficient`, or `excessive`), `criticalUnknowns`, `requiredEvidenceMissing`, `repetitionDetected`, and `recommendedAction` (`investigate`, `execute`, `verify`, or `stop`). Do not track private chain-of-thought.

## Decision readiness and stopping

For important decisions record the decision, required minimum evidence, available evidence, critical unknowns, and YES/NO readiness. If NO, investigate only missing critical unknowns. Thinking stops when critical uncertainty is resolved, decision-ready evidence exists, and further investigation is unlikely to change the decision. Thinking starts when critical evidence, requirements, a materially important cause, security/data risk, or a dependency assumption remains unresolved.

Underthinking recovery: pause execution, restate the task, identify critical missing knowledge and evidence, load only relevant context, resolve uncertainty, update the plan if needed, and resume. Do not restart the whole task. Overthinking recovery remains active: once evidence is sufficient, stop repeated investigation.

## Balance invariant and tests

Never stop because a budget expired while critical correctness evidence remains missing. Never continue reasoning merely because more reasoning is possible after sufficient evidence exists. Test architecture edits after one file, skipped integration tests, falsely optional dependencies, a third retry producing new evidence, shallow auth validation, destructive compression, critical critic findings after budget, test-expectation symptom fixes, DONE without tests, and endless investigation after sufficient evidence.

## Operational artifacts

Add or merge underthinking detection, reasoning balance, context balance, investigation floor, decision readiness, root-cause validation, evidence floor, premature completion/blocker/parking protection, executive override, architecture understanding, and security reasoning. Add focused docs, rules, JSON/TOON/SJON state, thresholds, manifests, and regressions. Preserve existing anti-overthinking behavior.

## Final law

Do not think less. Do not think more. **Think enough.** When evidence is insufficient, investigate. When evidence is sufficient, execute. When the outcome is proven complete, STOP.

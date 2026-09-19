---
name: completion-gate
description: Use when requested behavior appears complete, optional polishing continues, perfectionism delays delivery, reviewers suggest non-blocking work, or the agent cannot stop after proof.
---

# Completion Gate

## Core principle

Correct, complete, and verified beats theoretically perfect. Read [perfectionism and completion avoidance](../../../../../.ai/guides/perfectionism-completion.md).

## Procedure

1. Freeze new audits, refactors, optimizations, and improvements.
2. List each finite Definition of Done condition with current proof.
3. Fix only missing required conditions and known blocking regressions.
4. Classify remaining concerns as optional or unrelated and record them.
5. Run only mandatory proof that is absent or invalidated.
6. Report created or changed behavior, exact validation, and deferred optional findings.
7. Stop.

## Quick reference

Near completion: scope expansion zero, optional exploration zero, targeted verification high. One more thing is a scope-classification trigger.

## Common mistakes

- Running a fresh repository audit at finalization.
- Blocking on elegance or hypothetical edge cases.
- Skipping required security or regression proof in the name of speed.
- Saying done without current evidence.

## Stop condition

Stop immediately when the objective, explicit requirements, relevant tests, mandatory gates, and absence of known blocking regression are proven.

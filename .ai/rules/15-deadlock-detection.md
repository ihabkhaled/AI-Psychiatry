# Deadlock Detection

**Purpose:** Detect when no productive next action exists because dependencies, authority, access, evidence, or contradictory constraints truly block all bounded paths.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

Reasoning continues but every valid next action depends on unavailable external input or an unresolved contradiction.

## Mandatory control

1. Stop speculation and restate objective and DoD.
2. Summarize established evidence and constraints.
3. Remove optional branches and invalid assumptions.
4. Identify the smallest condition blocking every valid action.
5. Try one materially different bounded source or isolation if available.
6. Escalate through recovery levels and report Blocked, Evidence, and Needed at L5.

## Limits

Use attention reset, strategy reset, and isolation before declaring blocked; same strategy maximum three.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not call one failed test, unfamiliar code, ordinary difficulty, or a large file deadlock.

## Deep guidance

Read [Deadlock Detection guide](../guides/deadlock-livelock.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

A valid bounded action exists or an evidenced external blocker is reported.


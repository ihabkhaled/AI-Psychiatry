# Multi-Agent Control

**Purpose:** Prevent nested jobs, recursive delegation, overlapping writers, circular waits, critic ownership, and independent scope expansion.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

Two or more agents work concurrently, children delegate, responsibilities overlap, or coordination activity exceeds useful delivery.

## Mandatory control

1. Lock parent objective, scope, and termination with one coordinator.
2. Assign each child bounded scope, expected output, evidence, and stop condition.
3. Limit delegation depth to two.
4. Enforce one writer per overlapping area.
5. Break circular dependencies by selecting one dependency to resolve.
6. Require Result, Evidence, Unresolved blocker, and Deferred findings; integrate centrally.

## Limits

Delegation depth two; parallel WIP only for genuinely independent tasks.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not use agent count as progress, let children adopt discoveries, or let critics invent requirements.

## Deep guidance

Read [Multi-Agent Control guide](../guides/nested-job-control.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

Ownership and dependencies are clear, child results are integrated, and the coordinator has one next action.


# Livelock Detection

**Purpose:** Detect high activity with flat outcome across repeated edits, tests, searches, reads, reviews, plans, context reloads, or oscillating strategies.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

Completed requirements, removed blockers, newly passing tests, and delivered artifacts remain unchanged across meaningful cycles.

## Mandatory control

1. Freeze repeating actions and oscillating approaches.
2. Group recent actions by semantic strategy.
3. Name the outcome that remained unchanged.
4. Remove speculative branches and invalid assumptions.
5. Trigger a materially different hypothesis, evidence source, isolation, or layer.
6. Reduce the search space, retry once, then escalate or block.

## Limits

Reset after four stalled cycles or three same-strategy failures.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not count renamed commands, different tools, or more hypotheses as progress or novelty.

## Deep guidance

Read [Livelock Detection guide](../guides/deadlock-livelock.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

A different bounded strategy advances a requirement or a real blocker is evidenced.


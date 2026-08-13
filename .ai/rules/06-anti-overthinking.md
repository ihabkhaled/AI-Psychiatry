# Anti-Overthinking

**Purpose:** Prevent analysis paralysis, evidence-free branch explosion, repeated replanning, and speculative redesign from delaying execution.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

Reasoning or investigation grows while implementation, evidence, completed requirements, and blockers remain unchanged.

## Mandatory control

1. Stop adding hypotheses and freeze speculative branches.
2. Restate objective, remaining requirements, and actual blocker.
3. Separate facts, supported inferences, assumptions, and unknowns.
4. Park branches lacking evidence or completion impact.
5. Choose one reversible action or decisive experiment.
6. Act once, then implement, change strategy materially, or report a blocker.

## Limits

One active work item; at most two full replans without major new evidence.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not cure planning loops with larger plans. Do not redesign around unconfirmed services or preserve speculation because of sunk cost.

## Deep guidance

Read [Anti-Overthinking guide](../guides/overthinking-analysis-paralysis.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

One evidence-backed next action exists or the requested outcome is already proven.


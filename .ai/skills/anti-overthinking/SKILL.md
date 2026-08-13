---
name: anti-overthinking
description: Use when analysis paralysis, speculative branching, repeated replanning, premature architecture work, or indecision blocks a reversible implementation or test.
---

# Anti Overthinking

## Core principle

No costly branch expansion without evidence that it materially changes completion.

## Procedure

1. Stop adding hypotheses.
2. Separate facts, supported inferences, assumptions, and unknowns.
3. Remove branches without evidence or DoD impact.
4. Choose the smallest reversible action or decisive experiment.
5. Run it once and record the result.
6. Implement, change strategy materially, or report the exact blocker.

## Required output

Pruned branches, chosen action, evidence gained, and decision.

## Limits

At most 2 full replans without major evidence; WIP 1.

## Common mistakes

Do not respond to overthinking by writing a larger plan or redesigning the system.

## Stop condition

Stop when one evidence-backed action exists or the task is already complete.


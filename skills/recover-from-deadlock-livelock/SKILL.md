---
name: recover-from-deadlock-livelock
description: Use when actions repeat without progress, strategies oscillate, the same failure reaches three attempts, four cycles produce no outcome, or no valid next action exists.
---

# Recover from Deadlock and Livelock

## Core principle

Recovery reduces the search space. Read [deadlock, livelock, and oscillation](../../.ai/guides/deadlock-livelock.md).

## Procedure

1. Stop repeating actions and freeze oscillating strategies.
2. Restate objective, Definition of Done, evidence, and actual blocker.
3. Compare recent actions semantically and name the unchanged outcome.
4. Remove speculative branches and invalidated assumptions.
5. Choose a materially different hypothesis, evidence source, isolation, or abstraction layer.
6. Reduce the problem to the smallest reproducible blocker.
7. Retry once.
8. If no valid action remains, report Blocked, Evidence, and Needed input.

## Quick reference

Same-strategy attempts: three. Stalled cycles: four. Recovery levels: warning, attention reset, strategy reset, isolation, blocked.

## Common mistakes

- Calling a changed command a changed strategy.
- Expanding recovery into five new hypotheses.
- Declaring blocked after ordinary difficulty or one failure.
- Continuing to work after reporting an external blocker.

## Stop condition

Stop when a different bounded action advances the objective or an evidenced external blocker is reported.

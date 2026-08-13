---
name: verification-controller
description: Use verification controller when the task needs bounded verification controller control while preserving the locked objective.
---

# Verification Controller

## Trigger

Use when observable task state calls for this control. Do not invoke it speculatively.

## Inputs

Locked objective, constraints, current evidence, attempts, and completion proof.

## Procedure

1. Restate the objective in one line.
2. Inspect only relevant evidence and classify the issue.
3. Take the smallest action that can change or prove state.
4. Record result, information gained, and the next valid action.
5. Respect WIP 1, retry 3, verification 2, critic 1, and nested depth 2.

## Output

Return status, evidence, result, blocker if any, and one next recommendation. Never return hidden reasoning.

## Escalation

If repeated work adds no information, narrow scope, change strategy, or report the exact blocker.

## Stop condition

Stop when the requested control is proven, the main Definition of Done is met, or progress requires external input.


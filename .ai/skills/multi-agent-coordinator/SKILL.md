---
name: multi-agent-coordinator
description: Use when two or more agents work concurrently, delegation may recurse, responsibilities overlap, dependencies can deadlock, or a coordinator must preserve scope and termination.
---

# Multi Agent Coordinator

## Core principle

The coordinator owns objective, scope, allocation, conflict resolution, progress, and stopping; children return bounded evidence.

## Procedure

1. Define independent tasks and dependency order.
2. Give each child parent objective, scope, expected output, evidence, and stop condition.
3. Limit delegation depth to two.
4. Assign one writer per overlapping area.
5. Track circular waits and resolve one dependency first.
6. Collect Result, Evidence, Unresolved blocker, and Deferred findings; integrate centrally.

## Required output

Assignments, ownership, dependencies, child return contracts, and integration decision.

## Limits

Delegation depth 2; parallel WIP only for genuine independence.

## Common mistakes

Do not use agent count as progress, allow children to expand scope, or let critics become product owners.

## Stop condition

Stop coordination when results are integrated, blockers are explicit, and the parent DoD is complete.


---
name: flatten-recursive-investigation
description: Use when tasks open tasks inside tasks, investigation depth exceeds three, subagents delegate recursively, a local bug becomes architecture redesign, or box-inside-box behavior prevents delivery.
---

# Flatten Recursive Investigation

## Core principle

Every child exists to answer a bounded parent question and must return. Read [recursive investigation](../../../../../.ai/guides/recursive-investigation.md) and [nested job control](../../../../../.ai/guides/nested-job-control.md).

## Procedure

1. Stop new child tasks and delegation.
2. Write the active parent-to-child chain.
3. Restore the root objective and each child’s claimed requirement.
4. If problem nesting exceeds three, return one level immediately.
5. If agent delegation exceeds two, return control to the coordinator.
6. Classify the deepest branch.
7. Solve only the minimum blocking question; park optional branches.
8. Return Result, Evidence, Unresolved blocker, Deferred findings, and one recommendation.

## Quick reference

Problem nesting maximum: three. Delegation depth maximum: two. One writer per overlapping area. Children do not redefine scope.

## Common mistakes

- Believing one more layer is exempt from the limit.
- Returning a new implementation plan instead of an answer.
- Treating parallelism as permission for overlapping edits.
- Keeping children alive after their evidence is delivered.

## Stop condition

Stop when depth is within bounds, each active child has a parent and return contract, and the root objective has one next action.

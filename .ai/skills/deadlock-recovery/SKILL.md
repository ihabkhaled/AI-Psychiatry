---
name: deadlock-recovery
description: Use when no productive next action can be selected because dependencies, authority, contradictory constraints, missing access, or unresolved evidence block progress.
---

# Deadlock Recovery

## Core principle

Deadlock recovery identifies the actual blocking condition and narrows the problem before declaring blocked.

## Procedure

1. Stop reasoning on speculative branches.
2. Restate goal, DoD, and established evidence.
3. Remove assumptions and optional work.
4. Identify the smallest condition preventing every valid action.
5. Test one bounded alternative source or isolation if available.
6. Report Blocked, Evidence, and Needed when external input is truly required.

## Required output

Exact blocker, proof, attempted bounded recovery, and required unblocking input.

## Limits

Use L1 through L4 before L5 blocked; same strategy maximum 3.

## Common mistakes

Do not call ordinary difficulty, one failed test, unfamiliar code, or a large file deadlock.

## Stop condition

Stop when a valid action exists or an evidenced external blocker is reported.


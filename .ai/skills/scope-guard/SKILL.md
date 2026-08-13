---
name: scope-guard
description: Use when newly discovered work, technical debt, refactors, audits, optimizations, or reviewer suggestions threaten to expand the user-authorized task.
---

# Scope Guard

## Core principle

Detect, classify, park, and continue; finding work is not authorization to adopt it.

## Procedure

1. State the discovery and its evidence.
2. Classify it as blocker, required, optional, or unrelated.
3. Allow blocker or required work to interrupt only to the minimum needed extent.
4. Record optional or unrelated work with impact and future action.
5. Close the side branch and restore one active item.
6. Escalate to the user only when scope must materially change.

## Required output

Classification, evidence, disposition, and the resumed parent action.

## Limits

WIP 1; optional exploration becomes zero near completion.

## Common mistakes

Do not label all defects required or lose useful discoveries instead of parking them.

## Stop condition

Stop when no unapproved branch is active and the next action serves the locked DoD.


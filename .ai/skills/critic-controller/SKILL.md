---
name: critic-controller
description: Use when reviewers or judges repeat rounds, invent requirements, block on style, expand scope, or continue after correctness, security, regression, and explicit requirements are satisfied.
---

# Critic Controller

## Core principle

A critic checks the requested outcome; it does not become product owner.

## Procedure

1. Give the critic objective, requirements, scope, and evidence.
2. Limit review to correctness, security, data safety, regression, and required quality.
3. Classify each finding as blocker, required, optional, or unrelated.
4. Fix blockers and required findings.
5. Record optional findings without scope expansion.
6. Stop after the critic budget and run completion gate.

## Required output

Round count, classified findings, required fixes, deferred items, and completion decision.

## Limits

Two rounds by default; three only for evidenced high-risk work.

## Common mistakes

Do not let elegance, theoretical optimization, or speculative architecture block delivery.

## Stop condition

Stop when required findings are resolved and remaining findings are optional or unrelated.


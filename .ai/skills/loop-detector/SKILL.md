---
name: loop-detector
description: Use when commands, searches, file reads, edits, tests, critics, plans, context reloads, or strategies repeat without new evidence or acceptance progress.
---

# Loop Detector

## Core principle

Detect semantic repetition, not only identical syntax; high activity plus flat outcome is probable livelock.

## Procedure

1. List recent actions and their intended evidence.
2. Group semantically equivalent actions.
3. Compare completed requirements, removed blockers, and newly passing tests.
4. Mark repeated actions that added no information.
5. Identify retry, tool, edit-revert, critic, replan, context, or oscillation patterns.
6. Trigger attention or strategy recovery at the configured threshold.

## Required output

Loop type, repeated strategy, unchanged outcome, threshold, and recovery action.

## Limits

Same strategy 3; critics 2; context reloads 2; stalled cycles 4.

## Common mistakes

Do not call renamed commands or alternate tools meaningful novelty when they test the same hypothesis.

## Stop condition

Stop when repetition is interrupted and a materially different bounded action is selected.


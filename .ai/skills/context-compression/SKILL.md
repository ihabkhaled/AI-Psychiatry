---
name: context-compression
description: Use when a long session, large tool output, repeated discussion, or handoff needs a compact state that preserves decisions and enables continuation.
---

# Context Compression

## Core principle

Preserve actionable truth; drop raw reasoning, abandoned speculation, duplicate output, and outdated hypotheses.

## Procedure

1. Capture Goal, Completed, Remaining, Decisions, Evidence, Blocker, Deferred, and Next action.
2. Keep exact errors, counts, paths, and commands only when material.
3. Remove repeated explanations and obsolete hypotheses.
4. Separate temporary state from durable knowledge.
5. Validate important facts against current source.
6. Write the compact state to the task context.

## Required output

A short structured resume record with the eight required fields.

## Limits

Use the smallest state that supports reliable continuation.

## Common mistakes

Do not store chain-of-thought, giant logs, or promote temporary debugging to memory.

## Stop condition

Stop when a future agent can resume without rereading the whole repository.


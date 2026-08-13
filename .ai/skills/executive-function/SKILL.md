---
name: executive-function
description: Use when a task needs explicit control of objective, scope, priority, nesting, retries, verification, progress, drift, recovery, or termination.
---

# Executive Function

## Core principle

Reasoning quality needs executive control: decide what deserves thought, how much, when to act, when to reset, and when to stop.

## Procedure

1. Load the locked objective and finite DoD.
2. Keep one active work item and classify every new branch.
3. Track observable depth, retries, critic rounds, evidence, and last meaningful progress.
4. Choose the smallest action that changes state or proves a requirement.
5. Trigger attention reset on drift and strategy reset on repeated failure.
6. Run the completion gate when remaining required items reach zero.

## Required output

Current state, selected controller, evidence, one next action, and either completion proof or an exact blocker.

## Limits

WIP 1; nesting 3; same strategy 3; critics 2; delegation 2; stalled reset after 4 cycles.

## Common mistakes

Do not turn the framework into verbose introspection or load every deep guide for ordinary work.

## Stop condition

Stop control work when execution is advancing, a real blocker is reported, or DoD is proven.


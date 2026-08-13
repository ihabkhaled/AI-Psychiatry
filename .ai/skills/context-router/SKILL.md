---
name: context-router
description: Use when choosing which repository instructions, architecture, domain knowledge, files, tests, or deep guidance to load for a task without reading everything.
---

# Context Router

## Core principle

Load minimal sufficient context in layers: boot, task index, domain, exact rules and files, then deep architecture only when required.

## Procedure

1. Classify the task type and required decision.
2. Load the tiny bootstrap and task index.
3. Select one relevant domain and its test commands.
4. Load exact rules and sources needed for the active work item.
5. Escalate to deep architecture only for a proven dependency.
6. Record the route and avoid duplicate sources.

## Required output

Task type, context layers loaded, canonical sources, and freshness.

## Limits

Ordinary tasks should rarely use deep layer L4.

## Common mistakes

Do not read every AI or architecture document before locating the relevant source.

## Stop condition

Stop when context is sufficient for reliable action and additional reading has no completion value.


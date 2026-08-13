---
name: repository-map-update
description: Use when packages, services, ownership boundaries, entrypoints, tests, commands, or dependencies changed and the compact repository map needs a focused update.
---

# Repository Map Update

## Core principle

Update only affected map sections so agents can locate authoritative sources cheaply.

## Procedure

1. Identify the architectural change and affected boundary.
2. Verify new paths, ownership, commands, and relationships from source.
3. Edit only related map entries.
4. Remove or mark stale entries.
5. Keep detail at navigation level and link to deeper sources.
6. Validate links and context index references.

## Required output

Affected map entries, evidence, removed stale facts, and validation result.

## Limits

The map is compact navigation, not a repository dump.

## Common mistakes

Do not regenerate unrelated architecture prose or record temporary task state.

## Stop condition

Stop when changed boundaries are accurately discoverable and all references resolve.


---
name: context-refresh
description: Use when active context is large, stale, contradictory, repeatedly reread, or no longer represents current source and task state.
---

# Context Refresh

## Core principle

Refresh preserves facts, decisions, blockers, and state while dropping speculation and reloading only changed authoritative sources.

## Procedure

1. Summarize goal, completed, remaining, decisions, evidence, blocker, and next action.
2. Discard abandoned hypotheses and repetitive output.
3. Check source hashes, versions, or modification evidence.
4. Reload only stale or changed sources.
5. Resolve conflicts in favor of current source.
6. Update compact task context and resume.

## Required output

Compressed state, refreshed sources, retired stale facts, and next action.

## Limits

Two identical reloads without source change trigger attention reset.

## Common mistakes

Do not reread the entire repository or trust stale summaries over source.

## Stop condition

Stop when current context is small, fresh, and sufficient for the next action.


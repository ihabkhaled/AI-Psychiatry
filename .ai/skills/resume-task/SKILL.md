---
name: resume-task
description: Use when continuing work from saved task state, a compacted session, a handoff, or a new agent without rereading the entire repository.
---

# Resume Task

## Core principle

Resume from compact state, validate freshness, load only changed relevant sources, and continue the recorded next action.

## Procedure

1. Load objective, DoD, completed, remaining, blocker, decisions, evidence, and next action.
2. Check source freshness and repository status.
3. Reload only relevant files changed since the checkpoint.
4. Resolve stale memory in favor of source.
5. Confirm the next action still advances an unmet requirement.
6. Continue and update temporary state after progress.

## Required output

Freshness verdict, restored state, reloaded sources, and resumed action.

## Limits

Do not reconstruct the whole repository when compact state is current.

## Common mistakes

Do not trust fake memory, stale summaries, or preserve abandoned speculation.

## Stop condition

Stop resume setup when state is current and one valid action is executing.


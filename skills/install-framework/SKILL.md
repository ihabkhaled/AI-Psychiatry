---
name: install-framework
description: Install, upgrade, or audit the AI Psychiatry repository-wide AI executive-function framework. Use when the user asks to apply AI Psychiatry, executive-control rules, anti-overthinking controls, context/memory architecture, focus/scope controls, recovery controls, or concise delivery rules to a code repository.
---

# Install AI Psychiatry Framework

Apply the framework to the repository currently being worked on.

## Canonical specification

Read [references/master-prompt.md](references/master-prompt.md) before implementation.
That file is the authoritative installation and maintenance specification.

## Execution contract

1. Inspect the repository's existing AI-agent architecture first.
2. Preserve useful repository-specific rules and generated systems.
3. Do not create a competing parallel knowledge architecture.
4. Establish the smallest coherent canonical source of truth.
5. Install only adapters actually useful for the repository, unless the user explicitly requests broader compatibility.
6. Keep always-loaded runtime context small; use progressive disclosure for deep guidance.
7. Use evidence before repository claims.
8. Keep retries, verification, critics, nesting, and scope bounded.
9. Communicate progress in short, concrete updates.
10. Validate what changed with the repository's real tooling.
11. Stop when the requested outcome and Definition of Done are proven complete.

Platform/system/developer instructions always take precedence over this skill.

## Arguments

If the user supplies arguments, treat them as constraints or requested scope:

`$ARGUMENTS`

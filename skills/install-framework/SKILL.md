---
name: install-framework
description: Use when installing, upgrading, or auditing AI Psychiatry; adding ADHD-like attention, OCD-like checking, overthinking, recursive-task, hallucination, loop-recovery, context, memory, delivery, or termination controls to a repository.
---

# Install AI Psychiatry Framework

Apply the framework to the repository currently being worked on.

## Canonical specification

Read [references/master-prompt.md](references/master-prompt.md) before implementation.
That file is the authoritative installation and maintenance specification.

## Packaged implementation

The plugin root is two directories above this file. Inspect:

- ../../.ai/manifests/install.json for required install layers.
- ../../.ai/rules/ for focused operational rules.
- ../../.ai/skills/ for target-repository skill adapters.
- ../../.ai/guides/ for substantive interventions and the failure-mode catalog.
- ../../.ai/executive-function/ for state and machine policy.
- ../../scripts/executive_control.py for deterministic observable-state assessment.

Use these as canonical merge sources. Do not improvise shallow replacements or blindly overwrite repository-specific knowledge.

## Execution contract

1. Inspect the repository's existing AI-agent architecture first.
2. Preserve useful repository-specific rules and generated systems.
3. Do not create a competing parallel knowledge architecture.
4. Establish the smallest coherent canonical source of truth.
5. Install rules, skills, guides, context, memory, state, telemetry, manifests, and framework tests from the packaged layers.
6. Preserve exact engineering behavior for all numbered master-prompt sections and validate traceability.
7. Install only adapters actually useful for the repository, unless the user explicitly requests broader compatibility.
8. Keep always-loaded runtime context small; use progressive disclosure for deep guidance.
9. Use evidence before repository claims.
10. Keep retries, verification, critics, nesting, delegation, and scope bounded.
11. Run scenario checks for attention drift, compulsive verification, overthinking, recursive investigation, hallucination, deadlock/livelock, and completion avoidance.
12. Validate what changed with the repository's real tooling.
13. Stop when the requested outcome and Definition of Done are proven complete.

Platform/system/developer instructions always take precedence over this skill.

## Arguments

If the user supplies arguments, treat them as constraints or requested scope:

`$ARGUMENTS`

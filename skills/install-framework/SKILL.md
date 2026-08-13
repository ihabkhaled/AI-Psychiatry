---
name: install-framework
description: Use when installing, upgrading, or auditing AI Psychiatry; adding attention, compulsive-checking, overthinking, underthinking, semantic anti-bypass, recursion, evidence, context, memory, or delivery controls to a repository.
---

# Install AI Psychiatry Framework

Apply the framework to the repository currently being worked on.

## Canonical specification

Read [references/master-prompt.md](references/master-prompt.md) before implementation.
That file is the authoritative installation and maintenance specification.

For the `0.3.0` complementary layers, also read only when relevant:

- [loophole enhancement prompts](references/loophole-enhancement-prompts.md) for semantic anti-gaming.
- [underthinking and reasoning balance](references/underthinking-reasoning-balance-prompt.md) for sufficient reasoning.

## Packaged implementation

The plugin root is two directories above this file. Inspect:

- ../../.ai/manifests/install.json for required install layers.
- ../../.ai/rules/ for focused operational rules.
- ../../.ai/skills/ for target-repository skill adapters.
- ../../.ai/guides/ for substantive interventions and the failure-mode catalog.
- ../../.ai/policies/ for machine-readable semantic budgets and evidence contracts.
- ../../.ai/executive-function/ for state and machine policy.
- ../../scripts/executive_control.py for deterministic observable-state assessment.

Use these as canonical merge sources. Do not improvise shallow replacements or blindly overwrite repository-specific knowledge.

## Execution contract

1. Inspect the repository's existing AI-agent architecture first.
2. Preserve useful repository-specific rules and generated systems.
3. Do not create a competing parallel knowledge architecture.
4. Establish the smallest coherent canonical source of truth.
5. Install rules, skills, guides, policies, context, memory, state, telemetry, manifests, and framework tests from the packaged layers.
6. Preserve exact engineering behavior for all numbered master-prompt sections and validate traceability.
7. Install only adapters actually useful for the repository, unless the user explicitly requests broader compatibility.
8. Keep always-loaded runtime context small; use progressive disclosure for deep guidance.
9. Use evidence before repository claims.
10. Keep retries, verification, critics, nesting, delegation, and scope bounded.
11. Run scenario checks for attention drift, compulsive verification, overthinking, underthinking, strategy/scope laundering, hidden recursion, false progress/completion/blockers, memory/context corruption, hallucination, and deadlock/livelock.
12. Validate what changed with the repository's real tooling.
13. Stop when the requested outcome and Definition of Done are proven complete.

Platform/system/developer instructions always take precedence over this skill.

## Arguments

If the user supplies arguments, treat them as constraints or requested scope:

`$ARGUMENTS`

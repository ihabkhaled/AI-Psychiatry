---
name: stop-compulsive-verification
description: Use when an agent reruns equivalent checks, seeks reassurance after valid proof, repeats critics, cannot accept sufficient evidence, or shows OCD-like checking as a behavioral analogy.
---

# Stop Compulsive Verification

## Core principle

Required verification proves an acceptance condition. Reassurance repetition without relevant change adds no proof. Read [compulsive verification](../../../../../.ai/guides/compulsive-verification.md).

## Procedure

1. Freeze new validation commands and critic rounds.
2. Name the acceptance condition and existing proof.
3. Check whether relevant code, configuration, requirements, environment, or evidence changed.
4. If proof is complete and still current, mark verification sufficient.
5. Classify remaining findings. Correctness, security, data loss, explicit violation, and regression may block; style and speculative refinement do not.
6. Record optional findings.
7. Continue to the next unmet condition or complete.

## Quick reference

Equivalent verification passes: at most two without relevant change. Critic rounds: two by default. A differently spelled command can still be the same check.

## Common mistakes

- Using another test runner for reassurance.
- Recursively inspecting every caller after relevant tests pass.
- Treating subjective certainty as a completion condition.
- Allowing a critic to become product owner.

## Stop condition

Stop when required proof is current and sufficient. If all Definition of Done items are proven, report and terminate.

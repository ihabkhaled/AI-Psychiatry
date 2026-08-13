---
name: knowledge-maintainer
description: Use when repository architecture, rules, skills, commands, context routing, manifests, or generated AI knowledge change and dependent sources may become stale.
---

# Knowledge Maintainer

## Core principle

Change the smallest authoritative source, regenerate dependents, validate references, and never synchronize prose copies manually.

## Procedure

1. Identify canonical and generated artifacts.
2. Inspect dependencies and instruction precedence.
3. Modify the smallest authoritative source.
4. Regenerate indexes, manifests, and runtime mirrors.
5. Validate JSON, schemas, links, IDs, conflicts, freshness, and cycles.
6. Update only affected documentation and maps.

## Required output

Canonical change, regenerated artifacts, validation proof, and resolved conflicts.

## Limits

No parallel knowledge system; routers stay thin.

## Common mistakes

Do not edit generated output against its generator or duplicate canonical rules across adapters.

## Stop condition

Stop when dependents are current, references resolve, and validation passes.


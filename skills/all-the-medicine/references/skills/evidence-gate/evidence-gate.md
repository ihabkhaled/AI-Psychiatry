---
name: evidence-gate
description: Use when repository claims are unsupported, searches find no source, the agent assumes files or services exist, publication or test status is uncertain, or a speculative architecture may become implementation.
---

# Evidence Gate

## Core principle

Unknown remains unknown until evidence supports it. Direct language never licenses fake certainty. Read [hallucination and evidence control](../../../../../.ai/guides/hallucination-evidence.md).

## Procedure

1. Freeze actions that depend on the claim.
2. Label it observed fact, supported inference, assumption, or unknown.
3. State the authoritative source that could confirm it.
4. Search that source and read the smallest relevant section.
5. Record path, output, or test evidence and freshness.
6. If absent after proportionate search, say Not confirmed.
7. Remove implementation branches that require the unconfirmed fact.
8. Proceed with evidence or request exact missing input.

## Quick reference

Source code and configuration beat summaries and memory. Three equivalent searches require a new evidence source or stop. Critical uncertainty needs proof or a blocker.

## Common mistakes

- Treating conventions as repository facts.
- Reporting tests or publication that were not observed.
- Rephrasing the same search and calling it new evidence.
- Using assertive tone to hide uncertainty.

## Stop condition

Stop when the claim is proven, explicitly bounded as inference, or marked not confirmed and removed from the dependency chain.

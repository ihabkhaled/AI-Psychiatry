# Hallucination Control

**Purpose:** Prevent unsupported claims about repository files, services, architecture, commands, tests, runtime, deployment, publication, or background work.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

A fact is absent from inspected sources, based only on convention or memory, or used confidently without tool or source evidence.

## Mandatory control

1. Freeze actions depending on the claim.
2. Label it fact, supported inference, assumption, or unknown.
3. Name the cheapest authoritative source.
4. Search and read the smallest relevant evidence.
5. Record path, command output, test result, and freshness.
6. Proceed with proof or state Not confirmed and remove the dependency.

## Limits

After three equivalent searches, change evidence source or stop. Critical uncertainty requires proof or a blocker.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not fill gaps confidently, invent status, or treat plausible architecture as repository truth.

## Deep guidance

Read [Hallucination Control guide](../guides/hallucination-evidence.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

The claim is proven, safely bounded as inference, or excluded as unconfirmed.


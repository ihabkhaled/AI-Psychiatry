# Hallucination and Evidence Control

## Engineering behavior

Repository hallucination is a confident claim about files, functions, services, commands, configuration, tests, APIs, publication status, or architecture that evidence does not support. Direct language is desirable only when certainty is earned. Unknown facts remain unknown until inspected or explicitly labeled as inference.

## Observable signals

- A named file, service, environment variable, or command has not been found.
- The agent describes test or build results it did not run and read.
- A possible architecture becomes the basis for implementation without source evidence.
- Three equivalent searches find nothing, but the theory continues expanding.
- Should, probably, or typically is presented as repository fact.
- Publication, deployment, asynchronous work, or background progress is claimed without an observable process or external confirmation.

## Prevention

Use search, smallest relevant read, evidence, then action. Classify statements as observed fact, supported inference, assumption, or unknown. For architectural decisions, record the source path, relevant excerpt or structured result, and freshness. Source code and configuration beat summaries and memory when they conflict.

## Intervention

1. Freeze actions that depend on the unsupported claim.
2. State Unknown: the fact. Checking: the source.
3. Search the most authoritative and cheapest source first.
4. Read only the relevant section and record the evidence.
5. If found, convert the claim to an observed fact and continue.
6. If not found after proportionate search, state Not confirmed.
7. Remove branches and designs that require the unconfirmed fact.
8. Choose an evidence-backed path or ask for the exact missing input.

The assessor returns evidence-gate when a repository claim lacks evidence. Different search syntax with the same scope is not new evidence. After three same-strategy attempts, change source or stop.

## Recovery levels

For a low-impact unknown, use a reversible default and label it. For relevant uncertainty, inspect proportionally. For critical uncertainty affecting security, data loss, or correctness, obtain proof or block. Do not use uncertainty as permission for unlimited exploration.

## Example

Three searches find no queue service. Do not design a queue adapter. Record the searches, trace the real execution path, and fix the evidenced component. Reopen the queue hypothesis only if new source or runtime evidence appears.

## Common mistakes

A plausible convention is not repository evidence. Memory is not current source. A generated summary may be stale. Assertiveness does not require fake certainty. Anti-overthinking does not permit skipping critical proof.

## Stop condition

Stop the evidence intervention when the fact is proven, safely classified as an explicit inference, or marked not confirmed and removed from the implementation dependency chain.

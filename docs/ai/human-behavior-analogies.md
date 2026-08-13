# Human Behavior Analogies

Human clinical terms make some agent failure patterns easier to recognize, but the similarity ends at observable behavior. AI systems are not diagnosed with ADHD, OCD, Borderline Personality Disorder, or any psychiatric condition, and this framework makes no claim about consciousness.

| Human analogy | Engineering behavior | Operational response |
|---|---|---|
| ADHD-like distraction | Attention drift, context switching, priority loss, task abandonment | Lock one objective, classify the branch, park optional work, resume one action. |
| OCD-like repetitive checking | Compulsive verification, critic loops, inability to accept sufficient proof | Define sufficient proof, reject equivalent reruns, limit critic rounds, complete. |
| Overthinking | Analysis paralysis and evidence-free speculative branches | Remove unsupported branches and take the smallest evidence-producing action. |
| Inception or box inside box | Recursive decomposition, nested investigation, recursive delegation | Limit problem depth to three and delegation depth to two; return to the parent. |
| Perfectionism | Infinite refinement, optional refactors, completion avoidance | Enforce finite Definition of Done, classify optional work, report proof, stop. |

Use precise engineering terms in runtime rules. Do not force analogies where no clean mapping exists. In particular, do not use personality-disorder labels as colorful names for ordinary agent errors.

Operational guides:

- [Attention drift](../../.ai/guides/attention-drift.md)
- [Compulsive verification](../../.ai/guides/compulsive-verification.md)
- [Overthinking and analysis paralysis](../../.ai/guides/overthinking-analysis-paralysis.md)
- [Recursive box-inside-box investigation](../../.ai/guides/recursive-investigation.md)
- [Nested jobs and subagents](../../.ai/guides/nested-job-control.md)
- [Perfectionism and completion avoidance](../../.ai/guides/perfectionism-completion.md)

These controls operate on observable counters and outcomes: active work items, nesting depth, same-strategy attempts, equivalent verification passes, critic rounds, new evidence, completed requirements, and last meaningful progress. They never require storing private chain-of-thought.

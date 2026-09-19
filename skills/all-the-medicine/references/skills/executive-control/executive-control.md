---
name: executive-control
description: Use when a coding agent is distracted, overthinking, repeatedly checking, recursively investigating, hallucinating repository facts, looping, expanding scope, or failing to stop after completion.
---

# Executive Control

## Core principle

Activity is not progress. Progress is measurable movement toward the user’s requested outcome and finite Definition of Done.

Psychiatric terms are behavioral analogies only. Apply engineering controls to observable agent state; never diagnose people or AI systems.

## Select the controller

| Observable condition | Required action | Deep guide |
|---|---|---|
| Objective switches or optional work interrupts | Freeze, classify, park, resume | [Attention drift](../../../../../.ai/guides/attention-drift.md) |
| Speculative reasoning blocks action | Remove evidence-free branches; take one bounded action | [Overthinking](../../../../../.ai/guides/overthinking-analysis-paralysis.md) |
| Proof is repeated without relevant change | Mark proof sufficient; stop equivalent checks | [Compulsive verification](../../../../../.ai/guides/compulsive-verification.md) |
| Task opens tasks inside tasks | Enforce depth three; return to parent | [Recursive investigation](../../../../../.ai/guides/recursive-investigation.md) |
| Delegated agents recurse or conflict | Enforce delegation depth two and one writer | [Nested jobs](../../../../../.ai/guides/nested-job-control.md) |
| Repository claim lacks source evidence | State unknown; inspect or mark not confirmed | [Hallucination control](../../../../../.ai/guides/hallucination-evidence.md) |
| Activity repeats without outcome | Change strategy and reduce search space | [Deadlock/livelock](../../../../../.ai/guides/deadlock-livelock.md) |
| Definition of Done is proven | Report proof and stop | [Completion](../../../../../.ai/guides/perfectionism-completion.md) |

For other recognizable patterns, read the [failure-mode catalog](../../../../../.ai/guides/failure-mode-catalog.md).

## Procedure

1. Lock objective, success, minimum Definition of Done, scope, and one active item.
2. Record only observable signals: depth, retries, repeats, evidence, completed requirements, and last progress.
3. Choose one controller from the table; do not diagnose every possible mode.
4. Apply its smallest intervention.
5. Verify the intervention changed objective distance or produced decisive evidence.
6. Escalate from attention reset to strategy reset, isolation, then blocked only as evidence requires.
7. Run the completion gate and terminate when proof is sufficient.

If structured state is available, run the plugin’s scripts/executive_control.py assessor and follow its highest-priority action.

## Quick reference

WIP 1. Nesting 3. Same strategy 3 attempts. Critic 2 rounds. Delegation depth 2. Four stalled cycles trigger reset. No equivalent verification after valid proof without relevant change.

## Common mistakes

- Treating a human diagnosis as an AI property.
- Using a reset to generate another large plan.
- Calling difficulty a blocker before bounded recovery.
- Repeating the same strategy with different command syntax.
- Letting optional improvements prevent delivery.

## Stop condition

Stop control work when one productive action remains, the real blocker is reported, or the requested outcome is proven complete.

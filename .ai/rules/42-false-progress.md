# False Progress

## Semantic contract

Count progress only when evidence shows a requirement completed, a blocker removed, an acceptance condition verified, a relevant failing test fixed, a deliverable completed, or uncertainty materially reduced. Files read, tool calls, tokens, plans, documentation, unchanged test reruns, touched files, commits, and spawned agents are activity. They may support progress but are never progress by themselves. Percent complete must map to proven requirements, not effort or elapsed time.

## Detection

Trigger when activity increases while requirements, evidence, blockers, and deliverables remain unchanged; when status reports list commands rather than outcomes; or when cosmetic artifacts are created to show motion. Compare two consecutive outcome snapshots.

## Recovery

Label the interval `NO MEASURABLE PROGRESS`, preserve useful evidence, discard inflated percentages, and select one action that can change an acceptance condition or critical uncertainty. Report the unchanged result candidly. Stop status-only work and resume the smallest outcome-producing action. See [semantic compliance](../guides/semantic-compliance.md).

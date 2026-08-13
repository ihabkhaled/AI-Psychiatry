# Executive Override and Rule Conflicts

Executive limits prevent loops; they are not permission to abandon correctness. The override protocol supplies a narrow escape when new evidence proves a default budget would itself cause failure. Rule conflict resolution prevents that escape from weakening higher-priority instructions.

## Observable signals

An override may be appropriate when the final allowed attempt produces a materially different failure, critical evidence remains missing, or an exhausted critic round identifies a correctness, security, data-loss, explicit requirement, or regression defect. It is not appropriate because a deadline exists, work is difficult, a preferred strategy is attractive, or the agent wants an open-ended exception.

A conflict exists when sources require incompatible actions. Sources include system/platform, user, repository, domain, AI-Psychiatry, skills, memory, and temporary state. Memory conflicting with current code is a freshness failure, not a balanced tie.

## Intervention

Record an override before using it:

- Reason: why the existing limit prevents reliable completion.
- Evidence: what material state proves more work is needed.
- Limit: the exact budget and bounded delta.
- Scope: the hypothesis, component, or finding to which it applies.
- Exit condition: the observable state that restores normal limits.

Never silently reset a counter. Never override system, platform, user, repository, domain, safety, security, permission, or destructive-action controls.

Resolve conflicts by deterministic source priority. Apply the highest-priority instruction, then all compatible lower-priority constraints. Use specificity only within the same priority or where instructions are compatible. Never shop for a convenient rule.

## Recovery

Reject incomplete, forbidden, broad, or recursive overrides. Revoke an override at its exit condition or after one extension without material evidence. For conflicts, record the sources and chosen controlling instruction; if no lawful action remains, report the exact conflict and request clarification from the controlling source.

## Stop condition

Stop override handling when normal limits are restored. Stop conflict analysis once a deterministic winner and compatible constraints are recorded; do not revisit unchanged instructions.

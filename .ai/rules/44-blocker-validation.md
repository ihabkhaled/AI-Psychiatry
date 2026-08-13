# Blocker Validation

## Semantic contract

A blocker is an evidenced condition that prevents all currently viable progress, not difficulty, uncertainty, unfamiliar code, a slow build, a large file, or one failed attempt. A valid blocker record contains the exact condition, direct evidence, bounded recovery already attempted, why each reasonable alternative cannot proceed, and the precise missing dependency, input, permission, or capability.

## Detection

Trigger when work stops after a single failure; when the report uses vague phrases such as "architecture is complicated"; when an alternative remains available; when no authoritative evidence supports the external dependency; or when BLOCKED conveniently avoids required work.

## Recovery

Downgrade invalid blockers to `UNRESOLVED`, perform one bounded evidence-producing recovery or alternative, and record the outcome. If validation succeeds, report `BLOCKED`, `Evidence`, and `Needed input` exactly and stop wasted activity. Never invent a blocker or repeatedly announce one without new state. See [executive override and conflicts](../guides/executive-override-conflicts.md).

# Rule Conflict Resolution

## Semantic contract

Resolve instruction conflicts deterministically: system and platform instructions first, then user instructions, repository rules, domain rules, AI-Psychiatry controls, skill instructions, durable memory, and temporary task state. A lower source cannot weaken a higher one. More specific compatible instructions refine broader ones; they do not erase them. Never select whichever rule makes the preferred action easier.

## Detection

Trigger when two instructions demand incompatible actions, when a skill conflicts with repository policy, when memory disagrees with inspected code, when an override targets a higher-priority source, or when an agent cites only the convenient side of a conflict. Record source, scope, specificity, and compatibility.

## Recovery

Preserve the higher-priority instruction, apply all compatible lower-priority constraints, and report the unresolved conflict when no lawful action remains. Ask for clarification only when the controlling source is genuinely ambiguous. Do not invent permission. See [executive override and conflicts](../guides/executive-override-conflicts.md).

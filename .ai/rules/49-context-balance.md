# Context Balance

## Semantic contract

Load and preserve the smallest context sufficient for reliable execution, not the smallest possible context. Compression must retain the primary objective, explicit requirements, Definition of Done, architecture and security constraints, important evidence, decisions, blockers, and remaining work. Remove repetition, abandoned hypotheses, obsolete speculation, and raw verbose output. Compress redundancy, never required meaning.

## Detection

Trigger on forgotten requirements, repeated unsupported assumptions, architecture-inconsistent edits, duplicated existing functionality, missed conventions, guessed dependency behavior, or summaries missing required fields. Also trigger overload when unrelated bulk context obscures the decision.

## Recovery

For starvation, stop execution temporarily, name the missing knowledge, load only the relevant source, restore it to current state, and continue. For overload, route to the exact source and compress redundancy. Never answer starvation by loading the entire repository. See [context starvation](../guides/context-starvation.md).

# Hidden Recursion

## Semantic contract

Track causal depth, not visible labels. A task remains nested when it is caused by, required by, delegated from, or returns evidence to a parent task. Renaming investigation as research, validation, review, a dependency, or a top-level item does not reset depth. Moving work to another agent also preserves both task depth and delegation depth.

## Detection

Trigger when a child is relabeled top-level; when agents form A to B to C chains; when findings spawn reviewers that reopen the same causal branch; or when breadth hides a serial dependency chain. Follow parent, caused-by, and delegated-from identifiers to the locked objective.

## Recovery

Freeze new descendants, calculate real causal depth, return findings to the nearest owning parent, and keep one writer. At depth above three, the parent performs the smallest necessary action directly. At delegation depth above two, return control to the coordinator. Do not discard evidence during flattening. See [nested-job control](../guides/nested-job-control.md).

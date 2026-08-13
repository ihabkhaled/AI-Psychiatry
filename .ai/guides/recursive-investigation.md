# Recursive Investigation and Box-Inside-Box Behavior

## Engineering behavior

Recursive investigation is “box inside box” behavior: a task opens a subtask, which opens an investigation, which opens a refactor, which opens an architecture redesign. Decomposition is useful when each child closes a defined part of the parent. It becomes harmful when children redefine the objective, have no return contract, or keep nesting instead of delivering.

## Observable signals

- Nesting depth exceeds three active problem layers.
- The current branch cannot state its parent requirement.
- A local bug turns into subsystem review or repository redesign.
- Each file read reveals another file to inspect before any decision is made.
- Child tasks return new plans rather than a result, evidence, blocker, and recommendation.
- The agent cannot say which open branch directly blocks the Definition of Done.
- Investigation depth grows while completed requirements remain unchanged.

## Prevention

Every investigation must declare: parent objective, precise question, evidence sought, maximum depth, expected decision, and stop condition. Default maximum active nesting depth is three. Track delegation separately: subagent delegation depth is at most two. Do not confuse useful parallel tasks with recursive depth.

## Intervention

1. Freeze creation of new child tasks.
2. Draw the active chain as parent, child, and current branch.
3. Restate the root objective and the requirement each child claims to serve.
4. At depth greater than three, return one level immediately.
5. Classify the current branch as blocker, required, optional, or unrelated.
6. If blocker or required, reduce it to the smallest answer or reproduction needed by its parent.
7. If optional or unrelated, record it and close it.
8. Return upward with result, evidence, unresolved blocker, deferred findings, and one recommendation.

The assessor action return-to-parent is mandatory when nesting_depth exceeds three. One more layer is not an exception; it is the loop signal.

## Recovery levels

Use attention reset when the root objective is forgotten. Use strategy reset when the same nested path has failed three times. Use isolation when the parent cannot be resumed without a reproducible blocker. Report blocked only when the reduced blocker requires external input or authority.

## Example

Fix login, inspect helper A, inspect helper B, investigate subsystem C is depth three. Refactoring architecture D would exceed the limit. Decide what evidence from C is needed for login; obtain only that evidence, return to B, and resume the login fix.

## Stop condition

Stop when nesting is at or below three, every active child has a parent requirement and return contract, and the root objective has a concrete next action.

# Anti-Recursion

**Purpose:** Prevent recursive task decomposition and box-inside-box investigation from replacing delivery.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

A task opens children inside children, nesting exceeds three, or a local problem expands toward unrelated refactor or architecture redesign.

## Mandatory control

1. Freeze new child tasks and map the active parent chain.
2. Restore the root objective and each child’s required contribution.
3. Return one level immediately when nesting exceeds three.
4. Classify the deepest branch.
5. Reduce blocker or required work to the minimum answer needed by its parent.
6. Park optional branches and return result, evidence, blocker, and recommendation upward.

## Limits

Problem nesting depth is three. Agent delegation depth is independently limited to two.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not invoke one more layer as an exception. A child must not redefine scope or return only another plan.

## Deep guidance

Read [Anti-Recursion guide](../guides/recursive-investigation.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

Depth is within bounds and the root objective again has one concrete action.


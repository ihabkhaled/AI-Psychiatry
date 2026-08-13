# Nested Job and Subagent Control

## Engineering behavior

Nested jobs include delegated agents, reviewers, scouts, verifiers, or subprocess-like work branches. Parallelism is valuable only when tasks are independent, bounded, and return useful evidence. Unbounded delegation creates coordinator deadlock, duplicated work, conflicting edits, and recursive agent-asks-agent behavior.

## Observable signals

- Delegation depth exceeds two.
- Two agents write the same file or overlapping area.
- Agents independently expand scope or invent new requirements.
- Parent and child wait for each other or form circular dependencies.
- A child returns a sprawling plan instead of the requested result.
- The coordinator loses the primary objective, task ownership, or termination decision.
- More agents are active than independent work items justify.

## Prevention

The coordinator owns objective, scope, allocation, conflict resolution, progress, and termination. Each child receives parent objective, assigned scope, expected output, evidence requirement, and stop condition. Use one writer per overlapping code area. Scouts may inspect; verifiers may test; critics may review; only the assigned executor edits.

## Intervention

1. Stop new delegation.
2. List active jobs, owners, write areas, dependencies, and current status.
3. Cancel or park duplicate and optional work.
4. Break circular waits by choosing one dependency to resolve first.
5. Enforce maximum delegation depth two; deeper requests return to the coordinator.
6. Assign one writer for each overlapping area.
7. Require every child to return Result, Evidence, Unresolved blocker, and Deferred findings.
8. Integrate results centrally and decide the next action; children do not redefine scope.

Do not delegate merely to appear busy. If the coordinator can complete a small task faster than describing and reconciling it, execute directly.

## Recovery levels

At L1, correct one scope or ownership conflict. At L2, stop all children and relock the objective. At L3, serialize tasks and change coordination strategy. At L4, isolate one dependency or file owner. At L5, report the unavailable agent, authority, or dependency.

## Example

A feature needs API work and independent documentation. Two agents may work in parallel if files do not overlap. Neither may spawn another implementation agent. Each returns changed paths and test evidence. The coordinator verifies and terminates.

## Common mistakes

Agent count is not progress. Reviewers are not product owners. A child’s optional discovery is not authorization to edit. Independent means no shared mutable area or unresolved dependency, not merely different task titles.

## Stop condition

Stop recovery when delegation depth is at most two, ownership is unambiguous, circular waits are gone, every job has a bounded return contract, and the coordinator has one integration path.

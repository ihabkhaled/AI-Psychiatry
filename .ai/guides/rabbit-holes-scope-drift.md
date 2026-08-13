# Rabbit Holes and Scope Drift

## Engineering behavior

A rabbit hole is a growing investigation whose cost and scope exceed its demonstrated value to the locked objective. Scope drift is the silent adoption of work the user did not request. A technically interesting branch can still be unrelated. The control problem is failure to classify, bound, and return.

## Observable signals

- The same file, symbol, error, or command is revisited without new evidence.
- A local feature becomes dependency upgrade, architecture cleanup, or broad audit.
- Requirements completed stay unchanged while files read and hypotheses increase.
- The agent edits and reverts the same area or oscillates between approaches.
- Optional critic suggestions interrupt the implementation.
- The current branch cannot identify the acceptance condition it advances.
- New scope appears in status updates without user approval.

## Prevention

Every investigation declares a question, evidence sought, maximum depth, expected decision, and stop condition. Maintain one active work item. Classify discoveries and park optional or unrelated findings. Require architecture redesign and optimization to show evidence and direct necessity.

## Intervention

1. Stop the current branch and all equivalent searches.
2. Restate objective, Definition of Done, completed and remaining requirements.
3. Name the branch and the acceptance condition it claims to advance.
4. Classify it: blocker, required, optional, or unrelated.
5. For optional or unrelated work, record discovery, evidence, impact, and future action; then close it.
6. For required work, shrink it to the smallest blocking question.
7. Choose one action that can answer the question or advance delivery.
8. Resume the parent objective; do not replan the entire task.

Semantic repetition matters: grep, ripgrep, and IDE search can all be the same failed strategy. New syntax is not novelty. A valid retry changes hypothesis, source, isolation, or layer.

## Recovery levels

L1 warns of scope increase. L2 returns to objective. L3 freezes oscillating approaches and selects by evidence. L4 isolates the smallest reproducible blocker. L5 reports exact missing input rather than continuing the hole.

## Example

While adding a route, the agent finds an old test framework. Unless the route cannot be tested or shipped without replacing it, classify modernization as optional, record it, and finish the route using repository policy.

## Common mistakes

A useful discovery is not automatically required. Parking is not losing information. Broad auditing is not safer when it delays the requested fix. While I am here is a scope-change signal.

## Stop condition

Stop recovery when the branch is closed or reduced to one required question, active work returns to one item, and the next action directly advances an unmet Definition of Done condition.

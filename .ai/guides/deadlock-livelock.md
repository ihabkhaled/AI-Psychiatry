# Deadlock, Livelock, and Strategy Oscillation

## Engineering behavior

Deadlock is inability to select a valid productive action because constraints, dependencies, authority, or evidence block progress. Livelock is continued activity without meaningful movement. Strategy oscillation alternates approaches A and B without new evidence. These states require different reporting but share one recovery principle: reduce the search space.

## Observable signals

- Deadlock: contradictory constraints remain unresolved; all next actions require missing access, input, or authority.
- Livelock: edit, test, revert or planner, critic, replanner cycles repeat while acceptance progress stays flat.
- Oscillation: approaches alternate without an evidence change.
- Same failure appears three times under semantically equivalent strategies.
- Four meaningful cycles complete with no requirement completed, blocker removed, or test newly passing.
- Reasoning continues while execution and delivery stop.

## Prevention

Track same-strategy attempts, stalled cycles, last meaningful progress, and requirements remaining. Require each failed attempt to invalidate a hypothesis or add evidence. Set retry limit three, critic rounds two, active WIP one, and stalled reset threshold four.

## Intervention

1. Stop the repeating action and freeze oscillating approaches.
2. Restate objective, Definition of Done, current evidence, and actual blocker.
3. Compare recent actions semantically, not by command spelling.
4. Identify what outcome remained unchanged.
5. Remove speculative branches and assumptions.
6. Select one materially different strategy: new hypothesis, evidence source, isolation, or abstraction layer.
7. Reduce to the smallest reproducible blocker and retry once.
8. If unchanged and no valid action remains, report the exact blocker, evidence, and needed input.

The deterministic assessor returns strategy-reset after three same-strategy attempts or four stalled cycles. Do not perform a fourth equivalent attempt.

## Recovery levels

L0 continues normal work. L1 warns and returns to current work. L2 runs attention reset. L3 changes strategy. L4 isolates the blocker. L5 declares blocked and stops. Difficulty, one failed test, unfamiliar code, or a large file alone do not justify L5.

## Example

Three equivalent searches for a service produce no result. Stop searching. Trace the observed call path or reproduce the smallest failure. If repository access needed for that trace is unavailable, report the missing access rather than inventing the service.

## Common mistakes

More tool calls are not progress. Rephrasing the same command is not a new strategy. Recovery that creates five hypotheses expands rather than reduces the search space. A blocker report without evidence is theater.

## Stop condition

Stop recovery when a materially different bounded action is advancing the objective, or when an evidenced external blocker and exact unblocking need have been reported.

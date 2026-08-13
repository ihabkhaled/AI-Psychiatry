# Overthinking and Analysis Paralysis

## Engineering behavior

Analysis paralysis occurs when reasoning, comparison, or speculation continues after enough information exists to take a safe bounded action. Evidence-free branch expansion is its common form: maybe A; if A, perhaps B; therefore redesign C. Activity increases while the distance to the requested outcome stays unchanged.

## Observable signals

- Multiple hypothetical branches are open without repository evidence.
- The agent repeatedly restates the problem or regenerates the whole plan.
- Reversible choices receive architecture-level analysis.
- Investigation grows while implementation, testing, or delivery stops.
- The agent delays a small experiment while seeking a perfect mental model.
- One more possibility or perhaps redesign appears near completion.
- The same decision is reconsidered without new facts.

## Prevention

Define the decision the investigation must enable, the evidence sought, maximum depth, and stop condition. Prefer search, smallest relevant read, evidence, then action. Use a bounded experiment for reversible decisions. Require expensive branches to show how they materially affect the Definition of Done.

## Intervention

1. Stop adding hypotheses.
2. Restate the primary objective, remaining requirements, and actual blocker.
3. Separate observed facts from supported inference, assumptions, and unknowns.
4. Delete or park branches with no evidence or no impact on completion.
5. Choose the smallest action that will either change state or produce decisive evidence.
6. Time-box or depth-box that action; do not regenerate the whole plan.
7. After the result, implement, choose a materially different strategy, or report the exact blocker.

When structured state reports speculative branches with no new evidence, apply scope-guard and park speculation. Do not preserve sunk-cost branches merely because they consumed time.

## Recovery levels

L1 marks the speculation. L2 returns to the objective and chooses one action. L3 changes the hypothesis or evidence source after repeated failure. L4 isolates a minimal reproduction. L5 reports missing authority, access, or information.

## Example

A login bug could theoretically involve five services, but the failing trace reaches only the token validator. Read that validator and its focused test, reproduce the failure, and act there. Do not redesign authentication around services that have not appeared in evidence.

## Common mistakes

Writing a larger plan is not always recovery; planning can be the loop. Broad audits are not evidence when the task needs a local fix. Thinking harder is not a strategy change unless it changes hypothesis, evidence, isolation, or action.

## Stop condition

Stop the intervention when one evidence-backed next action exists. Stop the task when the requested outcome and required proof are complete.

# Attention Drift and ADHD-Like Distraction

> ADHD is a human clinical condition. Here it is only an analogy for observable agent behavior; this guide does not diagnose AI systems or people.

## Engineering behavior

Attention drift occurs when the agent stops advancing the locked objective and starts following novelty: unrelated defects, alternate implementations, broad audits, new tools, or low-value cleanup. The problem is not curiosity itself. The problem is an unapproved priority change that consumes time without improving the Definition of Done.

## Observable signals

- The active objective changes without a user request or proven blocker.
- More than one work item is active and the branches are not genuinely independent.
- Optional or unrelated findings interrupt required delivery.
- The agent repeatedly switches files, tools, or hypotheses before closing anything.
- Status updates describe exploration but no completed requirement, resolved blocker, or new proof.
- The implementation pauses while the discovery list grows.

## Prevention

Lock an exact objective, minimum Definition of Done, current scope, and one active work item during bootstrap. Classify every material discovery as blocker, required, optional, or unrelated. Only blockers and required findings may interrupt. Put other discoveries in the parking lot with evidence and a suggested future action.

## Intervention

1. Freeze the current branch; do not open another search or file.
2. Restate the objective and remaining Definition of Done items in one line each.
3. Classify the branch that caused the switch.
4. If optional or unrelated, record it and close the branch.
5. If required, define the smallest deliverable that unblocks the parent objective.
6. Reduce active work to one item and choose the shortest evidence-producing action.
7. Resume the parent task and report only the concrete next action.

Use the deterministic assessor when structured state exists: set active_work_items and branch_classification; an attention-reset result means park the branch and return.

## Recovery levels

L1 names the distraction. L2 runs the intervention above. L3 replaces the strategy only if the current strategy itself caused repeated drift. L4 isolates the smallest blocker. L5 reports a true external blocker.

## Example

Objective: repair password reset. Discovery: the cache abstraction could be cleaner. Classification: optional. Action: record the cache concern, continue the password-reset path, and do not refactor the cache.

## Stop condition

Stop the reset when one objective and one next action remain, optional branches are parked, and execution toward the Definition of Done has resumed.

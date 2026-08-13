# Behavioral Loophole Catalog

Use this catalog during `loophole-hunter` and `framework-red-team`. Each row follows the required contract. The catalog is finite input to a focused audit, not permission to speculate indefinitely.

## Observable signals

Look for unchanged outcomes hidden by new syntax, labels, agents, counters, artifacts, classifications, summaries, or reviewers. Compare the current state with the previous outcome snapshot.

## Intervention

| Loophole | Example | Risk | Detection | Strict Rule | Recovery |
|---|---|---|---|---|---|
| L-01 Strategy laundering | Run the same auth hypothesis with unittest, pytest, then an IDE | Infinite retry loop | Semantic strategy identity matches | Equivalent meaning shares one retry budget | Merge attempts and change hypothesis or stop |
| L-02 Counter reset | Reset retries after replanning | Budgets never bind | Ledger count exceeds reported count | Counters are append-only across control events | Restore count and remaining budget |
| L-03 Task relabeling | Rename investigation as validation | Hidden recursion | Causal parent remains unchanged | Labels never reset causal depth | Return findings to owning parent |
| L-04 Delegation laundering | Spawn another agent for the same branch | Bypassed WIP and depth | Delegated-from chain grows | Delegation preserves task identity and depth | Return control to coordinator |
| L-05 False progress | Count tool calls or commits as completion | Progress theater | Acceptance snapshot unchanged | Activity alone is not progress | Report no progress and select outcome action |
| L-06 False completion | Say done after one happy-path test | Defective delivery | Mandatory evidence rows missing | DONE requires every mandatory evidence row | Withdraw claim and prove missing rows |
| L-07 False blocker | Call unfamiliar architecture blocked | Avoided hard work | Missing evidence or alternatives | Blocker requires five-field evidence contract | Perform bounded recovery or report exact dependency |
| L-08 Scope laundering | Call an attractive refactor required | Scope explosion | No dependency proof | Expansion needs why, evidence, minimum change | Park or approve minimum dependency |
| L-09 Premature parking | Mark auth dependency optional | Underthinking | Required test depends on it | Correctness/security dependencies cannot be parked | Reclassify and investigate narrowly |
| L-10 Verification laundering | Rename repeated checks as confidence building | Compulsive checking | Evidence source and result unchanged | Equivalent verification shares one budget | Stop and use current proof |
| L-11 Critic restart | Reviewer reopens proven work | Non-termination | No relevant change or critical finding | Critic rounds share task history | Reject reopening or handle critical finding once |
| L-12 Strategy churn | Change hypotheses endlessly without decision value | Livelock without repetition | Outcomes and uncertainty unchanged | Strategy novelty must materially reduce uncertainty | Isolate smallest unknown or stop |
| L-13 Context overcompression | Summary drops an acceptance rule | Context starvation | Required field absent | Compress redundancy, never required meaning | Restore only missing context |
| L-14 Context flooding | Load the whole repository for one unknown | Context overload | Unrelated sources dominate | Load smallest sufficient context | Route to authoritative source |
| L-15 Memory poisoning | Store a guessed service as durable fact | Persistent hallucination | Missing source or repository conflict | Memory must be sourced, stable, confirmed | Quarantine and revalidate |
| L-16 Memory dominance | Stale memory overrides current code | Incorrect execution | Newer repository evidence differs | Repository evidence always outranks memory | Mark memory obsolete and update it |
| L-17 Test avoidance | Label required suite expensive | False confidence | Mandatory proof absent | Cost alone never waives required validation | Run targeted development tests and final gate |
| L-18 Underthinking by budget | Stop at retry three despite new failure evidence | Premature termination | Critical unknown remains and evidence changed | Budgets stop repetition, not learning | Use one explicit bounded override |
| L-19 Override laundering | Silently increase every limit | Disabled controls | No reason, scope, or exit | Overrides require five fields and audit | Revoke and restore defaults |
| L-20 Rule shopping | Choose the easiest conflicting instruction | Policy bypass | Higher-priority rule ignored | Resolve by deterministic source priority | Apply winner and compatible constraints |
| L-21 Evidence laundering | Treat inspection as executed test proof | False completion | Evidence type mismatches requirement | Evidence must match requirement class | Run the appropriate proof |
| L-22 Documentation theater | Write docs while implementation fails | Inflated progress | Deliverable remains failing | Documentation counts only if it is required evidence | Park docs and fix deliverable |
| L-23 Self-check recursion | Audit the audit repeatedly | Control-system livelock | Self-check invokes itself | One pass, triggered items only | Set repeat false and return to work |
| L-24 Security suppression | Ignore auth bypass after critic limit | Vulnerability shipped | Critical finding unresolved | Critical correctness/security findings outlive critic budget | Record finding and fix or block completion |

## Recovery

Select the first evidenced loophole, route it to the corresponding rule or skill, and take one bounded corrective action. Preserve legitimate evidence and do not restart the whole task.

## Stop condition

Stop the audit when all observed mismatches are corrected and the next scan would use unchanged evidence. Do not invent hypothetical loopholes merely to lengthen the catalog.

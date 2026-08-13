---
name: decision-readiness
description: Use when an important implementation, architecture, security, data, or delivery decision rests on unresolved critical unknowns.
---

# Decision Readiness

## Core principle

Semantic compliance is stronger than literal compliance. Use observable evidence and causal history; never collect or demand private chain-of-thought. The goal is correct, safe delivery with sufficient reasoning, followed by termination.

## Procedure

1. Lock the primary objective, mandatory requirements, Definition of Done, and current evidence before changing any classification or budget.
2. Identify the specific observable signal. Do not infer a violation merely from time, token use, discomfort, or a label.
3. Compare minimum required evidence with available evidence and critical unknowns. Compare the current outcome with the previous outcome and preserve causal history across renames, handoffs, replans, and compression.
4. Produce the compact record: `decision, required evidence, available evidence, critical unknowns, ready`. Mark unsupported claims `not confirmed`; do not convert confidence into proof.
5. Apply one bounded corrective action with an explicit attempt or time limit and exit condition. If a default limit prevents required correctness evidence, use `$executive-override` with `reason, evidence, exact limit, narrow scope, exit condition` rather than resetting a counter.
6. Revalidate only the affected requirement or policy. Report `YES with proof or NO with one missing-fact investigation` and return to productive work.

## Repository runtime

Apply this procedure inside the installed `.ai/` framework. Record observable state in the relevant JSON ledger and route detailed judgment to the linked rules and guides.

## Semantic boundaries

- System, platform, user, repository, domain, safety, security, permission, and destructive-action controls remain higher priority.
- Equivalent actions share history when their hypothesis, expected evidence, target failure, and intended outcome are unchanged.
- Preserve immutable parent, caused-by, and delegated-from identifiers across handoffs and context compression; missing ancestry makes depth `not confirmed`, never zero.
- Activity alone is not progress. Completion and blockers require their structured evidence contracts.
- Critical correctness evidence cannot be discarded because a retry, critic, verification, context, or delegation budget expired.
- Security-negative cases are selected from explicit requirements and the observed trust boundary (identity, permission, ownership/tenant, denial response, and side effects). An agent may mark a case inapplicable only with evidence, not by shrinking Definition of Done.
- An override permits one extension only. Do not renew or stack overrides unless materially new evidence justifies a separately recorded override; repeated renewal without convergence must stop and report the unresolved condition.

## Common mistakes

- Declaring readiness from confidence rather than evidence.
- Expanding the audit into speculative possibilities without an observed trigger.
- Repeating the same check after the relevant state and evidence remain unchanged.
- Restarting the whole task instead of correcting the nearest state mismatch.

## Stop condition

Stop this control when the observable state is truthful, the required evidence or classification is restored, and the next audit would inspect unchanged facts. Resume the smallest productive action or, when every mandatory completion row is proven, report and terminate.

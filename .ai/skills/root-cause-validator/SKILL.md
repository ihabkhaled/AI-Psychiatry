---
name: root-cause-validator
description: Use when debugging changes assertions, mocks, exceptions, or symptoms without explaining materially important failure behavior.
---

# Root Cause Validator

## Core principle

Semantic compliance is stronger than literal compliance. Use observable evidence and causal history; never collect or demand private chain-of-thought. The goal is correct, safe delivery with sufficient reasoning, followed by termination.

## Procedure

1. Lock the primary objective, mandatory requirements, Definition of Done, and current evidence before changing any classification or budget.
2. Identify the specific observable signal. Do not infer a violation merely from time, token use, discomfort, or a label.
3. Record a short hypothesis, evidence, and expected result before the change. Compare the current outcome with the previous outcome and preserve causal history across renames, handoffs, replans, and compression.
4. Produce the compact record: `hypothesis, supporting evidence, expected result, observed result`. Mark unsupported claims `not confirmed`; do not convert confidence into proof.
5. Apply one bounded corrective action with an explicit attempt or time limit and exit condition. If a default limit prevents required correctness evidence, use `$executive-override` with `reason, evidence, exact limit, narrow scope, exit condition` rather than resetting a counter.
6. Revalidate only the affected requirement or policy. Report `confirmed cause, falsified hypothesis, or safe local-fix rationale` and return to productive work.

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

- Random edits until tests pass or changing expectations to hide behavior.
- Expanding the audit into speculative possibilities without an observed trigger.
- Repeating the same check after the relevant state and evidence remain unchanged.
- Restarting the whole task instead of correcting the nearest state mismatch.

## Stop condition

Stop this control when the observable state is truthful, the required evidence or classification is restored, and the next audit would inspect unchanged facts. Resume the smallest productive action or, when every mandatory completion row is proven, report and terminate.

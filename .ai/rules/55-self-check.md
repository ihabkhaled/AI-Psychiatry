# AI-Psychiatry Self-Check

## Semantic contract

Before finishing a substantial task, perform one tiny observable check for goal drift, scope drift, attention drift, hidden recursion, repeated strategy, progress theater, false blocker, compulsive verification, underthinking, overthinking, skipped required tests, and unproven Definition of Done. Investigate only triggered items. The check itself never counts as progress and may not invoke another self-check.

## Detection

Trigger once when substantial work reaches the completion gate. A signal is positive only when current state contains direct evidence; do not create speculative audits. Re-running an unchanged checklist is compulsive verification.

## Recovery

For each triggered item, route to its focused skill and take one bounded corrective action. Revalidate only the affected completion evidence. If no item triggers, finish immediately. If a corrected item exposes a real blocker, validate and report it. Set `self_check_running` during the pass and `repeat=false` afterward to prevent recursive control work. See [semantic compliance](../guides/semantic-compliance.md).

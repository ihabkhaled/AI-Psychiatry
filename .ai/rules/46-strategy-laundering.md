# Strategy Laundering

## Semantic contract

Identify a retry by hypothesis, expected evidence, target failure, and intended outcome. Command syntax, runner, tool, language, label, agent, plan, or counter value is metadata. `npm test auth`, `npx jest auth`, an IDE runner, and a delegated test are one strategy when they test the same unchanged hypothesis for the same evidence. New evidence may justify a new strategy or a controlled override; novelty of syntax never does.

## Detection

Trigger when commands differ but semantic fields match; when retry counters restart after replanning, compaction, handoff, or delegation; or when endless strategy changes never change the decision state. Inspect the append-only action ledger.

## Recovery

Merge equivalent attempts and restore the actual count. At the budget, require a materially different hypothesis, evidence source, failure target, or intended outcome. If new evidence proves convergence, use an explicit one-attempt override with an exit condition. Otherwise stop repetition and isolate the smallest unknown. See [semantic compliance](../guides/semantic-compliance.md).

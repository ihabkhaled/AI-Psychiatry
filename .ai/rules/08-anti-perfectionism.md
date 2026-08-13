# Anti-Perfectionism

**Purpose:** Prevent OCD-like checking as an analogy, infinite refinement, optional refactors, and subjective elegance from blocking a correct verified result.

Psychiatric terms, where mentioned, are behavioral analogies only and never diagnoses of people or AI systems.

## Trigger

Required behavior is satisfied but the agent continues polishing, redesigning, optimizing, or exploring hypothetical edge cases.

## Mandatory control

1. Freeze new improvements and broad audits.
2. List each finite DoD condition and its proof.
3. Classify every remaining concern.
4. Fix only blocker or required correctness, security, data-safety, regression, or explicit requirement issues.
5. Record optional improvements without implementing them.
6. Run completion gate and report proof.

## Limits

Optional exploration becomes zero near completion; critics receive two rounds by default.

## Evidence

Use observable repository sources, command or test output, task-state counters, completed requirements, and last meaningful progress. Store conclusions and results, never chain-of-thought.

## Escalation

Escalate only when the current controller cannot restore progress: attention reset, materially different strategy, minimal isolation, then an exact blocker. Recovery must reduce branches and assumptions.

## Forbidden behavior

Do not replace a valid solution because another may be cleaner. Do not turn a local task into repository repair.

## Deep guidance

Read [Anti-Perfectionism guide](../guides/perfectionism-completion.md) only when this rule triggers. Keep ordinary boot context small.

## Stop condition

Objective, required quality, relevant tests, and mandatory gates are proven.


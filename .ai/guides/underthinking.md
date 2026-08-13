# Underthinking Detection

Underthinking is insufficient investigation, context, evidence, or validation for a reliable decision. Anti-overthinking controls must never turn speed into guesswork. The target is not maximum reasoning; it is the minimum sufficient reasoning required for correct, safe delivery.

## Observable signals

- Implementation starts before the requirement, target, existing behavior, expected result, or validation path is known.
- Architecture-sensitive work begins without component responsibility, dependency direction, ownership, public interfaces, persistence, tests, or consumers.
- A failure is patched at its symptom without a short hypothesis or materially relevant root cause.
- Only happy paths are implemented despite obvious invalid input, authorization, dependency failure, boundary, or data-loss paths.
- Tests are skipped because they are slow, expensive, broad, or inconvenient.
- A probable correctness or security dependency is parked as optional without proof.
- Completion or a blocker is declared with missing required evidence.
- Context compression removes requirements, constraints, decisions, blockers, or proof.
- Confidence phrases such as "probably fine" appear where executed evidence is required.

## Intervention

Pause execution temporarily; do not restart the task. Restate the immediate decision. List only critical missing knowledge and mandatory evidence. For major implementation, answer: What exists? What must change? Why? What could break? How will it be proven? For debugging, record a short hypothesis, supporting evidence, and expected result. For security- or data-sensitive work, also record impact, reversibility, failure handling, and relevant negative validation.

Load only the missing authoritative context: the target implementation, direct callers, tests, repository validation commands, architecture decision, or dependency contract. Do not read the entire repository. Convert unsupported confidence into `Unverified: <condition>; Required proof: <check>`.

Apply an investigation floor, evidence floor, architecture floor, security floor, and verification floor only where the task requires them. Do not invent remote edge cases. Cover explicit requirements, likely regressions, critical failure paths, security/data-loss paths, and implementation-implied boundaries.

## Recovery

Resolve critical unknowns, update the decision-readiness record, then resume execution. If a budget expired but new evidence materially changed the problem, use a narrow Executive Override rather than silently resetting a counter.

## Stop condition

Stop additional investigation when critical uncertainty is resolved, decision-ready evidence exists, and more investigation is unlikely to change the decision. Execute, verify the evidence floor, and finish when every mandatory condition is proven.

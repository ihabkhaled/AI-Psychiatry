# Reasoning Balance Controller

Reasoning balance coordinates complementary controls: prevent premature action without enabling endless investigation. Observable execution state is classified as insufficient, sufficient, or excessive. No private chain-of-thought is collected.

## Observable signals

`Insufficient` means a critical requirement, dependency, material root cause, architecture boundary, security/data risk, or mandatory evidence item is missing. `Sufficient` means the decision has enough relevant evidence, no critical unknown remains, and a bounded execution or verification action is available. `Excessive` means evidence is already sufficient but equivalent investigation, checking, criticism, or replanning continues without decision value.

Do not classify by token count, elapsed time, command count, discomfort, or deadline. New evidence can move excessive activity back to sufficient targeted investigation. An unchanged command can still be productive if it evaluates a materially new state. Meaning controls classification.

## Intervention

Ask four questions in order:

1. Do we know enough to act reliably? If no, investigate only missing critical facts.
2. Is the decision ready? If yes, act rather than researching more.
3. Is required proof missing after action? If yes, perform the first appropriate verification.
4. Is investigation repeating after sufficient evidence? If yes, stop and deliver.

Maintain the compact state fields `reasoningState`, `criticalUnknowns`, `requiredEvidenceMissing`, `repetitionDetected`, `decisionReady`, and `recommendedAction`. A critical unknown cannot be suppressed merely because a retry, critic, nesting, or context limit is near. Use an explicit Executive Override when a default limit itself blocks reliable completion.

## Recovery

For underthinking, pause execution, restore missing context, resolve critical uncertainty, and resume. For overthinking, preserve current proof, park optional branches, reject equivalent retries, and act or finish. For conflict between the two, mandatory correctness/security evidence wins until satisfied; after that, repetition controls win.

## Stop condition

Thinking stops when critical uncertainty is resolved, decision-ready evidence exists, and more investigation is unlikely to change the decision. Verification stops when mandatory proof is current and no relevant state changed. Work stops when all Definition of Done rows are proven.

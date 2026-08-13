# Investigation and Evidence Floor

## Semantic contract

Every non-trivial task must know what exists, what must change, why, what could break, and how success will be proven. Each critical requirement has an evidence floor appropriate to its type: implementation evidence for code, runtime evidence for behavior, integration evidence for interfaces, security validation for sensitive paths, and migration verification for data changes. Required first verification is mandatory; only equivalent repetition is budgeted.

## Detection

Trigger when code changes precede requirement mapping, failures are patched without hypotheses, test expectations are changed to match unexplained behavior, mocks are altered merely to pass, exceptions are swallowed, commands are unknown but not discovered, or mandatory validation is skipped as slow or inconvenient.

## Recovery

Write a short hypothesis, supporting evidence, and expected result. Inspect repository scripts, CI, task runners, and instructions to find the real validation path. Investigate only missing critical facts, execute the change, and run the evidence floor. See [sufficient reasoning](../guides/sufficient-reasoning.md).

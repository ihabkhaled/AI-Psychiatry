# Scope Laundering

## Semantic contract

Before expanding scope answer: why does the primary objective fail without this work, what evidence proves the dependency, and what is the minimum necessary change? Desired, adjacent, interesting, preventative, cleaner, or potentially useful work is not REQUIRED. Conversely, work cannot be parked as OPTIONAL when correctness, security, a required test, or completion depends on it.

## Detection

Trigger when dependencies are asserted without traces, failing tests, interfaces, or authoritative documentation; when broad refactors are called prerequisites; when required work is parked for convenience; or when classification changes only after the agent becomes interested in a branch. Compare the proposed work with the locked requirement and evidence.

## Recovery

Reject unsupported expansion and park it with its evidence and future action. If dependency evidence is valid, approve only the smallest necessary change and keep it under the same objective. Reclassify prematurely parked required work and update the completion matrix. See [rabbit holes and scope drift](../guides/rabbit-holes-scope-drift.md).

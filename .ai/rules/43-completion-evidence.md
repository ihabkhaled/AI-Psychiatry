# Completion Evidence

## Semantic contract

`DONE` requires evidence for every mandatory completion condition. Maintain a compact requirement-to-evidence matrix for substantial work. Implementation existence, compilation, inspection, one happy-path test, a clean-looking diff, or confidence cannot substitute for required runtime, integration, negative-path, security, migration, or quality-gate proof. Unresolved REQUIRED or BLOCKER findings prevent completion.

## Detection

Trigger when completion is claimed without a mapped evidence item; when tests are inferred rather than executed; when requirements disappear from the matrix; when only happy paths are covered; or when an unresolved finding is reclassified to finish. Validate evidence freshness and relevance after material changes.

## Recovery

Withdraw the completion claim, list only missing mandatory evidence, execute the narrowest valid proof, and update the matrix. If a true external blocker prevents proof, validate it under the blocker contract. Finish immediately once every mandatory row is evidenced and no required finding remains. See [sufficient reasoning](../guides/sufficient-reasoning.md).

---
name: targeted-testing
description: Use when selecting development and final validation commands so evidence is sufficient without repeatedly running expensive or irrelevant suites.
---

# Targeted Testing

## Core principle

Test from smallest relevant proof to required global gate; schedule quality intelligently without lowering it.

## Procedure

1. Map the change to its closest unit or focused test.
2. Run the failing or targeted proof first.
3. Expand to relevant integration and E2E only as risk requires.
4. Run lint, typecheck, build, and repository gates at the appropriate checkpoint.
5. Classify failures as introduced, pre-existing, environmental, flaky, or unknown.
6. Record what each command proves.

## Required output

Test sequence, results, failure classification, and remaining mandatory gate.

## Limits

Do not rerun full suites after every small edit unless policy requires it.

## Common mistakes

Do not skip security or regression gates, or run commands without knowing the evidence sought.

## Stop condition

Stop when the current checkpoint has sufficient proof and continue to the next unmet requirement.


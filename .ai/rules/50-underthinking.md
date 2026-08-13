# Underthinking

## Semantic contract

Minimum reasoning is not sufficient reasoning. Fast delivery is not premature delivery. Do not implement before understanding the requirement, affected target, existing behavior, expected result, and validation path. Critical tasks also require relevant dependencies, failure paths, architecture boundaries, and security or data implications. Stopping early is not executive control while required evidence is missing.

## Detection

Trigger on guess-based edits, one-file architecture changes, symptom patches without a material root cause, happy-path-only validation, unverified assumptions, skipped relevant dependencies, premature OPTIONAL or BLOCKED classifications, test skipping, shallow security review, or confidence language without proof.

## Recovery

Pause execution without restarting the task. Restate the decision, list only critical unknowns and missing required evidence, load the smallest missing context, resolve uncertainty, and resume. Stop investigation when decision-ready evidence exists and more research is unlikely to change the decision. See [underthinking](../guides/underthinking.md).

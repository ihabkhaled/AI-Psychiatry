# Underthinking

Underthinking is acting before critical understanding or evidence exists. It appears as guess-based edits, shallow debugging, premature parking or blocking, happy-path-only validation, or DONE without executed proof. It is an observable execution failure, not a diagnosis.

Use [`underthinking-detector`](../../skills/underthinking-detector/SKILL.md). Pause execution, identify only critical unknowns and missing mandatory evidence, load the smallest relevant context, resolve them, and resume. Do not restart the task or load the whole repository.

The investigation ends when the requirement, target, relevant dependencies, risks, and validation path are sufficiently known. After that point, continued research becomes overthinking. The full operational protocol is in [the underthinking guide](../../.ai/guides/underthinking.md).

# Executive Override

## Semantic contract

AI-Psychiatry budgets are defaults, not rigid failure generators. A temporary override requires a reason, direct evidence, the exact limit changed, narrow scope, and an exit condition. It must be recorded before use. An override cannot disable system, platform, user, repository, domain, safety, security, permission, or destructive-action controls. Never silently reset counters.

## Detection

Trigger when a budget expires while new evidence materially changes the failure; when a critic finds a correctness, security, data-loss, explicit-requirement, or regression issue after its round limit; or when critical uncertainty remains despite a context/retry cap. Also trigger on silent relaxations or open-ended exceptions.

## Recovery

Reject incomplete or forbidden overrides. For a valid case, grant the smallest bounded extension, record it in executive-override state, and restore normal limits at the exit condition. If the extension yields no material evidence, stop and do not renew automatically. See [executive override and conflicts](../guides/executive-override-conflicts.md).

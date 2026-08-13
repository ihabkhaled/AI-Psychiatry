# Context Refresh

**Purpose:** Reload context only when stale, changed, or required. Two identical reloads without new evidence trigger a reset.

**Trigger:** Load when the manifest condition matches the current task.

**Required behavior:** Preserve repository constraints and canonical sources. Classify side findings before acting.

**Budget:** WIP 1; same-strategy attempts 3; verification passes 2; critic rounds 1; nested depth 2.

**Evidence:** Record commands, source locations, test output, or explicitly labeled inference.

**Escalation:** If the next action is invalid or repeated work adds no information, reset strategy or report the exact blocker.

**Stop condition:** The rule's required outcome is proven or a blocker is declared.

**Master prompt:** sections 92–96.


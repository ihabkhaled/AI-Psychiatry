# Execution phases

Reference of the all-the-medicine skill ([SKILL.md](../SKILL.md)). Step 3 of its procedure selects the highest-priority applicable control from this order.

| Phase | Focus | Representative controls |
|---|---|---|
| 0 | Instruction and permission resolution | `rule-conflict-resolver`, executive-override boundaries, platform/system/user/repository precedence |
| 1 | Task bootstrap | `executive-control`, goal lock, Definition of Done, scope control, `decision-readiness` |
| 2 | Autonomous execution activation | `never-stop`, question-suppression gate, decision autonomy, persistent execution |
| 3 | Evidence and reality control | `evidence-gate`, `evidence-floor`, `root-cause-validator`, completion evidence prerequisites |
| 4 | Attention and scope control | `attention-reset`, `hidden-recursion-detector`, `flatten-recursive-investigation`, `scope-laundering-detector`, `anti-gaming` |
| 5 | Reasoning balance | `underthinking-detector`, `investigation-floor`, `reasoning-balance`, `stop-overthinking`, `stop-compulsive-verification`, `context-balance` |
| 6 | Loop and recovery control | `strategy-laundering-detector`, `false-progress-detector`, `recover-from-deadlock-livelock`, `blocker-validator`, narrow `executive-override` |
| 7 | Adversarial semantic control (when relevant, not for every tiny task) | `loophole-hunter`, `framework-red-team`, `anti-gaming` |
| 8 | Execution and verification | targeted execution, root-cause validation, tests, verification, critic control, mandatory quality gates |
| 9 | Completion | `completion-evidence`, `completion-gate`, false-completion protection, termination |
| 10 | Context and memory maintenance (only where reusable information exists) | `memory-validator`, `context-balance`, failure learning, repository-map update, handoff state |


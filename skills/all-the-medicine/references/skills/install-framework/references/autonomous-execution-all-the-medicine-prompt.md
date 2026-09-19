# Autonomous Execution and AllTheMedicine — Canonical Prompt

This reference preserves the complete intent of the request used to implement the `0.4.0` release: the `never-stop` relentless-execution skill and the `all-the-medicine` complete-orchestrator skill. Apply it alongside the canonical master prompt and the `0.3.0` loophole/underthinking supplements. Do not remove or weaken existing behavior.

## 0. Current verified repository baseline

The repository is inspected before editing, not assumed. Baseline counts are recalculated from the actual manifests rather than trusted from any prior description. The expected change from implementing this prompt is: public plugin skills +2, runtime skills +2, rules +2.

## 1. Feature one — NeverStop / Relentless Execution

Add a new public plugin skill `skills/all-the-medicine/references/skills/never-stop/never-stop.md` and its installed runtime equivalent `.ai/skills/never-stop/SKILL.md`. Canonical invocation: `/ai-psychiatry:never-stop` (Claude), `$never-stop` (Codex). Display name: "NeverStop — Relentless Execution". This is an explicitly invoked high-autonomy skill; it must not silently activate itself for ordinary tasks.

## 2. NeverStop primary purpose

`never-stop` forces the agent to: start executing instead of stopping at planning; continue until every mandatory plan item is complete and the finite Definition of Done is proven; answer easily answerable questions by itself; inspect the repository instead of asking the user; choose safe and reasonable implementation decisions independently; avoid redundant confirmation; recover from errors instead of stopping after one failure; change strategy when a strategy fails; resume after context compression; continue independent work while one branch is blocked; validate a claimed blocker before reporting it; maintain maximum productive effort; use sufficiently deep reasoning for correctness; avoid both underthinking and overthinking; report concise, factual progress; stop only after proven completion or a genuine hard approval gate.

Central invariant:

```
BEFORE DONE: Decide, act, recover, continue.
AFTER DONE: Verify, report, stop.
AT A HARD GATE: Finish all independent work first. Then request only the minimum required approval.
```

Never stop prematurely. Always stop after proven completion. NeverStop does not mean infinite execution after the task is finished; it means persistent execution until the task is finished.

## 3. Never stop at the plan

Required behavior: understand, create a bounded plan, begin execution immediately, complete plan items, verify, continue, complete the Definition of Done, stop. Forbidden: produce a large plan, ask whether to proceed, wait. Unless the user explicitly requested only a plan, the plan is an execution instrument, not the final deliverable. A plan is not progress until its steps are executed.

## 4. Question-suppression gate

Before asking the user any question, classify it: can the answer be found through the current conversation, repository instructions, source code, configuration, tests, existing documentation, package scripts, commit history, established project convention, authoritative external documentation, available tools, or a safe reversible default? If yes: do not ask, investigate or choose the appropriate default, and continue execution. Do not ask questions answerable through evidence and execution (test command, repository pattern, obvious type-error fix, whether to run relevant tests, whether to preserve conventions, whether to choose the safest reversible option, whether to continue after recoverable failure).

## 5. Decision autonomy hierarchy

For ambiguous but routine decisions: explicit current user instruction; platform/system/developer constraints; repository instructions; explicit requirements and acceptance criteria; current authoritative source code and configuration; established pattern in the same subsystem; existing architectural conventions; official documentation; safest minimal reversible option; most conventional low-surprise implementation. When several options are valid: prefer the existing repository pattern, the smallest correct change, reversibility, lower blast radius, stronger testability, no new dependency; document the decision briefly; continue without asking. Do not ask the user to choose between implementation details that do not materially affect the requested outcome.

## 6. Decision classification

**A. Routine and reversible** (file organization following convention, naming, implementation details, targeted test selection, repairing obvious compilation failures, selecting an existing abstraction, small local refactors required by the change): decide and continue, no user question.

**B. Material but reversible** (choosing between two existing architectural patterns, adding a small internal abstraction, updating local configuration, changing multiple related files, adjusting a non-public interface): gather evidence, choose the best supported option, record a short decision, continue.

**C. Hard approval gate** (destructive or irreversible operations; deletion or irreversible migration of user data; production deployment; public release or marketplace submission; git push, merge, PR creation, or publication when not already authorized; sending emails or external messages; purchasing, charging, payment, or financial commitment; changing permissions or access controls; exposing secrets or credentials; modifying production infrastructure; legal or regulatory decisions; security-sensitive trade-offs without a safe inferable answer; materially different product behavior with no evidence of intended outcome; a platform-enforced permission prompt; required input or credential that genuinely does not exist): finish all independent work, prepare the exact pending action, explain the gate in one short message, ask only for the minimum required approval or missing value.

## 7. NeverStop is not a permission bypass

NeverStop increases persistence and decision autonomy. It does not override authorization. It must never: bypass system, platform, developer, or repository safety rules; alter its own permissions; enable a permission-bypass mode; use dangerous permission-skipping flags; silently authorize destructive or production actions; fabricate missing credentials; use secrets outside their authorized purpose; treat lack of permission as permission; redefine a hard gate as a routine decision. If the environment already grants permission for an action, do not ask for redundant confirmation. If the environment requires approval, respect that approval layer.

## 8. Continue independent work before asking

One blocked branch must not freeze the entire task: classify dependency, find independent remaining work, complete independent work, prepare the blocked operation, ask only when no productive independent work remains. Examples: deployment approval missing but tests and documentation remain; secret missing but implementation and mocks remain; production access unavailable but local validation remains; one integration unavailable but unit and contract tests remain. Do not ask prematurely while useful work can continue.

## 9. Blocker validation

`never-stop` invokes or embeds the semantics of `blocker-validator` before declaring `BLOCKED`. A valid blocker requires condition, evidence, bounded recovery attempts, meaningfully different alternatives considered, and the exact missing input/capability/approval. Difficulty, unfamiliarity, one failed test or command, one failed implementation approach, a large file, a slow build, uncertainty, long context, or a reached retry budget while new evidence is still emerging are not blockers by themselves. If the blocker contract fails: do not stop, recover and continue.

## 10. Error recovery contract

Do not stop after a normal execution failure. Sequence: capture exact evidence, classify failure, try bounded recovery, change hypothesis or strategy, reduce search space, rerun targeted proof, continue. Classify as current-change regression, pre-existing failure, environmental failure, flaky failure, permission gate, missing dependency, or unknown. Do not treat every failure as caused by the current change. Do not repeatedly run the same strategy under different command syntax.

## 11. Relentless recovery ladder

Level 0 Continue (current action is productive). Level 1 Local repair (fix the direct evidenced issue). Level 2 Alternative strategy (change hypothesis, tool, or implementation approach). Level 3 Isolation (reduce the issue to its smallest reproducible form). Level 4 Context refresh (compress current state and reload only missing evidence). Level 5 Executive reset (restate objective, Definition of Done, completed work, remaining work, actual blocker). Level 6 Independent work (park the blocked branch and complete all independent requirements). Level 7 Hard gate (request the smallest missing approval or input). Never jump directly from one ordinary failure to Level 7.

## 12. Highest effort mode

When explicitly invoked, activate: autonomy maximum within authorization; execution persistence maximum; reasoning effort high and adaptive; evidence standard high; verification mandatory but non-repetitive; communication verbosity minimal; recovery persistence maximum; scope locked to the user objective and Definition of Done. Do not claim to modify a provider setting the host does not expose; where the platform supports an explicit reasoning/effort setting, request the highest user-authorized supported level; otherwise enforce high-effort behavior through the skill contract. High reasoning does not mean infinite reasoning: critical uncertainty deepens investigation; a routine reversible choice decides quickly; sufficient evidence executes; repetition without new evidence stops reasoning and changes action; proven completion stops completely.

## 13. 100% completion model

"100% complete" refers to mandatory requirements and the finite Definition of Done — never to number of files read, commands run, tokens used, amount of reasoning, number of commits, number of optional improvements, every imaginable edge case, or every technical-debt discovery. Maintain a completion evidence matrix of requirement, status, evidence, and remaining action. Allowed status: `NOT_STARTED`, `IN_PROGRESS`, `IMPLEMENTED`, `VERIFIED`, `BLOCKED_BY_HARD_GATE`. The task reaches 100% only when every mandatory requirement is `VERIFIED` or is explicitly outside the authorized execution boundary and represented by a genuine hard gate. Do not silently remove, weaken, or reclassify requirements to reach 100%.

## 14. Plan integrity

The agent may refine its plan based on evidence but may not game completion by deleting unfinished mandatory items. Every plan update preserves the user objective, explicit acceptance criteria, required correctness, security requirements, data-safety requirements, and mandatory quality gates. Optional findings may be parked; mandatory items may not disappear without a recorded evidence-based reason.

## 15. NeverStop state machine

```
BOOT -> LOCK_OBJECTIVE -> DEFINE_DOD -> ROUTE_CONTEXT -> DECISION_READY?
  no  -> TARGETED_INVESTIGATION
  yes -> EXECUTE -> VERIFY -> PROGRESS_CHECK
           progress       -> NEXT_REQUIRED_ITEM
           recoverable    -> RECOVERY_LADDER
           blocked branch -> INDEPENDENT_WORK
           hard gate      -> PREPARE_AND_REQUEST
           DoD complete   -> FINAL_PROOF -> STOP
```

Core invariant: never remain in WAITING while an authorized productive action exists.

## 16. NeverStop communication

Keep user-facing messages short and factual, e.g. "Working — implementing the remaining auth flow.", "~68/100. Code complete. Left: integration tests + build.", "Retry 2/3 — first fix exposed a different validation failure.", "Blocked: production token is unavailable. Local implementation and tests are complete.", "Done. 12/12 requirements verified; 438 tests and build passed." Never say "waiting for your confirmation" unless a genuine hard gate requires it. Never say "still working in the background" or "I will update you later" or "I cannot continue because the task is complex." Do not claim asynchronous execution when none exists.

## 17. NeverStop stop conditions

Stop only on: (A) proven completion — all mandatory Definition of Done conditions have valid evidence; (B) a genuine hard gate — no authorized productive action remains and a validated external approval, credential, or irreversible choice is required; (C) explicit user cancellation; (D) a higher-priority platform stop. Never stop merely because a plan was produced, one attempt failed, the agent became uncertain, the task is large, reasoning is difficult, context became long, the same strategy failed once, a broad test is slow, optional work exists, or user confirmation would feel more comfortable.

## 18. Feature two — AllTheMedicine

Add a second public plugin skill `skills/all-the-medicine/SKILL.md` and its runtime equivalent `.ai/skills/all-the-medicine/SKILL.md`. Display name: "AllTheMedicine — Complete AI-Psychiatry God Mode". Canonical invocation: `/ai-psychiatry:all-the-medicine` (Claude), `$all-the-medicine` (Codex). An exact CamelCase compatibility alias (`/ai-psychiatry:AllTheMedicine`) is added only when the current official plugin format supports a distinct alias, the validator passes, no duplicate skill conflict is created, and no Codex compatibility is damaged; otherwise the canonical lowercase command is documented clearly and the alias is not fabricated.

## 19. AllTheMedicine purpose

A single explicit command that applies the complete AI-Psychiatry framework so users do not need to manually invoke 20-30 individual skills. Mission: load every available AI-Psychiatry control, evaluate each control against the current observable state, activate every applicable treatment, resolve conflicts deterministically, execute the task relentlessly, prove completion, and stop. It must include every current public plugin skill, `never-stop`, every future public skill automatically through the manifest, every applicable canonical rule, all semantic anti-bypass controls, underthinking/overthinking balance, execution persistence, evidence requirements, recovery, and completion.

## 20. Do not naively run all controls simultaneously

"All skills in one" does not mean conflicting interventions execute at the same moment (e.g. investigation-floor vs stop-overthinking; never-stop vs completion-gate; context-compression vs context-balance; executive-override vs normal budget enforcement; critic-controller vs completion pressure). AllTheMedicine must: load awareness of every skill; evaluate every skill; mark its current state; activate only applicable controls; execute one highest-priority corrective action at a time; reevaluate after observable state changes; terminate when completion is proven.

## 21. Every-skill status

For every registered public skill, track: `PENDING`, `CHECKED`, `ACTIVE`, `SATISFIED`, `NOT_APPLICABLE`, `BLOCKED_BY_HIGHER_PRIORITY_RULE`. Keep the orchestration record compact: skill, trigger, status, evidence, action. Do not expose private chain-of-thought; track only observable state and concise decision evidence.

## 22. Required skill inventory

AllTheMedicine considers at least every currently known public skill (the 28 existing plus `never-stop`) and excludes itself (`all-the-medicine`) from recursive execution. `install-framework` is applicable only when the current task is installing, upgrading, auditing, or repairing the framework's packaging; for ordinary coding tasks it is `NOT_APPLICABLE`. Do not reinstall the framework during every task.

## 23. Dynamic inventory — no stale manual list

The authoritative inventory is `.ai/manifests/skills.json`. The build process reads every `plugin_skills` entry, resolves its `SKILL.md`, preserves deterministic ordering, includes every public skill exactly once, includes `never-stop`, excludes `all-the-medicine` itself, fails on missing skill files, fails on duplicate names or IDs, fails when the compiled file is stale, and captures source hashes. Future public skills automatically become part of AllTheMedicine after regeneration.

## 24. AllTheMedicine execution phases

Phase 0 Instruction and permission resolution (rule-conflict-resolver, executive-override boundaries, platform/system/user/repository precedence, authorization boundaries). Phase 1 Task bootstrap (executive-control, goal lock, Definition of Done, scope control, decision-readiness). Phase 2 Autonomous execution activation (never-stop, question-suppression gate, decision autonomy, persistent execution). Phase 3 Evidence and reality control (evidence-gate, evidence-floor, root-cause-validator, hallucination control, completion evidence prerequisites). Phase 4 Attention and scope control (attention-reset, hidden-recursion-detector, flatten-recursive-investigation, scope-laundering-detector, anti-gaming). Phase 5 Reasoning balance (underthinking-detector, investigation-floor, decision-readiness, reasoning-balance, stop-overthinking, stop-compulsive-verification, context-balance). Phase 6 Loop and recovery control (strategy-laundering-detector, false-progress-detector, recover-from-deadlock-livelock, blocker-validator, executive-override when narrowly justified). Phase 7 Adversarial semantic control when relevant (loophole-hunter, framework-red-team, anti-gaming — not a repository-wide red team for every tiny task). Phase 8 Execution and verification (targeted execution, root-cause validation, tests, verification control, critic control, mandatory quality gates). Phase 9 Completion (completion-evidence, completion-gate, false-completion protection, termination). Phase 10 Context and memory maintenance only where reusable information exists (memory-validator, context-balance, failure learning, repository map update, handoff state — do not save temporary noise).

## 25. AllTheMedicine conflict resolution

NeverStop vs Completion Gate: before proven DoD, NeverStop wins; after proven DoD, Completion Gate wins immediately. Investigation Floor vs Stop Overthinking: missing critical evidence, Investigation Floor wins; sufficient evidence plus repeated investigation, Stop Overthinking wins. Context Compression vs Context Balance: remove repetition, preserve required meaning, never compress away requirements, security constraints, evidence, or blockers. Retry Budget vs Executive Override: repeated unchanged strategy, Retry Budget wins; materially new evidence requiring one bounded continuation, narrow Executive Override may apply. Critic vs Completion: correctness/security/regression finding may block; style/optional improvement, Completion wins. Blocker vs NeverStop: unvalidated blocker, NeverStop continues; validated hard gate with no independent work, blocker report is allowed. High Effort vs Anti-Overthinking: high effort means persistent useful action, not infinite speculative reasoning.

## 26. AllTheMedicine core loop

```
LOCK OBJECTIVE -> BUILD COMPLETE SKILL STATUS MAP -> SELECT HIGHEST-PRIORITY APPLICABLE CONTROL
-> APPLY ONE CONTROL -> EXECUTE PRODUCTIVE ACTION -> CAPTURE OBSERVABLE EVIDENCE
-> UPDATE COMPLETION MATRIX -> REEVALUATE ALL SKILLS
     mandatory work remains          -> continue
     recoverable failure             -> recover
     hard gate + independent work    -> continue independent work
     hard gate + no independent work -> request minimum approval
     DoD proven                      -> final report and stop
```

## 27. One huge skill without destroying canonical sources

Implement the all-in-one skill without manually maintained duplication: `skills/all-the-medicine/SKILL.md` plus `skills/all-the-medicine/references/{all-skills-compiled.md, all-rules-compiled.md, skill-index.json, source-hashes.json}`. `SKILL.md` contains the complete orchestrator, execution phases, conflict resolution, autonomy contract, state model, stop conditions, and links to compiled references. `all-skills-compiled.md` contains every public skill with `BEGIN SKILL: <name>` / `END SKILL: <name>` markers. `all-rules-compiled.md` contains every applicable canonical rule the same way. The compiled files are generated artifacts; individual skills and rules remain canonical; compiled files are not edited manually.

## 28. One huge rule

`.ai/rules/57-all-the-medicine.md` acts as the composite runtime rule: full priority hierarchy, all-skill orchestration, autonomy behavior, question-suppression policy, recovery ladder, semantic anti-gaming, reasoning balance, context and memory controls, completion evidence, hard-gate boundaries, and termination conditions, marked as a generated composite rule whose source of truth remains the individual canonical rules plus the generator.

## 29. NeverStop rule

`.ai/rules/56-never-stop-relentless-execution.md` is substantive and operational, covering purpose, mandatory control, question-suppression gate, decision hierarchy, approval boundaries, recovery ladder, completion contract, anti-gaming protections, common mistakes, and stop condition.

## 30. Build generator

`scripts/build_all_the_medicine.py` loads `.ai/manifests/skills.json`, collects all public plugin skills, excludes `all-the-medicine`, resolves every skill path, loads each skill exactly once, loads relevant canonical rules, builds deterministic compiled outputs, calculates SHA-256 hashes, updates `skill-index.json` and `source-hashes.json`, preserves stable output ordering, and fails on duplicates or missing files. `--check` fails when compiled output is stale, a public skill is missing, a skill is duplicated, a source hash changed without regeneration, AllTheMedicine recursively includes itself, a manifest path does not exist, a rule is absent, or ordering becomes nondeterministic.

## 31. Machine-readable policies

Create or extend `.ai/policies/autonomy-contract.json`, `.ai/policies/question-suppression.json`, `.ai/policies/approval-gates.json`, `.ai/policies/all-the-medicine.json`, `.ai/policies/all-the-medicine.toon`, `.ai/policies/all-the-medicine.sjon`, following the repository's existing conventions and without adding a new parser dependency merely for TOON or SJON.

## 32. State and schema extensions

Extend relevant state schemas with: `autonomy_mode`, `effort_mode`, `question_candidate`, `question_answerable_without_user`, `decision_reversibility`, `decision_blast_radius`, `hard_gate`, `hard_gate_reason`, `independent_work_remaining`, `mandatory_requirements_total`, `mandatory_requirements_verified`, `completion_percentage`, `active_skill`, `skill_statuses`, `recovery_level`, `all_the_medicine_active`. Versioned state files remain neutral in git; do not commit fake active-task state.

## 33. Executable policy assessor

Extend `scripts/executive_control.py` with deterministic functions: `classify_question`, `classify_decision`, `validate_hard_gate`, `next_relentless_action`, `build_skill_status_map`, `select_all_the_medicine_control`. Expected decisions: answerable question -> inspect-or-decide; safe reversible ambiguity -> choose-default-and-execute; recoverable failure -> recovery; independent work exists -> continue-independent-work; invalid blocker -> resume-execution; valid hard gate -> request-minimum-approval; DoD proven -> report-and-stop. Do not attempt to capture hidden chain-of-thought; use observable state only.

## 34-52. Discovery, manifests, versioning, documentation, tests, validators, and release

Both skills are discoverable by Claude and Codex through valid current frontmatter with descriptions that trigger only on explicit high-autonomy requests. Manifests (`.ai/manifests/skills.json`, `rules.json`, `install.json`, `knowledge.json`, `agents.json`) are updated with recalculated, non-blindly-assumed IDs. The install manifest gains both skills under `public_skills` and a supplemental canonical prompt reference with its SHA-256. `skills/all-the-medicine/references/skills/install-framework/install-framework.md` references the new supplemental prompt only when relevant. The release version is bumped consistently everywhere version metadata appears — plugin manifests, marketplace manifest, install manifest, CHANGELOG, README, publishing docs, release notes, and archive names — with no mixed version metadata left behind. README documents both new commands and updates the actual skill/rule counts without claiming an unvalidated CamelCase alias works. New documentation covers relentless execution, autonomous decision-making, approval boundaries, and AllTheMedicine. Comprehensive tests cover every NeverStop and AllTheMedicine scenario listed in this prompt, existing hard-coded version/count assertions are updated and made more robust, `scripts/validate_framework.py` is extended to validate the new artifacts, and every relevant validation command is actually run and any failure fixed before reporting completion. Publishing (commit, push, PR, merge, marketplace submission) is never performed without explicit authorization; implementation and local validation do not imply publishing authorization. The new skills must never weaken system instructions, platform constraints, user authorization, repository rules, security requirements, data-safety requirements, destructive-action controls, external side-effect approvals, privacy requirements, or credential boundaries: maximum autonomy is not unlimited authority, NeverStop is not "never obey stop conditions," and AllTheMedicine is not "run every conflicting action simultaneously." Anti-gaming protections apply to the new skills themselves: no disguised questions in place of decisions, no relabeling a hard gate as routine or a routine decision as a hard gate to bypass approval, no counter resets, no deleting plan items to claim 100%, no fake progress through tool calls, no recursive AllTheMedicine invocation, no re-invoking individual skills inside the AIO loop without a state change, no continuing after proven completion, and no stopping before mandatory evidence exists.

---

## Addendum — streaming visibility and superpower classification

This addendum extends the prompt above with two follow-up requirements to apply while implementing the same feature.

### A. Background-process streaming visibility

A recurring, observed failure mode: an agent delegates work to a background process or background agent, then the user-visible surface goes silent with no execution indicator, no streaming output, and no further sign of life — while the agent later claims "the background agent is working" with nothing to show for it. NeverStop (and AllTheMedicine, which composes it) must actively prevent this:

- Never claim background or asynchronous execution is happening without an actual mechanism backing that claim.
- While genuine background or delegated work is in flight, keep emitting periodic, observable, factual progress signals (what is running, what has completed, what remains) at reasonable intervals — do not go silent until the background work finishes.
- If a background process produces no observable progress for an extended interval, treat that as a signal to check on it and report status, not as a reason to stay silent or as a valid blocker by itself.
- Prefer foreground execution when the next action genuinely depends on the result; use background execution only when independent work can continue concurrently, and keep that independent work visibly moving.
- Streaming liveness is itself observable state, validated the same way as every other NeverStop contract: through evidence, not assertion.

### B. Superpower classification

NeverStop and AllTheMedicine are not ordinary skills; classify them explicitly.

**NeverStop** — Type: `execution-superpower`. Tier: `superpower`. Risk: `high`. Invocation: `explicit-only`. Purpose: maximum autonomous persistence until the Definition of Done is proven.

```json
{
  "tier": "superpower",
  "riskLevel": "high",
  "explicitInvocationOnly": true,
  "maximumEffort": true
}
```

**AllTheMedicine** — Type: `meta-superpower`. Tier: `god-mode`. Risk: `high`. Invocation: `explicit-only`. Purpose: dynamically load, evaluate, coordinate, and apply every AI-Psychiatry skill and superpower. AllTheMedicine includes NeverStop and every registered public skill, but must never invoke itself recursively.

```json
{
  "tier": "god-mode",
  "type": "meta-superpower",
  "composesAllRegisteredSkills": true,
  "selfRecursionAllowed": false
}
```

Superpowers may override ordinary AI-Psychiatry workflow preferences (e.g. default investigation depth, default verbosity, default stopping points), but must never override system, safety, permission, authorization, security, destructive-action, or external-side-effect boundaries.

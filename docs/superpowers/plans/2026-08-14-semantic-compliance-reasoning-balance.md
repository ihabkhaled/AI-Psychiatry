# Semantic Compliance and Reasoning Balance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship, push, and submit AI-Psychiatry `0.3.0` with operational semantic anti-bypass and sufficient-reasoning controls.

**Architecture:** Extend the pure Python assessor with observable semantic classifiers and immutable evidence contracts, backed by portable JSON/TOON/SJON policy state. Route those controls through provider-neutral plugin skills, repository rules, focused guides, manifests, and adversarial regressions.

**Tech Stack:** Python 3 standard library, JSON, Markdown/YAML skill files, TOON/SJON text representations, unittest, Claude Code CLI, Codex plugin validator, official browser submission portals.

**Spec:** `docs/superpowers/specs/2026-08-14-semantic-compliance-reasoning-balance-design.md`

## Global Constraints

- Work directly on the clean `main` branch as explicitly requested.
- Preserve all existing AI-Psychiatry behavior and the canonical master prompt hash.
- Use test-first implementation for executable behavior and baseline/forward pressure tests for discipline skills.
- Track only observable execution state, never private chain-of-thought.
- Keep the plugin skills-only and provider-neutral; no MCP server or external runtime dependency.
- Bump Claude, Codex, and marketplace versions together to `0.3.0`.

---

### Task 1: Baseline adversarial behavior

**Files:**
- Create: `docs/ai/loophole-baseline-results.md`

**Interfaces:**
- Consumes: current `0.2.0` skills and rules.
- Produces: exact baseline rationalizations that the new skills must counter.

- [ ] Run fresh-context agents against strategy laundering, false completion/blocker, hidden recursion, and underthinking scenarios without new skills.
- [ ] Record choices, semantic violations, and verbatim rationalizations.
- [ ] Select only failures that require new instruction; retain already-good behavior as regression expectations.

### Task 2: Semantic policy engine

**Files:**
- Modify: `scripts/executive_control.py`
- Create: `tests/test_semantic_compliance.py`

**Interfaces:**
- Produces: `strategy_identity`, `count_equivalent_attempts`, `causal_depth`, `validate_progress`, `validate_completion`, `validate_blocker`, `validate_scope_expansion`, `validate_memory`, `validate_context`, `reasoning_balance`, `validate_override`, `resolve_rule_conflict`, and `self_check`.

- [ ] Write behavioral tests with literal expected decisions for each function and each stated bypass.
- [ ] Run the new test module and confirm failures are caused by missing functions.
- [ ] Implement the minimum pure functions and integrate them into backward-compatible `assess` routing.
- [ ] Run the new module and the existing intervention suite until both pass.

### Task 3: Machine-readable evidence state

**Files:**
- Create: `.ai/policies/semantic-compliance.json`
- Create: `.ai/policies/semantic-compliance.toon`
- Create: `.ai/state/action-ledger.json`
- Create: `.ai/state/completion-evidence.json`
- Create: `.ai/state/reasoning-balance.json`
- Create: `.ai/state/reasoning-balance.toon`
- Create: `.ai/state/reasoning-balance.sjon`
- Create: `.ai/state/executive-override.json`
- Create: `.ai/executive-function/semantic-state.schema.json`
- Modify: `.ai/telemetry/thresholds.json`
- Test: `tests/test_semantic_assets.py`

**Interfaces:**
- Consumes: semantic function field names from Task 2.
- Produces: portable state contracts used by skills, rules, and validation.

- [ ] Write schema/fixture tests that load real files and exercise the semantic engine.
- [ ] Confirm the tests fail because the artifacts are absent.
- [ ] Add compact artifacts with semantic counters, evidence floors, critical unknowns, conflict priority, and explicit override fields.
- [ ] Run the asset tests and existing framework tests.

### Task 4: Rules, guides, and loophole catalog

**Files:**
- Create: `.ai/rules/41-semantic-compliance.md` through `.ai/rules/55-self-check.md`
- Create: `.ai/guides/semantic-compliance.md`
- Create: `.ai/guides/loophole-catalog.md`
- Create: `.ai/guides/underthinking.md`
- Create: `.ai/guides/reasoning-balance.md`
- Create: `.ai/guides/context-starvation.md`
- Create: `.ai/guides/sufficient-reasoning.md`
- Create: `.ai/guides/executive-override-conflicts.md`
- Create: `.ai/tests/loophole-regression-cases.md`
- Create: `.ai/tests/underthinking-cases.md`
- Test: `tests/test_semantic_assets.py`

**Interfaces:**
- Consumes: policy contracts from Task 3.
- Produces: mandatory controls and regression cases discoverable by installers.

- [ ] Add failing asset tests for numbered rules, required guide contracts, loophole row fields, and all ten underthinking scenarios.
- [ ] Write focused rules and guides without weakening rules 00-40.
- [ ] Run asset and framework validators; repair links and manifest references.

### Task 5: Public and installed skills

**Files:**
- Create: `skills/<new-skill>/SKILL.md` for the nineteen design-listed skills.
- Create: `.ai/skills/<new-skill>/SKILL.md` for the same operational controls.
- Modify: `skills/executive-control/SKILL.md`
- Modify: `skills/install-framework/SKILL.md`
- Modify: `.ai/skills/executive-function/SKILL.md`
- Test: `tests/test_semantic_assets.py`

**Interfaces:**
- Consumes: baseline rationalizations and semantic policy artifacts.
- Produces: callable Claude `/ai-psychiatry:<skill>` and Codex `$<skill>` workflows.

- [ ] Add failing discoverability and uniqueness tests for all new skills.
- [ ] Initialize each new public skill using the skill-creator initializer, then replace templates with concise provider-neutral procedures.
- [ ] Add exact anti-rationalization counters from baseline results, common mistakes, and termination conditions.
- [ ] Validate each public and installed skill separately.
- [ ] Forward-test representative anti-gaming, completion/blocker, recursion/laundering, and reasoning-balance skills and close any new bypasses.

### Task 6: Manifests, installer, docs, and release metadata

**Files:**
- Modify: `.ai/manifests/rules.json`
- Modify: `.ai/manifests/skills.json`
- Modify: `.ai/manifests/knowledge.json`
- Modify: `.ai/manifests/install.json`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `.codex-plugin/plugin.json`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `docs/ai/README.md`
- Create: `docs/ai/underthinking.md`
- Create: `docs/ai/reasoning-balance.md`
- Create: `docs/ai/context-starvation.md`
- Create: `docs/ai/sufficient-reasoning.md`
- Create: `skills/install-framework/references/loophole-enhancement-prompts.md`
- Create: `skills/install-framework/references/underthinking-reasoning-balance-prompt.md`
- Test: `tests/test_plugin_package.py`

**Interfaces:**
- Produces: installable `0.3.0` packages with complete progressive disclosure.

- [ ] Add failing tests for version parity, public skill catalogs, policy layers, and reference prompts.
- [ ] Update manifests and installer routes, preserving the existing canonical prompt.
- [ ] Document direct marketplace installation and the distinction between hosted, submitted, approved, and searchable.
- [ ] Run package and full repository tests.

### Task 7: Publication materials and archive

**Files:**
- Create: `assets/ai-psychiatry-logo.png`
- Create: `PRIVACY.md`
- Create: `TERMS.md`
- Create: `SUPPORT.md`
- Modify: `docs/listing/claude.md`
- Modify: `docs/listing/codex.md`
- Modify: `docs/listing/test-cases.md`
- Modify: `docs/listing/release-notes.md`
- Modify: `docs/listing/publisher-checklist.md`
- Generate: `dist/ai-psychiatry-0.3.0.zip`
- Test: `tests/test_publication_materials.py`

**Interfaces:**
- Produces: a Claude GitHub source and an OpenAI Skills-only upload archive with public listing/legal URLs.

- [ ] Add failing publication tests for assets, eight listing cases, legal/support files, and archive-root structure.
- [ ] Add accurate no-telemetry/no-service policy text and a neutral production logo.
- [ ] Build the archive with `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `skills/`, referenced runtime assets, README, license, and policy files at valid paths.
- [ ] Open the archive and assert every skill reference resolves inside it.

### Task 8: Validation, push, and submission

**Files:**
- Modify: `docs/listing/publisher-checklist.md`

**Interfaces:**
- Consumes: completed `0.3.0` release and authenticated platform sessions.
- Produces: remote main commit plus recorded Claude and OpenAI submission identifiers or exact external blockers.

- [ ] Run all unit tests, framework validation, 75 skill validations, strict Claude validation, Codex validation, link validation, and `git diff --check`.
- [ ] Add the GitHub marketplace locally with Claude CLI, install `ai-psychiatry@ihabkhaled-ai`, and confirm skills are discoverable.
- [ ] Commit on `main`, push `origin/main`, and confirm remote SHA.
- [ ] Submit the GitHub plugin through Anthropic's community marketplace form.
- [ ] Upload the skills-only archive through the OpenAI Platform plugin portal, repair scan findings, and submit the draft.
- [ ] Record submission IDs/statuses without claiming approval before vendor review.

# AI Psychiatry Full Plugin Build Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, and prepare publication of one complete AI Psychiatry framework distributed as compatible Claude Code and OpenAI Codex plugins.

**Architecture:** A shared `install-framework` skill progressively loads the canonical master prompt and installs a dogfooded `.ai/` runtime. Thin platform adapters route to focused canonical rules and skills, while generated manifests and a standard-library validator prove structure, traceability, context budgets, and scenario coverage.

**Tech Stack:** Markdown, JSON, TOON, SJON, JSON Schema, Python 3 standard library, Claude Code CLI, Codex CLI, Git.

**Spec:** `docs/superpowers/specs/2026-08-14-ai-psychiatry-full-build-design.md`

## Global Constraints

- Preserve the source pack at `D:\Freelance\Packs, Plans, And Prompts\AI-Psychiatry` unchanged.
- Preserve useful repository-specific instructions and never create competing canonical knowledge systems.
- Treat psychiatric terminology as branding or behavioral analogy; operational controls use engineering language and make no diagnosis or consciousness claim.
- Cover every numbered master-prompt section through traceable runtime, skill, adapter, test, packaging, or documentation artifacts.
- Keep root/platform adapters thin and keep the large master prompt out of always-loaded skill context.
- Use no runtime package dependencies, MCP server, hooks, or app.
- Store no chain-of-thought or fabricated progress; version only neutral state templates.
- Do not claim marketplace publication until submission and platform acceptance are evidenced.

---

### Task 1: Replace the Placeholder with Canonical Plugin Packaging

**Files:**
- Modify: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`
- Create: `.codex-plugin/plugin.json`
- Delete: `skills/example-skill/SKILL.md`
- Delete: `agents/.gitkeep`
- Delete: `hooks/.gitkeep`
- Delete: `codex/README.md`
- Delete: `codex/prompts/.gitkeep`
- Create: `skills/install-framework/SKILL.md`
- Create: `skills/install-framework/references/master-prompt.md`
- Create: `tests/test_plugin_package.py`

**Interfaces:**
- Consumes: source-pack manifests, installer skill, and master prompt.
- Produces: valid shared skill path `skills/install-framework`, plugin name `ai-psychiatry`, and canonical specification path used by all later tasks.

- [ ] **Step 1: Write failing package tests**

```python
def test_both_manifests_expose_shared_install_skill(repo):
    assert (repo / ".claude-plugin/plugin.json").exists()
    codex = load_json(repo / ".codex-plugin/plugin.json")
    assert codex["skills"] == "./skills/"
    assert (repo / "skills/install-framework/SKILL.md").exists()

def test_master_prompt_is_progressively_disclosed(repo):
    skill = read(repo / "skills/install-framework/SKILL.md")
    assert "references/master-prompt.md" in skill
    assert len(skill.encode()) < 5000
    assert (repo / "skills/install-framework/references/master-prompt.md").stat().st_size > 60000
```

- [ ] **Step 2: Run the focused tests and verify failure**

Run: `python -m unittest tests.test_plugin_package -v`

Expected: FAIL because Codex packaging and the real shared skill do not exist.

- [ ] **Step 3: Copy canonical source artifacts and remove placeholders**

Use `apply_patch` for small manifests and deletion; copy the unchanged 66 KB master prompt with `Copy-Item -LiteralPath` and verify its SHA-256 matches the source. Ensure both manifest names equal `ai-psychiatry`, descriptions match, and only Codex declares `"skills": "./skills/"` where its schema supports it.

- [ ] **Step 4: Run package and vendor validation**

Run: `python -m unittest tests.test_plugin_package -v`

Run: `claude plugin validate .`

Run: `python C:\Users\Ihab\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .`

Expected: all checks PASS.

- [ ] **Step 5: Commit the canonical plugin package**

```powershell
git add .claude-plugin .codex-plugin skills tests/test_plugin_package.py agents hooks codex
git commit -m "feat: add shared Claude and Codex plugin package"
```

### Task 2: Build the Runtime Core and Machine State

**Files:**
- Create: `.ai/README.md`
- Create: `.ai/bootstrap/{boot.md,boot.json,boot.toon,boot.sjon}`
- Create: `.ai/executive-function/{README.md,executive-function.md,executive-function.json,executive-function.toon,executive-function.sjon,state-machine.md,state-machine.json,state.schema.json}`
- Create: `.ai/state/{active-task.json,active-task.toon,progress.json,recovery.json,session-summary.md}`
- Create: `.ai/telemetry/{README.md,signals.schema.json,thresholds.json}`
- Create: `tests/test_runtime_core.py`

**Interfaces:**
- Consumes: canonical master prompt sections 10–14, 21–39, 47–55, 80–83, 98–103, and 167–172.
- Produces: state names `idle`, `focused`, `drift_warning`, `attention_reset`, `strategy_reset`, `isolated`, `blocked`, and `complete`; neutral state templates; retry limit 3; nested-job depth limit 2.

- [ ] **Step 1: Write failing state-machine and neutral-state tests**

```python
def test_state_machine_has_bounded_recovery(repo):
    machine = load_json(repo / ".ai/executive-function/state-machine.json")
    assert machine["limits"]["same_strategy_attempts"] == 3
    assert machine["limits"]["nested_job_depth"] == 2
    assert set(machine["terminal_states"]) == {"blocked", "complete"}

def test_versioned_state_never_fakes_activity(repo):
    state = load_json(repo / ".ai/state/active-task.json")
    assert state["status"] == "idle"
    assert state["objective"] is None
    assert state["history"] == []
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_runtime_core -v`

Expected: FAIL because `.ai/` does not exist.

- [ ] **Step 3: Implement the compact runtime in four synchronized formats**

Define bootstrap as objective → constraints → evidence → next action → completion proof. Define only observable state, counters, transitions, and timestamps. JSON is machine canonical; TOON/SJON mirror its fields and name the JSON source.

- [ ] **Step 4: Validate runtime files**

Run: `python -m unittest tests.test_runtime_core -v`

Run: `python -m json.tool .ai/executive-function/state-machine.json > $null`

Expected: PASS and valid JSON.

- [ ] **Step 5: Commit the runtime core**

```powershell
git add .ai tests/test_runtime_core.py
git commit -m "feat: add executive control runtime"
```

### Task 3: Decompose the Complete Prompt into Focused Rules

**Files:**
- Create: `.ai/rules/00-master-rules.md` through `.ai/rules/40-change-strategy.md`
- Create: `.ai/manifests/rules.json`
- Create: `.ai/manifests/prompt-traceability.json`
- Create: `tests/test_rule_catalog.py`

**Interfaces:**
- Consumes: all numbered master-prompt sections 0–189.
- Produces: stable rule IDs `rule-00` through `rule-40`; manifest fields `id`, `path`, `priority`, `load_when`, `canonical_source`, and `prompt_sections`; complete prompt-section coverage.

- [ ] **Step 1: Write failing catalog and traceability tests**

```python
def test_rule_manifest_is_complete(repo):
    rules = load_json(repo / ".ai/manifests/rules.json")["rules"]
    assert [r["id"] for r in rules] == [f"rule-{n:02d}" for n in range(41)]
    assert all((repo / r["path"]).exists() for r in rules)

def test_every_prompt_section_is_traced(repo):
    trace = load_json(repo / ".ai/manifests/prompt-traceability.json")["sections"]
    assert set(map(str, range(190))).issubset(trace)
    assert all(trace[str(n)]["artifacts"] for n in range(190))
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_rule_catalog -v`

Expected: FAIL because focused rules and traceability do not exist.

- [ ] **Step 3: Author all 41 focused rules and manifests**

Each rule states purpose, trigger, required behavior, budget/limit, evidence, escalation, stop condition, and master-prompt sections. Explicitly map hallucination; ADHD-style attention drift; OCD-style compulsive checking; nested jobs; recursive thinking; rabbit holes; context reload loops; fake progress; deadlock/livelock; scope drift; and completion avoidance.

- [ ] **Step 4: Run catalog tests and scan for instruction duplication**

Run: `python -m unittest tests.test_rule_catalog -v`

Run: `rg -n "AI systems have|diagnos" .ai/rules`

Expected: tests PASS; terminology appears only in analogy disclaimers, never as a diagnosis.

- [ ] **Step 5: Commit the rule catalog**

```powershell
git add .ai/rules .ai/manifests tests/test_rule_catalog.py
git commit -m "feat: add traceable executive control rules"
```

### Task 4: Add Operational Skills

**Files:**
- Create: `.ai/skills/*/SKILL.md` for the 28 skill names in master-prompt section 8.
- Create: `.ai/manifests/skills.json`
- Create: `tests/test_skill_catalog.py`

**Interfaces:**
- Consumes: rule IDs from Task 3 and runtime states from Task 2.
- Produces: 28 uniquely named focused skills with YAML frontmatter, trigger, inputs, bounded steps, outputs, escalation, and stop condition.

- [ ] **Step 1: Write failing skill discovery tests**

```python
def test_all_operational_skills_are_discoverable(repo):
    manifest = load_json(repo / ".ai/manifests/skills.json")["skills"]
    assert len(manifest) == 28
    for item in manifest:
        text = read(repo / item["path"])
        assert text.startswith("---\nname:")
        assert "## Stop condition" in text
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_skill_catalog -v`

Expected: FAIL because operational skills are absent.

- [ ] **Step 3: Implement the 28 focused skills**

Create task-bootstrap, executive-function, goal-lock, scope-guard, attention-reset, bounded-investigation, anti-overthinking, loop-detector, deadlock-recovery, livelock-recovery, strategy-reset, progress-audit, evidence-gate, context-router, context-refresh, context-compression, memory-curator, knowledge-maintainer, communicate-briefly, targeted-testing, verification-controller, critic-controller, completion-gate, failure-learning, repository-map-update, multi-agent-coordinator, resume-task, and handoff-task.

- [ ] **Step 4: Validate the skill catalog**

Run: `python -m unittest tests.test_skill_catalog -v`

Run each skill through `quick_validate.py` in a PowerShell loop.

Expected: all 28 skills PASS.

- [ ] **Step 5: Commit operational skills**

```powershell
git add .ai/skills .ai/manifests/skills.json tests/test_skill_catalog.py
git commit -m "feat: add bounded operational skills"
```

### Task 5: Add Context, Memory, and Knowledge Architecture

**Files:**
- Create: `.ai/context/{index.md,context-index.json,context-index.toon,repository-map.md,architecture.md,current-task.md,current-task.json,current-task.toon,decisions.md,discoveries.md,blockers.md,follow-ups.md}`
- Create: `.ai/context/domains/.gitkeep`
- Create: `.ai/memory/{README.md,index.md,index.json,preferences.md,architecture.md,decisions.md,recurring-problems.md,lessons.md,failure-patterns.md}`
- Create: `.ai/manifests/knowledge.json`
- Create: `tests/test_knowledge_architecture.py`

**Interfaces:**
- Consumes: runtime state boundary from Task 2.
- Produces: load conditions `always`, `task`, `domain`, and `on_demand`; a repository map; durable-memory promotion criteria; neutral current-task templates.

- [ ] **Step 1: Write failing boundary tests**

```python
def test_context_index_has_progressive_disclosure(repo):
    index = load_json(repo / ".ai/context/context-index.json")
    assert {x["load"] for x in index["sources"]} >= {"always", "task", "domain", "on_demand"}

def test_memory_manifest_excludes_task_state(repo):
    knowledge = load_json(repo / ".ai/manifests/knowledge.json")
    durable = {x["path"] for x in knowledge["durable_memory"]}
    assert not any("current-task" in p or "/state/" in p for p in durable)
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_knowledge_architecture -v`

Expected: FAIL because indexes and manifests are absent.

- [ ] **Step 3: Implement layered context and durable memory**

Document promotion only when knowledge is reusable, evidenced, stable, and future-token-saving. Keep discoveries/blockers/follow-ups temporary until promoted. Describe this plugin repository in `repository-map.md` without inventing external services.

- [ ] **Step 4: Validate boundaries**

Run: `python -m unittest tests.test_knowledge_architecture -v`

Expected: PASS.

- [ ] **Step 5: Commit context and memory**

```powershell
git add .ai/context .ai/memory .ai/manifests/knowledge.json tests/test_knowledge_architecture.py
git commit -m "feat: add context and memory architecture"
```

### Task 6: Add Thin Agent Adapters

**Files:**
- Create: `CLAUDE.md`, `CODEX.md`, `AGENTS.md`, `GEMINI.md`, `KIMI.md`, `QWEN.md`, `DEEPSEEK.md`, `GLM.md`, `MISTRAL.md`, `.cursorrules`
- Create: `.github/copilot-instructions.md`
- Create: `.cursor/rules/{ai-executive-function.mdc,communication.mdc,context-routing.mdc}`
- Create: `.claude/rules/ai-psychiatry.md`
- Create: `.codex/instructions/ai-psychiatry.md`
- Create: `.ai/manifests/agents.json`
- Create: `tests/test_agent_adapters.py`

**Interfaces:**
- Consumes: `.ai/bootstrap/boot.md` and `.ai/rules/00-master-rules.md`.
- Produces: adapters under 1,500 bytes each with explicit precedence and canonical links.

- [ ] **Step 1: Write failing adapter consistency tests**

```python
def test_adapters_are_thin_and_route_to_boot(repo):
    for path in adapter_paths(repo):
        text = read(path)
        assert len(text.encode()) <= 1500
        assert ".ai/bootstrap/boot.md" in text
        assert ".ai/rules/00-master-rules.md" in text
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_agent_adapters -v`

Expected: FAIL because adapters are absent.

- [ ] **Step 3: Implement platform adapters and manifest**

Use platform syntax only where needed. Every adapter states precedence and analogy disclaimer, then routes to canonical files without copying rule prose.

- [ ] **Step 4: Validate adapter size and consistency**

Run: `python -m unittest tests.test_agent_adapters -v`

Expected: PASS.

- [ ] **Step 5: Commit adapters**

```powershell
git add CLAUDE.md CODEX.md AGENTS.md GEMINI.md KIMI.md QWEN.md DEEPSEEK.md GLM.md MISTRAL.md .cursorrules .github .cursor .claude .codex .ai/manifests/agents.json tests/test_agent_adapters.py
git commit -m "feat: add thin cross-agent adapters"
```

### Task 7: Add Human Documentation and Framework Scenarios

**Files:**
- Create: `docs/ai/*.md` for the 14 documents in master-prompt section 8.
- Create: `.ai/tests/{README.md,executive-function-cases.md,deadlock-cases.md,livelock-cases.md,scope-drift-cases.md,context-drift-cases.md,retry-loop-cases.md,critic-loop-cases.md,completion-cases.md}`
- Create: `tests/test_scenario_coverage.py`

**Interfaces:**
- Consumes: rule and skill IDs.
- Produces: human analogy mapping and Given/When/Then cases with expected state transitions and stop conditions.

- [ ] **Step 1: Write failing scenario coverage tests**

```python
def test_required_failure_modes_have_cases(repo):
    corpus = "\n".join(read(p).lower() for p in (repo / ".ai/tests").glob("*.md"))
    for term in ["hallucination", "attention drift", "compulsive checking", "nested job", "deadlock", "livelock", "completion avoidance"]:
        assert term in corpus
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_scenario_coverage -v`

Expected: FAIL because scenario and human documentation are absent.

- [ ] **Step 3: Write focused documentation and executable prose cases**

Each case contains setup, observable signals, required control, expected transition, forbidden behavior, proof, and termination. The analogy document explicitly separates human clinical conditions from agent behavior labels.

- [ ] **Step 4: Validate scenario coverage**

Run: `python -m unittest tests.test_scenario_coverage -v`

Expected: PASS.

- [ ] **Step 5: Commit docs and scenarios**

```powershell
git add docs/ai .ai/tests tests/test_scenario_coverage.py
git commit -m "docs: add framework guidance and regression cases"
```

### Task 8: Build the Repository Validator

**Files:**
- Create: `scripts/validate_framework.py`
- Create: `tests/test_validate_framework.py`
- Create: `.gitignore`

**Interfaces:**
- Consumes: all manifests, schemas, Markdown, adapters, skills, and traceability data.
- Produces: CLI `python scripts/validate_framework.py [--root PATH]` returning 0 on success and a concise categorized error list on failure.

- [ ] **Step 1: Write failing validator unit tests**

```python
def test_validator_rejects_broken_link(tmp_repo):
    write(tmp_repo / "README.md", "[broken](missing.md)")
    result = validate(tmp_repo)
    assert "broken-link" in result.codes

def test_validator_rejects_untraced_section(tmp_repo):
    fixture_framework(tmp_repo, omit_section="189")
    assert "traceability-gap" in validate(tmp_repo).codes
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_validate_framework -v`

Expected: FAIL because validator API is absent.

- [ ] **Step 3: Implement dependency-free validation**

Implement JSON parsing, required-field/schema subset checks, Markdown link resolution, unique IDs, declared-path checks, rule dependency cycle detection, adapter and boot-size budgets, skill frontmatter checks, neutral-state checks, analogy disclaimer checks, traceability coverage, and scenario keywords. Emit `[category] path: message` and a final count.

- [ ] **Step 4: Run validator tests and full validation**

Run: `python -m unittest tests.test_validate_framework -v`

Run: `python scripts/validate_framework.py`

Expected: PASS and `Framework validation passed`.

- [ ] **Step 5: Commit validation tooling**

```powershell
git add scripts tests .gitignore
git commit -m "test: add framework integrity validator"
```

### Task 9: Complete README and Publication Materials

**Files:**
- Modify: `README.md`
- Create: `docs/publishing.md`
- Create: `docs/listing/{claude.md,codex.md,test-cases.md,release-notes.md,publisher-checklist.md}`
- Create: `CHANGELOG.md`
- Create: `LICENSE`
- Create: `tests/test_publication_materials.py`

**Interfaces:**
- Consumes: final invocation names and validation commands.
- Produces: accurate install/invoke docs, ten listing-ready prompts/cases, release `0.1.0`, and an external-gate checklist.

- [ ] **Step 1: Write failing publication-document tests**

```python
def test_readme_documents_both_install_paths(repo):
    text = read(repo / "README.md")
    assert "/ai-psychiatry:install-framework" in text
    assert "$install-framework" in text
    assert "behavioral analogy" in text.lower()

def test_listing_has_required_cases(repo):
    text = read(repo / "docs/listing/test-cases.md")
    assert text.count("## Positive") == 5
    assert text.count("## Negative") == 3
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests.test_publication_materials -v`

Expected: FAIL because publication materials do not exist.

- [ ] **Step 3: Write accurate public documentation**

Document Claude local/marketplace install, Codex marketplace install, examples, architecture, full failure-mode coverage, disclaimer, validation, privacy (no network/data collection), known external listing requirements, and status language that distinguishes prepared/submitted/published.

- [ ] **Step 4: Validate documentation and links**

Run: `python -m unittest tests.test_publication_materials -v`

Run: `python scripts/validate_framework.py`

Expected: PASS.

- [ ] **Step 5: Commit public materials**

```powershell
git add README.md docs CHANGELOG.md LICENSE tests/test_publication_materials.py
git commit -m "docs: prepare Claude and Codex publication"
```

### Task 10: Verify, Test Installations, and Attempt Publication

**Files:**
- Modify: `docs/listing/publisher-checklist.md`
- Modify: `README.md` only if verified publication status changes.

**Interfaces:**
- Consumes: complete plugin tree and authenticated CLI state.
- Produces: proof of validation/local loading, unchanged-source hash evidence, remote readiness, and exact external blockers or publication identifiers.

- [ ] **Step 1: Run the complete automated suite**

Run: `python -m unittest discover -s tests -v`

Run: `python scripts/validate_framework.py`

Expected: all tests PASS.

- [ ] **Step 2: Run official platform validation and local smoke tests**

Run: `claude plugin validate .`

Run: `python C:\Users\Ihab\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .`

Inspect `claude plugin --help` and `codex plugin --help`, then use only documented non-destructive local add/install/test commands supported by the installed versions. Record exact output in the publisher checklist without committing credentials or machine-specific tokens.

- [ ] **Step 3: Prove source preservation and repository integrity**

Run SHA-256 over every source-pack file and compare against a pre-implementation inventory if present; otherwise verify the source directory has no Git/file timestamp changes caused by implementation. Run `git diff --check`, `git status --short`, and inspect `git diff main...HEAD --stat`.

- [ ] **Step 4: Attempt authorized submission/publication**

If installed CLIs expose authenticated submission commands, run their help/status checks and submit only when the target repository/marketplace and version are unambiguous. If submission is browser/vendor-review-only, stop at the external gate and record the exact URL, artifact, account requirement, and next action. Never report “published” from validation alone.

- [ ] **Step 5: Run verification-before-completion and commit status evidence**

Re-run the full suite after any status-doc edit, then:

```powershell
git add README.md docs/listing/publisher-checklist.md
git commit -m "docs: record plugin publication status"
```

If no tracked status changed, do not create an empty commit.

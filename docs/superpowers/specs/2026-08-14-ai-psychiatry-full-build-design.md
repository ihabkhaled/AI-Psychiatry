# AI Psychiatry Full Plugin Build Design

## Purpose

Build `AI-Psychiatry` as a distributable, skills-only plugin for Claude Code and OpenAI Codex, then apply the same framework to its own repository. The result must provide practical executive-control guidance without claiming that AI systems have psychiatric diagnoses.

The source pack at `D:\Freelance\Packs, Plans, And Prompts\AI-Psychiatry` is the requirements source. It remains unchanged. The implementation target is this repository.

## Chosen Approach

Use a hybrid package:

- A compact public `install-framework` skill drives installation, upgrades, and audits.
- Its canonical `master-prompt.md` retains the complete installation contract through progressive disclosure.
- Reusable framework assets under `.ai/` provide concrete rules, operational skills, machine-readable state, manifests, schemas, tests, context routing, and memory conventions.
- Thin agent adapters route Claude, Codex, Cursor, Copilot, and other supported agents to the same canonical framework.
- The plugin repository dogfoods those assets, proving that the package can coexist with its own packaging instructions.

This avoids both extremes: a thin wrapper that asks every installer to improvise hundreds of details, and a duplicated instruction tree whose copies drift independently.

## Source-of-Truth Model

The repository has three deliberately different truth layers:

1. `skills/install-framework/references/master-prompt.md` is the authoritative installation and maintenance specification.
2. `.ai/rules/00-master-rules.md`, `.ai/executive-function/`, and `.ai/bootstrap/` are the small runtime core for daily agent behavior.
3. Focused `.ai/rules/`, `.ai/skills/`, and `docs/ai/` files provide progressively disclosed operational and explanatory guidance.

Machine representations mirror only runtime-relevant facts. They do not become independent prose sources. Every generated or mirrored artifact records its canonical source in a manifest.

## Repository Architecture

### Plugin packaging

- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` package the Claude plugin.
- `.codex-plugin/plugin.json` packages the Codex plugin and points to the shared `skills/` tree.
- `skills/install-framework/SKILL.md` is the shared public entrypoint.
- `skills/install-framework/references/master-prompt.md` holds the large specification outside always-loaded context.
- `docs/publishing.md` documents validation, local testing, and public submission requirements.

No MCP server, hook, or app is added because the plugin needs no external tools or data.

### Dogfood runtime

- `.ai/bootstrap/` defines the mandatory pre-planning/pre-audit/pre-modification boot sequence in Markdown, JSON, TOON, and SJON.
- `.ai/executive-function/` defines the control model and state machine.
- `.ai/rules/` contains the focused rule catalog described by the master prompt.
- `.ai/skills/` contains reusable operational skills for goal locking, scope control, recovery, evidence, verification, completion, context, memory, testing, coordination, resume, and handoff.
- `.ai/context/` separates durable repository knowledge from temporary task state.
- `.ai/memory/` stores only reusable preferences, architecture, decisions, recurring problems, lessons, and failure patterns.
- `.ai/state/` contains neutral templates rather than fabricated active progress.
- `.ai/telemetry/` defines observable loop signals and thresholds without storing chain-of-thought.
- `.ai/manifests/` makes rules, skills, adapters, and knowledge machine-discoverable.
- `.ai/tests/` provides scenario-based framework and regression cases.
- `docs/ai/` explains the framework for human maintainers.

### Compatibility adapters

Root adapters (`CLAUDE.md`, `CODEX.md`, `AGENTS.md`, `GEMINI.md`, `KIMI.md`, `QWEN.md`, `DEEPSEEK.md`, `GLM.md`, and `MISTRAL.md`) remain short and point to the runtime core. Cursor, Copilot, Claude, and Codex scoped adapter directories follow the same principle.

Adapters may express platform-specific loading syntax, but may not restate the framework. Precedence is explicit: platform/system/developer instructions, repository-specific requirements, canonical framework rules, then optional guidance.

## Operational Behavior

An installing agent follows this flow:

1. Inspect existing agent instructions and generated knowledge.
2. Build an instruction graph and identify canonical sources, duplicates, conflicts, and generated files.
3. Preserve useful repository-specific semantics.
4. Install or upgrade the smallest coherent runtime core.
5. Add only useful compatibility adapters unless broader compatibility was explicitly requested.
6. Generate manifests and machine representations from canonical content.
7. Run structural, semantic, and scenario validation.
8. Report concrete proof and stop when the Definition of Done is satisfied.

Daily runtime behavior begins with bootstrap, locks the primary objective, classifies findings, limits work in progress, uses bounded retries and verification, records evidence, detects deadlock/livelock, narrows recovery strategies, and terminates after proven completion.

## State and Memory Boundaries

- Durable memory contains reusable knowledge that will save future work.
- Current task files contain temporary objective, progress, blockers, and next action.
- Telemetry contains observable counters and transitions, never hidden reasoning.
- Initial templates use `idle`, empty collections, and explicit timestamps or nulls; they never claim work occurred.
- Runtime-generated task state is ignored by Git where appropriate, while schemas and clean templates remain versioned.

## Error and Conflict Handling

- Existing useful instructions are merged semantically, not deleted because they overlap.
- Direct conflicts are documented and resolved by explicit precedence rather than silently choosing a copy.
- Broken internal links, duplicate identifiers, circular rule references, orphaned skills, schema failures, or adapter inconsistencies fail validation.
- Unsupported TOON or SJON tooling does not block structural validation; their syntax and required fields are checked locally and limitations are reported.
- Three failed attempts at the same strategy trigger escalation or a declared blocker rather than continued retries.

## Validation Strategy

Validation is layered:

1. Parse every JSON file and validate state/config files against checked-in schemas.
2. Validate Claude and Codex plugin manifests using their available official/local tooling.
3. Check all Markdown links and canonical-source references.
4. Verify manifest completeness, unique IDs, priorities, load conditions, and absence of circular references.
5. Enforce thin-adapter and boot-context size budgets.
6. Confirm every declared skill and rule exists and every required frontmatter field is present.
7. Run scenario cases for attention drift, nested investigation, retry loops, critic loops, context reload loops, scope drift, livelock, and completion avoidance.
8. Run repository integrity checks and inspect the final Git diff.

Validation scripts use only the Python standard library so plugin consumers do not inherit a package dependency.

## Delivery Scope

The full build includes plugin manifests, the public installer skill and master reference, the useful target `.ai/` architecture, adapters, human documentation, validation scripts, and framework tests. Files are split by responsibility but omitted when they would be empty or meaningless.

Public-listing artwork, screenshots, support/legal URLs, and actual marketplace submission remain deferred because they require publisher assets or external actions. The build will document those requirements without inventing them.

## Acceptance Criteria

- Claude and Codex consume one shared install skill.
- The complete master specification is present and progressively disclosed.
- The dogfood runtime covers objective locking, scope, attention, retry/verification/critic budgets, evidence, recovery, context, memory, communication, progress, multi-agent control, completion, and termination.
- Routers are thin and consistent; canonical knowledge is not duplicated.
- Markdown, JSON, TOON, SJON, schemas, and manifests are present where operationally useful.
- Initial state contains no fake task history or chain-of-thought.
- Framework scenarios and structural validators pass.
- Plugin manifests pass available platform validation.
- The README explains installation, invocation, architecture, validation, and publishing links accurately.
- The source pack is unchanged and the destination repository contains the complete implementation.

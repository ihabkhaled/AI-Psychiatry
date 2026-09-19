# AI Psychiatry Full Plugin Build Design

## Purpose

Build and publish `AI-Psychiatry` as a skills-only plugin for both Claude Code and OpenAI Codex, then apply the same framework to its own repository. Each plugin installs the complete system derived from the master prompt: skills, rules, agent adapters, context, memory, state, machine formats, tests, and documentation. The result must provide practical executive-control guidance without claiming that AI systems have psychiatric diagnoses.

The product name deliberately uses psychiatry as branding. Human terms such as ADHD, OCD, executive dysfunction, perseveration, distraction, and perfectionism are explanatory analogies for observable agent failure modes—not diagnoses or claims about consciousness. Operational rules use engineering terms and map those analogies to measurable behaviors such as objective switching, repeated verification, recursive task spawning, context reload loops, unsupported claims, and failure to terminate.

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

1. `skills/all-the-medicine/references/skills/install-framework/references/master-prompt.md` is the authoritative installation and maintenance specification.
2. `.ai/rules/00-master-rules.md`, `.ai/executive-function/`, and `.ai/bootstrap/` are the small runtime core for daily agent behavior.
3. Focused `.ai/rules/`, `.ai/skills/`, and `docs/ai/` files provide progressively disclosed operational and explanatory guidance.

Machine representations mirror only runtime-relevant facts. They do not become independent prose sources. Every generated or mirrored artifact records its canonical source in a manifest.

## Repository Architecture

### Plugin packaging

- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` package the Claude plugin.
- `.codex-plugin/plugin.json` packages the Codex plugin and points to the shared `skills/` tree.
- `skills/all-the-medicine/references/skills/install-framework/install-framework.md` is the shared public entrypoint.
- `skills/all-the-medicine/references/skills/install-framework/references/master-prompt.md` holds the large specification outside always-loaded context.
- `docs/publishing.md` documents validation, local testing, and public submission requirements.
- Public listing metadata, starter prompts, positive and negative evaluation cases, release notes, support information, and publisher-verification requirements are checked in where each marketplace accepts repository-hosted materials.

No MCP server, hook, or app is added because the plugin needs no external tools or data. Claude and Codex packages expose the same capability and installation semantics even where their marketplace manifest formats differ.

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

The rule and skill catalog must cover every normative requirement in the master prompt, including hallucination/evidence control; ADHD-style distraction, attention switching, and task abandonment; OCD-style repeated checking, perfectionism, and compulsive verification; recursive thinking and nested-job limits; rabbit holes; semantic repetition; retry, critic, and verification budgets; context reload loops; deadlock, livelock, and strategy oscillation; fake progress/background work; multi-agent coordination; destructive-action safety; and completion avoidance. A traceability manifest maps all numbered master-prompt sections to their implementing rule, skill, adapter, test, or documentation artifact so no section disappears during decomposition.

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
8. Verify master-prompt traceability: every numbered normative section has an implementation or an explicit packaging/documentation classification.
9. Run repository integrity checks and inspect the final Git diff.

Validation scripts use only the Python standard library so plugin consumers do not inherit a package dependency.

## Delivery Scope

The full build includes plugin manifests, the public installer skill and master reference, the useful target `.ai/` architecture, adapters, human documentation, validation scripts, framework tests, prompt-to-artifact traceability, and marketplace submission materials. Files are split by responsibility but omitted when they would be empty or meaningless.

Publication is part of the goal. The implementation will validate and locally test both packages, prepare complete listing materials, configure the repository marketplace metadata, and execute submission or publication commands when supported by installed tooling and existing authenticated accounts. Vendor review, account verification, legal/support URLs owned by the publisher, and marketplace approval are external gates; if any gate cannot be completed from the workspace, the final report must identify the exact remaining action rather than describing a publish-ready package as already published.

## Acceptance Criteria

- Claude and Codex consume one shared install skill.
- Claude and Codex plugin packages are submitted/published through their supported channels when authentication and platform tooling permit; otherwise the precise external gate and ready-to-submit artifact are proven.
- The complete master specification is present and progressively disclosed.
- Every normative master-prompt section is represented in the traceability manifest and covered by an operational or explanatory artifact.
- The dogfood runtime covers objective locking, scope, attention, retry/verification/critic budgets, evidence, recovery, context, memory, communication, progress, multi-agent control, completion, and termination.
- Named failure-mode coverage includes hallucination, distraction/ADHD analogy, compulsive checking/OCD analogy, nested jobs, recursive thinking, rabbit holes, deadlock, livelock, context reload loops, fake progress, perfectionism, scope drift, and completion avoidance.
- Routers are thin and consistent; canonical knowledge is not duplicated.
- Markdown, JSON, TOON, SJON, schemas, and manifests are present where operationally useful.
- Initial state contains no fake task history or chain-of-thought.
- Framework scenarios and structural validators pass.
- Plugin manifests pass available platform validation.
- The README explains installation, invocation, architecture, analogy terminology, validation, publication status, and publishing links accurately.
- The source pack is unchanged and the destination repository contains the complete implementation.

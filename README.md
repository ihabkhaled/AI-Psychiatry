# AI Psychiatry

AI Psychiatry is a cross-platform executive-control plugin for Claude Code and OpenAI Codex. It adds semantic anti-bypass enforcement and balances underthinking against overthinking so agents investigate enough, execute, prove the outcome, and stop.

> “Psychiatry” is branding and behavioral analogy. ADHD, OCD, executive dysfunction, and related human terms describe analogous observable failure patterns; they are not diagnoses of AI systems or claims about consciousness.

## Install

### Claude Code

Local validation and use:

```powershell
claude plugin validate .
claude --plugin-dir .
```

Marketplace installation after publication:

```text
/plugin marketplace add ihabkhaled/AI-Psychiatry
/plugin install ai-psychiatry@ihabkhaled-ai
/ai-psychiatry:install-framework
```

### OpenAI Codex

```powershell
codex plugin marketplace add ihabkhaled/AI-Psychiatry
```

Install **AI Psychiatry** from the Plugins Directory, then invoke:

```text
$install-framework
```

## Use the controls directly

The plugin exposes focused skills in both platforms. Claude uses `/ai-psychiatry:<skill>`; Codex uses `$<skill>`.

| Behavior | Skill |
|---|---|
| Select the correct controller | `executive-control` |
| ADHD-like attention drift analogy | `attention-reset` |
| Analysis paralysis and rabbit holes | `stop-overthinking` |
| OCD-like repetitive checking analogy | `stop-compulsive-verification` |
| Box-inside-box tasks and nested agents | `flatten-recursive-investigation` |
| Unsupported repository claims | `evidence-gate` |
| Repeating activity or no valid action | `recover-from-deadlock-livelock` |
| Perfectionism and refusal to finish | `completion-gate` |
| Literal-compliance loopholes | `loophole-hunter`, `anti-gaming` |
| Fake activity presented as progress | `false-progress-detector` |
| False DONE or BLOCKED claims | `completion-evidence`, `blocker-validator` |
| Hidden causal nesting | `hidden-recursion-detector` |
| Renamed equivalent retries | `strategy-laundering-detector` |
| Disguised scope expansion or parking | `scope-laundering-detector` |
| Memory poisoning and context starvation | `memory-validator`, `context-balance` |
| Premature action and shallow reasoning | `underthinking-detector`, `investigation-floor` |
| Sufficient-reasoning decision control | `reasoning-balance`, `decision-readiness`, `evidence-floor` |
| Root-cause and debugging evidence | `root-cause-validator` |
| Controlled budget exception | `executive-override` |
| Conflicting instruction sources | `rule-conflict-resolver` |

Example:

```text
/ai-psychiatry:flatten-recursive-investigation
$stop-compulsive-verification
```

## What it installs

The shared installer preserves repository-specific instructions and adds a compact `.ai/` runtime with 56 focused rules, 47 operational skills, 28 public plugin skills, semantic policies, thin agent adapters, context and durable memory, JSON/TOON/SJON state, schemas, manifests, and scenario tests. The original master prompt and complementary loophole/underthinking prompts are progressively disclosed from `skills/install-framework/references/`.

Coverage includes hallucination, attention drift, ADHD-style distraction analogy, OCD-style compulsive-checking analogy, underthinking, overthinking, hidden recursion, strategy and scope laundering, false progress/completion/blockers, memory poisoning, context starvation, critic suppression, deadlock, livelock, and completion avoidance. Guidance is indexed in [AI framework guidance](docs/ai/README.md); semantic loopholes are cataloged [here](.ai/guides/loophole-catalog.md).

## Validate

```powershell
python -m unittest discover -s tests -v
python scripts/validate_framework.py
claude plugin validate .
python C:\\Users\\Ihab\\.codex\\skills\\.system\\plugin-creator\\scripts\\validate_plugin.py .
```

See [architecture](docs/ai/architecture.md), [publishing](docs/publishing.md), [privacy](PRIVACY.md), [terms](TERMS.md), [support](SUPPORT.md), and [release notes](docs/listing/release-notes.md).

## Privacy

The plugin is skills-only. It adds no MCP server, network service, analytics, or data collection.

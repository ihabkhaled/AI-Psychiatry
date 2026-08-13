# AI Psychiatry

AI Psychiatry is a cross-platform executive-control plugin for Claude Code and OpenAI Codex. It installs the complete prompt-derived system: goal locking, attention and scope control, anti-overthinking, evidence and hallucination control, bounded retries and verification, nested-job limits, deadlock/livelock recovery, context, memory, concise communication, testing, and proof-based completion.

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

Example:

```text
/ai-psychiatry:flatten-recursive-investigation
$stop-compulsive-verification
```

## What it installs

The shared installer preserves repository-specific instructions and adds a compact `.ai/` runtime with 41 focused rules, 28 operational skills, thin agent adapters, context and durable memory, JSON/TOON/SJON state, schemas, manifests, and scenario tests. The complete master prompt is progressively disclosed from `skills/install-framework/references/master-prompt.md`.

Coverage includes hallucination, attention drift, ADHD-style distraction analogy, OCD-style compulsive-checking analogy, recursive thinking, nested jobs, rabbit holes, retry and critic loops, deadlock, livelock, context reload loops, fake progress, perfectionism, scope drift, and completion avoidance. The substantive intervention files are indexed in [AI framework guidance](docs/ai/README.md); the complete 25-mode catalog is [here](.ai/guides/failure-mode-catalog.md).

## Validate

```powershell
python -m unittest discover -s tests -v
python scripts/validate_framework.py
claude plugin validate .
python C:\\Users\\Ihab\\.codex\\skills\\.system\\plugin-creator\\scripts\\validate_plugin.py .
```

See [architecture](docs/ai/architecture.md), [publishing](docs/publishing.md), and [release notes](docs/listing/release-notes.md).

## Privacy

The plugin is skills-only. It adds no MCP server, network service, analytics, or data collection.

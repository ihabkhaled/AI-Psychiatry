# AI Psychiatry

AI Psychiatry is a cross-platform executive-control plugin for Claude Code and OpenAI Codex. It adds semantic anti-bypass enforcement and balances underthinking against overthinking so agents investigate enough, execute, prove the outcome, and stop.

> “Psychiatry” is branding and behavioral analogy. ADHD, OCD, executive dysfunction, and related human terms describe analogous observable failure patterns; they are not diagnoses of AI systems or claims about consciousness.

## Install

One line, no clone. It installs for every one of Claude Code, Codex and Cursor it finds; re-run to update.

```bash
curl -fsSL https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.sh | sh
```

```powershell
irm https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.ps1 | iex
```

`--repo PATH` (`-Repo`) installs into one project only; `--uninstall` (`-Uninstall`) removes everything it added and restores edited files byte for byte.

Claude Code without the script:

```bash
claude plugin marketplace add https://github.com/ihabkhaled/AI-Psychiatry.git
claude plugin install ai-psychiatry@ihabkhaled-ai
```

In the VS Code extension: `/plugins` -> Marketplaces -> add the URL above -> install. Try it for one session only: `claude --plugin-dir .` from a checkout.

## One skill, one command, always on

AI-Psychiatry is **one skill**, `all-the-medicine`, and it is also the **one command**. You normally type nothing: it is always on.

| Platform | Always on via | The one command |
|---|---|---|
| Claude Code | SessionStart hook | `/ai-psychiatry:all-the-medicine` |
| Codex | a marked block in `~/.codex/AGENTS.md` | `$all-the-medicine` |
| Cursor | an `alwaysApply` rule in `~/.cursor/rules/` | `/all-the-medicine` |

The always-on contract is one file, `skills/all-the-medicine/references/always-on.md`; the hook, the Codex block and the Cursor rule all print it.

Every control below is a **reference inside the one skill** (`skills/all-the-medicine/references/skills/<name>/<name>.md`), selected one at a time when its behavior is observed - never a separate skill, so no platform lists it as a separate command. To use one deliberately, name it: "apply stop-overthinking".

| Behavior | Control |
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
| Maximum autonomous execution until proven completion | `never-stop` |
| Verbose, indirect, repetitive answers or questions | `direct-communication` |
| Installing the `.ai/` framework into a repository | `install-framework` - ask "install the AI-Psychiatry framework" |

**NeverStop** stays explicit: relentless autonomous execution runs only when you ask for it ("never stop until it's done"), inside existing permissions, and stops at proven completion or a genuine hard approval gate.

## What it installs

The shared installer preserves repository-specific instructions and adds a compact `.ai/` runtime with 58 focused rules, 49 operational skills, 31 public plugin skills, semantic policies, thin agent adapters, context and durable memory, JSON/TOON/SJON state, schemas, manifests, and scenario tests. The original master prompt and complementary loophole/underthinking prompts are progressively disclosed from `skills/all-the-medicine/references/skills/install-framework/references/`.

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

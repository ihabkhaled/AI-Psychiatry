# AI Psychiatry

AI-PSYCHIATRY IS NOT OPTIONAL. Always-on executive control for Claude Code, Codex and Cursor: it stops agents from skipping evidence, drifting, looping, gaming the rules or faking "done". One skill, `all-the-medicine`, always on, nothing to type.

> "Psychiatry" is branding and behavioral analogy. ADHD, OCD and related human terms describe analogous, observable failure patterns; they are not diagnoses of AI systems or claims about consciousness.

## Get it in 30 seconds

macOS / Linux / Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.ps1 | iex
```

It installs for every one of Claude Code, Codex and Cursor it finds. Re-run to update. `--uninstall` (`-Uninstall`) removes everything it added, restores edited files byte for byte and deletes its download cache.

## Explicit form, per platform

| Platform | Install | Always on via | The one command |
|---|---|---|---|
| Claude Code | `claude plugin marketplace add https://github.com/ihabkhaled/AI-Psychiatry.git`, then `claude plugin install ai-psychiatry@ihabkhaled-ai` | `SessionStart` and `UserPromptSubmit` hooks | `/ai-psychiatry:all-the-medicine` |
| Codex | `sh install.sh --codex` (`.\install.ps1 -Codex`) | a marked block in `~/.codex/AGENTS.md` | `$all-the-medicine` |
| Cursor | `sh install.sh --cursor` (`.\install.ps1 -Cursor`) | an `alwaysApply` rule in `~/.cursor/rules/` | `/all-the-medicine` |

You normally type nothing. The contract is one file, `skills/all-the-medicine/references/always-on.md`; the session hook, the Codex block and the Cursor rule all print it, and a short reminder rides along with every prompt on Claude Code.

<details>
<summary>Other routes</summary>

- One project only: `sh install.sh --repo PATH` (`-Repo PATH`).
- A pinned branch or tag: `--ref REF` (`-Ref REF`).
- VS Code extension: `/plugins`, Marketplaces, add `https://github.com/ihabkhaled/AI-Psychiatry.git`, install.
- Try it for one session: `claude --plugin-dir .` from a checkout.

</details>

<details>
<summary>The controls inside the one skill</summary>

Each control is a reference file inside the one skill (`skills/all-the-medicine/references/skills/<name>/<name>.md`), selected one at a time when its behavior is observed; none is a separate skill or command. To use one deliberately, name it: "apply stop-overthinking".

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

`never-stop` stays explicit: relentless autonomous execution runs only when you ask for it, inside existing permissions, and stops at proven completion or a genuine hard approval gate.

</details>

<details>
<summary>What the framework installs</summary>

The shared installer preserves repository-specific instructions and adds a compact `.ai/` runtime with 59 focused rules, 49 operational skills, 31 public plugin skills, semantic policies, thin agent adapters, context and durable memory, JSON/TOON/SJON state, schemas, manifests, and scenario tests. Guidance is indexed in [AI framework guidance](docs/ai/README.md); semantic loopholes are cataloged [here](.ai/guides/loophole-catalog.md); the docs start at [docs/README.md](docs/README.md) and the wiki at [docs/wiki/index.md](docs/wiki/index.md).

</details>

## Developing

```bash
python -m unittest discover -s tests
python scripts/validate_framework.py
python scripts/psychiatry_version.py check --base origin/main
claude plugin validate .
```

A change to a shipped path must raise the version: `python scripts/psychiatry_version.py next`, then `bump ... --date YYYY-MM-DD` ([rule 58](.ai/rules/58-version-discipline.md)). Never run `scripts/build_release_manifests.py` wholesale.

See [publishing](docs/publishing.md), [privacy](PRIVACY.md), [terms](TERMS.md), [support](SUPPORT.md) and [release notes](docs/listing/release-notes.md). The plugin is skills plus two local hook scripts that only print text. It adds no MCP server, network service, analytics, or data collection.

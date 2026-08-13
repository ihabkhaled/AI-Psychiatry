"""Regenerate AI-Psychiatry 0.3.0 catalogs from checked-in artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.3.0"
NEW_SKILLS = [
    "loophole-hunter", "framework-red-team", "anti-gaming", "false-progress-detector",
    "blocker-validator", "hidden-recursion-detector", "strategy-laundering-detector",
    "scope-laundering-detector", "completion-evidence", "memory-validator", "context-balance",
    "underthinking-detector", "reasoning-balance", "investigation-floor", "decision-readiness",
    "root-cause-validator", "evidence-floor", "executive-override", "rule-conflict-resolver",
]
NEW_GUIDES = [
    "semantic-compliance.md", "loophole-catalog.md", "underthinking.md", "reasoning-balance.md",
    "context-starvation.md", "sufficient-reasoning.md", "executive-override-conflicts.md",
]


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write(relative: str, value: dict) -> None:
    (ROOT / relative).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")


def sha(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest().upper()


def main() -> None:
    rules = load(".ai/manifests/rules.json")
    existing = {item["id"]: item for item in rules["rules"]}
    for number in range(41, 56):
        name = next((path.name for path in (ROOT / ".ai/rules").glob(f"{number:02d}-*.md")), None)
        if name is None:
            raise FileNotFoundError(f"rule {number}")
        existing[f"rule-{number:02d}"] = {
            "id": f"rule-{number:02d}",
            "path": f".ai/rules/{name}",
            "priority": 59 - (number - 41),
            "load_when": "on_demand",
            "canonical_source": "skills/install-framework/references/loophole-enhancement-prompts.md",
            "prompt_sections": [],
        }
    rules["rules"] = [existing[f"rule-{number:02d}"] for number in range(56)]
    write(".ai/manifests/rules.json", rules)

    manifest = load(".ai/manifests/skills.json")
    installed = {item["name"]: item for item in manifest["skills"]}
    for index, name in enumerate(NEW_SKILLS, start=28):
        rule_number = 41 + min(index - 28, 14)
        installed[name] = {
            "id": f"skill-{index:02d}", "name": name, "path": f".ai/skills/{name}/SKILL.md",
            "purpose": f"Semantic {name.replace('-', ' ')} controller", "priority": 98,
            "scope": "repository", "loadCondition": "on-semantic-risk", "load_when": "on-semantic-risk",
            "canonical_rules": [f"rule-{rule_number:02d}"], "version": VERSION,
        }
    for item in installed.values():
        item["version"] = VERSION
    manifest["version"] = VERSION
    manifest["skills"] = sorted(installed.values(), key=lambda item: int(item["id"].split("-")[-1]))

    public = {item["name"]: item for item in manifest["plugin_skills"]}
    for offset, name in enumerate(NEW_SKILLS, start=9):
        public[name] = {
            "id": f"plugin-skill-{offset:02d}", "name": name, "path": f"skills/{name}/SKILL.md",
            "purpose": f"Apply {name.replace('-', ' ')} controls", "priority": 98, "scope": "plugin",
            "loadCondition": "on_demand", "version": VERSION,
        }
    for item in public.values():
        item["version"] = VERSION
    manifest["plugin_skills"] = sorted(public.values(), key=lambda item: int(item["id"].split("-")[-1]))
    write(".ai/manifests/skills.json", manifest)

    knowledge = load(".ai/manifests/knowledge.json")
    guides = {item["path"]: item for item in knowledge["guides"]}
    for name in NEW_GUIDES:
        guides[f".ai/guides/{name}"] = {"path": f".ai/guides/{name}", "load_when": "on-semantic-risk"}
    knowledge["guides"] = list(guides.values())
    write(".ai/manifests/knowledge.json", knowledge)

    install = load(".ai/manifests/install.json")
    install["version"] = 2
    install["release"] = VERSION
    install["public_skills"] = [item["name"] for item in manifest["plugin_skills"]]
    install["layers"] = ["rules", "skills", "guides", "policies", "context", "memory", "state", "telemetry", "manifests", "tests"]
    install["supplemental_prompts"] = [
        {"path": "skills/install-framework/references/loophole-enhancement-prompts.md", "sha256": sha("skills/install-framework/references/loophole-enhancement-prompts.md")},
        {"path": "skills/install-framework/references/underthinking-reasoning-balance-prompt.md", "sha256": sha("skills/install-framework/references/underthinking-reasoning-balance-prompt.md")},
    ]
    write(".ai/manifests/install.json", install)

    for relative in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        plugin = load(relative)
        plugin["version"] = VERSION
        plugin["description"] = "Semantic executive control for loopholes, underthinking, overthinking, evidence, recursion, context, memory, and reliable delivery."
        plugin["keywords"] = list(dict.fromkeys(plugin.get("keywords", []) + ["semantic-compliance", "underthinking", "anti-gaming"]))
        if "interface" in plugin:
            plugin["interface"]["longDescription"] = "Detects semantic bypasses, false progress/completion/blockers, hidden recursion, strategy and scope laundering, memory/context corruption, underthinking, overthinking, and missing evidence."
            plugin["interface"]["defaultPrompt"] = [
                "Audit this task for AI-Psychiatry loopholes and semantic bypasses.",
                "Balance underthinking and overthinking using sufficient reasoning.",
                "Validate completion evidence, blockers, recursion, scope, and progress.",
            ]
        write(relative, plugin)

    marketplace = load(".claude-plugin/marketplace.json")
    marketplace["plugins"][0]["version"] = VERSION
    marketplace["plugins"][0]["description"] = "Semantic anti-bypass and sufficient-reasoning controls for coding agents."
    marketplace["plugins"][0]["tags"] = list(dict.fromkeys(marketplace["plugins"][0]["tags"] + ["semantic-compliance", "underthinking", "anti-gaming"]))
    write(".claude-plugin/marketplace.json", marketplace)
    print("Regenerated 0.3.0 release manifests")


if __name__ == "__main__":
    main()

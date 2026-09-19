from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Issue:
    code: str
    path: str
    message: str


LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
REPO_ROOT = Path(__file__).resolve().parents[1]
COUNT_SENTENCE = re.compile(
    r"(\d+) focused rules, (\d+) operational skills, (\d+) public plugin skills"
)
REQUIRED_NEW_SKILLS = ("never-stop", "all-the-medicine")



def public_skill_path(name: str) -> str:
    """Where a public skill lives. There is ONE plugin skill, all-the-medicine;
    every other public skill is a reference inside it, never a skill of its own,
    so no platform lists it as a separate command."""
    if name == "all-the-medicine":
        return "skills/all-the-medicine/SKILL.md"
    return f"skills/all-the-medicine/references/skills/{name}/{name}.md"

def validate_traceability(root: Path) -> list[Issue]:
    root = Path(root).resolve()
    prompt_path = root / "skills/all-the-medicine/references/skills/install-framework/references/master-prompt.md"
    trace_path = root / ".ai/manifests/prompt-traceability.json"
    if not prompt_path.exists() or not trace_path.exists():
        return [Issue("traceability-missing", str(trace_path.relative_to(root)), "canonical prompt or traceability manifest missing")]
    prompt_bytes = prompt_path.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    headings = {number: title.rstrip("\r") for number, title in re.findall(r"^# (\d+)\. (.+)$", prompt, flags=re.MULTILINE)}
    trace = json.loads(trace_path.read_text(encoding="utf-8"))
    issues: list[Issue] = []
    digest = hashlib.sha256(prompt_bytes).hexdigest().upper()
    if trace.get("canonical_sha256") != digest:
        issues.append(Issue("traceability-hash", str(trace_path.relative_to(root)), "canonical prompt hash is stale"))
    sections = trace.get("sections", {})
    if set(sections) != set(headings):
        issues.append(Issue("traceability-gap", str(trace_path.relative_to(root)), "section IDs do not match canonical prompt"))
    for number, title in headings.items():
        entry = sections.get(number, {})
        if entry.get("title") != title:
            issues.append(Issue("traceability-stale", str(trace_path.relative_to(root)), f"section {number} title differs"))
        for artifact in entry.get("artifacts", []):
            if not (root / artifact).exists():
                issues.append(Issue("traceability-artifact", artifact, f"declared by section {number}"))
    return issues


def validate(root: Path, package_required: bool = True) -> list[Issue]:
    root = Path(root).resolve()
    issues: list[Issue] = []
    for path in root.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(Issue("invalid-json", str(path.relative_to(root)), str(exc)))
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for target in LINK.findall(text):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if root not in resolved.parents and resolved != root:
                issues.append(Issue("unsafe-link", str(path.relative_to(root)), target))
            elif not resolved.exists():
                issues.append(Issue("broken-link", str(path.relative_to(root)), target))
    if not package_required:
        return issues
    required = [
        ".claude-plugin/plugin.json", ".codex-plugin/plugin.json",
        "skills/all-the-medicine/references/skills/install-framework/install-framework.md", ".ai/manifests/rules.json",
        ".ai/manifests/skills.json", ".ai/manifests/agents.json",
        ".ai/manifests/prompt-traceability.json"
    ]
    for item in required:
        if not (root / item).exists():
            issues.append(Issue("missing-required", item, "required package artifact"))
    issues.extend(validate_traceability(root))
    try:
        rules = json.loads((root / ".ai/manifests/rules.json").read_text(encoding="utf-8"))["rules"]
        ids = [item["id"] for item in rules]
        if len(ids) != len(set(ids)):
            issues.append(Issue("duplicate-id", ".ai/manifests/rules.json", "rule IDs must be unique"))
        for item in rules:
            if not (root / item["path"]).exists():
                issues.append(Issue("missing-declared-path", item["path"], item["id"]))
    except (OSError, KeyError, json.JSONDecodeError):
        pass
    try:
        agents = json.loads((root / ".ai/manifests/agents.json").read_text(encoding="utf-8"))["agents"]
        for item in agents:
            path = root / item["path"]
            if path.exists() and path.stat().st_size > 1500:
                issues.append(Issue("adapter-budget", item["path"], "exceeds 1500 bytes"))
    except (OSError, KeyError, json.JSONDecodeError):
        pass
    state = root / ".ai/state/active-task.json"
    if state.exists():
        data = json.loads(state.read_text(encoding="utf-8"))
        if data.get("status") != "idle" or data.get("objective") is not None or data.get("history") != []:
            issues.append(Issue("fake-state", str(state.relative_to(root)), "versioned task state must be neutral"))

    issues.extend(validate_never_stop_and_all_the_medicine(root))
    return issues


def validate_never_stop_and_all_the_medicine(root: Path) -> list[Issue]:
    """Validate the never-stop / all-the-medicine additions: presence, manifests, generation, versions."""
    issues: list[Issue] = []

    for name in REQUIRED_NEW_SKILLS:
        for rel in (public_skill_path(name), f".ai/skills/{name}/SKILL.md"):
            path = root / rel
            if not path.exists():
                issues.append(Issue("missing-required", rel, "required superpower skill"))
                continue
            text = path.read_text(encoding="utf-8")
            if "## Stop condition" not in text:
                issues.append(Issue("missing-stop-condition", rel, "superpower skill must declare a stop condition"))

    for rule in ("56-never-stop-relentless-execution.md", "57-all-the-medicine.md"):
        if not (root / ".ai/rules" / rule).exists():
            issues.append(Issue("missing-required", f".ai/rules/{rule}", "required superpower rule"))

    try:
        skills = json.loads((root / ".ai/manifests/skills.json").read_text(encoding="utf-8"))
        for section in ("skills", "plugin_skills"):
            entries = skills[section]
            names = [item["name"] for item in entries]
            if len(names) != len(set(names)):
                issues.append(Issue("duplicate-skill-name", ".ai/manifests/skills.json", f"duplicate name in {section}"))
            ids = [item["id"] for item in entries]
            if len(ids) != len(set(ids)):
                issues.append(Issue("duplicate-skill-id", ".ai/manifests/skills.json", f"duplicate id in {section}"))
            for item in entries:
                if not (root / item["path"]).exists():
                    issues.append(Issue("missing-declared-path", item["path"], item.get("id", item.get("name", ""))))
        # One plugin skill; the rest are references inside it (see public_skill_path).
        plugin_dirs = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
        refs = root / "skills/all-the-medicine/references/skills"
        if refs.is_dir():
            plugin_dirs |= {p.name for p in refs.iterdir() if p.is_dir()}
        stray = sorted(str(p.relative_to(root)) for p in (root / "skills").rglob("SKILL.md")
                       if p != root / "skills/all-the-medicine/SKILL.md")
        if stray or sorted(p.name for p in (root / "skills").iterdir() if p.is_dir()) != ["all-the-medicine"]:
            issues.append(Issue("second-plugin-skill", "skills/",
                                f"exactly one plugin skill may exist; found extra {stray or 'directories'}"))
        manifest_plugin_names = {item["name"] for item in skills["plugin_skills"]}
        if plugin_dirs != manifest_plugin_names:
            issues.append(Issue(
                "skill-inventory-drift", ".ai/manifests/skills.json",
                f"skills/ directories {sorted(plugin_dirs)} do not match plugin_skills {sorted(manifest_plugin_names)}",
            ))
        lowercase_names = [name.lower() for name in plugin_dirs]
        if len(lowercase_names) != len(set(lowercase_names)):
            issues.append(Issue("unvalidated-alias", "skills/", "case-insensitive duplicate skill directory names"))
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        issues.append(Issue("invalid-manifest", ".ai/manifests/skills.json", str(exc)))

    try:
        install = json.loads((root / ".ai/manifests/install.json").read_text(encoding="utf-8"))
        claude = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        codex = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        versions = {
            "install.release": install.get("release"),
            "claude.version": claude.get("version"),
            "codex.version": codex.get("version"),
            "marketplace.version": marketplace.get("plugins", [{}])[0].get("version"),
        }
        if len(set(versions.values())) > 1:
            issues.append(Issue("version-mismatch", ".claude-plugin/plugin.json", f"inconsistent release versions: {versions}"))
    except (OSError, KeyError, IndexError, json.JSONDecodeError) as exc:
        issues.append(Issue("invalid-manifest", ".claude-plugin/plugin.json", str(exc)))

    readme = root / "README.md"
    if readme.exists():
        try:
            rules_count = len(json.loads((root / ".ai/manifests/rules.json").read_text(encoding="utf-8"))["rules"])
            skills = json.loads((root / ".ai/manifests/skills.json").read_text(encoding="utf-8"))
            operational_count = len(skills["skills"])
            plugin_count = len(skills["plugin_skills"])
            match = COUNT_SENTENCE.search(readme.read_text(encoding="utf-8"))
            if not match:
                issues.append(Issue("readme-counts-missing", "README.md", "no rules/skills count sentence found"))
            else:
                declared = tuple(int(value) for value in match.groups())
                actual = (rules_count, operational_count, plugin_count)
                if declared != actual:
                    issues.append(Issue("readme-counts-stale", "README.md", f"declared {declared} != actual {actual}"))
        except (OSError, KeyError, json.JSONDecodeError) as exc:
            issues.append(Issue("invalid-manifest", "README.md", str(exc)))

    gates_path = root / ".ai/policies/approval-gates.json"
    if gates_path.exists():
        gates = json.loads(gates_path.read_text(encoding="utf-8"))
        if gates.get("permissionBypass") is not False:
            issues.append(Issue("permission-bypass-allowed", ".ai/policies/approval-gates.json", "hard-gate policy must forbid permission bypass"))

    for generated_path, marker in (
        ("skills/all-the-medicine/references/all-skills-compiled.md", "GENERATED"),
        ("skills/all-the-medicine/references/all-rules-compiled.md", "GENERATED"),
        (".ai/rules/57-all-the-medicine.md", "GENERATED COMPOSITE RULE"),
    ):
        full = root / generated_path
        if full.exists() and marker not in full.read_text(encoding="utf-8"):
            issues.append(Issue("generated-artifact-unmarked", generated_path, f"missing '{marker}' marker"))

    if root == REPO_ROOT:
        sys.path.insert(0, str(REPO_ROOT))
        try:
            from scripts.build_all_the_medicine import build as build_all_the_medicine, check as check_all_the_medicine

            outputs = build_all_the_medicine()
            for stale in check_all_the_medicine(outputs):
                issues.append(Issue("all-the-medicine-stale", "skills/all-the-medicine/references/", stale))
        except (FileNotFoundError, ValueError, KeyError, ImportError) as exc:
            issues.append(Issue("all-the-medicine-build-failed", "scripts/build_all_the_medicine.py", str(exc)))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the AI Psychiatry plugin and framework")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    issues = validate(args.root)
    for issue in issues:
        print(f"[{issue.code}] {issue.path}: {issue.message}")
    if issues:
        print(f"Framework validation failed: {len(issues)} issue(s)")
        return 1
    print("Framework validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

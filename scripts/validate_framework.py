from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Issue:
    code: str
    path: str
    message: str


LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def validate_traceability(root: Path) -> list[Issue]:
    root = Path(root).resolve()
    prompt_path = root / "skills/install-framework/references/master-prompt.md"
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
        "skills/install-framework/SKILL.md", ".ai/manifests/rules.json",
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

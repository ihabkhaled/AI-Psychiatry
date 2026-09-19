"""Generate prompt-section traceability from the canonical master prompt."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "skills/all-the-medicine/references/skills/install-framework/references/master-prompt.md"
OUTPUT = ROOT / ".ai/manifests/prompt-traceability.json"


SKILL_SECTIONS = {
    104: "context-compression",
    105: "resume-task",
    106: "handoff-task",
    107: "direct-communication",
    108: "executive-function",
    109: "goal-lock",
    110: "scope-guard",
    111: "bounded-investigation",
    112: "loop-detector",
    113: "deadlock-recovery",
    114: "livelock-recovery",
    115: "progress-audit",
    116: "evidence-gate",
    117: "verification-controller",
    118: "critic-controller",
    119: "completion-gate",
    120: "failure-learning",
    121: "knowledge-maintainer",
    122: "repository-map-update",
}


SPECIAL = {
    0: ["docs/ai/human-behavior-analogies.md", ".ai/guides/failure-mode-catalog.md"],
    8: [".ai/README.md", ".ai/manifests/install.json"],
    10: [".ai/bootstrap/boot.md"],
    18: [".ai/guides/recursive-investigation.md"],
    19: [".ai/guides/rabbit-holes-scope-drift.md"],
    20: [".ai/guides/deadlock-livelock.md"],
    23: [".ai/guides/compulsive-verification.md"],
    24: [".ai/guides/compulsive-verification.md"],
    25: [".ai/guides/perfectionism-completion.md"],
    26: [".ai/guides/hallucination-evidence.md"],
    27: [".ai/guides/hallucination-evidence.md"],
    29: [".ai/guides/overthinking-analysis-paralysis.md"],
    32: [".ai/guides/deadlock-livelock.md"],
    33: [".ai/guides/deadlock-livelock.md"],
    34: [".ai/guides/deadlock-livelock.md"],
    38: [".ai/executive-function/state-machine.json"],
    46: [".ai/context/context-index.json"],
    52: [".ai/memory/index.md"],
    59: [".ai/executive-function/executive-function.json"],
    60: [".ai/executive-function/executive-function.toon"],
    61: [".ai/executive-function/executive-function.sjon"],
    90: [".ai/guides/nested-job-control.md"],
    91: [".ai/guides/nested-job-control.md"],
    92: [".ai/guides/nested-job-control.md"],
    93: [".ai/guides/nested-job-control.md"],
    94: [".ai/guides/nested-job-control.md"],
    95: [".ai/guides/nested-job-control.md"],
    96: [".ai/guides/nested-job-control.md"],
    97: ["docs/ai/human-behavior-analogies.md", ".ai/guides/attention-drift.md", ".ai/guides/compulsive-verification.md", ".ai/guides/overthinking-analysis-paralysis.md", ".ai/guides/recursive-investigation.md", ".ai/guides/perfectionism-completion.md"],
    98: [".ai/guides/failure-mode-catalog.md"],
    99: [".ai/telemetry/signals.schema.json"],
    100: [".ai/telemetry/thresholds.json"],
    101: [".ai/guides/deadlock-livelock.md"],
    102: [".ai/guides/deadlock-livelock.md"],
    103: [".ai/guides/deadlock-livelock.md"],
    123: ["scripts/validate_framework.py"],
    125: [".ai/tests/executive-function-cases.md"],
    126: ["tests/test_interventions.py"],
    128: [".ai/manifests/agents.json"],
    129: ["tests/test_framework_assets.py"],
    137: [".ai/manifests/rules.json", ".ai/manifests/skills.json", ".ai/manifests/agents.json", ".ai/manifests/knowledge.json"],
    174: ["scripts/validate_framework.py"],
    175: ["tests/test_interventions.py"],
    176: [".ai/skills/direct-communication/SKILL.md"],
    177: [".ai/context/context-index.json"],
    178: [".ai/memory/index.json"],
    179: [".ai/executive-function/state-machine.json"],
    180: [".ai/executive-function/executive-function.json", ".ai/executive-function/executive-function.toon", ".ai/executive-function/executive-function.sjon"],
    181: [".ai/tests/executive-function-cases.md"],
    182: ["scripts/validate_framework.py"],
    183: ["scripts/validate_framework.py"],
    188: ["skills/all-the-medicine/references/skills/install-framework/install-framework.md", ".ai/manifests/install.json"],
    189: ["skills/all-the-medicine/references/skills/install-framework/install-framework.md"],
}



def public_skill_path(name: str) -> str:
    """Where a public skill lives. There is ONE plugin skill, all-the-medicine;
    every other public skill is a reference inside it, never a skill of its own,
    so no platform lists it as a separate command."""
    if name == "all-the-medicine":
        return "skills/all-the-medicine/SKILL.md"
    return f"skills/all-the-medicine/references/skills/{name}/{name}.md"

def build() -> dict:
    prompt_bytes = PROMPT.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    headings = {int(number): title.rstrip("\r") for number, title in re.findall(r"^# (\d+)\. (.+)$", prompt, flags=re.MULTILINE)}
    if set(headings) != set(range(190)):
        missing = sorted(set(range(190)) - set(headings))
        raise ValueError(f"canonical prompt headings missing: {missing}")

    rules = json.loads((ROOT / ".ai/manifests/rules.json").read_text(encoding="utf-8"))["rules"]
    sections = {}
    for number in range(190):
        default_rule = next((item["path"] for item in rules if item["prompt_sections"][0] <= number <= item["prompt_sections"][1]), rules[-1]["path"])
        artifacts = [default_rule]
        artifacts.extend(SPECIAL.get(number, []))
        if number in SKILL_SECTIONS:
            skill = SKILL_SECTIONS[number]
            artifacts.append(f".ai/skills/{skill}/SKILL.md")
            if (ROOT / public_skill_path(skill)).exists():
                artifacts.append(public_skill_path(skill))
        artifacts = list(dict.fromkeys(artifacts))
        sections[str(number)] = {
            "title": headings[number],
            "classification": "acceptance" if 174 <= number <= 183 else "operational",
            "artifacts": artifacts,
        }
    return {
        "canonical_source": str(PROMPT.relative_to(ROOT)).replace("\\", "/"),
        "canonical_sha256": hashlib.sha256(prompt_bytes).hexdigest().upper(),
        "sections": sections,
    }


def main() -> int:
    OUTPUT.write_text(json.dumps(build(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} with 190 traced sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

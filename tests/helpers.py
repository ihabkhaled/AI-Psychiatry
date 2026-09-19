import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path):
    return path.read_text(encoding="utf-8")


def public_skill(name: str) -> Path:
    """AI-Psychiatry ships ONE plugin skill; every other public skill is a
    reference inside it (see scripts/validate_framework.public_skill_path)."""
    if name == "all-the-medicine":
        return REPO / "skills/all-the-medicine/SKILL.md"
    return REPO / f"skills/all-the-medicine/references/skills/{name}/{name}.md"

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path):
    return path.read_text(encoding="utf-8")

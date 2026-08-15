"""Build the portable skills-only marketplace submission archive."""

from __future__ import annotations

import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.4.0"
OUTPUT = ROOT / "dist" / f"ai-psychiatry-{VERSION}.zip"

DIRECTORIES = (
    ".ai",
    ".claude",
    ".claude-plugin",
    ".codex",
    ".codex-plugin",
    ".cursor",
    "agents",
    "assets",
    "codex",
    "docs/ai",
    "docs/listing",
    "hooks",
    "skills",
)

FILES = (
    ".cursorrules",
    "AGENTS.md",
    "CHANGELOG.md",
    "CLAUDE.md",
    "CODEX.md",
    "DEEPSEEK.md",
    "GEMINI.md",
    "GLM.md",
    "KIMI.md",
    "LICENSE",
    "MISTRAL.md",
    "PRIVACY.md",
    "QWEN.md",
    "README.md",
    "SUPPORT.md",
    "TERMS.md",
    "docs/publishing.md",
    "scripts/executive_control.py",
    "scripts/validate_framework.py",
)

EXCLUDED_PARTS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}
FIXED_TIME = (2026, 8, 14, 0, 0, 0)


def iter_files() -> list[Path]:
    candidates: set[Path] = set()
    for directory in DIRECTORIES:
        candidates.update(path for path in (ROOT / directory).rglob("*") if path.is_file())
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        candidates.add(path)
    return sorted(
        (
            path
            for path in candidates
            if not EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts)
            and path.suffix.lower() not in EXCLUDED_SUFFIXES
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def build() -> Path:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in iter_files():
            name = PurePosixPath(path.relative_to(ROOT)).as_posix()
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, path.read_bytes(), compresslevel=9)
    return OUTPUT


if __name__ == "__main__":
    result = build()
    print(f"Built {result.relative_to(ROOT)} ({result.stat().st_size} bytes)")

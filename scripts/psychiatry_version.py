"""AI-Psychiatry version discipline: one version, everywhere, bumped on every shipped change.

    python scripts/psychiatry_version.py [--root .] show
    python scripts/psychiatry_version.py [--root .] check [--base REF]
    python scripts/psychiatry_version.py [--root .] next  [--base REF]
    python scripts/psychiatry_version.py [--root .] bump major|minor|patch --date YYYY-MM-DD
    python scripts/psychiatry_version.py [--root .] set X.Y.Z [--date YYYY-MM-DD]

Exit codes: 0 ok, 1 a check failed, 2 usage error or unknown git ref.

The tool only ever edits version strings in place (formatting and line endings
are preserved) and never regenerates a manifest. It reads no clock: `bump`
needs `--date`. Rule: `.ai/rules/58-version-discipline.md`.
"""

from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PLACEHOLDER = "_Describe the change._"

# (path, regex whose group 2 is the version string, edit every match or the first only)
JSON_VERSION = r'^([ \t]*"version"[ \t]*:[ \t]*")([^"]*)(")'
CARRIERS = (
    (".claude-plugin/plugin.json", JSON_VERSION, False),
    (".claude-plugin/marketplace.json", JSON_VERSION, True),
    (".codex-plugin/plugin.json", JSON_VERSION, False),
    ("package.json", JSON_VERSION, False),
    ("pyproject.toml", r'^(version[ \t]*=[ \t]*")([^"]*)(")', False),
    ("VERSION", r"^()(\d[^\r\n]*?)([ \t]*)(?=\r?$)", False),
    (".ai/manifests/install.json", r'^([ \t]*"release"[ \t]*:[ \t]*")([^"]*)(")', False),
    (".ai/manifests/skills.json", JSON_VERSION, True),
    ("scripts/build_release_manifests.py", r'^(VERSION[ \t]*=[ \t]*")([^"]*)(")', False),
    ("scripts/build_submission_archive.py", r'^(VERSION[ \t]*=[ \t]*")([^"]*)(")', False),
)
PRIMARY = ".claude-plugin/plugin.json"

SHIPPED = (
    "skills/**", "hooks/**", "install.sh", "install.ps1", ".claude-plugin/**",
    ".codex-plugin/**", ".agents/**", "agents/**", "templates/**",
)
# Removing one of these breaks an installed setup: a major change.
BREAKING_DELETES = (
    "install.sh", "install.ps1", "hooks/hooks.json", ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json", "skills/*/SKILL.md",
)


class Usage(Exception):
    """Bad invocation or bad git ref: exit 2."""


def parse(version: str) -> tuple[int, int, int]:
    match = SEMVER.match(version)
    if not match:
        raise Usage(f"not a version X.Y.Z: {version!r}")
    return tuple(int(part) for part in match.groups())  # type: ignore[return-value]


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def versions_in(text: str, pattern: str, every: bool) -> list[str]:
    found = [m.group(2) for m in re.finditer(pattern, text, re.MULTILINE)]
    return found if every else found[:1]


def collect(root: Path) -> dict[str, list[str]]:
    """Every version string, by manifest path, for the manifests that exist."""
    out: dict[str, list[str]] = {}
    for rel, pattern, every in CARRIERS:
        path = root / rel
        if path.is_file():
            out[rel] = versions_in(read_text(path), pattern, every)
    return out


def current(root: Path) -> tuple[str, list[str]]:
    """The one version, and a list of problems (empty when every manifest agrees)."""
    found = collect(root)
    problems: list[str] = []
    distinct = {v for values in found.values() for v in values}
    for rel, values in found.items():
        if not values:
            problems.append(f"{rel}: no version string found")
    if len(distinct) > 1:
        problems.append("manifests disagree: " + "; ".join(
            f"{rel}={','.join(sorted(set(values)))}" for rel, values in sorted(found.items()) if values))
    if not distinct:
        raise Usage("no manifest with a version found under --root")
    primary = found.get(PRIMARY) or next((v for v in found.values() if v), [])
    return (primary[0] if primary else sorted(distinct)[0]), problems


def git(root: Path, *args: str) -> str:
    try:
        done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8")
    except OSError as exc:
        raise Usage(f"git is not available: {exc}") from exc
    if done.returncode != 0:
        raise Usage(f"git {' '.join(args)} failed: {done.stderr.strip()}")
    return done.stdout


def verify_ref(root: Path, ref: str) -> None:
    git(root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")


def glob_regex(pattern: str) -> re.Pattern[str]:
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(out + r"\Z")


def is_shipped(path: str, patterns: tuple[str, ...]) -> bool:
    return any(glob_regex(p).match(path) for p in patterns)


def changes(root: Path, ref: str) -> dict[str, str]:
    """path -> A, M or D since REF, committed or not (untracked files count as A)."""
    verify_ref(root, ref)
    result: dict[str, str] = {}
    for line in git(root, "diff", "--name-status", "--no-renames", ref).splitlines():
        status, _, path = line.partition("\t")
        result[path.strip()] = status[:1]
    for path in git(root, "ls-files", "--others", "--exclude-standard").splitlines():
        result.setdefault(path.strip(), "A")
    return result


def version_at(root: Path, ref: str) -> str | None:
    for rel in (PRIMARY, ".codex-plugin/plugin.json", "package.json"):
        try:
            text = git(root, "show", f"{ref}:{rel}")
        except Usage:
            continue
        values = versions_in(text, JSON_VERSION, False)
        if values:
            return values[0]
    return None


def changelog_section(root: Path, version: str) -> str | None:
    path = root / "CHANGELOG.md"
    if not path.is_file():
        return None
    lines = read_text(path).splitlines()
    heading = f"## [{version}]"
    for index, line in enumerate(lines):
        if line.strip() == heading or line.startswith(heading + " "):
            body = []
            for rest in lines[index + 1:]:
                if rest.startswith("## "):
                    break
                body.append(rest)
            return "\n".join(body)
    return None


def cmd_show(root: Path, _args: argparse.Namespace) -> int:
    for rel, values in collect(root).items():
        print(f"{rel}: {', '.join(sorted(set(values))) or '(none)'}")
    version, problems = current(root)
    print(f"version: {version}")
    for problem in problems:
        print(f"problem: {problem}")
    return 1 if problems else 0


def cmd_check(root: Path, args: argparse.Namespace) -> int:
    version, problems = current(root)
    parse(version)
    patterns = tuple(args.shipped) if args.shipped else SHIPPED
    if args.base:
        moved = {p: s for p, s in changes(root, args.base).items() if is_shipped(p, patterns)}
        base = version_at(root, args.base)
        if base is not None and parse(version) < parse(base):
            problems.append(f"version {version} is lower than {base} at {args.base}")
        if moved:
            shown = ", ".join(sorted(moved)[:3]) + (" ..." if len(moved) > 3 else "")
            if base is not None and not parse(version) > parse(base):
                problems.append(
                    f"shipped paths changed since {args.base} ({shown}) but version {version} "
                    f"is not greater than {base}: run `bump`")
            section = changelog_section(root, version)
            if section is None:
                problems.append(f"CHANGELOG.md has no `## [{version}]` section")
            elif PLACEHOLDER in section:
                problems.append(f"CHANGELOG.md `## [{version}]` still holds the placeholder text")
    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        return 1
    print(f"ok: version {version}" + (f" (base {args.base})" if args.base else ""))
    return 0


def cmd_next(root: Path, args: argparse.Namespace) -> int:
    version, problems = current(root)
    patterns = tuple(args.shipped) if args.shipped else SHIPPED
    moved = {p: s for p, s in changes(root, args.base).items() if is_shipped(p, patterns)}
    if not moved:
        print(f"bump: none\nreason: no shipped path changed since {args.base}")
        return 0
    removed = sorted(p for p, s in moved.items() if s == "D" and is_shipped(p, BREAKING_DELETES))
    added = sorted(p for p, s in moved.items() if s == "A")
    deleted = sorted(p for p, s in moved.items() if s == "D")
    if removed:
        kind, reason = "major", "removed " + ", ".join(removed)
    elif added or deleted:
        kind = "minor"
        reason = f"{len(added)} shipped path(s) added, {len(deleted)} removed (e.g. {(added or deleted)[0]})"
    else:
        kind, reason = "patch", f"{len(moved)} shipped path(s) modified (e.g. {sorted(moved)[0]})"
    print(f"bump: {kind}\nnext: {bump_version(version, kind)}\nreason: {reason}")
    return 0


def bump_version(version: str, kind: str) -> str:
    major, minor, patch = parse(version)
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def check_date(value: str | None) -> str:
    if not value:
        raise Usage("--date YYYY-MM-DD is required (this tool reads no clock)")
    try:
        datetime.date.fromisoformat(value)
    except ValueError as exc:
        raise Usage(f"bad --date {value!r}: {exc}") from exc
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise Usage(f"bad --date {value!r}: use YYYY-MM-DD")
    return value


def write_version(root: Path, new: str) -> list[str]:
    touched = []
    for rel, pattern, every in CARRIERS:
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        count = 0 if every else 1
        updated = re.sub(pattern, lambda m: m.group(1) + new + m.group(3), text, count=count, flags=re.MULTILINE)
        if updated != text:
            path.write_bytes(updated.encode("utf-8"))
            touched.append(rel)
    return touched


def add_changelog(root: Path, version: str, date: str) -> bool:
    path = root / "CHANGELOG.md"
    if not path.is_file():
        path.write_bytes(f"# Changelog\n\n## [{version}] - {date}\n\n- {PLACEHOLDER}\n".encode("utf-8"))
        return True
    text = read_text(path)
    if changelog_section(root, version) is not None:
        return False
    nl = "\r\n" if "\r\n" in text else "\n"
    block = f"## [{version}] - {date}{nl}{nl}- {PLACEHOLDER}{nl}{nl}"
    match = re.search(r"^## ", text, re.MULTILINE)
    if match:
        text = text[:match.start()] + block + text[match.start():]
    else:
        text = text.rstrip("\r\n") + nl + nl + block.rstrip("\r\n") + nl
    path.write_bytes(text.encode("utf-8"))
    return True


def apply(root: Path, new: str, date: str | None) -> int:
    touched = write_version(root, new)
    added = add_changelog(root, new, date) if date else False
    print(f"version: {new}")
    for rel in touched:
        print(f"updated: {rel}")
    if added:
        print(f"added: CHANGELOG.md section [{new}] (replace the placeholder)")
    return 0


def cmd_bump(root: Path, args: argparse.Namespace) -> int:
    date = check_date(args.date)
    version, problems = current(root)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        print("manifests disagree; fix with `set X.Y.Z` first")
        return 1
    return apply(root, bump_version(version, args.kind), date)


def cmd_set(root: Path, args: argparse.Namespace) -> int:
    parse(args.version)
    return apply(root, args.version, check_date(args.date) if args.date else None)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AI-Psychiatry version discipline")
    parser.add_argument("--root", type=Path, default=Path("."))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    for name in ("check", "next"):
        p = sub.add_parser(name)
        p.add_argument("--base", default=None if name == "check" else "HEAD")
        p.add_argument("--shipped", action="append", help="shipped glob (repeatable; replaces the default list)")
    p = sub.add_parser("bump")
    p.add_argument("kind", choices=("major", "minor", "patch"))
    p.add_argument("--date")
    p = sub.add_parser("set")
    p.add_argument("version")
    p.add_argument("--date")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        return {"show": cmd_show, "check": cmd_check, "next": cmd_next, "bump": cmd_bump, "set": cmd_set}[args.command](root, args)
    except Usage as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

# Version Discipline

## Semantic contract

A change to anything that ships - the skill, hooks, installers, plugin manifests, the portable pack, agents, templates - is not done until the version moves up and the CHANGELOG says why. Every manifest carries the same one version. The version is edited only through `scripts/psychiatry_version.py` (`bump`, `set`), which rewrites version strings in place and never regenerates a manifest. A change that touches only docs, tests or build scripts needs no bump.

## Detection

Trigger when a shipped path changed since the base ref and the version is not strictly greater than the one there; when the CHANGELOG has no `## [<version>]` section for the current version, or that section still holds the placeholder text; when two manifests disagree on the version; when a version is about to be hand-edited in one file; or when a build script that regenerates manifests is about to run wholesale.

## Recovery

Run `python scripts/psychiatry_version.py next --base <ref>` for the suggested bump and its reason, then `bump major|minor|patch --date YYYY-MM-DD` (the date is passed in; the tool reads no clock), replace the CHANGELOG placeholder with the real entry, and re-run `check --base <ref>`. Repair disagreeing manifests with `set X.Y.Z`. Never regenerate manifests wholesale: that once dropped rules 56 and 57.

## Enforcement

- Tool: `scripts/psychiatry_version.py` (`show`, `check [--base REF]`, `next`, `bump`, `set`; exit 1 on a failed check, 2 on usage or an unknown ref).
- Tests, with one mutation test per invariant: `tests/test_version_discipline.py`.
- CI: the `version-discipline` job in `.github/workflows/ci.yml` runs `check --base` against the PR base or the previous push.

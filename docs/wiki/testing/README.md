# Testing

What this answers: test strategy, coverage, user acceptance (UAT).

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## What is the test strategy, what coverage is expected, and who signs off user acceptance?

`python -m unittest discover -s tests` (or `python -m pytest tests -q`). Invariants carry mutation tests that prove the check fires: `tests/test_version_discipline.py`, `tests/test_always_followed.py`. Installer tests use the `PSYCH_*` environment overrides and temporary homes, never the real `~/.claude`, `~/.codex` or `~/.cursor`. The `install.ps1` test runs only on Windows. User acceptance sign-off: _Unknown - ask the owner and record the answer._

# Product

What this answers: goals, users and personas, journeys, features, acceptance criteria.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Who are the primary users, and what problem does this solve for them?

AI-Psychiatry is a plugin and installer that keeps coding agents (Claude Code, Codex, Cursor) honest and finishing: it names observable failure patterns (skipped evidence, drift, loops, rule-gaming, fake "done") and applies one control at a time. Users: people who run coding agents and are tired of repeating themselves. Owner: Ihab Khaled. Source: [README](../../../README.md).

Settled product decisions: one skill and one command per platform ([ADR 0001](../../adr/0001-loud-always-on-hooks-and-version-discipline.md), [0.6.0 changelog](../../../CHANGELOG.md)); always on, with relentless `never-stop` execution only on explicit request; the tone is loud and aimed at the AI, never at the human.

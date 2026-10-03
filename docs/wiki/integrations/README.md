# Integrations

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### SDKs and clients

Nothing detected.

### Environment variables naming an external service

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: external systems and vendors.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which external systems and vendors does this depend on, and what happens when each is down?

- GitHub: the installers clone or download this repository (`PSYCH_REPO_URL` overrides the URL). If GitHub is down, an install from a local checkout (`sh install.sh` inside it) still works.
- Claude Code CLI: used for `plugin marketplace add`, `plugin install` and `plugin uninstall`; if absent the installer warns and the other platforms still install.
- Codex and Cursor: file conventions only, no API.

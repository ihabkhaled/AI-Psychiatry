# Security

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### Secret handling

| Detected | Where |
|---|---|
| `.env` is gitignored | `.gitignore` |

### Environment variable names

Nothing detected.

### Dependency and vulnerability scanning

Nothing detected.

### Authentication libraries

Nothing detected.

### Ownership and policy

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: secret handling, auth, threat model.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## How are secrets handled, how do users and services authenticate, and what is the threat model?

Secrets: none are used or stored. `.env` files are gitignored. The hooks read no prompt, make no network call and never make a permission decision. The installers touch only files they recognise as their own and restore edited files byte for byte on uninstall. Threat model beyond this: _Unknown - ask the owner and record the answer._ See [sensitive data](sensitive-data.md).

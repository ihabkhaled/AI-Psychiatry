# Data

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### Databases

Nothing detected.

### Caches

Nothing detected.

### Queues and brokers

Nothing detected.

### ORMs and query layers

Nothing detected.

### Migrations

Nothing detected.

### Connection settings (env var names)

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: databases, caches, queues.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which databases, caches and queues exist, what lives in each, and how is it migrated and backed up?

None: no database, cache or queue. Durable state is files only: `.ai/memory/` and `.ai/state/` in a target repository, and the installer's download cache `~/.ai-psychiatry/src`, which `--uninstall` removes.

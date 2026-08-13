# Memory Integrity

## Semantic contract

Promote durable memory only when a fact is sourced, high-confidence, stable, reusable, and expensive enough to rediscover. Store the source or reference where practical. Speculation, temporary debugging, transient task state, duplicated facts, obsolete decisions, and unsupported assumptions never become durable memory. Newer repository evidence outranks memory without exception.

## Detection

Trigger when memory lacks a source, conflicts with inspected code or configuration, contains uncertainty language as fact, duplicates an existing record, describes an active task, or survives after its underlying decision changed. Check freshness before use, not only before storage.

## Recovery

Quarantine the candidate, inspect the smallest authoritative source, then confirm, revise, or delete it. Mark contradicted or obsolete records explicitly so they cannot silently guide work. Promote stable validated knowledge when avoiding memory would cause repeated expensive rediscovery. Balance pollution against starvation. See [context starvation](../guides/context-starvation.md).

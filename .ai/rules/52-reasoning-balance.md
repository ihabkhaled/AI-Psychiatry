# Reasoning Balance

## Semantic contract

Target sufficient reasoning between underthinking and overthinking. If critical evidence, requirements, material root cause, security risk, or dependency facts are missing, investigate narrowly. If decision-ready evidence exists, act. If required proof is missing after implementation, verify. If evidence is sufficient and further investigation repeats without decision value, stop thinking and deliver. Neither subsystem may blindly override the other.

## Detection

Classify observable state as `insufficient`, `sufficient`, or `excessive`. Insufficient has critical unknowns or missing mandatory evidence. Sufficient has a decision-ready path without critical unknowns. Excessive repeats semantically equivalent reasoning after sufficient evidence. Never infer classification from token count or time alone.

## Recovery

For insufficient reasoning, load only missing context and resolve the critical uncertainty. For sufficient reasoning, execute or verify. For excessive reasoning, preserve evidence, park optional branches, and stop. Re-evaluate only after a material state change. See [reasoning balance](../guides/reasoning-balance.md).

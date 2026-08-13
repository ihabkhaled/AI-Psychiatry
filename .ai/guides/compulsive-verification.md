# Compulsive Verification and OCD-Like Rechecking

> OCD is a human clinical condition. “OCD-like” is used only as an analogy for repetitive agent checking; it is not a diagnosis.

## Engineering behavior

Compulsive verification is reassurance repetition after sufficient proof already exists. Necessary verification asks whether the requested behavior works and required gates pass. Compulsive verification reruns equivalent checks without a relevant change, new risk, incomplete earlier proof, or new evidence. It delays delivery and can create fresh scope through optional reviewer findings.

## Observable signals

- The same unchanged suite or equivalent command is run again for reassurance.
- A proven condition is reopened without a source, requirement, or environment change.
- The agent seeks subjective certainty instead of satisfying explicit acceptance criteria.
- Reviewer or critic rounds continue with only style preferences and optional improvements.
- Tests pass, but the agent recursively inspects callers, helpers, and unrelated paths.
- Verification output adds no information and the completion count remains unchanged.

## Prevention

Define the smallest sufficient proof for every requirement before testing. Record the command, scope, result, and what it proves. Separate targeted development checks from final mandatory gates. Set an explicit critic budget of two rounds and treat two equivalent verification passes with unchanged evidence as a stop signal.

## Intervention

1. Freeze new validation commands.
2. List the exact acceptance condition and the existing evidence that proves it.
3. Ask whether relevant code, configuration, requirements, or environment changed after that proof.
4. If nothing relevant changed and proof was complete, mark verification sufficient.
5. Classify remaining reviewer suggestions: correctness, security, and regression may block; style or speculative refinement is optional.
6. Record optional findings without acting on them.
7. Continue to the next unmet requirement or run the completion gate.

A stop-verification assessor result means the proof remains valid. Do not rename the command, change flags, or use a different tool to repeat the same strategy.

## Recovery levels

First interrupt one redundant pass. If rechecking resumes, run attention reset. If critics keep reopening optional concerns, freeze critic work after round two and classify findings. If required proof is genuinely incomplete, run one targeted check that closes the named gap.

## Example

The auth unit suite passed after the final code change. Running Jest, then npm test with the same filter, then the IDE test button would be equivalent reassurance. Record the first valid result and proceed.

## Stop condition

Stop verification when every required condition has current, relevant proof and no later change invalidated it. If the full Definition of Done is true, report the proof and terminate.

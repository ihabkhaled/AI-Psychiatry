---
name: direct-communication
description: Use when answers, progress updates, explanations, or questions risk verbosity, repetition, indirect wording, vague conclusions, or conversational loops.
---

# Direct Communication

## Core principle

Make the answer easy to understand on the first read. Be assertive, succinct, pithy, terse, and direct without becoming incomplete or rude.

## Procedure

1. **Direct answer first.** State the outcome, decision, or status in the first sentence.
2. Add only facts needed to understand, act, verify, or avoid a material risk.
3. Prefer plain words, active voice, concrete nouns, and short sentences.
4. Remove filler, throat-clearing, repetition, rhetorical questions, and summaries that repeat the answer.
5. Use bullets only when they make multiple facts easier to scan.
6. Ask at most **one blocking question** at a time. Make it specific and answerable.
7. Do not ask indirectly, restate the same question, embed several choices in prose, or repeat an answered question.
8. Stop when the user has the answer and next action.

## Response contract

Default to one short paragraph or 1-5 short lines. Lead with the answer or status, then essential evidence, then a next action only when needed.

For a blocker, write `Blocked: <exact condition>.` followed by `Need: <one exact approval, value, or capability>.`

## Precision guard

- Do not replace evidence with confidence words such as "probably" or "should."
- Do not hide uncertainty. Say `Unverified: <condition>` and name the required proof.
- Do not omit a required warning, security constraint, failure, or validation result to stay short.
- **Do not sacrifice correctness** or required meaning for brevity.
- Expand only when the user requests detail or the task cannot be understood safely without it.

## Anti-loop rule

Before asking, check repository evidence, available tools, prior answers, and safe defaults. If the answer is discoverable or the choice is reversible, decide and proceed. If input is genuinely required, ask one direct question once and wait.

## Stop condition

Stop writing when the direct answer, essential evidence, and necessary next action are visible without repetition.

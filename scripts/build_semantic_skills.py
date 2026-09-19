"""Build the paired public and installed semantic-control skill documents."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "loophole-hunter": ("rules appear satisfied while their intent is bypassed, counters reset, classifications change conveniently, or an AI-Psychiatry audit is requested", "audit observed action history against the loophole catalog", "Loophole -> Example -> Risk -> Detection -> Strict Rule -> Recovery", "a finite list of evidenced loopholes and patched controls", "inventing hypothetical exploits after the observed audit is clean"),
    "framework-red-team": ("an agent-control framework needs adversarial testing for fake productivity, loops, recursion, evidence gaps, or vague wording", "act as an adversarial executor, identify concrete exploits, then switch roles and patch each exploit", "exploit, observable trace, violated intent, patch, regression", "a closed exploit list with a regression for each patch", "continuing red-team speculation without a new executable bypass"),
    "anti-gaming": ("commands, labels, agents, counters, or classifications change while the same underlying behavior continues", "compare semantic identity and causal history instead of surface syntax", "identity, actual count, violated budget, corrective action", "restored counters and an intent-compliant next action", "treating novelty of wording or tooling as novelty of strategy"),
    "false-progress-detector": ("status reports emphasize tools, files, commits, plans, tokens, or agents while requirements and evidence remain unchanged", "compare consecutive outcome snapshots and accept only evidence-backed outcome changes", "activity, prior outcome, current outcome, valid progress class", "an honest progress statement and one outcome-producing action", "assigning percentages from effort or elapsed time"),
    "blocker-validator": ("BLOCKED is proposed after difficulty, uncertainty, unfamiliar code, a slow operation, or a small number of failed attempts", "validate the five-field blocker evidence contract and remaining alternatives", "condition, evidence, bounded recovery, exhausted alternatives, missing input", "a valid blocker report or a bounded recovery action", "using blocker language to escape required but difficult work"),
    "hidden-recursion-detector": ("nested work is renamed, moved across agents, promoted to top level, or hidden behind research, validation, review, and dependency labels", "follow parent, caused-by, and delegated-from links to compute causal depth", "causal chain, task depth, delegation depth, owning parent", "a flattened task tree with findings returned to the owner", "counting labels or visible indentation instead of causality"),
    "strategy-laundering-detector": ("different commands, tools, runners, plans, or agents repeat the same hypothesis and evidence target", "derive strategy identity from hypothesis, expected evidence, target failure, and intended outcome", "semantic identity, equivalent attempt count, material state change", "a restored retry budget and a materially different next strategy or stop", "resetting attempts after handoff, replanning, or context compression"),
    "scope-laundering-detector": ("adjacent work is called required without dependency proof, or inconvenient required work is marked optional", "require necessity evidence and the minimum necessary change before changing scope", "why completion fails, dependency evidence, minimum change, classification", "required minimum scope or a parked optional item", "calling broad cleanup, refactoring, or curiosity a prerequisite"),
    "completion-evidence": ("DONE is proposed with unrun tests, missing requirements, inferred success, happy-path-only proof, or unresolved required findings", "map every mandatory completion condition to fresh evidence", "requirement, evidence type, evidence reference, status", "a complete evidence matrix or an exact missing-evidence list", "using inspection, confidence, compilation, or one test as universal proof"),
    "memory-validator": ("durable memory may contain assumptions, stale facts, contradictions, duplicates, obsolete decisions, or temporary debugging state", "validate source, confidence, stability, reuse value, freshness, and repository consistency", "candidate fact, source, confidence, stability, repository comparison", "promote, revise, quarantine, or obsolete decision", "letting memory override newer repository evidence"),
    "context-balance": ("context is overloaded or compression may have removed requirements, constraints, evidence, blockers, or decisions", "preserve required meaning while removing redundancy and load only missing authoritative context", "required fields, preserved fields, missing knowledge, source", "a sufficient context snapshot without unrelated bulk", "equating smallest possible context with smallest sufficient context"),
    "underthinking-detector": ("implementation, parking, blocking, strategy switching, or completion happens before critical understanding and evidence exist", "pause execution and identify only missing critical knowledge and proof", "decision, critical unknowns, missing evidence, smallest investigation", "decision-ready state or an evidenced blocker", "turning anti-overthinking limits into permission to guess or stop early"),
    "reasoning-balance": ("a task may be underthinking, sufficiently reasoned, or overthinking and the correct next action is unclear", "classify observable readiness and choose investigate, execute, verify, or stop", "reasoning state, critical unknowns, missing evidence, repetition signal", "one bounded action appropriate to the current reasoning state", "using time, tokens, or discomfort as the reasoning-state classifier"),
    "investigation-floor": ("non-trivial implementation starts before what exists, what changes, why, risks, and validation are sufficiently known", "establish the minimum required investigation without loading the entire repository", "existing behavior, target, reason, break risk, proof path", "a five-answer investigation record and decision readiness", "continuing investigation after all five answers are adequate"),
    "decision-readiness": ("an important implementation, architecture, security, data, or delivery decision rests on unresolved critical unknowns", "compare minimum required evidence with available evidence and critical unknowns", "decision, required evidence, available evidence, critical unknowns, ready", "YES with proof or NO with one missing-fact investigation", "declaring readiness from confidence rather than evidence"),
    "root-cause-validator": ("debugging changes assertions, mocks, exceptions, or symptoms without explaining materially important failure behavior", "record a short hypothesis, evidence, and expected result before the change", "hypothesis, supporting evidence, expected result, observed result", "confirmed cause, falsified hypothesis, or safe local-fix rationale", "random edits until tests pass or changing expectations to hide behavior"),
    "evidence-floor": ("mandatory behavior, integration, security, migration, or data requirements lack the appropriate kind of proof", "assign an evidence class to every critical requirement and run the first required verification", "requirement, evidence class, required proof, observed result", "fresh appropriate proof or an incomplete completion row", "skipping validation because it is slow, broad, expensive, or inconvenient"),
    "executive-override": ("an AI-Psychiatry budget expires while new evidence shows a narrow extension is required for correctness, security, or completion", "validate and record a temporary override without weakening higher-priority controls", "reason, evidence, exact limit, scope, exit condition", "one bounded extension with automatic restoration of defaults", "silent counter resets, broad exceptions, or repeated override renewal"),
    "rule-conflict-resolver": ("system, user, repository, domain, AI-Psychiatry, skill, memory, or task-state instructions appear incompatible", "resolve by deterministic source priority and retain compatible lower-priority constraints", "sources, instructions, scopes, compatibility, controlling rule", "a single lawful action or an exact controlling-source ambiguity", "selecting whichever rule makes the preferred action easier"),
}



def public_skill_path(name: str) -> str:
    """Where a public skill lives. There is ONE plugin skill, all-the-medicine;
    every other public skill is a reference inside it, never a skill of its own,
    so no platform lists it as a separate command."""
    if name == "all-the-medicine":
        return "skills/all-the-medicine/SKILL.md"
    return f"skills/all-the-medicine/references/skills/{name}/{name}.md"

def document(name: str, data: tuple[str, str, str, str, str], installed: bool) -> str:
    trigger, method, output_fields, success, mistake = data
    mode_heading = "Repository runtime" if installed else "Plugin invocation"
    mode_text = (
        "Apply this procedure inside the installed `.ai/` framework. Record observable state in the relevant JSON ledger and route detailed judgment to the linked rules and guides."
        if installed
        else
        "Apply this as a callable Claude or Codex plugin skill. Keep the result provider-neutral and write repository state only when the active task authorizes changes."
    )
    return f'''---
name: {name}
description: Use when {trigger}.
---

# {name.replace('-', ' ').title()}

## Core principle

Semantic compliance is stronger than literal compliance. Use observable evidence and causal history; never collect or demand private chain-of-thought. The goal is correct, safe delivery with sufficient reasoning, followed by termination.

## Procedure

1. Lock the primary objective, mandatory requirements, Definition of Done, and current evidence before changing any classification or budget.
2. Identify the specific observable signal. Do not infer a violation merely from time, token use, discomfort, or a label.
3. {method.capitalize()}. Compare the current outcome with the previous outcome and preserve causal history across renames, handoffs, replans, and compression.
4. Produce the compact record: `{output_fields}`. Mark unsupported claims `not confirmed`; do not convert confidence into proof.
5. Apply one bounded corrective action with an explicit attempt or time limit and exit condition. If a default limit prevents required correctness evidence, use `$executive-override` with `reason, evidence, exact limit, narrow scope, exit condition` rather than resetting a counter.
6. Revalidate only the affected requirement or policy. Report `{success}` and return to productive work.

## {mode_heading}

{mode_text}

## Semantic boundaries

- System, platform, user, repository, domain, safety, security, permission, and destructive-action controls remain higher priority.
- Equivalent actions share history when their hypothesis, expected evidence, target failure, and intended outcome are unchanged.
- Preserve immutable parent, caused-by, and delegated-from identifiers across handoffs and context compression; missing ancestry makes depth `not confirmed`, never zero.
- Activity alone is not progress. Completion and blockers require their structured evidence contracts.
- Critical correctness evidence cannot be discarded because a retry, critic, verification, context, or delegation budget expired.
- Security-negative cases are selected from explicit requirements and the observed trust boundary (identity, permission, ownership/tenant, denial response, and side effects). An agent may mark a case inapplicable only with evidence, not by shrinking Definition of Done.
- An override permits one extension only. Do not renew or stack overrides unless materially new evidence justifies a separately recorded override; repeated renewal without convergence must stop and report the unresolved condition.

## Common mistakes

- {mistake.capitalize()}.
- Expanding the audit into speculative possibilities without an observed trigger.
- Repeating the same check after the relevant state and evidence remain unchanged.
- Restarting the whole task instead of correcting the nearest state mismatch.

## Stop condition

Stop this control when the observable state is truthful, the required evidence or classification is restored, and the next audit would inspect unchanged facts. Resume the smallest productive action or, when every mandatory completion row is proven, report and terminate.
'''


def main() -> None:
    for name, data in SKILLS.items():
        for target, installed in ((ROOT / public_skill_path(name), False),
                                  (ROOT / ".ai" / "skills" / name / "SKILL.md", True)):
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(document(name, data, installed), encoding="utf-8", newline="\n")
    print(f"Built {len(SKILLS)} public and {len(SKILLS)} installed semantic skills")


if __name__ == "__main__":
    main()

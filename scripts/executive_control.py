"""Deterministic policy assessor for observable coding-agent state."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


STRATEGY_FIELDS = ("hypothesis", "expected_evidence", "target_failure", "intended_outcome")
PROGRESS_OUTCOMES = {
    "requirement-completed",
    "blocker-removed",
    "acceptance-verified",
    "relevant-test-fixed",
    "deliverable-completed",
    "uncertainty-reduced",
}
RULE_PRIORITY = {
    "system": 800,
    "platform": 800,
    "user": 700,
    "repository": 600,
    "domain": 500,
    "ai-psychiatry": 400,
    "skill": 300,
    "memory": 200,
    "temporary-state": 100,
}


def _normalized(value: Any) -> str:
    """Return a stable semantic comparison value for observable labels."""
    if value is None:
        return ""
    if isinstance(value, str):
        return " ".join(value.lower().split())
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def strategy_identity(action: dict[str, Any]) -> str:
    """Identify a strategy by its reasoning contract, never its command syntax."""
    semantic = {field: _normalized(action.get(field)) for field in STRATEGY_FIELDS}
    encoded = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def count_equivalent_attempts(history: list[dict[str, Any]], current: dict[str, Any]) -> int:
    """Count semantic attempts across renamed commands, counters, tasks, and agents."""
    identity = strategy_identity(current)
    return 1 + sum(strategy_identity(item) == identity for item in history)


def causal_depth(tasks: dict[str, dict[str, Any]], task_id: str) -> int:
    """Follow causal parents across labels and agents and reject cycles as over-depth."""
    depth = 0
    current: str | None = task_id
    visited: set[str] = set()
    while current is not None and current in tasks:
        if current in visited:
            return len(tasks) + 1
        visited.add(current)
        depth += 1
        task = tasks[current]
        current = task.get("parent") or task.get("caused_by")
    return depth


def validate_progress(event: dict[str, Any]) -> dict[str, Any]:
    """Accept only evidence-backed changes to the deliverable or decision state."""
    kind = event.get("kind", "")
    evidence = event.get("evidence")
    valid = kind in PROGRESS_OUTCOMES and bool(evidence)
    return {"valid": valid, "kind": kind, "reason": "outcome-change" if valid else "activity-only"}


def validate_completion(state: dict[str, Any]) -> dict[str, Any]:
    """Require evidence for every mandatory condition and resolve required findings."""
    missing: list[str] = []
    for requirement in state.get("requirements", []):
        if requirement.get("mandatory", True) and not requirement.get("evidence"):
            missing.append(str(requirement.get("id", "unnamed-requirement")))
    if state.get("tests_required", False) and not state.get("tests_run", False):
        missing.append("tests-not-run")
    for finding in state.get("required_findings", []):
        if not finding.get("resolved", False):
            missing.append(f"unresolved:{finding.get('id', 'finding')}")
    return {"complete": not missing, "missing": missing}


def validate_blocker(blocker: dict[str, Any]) -> dict[str, Any]:
    """Validate that a blocker is evidenced, recovered, unavoidable, and actionable."""
    missing: list[str] = []
    for field in ("condition", "evidence", "bounded_recovery", "alternatives", "missing"):
        if not blocker.get(field):
            missing.append(field)
    alternatives = blocker.get("alternatives", [])
    if alternatives and any(item.get("available", True) or not item.get("evidence") for item in alternatives):
        missing.append("alternatives-not-exhausted")
    return {"valid": not missing, "missing_fields": missing}


def validate_scope_expansion(proposal: dict[str, Any]) -> dict[str, Any]:
    """Require proof that completion fails without the minimum proposed work."""
    why = _normalized(proposal.get("why_required"))
    evidence = proposal.get("dependency_evidence", [])
    minimum = _normalized(proposal.get("minimum_change"))
    vague = why in {"", "it may help", "might help", "could help"}
    overbroad = any(token in minimum for token in ("all ", "everything", "entire ", "full refactor"))
    required = bool(evidence) and not vague and bool(minimum) and not overbroad
    return {"classification": "required" if required else "optional", "action": "allow-minimum" if required else "park"}


def validate_memory(candidate: dict[str, Any], repository_evidence: dict[str, Any] | None = None) -> dict[str, Any]:
    """Promote only sourced, stable, non-speculative facts not contradicted by newer evidence."""
    reasons: list[str] = []
    fact = candidate.get("fact")
    if not candidate.get("source"):
        reasons.append("missing-source")
    if candidate.get("confidence") not in {"high", "confirmed"}:
        reasons.append("insufficient-confidence")
    if not candidate.get("stable", False):
        reasons.append("unstable")
    if candidate.get("kind") in {"assumption", "speculation", "temporary-debugging"}:
        reasons.append("speculative-or-temporary")
    if candidate.get("duplicate", False):
        reasons.append("duplicate")
    if candidate.get("obsolete", False):
        reasons.append("obsolete")
    if repository_evidence is not None and fact in repository_evidence and repository_evidence[fact] is False:
        reasons.append("contradicted-by-repository")
    return {"promote": not reasons, "reasons": reasons}


def validate_context(summary: dict[str, Any]) -> dict[str, Any]:
    """Compress redundancy while preserving all required meaning."""
    required = set(summary.get("required_fields", []))
    preserved = set(summary.get("preserved", []))
    missing = sorted(required - preserved)
    return {"safe": not missing, "missing": missing, "action": "accept" if not missing else "restore-missing-context"}


def reasoning_balance(state: dict[str, Any]) -> dict[str, Any]:
    """Choose the minimum sufficient reasoning action from observable readiness signals."""
    critical = list(state.get("critical_unknowns", []))
    evidence = list(state.get("required_evidence_missing", []))
    if critical or evidence:
        return {
            "reasoningState": "insufficient",
            "criticalUnknowns": critical,
            "requiredEvidenceMissing": evidence,
            "recommendedAction": "investigate",
        }
    if state.get("repetition_detected", False):
        return {
            "reasoningState": "excessive",
            "criticalUnknowns": [],
            "requiredEvidenceMissing": [],
            "recommendedAction": "stop",
        }
    action = "execute" if state.get("decision_ready", False) else "verify"
    return {
        "reasoningState": "sufficient",
        "criticalUnknowns": [],
        "requiredEvidenceMissing": [],
        "recommendedAction": action,
    }


def validate_override(override: dict[str, Any]) -> dict[str, Any]:
    """Allow only explicit, evidenced, scoped, temporary AI-Psychiatry budget overrides."""
    missing = [field for field in ("reason", "evidence", "limit", "scope", "exit_condition") if not override.get(field)]
    source = override.get("target_rule_source", "ai-psychiatry")
    forbidden = source in {"system", "platform", "user", "repository", "domain"}
    return {"valid": not missing and not forbidden, "missing_fields": missing, "forbidden_source": source if forbidden else None}


def resolve_rule_conflict(rules: list[dict[str, Any]]) -> dict[str, Any]:
    """Resolve conflicts by declared source priority, preserving input order on ties."""
    if not rules:
        return {"source": None, "instruction": None, "status": "no-rule"}
    winner = max(enumerate(rules), key=lambda item: (RULE_PRIORITY.get(item[1].get("source", ""), 0), -item[0]))[1]
    return {**winner, "status": "selected-by-priority"}


def self_check(state: dict[str, Any]) -> dict[str, Any]:
    """Return a single bounded list of triggered behavioral checks."""
    if state.get("self_check_running", False):
        return {"triggered": [], "repeat": False}
    triggered: list[str] = []
    checks = [
        (state.get("goal_drift", False), "goal-drift"),
        (state.get("scope_drift", False), "scope-drift"),
        (state.get("active_work_items", 1) > 1, "attention-drift"),
        (state.get("causal_depth", 0) > 3, "hidden-recursion"),
        (state.get("equivalent_attempts", 0) >= 3, "repeated-strategy"),
        (state.get("progress_theater", False), "progress-theater"),
        (state.get("false_blocker_risk", False), "false-blocker"),
        (state.get("compulsive_verification", False), "compulsive-verification"),
        (state.get("critical_unknowns", []), "underthinking"),
        (state.get("overthinking", False), "overthinking"),
        (state.get("tests_required", False) and not state.get("tests_run", False), "required-tests-skipped"),
        (state.get("dod_claimed", False) and not state.get("dod_proven", False), "dod-not-proven"),
    ]
    for condition, name in checks:
        if condition:
            triggered.append(name)
    return {"triggered": triggered, "repeat": False}


def assess(state: dict[str, Any]) -> dict[str, str]:
    """Return the highest-priority bounded intervention for observable state."""
    if not state.get("objective_locked", False):
        return {"action": "goal-lock", "status": "required", "next": "define-objective-and-dod"}

    if state.get("repository_claim") and not state.get("claim_evidence", False):
        return {"action": "evidence-gate", "status": "not-confirmed", "next": "inspect-smallest-authoritative-source"}

    if state.get("nesting_depth", 0) > 3:
        parent = state.get("parent_task") or "locked-objective"
        return {"action": "return-to-parent", "status": "depth-exceeded", "next": f"resume:{parent}"}

    if state.get("active_work_items", 1) > 1 or state.get("branch_classification") in {"optional", "unrelated"}:
        return {"action": "attention-reset", "status": "drift", "next": "park-current-branch"}

    if state.get("speculative_branches", 0) > 0 and not state.get("new_evidence", False):
        return {"action": "scope-guard", "status": "evidence-free-expansion", "next": "park-speculation"}

    if state.get("same_strategy_attempts", 0) >= 3 or state.get("stalled_progress_cycles", 0) >= 4:
        return {"action": "strategy-reset", "status": "livelock-risk", "next": "reduce-search-space"}

    if state.get("verification_passes", 0) >= 2 and state.get("proof_valid", False) and not state.get("relevant_change", False):
        return {"action": "stop-verification", "status": "sufficient-proof", "next": "continue-or-complete"}

    if state.get("dod_satisfied", False):
        evidence_contract_present = any(key in state for key in ("requirements", "required_findings", "tests_required"))
        completion = validate_completion(state)
        if evidence_contract_present and not completion["complete"]:
            return {"action": "completion-evidence", "status": "incomplete-proof", "next": "satisfy-missing-evidence"}
        return {"action": "completion-gate", "status": "complete", "next": "report-proof-and-stop"}

    balance_contract_present = any(key in state for key in ("critical_unknowns", "required_evidence_missing", "decision_ready"))
    if balance_contract_present:
        balance = reasoning_balance(state)
        if balance["reasoningState"] == "insufficient":
            return {"action": "underthinking-detector", "status": "insufficient-evidence", "next": "investigate-critical-unknowns"}

    return {"action": "execute", "status": "advancing", "next": "smallest-evidence-producing-action"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Assess observable AI executive-control state")
    parser.add_argument("state", type=Path, help="JSON state file")
    args = parser.parse_args()
    state = json.loads(args.state.read_text(encoding="utf-8"))
    print(json.dumps(assess(state), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

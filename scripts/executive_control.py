"""Deterministic policy assessor for observable coding-agent state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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
        return {"action": "completion-gate", "status": "complete", "next": "report-proof-and-stop"}

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

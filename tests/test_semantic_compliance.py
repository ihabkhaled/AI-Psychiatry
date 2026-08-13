import unittest

from scripts.executive_control import (
    assess,
    causal_depth,
    count_equivalent_attempts,
    reasoning_balance,
    resolve_rule_conflict,
    self_check,
    strategy_identity,
    validate_blocker,
    validate_completion,
    validate_context,
    validate_memory,
    validate_override,
    validate_progress,
    validate_scope_expansion,
)


class SemanticComplianceTests(unittest.TestCase):
    def test_strategy_identity_ignores_command_and_label_laundering(self):
        unittest_action = {
            "command": "python -m unittest tests.test_auth",
            "label": "unit test",
            "hypothesis": "token parser rejects valid token",
            "expected_evidence": "auth test result",
            "target_failure": "login returns 401",
            "intended_outcome": "prove token parser defect",
        }
        pytest_action = {**unittest_action, "command": "pytest tests/test_auth.py", "label": "integration validation"}
        self.assertEqual(strategy_identity(unittest_action), strategy_identity(pytest_action))

    def test_equivalent_attempts_survive_reset_and_agent_changes(self):
        base = {
            "hypothesis": "token parser rejects valid token",
            "expected_evidence": "auth test result",
            "target_failure": "login returns 401",
            "intended_outcome": "prove token parser defect",
        }
        history = [
            {**base, "command": "pytest auth", "agent": "A", "reported_retry": 1},
            {**base, "command": "npm test auth", "agent": "B", "reported_retry": 0},
        ]
        self.assertEqual(count_equivalent_attempts(history, {**base, "command": "IDE runner"}), 3)

    def test_causal_depth_crosses_relabels_and_agents(self):
        tasks = {
            "root": {"parent": None, "agent": "A"},
            "research": {"parent": "root", "agent": "B"},
            "validation": {"caused_by": "research", "agent": "C"},
            "top-level-review": {"caused_by": "validation", "agent": "D", "label": "top level"},
        }
        self.assertEqual(causal_depth(tasks, "top-level-review"), 4)

    def test_progress_requires_outcome_change(self):
        for kind in ["file-read", "tool-call", "plan", "file-touch", "commit", "subagent-spawn"]:
            self.assertFalse(validate_progress({"kind": kind, "evidence": "activity only"})["valid"], kind)
        result = validate_progress({"kind": "uncertainty-reduced", "evidence": "reproduction isolated failure to parser"})
        self.assertTrue(result["valid"])

    def test_completion_requires_every_mandatory_evidence_item(self):
        result = validate_completion({
            "requirements": [
                {"id": "implementation", "mandatory": True, "evidence": ["commit:abc"]},
                {"id": "auth-negative", "mandatory": True, "evidence": []},
            ],
            "required_findings": [{"id": "security", "resolved": False}],
            "tests_required": True,
            "tests_run": False,
        })
        self.assertFalse(result["complete"])
        self.assertEqual(set(result["missing"]), {"auth-negative", "tests-not-run", "unresolved:security"})

    def test_blocker_needs_evidence_recovery_alternatives_and_missing_input(self):
        weak = validate_blocker({"condition": "test failed once", "evidence": []})
        self.assertFalse(weak["valid"])
        strong = validate_blocker({
            "condition": "deployment API rejects organization access",
            "evidence": ["403 organization role missing"],
            "bounded_recovery": ["refreshed session", "confirmed same organization"],
            "alternatives": [{"name": "CLI submission", "available": False, "evidence": "no command exists"}],
            "missing": "organization owner grants Apps Management write",
        })
        self.assertTrue(strong["valid"])

    def test_scope_expansion_requires_dependency_evidence_and_minimum_change(self):
        weak = validate_scope_expansion({"why_required": "it may help", "dependency_evidence": [], "minimum_change": "refactor all auth"})
        self.assertEqual(weak["classification"], "optional")
        strong = validate_scope_expansion({
            "why_required": "login cannot validate tokens without the parser",
            "dependency_evidence": ["failing trace enters parser"],
            "minimum_change": "correct one parser branch",
        })
        self.assertEqual(strong["classification"], "required")

    def test_memory_rejects_speculation_staleness_and_repository_contradiction(self):
        result = validate_memory(
            {"fact": "queue service exists", "confidence": "low", "stable": False, "source": None, "kind": "assumption"},
            {"queue service exists": False},
        )
        self.assertFalse(result["promote"])
        self.assertIn("contradicted-by-repository", result["reasons"])

    def test_context_compression_preserves_required_meaning(self):
        required = ["objective", "requirements", "security_constraints", "evidence", "blockers", "remaining_work"]
        starved = validate_context({"required_fields": required, "preserved": ["objective", "remaining_work"]})
        self.assertFalse(starved["safe"])
        self.assertIn("security_constraints", starved["missing"])

    def test_reasoning_balance_detects_underthinking_sufficient_and_overthinking(self):
        under = reasoning_balance({"critical_unknowns": ["auth ownership"], "required_evidence_missing": ["negative auth test"]})
        self.assertEqual((under["reasoningState"], under["recommendedAction"]), ("insufficient", "investigate"))
        ready = reasoning_balance({"critical_unknowns": [], "required_evidence_missing": [], "decision_ready": True})
        self.assertEqual((ready["reasoningState"], ready["recommendedAction"]), ("sufficient", "execute"))
        excessive = reasoning_balance({"critical_unknowns": [], "required_evidence_missing": [], "decision_ready": True, "repetition_detected": True})
        self.assertEqual((excessive["reasoningState"], excessive["recommendedAction"]), ("excessive", "stop"))

    def test_override_is_explicit_temporary_and_cannot_override_higher_priority(self):
        valid = validate_override({
            "reason": "third attempt produced a different failure",
            "evidence": ["timeout changed to validation mismatch"],
            "limit": "same_strategy_attempts:+1",
            "scope": "token validation hypothesis",
            "exit_condition": "validate mismatch once",
            "target_rule_source": "ai-psychiatry",
        })
        self.assertTrue(valid["valid"])
        forbidden = validate_override({
            "reason": "move faster", "evidence": ["deadline"], "limit": "safety:disable", "scope": "all",
            "exit_condition": "done", "target_rule_source": "system",
        })
        self.assertFalse(forbidden["valid"])

    def test_conflict_resolution_is_deterministic_and_not_convenience_based(self):
        winner = resolve_rule_conflict([
            {"source": "memory", "instruction": "skip tests"},
            {"source": "repository", "instruction": "run auth tests"},
            {"source": "user", "instruction": "finish and test auth"},
        ])
        self.assertEqual(winner["source"], "user")

    def test_self_check_returns_only_triggered_checks_once(self):
        result = self_check({"active_work_items": 2, "tests_required": True, "tests_run": False, "self_check_running": False})
        self.assertEqual(result["triggered"], ["attention-drift", "required-tests-skipped"])
        self.assertFalse(result["repeat"])

    def test_assessor_blocks_premature_completion(self):
        result = assess({
            "objective_locked": True,
            "dod_satisfied": True,
            "requirements": [{"id": "negative-auth", "mandatory": True, "evidence": []}],
            "tests_required": True,
            "tests_run": False,
        })
        self.assertEqual(result["action"], "completion-evidence")


if __name__ == "__main__":
    unittest.main()

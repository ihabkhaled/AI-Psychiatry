import unittest

from scripts.executive_control import (
    classify_decision,
    classify_question,
    next_relentless_action,
    validate_blocker,
    validate_hard_gate,
    validate_streaming_liveness,
)
from tests.helpers import REPO, load_json, read


class NeverStopAssetTests(unittest.TestCase):
    def test_skill_pair_is_discoverable_and_declares_stop_condition(self):
        for root in ("skills", ".ai/skills"):
            path = REPO / root / "never-stop" / "SKILL.md"
            self.assertTrue(path.exists(), str(path))
            text = read(path)
            self.assertTrue(text.startswith("---\nname: never-stop\n"), str(path))
            self.assertIn("description: Use when", text)
            self.assertIn("## Procedure", text)
            self.assertIn("## Stop condition", text)
            self.assertIn("## Superpower classification", text)

    def test_rule_and_guide_exist_with_required_sections(self):
        rule = read(REPO / ".ai/rules/56-never-stop-relentless-execution.md")
        self.assertGreaterEqual(len(rule.split()), 100)
        for heading in ["## Semantic contract", "## Detection", "## Recovery"]:
            self.assertIn(heading, rule)
        guide = read(REPO / ".ai/guides/relentless-execution.md")
        self.assertGreaterEqual(len(guide.split()), 180)
        for heading in ["## Observable signals", "## Intervention", "## Stop condition"]:
            self.assertIn(heading, guide)

    def test_manifest_registers_never_stop_as_explicit_invocation_only(self):
        skills = load_json(REPO / ".ai/manifests/skills.json")
        runtime = next(item for item in skills["skills"] if item["name"] == "never-stop")
        self.assertEqual(runtime["loadCondition"], "explicit-invocation")
        plugin = next(item for item in skills["plugin_skills"] if item["name"] == "never-stop")
        self.assertEqual(plugin["path"], "skills/never-stop/SKILL.md")
        self.assertIn("rule-56", runtime["canonical_rules"])

    def test_autonomy_policy_declares_superpower_and_forbids_bypass(self):
        policy = load_json(REPO / ".ai/policies/autonomy-contract.json")
        self.assertFalse(policy["permissionBypass"])
        self.assertTrue(policy["independentWorkBeforeQuestion"])
        self.assertEqual(policy["superpower"], {
            "tier": "superpower",
            "riskLevel": "high",
            "explicitInvocationOnly": True,
            "maximumEffort": True,
        })

    def test_approval_gates_policy_forbids_bypass(self):
        policy = load_json(REPO / ".ai/policies/approval-gates.json")
        self.assertFalse(policy["permissionBypass"])
        self.assertIn("production-deployment", policy["hardGateConditions"])
        self.assertNotIn("task-is-difficult", policy["hardGateConditions"])

    def test_schema_declares_relentless_execution_fields(self):
        schema = load_json(REPO / ".ai/executive-function/semantic-state.schema.json")
        for field in [
            "autonomyMode", "hardGate", "independentWorkRemaining", "recoveryLevel",
            "skillStatuses", "allTheMedicineActive", "backgroundTaskActive", "backgroundStreamingStale",
        ]:
            self.assertIn(field, schema["properties"], field)

    def test_all_scenarios_present(self):
        cases = read(REPO / ".ai/tests/never-stop-cases.md")
        for number in range(1, 13):
            self.assertIn(f"## Scenario {number}", cases, number)
            self.assertIn(f"Expected {number}:", cases, number)


class NeverStopAssessorTests(unittest.TestCase):
    def test_answerable_question_is_suppressed_not_asked(self):
        result = classify_question({"answerable_via": ["repository-instructions"]})
        self.assertTrue(result["suppress"])
        self.assertEqual(result["action"], "investigate-or-decide")

    def test_unanswerable_question_is_asked(self):
        result = classify_question({"answerable_via": []})
        self.assertFalse(result["suppress"])
        self.assertEqual(result["action"], "ask-minimum-required")

    def test_safe_reversible_ambiguity_is_decided_autonomously(self):
        result = classify_decision({"reversible": True, "blast_radius": "small"})
        self.assertEqual(result["class"], "A")
        self.assertEqual(result["action"], "choose-default-and-execute")

    def test_material_but_reversible_decision_is_recorded_not_asked(self):
        result = classify_decision({"reversible": True, "blast_radius": "medium"})
        self.assertEqual(result["class"], "B")
        self.assertEqual(result["action"], "record-decision-and-continue")

    def test_hard_gate_condition_is_never_classified_as_routine(self):
        result = classify_decision({"hard_gate_condition": "production-deployment", "reversible": True, "blast_radius": "small"})
        self.assertEqual(result["class"], "C")

    def test_recoverable_failure_triggers_recovery_not_a_stop(self):
        action = next_relentless_action({"recoverable_failure": True})
        self.assertEqual(action["action"], "recovery")

    def test_false_blocker_is_rejected_and_execution_resumes(self):
        blocker = {
            "condition": "one test failed",
            "evidence": "log",
            "bounded_recovery": "retried once",
            "alternatives": [{"available": True, "evidence": False}],
            "missing": None,
        }
        self.assertFalse(validate_blocker(blocker)["valid"])
        action = next_relentless_action({"blocker": blocker})
        self.assertEqual(action["action"], "resume-execution")

    def test_independent_work_continues_before_asking_at_a_blocked_branch(self):
        action = next_relentless_action({
            "blocked_branch": True,
            "independent_work_remaining": ["write unit tests", "update documentation"],
        })
        self.assertEqual(action["action"], "continue-independent-work")

    def test_genuine_hard_gate_with_no_independent_work_requests_minimum_approval(self):
        action = next_relentless_action({
            "hard_gate": {"condition": "production-deployment", "independent_work_remaining": []},
        })
        self.assertEqual(action["action"], "request-minimum-approval")

    def test_invalid_hard_gate_condition_is_rejected(self):
        result = validate_hard_gate({"condition": "the task is difficult", "independent_work_remaining": []})
        self.assertFalse(result["valid"])
        self.assertEqual(result["action"], "resume-execution")

    def test_proven_completion_stops_immediately_over_optional_work(self):
        action = next_relentless_action({"dod_proven": True, "independent_work_remaining": ["polish formatting"]})
        self.assertEqual(action["action"], "report-and-stop")

    def test_fabricated_background_execution_claim_is_rejected(self):
        result = validate_streaming_liveness({"claims_background_execution": True, "mechanism_present": False})
        self.assertFalse(result["live"])
        self.assertEqual(result["issue"], "fabricated-background-claim")

    def test_stale_background_progress_is_flagged_for_a_status_check(self):
        result = validate_streaming_liveness({
            "background_task_active": True, "seconds_since_progress": 999, "stale_after_seconds": 120,
        })
        self.assertFalse(result["live"])
        self.assertEqual(result["issue"], "stale-background-progress")
        self.assertEqual(result["action"], "check-and-report-status")

    def test_live_background_progress_is_accepted(self):
        result = validate_streaming_liveness({
            "background_task_active": True, "seconds_since_progress": 5, "stale_after_seconds": 120,
        })
        self.assertTrue(result["live"])


if __name__ == "__main__":
    unittest.main()

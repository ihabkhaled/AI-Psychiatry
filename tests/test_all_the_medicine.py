import unittest

from scripts.build_all_the_medicine import (
    SELF_NAME,
    assert_no_duplicates,
    assert_paths_exist,
    build,
    check,
    load_plugin_skills,
    load_rules,
)
from scripts.executive_control import build_skill_status_map, select_all_the_medicine_control
from tests.helpers import REPO, load_json, read


class AllTheMedicineAssetTests(unittest.TestCase):
    def test_skill_pair_is_discoverable_and_declares_stop_condition(self):
        for root in ("skills", ".ai/skills"):
            path = REPO / root / "all-the-medicine" / "SKILL.md"
            self.assertTrue(path.exists(), str(path))
            text = read(path)
            self.assertTrue(text.startswith("---\nname: all-the-medicine\n"), str(path))
            self.assertIn("## Procedure", text)
            self.assertIn("## Stop condition", text)
            self.assertIn("## Superpower classification", text)

    def test_rule_is_marked_generated_composite_with_required_sections(self):
        rule = read(REPO / ".ai/rules/57-all-the-medicine.md")
        self.assertIn("GENERATED COMPOSITE RULE", rule)
        for heading in ["## Semantic contract", "## Detection", "## Recovery"]:
            self.assertIn(heading, rule)

    def test_guide_exists_with_required_sections(self):
        guide = read(REPO / ".ai/guides/all-the-medicine.md")
        self.assertGreaterEqual(len(guide.split()), 180)
        for heading in ["## Observable signals", "## Intervention", "## Stop condition"]:
            self.assertIn(heading, guide)

    def test_policy_declares_self_exclusion_and_one_control_at_a_time(self):
        policy = load_json(REPO / ".ai/policies/all-the-medicine.json")
        self.assertEqual(policy["excludes"], [SELF_NAME])
        self.assertIn("never-stop", policy["includes"])
        self.assertTrue(policy["oneControlAtATime"])
        self.assertFalse(policy["selfRecursionAllowed"])
        self.assertEqual(policy["superpower"]["tier"], "god-mode")
        self.assertEqual(policy["superpower"]["type"], "meta-superpower")

    def test_compact_toon_and_sjon_variants_exist(self):
        for relative in [".ai/policies/all-the-medicine.toon", ".ai/policies/all-the-medicine.sjon"]:
            path = REPO / relative
            self.assertTrue(path.exists(), relative)
            self.assertGreater(path.stat().st_size, 80, relative)

    def test_all_scenarios_present(self):
        cases = read(REPO / ".ai/tests/all-the-medicine-cases.md")
        for number in range(1, 15):
            self.assertIn(f"## Scenario {number}", cases, number)
            self.assertIn(f"Expected {number}:", cases, number)


class AllTheMedicineGeneratorTests(unittest.TestCase):
    def test_every_public_skill_is_included_exactly_once_and_self_excluded(self):
        skills = load_plugin_skills()
        names = [item["name"] for item in skills]
        self.assertEqual(len(names), len(set(names)))
        self.assertNotIn(SELF_NAME, names)
        self.assertIn("never-stop", names)
        manifest = load_json(REPO / ".ai/manifests/skills.json")
        expected = {item["name"] for item in manifest["plugin_skills"]} - {SELF_NAME}
        self.assertEqual(set(names), expected)

    def test_future_skill_registered_in_manifest_is_discovered_without_code_changes(self):
        manifest = load_json(REPO / ".ai/manifests/skills.json")
        declared_names = {item["name"] for item in manifest["plugin_skills"]} - {SELF_NAME}
        loaded_names = {item["name"] for item in load_plugin_skills()}
        self.assertEqual(declared_names, loaded_names)

    def test_build_output_is_deterministic_across_runs(self):
        self.assertEqual(build(), build())

    def test_check_passes_against_current_repository_output(self):
        self.assertEqual(check(build()), [])

    def test_compiled_documents_are_marked_generated_and_self_recursion_free(self):
        outputs = build()
        skills_doc = next(value for key, value in outputs.items() if key.endswith("all-skills-compiled.md"))
        rules_doc = next(value for key, value in outputs.items() if key.endswith("all-rules-compiled.md"))
        self.assertIn("GENERATED", skills_doc)
        self.assertIn("GENERATED", rules_doc)
        self.assertNotIn(f"BEGIN SKILL: {SELF_NAME}", skills_doc)

    def test_orchestration_order_is_stable_and_matches_manifest_id_order(self):
        skills = load_plugin_skills()
        ids = [int(item["id"].split("-")[-1]) for item in skills]
        self.assertEqual(ids, sorted(ids))

    def test_missing_declared_skill_file_fails_generation(self):
        with self.assertRaises(FileNotFoundError):
            assert_paths_exist([{"path": "skills/does-not-exist/SKILL.md"}])

    def test_duplicate_skill_ids_fail_generation(self):
        with self.assertRaises(ValueError):
            assert_no_duplicates(
                [{"id": "plugin-skill-00", "name": "a"}, {"id": "plugin-skill-00", "name": "b"}],
                "id", "test-fixture",
            )

    def test_duplicate_skill_names_fail_generation(self):
        with self.assertRaises(ValueError):
            assert_no_duplicates(
                [{"id": "plugin-skill-00", "name": "a"}, {"id": "plugin-skill-01", "name": "a"}],
                "name", "test-fixture",
            )

    def test_duplicate_rule_ids_fail_generation(self):
        rules = load_rules()
        with self.assertRaises(ValueError):
            assert_no_duplicates(rules + [rules[0]], "id", "test-fixture")


class AllTheMedicineOrchestrationTests(unittest.TestCase):
    PHASE_ORDER = ["evidence-gate", "attention-reset", "reasoning-balance", "completion-gate"]

    def test_install_framework_is_not_applicable_for_ordinary_coding_tasks(self):
        status = build_skill_status_map(
            ["install-framework", "executive-control"],
            {"is_framework_task": False, "satisfied_skills": ["executive-control"]},
        )
        self.assertEqual(status["install-framework"], "NOT_APPLICABLE")

    def test_install_framework_is_active_for_a_framework_install_task(self):
        status = build_skill_status_map(
            ["install-framework"],
            {"is_framework_task": True, "active_skills": ["install-framework"]},
        )
        self.assertEqual(status["install-framework"], "ACTIVE")

    def test_all_the_medicine_never_appears_in_its_own_status_map(self):
        status = build_skill_status_map(["executive-control", SELF_NAME], {"active_skills": [SELF_NAME]})
        self.assertNotIn(SELF_NAME, status)

    def test_select_control_raises_on_self_recursion_in_status_map(self):
        with self.assertRaises(ValueError):
            select_all_the_medicine_control({SELF_NAME: "ACTIVE"}, [SELF_NAME])

    def test_every_applicable_skill_receives_exactly_one_final_status(self):
        names = ["install-framework", "evidence-gate", "attention-reset", "completion-gate"]
        status = build_skill_status_map(names, {
            "satisfied_skills": ["evidence-gate"],
            "active_skills": ["attention-reset"],
            "not_applicable_skills": ["completion-gate"],
        })
        self.assertEqual(set(status), set(names))
        for value in status.values():
            self.assertIn(value, {"PENDING", "CHECKED", "ACTIVE", "SATISFIED", "NOT_APPLICABLE", "BLOCKED_BY_HIGHER_PRIORITY_RULE"})

    def test_exactly_one_control_is_selected_when_two_would_otherwise_activate(self):
        status = {"attention-reset": "ACTIVE", "reasoning-balance": "ACTIVE"}
        selected = select_all_the_medicine_control(status, self.PHASE_ORDER)
        self.assertEqual(selected, "attention-reset")

    def test_no_control_selected_once_everything_is_satisfied_or_not_applicable(self):
        status = {"evidence-gate": "SATISFIED", "attention-reset": "NOT_APPLICABLE"}
        self.assertIsNone(select_all_the_medicine_control(status, self.PHASE_ORDER))

    def test_optional_work_does_not_prevent_termination(self):
        from scripts.executive_control import validate_completion

        state = {
            "requirements": [{"id": "core-feature", "mandatory": True, "evidence": ["tests passed"]}],
            "tests_required": True,
            "tests_run": True,
            "required_findings": [],
        }
        self.assertTrue(validate_completion(state)["complete"])


if __name__ == "__main__":
    unittest.main()

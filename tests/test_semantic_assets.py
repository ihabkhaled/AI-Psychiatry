import json
import unittest
from pathlib import Path

from scripts.executive_control import reasoning_balance, validate_completion, validate_override
from tests.helpers import REPO, load_json, read


NEW_SKILLS = {
    "loophole-hunter",
    "framework-red-team",
    "anti-gaming",
    "false-progress-detector",
    "blocker-validator",
    "hidden-recursion-detector",
    "strategy-laundering-detector",
    "scope-laundering-detector",
    "completion-evidence",
    "memory-validator",
    "context-balance",
    "underthinking-detector",
    "reasoning-balance",
    "investigation-floor",
    "decision-readiness",
    "root-cause-validator",
    "evidence-floor",
    "executive-override",
    "rule-conflict-resolver",
}

NEW_RULES = {
    "41-semantic-compliance.md",
    "42-false-progress.md",
    "43-completion-evidence.md",
    "44-blocker-validation.md",
    "45-hidden-recursion.md",
    "46-strategy-laundering.md",
    "47-scope-laundering.md",
    "48-memory-integrity.md",
    "49-context-balance.md",
    "50-underthinking.md",
    "51-investigation-evidence-floor.md",
    "52-reasoning-balance.md",
    "53-executive-override.md",
    "54-rule-conflict.md",
    "55-self-check.md",
}

NEW_GUIDES = {
    "semantic-compliance.md",
    "loophole-catalog.md",
    "underthinking.md",
    "reasoning-balance.md",
    "context-starvation.md",
    "sufficient-reasoning.md",
    "executive-override-conflicts.md",
}


class SemanticMachineAssetTests(unittest.TestCase):
    def test_semantic_policy_defines_meaning_based_budgets(self):
        policy = load_json(REPO / ".ai/policies/semantic-compliance.json")
        self.assertEqual(policy["strategyIdentity"], ["hypothesis", "expectedEvidence", "targetFailure", "intendedOutcome"])
        self.assertIn("requirement-completed", policy["acceptedProgress"])
        self.assertEqual(policy["causalDepth"]["ignores"], ["label", "agent", "counterReset"])
        self.assertEqual(policy["conflictPriority"][:3], ["system-platform", "user", "repository"])

    def test_machine_state_exercises_runtime_contracts(self):
        completion = load_json(REPO / ".ai/state/completion-evidence.json")
        self.assertFalse(validate_completion(completion)["complete"])
        balance = load_json(REPO / ".ai/state/reasoning-balance.json")
        self.assertEqual(reasoning_balance(balance)["reasoningState"], balance["reasoningState"])
        override = load_json(REPO / ".ai/state/executive-override.json")
        self.assertFalse(validate_override(override)["valid"])

    def test_compact_representations_and_schema_exist(self):
        for relative in [
            ".ai/policies/semantic-compliance.toon",
            ".ai/state/reasoning-balance.toon",
            ".ai/state/reasoning-balance.sjon",
            ".ai/executive-function/semantic-state.schema.json",
            ".ai/state/action-ledger.json",
        ]:
            path = REPO / relative
            self.assertTrue(path.exists(), relative)
            self.assertGreater(path.stat().st_size, 80, relative)
        schema = load_json(REPO / ".ai/executive-function/semantic-state.schema.json")
        self.assertEqual(schema["type"], "object")
        self.assertIn("reasoningState", schema["properties"])


class SemanticInstructionAssetTests(unittest.TestCase):
    def test_semantic_skills_close_forward_pressure_loopholes(self):
        public = "\n".join(
            read(REPO / "skills" / name / "SKILL.md")
            for name in [
                "anti-gaming",
                "hidden-recursion-detector",
                "reasoning-balance",
                "executive-override",
                "evidence-floor",
            ]
        )
        for required in [
            "reason, evidence, exact limit, narrow scope, exit condition",
            "explicit attempt or time limit",
            "immutable parent, caused-by, and delegated-from identifiers",
            "observed trust boundary",
            "Do not renew or stack overrides",
        ]:
            self.assertIn(required, public)

    def test_numbered_semantic_rules_have_contract_and_recovery(self):
        for name in NEW_RULES:
            text = read(REPO / ".ai/rules" / name)
            self.assertGreaterEqual(len(text.split()), 100, name)
            self.assertIn("## Semantic contract", text, name)
            self.assertIn("## Detection", text, name)
            self.assertIn("## Recovery", text, name)

    def test_guides_are_operational_and_balanced(self):
        for name in NEW_GUIDES:
            text = read(REPO / ".ai/guides" / name)
            self.assertGreaterEqual(len(text.split()), 180, name)
            self.assertIn("## Observable signals", text, name)
            self.assertIn("## Intervention", text, name)
            self.assertIn("## Stop condition", text, name)

    def test_loophole_catalog_uses_required_six_field_contract(self):
        catalog = read(REPO / ".ai/guides/loophole-catalog.md")
        rows = [line for line in catalog.splitlines() if line.startswith("| L-")]
        self.assertGreaterEqual(len(rows), 20)
        for row in rows:
            self.assertEqual(len([cell for cell in row.split("|")[1:-1]]), 6, row)

    def test_underthinking_red_team_has_all_ten_scenarios(self):
        cases = read(REPO / ".ai/tests/underthinking-cases.md")
        for number in range(1, 11):
            self.assertIn(f"## Scenario {number}", cases)
            self.assertIn(f"Expected {number}:", cases)

    def test_loophole_regressions_cover_requested_bypasses(self):
        cases = read(REPO / ".ai/tests/loophole-regression-cases.md").lower()
        for phrase in [
            "strategy laundering", "scope laundering", "false progress", "false completion",
            "false blocker", "hidden recursion", "memory poisoning", "context starvation",
            "critic", "delegation", "counter reset", "executive override",
        ]:
            self.assertIn(phrase, cases)

    def test_public_and_installed_skills_are_discoverable_and_distinct(self):
        bodies = set()
        for name in NEW_SKILLS:
            for root in ("skills", ".ai/skills"):
                path = REPO / root / name / "SKILL.md"
                self.assertTrue(path.exists(), f"{root}/{name}")
                text = read(path)
                self.assertTrue(text.startswith(f"---\nname: {name}\n"), str(path))
                self.assertIn("description: Use when", text, str(path))
                self.assertIn("## Procedure", text, str(path))
                self.assertIn("## Stop condition", text, str(path))
                self.assertGreaterEqual(len(text.split()), 100, str(path))
                bodies.add(text.split("## Procedure", 1)[1])
        self.assertEqual(len(bodies), len(NEW_SKILLS) * 2)

    def test_both_enhancement_prompts_are_packaged(self):
        for name, marker in [
            ("loophole-enhancement-prompts.md", "Semantic compliance > literal compliance"),
            ("underthinking-reasoning-balance-prompt.md", "Think enough"),
        ]:
            text = read(REPO / "skills/install-framework/references" / name)
            self.assertIn(marker.lower(), text.lower())
            self.assertGreaterEqual(len(text.split()), 800, name)


if __name__ == "__main__":
    unittest.main()

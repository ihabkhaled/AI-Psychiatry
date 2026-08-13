import hashlib
import re
import unittest

from scripts.executive_control import assess
from tests.helpers import REPO, load_json, read


class InterventionBehaviorTests(unittest.TestCase):
    def test_attention_drift_returns_to_locked_objective(self):
        result = assess({"objective_locked": True, "active_work_items": 3, "branch_classification": "optional"})
        self.assertEqual(result["action"], "attention-reset")
        self.assertEqual(result["next"], "park-current-branch")

    def test_recursive_box_inside_box_returns_to_parent(self):
        result = assess({"objective_locked": True, "nesting_depth": 4, "parent_task": "fix-login"})
        self.assertEqual(result["action"], "return-to-parent")
        self.assertEqual(result["next"], "resume:fix-login")

    def test_compulsive_rechecking_stops_when_proof_is_still_valid(self):
        result = assess({"objective_locked": True, "verification_passes": 2, "proof_valid": True, "relevant_change": False})
        self.assertEqual(result["action"], "stop-verification")

    def test_unsupported_repository_claim_requires_evidence(self):
        result = assess({"objective_locked": True, "repository_claim": "queue service exists", "claim_evidence": False})
        self.assertEqual(result["action"], "evidence-gate")
        self.assertEqual(result["status"], "not-confirmed")

    def test_stalled_activity_triggers_livelock_recovery(self):
        result = assess({"objective_locked": True, "stalled_progress_cycles": 4, "same_strategy_attempts": 3})
        self.assertEqual(result["action"], "strategy-reset")
        self.assertEqual(result["next"], "reduce-search-space")

    def test_evidence_free_speculation_is_parked(self):
        result = assess({"objective_locked": True, "speculative_branches": 3, "new_evidence": False})
        self.assertEqual(result["action"], "scope-guard")
        self.assertEqual(result["next"], "park-speculation")


class PluginInterventionAssetTests(unittest.TestCase):
    PUBLIC_SKILLS = {
        "executive-control",
        "attention-reset",
        "stop-overthinking",
        "stop-compulsive-verification",
        "flatten-recursive-investigation",
        "evidence-gate",
        "recover-from-deadlock-livelock",
        "completion-gate",
    }

    GUIDE_FILES = {
        "attention-drift.md",
        "compulsive-verification.md",
        "overthinking-analysis-paralysis.md",
        "recursive-investigation.md",
        "nested-job-control.md",
        "hallucination-evidence.md",
        "perfectionism-completion.md",
        "rabbit-holes-scope-drift.md",
        "deadlock-livelock.md",
        "failure-mode-catalog.md",
    }

    def test_reattached_master_prompt_is_canonical(self):
        data = (REPO / "skills/install-framework/references/master-prompt.md").read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest().upper(), "32AAB10548A9B1808BE5051207EA2732A72274081933AC8F87B5F57B9DBE1075")

    def test_interventions_are_discoverable_as_plugin_skills(self):
        for name in self.PUBLIC_SKILLS:
            skill = REPO / "skills" / name / "SKILL.md"
            self.assertTrue(skill.exists(), name)
            text = read(skill)
            self.assertTrue(text.startswith(f"---\nname: {name}\n"))
            self.assertIn("description: Use when", text)

    def test_guides_are_substantive_operational_references(self):
        for name in self.GUIDE_FILES:
            path = REPO / ".ai/guides" / name
            self.assertTrue(path.exists(), name)
            text = read(path)
            self.assertGreaterEqual(len(text.split()), 250, name)
            for heading in ["## Observable signals", "## Intervention", "## Stop condition"]:
                self.assertIn(heading, text, f"{name}: {heading}")

    def test_runtime_thresholds_match_reattached_prompt(self):
        thresholds = load_json(REPO / ".ai/telemetry/thresholds.json")
        self.assertEqual(thresholds["maxNestingDepth"], 3)
        self.assertEqual(thresholds["maxSameStrategyAttempts"], 3)
        self.assertEqual(thresholds["maxCriticRounds"], 2)
        self.assertEqual(thresholds["maxAgentDelegationDepth"], 2)
        self.assertEqual(thresholds["stalledProgressCyclesBeforeReset"], 4)

    def test_install_manifest_includes_rules_skills_guides_and_machine_runtime(self):
        manifest = load_json(REPO / ".ai/manifests/install.json")
        self.assertEqual(set(manifest["layers"]), {"rules", "skills", "guides", "context", "memory", "state", "telemetry", "manifests", "tests"})
        self.assertEqual(manifest["public_skill_root"], "skills/")
        self.assertEqual(manifest["target_runtime_root"], ".ai/")

    def test_installable_operational_skills_are_not_generic_duplicates(self):
        manifest = load_json(REPO / ".ai/manifests/skills.json")["skills"]
        bodies = []
        for item in manifest:
            text = read(REPO / item["path"])
            self.assertGreaterEqual(len(text.split()), 110, item["name"])
            self.assertIn("## Procedure", text, item["name"])
            self.assertIn("## Stop condition", text, item["name"])
            body = text.split("## Procedure", 1)[1]
            bodies.append(body)
        self.assertEqual(len(set(bodies)), len(manifest))

    def test_high_risk_rules_contain_mandatory_interventions(self):
        rules = {
            "05-anti-distraction.md": "attention-drift.md",
            "06-anti-overthinking.md": "overthinking-analysis-paralysis.md",
            "07-anti-recursion.md": "recursive-investigation.md",
            "08-anti-perfectionism.md": "perfectionism-completion.md",
            "12-verification-budget.md": "compulsive-verification.md",
            "14-hallucination-control.md": "hallucination-evidence.md",
            "15-deadlock-detection.md": "deadlock-livelock.md",
            "16-livelock-detection.md": "deadlock-livelock.md",
            "25-multi-agent-control.md": "nested-job-control.md",
            "28-termination.md": "perfectionism-completion.md",
        }
        for rule, guide in rules.items():
            text = read(REPO / ".ai/rules" / rule)
            self.assertGreaterEqual(len(text.split()), 150, rule)
            self.assertIn("## Mandatory control", text, rule)
            self.assertIn(f"../guides/{guide}", text, rule)

    def test_traceability_uses_exact_prompt_titles_and_existing_artifacts(self):
        prompt = read(REPO / "skills/install-framework/references/master-prompt.md")
        headings = dict(re.findall(r"^# (\d+)\. (.+)$", prompt, flags=re.MULTILINE))
        trace = load_json(REPO / ".ai/manifests/prompt-traceability.json")["sections"]
        self.assertEqual(set(headings), set(trace))
        for number, title in headings.items():
            self.assertEqual(trace[number]["title"], title)
            self.assertTrue(trace[number]["artifacts"], number)
            for artifact in trace[number]["artifacts"]:
                self.assertTrue((REPO / artifact).exists(), f"{number}: {artifact}")
        self.assertIn(".ai/guides/attention-drift.md", trace["97"]["artifacts"])
        self.assertIn(".ai/guides/failure-mode-catalog.md", trace["98"]["artifacts"])


if __name__ == "__main__":
    unittest.main()

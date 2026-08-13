import unittest

from tests.helpers import REPO, load_json, read


class PluginPackageTests(unittest.TestCase):
    def test_both_manifests_expose_shared_install_skill(self):
        self.assertTrue((REPO / ".claude-plugin/plugin.json").exists())
        codex = load_json(REPO / ".codex-plugin/plugin.json")
        self.assertEqual(codex["skills"], "./skills/")
        self.assertTrue((REPO / "skills/install-framework/SKILL.md").exists())

    def test_master_prompt_is_progressively_disclosed(self):
        skill_path = REPO / "skills/install-framework/SKILL.md"
        skill = read(skill_path)
        self.assertIn("references/master-prompt.md", skill)
        self.assertLess(len(skill.encode()), 5000)
        master = REPO / "skills/install-framework/references/master-prompt.md"
        self.assertGreater(master.stat().st_size, 60000)

    def test_release_versions_match_semantic_compliance_release(self):
        claude = load_json(REPO / ".claude-plugin/plugin.json")
        codex = load_json(REPO / ".codex-plugin/plugin.json")
        marketplace = load_json(REPO / ".claude-plugin/marketplace.json")
        self.assertEqual(claude["version"], "0.3.0")
        self.assertEqual(codex["version"], "0.3.0")
        self.assertEqual(marketplace["plugins"][0]["version"], "0.3.0")

    def test_semantic_skills_and_policies_are_installable(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        self.assertIn("policies", install["layers"])
        self.assertIn("reasoning-balance", install["public_skills"])
        skills = load_json(REPO / ".ai/manifests/skills.json")
        self.assertEqual(len(skills["skills"]), 47)
        self.assertEqual(len(skills["plugin_skills"]), 28)


if __name__ == "__main__":
    unittest.main()

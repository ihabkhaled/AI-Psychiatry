import struct
import unittest

from tests.helpers import REPO, load_json, read


class PluginPackageTests(unittest.TestCase):
    def test_codex_branding_assets_use_valid_relative_square_paths(self):
        codex = load_json(REPO / ".codex-plugin/plugin.json")
        interface = codex["interface"]
        for field in ["composerIcon", "logo"]:
            relative = interface[field]
            self.assertTrue(relative.startswith("./"), field)
            asset = REPO / relative[2:]
            self.assertTrue(asset.is_file(), field)
        with (REPO / interface["composerIcon"][2:]).open("rb") as image:
            self.assertEqual(image.read(8), b"\x89PNG\r\n\x1a\n")
            image.read(4)
            self.assertEqual(image.read(4), b"IHDR")
            width, height = struct.unpack(">II", image.read(8))
        self.assertEqual(width, height)

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

    def test_release_versions_match_current_release(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        claude = load_json(REPO / ".claude-plugin/plugin.json")
        codex = load_json(REPO / ".codex-plugin/plugin.json")
        marketplace = load_json(REPO / ".claude-plugin/marketplace.json")
        release = install["release"]
        self.assertEqual(release, "0.4.0")
        self.assertEqual(claude["version"], release)
        self.assertEqual(codex["version"], release)
        self.assertEqual(marketplace["plugins"][0]["version"], release)

    def test_semantic_skills_and_policies_are_installable(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        self.assertIn("policies", install["layers"])
        self.assertIn("reasoning-balance", install["public_skills"])
        skills = load_json(REPO / ".ai/manifests/skills.json")
        self.assertEqual(len(skills["skills"]), 49)
        self.assertEqual(len(skills["plugin_skills"]), 30)

    def test_superpowers_are_registered_as_public_skills_and_manifest_paths_resolve(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        for name in ("never-stop", "all-the-medicine"):
            self.assertIn(name, install["public_skills"])
        skills = load_json(REPO / ".ai/manifests/skills.json")
        for section in ("skills", "plugin_skills"):
            for item in skills[section]:
                self.assertTrue((REPO / item["path"]).exists(), item["path"])


if __name__ == "__main__":
    unittest.main()

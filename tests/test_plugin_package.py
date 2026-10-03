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
        self.assertTrue((REPO / "skills/all-the-medicine/references/skills/install-framework/install-framework.md").exists())

    def test_master_prompt_is_progressively_disclosed(self):
        skill_path = REPO / "skills/all-the-medicine/references/skills/install-framework/install-framework.md"
        skill = read(skill_path)
        self.assertIn("references/master-prompt.md", skill)
        self.assertLess(len(skill.encode()), 5000)
        master = REPO / "skills/all-the-medicine/references/skills/install-framework/references/master-prompt.md"
        self.assertGreater(master.stat().st_size, 60000)

    def test_release_versions_match_current_release(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        claude = load_json(REPO / ".claude-plugin/plugin.json")
        codex = load_json(REPO / ".codex-plugin/plugin.json")
        marketplace = load_json(REPO / ".claude-plugin/marketplace.json")
        release = install["release"]
        self.assertEqual(release, "0.7.0")
        self.assertEqual(claude["version"], release)
        self.assertEqual(codex["version"], release)
        self.assertEqual(marketplace["plugins"][0]["version"], release)

    def test_semantic_skills_and_policies_are_installable(self):
        install = load_json(REPO / ".ai/manifests/install.json")
        self.assertIn("policies", install["layers"])
        self.assertIn("reasoning-balance", install["public_skills"])
        skills = load_json(REPO / ".ai/manifests/skills.json")
        self.assertEqual(len(skills["skills"]), 49)
        self.assertEqual(len(skills["plugin_skills"]), 31)

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


class OneSkillTests(unittest.TestCase):
    def test_exactly_one_plugin_skill_exists(self):
        """Every SKILL.md is a separate menu entry on Claude Code, Codex and
        Cursor - Codex and Cursor even scan recursively. One skill, one entry."""
        found = sorted(p.relative_to(REPO).as_posix() for p in (REPO / "skills").rglob("SKILL.md"))
        self.assertEqual(found, ["skills/all-the-medicine/SKILL.md"])

    def test_skill_fits_codex_explicit_invocation(self):
        """Codex truncates an explicitly invoked SKILL.md at 8,000 bytes."""
        self.assertLessEqual(len((REPO / "skills/all-the-medicine/SKILL.md").read_bytes()), 8000)

    def test_always_on_hook_is_exec_form(self):
        hook = load_json(REPO / "hooks/hooks.json")["hooks"]["SessionStart"][0]["hooks"][0]
        self.assertEqual(hook["command"], "sh")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}", hook["args"][0])

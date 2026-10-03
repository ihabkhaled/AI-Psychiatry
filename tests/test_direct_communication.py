import json
import unittest

from tests.helpers import REPO, public_skill, read


class DirectCommunicationTests(unittest.TestCase):
    def test_public_and_runtime_skills_exist(self):
        for root in ("skills", ".ai/skills"):
            path = public_skill("direct-communication") if root == "skills" else REPO / root / "direct-communication" / "SKILL.md"
            self.assertTrue(path.exists(), str(path))
            text = read(path)
            self.assertTrue(text.startswith("---\nname: direct-communication\n"))
            for phrase in ("Direct answer first", "one blocking question", "Do not sacrifice correctness"):
                self.assertIn(phrase, text)

    def test_skill_is_registered_and_old_name_is_removed(self):
        manifest = json.loads(read(REPO / ".ai/manifests/skills.json"))
        runtime_names = {item["name"] for item in manifest["skills"]}
        public_names = {item["name"] for item in manifest["plugin_skills"]}
        self.assertIn("direct-communication", runtime_names)
        self.assertIn("direct-communication", public_names)
        self.assertNotIn("communicate-briefly", runtime_names)

    def test_codex_prompts_meet_platform_limits(self):
        plugin = json.loads(read(REPO / ".codex-plugin/plugin.json"))
        prompts = plugin["interface"]["defaultPrompt"]
        self.assertLessEqual(len(prompts), 3)
        self.assertTrue(all(len(prompt) <= 128 for prompt in prompts))

    def test_release_is_050(self):
        for path in (
            ".codex-plugin/plugin.json",
            ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json",
            ".ai/manifests/install.json",
            ".ai/manifests/skills.json",
        ):
            data = json.loads(read(REPO / path))
            version = data.get("release") or data.get("version") or data["plugins"][0]["version"]
            self.assertEqual(version, "0.7.0", path)


if __name__ == "__main__":
    unittest.main()

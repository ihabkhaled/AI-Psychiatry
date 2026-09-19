import unittest

from tests.helpers import REPO, read


class PublicationTests(unittest.TestCase):
    def test_readme_documents_both_install_paths(self):
        text = read(REPO / "README.md")
        # One skill, one command: the install paths and the single entry point.
        self.assertIn("install.sh | sh", text)
        self.assertIn("install.ps1 | iex", text)
        self.assertIn("claude plugin install ai-psychiatry@ihabkhaled-ai", text)
        self.assertIn("/ai-psychiatry:all-the-medicine", text)
        self.assertIn("$all-the-medicine", text)
        self.assertIn("behavioral analogy", text.lower())

    def test_listing_has_required_cases(self):
        text = read(REPO / "docs/listing/test-cases.md")
        self.assertEqual(text.count("## Positive"), 5)
        self.assertEqual(text.count("## Negative"), 3)

    def test_publication_policy_and_support_materials_exist(self):
        for name in ["PRIVACY.md", "TERMS.md", "SUPPORT.md"]:
            text = read(REPO / name)
            self.assertGreaterEqual(len(text.split()), 80, name)
        self.assertTrue((REPO / "assets/ai-psychiatry-logo.png").exists())

    def test_submission_archive_has_portable_root(self):
        import zipfile

        archive = REPO / "dist/ai-psychiatry-0.6.0.zip"
        self.assertTrue(archive.exists())
        with zipfile.ZipFile(archive) as bundle:
            names = set(bundle.namelist())
        self.assertIn(".claude-plugin/plugin.json", names)
        self.assertIn(".codex-plugin/plugin.json", names)
        self.assertIn("skills/all-the-medicine/references/skills/underthinking-detector/underthinking-detector.md", names)
        self.assertIn("skills/all-the-medicine/references/skills/reasoning-balance/reasoning-balance.md", names)
        self.assertIn("skills/all-the-medicine/references/skills/never-stop/never-stop.md", names)
        self.assertIn("skills/all-the-medicine/SKILL.md", names)
        self.assertIn("skills/all-the-medicine/references/all-skills-compiled.md", names)


if __name__ == "__main__":
    unittest.main()

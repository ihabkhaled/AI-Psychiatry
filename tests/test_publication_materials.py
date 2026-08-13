import unittest

from tests.helpers import REPO, read


class PublicationTests(unittest.TestCase):
    def test_readme_documents_both_install_paths(self):
        text = read(REPO / "README.md")
        self.assertIn("/ai-psychiatry:install-framework", text)
        self.assertIn("$install-framework", text)
        self.assertIn("behavioral analogy", text.lower())

    def test_listing_has_required_cases(self):
        text = read(REPO / "docs/listing/test-cases.md")
        self.assertEqual(text.count("## Positive"), 5)
        self.assertEqual(text.count("## Negative"), 3)


if __name__ == "__main__":
    unittest.main()

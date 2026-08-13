import tempfile
import unittest
from pathlib import Path

from scripts.validate_framework import validate


class ValidatorTests(unittest.TestCase):
    def test_validator_rejects_broken_markdown_link(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text("[broken](missing.md)", encoding="utf-8")
            codes = {issue.code for issue in validate(root, package_required=False)}
            self.assertIn("broken-link", codes)

    def test_validator_accepts_repository(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(validate(root), [])


if __name__ == "__main__":
    unittest.main()

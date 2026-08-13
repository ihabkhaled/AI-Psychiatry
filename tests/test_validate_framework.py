import tempfile
import unittest
from pathlib import Path

from scripts.validate_framework import validate, validate_traceability


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

    def test_traceability_validator_rejects_stale_prompt_title(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            prompt = root / "skills/install-framework/references/master-prompt.md"
            trace = root / ".ai/manifests/prompt-traceability.json"
            prompt.parent.mkdir(parents=True)
            trace.parent.mkdir(parents=True)
            prompt.write_text("# 0. EXACT TITLE\n", encoding="utf-8")
            trace.write_text('{"canonical_sha256":"bad","sections":{"0":{"title":"STALE","artifacts":[]}}}', encoding="utf-8")
            codes = {issue.code for issue in validate_traceability(root)}
            self.assertIn("traceability-stale", codes)
            self.assertIn("traceability-hash", codes)


if __name__ == "__main__":
    unittest.main()

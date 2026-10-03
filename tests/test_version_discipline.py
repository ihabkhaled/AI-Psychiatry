"""Rule 58: every invariant of scripts/psychiatry_version.py has a mutation test that proves it fires."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.helpers import REPO

TOOL = REPO / "scripts/psychiatry_version.py"


def plugin(version, nl="\n"):
    return nl.join(['{', f'  "name": "demo",', f'  "version": "{version}"', '}', ''])


def market(version):
    return json.dumps({"plugins": [{"name": "demo", "version": version}]}, indent=2) + "\n"


class Repo:
    def __init__(self, test, version="1.2.3"):
        self.dir = tempfile.TemporaryDirectory()
        test.addCleanup(self.dir.cleanup)
        self.root = Path(self.dir.name)
        self.git("init", "-q")
        for key, value in (("user.name", "t"), ("user.email", "t@example.invalid"),
                           ("core.autocrlf", "false"), ("commit.gpgsign", "false")):
            self.git("config", "--local", key, value)
        self.write(".claude-plugin/plugin.json", plugin(version))
        self.write(".claude-plugin/marketplace.json", market(version))
        self.write("CHANGELOG.md", f"# Changelog\n\n## [{version}] - 2026-01-01\n\n- first\n")
        self.write("skills/demo/SKILL.md", "---\nname: demo\n---\n")
        self.write("docs/note.md", "note\n")
        self.commit("base")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True, text=True).stdout

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def read(self, rel):
        return (self.root / rel).read_bytes().decode("utf-8")

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def run(self, *args):
        done = subprocess.run([sys.executable, str(TOOL), "--root", str(self.root), *args],
                              capture_output=True, text=True)
        return done.returncode, done.stdout + done.stderr


class ShowAndAgreement(unittest.TestCase):
    def test_show_reports_the_version(self):
        code, out = Repo(self).run("show")
        self.assertEqual(code, 0)
        self.assertIn("version: 1.2.3", out)

    def test_disagreeing_manifests_fail_check(self):
        repo = Repo(self)
        self.assertEqual(repo.run("check")[0], 0)
        repo.write(".claude-plugin/marketplace.json", market("1.2.4"))  # mutation
        code, out = repo.run("check")
        self.assertEqual(code, 1)
        self.assertIn("disagree", out)

    def test_every_carrier_is_read(self):
        repo = Repo(self)
        repo.write("VERSION", "1.2.3\n")
        repo.write("package.json", '{\n  "name": "d",\n  "version": "1.2.3"\n}\n')
        repo.write("pyproject.toml", '[project]\nname = "d"\nversion = "1.2.3"\n')
        self.assertEqual(repo.run("check")[0], 0)
        for rel, text in (("VERSION", "1.2.9\n"), ("package.json", '{\n  "version": "1.2.9"\n}\n'),
                          ("pyproject.toml", '[project]\nversion = "1.2.9"\n')):
            other = Repo(self)
            other.write("VERSION", "1.2.3\n")
            other.write("package.json", '{\n  "version": "1.2.3"\n}\n')
            other.write("pyproject.toml", '[project]\nversion = "1.2.3"\n')
            other.write(rel, text)  # mutation
            self.assertEqual(other.run("check")[0], 1, rel)


class BaseCheck(unittest.TestCase):
    def test_shipped_change_without_bump_fails(self):
        repo = Repo(self)
        repo.write("skills/demo/SKILL.md", "changed\n")  # mutation: shipped, no bump
        code, out = repo.run("check", "--base", "HEAD")
        self.assertEqual(code, 1)
        self.assertIn("not greater", out)

    def test_unshipped_change_needs_no_bump(self):
        repo = Repo(self)
        repo.write("docs/note.md", "changed\n")
        self.assertEqual(repo.run("check", "--base", "HEAD")[0], 0)

    def test_bump_without_changelog_fails(self):
        repo = Repo(self)
        repo.write("skills/demo/SKILL.md", "changed\n")
        repo.run("set", "1.3.0")  # version moved, changelog not touched
        code, out = repo.run("check", "--base", "HEAD")
        self.assertEqual(code, 1)
        self.assertIn("CHANGELOG.md has no", out)

    def test_untouched_placeholder_fails(self):
        repo = Repo(self)
        repo.write("skills/demo/SKILL.md", "changed\n")
        repo.run("bump", "minor", "--date", "2026-02-02")
        code, out = repo.run("check", "--base", "HEAD")
        self.assertEqual(code, 1)
        self.assertIn("placeholder", out)

    def test_full_flow_passes(self):
        repo = Repo(self)
        repo.write("skills/demo/SKILL.md", "changed\n")
        repo.run("bump", "patch", "--date", "2026-02-02")
        log = repo.read("CHANGELOG.md").replace("_Describe the change._", "fixed")
        repo.write("CHANGELOG.md", log)
        self.assertEqual(repo.run("check", "--base", "HEAD")[0], 0)

    def test_untracked_shipped_file_counts(self):
        repo = Repo(self)
        repo.write("hooks/new.sh", "echo\n")  # mutation: new untracked shipped file
        self.assertEqual(repo.run("check", "--base", "HEAD")[0], 1)

    def test_downgrade_fails(self):
        repo = Repo(self)
        repo.run("set", "1.0.0")
        self.assertEqual(repo.run("check", "--base", "HEAD")[0], 1)

    def test_bad_ref_is_a_usage_error(self):
        repo = Repo(self)
        self.assertEqual(repo.run("check", "--base", "no-such-ref")[0], 2)
        self.assertEqual(repo.run("next", "--base", "no-such-ref")[0], 2)


class Next(unittest.TestCase):
    def suggest(self, repo):
        code, out = repo.run("next", "--base", "HEAD")
        self.assertEqual(code, 0)
        return out

    def test_nothing_shipped_means_none(self):
        repo = Repo(self)
        repo.write("docs/note.md", "x\n")
        self.assertIn("bump: none", self.suggest(repo))

    def test_modified_is_patch(self):
        repo = Repo(self)
        repo.write("skills/demo/SKILL.md", "x\n")
        out = self.suggest(repo)
        self.assertIn("bump: patch", out)
        self.assertIn("next: 1.2.4", out)

    def test_added_is_minor(self):
        repo = Repo(self)
        repo.write("hooks/hooks.json", "{}\n")
        out = self.suggest(repo)
        self.assertIn("bump: minor", out)
        self.assertIn("next: 1.3.0", out)

    def test_removed_skill_is_major(self):
        repo = Repo(self)
        (repo.root / "skills/demo/SKILL.md").unlink()
        out = self.suggest(repo)
        self.assertIn("bump: major", out)
        self.assertIn("next: 2.0.0", out)


class BumpAndSet(unittest.TestCase):
    def test_bump_needs_a_date(self):
        repo = Repo(self)
        self.assertEqual(repo.run("bump", "minor")[0], 2)
        self.assertEqual(repo.run("bump", "minor", "--date", "2026-13-40")[0], 2)
        self.assertEqual(repo.run("bump", "minor", "--date", "2026-1-4")[0], 2)
        self.assertIn('"version": "1.2.3"', repo.read(".claude-plugin/plugin.json"))

    def test_bump_edits_only_version_strings(self):
        repo = Repo(self)
        before = repo.read(".claude-plugin/plugin.json")
        self.assertEqual(repo.run("bump", "major", "--date", "2026-02-02")[0], 0)
        self.assertEqual(repo.read(".claude-plugin/plugin.json"), before.replace("1.2.3", "2.0.0"))
        self.assertEqual(repo.read(".claude-plugin/marketplace.json"), market("1.2.3").replace("1.2.3", "2.0.0"))
        self.assertEqual(repo.read("skills/demo/SKILL.md"), "---\nname: demo\n---\n")

    def test_crlf_is_preserved(self):
        repo = Repo(self)
        repo.write(".claude-plugin/plugin.json", plugin("1.2.3", "\r\n"))
        repo.write("CHANGELOG.md", "# Changelog\r\n\r\n## [1.2.3] - 2026-01-01\r\n\r\n- first\r\n")
        repo.write("VERSION", "1.2.3\r\n")
        self.assertEqual(repo.run("bump", "patch", "--date", "2026-02-02")[0], 0)
        self.assertEqual(repo.read(".claude-plugin/plugin.json"), plugin("1.2.4", "\r\n"))
        self.assertEqual(repo.read("VERSION"), "1.2.4\r\n")
        log = repo.read("CHANGELOG.md")
        self.assertTrue(log.startswith("# Changelog\r\n\r\n## [1.2.4] - 2026-02-02\r\n"))
        self.assertNotIn("\n\n", log.replace("\r\n", ""))

    def test_changelog_section_is_inserted_once(self):
        repo = Repo(self)
        repo.run("bump", "minor", "--date", "2026-02-02")
        repo.run("set", "1.3.0", "--date", "2026-02-03")
        self.assertEqual(repo.read("CHANGELOG.md").count("## [1.3.0]"), 1)
        self.assertLess(repo.read("CHANGELOG.md").index("## [1.3.0]"), repo.read("CHANGELOG.md").index("## [1.2.3]"))

    def test_bump_refuses_disagreeing_manifests(self):
        repo = Repo(self)
        repo.write(".claude-plugin/marketplace.json", market("9.9.9"))
        self.assertEqual(repo.run("bump", "patch", "--date", "2026-02-02")[0], 1)

    def test_set_validates_and_repairs(self):
        repo = Repo(self)
        self.assertEqual(repo.run("set", "1.2")[0], 2)
        repo.write(".claude-plugin/marketplace.json", market("9.9.9"))
        self.assertEqual(repo.run("set", "2.0.0")[0], 0)
        self.assertEqual(repo.run("check")[0], 0)


class ThisRepo(unittest.TestCase):
    def test_manifests_agree_here(self):
        done = subprocess.run([sys.executable, str(TOOL), "--root", str(REPO), "check"], capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    def test_rule_58_is_enforced_by_ci_and_named(self):
        rule = (REPO / ".ai/rules/58-version-discipline.md").read_text(encoding="utf-8")
        self.assertIn("scripts/psychiatry_version.py", rule)
        self.assertIn("tests/test_version_discipline.py", rule)
        ci = (REPO / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        self.assertIn("psychiatry_version.py", ci)
        self.assertIn("check --base", ci)

    def test_release_documents_name_the_current_version(self):
        version = json.loads((REPO / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
        self.assertIn(f"## [{version}]", (REPO / "CHANGELOG.md").read_text(encoding="utf-8"))
        self.assertIn(f"## {version}", (REPO / "docs/listing/release-notes.md").read_text(encoding="utf-8"))
        self.assertIn(f"ai-psychiatry-{version}.zip", (REPO / "docs/publishing.md").read_text(encoding="utf-8"))
        self.assertTrue((REPO / f"dist/ai-psychiatry-{version}.zip").is_file())

    def test_the_skill_names_the_tool(self):
        skill = (REPO / "skills/all-the-medicine/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("psychiatry_version.py", skill)


if __name__ == "__main__":
    unittest.main()

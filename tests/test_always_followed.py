"""Always followed: both hooks wired in exec form, fast, harmless; the installers leave nothing behind."""

import json
import os
import shutil
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

from tests.helpers import REPO, load_json, read

LOUD = "NOT OPTIONAL"
SH = shutil.which("sh")
POWERSHELL = shutil.which("powershell") or shutil.which("pwsh")


def hook_commands(event):
    groups = load_json(REPO / "hooks/hooks.json")["hooks"][event]
    return [hook for group in groups for hook in group["hooks"]], groups


@unittest.skipUnless(SH, "needs a POSIX sh")
class HookTests(unittest.TestCase):
    def test_both_events_are_wired_in_exec_form(self):
        for event, script in (("SessionStart", "session-start.sh"), ("UserPromptSubmit", "prompt-reminder.sh")):
            hooks, _ = hook_commands(event)
            self.assertEqual(len(hooks), 1, event)
            hook = hooks[0]
            self.assertEqual(hook["type"], "command")
            self.assertEqual(hook["command"], "sh", "exec form: the shell form exits 126 under Git Bash")
            self.assertEqual(hook["args"], [f"${{CLAUDE_PLUGIN_ROOT}}/hooks/{script}"])
            self.assertTrue((REPO / "hooks" / script).is_file())

    def test_session_start_has_no_matcher_so_it_fires_on_every_source(self):
        _, groups = hook_commands("SessionStart")
        for group in groups:
            self.assertNotIn("matcher", group, "a matcher would skip resume, clear or compact")

    def test_only_these_two_events_exist(self):
        self.assertEqual(sorted(load_json(REPO / "hooks/hooks.json")["hooks"]), ["SessionStart", "UserPromptSubmit"])

    def run_script(self, name):
        return subprocess.run([SH, str(REPO / "hooks" / name)], capture_output=True, text=True, cwd=tempfile.gettempdir())

    def test_scripts_exit_zero_and_print(self):
        for name in ("session-start.sh", "prompt-reminder.sh"):
            done = self.run_script(name)
            self.assertEqual(done.returncode, 0, name)
            self.assertTrue(done.stdout.strip(), name)
            self.assertEqual(done.stderr, "", name)

    def test_prompt_reminder_is_two_short_lines_and_decides_nothing(self):
        out = self.run_script("prompt-reminder.sh").stdout
        lines = out.splitlines()
        self.assertLessEqual(len(lines), 3)
        self.assertTrue(all(len(line) <= 200 for line in lines))
        self.assertIn("no command needed", out)
        self.assertIn(LOUD, out)
        for word in ("permissionDecision", "deny", "decision\":"):
            self.assertNotIn(word, out)
        self.assertNotIn("{", out, "plain text only; JSON output could carry a decision")

    def test_prompt_reminder_is_fast(self):
        best = min(self.timed("prompt-reminder.sh") for _ in range(7))
        # Spec: under 50 ms. Process start under Git Bash on Windows costs more, so the bound is loose there.
        self.assertLess(best, 0.25 if os.name == "nt" else 0.05, f"best of 7 was {best * 1000:.0f} ms")

    def timed(self, name):
        start = time.perf_counter()
        self.run_script(name)
        return time.perf_counter() - start

    def test_prompt_reminder_reads_no_files(self):
        text = read(REPO / "hooks/prompt-reminder.sh")
        for token in ("cat ", " < ", "curl", "git ", "$(", "`"):
            self.assertNotIn(token, text)


class NoCommandNeededTests(unittest.TestCase):
    def test_the_one_contract_says_no_command_is_required(self):
        contract = read(REPO / "skills/all-the-medicine/references/always-on.md")
        self.assertIn("No command is required", contract)

    def test_installers_project_that_contract_to_codex_and_cursor(self):
        for name in ("install.sh", "install.ps1"):
            text = read(REPO / name)
            self.assertIn("references/always-on.md", text.replace("\\", "/"), name)
            self.assertIn("alwaysApply", text, name)
            self.assertIn("ai-psychiatry:begin", text, name)


class LoudContractTests(unittest.TestCase):
    """The agents skip a quiet plugin. The loud marker must survive in every output."""

    def test_marker_is_in_every_source(self):
        for rel in ("skills/all-the-medicine/references/always-on.md", "skills/all-the-medicine/SKILL.md",
                    "hooks/prompt-reminder.sh"):
            self.assertIn(LOUD, read(REPO / rel), rel)

    @unittest.skipUnless(SH, "needs a POSIX sh")
    def test_marker_is_in_every_output(self):
        for name in ("session-start.sh", "prompt-reminder.sh"):
            out = subprocess.run([SH, str(REPO / "hooks" / name)], capture_output=True, text=True).stdout
            self.assertIn(LOUD, out, name)
        self.assertLessEqual(len(subprocess.run([SH, str(REPO / "hooks/session-start.sh")],
                                                capture_output=True, text=True).stdout.splitlines()), 40)

    @unittest.skipUnless(SH, "needs a POSIX sh")
    def test_marker_reaches_the_codex_block_and_cursor_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "proj"
            repo.mkdir()
            done = subprocess.run([SH, str(REPO / "install.sh"), "--codex", "--cursor", "--repo", str(repo)],
                                  capture_output=True, text=True, env={**os.environ, "PSYCH_CLAUDE_BIN": "none"})
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
            self.assertIn(LOUD, read(repo / "AGENTS.md"))
            self.assertIn(LOUD, read(repo / ".cursor/rules/ai-psychiatry.mdc"))
            self.assertIn(LOUD, read(repo / ".agents/skills/all-the-medicine/SKILL.md"))

    def test_the_skill_stays_under_the_codex_limit(self):
        self.assertLessEqual(len((REPO / "skills/all-the-medicine/SKILL.md").read_bytes()), 8000)


def make_source(root: Path) -> Path:
    """A minimal committed checkout (branch main) the installer will accept."""
    src = root / "source"
    shutil.copytree(REPO / "skills/all-the-medicine", src / "skills/all-the-medicine",
                    ignore=shutil.ignore_patterns("references"))
    (src / "skills/all-the-medicine/references").mkdir()
    shutil.copy(REPO / "skills/all-the-medicine/references/always-on.md", src / "skills/all-the-medicine/references")
    (src / ".claude-plugin").mkdir()
    shutil.copy(REPO / ".claude-plugin/plugin.json", src / ".claude-plugin")
    for args in (("init", "-q", "-b", "main"), ("config", "--local", "user.name", "t"),
                 ("config", "--local", "user.email", "t@example.invalid"),
                 ("config", "--local", "commit.gpgsign", "false"), ("add", "-A"), ("commit", "-q", "-m", "x")):
        subprocess.run(["git", "-C", str(src), *args], check=True, capture_output=True)
    return src


def tree(root: Path):
    # AppData is created by Windows PowerShell itself, not by the installer.
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                  if "AppData" not in p.relative_to(root).parts)


class InstallerCleanupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / "home"
        (self.home / ".cursor").mkdir(parents=True)
        (self.home / ".codex").mkdir()
        for tool in (".cursor", ".codex"):  # the user's own, non-empty config dirs
            (self.home / tool / "settings.keep").write_text("mine", encoding="utf-8")
        self.env = {**os.environ, "PSYCH_USER_HOME": str(self.home), "CODEX_HOME": str(self.home / ".codex"),
                    "PSYCH_CLAUDE_BIN": "none", "HOME": str(self.home), "USERPROFILE": str(self.home)}
        self.env.pop("PSYCH_SOURCE", None)
        self.before = tree(self.home)

    @unittest.skipUnless(SH, "needs a POSIX sh")
    def test_sh_uninstall_removes_the_download_cache_it_created(self):
        src = make_source(self.root)
        env = {**self.env, "PSYCH_REPO_URL": src.as_posix()}
        install = subprocess.run([SH, "-s", "--", "--codex", "--cursor"], stdin=(REPO / "install.sh").open("rb"),
                                 env=env, capture_output=True, text=True)
        self.assertEqual(install.returncode, 0, install.stdout + install.stderr)
        cache = self.home / ".ai-psychiatry/src"
        self.assertTrue(cache.is_dir(), "the piped install should have downloaded to the cache")
        gone = subprocess.run([SH, str(REPO / "install.sh"), "--uninstall", "--codex", "--cursor"],
                              env=env, capture_output=True, text=True)
        self.assertEqual(gone.returncode, 0, gone.stdout + gone.stderr)
        self.assertEqual(tree(self.home), self.before, "uninstall must leave nothing behind")

    @unittest.skipUnless(SH, "needs a POSIX sh")
    def test_sh_uninstall_keeps_a_directory_that_is_not_our_checkout(self):
        stranger = self.home / ".ai-psychiatry/src"
        stranger.mkdir(parents=True)
        (stranger / "mine.txt").write_text("keep", encoding="utf-8")
        subprocess.run([SH, str(REPO / "install.sh"), "--uninstall", "--codex", "--cursor"],
                       env=self.env, capture_output=True, text=True, check=True)
        self.assertTrue((stranger / "mine.txt").exists())

    @unittest.skipUnless(POWERSHELL and os.name == "nt", "needs Windows PowerShell")
    def test_ps1_uninstall_removes_the_download_cache(self):
        cache = self.home / ".ai-psychiatry/src"
        shutil.copytree(make_source(self.root), cache, ignore=shutil.ignore_patterns(".git"))
        done = subprocess.run([POWERSHELL, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                               str(REPO / "install.ps1"), "-Uninstall", "-Codex", "-Cursor"],
                              env=self.env, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(tree(self.home), self.before, "uninstall must leave nothing behind")


if __name__ == "__main__":
    unittest.main()

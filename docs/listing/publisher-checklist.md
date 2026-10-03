# Publisher Checklist

Status: release `0.3.0` is published through the repository-hosted Claude/Codex marketplace and installed successfully on both CLIs. Community-directory submissions remain blocked by unauthenticated vendor portal sessions; approval must remain unclaimed until authenticated receipts exist.

Evidence recorded 2026-08-14:

- `python -m unittest discover -s tests -v`: 59 tests passed.
- `python scripts/validate_framework.py`: passed.
- `claude plugin validate .`: marketplace manifest passed.
- Codex `validate_plugin.py .`: plugin validation passed.
- Skill validator: all 75 public and installed skill definitions passed.
- Archive: 292 safe root-relative files; both manifests and all referenced runtime assets are present.
- The canonical 0-189 master prompt remains byte-for-byte unchanged; loophole and underthinking prompts are supplemental, progressively disclosed references.
- Baseline pressure tests found the existing framework already resisted core command/label laundering, false completion/blockers, and hidden-recursion pressure; release 0.3.0 adds deterministic, portable contracts and regression coverage.
- Official Claude and OpenAI publication requirements were reviewed against the 0.3.0 package.
- Git remote is `git@github.com:ihabkhaled/AI-Psychiatry.git`.
- Claude hosted-marketplace receipt: `ihabkhaled-ai` added at user scope; `ai-psychiatry@ihabkhaled-ai` installed successfully.
- Codex hosted-marketplace receipt: `ihabkhaled-ai` added from `main`; `ai-psychiatry@ihabkhaled-ai` version `0.3.0` installed successfully.
- Claude community submission portal redirected to `platform.claude.com/login?returnTo=%2Fplugins%2Fsubmit`.
- OpenAI Plugins Directory portal redirected to `platform.openai.com/login?next=%2Fplugins`.

- [x] Push the validated `0.3.0` release to `ihabkhaled/AI-Psychiatry` main (`cf2b84f`).
- [x] Add support, privacy, terms, listing copy, logo, and release notes.
- [x] Build and validate the 0.3.0 submission archive (no longer kept in the tree).
- [x] Claude hosted marketplace smoke test completed.
- [ ] Claude marketplace submission completed and identifier recorded.
- [x] Codex hosted marketplace smoke test completed.
- [ ] Codex Plugins Directory submission completed and identifier recorded.
- [ ] Publisher identity verified.
- [x] Support, privacy, and terms URLs prepared.
- [ ] Vendor approvals recorded before README says "published."

# Publisher Checklist

Status: release `0.2.0` is built and locally validated on branch `feat/ai-psychiatry-full-build`; vendor submission and approval are not yet evidenced.

Evidence recorded 2026-08-14:

- `python -m unittest discover -s tests -v`: 31 tests passed.
- `python scripts/validate_framework.py`: passed.
- `claude plugin validate .`: marketplace manifest passed.
- Codex `validate_plugin.py .`: plugin validation passed.
- Skill validator: all 37 public and installed skill definitions passed.
- Prompt traceability: exact titles and artifacts validated for sections 0 through 189.
- Fresh-context pressure tests: attention drift, compulsive checking, recursive work, unsupported claims, and livelock controls behaved as designed.
- Installed Claude and Codex CLIs expose validation/install/marketplace commands but no vendor submission command.
- Git remote is `git@github.com:ihabkhaled/AI-Psychiatry.git`.

- [ ] Push the validated `0.2.0` release to `ihabkhaled/AI-Psychiatry`.
- [ ] Claude local smoke test completed.
- [ ] Claude marketplace submission completed and identifier recorded.
- [ ] Codex local marketplace smoke test completed.
- [ ] Codex Plugins Directory submission completed and identifier recorded.
- [ ] Publisher identity verified.
- [ ] Support, privacy, and terms URLs supplied if required by the vendors.
- [ ] Vendor approvals recorded before README says "published."

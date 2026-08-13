# Publisher Checklist

Status: package built and locally validated on branch `feat/ai-psychiatry-full-build`; submission and vendor approval are not yet evidenced.

Evidence recorded 2026-08-14:

- `python -m unittest discover -s tests -v`: 15 tests passed.
- `python scripts/validate_framework.py`: passed.
- `claude plugin validate .`: marketplace manifest passed.
- Codex `validate_plugin.py .`: plugin validation passed.
- Installed Claude and Codex CLIs expose validation/install/marketplace commands but no vendor submission command.
- Git remote is `git@github.com:ihabkhaled/AI-Psychiatry.git`.

- [ ] Merge the validated feature branch and push the complete public repository to `ihabkhaled/AI-Psychiatry`.
- [ ] Claude local smoke test completed.
- [ ] Claude marketplace submission completed and identifier recorded.
- [ ] Codex local marketplace smoke test completed.
- [ ] Codex Plugins Directory submission completed and identifier recorded.
- [ ] Publisher identity verified.
- [ ] Support, privacy, and terms URLs supplied if required by the vendors.
- [ ] Vendor approvals recorded before README says “published.”

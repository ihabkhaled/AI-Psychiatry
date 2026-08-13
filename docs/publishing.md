# Publishing

## Claude Code

1. Run the full test suite and `claude plugin validate .`.
2. Smoke-test with `claude --plugin-dir .`.
3. Push the public GitHub repository, run `/plugin marketplace add ihabkhaled/AI-Psychiatry`, and install `ai-psychiatry@ihabkhaled-ai`.
4. Submit to the Claude community directory through `https://platform.claude.com/plugins/submit` (or the organization directory form for eligible Team/Enterprise accounts).
5. Record the submission identifier and later the approved `ai-psychiatry@claude-community` entry. A GitHub-hosted marketplace is installable before community-directory approval, but it does not automatically appear in Claude's curated search.

## OpenAI Codex

1. Run the full test suite and Codex plugin validator.
2. Build `dist/ai-psychiatry-0.3.0.zip` with the plugin manifests and `skills/` at the archive root.
3. Upload the archive as a skills-only plugin in the OpenAI Plugins Directory publisher portal.
4. Supply listing details, the positive and negative test cases, availability, and release notes; complete scans and authenticated publisher attestations.

Validation proves readiness, not marketplace acceptance. Record authenticated submission and vendor approval separately in the [publisher checklist](listing/publisher-checklist.md).


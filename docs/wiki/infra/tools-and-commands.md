# Tools and commands

<!-- akinator:generated:begin -->
<!-- Facts extracted from the tree. This block is rewritten on every run;
     write outside it. -->
### Commands

| Command | What | Where defined |
|---|---|---|
| `CI job test` | - | `.github/workflows/ci.yml` |
| `CI job version-discipline` | - | `.github/workflows/ci.yml` |
| `python scripts/__init__.py` | - | `scripts/__init__.py` |
| `python scripts/build_all_the_medicine.py` | Build the compiled all-the-medicine skill and rule references from the manifests. | `scripts/build_all_the_medicine.py` |
| `python scripts/build_release_manifests.py` | Regenerate AI-Psychiatry 0.3.0 catalogs from checked-in artifacts. | `scripts/build_release_manifests.py` |
| `python scripts/build_semantic_skills.py` | Build the paired public and installed semantic-control skill documents. | `scripts/build_semantic_skills.py` |
| `python scripts/build_submission_archive.py` | Build the portable skills-only marketplace submission archive. | `scripts/build_submission_archive.py` |
| `python scripts/build_traceability.py` | Generate prompt-section traceability from the canonical master prompt. | `scripts/build_traceability.py` |
| `python scripts/executive_control.py` | Deterministic policy assessor for observable coding-agent state. | `scripts/executive_control.py` |
| `python scripts/psychiatry_version.py` | AI-Psychiatry version discipline: one version, everywhere, bumped on every shipped change. | `scripts/psychiatry_version.py` |
| `python scripts/validate_framework.py` | Where a public skill lives. There is ONE plugin skill, all-the-medicine; | `scripts/validate_framework.py` |

### Required CLI tools

| Tool | Implied by |
|---|---|
| `gh` | `.github` |
| `git` | `.git`, `.github/workflows/ci.yml` |
| `python` | `.github/workflows/ci.yml`, `scripts/__init__.py`, `scripts/build_all_the_medicine.py` +7 more |

Regenerate with: `python <skill>/scripts/extract_operations.py --write`
<!-- akinator:generated:end -->

## Notes on tools and commands

Developer commands are in the [README](../../../README.md) (Developing). Regenerate compiled references with `python scripts/build_all_the_medicine.py`; never run `scripts/build_release_manifests.py` wholesale (it once dropped rules 56 and 57).

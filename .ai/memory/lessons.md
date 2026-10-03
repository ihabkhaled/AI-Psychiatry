# lessons

- A quiet contract is skipped. On 2026-10-03 an agent ignored the installed plugin until the owner yelled, then complied; the contract is now loud, aimed at the AI only, and repeated on every prompt.
- Never run `scripts/build_release_manifests.py` wholesale: it once dropped rules 56 and 57 (its list was cut at rule 55). Edit manifests in place; use `scripts/psychiatry_version.py` for versions.
- An uninstaller must remove every directory its installer created, including the download cache.


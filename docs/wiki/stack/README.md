# Stack

What this answers: languages, frameworks, runtime, versions.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which languages, frameworks, runtimes and versions does this run on, and which versions are pinned deliberately?

Python 3 (standard library; CI uses 3.12), POSIX shell for `install.sh` and the hooks, Windows PowerShell for `install.ps1`, Markdown and JSON for everything shipped. Claude Code hooks use the exec form (`"command": "sh"` with `args`) because the shell form exits 126 on Claude Code 2.1.154 under Git Bash. No version is pinned beyond that.

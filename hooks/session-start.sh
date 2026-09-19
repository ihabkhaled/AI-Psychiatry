#!/bin/sh
# AI-Psychiatry SessionStart hook: the always-on contract, printed from the one
# skill's reference so it has a single source.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
CONTRACT="$HERE/../skills/all-the-medicine/references/always-on.md"
[ -f "$CONTRACT" ] && tr -d '\r' < "$CONTRACT"
exit 0

#!/bin/sh
# AI-Psychiatry installer - Claude Code, Codex and Cursor, straight from GitHub.
#
#   curl -fsSL https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.sh | sh
#
# Always on. One skill, all-the-medicine, which is also the one command:
#   Claude Code  /ai-psychiatry:all-the-medicine   plugin + SessionStart hook
#   Codex        $all-the-medicine                 skill + a block in AGENTS.md
#   Cursor       /all-the-medicine                 skill + an alwaysApply rule
#
# Options: --claude --codex --cursor (default: every one detected), --repo PATH,
# --ref REF, --uninstall. Re-running updates. Removes only what it recognises as
# its own. Environment (testing): PSYCH_SOURCE, PSYCH_USER_HOME, CODEX_HOME,
# PSYCH_CLAUDE_BIN ('none' to skip).

set -eu

NAME="all-the-medicine"
PLUGIN="ai-psychiatry@ihabkhaled-ai"
REPO_URL="${PSYCH_REPO_URL:-https://github.com/ihabkhaled/AI-Psychiatry.git}"
USER_HOME="${PSYCH_USER_HOME:-$HOME}"
CODEX_DIR="${CODEX_HOME:-$USER_HOME/.codex}"
REF="main"; TARGET_REPO=""; UNINSTALL=0; WANT_CLAUDE=0; WANT_CODEX=0; WANT_CURSOR=0
BEGIN_MARK="<!-- ai-psychiatry:begin"
END_MARK="<!-- ai-psychiatry:end -->"
MARKER="AI-Psychiatry is always on"

usage() {
  cat <<'USAGE'
AI-Psychiatry installer - always-on executive control for Claude Code, Codex and Cursor.

  sh install.sh [--claude] [--codex] [--cursor] [--repo PATH] [--ref REF] [--uninstall]

Default: every platform detected on this machine. Re-run to update.
USAGE
}
say() { printf '%s\n' "$*"; }
warn() { printf 'warning: %s\n' "$*" >&2; }
die() { printf 'error: %s\n' "$*" >&2; exit 1; }

while [ $# -gt 0 ]; do
  case "$1" in
    --claude) WANT_CLAUDE=1; shift ;;
    --codex) WANT_CODEX=1; shift ;;
    --cursor) WANT_CURSOR=1; shift ;;
    --repo) [ $# -ge 2 ] || die "--repo needs a path"; TARGET_REPO="$2"; shift 2 ;;
    --ref) [ $# -ge 2 ] || die "--ref needs a branch or tag"; REF="$2"; shift 2 ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "unknown option: $1 (see --help)" ;;
  esac
done

if [ -n "$TARGET_REPO" ]; then
  [ -d "$TARGET_REPO" ] || die "not a directory: $TARGET_REPO"
  TARGET_REPO=$(CDPATH= cd -- "$TARGET_REPO" && pwd)
fi

find_claude() {
  if [ -n "${PSYCH_CLAUDE_BIN:-}" ]; then
    [ "$PSYCH_CLAUDE_BIN" = "none" ] && return 1
    printf '%s' "$PSYCH_CLAUDE_BIN"; return 0
  fi
  if command -v claude >/dev/null 2>&1; then command -v claude; return 0; fi
  found=""
  for c in "$USER_HOME"/.vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude \
           "$USER_HOME"/.vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude.exe; do
    [ -f "$c" ] && found="$c"
  done
  [ -n "$found" ] || return 1
  printf '%s' "$found"
}
CLAUDE_BIN=$(find_claude || true)

if [ "$WANT_CLAUDE$WANT_CODEX$WANT_CURSOR" = "000" ]; then
  [ -n "$CLAUDE_BIN" ] && WANT_CLAUDE=1
  if command -v codex >/dev/null 2>&1 || [ -d "$CODEX_DIR" ]; then WANT_CODEX=1; fi
  if command -v cursor >/dev/null 2>&1 || [ -d "$USER_HOME/.cursor" ]; then WANT_CURSOR=1; fi
  if [ -n "$TARGET_REPO" ]; then WANT_CODEX=1; WANT_CURSOR=1; fi
  [ "$WANT_CLAUDE$WANT_CODEX$WANT_CURSOR" != "000" ] || die "found none of Claude Code, Codex or Cursor. Name one: --claude, --codex or --cursor."
fi

# --- the source ---------------------------------------------------------------

is_checkout() { [ -f "$1/skills/$NAME/SKILL.md" ] && [ -f "$1/.claude-plugin/plugin.json" ]; }
LOCAL_SOURCE=0; SRC=""
if [ -n "${PSYCH_SOURCE:-}" ]; then
  is_checkout "$PSYCH_SOURCE" || die "PSYCH_SOURCE is not an AI-Psychiatry checkout"
  SRC=$(CDPATH= cd -- "$PSYCH_SOURCE" && pwd); LOCAL_SOURCE=1
else
  case "$0" in *install.sh)
    here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
    if is_checkout "$here"; then SRC="$here"; LOCAL_SOURCE=1; fi ;;
  esac
fi
if [ -z "$SRC" ] && [ "$UNINSTALL" -eq 0 ] && { [ "$WANT_CODEX" -eq 1 ] || [ "$WANT_CURSOR" -eq 1 ]; }; then
  SRC="$USER_HOME/.ai-psychiatry/src"
  if command -v git >/dev/null 2>&1; then
    if [ -d "$SRC/.git" ]; then
      git -C "$SRC" fetch --quiet --depth 1 origin "$REF"; git -C "$SRC" checkout --quiet --force FETCH_HEAD
    else
      rm -rf "$SRC"; mkdir -p "$(dirname -- "$SRC")"
      git clone --quiet --depth 1 --branch "$REF" "$REPO_URL" "$SRC"
    fi
  else
    rm -rf "$SRC"; mkdir -p "$SRC"
    curl -fsSL "https://codeload.github.com/ihabkhaled/AI-Psychiatry/tar.gz/$REF" | tar -xz -C "$SRC" --strip-components=1
  fi
  is_checkout "$SRC" || die "the download at $SRC is incomplete"
fi

# The always-on rules: the skill's body, without its frontmatter and without the
# acknowledgement meant for an explicit run. The skill stays the only copy.
rules() { tr -d '\r' < "$SRC/skills/$NAME/references/always-on.md"; }

# --- helpers ------------------------------------------------------------------

has_crlf() { [ -f "$1" ] && [ "$(tr -dc '\r' < "$1" | wc -c)" -gt 0 ]; }
to_lf() { awk '{ sub(/\r$/, ""); print }' "$1" > "$1.tmp" && mv "$1.tmp" "$1"; }
to_crlf() { awk '{ sub(/\r$/, ""); printf "%s\r\n", $0 }' "$1" > "$1.tmp" && mv "$1.tmp" "$1"; }
trim_tail() { awk '{ l[NR] = $0 } END { n = NR; while (n > 0 && l[n] == "") n--; for (i = 1; i <= n; i++) print l[i] }' "$1" > "$1.tmp" && mv "$1.tmp" "$1"; }
strip_block() {
  awk -v b="$BEGIN_MARK" -v e="$END_MARK" 'index($0, b) == 1 { s = 1; next } s && index($0, e) == 1 { s = 0; next } !s { print }' "$1" > "$1.tmp" && mv "$1.tmp" "$1"
}

write_block() {
  file="$1"; mkdir -p "$(dirname -- "$file")"
  crlf=0; if has_crlf "$file"; then crlf=1; to_lf "$file"; fi
  if [ -f "$file" ]; then strip_block "$file"; trim_tail "$file"; fi
  {
    if [ -s "$file" ]; then printf '\n'; fi
    printf '%s - installed by AI-Psychiatry; reinstall to update. Replaced on reinstall. -->\n' "$BEGIN_MARK"
    rules
    printf '%s\n' "$END_MARK"
  } >> "$file"
  if [ "$crlf" -eq 1 ]; then to_crlf "$file"; fi
  say "wrote the AI-Psychiatry block in $file"
  override="$(dirname -- "$file")/AGENTS.override.md"
  if { [ -n "$TARGET_REPO" ] && [ -e "$override" ]; } || [ -s "$override" ]; then
    warn "$override exists; Codex reads it INSTEAD of AGENTS.md there, so merge the block into it."
  fi
}

remove_block() {
  file="$1"; [ -f "$file" ] || return 0; grep -q "$BEGIN_MARK" "$file" || return 0
  crlf=0; if has_crlf "$file"; then crlf=1; to_lf "$file"; fi
  strip_block "$file"
  if [ -z "$(tr -d ' \t\r\n' < "$file")" ]; then rm -f "$file"; say "removed $file"; return 0; fi
  trim_tail "$file"
  if [ "$crlf" -eq 1 ]; then to_crlf "$file"; fi
  say "removed the AI-Psychiatry block from $file"
}

remove_ours() {
  f="$SKILLS_ROOT/$NAME/SKILL.md"
  if [ -f "$f" ] && grep -q "name: all-the-medicine" "$f"; then rm -rf "$SKILLS_ROOT/$NAME"; say "removed $SKILLS_ROOT/$NAME"; fi
}

if [ -n "$TARGET_REPO" ]; then
  SKILLS_ROOT="$TARGET_REPO/.agents/skills"; CONTRACT="$TARGET_REPO/AGENTS.md"
  RULE="$TARGET_REPO/.cursor/rules/ai-psychiatry.mdc"; SCOPE="project"
else
  SKILLS_ROOT="$USER_HOME/.agents/skills"; CONTRACT="$CODEX_DIR/AGENTS.md"
  RULE="$USER_HOME/.cursor/rules/ai-psychiatry.mdc"; SCOPE="user"
fi
claude_run() { if [ -n "$TARGET_REPO" ]; then (cd "$TARGET_REPO" && "$CLAUDE_BIN" "$@"); else "$CLAUDE_BIN" "$@"; fi; }

if [ "$UNINSTALL" -eq 1 ]; then
  if [ "$WANT_CLAUDE" -eq 1 ] && [ -n "$CLAUDE_BIN" ]; then
    claude_run plugin uninstall "$PLUGIN" --scope "$SCOPE" || warn "claude: $NAME was not installed"
  fi
  if [ "$WANT_CODEX" -eq 1 ] || [ "$WANT_CURSOR" -eq 1 ]; then remove_ours; fi
  if [ "$WANT_CODEX" -eq 1 ]; then remove_block "$CONTRACT"; fi
  if [ "$WANT_CODEX" -eq 1 ] || [ "$WANT_CURSOR" -eq 1 ]; then
    # The download cache an install created is ours too: leave nothing behind.
    CACHE="$USER_HOME/.ai-psychiatry/src"
    if is_checkout "$CACHE"; then rm -rf "$CACHE"; say "removed $CACHE"; fi
    rmdir "$USER_HOME/.ai-psychiatry" 2>/dev/null || true
  fi
  if [ "$WANT_CURSOR" -eq 1 ] && [ -f "$RULE" ] && grep -q "$MARKER" "$RULE"; then rm -f "$RULE"; say "removed $RULE"; fi
  for d in "$SKILLS_ROOT" "$(dirname -- "$SKILLS_ROOT")" "$(dirname -- "$RULE")" "$(dirname -- "$(dirname -- "$RULE")")"; do
    rmdir "$d" 2>/dev/null || true
  done
  say "AI-Psychiatry uninstalled."; exit 0
fi

if [ "$WANT_CLAUDE" -eq 1 ]; then
  if [ -z "$CLAUDE_BIN" ]; then
    warn "Claude Code CLI not found. In VS Code: /plugins -> Marketplaces -> add $REPO_URL -> install."
  else
    if [ "$LOCAL_SOURCE" -eq 1 ]; then MARKET="$SRC"; else MARKET="$REPO_URL#$REF"; fi
    claude_run plugin marketplace add "$MARKET" --scope "$SCOPE"
    claude_run plugin install "$PLUGIN" --scope "$SCOPE" || true
    claude_run plugin update "$PLUGIN" --scope "$SCOPE" >/dev/null 2>&1 || true
    say "Claude Code: installed ($SCOPE scope). Restart Claude."
  fi
fi

if [ "$WANT_CODEX" -eq 1 ] || [ "$WANT_CURSOR" -eq 1 ]; then
  remove_ours
  mkdir -p "$SKILLS_ROOT"
  cp -R "$SRC/skills/$NAME" "$SKILLS_ROOT/$NAME"
  say "installed the skill to $SKILLS_ROOT/$NAME"
fi
if [ "$WANT_CODEX" -eq 1 ]; then write_block "$CONTRACT"; fi
if [ "$WANT_CURSOR" -eq 1 ]; then
  mkdir -p "$(dirname -- "$RULE")"
  { printf -- '---\ndescription: AI-Psychiatry - always-on executive control\nalwaysApply: true\n---\n\n'; rules; } > "$RULE"
  say "wrote $RULE"
fi
say "Done. AI-Psychiatry is always on. Re-run to update; --uninstall to remove."

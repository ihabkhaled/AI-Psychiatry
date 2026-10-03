<#
.SYNOPSIS
    AI-Psychiatry installer for Windows - always-on executive control.
.DESCRIPTION
    One line:  irm https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.ps1 | iex
    Options:   & ([scriptblock]::Create((irm https://raw.githubusercontent.com/ihabkhaled/AI-Psychiatry/main/install.ps1))) -Repo C:\src\app

    Claude Code: plugin + SessionStart hook. Codex: the skill + a block in AGENTS.md.
    Cursor: the skill + an alwaysApply rule. Re-run to update. Removes only what it
    recognises as its own. Environment (testing): PSYCH_SOURCE, PSYCH_USER_HOME,
    CODEX_HOME, PSYCH_CLAUDE_BIN ('none' to skip).
#>
[CmdletBinding()]
param([switch]$Claude, [switch]$Codex, [switch]$Cursor, [string]$Repo, [string]$Ref = 'main', [switch]$Uninstall)

$ErrorActionPreference = 'Stop'
$Name = 'all-the-medicine'
$Plugin = 'ai-psychiatry@ihabkhaled-ai'
$RepoUrl = if ($env:PSYCH_REPO_URL) { $env:PSYCH_REPO_URL } else { 'https://github.com/ihabkhaled/AI-Psychiatry.git' }
$UserHome = if ($env:PSYCH_USER_HOME) { $env:PSYCH_USER_HOME } elseif ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
$CodexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $UserHome '.codex' }
$BeginMark = '<!-- ai-psychiatry:begin'
$EndMark = '<!-- ai-psychiatry:end -->'
$Marker = 'AI-Psychiatry is always on'
$Utf8 = New-Object System.Text.UTF8Encoding($false)

function Say([string]$T) { Write-Host $T }
function Write-Utf8([string]$P, [string]$T) {
    $d = Split-Path -Parent $P; if ($d -and -not (Test-Path $d)) { New-Item -ItemType Directory -Force $d | Out-Null }
    [IO.File]::WriteAllText($P, $T, $Utf8)
}
function Read-Lf([string]$P) { [IO.File]::ReadAllText($P, $Utf8) -replace "`r`n", "`n" }
function Test-Crlf([string]$P) { (Test-Path $P) -and [IO.File]::ReadAllText($P, $Utf8).Contains("`r`n") }
function Write-Endings([string]$P, [string]$T, [bool]$Crlf) { if ($Crlf) { $T = $T -replace "`n", "`r`n" }; Write-Utf8 $P $T }

if ($Repo) { if (-not (Test-Path $Repo -PathType Container)) { throw "not a directory: $Repo" }; $Repo = (Resolve-Path $Repo).Path }

function Find-Claude {
    if ($env:PSYCH_CLAUDE_BIN) { if ($env:PSYCH_CLAUDE_BIN -eq 'none') { return $null }; return $env:PSYCH_CLAUDE_BIN }
    $c = Get-Command claude -ErrorAction SilentlyContinue; if ($c) { return $c.Source }
    $ext = Join-Path $UserHome '.vscode\extensions'
    if (Test-Path $ext) {
        $b = Get-ChildItem $ext -Directory -Filter 'anthropic.claude-code-*' | ForEach-Object { Join-Path $_.FullName 'resources\native-binary\claude.exe' } |
            Where-Object { Test-Path $_ } | Sort-Object { [version](($_ -split 'anthropic\.claude-code-')[1] -split '-')[0] } | Select-Object -Last 1
        if ($b) { return $b }
    }
    return $null
}
$ClaudeBin = Find-Claude

if (-not ($Claude -or $Codex -or $Cursor)) {
    if ($ClaudeBin) { $Claude = $true }
    if ((Get-Command codex -ErrorAction SilentlyContinue) -or (Test-Path $CodexDir)) { $Codex = $true }
    if ((Get-Command cursor -ErrorAction SilentlyContinue) -or (Test-Path (Join-Path $UserHome '.cursor'))) { $Cursor = $true }
    if ($Repo) { $Codex = $true; $Cursor = $true }
    if (-not ($Claude -or $Codex -or $Cursor)) { throw 'found none of Claude Code, Codex or Cursor. Name one: -Claude, -Codex or -Cursor.' }
}

function Test-Checkout([string]$D) { (Test-Path (Join-Path $D "skills\$Name\SKILL.md")) -and (Test-Path (Join-Path $D '.claude-plugin\plugin.json')) }
$LocalSource = $false; $Src = $null
if ($env:PSYCH_SOURCE) {
    if (-not (Test-Checkout $env:PSYCH_SOURCE)) { throw 'PSYCH_SOURCE is not an AI-Psychiatry checkout' }
    $Src = (Resolve-Path $env:PSYCH_SOURCE).Path; $LocalSource = $true
} elseif ($PSScriptRoot -and (Test-Checkout $PSScriptRoot)) { $Src = $PSScriptRoot; $LocalSource = $true }

if (-not $Src -and -not $Uninstall -and ($Codex -or $Cursor)) {
    $Src = Join-Path $UserHome '.ai-psychiatry\src'
    if (Get-Command git -ErrorAction SilentlyContinue) {
        if (Test-Path (Join-Path $Src '.git')) {
            git -C $Src fetch --quiet --depth 1 origin $Ref; git -C $Src checkout --quiet --force FETCH_HEAD
        } else {
            if (Test-Path $Src) { Remove-Item -Recurse -Force $Src }
            git clone --quiet --depth 1 --branch $Ref $RepoUrl $Src; if ($LASTEXITCODE) { throw 'git clone failed' }
        }
    } else {
        $zip = Join-Path ([IO.Path]::GetTempPath()) "ai-psychiatry-$Ref.zip"; $un = Join-Path ([IO.Path]::GetTempPath()) "ai-psychiatry-$Ref"
        Invoke-WebRequest -UseBasicParsing -Uri "https://codeload.github.com/ihabkhaled/AI-Psychiatry/zip/$Ref" -OutFile $zip
        if (Test-Path $un) { Remove-Item -Recurse -Force $un }; Expand-Archive $zip $un
        if (Test-Path $Src) { Remove-Item -Recurse -Force $Src }
        New-Item -ItemType Directory -Force (Split-Path -Parent $Src) | Out-Null
        Move-Item (Get-ChildItem $un -Directory | Select-Object -First 1).FullName $Src
    }
    if (-not (Test-Checkout $Src)) { throw "the download at $Src is incomplete" }
}

# The always-on rules: the skill body minus frontmatter and minus the
# acknowledgement meant for an explicit run. The skill stays the only copy.
function Get-Rules {
    (Read-Lf (Join-Path $Src "skills\$Name\references\always-on.md")).TrimEnd("`n") + "`n"
}

if ($Repo) {
    $SkillsRoot = Join-Path $Repo '.agents\skills'; $Contract = Join-Path $Repo 'AGENTS.md'
    $Rule = Join-Path $Repo '.cursor\rules\ai-psychiatry.mdc'; $Scope = 'project'
} else {
    $SkillsRoot = Join-Path $UserHome '.agents\skills'; $Contract = Join-Path $CodexDir 'AGENTS.md'
    $Rule = Join-Path $UserHome '.cursor\rules\ai-psychiatry.mdc'; $Scope = 'user'
}

function Remove-BlockText([string]$T) {
    [regex]::Replace($T, '(?ms)^' + [regex]::Escape($BeginMark) + '.*?^' + [regex]::Escape($EndMark) + '[^\n]*\n?', '')
}
function Remove-Ours {
    $f = Join-Path $SkillsRoot "$Name\SKILL.md"
    if ((Test-Path $f) -and (Select-String -Path $f -SimpleMatch 'name: all-the-medicine' -Quiet)) {
        Remove-Item -Recurse -Force (Split-Path -Parent $f); Say "removed $(Split-Path -Parent $f)"
    }
}
function Invoke-Claude([string[]]$A) {
    if ($Repo) { Push-Location $Repo }
    try { & $ClaudeBin @A | Out-Host; return $LASTEXITCODE } finally { if ($Repo) { Pop-Location } }
}

if ($Uninstall) {
    if ($Claude -and $ClaudeBin) { $null = Invoke-Claude @('plugin', 'uninstall', $Plugin, '--scope', $Scope) }
    if ($Codex -or $Cursor) { Remove-Ours }
    if ($Codex -and (Test-Path $Contract)) {
        $crlf = Test-Crlf $Contract; $t = Read-Lf $Contract
        if ($t.Contains($BeginMark)) {
            $rest = (Remove-BlockText $t).TrimEnd("`n", ' ', "`t")
            if ($rest) { Write-Endings $Contract "$rest`n" $crlf } else { Remove-Item -Force $Contract }
            Say "removed the AI-Psychiatry block from $Contract"
        }
    }
    if ($Cursor -and (Test-Path $Rule) -and (Select-String -Path $Rule -SimpleMatch $Marker -Quiet)) { Remove-Item -Force $Rule; Say "removed $Rule" }
    if ($Codex -or $Cursor) {
        # The download cache an install created is ours too: leave nothing behind.
        $Cache = Join-Path $UserHome '.ai-psychiatry\src'
        if (Test-Checkout $Cache) { Remove-Item -Recurse -Force $Cache; Say "removed $Cache" }
        $CacheRoot = Split-Path -Parent $Cache
        if ((Test-Path $CacheRoot) -and -not (Get-ChildItem -Force $CacheRoot)) { Remove-Item -Force $CacheRoot }
    }
    foreach ($d in @($SkillsRoot, (Split-Path -Parent $SkillsRoot), (Split-Path -Parent $Rule), (Split-Path -Parent (Split-Path -Parent $Rule)))) {
        if ((Test-Path $d) -and -not (Get-ChildItem -Force $d)) { Remove-Item -Force $d }
    }
    Say 'AI-Psychiatry uninstalled.'; return
}

if ($Claude) {
    if (-not $ClaudeBin) { Write-Warning "Claude Code CLI not found. In VS Code: /plugins -> Marketplaces -> add $RepoUrl -> install." }
    else {
        $market = if ($LocalSource) { $Src } else { "$RepoUrl#$Ref" }
        if (Invoke-Claude @('plugin', 'marketplace', 'add', $market, '--scope', $Scope)) { throw 'claude plugin marketplace add failed' }
        $null = Invoke-Claude @('plugin', 'install', $Plugin, '--scope', $Scope)
        $null = Invoke-Claude @('plugin', 'update', $Plugin, '--scope', $Scope) 2>$null
        Say "Claude Code: installed ($Scope scope). Restart Claude."
    }
}
if ($Codex -or $Cursor) {
    Remove-Ours
    New-Item -ItemType Directory -Force $SkillsRoot | Out-Null
    Copy-Item -Recurse -Force (Join-Path $Src "skills\$Name") (Join-Path $SkillsRoot $Name)
    Say "installed the skill to $(Join-Path $SkillsRoot $Name)"
}
if ($Codex) {
    $crlf = Test-Crlf $Contract
    $existing = if (Test-Path $Contract) { (Remove-BlockText (Read-Lf $Contract)).TrimEnd("`n", ' ', "`t") } else { '' }
    $block = "$BeginMark - installed by AI-Psychiatry; reinstall to update. Replaced on reinstall. -->`n" + (Get-Rules) + "$EndMark`n"
    $text = if ($existing) { "$existing`n`n$block" } else { $block }
    Write-Endings $Contract $text $crlf
    Say "wrote the AI-Psychiatry block in $Contract"
    $override = Join-Path (Split-Path -Parent $Contract) 'AGENTS.override.md'
    if ((Test-Path $override) -and ($Repo -or (Get-Item $override).Length -gt 0)) { Write-Warning "$override exists; Codex reads it INSTEAD of AGENTS.md there, so merge the block into it." }
}
if ($Cursor) {
    Write-Utf8 $Rule ("---`ndescription: AI-Psychiatry - always-on executive control`nalwaysApply: true`n---`n`n" + (Get-Rules))
    Say "wrote $Rule"
}
Say 'Done. AI-Psychiatry is always on. Re-run to update; -Uninstall to remove.'

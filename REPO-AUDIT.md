# Repo Audit

> **Auto-generated — do not hand-edit.** Regenerated and verified on every
> `plugin-release.sh` run. Every number here is counted from the filesystem at
> release time, and the release **fails** if `plugin.json`'s description
> disagrees with what is actually on disk. Hand-maintained counts drift; this
> one cannot.

**Version:** `1.4.15`  ·  **Commit:** `b269f74`  ·  **Generated:** 16 Jul 2026 18:13

## Totals

| Metric | Count |
|---|---:|
| **Total tracked files** | **236** |
| **Skills** (`SKILL.md`) | **82** |
| Supporting files inside `skills/` | 108 |
| Slash commands | 11 |

## Verified against `plugin.json`

The description claims a split; these are checked against the filesystem every release.

| Bucket | Claimed | Actual | |
|---|---:|---:|:--:|
| Total skills | 82 | 82 | ✔ |
| AI-PM skills | 64 | 64 | ✔ |
| General-purpose | 17 | 17 | ✔ |
| Slash commands | 11 | 11 | ✔ |
| Orchestrator | 1 | 1 | ✔ |

Version fields are locked in step: `plugin.json` = `marketplace.json` metadata = `marketplace.json` plugins[0] = **1.4.15**.

## Composition

| Area | Files |
|---|---:|
| `skills` | 190 |
| `diagrams` | 15 |
| `commands` | 11 |
| `workflows` | 6 |
| `frameworks` | 4 |
| `.claude-plugin` | 2 |
| `.gitignore` | 1 |
| `ARCHITECTURE.md` | 1 |
| `CLAUDE.md` | 1 |
| `COMPANION-PLUGINS.md` | 1 |
| `LICENSE` | 1 |
| `README.md` | 1 |
| `UNIVERSAL-SKILL-PROTOCOL.md` | 1 |
| `companion-plugins.json` | 1 |

## AI-PM layers (counted in `2_Skills/ai-pm-skills/`)

| Layer | Skills |
|---|---:|
| agent-design | 6 |
| ai-strategy | 11 |
| craft | 10 |
| eval-and-quality | 6 |
| product-sense | 14 |
| safety-and-trust | 7 |
| thinking-core | 11 |
| **7-layer total** | **65** |

The repo mirrors **64** of these. The difference is `rtp-failure-design`,
a redirect stub merged into `failure-modes` — intentionally excluded from the plugin.

## Supporting files inside `skills/`

82 skills carry 108 supporting files (1.3 per skill).

| Type | Count |
|---|---:|
| `.md` | 100 |
| `.svg` | 7 |
| `.py` | 1 |

## Name mapping (repo ↔ source)

These folders are renamed for plugin namespacing; content is identical to source.

| Repo folder | `2_Skills` folder |
|---|---|
| `rtp-aipm-orchestrator` | `rtp-orchestrator` |
| `rtp-personal-branding` | `rtp-ravi-personal-branding` |
| `rtp-research-synthesiser` | `rtp-grok-perplexity-research` |
| `rtp-thinking-skills` | `rtp-ravi-thinking-skills` |

## History

| Version | Commit | Generated | Files | Skills | Commands |
|---|---|---|---:|---:|---:|
<!--HISTORY
| 1.4.14 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |
| 1.4.15 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |
HISTORY-->
| 1.4.14 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |
| 1.4.15 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |

# Repo Audit

> **Auto-generated — do not hand-edit.** Regenerated and verified on every
> `plugin-release.sh` run. Every number here is counted from the filesystem at
> release time, and the release **fails** if `plugin.json`'s description
> disagrees with what is actually on disk. Hand-maintained counts drift; this
> one cannot.

**Version:** `1.7.0`  ·  **Commit:** `81e461c`  ·  **Generated:** 18 Jul 2026 09:58

## Totals

| Metric | Count |
|---|---:|
| **Total tracked files** | **242** |
| **Skills** (`SKILL.md`) | **84** |
| Supporting files inside `skills/` | 111 |
| Slash commands | 11 |

## Verified against `plugin.json`

The description claims a split; these are checked against the filesystem every release.

| Bucket | Claimed | Actual | |
|---|---:|---:|:--:|
| Total skills | 84 | 84 | ✔ |
| AI-PM skills | 65 | 65 | ✔ |
| General-purpose | 18 | 18 | ✔ |
| Slash commands | 11 | 11 | ✔ |
| Orchestrator | 1 | 1 | ✔ |

Version fields are locked in step: `plugin.json` = `marketplace.json` metadata = `marketplace.json` plugins[0] = **1.7.0**.

## Composition

| Area | Files |
|---|---:|
| `skills` | 195 |
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
| `REPO-AUDIT.md` | 1 |
| `UNIVERSAL-SKILL-PROTOCOL.md` | 1 |
| `companion-plugins.json` | 1 |

## AI-PM layers (counted in `2_Skills/ai-pm-skills/`)

| Layer | Skills |
|---|---:|
| agent-design | 6 |
| ai-strategy | 11 |
| craft | 11 |
| eval-and-quality | 6 |
| product-sense | 14 |
| safety-and-trust | 7 |
| thinking-core | 11 |
| **7-layer total** | **66** |

The repo mirrors **65** of these. The difference is `rtp-failure-design`,
a redirect stub merged into `failure-modes` — intentionally excluded from the plugin.

## Supporting files inside `skills/`

84 skills carry 111 supporting files (1.3 per skill).

| Type | Count |
|---|---:|
| `.md` | 103 |
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
| 1.5.0 | 71dc8e3 | 17 Jul 2026 06:47 | 237 | 83 | 11 |
| 1.6.0 | b4f1b68 | 17 Jul 2026 21:22 | 238 | 84 | 11 |
| 1.7.0 | 81e461c | 18 Jul 2026 09:58 | 242 | 84 | 11 |
HISTORY-->
| 1.4.14 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |
| 1.4.15 | b269f74 | 16 Jul 2026 18:13 | 236 | 82 | 11 |
| 1.5.0 | 71dc8e3 | 17 Jul 2026 06:47 | 237 | 83 | 11 |
| 1.6.0 | b4f1b68 | 17 Jul 2026 21:22 | 238 | 84 | 11 |
| 1.7.0 | 81e461c | 18 Jul 2026 09:58 | 242 | 84 | 11 |

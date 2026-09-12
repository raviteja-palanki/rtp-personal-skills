# Repo Audit

> **Auto-generated — do not hand-edit.** Regenerated and verified on every
> `plugin-release.sh` run. Every number here is counted from the filesystem at
> release time, and the release **fails** if `plugin.json`'s description
> disagrees with what is actually on disk. Hand-maintained counts drift; this
> one cannot.

**Version:** `2.7.3`  ·  **Commit:** `d629378`  ·  **Generated:** 12 Sep 2026 09:35

## Totals

| Metric | Count |
|---|---:|
| **Total tracked files** | **258** |
| **Skills** (`SKILL.md`) | **90** |
| Supporting files inside `skills/` | 119 |
| Slash commands | 11 |

## Verified against `plugin.json`

The description claims a split; these are checked against the filesystem every release.

| Bucket | Claimed | Actual | |
|---|---:|---:|:--:|
| Total skills | 90 | 90 | ✔ |
| AI-PM skills | 67 | 67 | ✔ |
| General-purpose | 22 | 22 | ✔ |
| Slash commands | 11 | 11 | ✔ |
| Orchestrator | 1 | 1 | ✔ |

Version fields are locked in step: `plugin.json` = `marketplace.json` metadata = `marketplace.json` plugins[0] = **2.7.3**.

## Composition

| Area | Files |
|---|---:|
| `skills` | 209 |
| `diagrams` | 16 |
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
| `_archived-skills` | 1 |
| `companion-plugins.json` | 1 |

## AI-PM layers (counted in `2_Skills/ai-pm-skills/`)

| Layer | Skills |
|---|---:|
| agent-design | 6 |
| ai-strategy | 12 |
| craft | 11 |
| eval-and-quality | 7 |
| product-sense | 14 |
| safety-and-trust | 7 |
| thinking-core | 11 |
| **7-layer total** | **68** |

The repo mirrors **67** of these. The difference is `rtp-failure-design`,
a redirect stub merged into `failure-modes` — intentionally excluded from the plugin.

## Supporting files inside `skills/`

90 skills carry 119 supporting files (1.3 per skill).

| Type | Count |
|---|---:|
| `.md` | 111 |
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
| 1.15.0 | 4b5f570 | 30 Aug 2026 08:07 | 252 | 88 | 11 |
| 1.16.0 | 2a902e4 | 30 Aug 2026 14:56 | 252 | 88 | 11 |
| 1.16.1 | 6b59a46 | 30 Aug 2026 14:59 | 252 | 88 | 11 |
| 1.17.0 | 2791a2f | 30 Aug 2026 15:33 | 252 | 88 | 11 |
| 2.0.0 | 404b360 | 30 Aug 2026 16:07 | 252 | 88 | 11 |
| 2.1.0 | 77e350e | 30 Aug 2026 18:26 | 252 | 88 | 11 |
| 2.2.0 | c3802c4 | 31 Aug 2026 01:24 | 252 | 88 | 11 |
| 2.3.0 | ac86e05 | 31 Aug 2026 04:43 | 252 | 88 | 11 |
| 2.4.0 | af49123 | 31 Aug 2026 05:01 | 252 | 88 | 11 |
| 2.5.0 | 57d5ca6 | 31 Aug 2026 05:15 | 252 | 88 | 11 |
| 2.6.0 | ac8b38e | 31 Aug 2026 09:59 | 252 | 88 | 11 |
| 2.7.0 | 9c667a0 | 10 Sep 2026 03:24 | 257 | 90 | 11 |
| 2.7.1 | b70ece0 | 10 Sep 2026 22:17 | 257 | 90 | 11 |
| 2.7.2 | d7d0797 | 11 Sep 2026 03:04 | 258 | 90 | 11 |
| 2.7.3 | d629378 | 12 Sep 2026 09:35 | 258 | 90 | 11 |
HISTORY-->
| 1.15.0 | 4b5f570 | 30 Aug 2026 08:07 | 252 | 88 | 11 |
| 1.16.0 | 2a902e4 | 30 Aug 2026 14:56 | 252 | 88 | 11 |
| 1.16.1 | 6b59a46 | 30 Aug 2026 14:59 | 252 | 88 | 11 |
| 1.17.0 | 2791a2f | 30 Aug 2026 15:33 | 252 | 88 | 11 |
| 2.0.0 | 404b360 | 30 Aug 2026 16:07 | 252 | 88 | 11 |
| 2.1.0 | 77e350e | 30 Aug 2026 18:26 | 252 | 88 | 11 |
| 2.2.0 | c3802c4 | 31 Aug 2026 01:24 | 252 | 88 | 11 |
| 2.3.0 | ac86e05 | 31 Aug 2026 04:43 | 252 | 88 | 11 |
| 2.4.0 | af49123 | 31 Aug 2026 05:01 | 252 | 88 | 11 |
| 2.5.0 | 57d5ca6 | 31 Aug 2026 05:15 | 252 | 88 | 11 |
| 2.6.0 | ac8b38e | 31 Aug 2026 09:59 | 252 | 88 | 11 |
| 2.7.0 | 9c667a0 | 10 Sep 2026 03:24 | 257 | 90 | 11 |
| 2.7.1 | b70ece0 | 10 Sep 2026 22:17 | 257 | 90 | 11 |
| 2.7.2 | d7d0797 | 11 Sep 2026 03:04 | 258 | 90 | 11 |
| 2.7.3 | d629378 | 12 Sep 2026 09:35 | 258 | 90 | 11 |

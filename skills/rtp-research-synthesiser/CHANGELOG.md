# Research Synthesiser — Changelog

## v2.0.0 — 4 APR 2026

### Redesigned — On-Demand Dimension-Based Architecture
This is a fundamental redesign, not an incremental update.

### Key Changes from v1.1
- **On-demand invocation** replaces fixed schedule. Ravi fires synthesis when ready.
- **One dimension per run** replaces "process everything at once." 10 runs for full weekly coverage.
- **Perplexity Notion page IDs added.** Both SuperGrok and Perplexity now read from Notion via MCP.
- **Perplexity schedule timing corrected.** All 10 Perplexity Spaces fire weekly on Saturday morning (5:00-9:00 AM IST), not staggered across the week.
- **10 synthesis dimensions defined** with explicit Grok↔Perplexity↔Module mappings.
- **Cross-temporal pattern recognition** is now a mandatory step, not optional. Every finding checked against rules.md, hypotheses.md, and previous digests.
- **Thought leadership seeds** are non-optional output for every dimension digest.
- **URL library by category** — every digest collects must-read and reference links.
- **Proprietary framework application** — CONTEXT, SHARP, Moat half-lives, Explore/Expand/Extract, Inner/Outer World, 3 PM Cultures are explicitly integrated.
- **n8n + FireCrawl pipeline acknowledged** in architecture diagram.
- **Rolling 1-month data window** with monthly Google Drive archival.
- **Dimension digest template** replaces the monolithic weekly report for individual runs.
- **Weekly summary report** rolls up all dimension digests after full cycle.

### Removed
- Fixed Wednesday + Sunday schedule (v1.1 proposal)
- Daily triage mode (replaced by on-demand flexibility)
- Separate Stream 1/2/3 extraction (replaced by per-dimension output that covers all streams)

## v1.1.0 — 3 APR 2026

### Added
- Notion-first ingestion protocol with page ID registry for all 10 schedule pages
- Chunked processing (3 batches) to handle context window limits
- Daily Triage mode for lightweight mid-week signal checking
- Deduplication protocol for overlapping accounts across schedules
- Prompt feedback loop producing concrete, copy-paste-ready prompt refinements
- Perplexity Space quality assessment in synthesis report
- Account watchlist change recommendations
- Priority ordering for time-limited sessions (Interview > Skills > Course)
- Mode 4: Prompt Refinement invocation mode

### Fixed
- Schedule name mismatches (v1.0 used abbreviated names that didn't match actual SuperGrok task names)
- Module mapping table now uses exact schedule names and correct Perplexity Space names
- Module 05 (UX for AI) gap acknowledged — no dedicated schedule, draws from multiple sources
- Schedule 7 (Claude Code & Cowork Mastery) elevated as primary feeder for Stream 3 (Skill Updates)
- Synthesis report now reviews all 10 schedules AND all 10 Perplexity Spaces separately

### Changed
- Input source for SuperGrok signals changed from local files to Notion pages via MCP
- Architecture diagram updated to show full pipeline: SuperGrok → n8n → Notion → Claude
- Schedule Performance Review table corrected from "20 schedules" to separate tables for 10 SuperGrok + 10 Perplexity

## v1.0 — 3 APR 2026
- Initial version

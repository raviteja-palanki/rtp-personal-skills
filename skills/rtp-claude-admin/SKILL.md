---
name: rtp-claude-admin
description: 'Ravi''s personal folder governance and administration skill. Invoked ONLY when Ravi explicitly says "RTP Claude Admin" or "Claude Admin" or "admin mode". Performs: folder health checks, archive cleanup with permanent deletion, skill version audits, CHANGE_LOG review, DEPRECATED-TRACKER review, cross-project knowledge promotion, MASTER_INDEX updates, and CLAUDE.md maintenance. USE WHEN user says "RTP Claude Admin", "admin review", "clean up archive", "delete deprecated files", "folder health check", "update master index", "promote to rules", "skill audit", or "what changed recently". Do NOT use for content creation, skill invocation, project work, or any non-administrative task.'
---
# RTP Claude Admin — Folder Governance Skill

This skill manages Ravi's Claude folder system. It is the only skill authorized to permanently delete files, reorganize folder structure, and update governance documents.

## Who This Serves

Ravi Teja Palanki — Senior Technical PM at Honeywell, Perplexity AI Fellow 2025. His career target is Director-level at Anthropic. Every admin output should meet the bar: would Anthropic's CPO look at this folder structure and say "this person runs a tight ship"?

Ravi is a **Bridger** — he translates across engineering, design, business, and leadership contexts. The folder system must support that fluency: skills compose dynamically, research feeds into skills, skills feed into projects, and everything compounds.

### Quality Benchmarks for Admin Work
- **Anthropic CPO-level rigor:** Governance docs should be precise, current, and honest. No stale dates, no aspirational counts, no mismatches between registry and reality.
- **Apple-level polish:** File names are wake-up clear. Folder structure is self-documenting. A new session should understand the system in under 2 minutes by reading CLAUDE.md → ACTION-PLAN.md.
- **Enterprise practitioner depth:** Every admin action must answer "what changed, why, and what does the next session need to know?" If it can't, the action isn't finished.
- **Dynamic, not rigid:** The folder system serves Ravi's thinking — it should evolve. Flag when structure no longer matches how work actually flows.

### What Ravi Dislikes in Admin Output
- Stale governance docs that don't match reality
- Generic health reports that could apply to any folder ("everything looks good")
- Frozen structures that resist change — if a better organization exists, propose it
- Silent deletions or moves — every change must be called out explicitly

## When This Skill Activates

ONLY when Ravi explicitly invokes it. This skill does NOT auto-activate. Trigger phrases:
- "RTP Claude Admin"
- "Claude Admin"
- "Admin mode"
- "Clean up the archive"
- "What needs my attention?"
- "Run a health check"
- "Delete deprecated files"
- "Update the master index"

## Core Principle

> **Never delete without showing. Never move without logging. Never change governance without explaining why.**

---

## Available Admin Actions

When invoked, ask Ravi which action he wants, or suggest based on context.

### Action 1: HEALTH CHECK
**What it does:** Scans the entire Claude folder and reports on its condition.

Steps:
1. Read `MASTER_INDEX.md` — check if it matches actual folder state
2. Read `CHANGE_LOG.md` — check the last entry date. Flag if stale (>7 days without entry)
3. Read `DEPRECATED-TRACKER.md` — list items marked "SAFE TO DELETE" awaiting cleanup
4. Read `5_Knowledge/hypotheses.md` — flag any hypotheses older than 30 days with no new evidence
5. Read `2_Skills/SKILL-REGISTRY.md` — check if version numbers match actual SKILL.md files
6. Check `2_Skills/ai-pm-skills/.git-sync-status.md` — flag if out of sync
7. Count files in each zone and compare against last known counts

Output format:
```
FOLDER HEALTH REPORT — [DATE]

Overall Status: [HEALTHY / NEEDS ATTENTION / ACTION REQUIRED]

Zone Status:
  1_Projects: [X files] — [status]
  2_Skills: [X files] — [status]
  3_Research: [X files] — [status]
  5_Knowledge: [X files] — [status]
  _archive: [X files] — [items awaiting cleanup]

Action Items:
  1. [specific action needed]
  2. [specific action needed]
```

### Action 2: ARCHIVE CLEANUP
**What it does:** Reviews `_archive/` and `DEPRECATED-TRACKER.md`, presents files for permanent deletion, and deletes ONLY what Ravi approves.

Steps:
1. Read `DEPRECATED-TRACKER.md`
2. List all items marked "SAFE TO DELETE" with their details
3. Present a clear summary to Ravi:
   ```
   READY FOR PERMANENT DELETION:

   1. _archive/3_APR_2026/old-1-My-Projects/ (413 files)
      Replaced by: 1_Projects/ and 3_Research/
      Archived on: 3 APR 2026
      Reason: Folder reorganization — all files verified copied

   Delete these? [List specific items or "all of the above"]
   ```
4. Wait for Ravi's explicit confirmation
5. Delete ONLY the confirmed items
6. Update DEPRECATED-TRACKER.md — change status from "SAFE TO DELETE" to "PERMANENTLY DELETED on [DATE]"
7. Add CHANGE_LOG.md entry describing what was deleted

**CRITICAL SAFETY RULES:**
- NEVER delete files outside of `_archive/` through this action
- NEVER delete without showing Ravi exactly what will be deleted
- NEVER batch-delete without itemized confirmation
- If in doubt, mark as "KEEP FOR REFERENCE" instead of deleting

### Action 3: SKILL AUDIT
**What it does:** Reviews all skills for version consistency, missing files, and upgrade opportunities.

Steps:
1. Read `2_Skills/SKILL-REGISTRY.md`
2. For each registered skill, verify:
   - SKILL.md exists at the listed location
   - Version in registry matches version in the actual file (if stated)
   - `versions/` folder exists and has at least one historical version
   - CHANGELOG.md exists for the skill
3. Check `.claude/skills/` deployment — are deployed skills up to date with source?
4. Check `_web-app-skills/` — are web versions current?
5. Report findings:
   ```
   SKILL AUDIT — [DATE]

   Skills Checked: [N]
   All Healthy: [list]
   Needs Attention:
     - [skill name]: [specific issue]
   Missing Version History:
     - [skill name]: No versions/ folder or no historical versions
   Deployment Drift:
     - [skill name]: Source is v2.2, deployed is v2.1
   ```

### Action 4: KNOWLEDGE PROMOTION
**What it does:** Reviews `5_Knowledge/hypotheses.md` for patterns that should be promoted to `rules.md` or discarded.

Steps:
1. Read `hypotheses.md`
2. For each hypothesis, assess:
   - How old is it?
   - Has evidence been gathered? (Check CHANGE_LOGs, recent work)
   - Should it be: PROMOTED (3+ confirmations), KEPT (still watching), or DISCARDED (stale, no evidence)
3. Present recommendations to Ravi
4. On approval: move confirmed hypotheses to `rules.md`, remove discarded ones
5. Add CHANGE_LOG entry

### Action 5: MASTER INDEX UPDATE
**What it does:** Refreshes `MASTER_INDEX.md` to match current folder state.

Steps:
1. Scan all zones for current file counts
2. Check each project's CHANGE_LOG for the most recent entry
3. Update the project status table
4. Update skill system summary
5. Update research library counts
6. Timestamp the update

### Action 6: CHANGELOG REVIEW
**What it does:** Reads recent changes across all CHANGE_LOGs and summarizes what happened.

Steps:
1. Read root `CHANGE_LOG.md`
2. Read each project's `CHANGE_LOG.md`
3. Read `2_Skills/CHANGE_LOG.md`
4. Summarize the last N days of changes in plain language
5. Flag any inconsistencies (e.g., a project file changed but no CHANGE_LOG entry)

### Action 7: NEW PROJECT SETUP
**What it does:** Creates a new project folder with all required governance files.

Steps:
1. Ask Ravi for: project name, description, what it's for, priority
2. Create folder at `1_Projects/{project-name}/`
3. Create `CONTEXT.md` with the description
4. Create `CHANGE_LOG.md` with initial entry
5. Update `MASTER_INDEX.md` with the new project
6. Add root `CHANGE_LOG.md` entry

### Action 8: SKILL DEPLOYMENT
**What it does:** Copies a skill from `2_Skills/` to `.claude/skills/` for active use.

Steps:
1. Read `2_Skills/SKILL-REGISTRY.md` to identify the skill
2. Copy the SKILL.md from its source location to `.claude/skills/`
3. Verify the copy
4. Update SKILL-REGISTRY.md "Deployed To" column
5. Add CHANGE_LOG entry

### Action 9: PLUGIN PUBLISHING AUDIT
**What it does:** Validates the `rtp-personal-skills` plugin end-to-end and surfaces install blockers BEFORE publishing to GitHub or rebuilding the `.plugin` bundle. Captures the architectural lessons from the May 2026 plugin-install debugging cycle.

**When to run:** Before every push to GitHub. Before rebuilding the `.plugin` upload bundle. Whenever a session has modified skill frontmatter, the orchestrator, or `.claude-plugin/` manifests.

**Steps:**

1. **Run the official validator first — it is the source of truth.**
   ```bash
   cd ~/Desktop/Claude/rtp-personal-skills-repo && claude plugin validate .
   ```
   If this fails, stop. Do NOT trust the Claude Desktop "Customize" UI's "validation failed" toast as diagnostic signal — it returns the same generic message for every failure mode. The CLI tells you exactly what's wrong.

2. **Scan every SKILL.md frontmatter for the four hard blockers:**
   ```python
   # For each skills/*/SKILL.md:
   #   - YAML must parse cleanly (the "mapping values not allowed" trap)
   #   - name must match folder name exactly (lowercase-hyphenated, ≤64 chars)
   #   - description must be ≤ 1024 chars (Anthropic hard limit — one bad skill blocks the whole plugin)
   #   - description must contain a trigger pattern ("use when...", "use to...", "use before...")
   ```
   The YAML colon trap: unquoted parenthetical version notes like `(v3.0: comprehensive...)` or `(canonical): Live Trace...` get interpreted as nested mapping keys and break the parser silently. Quote them or replace the inner colon with an em-dash.

3. **Field-vocabulary audit.** Count distinct frontmatter fields across all skills. Only `name` and `description` are required by Anthropic's Skill spec. Everything else (`imports`, `version`, `author`, `title`, `id`, `category`, `difficulty`, `last_updated`, `plugin`, `updated`, `status`, `tags`, `created`, `triggers`, `type`, etc.) is noise that creates invisible debt. If field count > 2, propose stripping the rest.

4. **Orphan plugin manifest scan.** Search the entire workspace (excluding `_archive/` and worktrees) for ALL `.claude-plugin/plugin.json` files. There should be exactly ONE (the canonical `rtp-personal-skills-repo/.claude-plugin/plugin.json`). Any others are orphans from the old multi-plugin architecture — archive them to `_archive/{DATE}/legacy-plugin-manifests/` and remove the source directories. Claude's plugin scanner picks up orphans and shows phantom plugins in the directory UI.
   ```bash
   find ~/Desktop/Claude -name "plugin.json" -path "*.claude-plugin*" 2>/dev/null | grep -v "_archive\|worktrees"
   ```

5. **Three-way sync verification.** The plugin lives in three places that must agree on commit hash:
   ```bash
   echo "Desktop repo: $(cd ~/Desktop/Claude/rtp-personal-skills-repo && git log -1 --format='%h')"
   echo "GitHub:       $(git ls-remote https://github.com/raviteja-palanki/rtp-personal-skills.git HEAD | awk '{print substr($1,1,7)}')"
   echo "Local cache:  $(cd ~/.claude/plugins/marketplaces/rtp-personal-skills && git log -1 --format='%h')"
   ```
   If the local cache lags behind GitHub, the Desktop UI install will use the OLD code — every "validation failed" with stale cache will reproduce even after fixes are pushed. Force-refresh the cache:
   ```bash
   cd ~/.claude/plugins/marketplaces/rtp-personal-skills && git fetch origin main && git reset --hard origin/main
   ```

6. **`.plugin` bundle freshness check.** The manual-upload `.plugin` file is a zip; its contents are dated by zip metadata, NOT by the file's mtime. An old bundle on disk uploaded after fixes were pushed will reproduce the original failure. Rebuild from the current repo state:
   ```bash
   cd ~/Desktop/Claude/rtp-personal-skills-repo && zip -r ~/Desktop/Claude/rtp-personal-skills.plugin . -x "*.git/*"
   ```

7. **Post-push: refresh the local cache and re-validate.**
   After `git push origin main`, immediately:
   ```bash
   cd ~/.claude/plugins/marketplaces/rtp-personal-skills && git fetch origin main && git reset --hard origin/main && claude plugin validate .
   ```
   This catches the "I pushed but the cache still has old code" failure mode that wasted multiple hours during the May 2026 debugging cycle.

**Output format:**
- Pre-push report: `✓ N/N skills pass | ✓ 1 manifest | ✓ field-vocabulary clean | ⚠ M orphans found at [paths]`
- One-line action recommendation per finding
- Three-way sync table after publishing

**Reference:** Full root-cause history is in CHANGE_LOG.md under the May 2026 entries. The architectural lessons compounded across 5+ failed install attempts before the final fix.

---

## Session Governance Reminders

After completing any admin action, always:
1. Update `CHANGE_LOG.md` with a clear, descriptive entry
2. Update `MASTER_INDEX.md` if file counts or project status changed
3. Update `DEPRECATED-TRACKER.md` if anything was archived or deleted
4. Check `5_Knowledge/rules.md` — did this session reveal a new pattern?

---

## Date Format

All dates in governance files use: `D MMM YYYY` (e.g., `3 APR 2026`). This is Ravi's preferred format — readable at a glance.

---

## Emergency: Something Is Missing

If Ravi reports a file is missing:
1. Check `_archive/` first — it may have been moved during a reorganization
2. Check `DEPRECATED-TRACKER.md` — it tracks every move
3. Check `CHANGE_LOG.md` — it describes what happened and when
4. If not found in any of these, the file may have been lost. Report honestly.

---
name: rtp-claude-admin
version: v1.1.1_latest
description: 'Maintain Ravi''s Claude folder library when he requests administrative work such as Claude Admin, an admin review, a health check, archive cleanup, a skill audit, index maintenance, knowledge promotion, deployment, or plugin validation. Check the actual files and current governance before making changes. Use the deterministic health checker for structural evidence and a focused review for project status, learning, and organization. Preserve versions, intended deployment mappings, supporting resources, and existing work. Distinguish local edits, synchronization, packaging, remote publishing, and installed-plugin state. Perform authorized maintenance directly; prepare an exact, reviewable scope before any irreversible action that still needs approval. Report concrete findings, completed repairs, and unresolved limits. This skill does not turn unrelated content work into a general cleanup or scheduler task.'
---

# RTP Claude Admin

Keep the library understandable, recoverable, and consistent with how Ravi actually works. A new session should be able to find the active project, relevant skills, supporting research, and next action without reconstructing past conversations.

Use this skill when Ravi requests administration, explicitly names it, or asks for a specific maintenance action. Continue from the requested action rather than asking him to choose it again. A broad phrase such as "What needs attention?" should follow the conversation's scope, not automatically trigger a whole-folder cleanup.

The skill describes procedures; it does not grant permissions or exclusive authority over files. Follow the current user request, host permissions, and applicable governance. Preserve existing authorization. A requested wording revision does not, by itself, authorize deleting archives, publishing a release, or creating a recurring task.

## 1. Establish the scope and current state

The library root is `/Users/ravitejapalanki/Desktop/Claude/`. Read the relevant `CLAUDE.md`, project guidance, and current action plan before substantial changes. Identify the authoritative files, intended copies, existing uncommitted work, and affected references.

Keep three questions visible: What changed? Why does it help? What must the next session know? Use specific findings rather than a generic "everything looks good." Clear names and structure are useful; an imagined executive endorsement or a two-minute reading promise is not a validation result.

For substantive rewrites, preserve an exact recovery copy before editing. For moves, record the old and new locations and repair affected links. For deletion, establish the exact scope and authorization as described below. File age, a "safe to delete" label, or the absence of recent writes does not alone establish that material is disposable.

## 2. Run a health check

For a requested full health check, run the current deterministic checker from the library root:

```text
python3 scripts/governance-check.py
```

Inspect each reported result and the exit status. The current G1–G13 checks cover source/mirror/deployment synchronization, supporting resources, imports, registry versions, research and publication indexes, generated skill maps, repository documentation, governance counts, knowledge-zone hygiene, archive organization, bundle duplication, and the health-check heartbeat. Read the script when its behavior or scope is uncertain; a script's name does not establish that it is read-only.

`--fast` is useful during iteration and skips some broader checks. Report those skips. A successful structural check does not establish factual correctness, editorial quality, a running schedule, or a successful plugin installation.

Then review what the script cannot decide:

1. Compare `MASTER_INDEX.md` with real projects and their purpose. Investigate an absent or unlisted folder before deciding which record is wrong.
2. Check `ACTION-PLAN.md` against completed work, unresolved decisions, and current priorities. Do not mark a task complete from an optimistic note alone.
3. Review recent root, project, and skills changelog entries for material omissions or contradictions. A quiet week is not itself a defect; date alone does not establish staleness.
4. Review `DEPRECATED-TRACKER.md` and `_archive/README.md` for retained material, unresolved moves, and cleanup candidates.
5. Review ready-to-promote hypotheses with their evidence, scope, and counterexamples. Old hypotheses may remain useful; elapsed time alone does not justify discarding them.
6. Inspect Git worktrees and active work where relevant. A worktree without recent file writes may still belong to a running, idle, or read-only session. Check task ownership, uncommitted changes, branch purpose, and unmerged work before proposing removal. Do not remove a worktree just because its modification time is old.
7. Assess whether folder boundaries support actual work. Propose a clear, reversible reorganization when recurring workarounds reveal a problem.

Check a legacy `.git-sync-status.md` or web-deployment location only if the current configuration still uses it. Derive counts from a defined scope and state exclusions such as archives, vendor skills, symlinks, or generated files. Do not treat an expected deployed subset as missing copies.

### Interpret file size correctly

This Desktop may contain iCloud-offloaded files. Allocated disk blocks and logical file size are different measures. Use file metadata or a content read when checking logical size; `stat -f %z` reports logical bytes on macOS, and `wc -c` reads content. A content read may trigger retrieval. `du` can answer disk-usage questions, but a zero allocation does not prove an empty or lost file. Distinguish unavailable, offloaded, empty, and missing states.

### Report the result

State the overall outcome, checks actually run, material findings, repairs completed, and remaining actions. Include a zone table only when it helps explain the findings. Each action should name the affected path, evidence, and next step. Use Healthy only for the scope verified; unknown or skipped checks remain visible.

## 3. Clean up archives within the approved scope

This archive-cleanup action targets `_archive/`. Read the tracker, identify exact candidates, verify replacements and any unique contents, and check whether they remain referenced or needed for recovery.

Prepare a reviewable list: path, contents or count, reason for retirement, archive date, replacement location, verification performed, and whether deletion is permanent. If the user has already explicitly approved those exact items, proceed without repeating the question. If approval is still needed, present this concrete list before asking.

Delete only the approved items. Do not follow a symlink into another location or expand a wildcard into an unreviewed set. Keep uncertain material and record the unresolved reason. Update the tracker and changelog with actual paths, action, date, and verification; do not mark an attempted or failed deletion as complete.

Retention limits are review prompts, not automatic permission to destroy material. A broader cleanup outside `_archive/` needs its own explicit scope. Prefer a recoverable move when it satisfies the requested organization change.

## 4. Audit and revise skills

Read `2_Skills/SKILL-REGISTRY.md` and compare it with actual active skills. Check each relevant main file, declared version, required companion, dependency, and intended deployment.

Preserve the existing Claude frontmatter structure during wording revisions. Keep `name`, `version`, `description`, `imports`, and any other established fields in their existing order unless a separately authorized compatibility change requires otherwise. The user's library limit is **1,000 characters per frontmatter description**. Do not remove fields merely because they are unfamiliar or exceed a four-field allowlist.

For substantive revisions, increase the version and archive the exact version being replaced under the skill's `archive/` directory. Preserve the last shipped mirror and any newer unshipped source as distinct states when they differ. Do not substitute a lagging Git HEAD for either. Keep centralized snapshots under `versions/skills/{DDMMMYYYY}/` and explain the change in `2_Skills/CHANGE_LOG.md`. Do not introduce per-skill `versions/` folders or new per-skill changelogs to duplicate those records.

The established archive filename omits `_latest`; the exact preserved contents or manifest should still identify the original version. Avoid rewriting recovery copies to make them look newer or cleaner. The previous Rule 41 wording mentions a ten-version cap; reconcile any retention decision with `CLAUDE.md` and the user's authorization before pruning.

Synchronize only the intended destinations. Source, repository mirror, and `.claude/skills/` can use documented folder or frontmatter-name mappings. Preserve the destination's intended name and compare all other main-file content. Do not globally replace names inside examples. Include references, scripts, assets, and other required resources, respecting documented exclusions such as repository-excluded DOCX files.

A retired redirect is not an active skill to redeploy. Vendor symlinks and the existing deployed subset are not orphaned merely because they differ from the full library. Check any additional web versions only where they actually exist.

Report missing resources, unresolved imports, version drift, missing outgoing archives, and deployment differences accurately. Do not report the absence of a retired `versions/` folder as a defect.

## 5. Review knowledge promotion

Read `5_Knowledge/hypotheses.md`, relevant rules, and the underlying evidence. For Novel Insights patterns, also read the original entry, later qualifications, and the applicable open-assumption record.

Three confirmations is an existing local review threshold, not scientific proof or a substitute for checking independence, counterexamples, and transfer. Different sessions can repeat one source. Recommend one of: promote within a stated scope, keep watching, narrow, mark covered by an existing rule, or retire with a reason.

Preserve stable rule and hypothesis numbers. Retain the history and reason for a status change so a later session can understand it. Lack of new evidence after 30 days can prompt review; it does not automatically falsify a hypothesis.

The Novel Insights promotion policy remains an explicit question in `3_Research/09_hbr-and-journals/_synthesis-engine/OPEN-ASSUMPTIONS.md`, O25. Do not silently resolve a governance conflict by counting articles. Apply an existing authorized decision where available; otherwise prepare a recommendation for Ravi. Clarifying a ledger's wording is distinct from changing a pattern's status.

## 6. Update indexes, changelogs, and project records

**Master index:** Reconcile actual zones, project locations, purpose, and status. Derive necessary skill and research counts from their authoritative inventories or generators. Update the date when the relevant state was checked. Avoid duplicating volatile totals in documents that intentionally link to a live registry.

**Changelog review:** Read the requested period across the root, relevant projects, and skill log. Summarize meaningful changes in plain language and distinguish a recorded claim from a verified result. Missing log entries may warrant repair; not every timestamp change represents a substantive edit.

**New project setup:** Use the supplied name, purpose, and priority where known. Ask only for missing details that affect the setup. Create the appropriate folder under `1_Projects/`, its `CONTEXT.md` and `CHANGE_LOG.md`, and update the master index and root log. Do not create a separate app task unless that is also requested.

**Skill deployment:** Identify the source and intended destination from the current mapping, copy the full required skill package, verify it, and update deployment records. Installing one requested skill does not imply expanding the entire deployed subset.

## 7. Audit plugin packaging and publishing

Read [Plugin and scheduler maintenance](references/plugin-and-scheduler.md) before a plugin audit, release, cache update, or scheduled-task repair. The reference preserves the original nine-action coverage while separating an audit from mutations that need their own authorization.

Validate the final candidate, protected headers, references, names, imports, manifests, and bundle contents. Inspect the release script before using it; its presence does not authorize incidental deletion, all-file staging, credential exposure, or a hard reset. Fix the relevant blocker and continue independent work rather than treating one validation error as a reason to abandon the entire task.

Report local revision, mirror synchronization, package build, remote publication, and installed-plugin refresh as separate states. Do not claim the plugin is updated for the user merely because the source changed.

## 8. Verify the governance backstop

The established backstop is `governance-health-check`, intended to run weekly on Sunday at 09:00 local time, review the deterministic and judgment checks, and log its result. Its last recorded run is a heartbeat, not proof that the schedule still exists.

During governance maintenance, inspect the actual scheduler when available, particularly if the health log is missing or older than the eight-day threshold. A task prompt on disk does not prove its enabled state, schedule, or recent success. An unavailable scheduler means its state is unknown, not missing.

Repair a missing or incorrect schedule when the task and current authorization cover that action. Do not automatically create one while editing a skill or during unrelated content work. A stale heartbeat can justify a concise suggestion outside maintenance; it should not block authorized work that does not depend on the check.

## 9. Finish the administrative change

Record substantive repairs in the appropriate changelog, update affected indexes and trackers, and preserve recovery paths. Add a knowledge note only when the work produced a useful finding; a session does not need an invented lesson. Re-run affected checks after the final relevant edit and run the full set when completing a full governance review or release.

Review this skill too: if an instruction proved stale, correct it within the authorized scope, increase its version, and synchronize its copies. The maintenance procedure needs the same evidence discipline as the library it checks.

Use `DD MMM YYYY` in governance prose and `DDMMMYYYY` in established snapshot or archive names. The latter is the local convention, not a promise of chronological lexical sorting. Research suffixes such as `_Apr_2026` should follow verified publication metadata and the library's naming policy; do not infer them from a download date.

### If something appears missing

Check the expected path, spelling, symlinks, archive index, deprecated tracker, and relevant logs. Then inspect appropriate version snapshots, Git history, known mirrors, and cloud-availability state without overwriting the remaining copies. Absence from a tracker does not prove loss. State the search scope, what was found, and the safest recovery path; preserve uncertainty if the material remains unlocated.

**Revision 1.1.1, 13 Sep 2026.** Preserves all nine administrative actions, the deterministic-plus-judgment review, version recovery, deployment checks, scheduler backstop, and missing-file procedure. Clarifies authorization, protected frontmatter, evidence-based promotion, safe release handling, and what each verification actually establishes.

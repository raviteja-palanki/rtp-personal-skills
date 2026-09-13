---
name: rtp-skill-refresh
version: v1.0.2_latest
description: 'Refresh existing skills without losing their purpose, evidence, or connections. Use for a requested library revision, a periodic review, a defective output, Ravi’s feedback, or research that changes guidance. Read each skill and relevant companions fully, understand its inputs and handoffs, then review content, structure, voice, and integrity as distinct passes. Preserve exact recovery copies before editing, keep Claude frontmatter structure intact, increase the version, and keep each description within 1,000 characters. Exercise consequential workflows with realistic cases and distinguish desk review from actual tool execution. Retain useful linked references while removing conflicting duplicate instructions. Finish with synchronized local copies, accurate change records, governance checks, and the requested plugin refresh. Remote publication is a separate action when authorized. Pair with rtp-claude-admin for governance and the relevant research and skill-creation guidance.'
imports:
  - claude-admin
---
# Skill refresh

Keep the skill library clear, current, and usable as a connected system. A refresh should improve the decisions or actions a skill supports while preserving its useful mechanisms, evidence, and handoffs. Finish through the requested local synchronization and plugin update, with an accurate record of what changed and what was checked.

## Choose the right depth

A requested full-library revision, signature-skill review, or substantive research update deserves a complete pass. A specific defect deserves a focused fix plus the checks affected by it. A typo needs proportionate review; follow the user's versioning instruction and current governance rather than silently treating it as exempt. Creating a new skill belongs with `skill-creator`; an urgent defective output should be repaired before a lengthy maintenance exercise.

Use a concrete reason for an edit: Ravi's request, a failure trace, unclear wording, contradictory instructions, a research correction, a renamed dependency, a missing handoff, or an observed usability problem. **An explicit clarity review is sufficient reason to inspect and improve a skill**; it does not require manufacturing a prior incident. Periodic review can find a defect, but age alone does not prove the content is wrong. A reviewed skill may need no change.

Honor the requested scope and working mode. If Ravi asks for all ninety skills sequentially, maintain a sequential ledger and complete that scope; do not reduce it to a small batch or delegate for convenience. For an open-ended maintenance cycle, choose a manageable slate that can reach a verified close. A “monthly” convention does not create a schedule by itself.

## Understand the skill before changing it

Read the complete current `SKILL.md`, relevant companion instructions, examples, schemas, and scripts. An index or heading scan is navigation, not a full reading. Use progressive reading only for resources that are optional and outside the change; record what was actually inspected.

Identify:

- the user's decision or task, and when the skill applies;
- what it consumes, including named upstream skills and required context;
- its distinctive computation, framework, examples and constraints;
- what it produces and which downstream work relies on it;
- source claims, assumptions, thresholds, syntax and factual limits that must survive;
- current aliases, canonical location, mirror and any deployed copies.

Consult `2_Skills/SKILL-REGISTRY.md`, `2_Skills/STRUCTURE.md`, and the relevant tracker. Current maintenance records include `2_Skills/ai-pm-skills/REFINEMENT-TRACKER.md`, `SKILL-REVISION-PLAN.md`, and `2_Skills/CHANGE_LOG.md`. Read relevant evidence in `5_Knowledge/session-anti-patterns.md`, user reviews, research update maps and synthesis digests. Do not treat an old “next action” or historical migration queue as the current assignment.

For **each skill revision**, re-read the current Novel Insights guide and the relevant pattern entries, including later challenges. Ask what useful instruction the evidence supports for this skill. Record the pattern considered and whether it changed the wording. Do not add a pattern merely to demonstrate that the ledger was consulted.

## Preserve a recovery copy first

Before changing a canonical skill or companion, capture its exact current bytes and record the source path and version. Recheck the source hash before installation to detect concurrent edits. Reconcile a mismatch rather than overwriting someone else's work.

Use the skill-local `archive/SKILL-vX.Y[.Z].md` and the established central dated backup when appropriate. **Keep the recovery copy exact**, including its original frontmatter; its archive path identifies it as historical. Do not strip `_latest` from the only recovery copy and then describe it as byte-identical. Archive files must be excluded from active-skill discovery.

Never overwrite an existing different archive or prune old versions automatically as a side effect of editing. Retention cleanup is separate from this task and requires the applicable authorization. Include changed references and scripts in recovery records, not just the main file.

Preserve the existing Claude frontmatter keys, order, names, import values and structure unless the user specifically authorizes a structural change. In this library wording pass, change only the version and description. Keep each description at **1,000 characters or fewer** after parsing, and preserve the `_latest` version convention. A compatible wording/fix revision can use a patch increase; a broader compatible addition may use minor, and a changed core contract may use major. A version bump describes a real revised file, not a proposal.

## Four distinct review passes

### 1. Content and connections

Reason from the skill's purpose and evidence. Preserve every useful mechanism, example, question family, schema, formula, limitation, and source relationship. Label illustrative numbers and verify consequential claims that may be wrong or stale. Prefer the relevant primary record; a prestige label or repeated citation does not establish the claim.

Use named neighboring skills for their deeper methods without making the current skill unusable in isolation. Short orientation and fallback context can be helpful; needless duplication of a whole framework creates drift. A handoff needs enough substance for its receiver to act.

If content moves to another skill, confirm that the destination actually contains it and update callers in the same authorized change. Otherwise record **routing debt**: source, destination, exact content owed, owner and verification condition. Do not delete the only usable explanation because the destination name sounds appropriate.

### 2. Structure and workflow

Place purpose, consequential prerequisites, decision points and safety/authority limits before the details that depend on them. Give the reader an actionable sequence and a clear stopping or completion condition. Use tables for true comparisons, lists for parallel or sequential material, and prose for reasoning that needs a connected explanation.

Design each skill's shape around its job: a diagnostic may need a symptom-to-action guide; a generator may need a template; a reference may need one compact table. A quick answer does not need a document, scorecard, universal questionnaire or every downstream artifact. Review both the instruction file and the output it asks the agent to produce.

Long examples, detailed catalogs and source notes can live in linked references. Keep essential operating rules in the main skill, provide clear “read when” links, and avoid circular or missing references. Do not impose a fixed section count, eight-line paragraph limit or mandatory bold label on every list.

### 3. Voice and clarity

Apply `rtp-thinking-writing`, with `rtp-humanizer` for a specific unresolved pattern when helpful. Use plain verbs, explain unfamiliar terms, and state the intended action directly. Replace scolding, inflated claims and ambiguous absolutes with clear instructions whose strength fits their purpose.

Keep a firm requirement when it matters. Explain its reason or boundary where that prevents misuse; not every sentence needs a separate “why” and “when wrong” section. Avoid claiming that perfect wording guarantees nobody will ever make a mistake. Read the revised text naturally and resolve sentences that require guessing the intended behavior.

### 4. Integrity and preservation

Check the final version after the last edit:

- YAML parses; protected fields and imports are unchanged; description is within 1,000 characters; version increased as intended.
- Skill names and aliases resolve; main and companion links, headings, section numbers, formulas and schemas remain consistent.
- Renamed terms propagate through descriptions, tables, templates and examples. Search for the superseded term rather than relying on memory.
- Current claims carry relevant dates and scope. Historical quotations and archived versions remain historical.
- Code fences close, examples identify required variables/assets, and executable snippets are checked appropriately. Valid parsing does not establish runtime correctness.
- The preservation record accounts for what remained, moved, changed or was deliberately retired and why.

Use automation for mechanical checks and reasoning for meaning. Keep the four passes distinct in attention; do not call one quick skim four reviews. Use `rtp-ai-prd` as an example of sound reasoning and handoffs, reading its current version rather than copying a historic v1.2 outline.

## Exercise consequential behavior

For signature or complex workflows, apply the revised instructions to a realistic case and a meaningful constraint: missing optional input, contradictory evidence, a failed tool, a narrow deadline, or a consequential action requiring authorization. Check whether the skill can reach a useful result without loops, invented facts or unnecessary questions. Record the case, expected behavior, observed friction and changes made.

Where the revision affects execution, perform the relevant tool/run/render checks when available. A desk walkthrough can find ambiguity but does not establish browser behavior, a successful deployment, a readable printed artifact or an independent review. Use an independent reviewer when the task permits and it adds value; a “Test Manager” persona in the same agent is still self-review. Respect Ravi's request for main-agent sequential work.

The earlier AI-PRD cold-run record reportedly found seven defects after structural reviews missed them. Preserve the lesson—exercise the workflow—without claiming this is the only method that can find execution defects or that every skill needs an elaborate simulation. If a required execution check cannot run, record the specific gap and its implication instead of inventing a pass.

## Keep companions coherent

Read an existing `CONCEPT.md` before deciding its future. Preserve useful atomic insights, worked examples and intellectual lineage. If it duplicates or contradicts the main instructions, consolidate those instructions into the main file or a clearly linked reference and update all affected links.

A distinct, maintained concept guide or reference is legitimate. Do not archive it merely because a historical audit found other concept files stale. If retiring a companion is appropriate and authorized, retain a recovery copy and verify that every useful part is preserved elsewhere. Do not mass-delete unreviewed material or keep two competing operational authorities.

## Close the actual requested work

1. Install the validated canonical revision and its intended companions. Preserve destination-specific name mappings.
2. Synchronize the repository mirror and any existing deployed subset; do not assume every skill is deployed in every host.
3. Update the registry, change log, relevant tracker and learning record with the version, specific change, reason, checks and file paths. Update `STRUCTURE.md` only if structure changed.
4. Review cross-skill imports, routing debt, shared protocols, examples and generated counts affected by the revision.
5. Run the applicable governance checks after the final edits. Fix actionable failures and distinguish passed, failed and skipped checks.
6. Refresh the **local plugin** when requested, checking its actual manifest/cache/content and installed version. A source mirror, bundle, marketplace copy and active installed cache may be different artifacts. Confirm which ones were updated; a copied file does not prove a running session reloaded it.
7. Commit or publish remotely only within the user's authorized scope. Local plugin refresh does not inherently require a GitHub push. Inspect sync/release tools before invoking them; avoid unrelated staging, destructive resets, credential exposure or automatic archive deletion.
8. Capture supported lessons, not a quota of new hypotheses. Rule promotion follows the current governance decision and evidence review; three repeated mentions do not settle O25 automatically.

If a plugin update or required check remains incomplete, identify the exact step and owner in the action plan and report the limitation. Do not mark the whole request complete just because the skill files were written. Conversely, do not rerun passed checks without a new change or unresolved concern.

## Completion record

For each skill, record the starting/revised version, complete-read scope, preserved content, specific clarifications, Novel Insights consideration, scenario or execution checks, changed files, backup and synchronization result. Maintain one authoritative progress ledger for a multi-skill pass and give Ravi frequent concise updates.

Useful completion measures are verified skill coverage, unresolved references, source/mirror/cache consistency, and demonstrated behavior on relevant cases. `_latest` tag coverage alone does not establish quality. The historic 60-day index drift, nine dead names and thirty-five stale concept guides are examples of prior failures, not current library counts or a measured 30–45-minute cost for every refresh.

Editorial revision: September 13, 2026. The evidence-informed selection, four reviews, realistic exercise, companion review and governance close remain; version recovery, description cap, full-scope persistence and local-versus-remote release semantics are explicit.

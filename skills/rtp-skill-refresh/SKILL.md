---
name: rtp-skill-refresh
version: v1.0_latest
description: 'The monthly (and on-touch) refresh discipline for Ravi''s skill library: one executable ritual instead of governance rules scattered across five files. Owns the full loop: evidence-gated selection (no evidence, no edit), Rule-41 archiving before any edit, and the four revision passes (content-as-node, structure, voice, verify-against-exemplar). Then the cold-run stress test for signature skills, because content review is not runnability review. Then CONCEPT.md absorb-and-archive, and the governance close through mirror sync and /plugin update, since git push is not the finish line. Use when: the monthly refresh fires, a skill produced a defective output, Ravi''s review lands on a skill, or the HBR research loop demands updates. Pairs with: rtp-claude-admin (folder governance), skill-creator (new skills; this refreshes existing ones), rtp-hbr-research (the research input). Triggers: ''skill refresh'', ''monthly skill pass'', ''revise this skill'
imports:
  - rtp-claude-admin
---

# Skill Refresh: The Library's Maintenance Ritual

## THE ONE IDEA

**A skill library rots by default — model eras shift, skills get renamed, sources go stale, and every ungoverned edit adds drift. The refresh is the counter-ritual: evidence-gated, archived-before-edited, four-pass reviewed, cold-run tested, and closed all the way through sync.** The reason this is a skill and not a checklist in five governance files: a ritual scattered across five files gets partially executed every time (that's how MASTER_INDEX drifted 60 days and how the orchestrator's rosters carried 9 dead skill names for 3 months). One skill, one read, the whole loop.

## DEPTH DECISION

**Go deep** if: running the monthly refresh, revising a flagship/signature skill, or applying a research cycle's update-map.

**Skim to Step 3 (the four passes)** if: touching a single skill for a specific defect.

**Skip** if: creating a brand-new skill (`skill-creator`), or fixing a typo (no bump, no archive, no ritual).

## THE TRAP

Five ways refreshes go wrong, all observed in this library's own history:

1. **Whiteboard refreshing.** Editing a skill because "this would be nice," not because evidence demands it. Every edit risks drift; an edit without a triggering trace is negative-expected-value. *No evidence, no edit.*
2. **Content review theater.** Reading the skill and pronouncing it good. The ai-prd v1.0 lesson: five structural review passes missed all seven runnability defects; only *running the skill cold* against a real case found them. Reviewing a skill is not the same as executing it.
3. **The unfinished close.** Editing the source and stopping. The source, the deployed copy, the repo mirror, and the installed plugin are four locations; git push isn't the finish line (the plugin caches until `/plugin update`). A refresh that skips the close creates the drift the next session inherits.
4. **Templatization creep.** Making every skill look like the best skill. Rule 42: copy ai-prd's *thinking moves*, never its shape — a quick-reference skill padded to 13 sections is accretion wearing a quality costume.
5. **Parallel-artifact drift.** Maintaining CONCEPT.md, README fragments, or duplicated protocol text "in sync" with SKILL.md. Dual maintenance is drift by design — absorb into the one loaded artifact and archive the rest.

## KEY TERMS (plain language)

- **Evidence gate** — a refresh candidate must cite its trigger: a session anti-pattern, a defective output, a Ravi review, a research update-map, a rename/boundary change, or a failed spot-check. "It's been a while" is not evidence; the *monthly cycle* selects candidates, evidence admits them.
- **Rule 39 (node)** — the skill is reasoned from first principles as a node: what it consumes from named neighbors, what it produces downstream. Sources set direction; they are never pasted.
- **Rule 40 (structure)** — the skill file AND the deliverable it prescribes must be legible at a glance.
- **Rule 41 (versioning)** — SKILL.md carries `version: vX.Y_latest`; superseded versions go to the skill-local `archive/` (max 10), copied *before* editing.
- **Rule 42 (exemplar)** — ai-prd v1.2 is the reference for depth of thinking and connections; emulate the process, derive each skill's own structure.
- **Cold run** — executing the skill against a realistic case with an adversarial reviewer (Test Manager seat) logging every stall, loop, and ambiguity. The only known detector of runnability defects.
- **Routing debt (H16)** — content routed out of skill A to sibling B that B doesn't yet hold. Logged as `⚑ [dest] must absorb [content]` and verified on B's refresh.

## WHAT THIS SKILL CONSUMES & PRODUCES

**Consumes:**
- **The evidence stream** — `5_Knowledge/session-anti-patterns.md`, `rules.md` promotions, defective outputs, Ravi's reviews, the REFINEMENT-TRACKER queue + boundary ledger + routing-debt flags.
- **The research input** — update-maps from `rtp-hbr-research` (monthly) and digest signals from `rtp-research-synthesiser`.
- **The current state** — SKILL-REGISTRY.md, `2_Skills/STRUCTURE.md`, the skill's own `archive/` history.

**Produces:**
- **Refreshed skills** at `vX.Y_latest` with archived predecessors → the mirror + plugin after the close.
- **Updated governance** — registry, CHANGE_LOG entries (with the WHY), tracker status, STRUCTURE.md if locations changed.
- **New evidence** — anti-patterns, hypotheses, rule candidates captured from the refresh itself (the loop that improves the loop) → `5_Knowledge/`.

## THE PROCESS

### Step 1: Select — the evidence gate

Build the refresh slate from the tracker queue + evidence stream. For each candidate write one line: *skill → trigger evidence → expected change*. A candidate without a trigger is cut. Cap the slate at what one session finishes *through the close* — three skills fully closed beat ten skills edited and unsynced (depth over breadth; the unfinished close is the #3 trap).

### Step 2: Archive first (Rule 41)

Before touching the file: `cp SKILL.md archive/SKILL-vX.Y.md`, strip `_latest` from the archived copy's tag, prune the archive past 10. Bump minor for refinements, major for a reframe of the ONE IDEA or node boundary. No snapshot, no edit.

### Step 3: The four revision passes (every touched skill)

| Pass | What it checks | The tests |
|---|---|---|
| **1 · Content as node (Rule 39)** | Sources synthesized against first principles; the skill owns its computation and consumes neighbors' | CONSUMES/PRODUCES names real skills; no re-taught neighbor content; routed-out content logged as routing debt; every number carries an evidence tier |
| **2 · Structure (Rule 40)** | File and deliverable legible at a glance | 30-second scan test; parallel structure in tables; label-led bullets; OUTPUT section prescribes a structured artifact; numbering monotonic |
| **3 · Voice** | Ravi's voice, zero AI-writing patterns | Slop scan (the 24 anti-patterns: no "Additionally/delve/foster/robust/seamless...", no hype, plain verbs); strong openers; every rule carries its Why and its when-wrong |
| **4 · Verify against exemplar** | Mechanical integrity | desc ≤1024 chars (scripted — eye-certified descs drifted over the cap on later touches); frontmatter version tag present; imports exist (phantom-import check — `prompt-as-spec` and `product-pricing` both shipped as phantoms before this check existed); internal § / item references resolve; **internal-rename consistency** — grep the file for its own superseded terms; a rename must propagate to every table, template, and the description in the same pass (the moat-finder "Brand & trust"→"Trust & reliability" catch: renamed in the table, stale in the OUTPUT template and desc); **calibration stamps** — market-dependent claims carry their as-of date ("mid-2026") so future readers know when the weighting was set; required sections present; no stray `---` |

Run the passes as separate reads, not one blended skim — each pass catches what the others' mindset misses.

### Step 4: The cold run (signature skills — mandatory; others — on judgment)

For flagship/always-used skills (ai-prd, orchestrator, eval-framework, strategy-canvas, the agent-design core): **execute the skill against a realistic case** — an interview prompt, a real feature from Ravi's work, a case from the research corpus — under a constraint (time-boxed, no upstream data). An adversarial Test Manager seat logs every point where the skill stalls, loops, contradicts itself, or under-serves. Findings become the next version's edits, each traceable to a finding ID. **Why mandatory:** the ai-prd precedent — structural review scored it world-class; the cold run found 7 defects including 2 HIGH. Content review is not runnability review.

### Step 5: CONCEPT.md absorb-and-archive (on touch)

If the skill folder holds a CONCEPT.md: mine it for content still worth keeping (atomic insights, worked examples, intellectual lineage), fold the keepers into SKILL.md or `references/`, then move CONCEPT.md into `archive/`. Never update it in parallel; never mass-delete unmined. All 35 CONCEPTs froze at 12 APR 2026 while SKILL.md files kept moving — that's the parallel-artifact trap, closed one skill at a time.

### Step 6: The governance close (a refresh isn't done until all boxes tick)

- [ ] SKILL-REGISTRY.md — version, status (and count, if skills were added)
- [ ] CHANGE_LOG.md — what changed AND why, plain language
- [ ] REFINEMENT-TRACKER — status, routing-debt flags opened/closed, boundary-ledger entries
- [ ] STRUCTURE.md — only if locations changed
- [ ] Mirror sync — `./scripts/skill-sync.sh` (confirmation-gated), rtp- prefix preserved in repo frontmatter
- [ ] Git commit + push, then **`/plugin update`** — the installed plugin lags the repo until this runs
- [ ] Learnings captured — anti-patterns from real waste, hypotheses, rule promotions (the refresh feeds its own evidence stream)

## QUALITY GATE (binary checklist)

- [ ] Every refreshed skill cites its trigger evidence (no whiteboard edits)
- [ ] Every touched skill was archived *before* editing, tag stripped on the copy, archive ≤10
- [ ] All four passes ran as separate reads; pass-4 mechanical checks scripted where possible, not eyeballed
- [ ] Signature skills got a cold run with logged findings; each edit traces to a finding
- [ ] No skill was reshaped toward another skill's structure (Rule 42 check: "did I derive this skill's form from its own job?")
- [ ] CONCEPT.md absorbed-and-archived for every touched skill that had one
- [ ] The close completed through `/plugin update` — or the pending steps are logged in ACTION-PLAN with owner
- [ ] The session's own learnings landed in `5_Knowledge/`

## WHEN WRONG

- **Creating a new skill** — that's `skill-creator` + Rule 39 node design; this skill governs existing ones.
- **A production emergency in a skill's output** — fix the output first, log the evidence, refresh on the next cycle; don't run a full ritual mid-incident.
- **Typo-level edits** — no bump, no archive, no ritual (Rule 41's own exception).
- **When the evidence says split or merge, not refresh** — boundary changes go through the tracker's boundary ledger and an explicit Ravi decision, not a solo refresh session.

---

## GROUNDING, TRADE-OFFS & CONCLUSION

- **Recommendation:** run this monthly (paired with the `rtp-hbr-research` cycle) plus on-touch for any skill that produced a defect. Slate small, close fully.
- **Key trade-off:** the ritual costs ~30–45 min per skill beyond the edit itself. The alternative was measured, not hypothetical: 60-day governance drift, 9 dead names in the always-on orchestrator, 35 frozen CONCEPTs.
- **Biggest risk if skipped:** the library becomes a museum of April 2026 — polished, internally referenced, and quietly wrong about its own contents.
- **Next action (first run):** slate = the six top-level rtp-* skills awaiting category migration + any skill flagged in the tracker's routing-debt list. Archive, four passes, close. Measure: % of library carrying `_latest` tags after 3 cycles.

---
name: rtp-research-synthesiser
version: 2.1.0
description: >
  On-demand intelligence synthesis skill. Reads SuperGrok X signals (daily,
  from Notion) and Perplexity Deep Research (weekly Saturday, from Notion),
  processes ONE dimension per invocation, and produces a curated digest with
  actionable extractions, categorised URLs, cross-temporal pattern connections,
  and thought leadership insights. Ravi fires this when ready — typically
  weekly on Sunday, but any time works. Requires ~10 invocations for full
  coverage across all dimensions. Use the strongest reasoning model available.
triggers:
  - run synthesis
  - synthesise
  - weekly digest
  - research digest
  - what did I learn
  - connect the dots
  - synthesis dimension
---

# Grok & Perplexity Research v2.1 — On-Demand Intelligence Engine

## Purpose

This skill transforms raw research inputs into compounding intelligence. It reads from Notion (the single source of truth for both SuperGrok and Perplexity outputs), processes one dimension at a time, and produces curated digests that map to Ravi's AIPM dimensions, skills, interview prep, and thought leadership.

The secret weapon: **cross-temporal pattern recognition.** Every synthesis run connects this week's findings to what came before. Patterns that others see as isolated events, Ravi sees as connected trends — because this skill is designed to find those connections by default.

---

## Architecture: The Complete Pipeline

```
SuperGrok (10 tasks)              Perplexity Max (10 Spaces)
Daily 7:00-9:15 AM IST           Weekly Saturday 5:00-9:00 AM IST
        │                                    │
        ▼                                    ▼
   Grok outputs                    Perplexity outputs
        │                                    │
        ▼                                    ▼
   n8n workflow                    n8n workflow
   (+ FireCrawl for               (+ FireCrawl for cited URLs
    metadata extraction)            + Perplexity model counsel)
        │                                    │
        ▼                                    ▼
┌───────────────────────────────────────────────────────┐
│                   NOTION (Source of Truth)              │
│                                                        │
│  Grok X Signals ──► 10 sub-pages (daily content)      │
│  Perplexity Deep Research ──► 10 sub-pages (weekly)   │
│                                                        │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼ (on-demand, Ravi triggers)
          ┌────────────────────────┐
          │  RESEARCH SYNTHESISER  │
          │  (this skill, v2.0)    │
          │  One dimension per run │
          └────────────┬───────────┘
                       │
          ┌────────────┼────────────┬──────────────┐
          │            │            │              │
     ┌────▼────┐  ┌────▼────┐  ┌───▼─────┐  ┌────▼─────┐
     │  WEEKLY │  │  URL    │  │ SKILL   │  │ THOUGHT  │
     │  DIGEST │  │ LIBRARY │  │ & COURSE│  │LEADERSHIP│
     │         │  │by categ.│  │ UPDATES │  │CONNECTIONS│
     └─────────┘  └─────────┘  └─────────┘  └──────────┘
```

---

## The 10 Synthesis Dimensions

Each invocation processes ONE dimension. A full weekly cycle requires ~10 runs.

| Dim | Name | Grok Source(s) | Perplexity Source | AIPM Modules | Extraction Priority |
|-----|------|---------------|-------------------|--------------|-------------------|
| 1 | **AI Models & Capabilities** | AI PM Builder Signals | AI Model Intelligence Brief | 01, 04 | Course Content |
| 2 | **Context Engineering** | Context Engineering Pulse | Context Engineering Deep | 07 (centrepiece) | Course + Skills |
| 3 | **Claude & Anthropic Intel** | Claude Ecosystem Intel + Cowork Mastery + Anthropic Interview Intel | *(no dedicated Perplexity)* | 09 | Interview Prep + Skills |
| 4 | **Agentic AI** | Agentic AI Signals | *(covered across Spaces)* | 08 | Course + Skills |
| 5 | **AI Evals & Observability** | AI Eval & Observability Watch | AI Model Intelligence Brief (eval sections) | 10 | Course + Skills |
| 6 | **Enterprise AI** | Enterprise AI Adoption Intel | Enterprise AI Casebook | 02, 06 | Course + Interview |
| 7 | **AI Governance & Ethics** | Thought Leadership (safety sections) | AI Governance Watch | 14, 15 | Course + Thought Leadership |
| 8 | **Product Strategy & GTM** | AI Pricing GTM & Monetisation | AI Product Strategy + AI PMF Growth | 11, 12, 13 | Course + Thought Leadership |
| 9 | **AI Teams & Leadership** | *(from Builder Signals + Enterprise)* | AI Team Intelligence + AI Leadership Research | 16, 17 | Course + Thought Leadership |
| 10 | **Frontier & Horizon** | Thought Leadership & Contrarian Takes | AI Frontier Watch | 17 | Thought Leadership |

---

## Notion Page ID Registry

### SuperGrok Pages (Grok X Signals)

| Schedule | Page Title | Notion Page ID |
|---|---|---|
| Parent | Grok X Signals | `d4bca926-d63a-4b53-a182-ed83a0502577` |
| 1 | AI PM Builder Signals | `f7aa08ca-dc88-4754-b6e0-70e578056306` |
| 2 | Context Engineering Pulse | `03a5a265-d233-4148-9f80-09c7c86f0695` |
| 3 | Claude & Anthropic Ecosystem Intel | `1d18d12f-0746-46c7-a6d5-8016394881c8` |
| 4 | Agentic AI Signals | `8fdfb6fc-b119-487c-9712-0a29416017fb` |
| 5 | AI Eval & Observability Watch | `b2b0bf5a-1ba2-452e-9e73-3d3a88697a21` |
| 6 | Enterprise AI Adoption Intel | `f72eddb1-f6da-4bd3-9728-57cfdafb4caf` |
| 7 | Claude Code & Cowork Mastery | `a4767c94-b578-41b5-a66e-9d8fc8638767` |
| 8 | Thought Leadership & Contrarian Takes | `92fff40c-a2f9-4692-b520-a7f845e6e2af` |
| 9 | AI Pricing GTM & Monetisation | `dc6c5792-b766-4ee5-a4f1-7ad6328361f5` |
| 10 | Anthropic Interview Intelligence | `b8598c92-c82b-4735-8ad2-27d360fdcea3` |

### Perplexity Pages (Perplexity Deep Research Signals)

| Schedule | Page Title | Notion Page ID |
|---|---|---|
| Parent | Perplexity Deep Research Signals | `5202c20f-1e08-43f0-9093-da68e201bf4c` |
| 1 | AI Model Intelligence Brief | `af392049-3156-41f5-859b-d6c46279009d` |
| 2 | Context Engineering Research | `42335202-8f9f-49be-a09d-87b2b9e47700` |
| 3 | Enterprise AI Case Study Bank | `5913a98c-0a9f-44dc-9087-d5c531c8444d` |
| 4 | AI Governance & Risk | `438edc4f-da9d-49d3-9f0c-97564ba34211` |
| 5 | AI Product Strategy | `e05f7386-3c52-4428-9fa9-4409e10ed74e` |
| 6 | AI Team Building & Skills | `d734f9d8-762d-47fe-8751-58069eb93d06` |
| 7 | AI Leadership & Transformation | `b73d8995-ef4e-4870-b436-7e573bd6cea7` |
| 8 | RAG & Data Infrastructure | `c573dea8-6356-4056-b2ec-c18bd560feaa` |
| 9 | AI PMF & Growth | `fff0f4d7-8dfd-476b-9bf7-4d5cfc985cf9` |
| 10 | Frontier Research | `ff09a04a-d198-4d3e-8fe6-dbc2e04a3e9b` |

### Other Key Pages

| Page | ID |
|---|---|
| SuperGrok X Intelligence Hub | `313a76c3-f3f8-4fbe-87bc-52fb0c8c31f1` |
| Master X Watchlist — 100 Accounts | `4da3dab5-a3c4-46f5-b2e9-e3609c30df19` |
| Schedule Run Tracker | `556afdcb-0ff4-4e39-bf1f-03540af8ec63` |

---

## Pre-Synthesis Protocol

Before EVERY synthesis run, execute in order:

### Step 0: Deduplication Check (MANDATORY — run before anything else)

1. **Read the run log:** `3_Research/weekly-digests/SYNTHESIS-RUN-LOG.md`
   - Note: last run date per dimension, which Notion pages were read, what was covered

2. **Verify new content exists:** Fetch the relevant Notion page(s) for this dimension.
   - Check the page's last-updated timestamp or the most recent dated entry.
   - **If Notion page content is unchanged since last synthesis run for this dimension → STOP.**
     - Report: "No new content on [page name] since [last run date]. Skipping dimension [X]."
     - Suggest next dimension that DOES have new content.
   - **If Notion page has new content → proceed to Step 1.**

3. **After confirming new content:** Update `SYNTHESIS-RUN-LOG.md` at the END of the run (not before) with: date, dimension processed, pages read, key output location.

---

### Step 1: Context Load

```
1. CLAUDE.md                                → Folder structure, rules
2. 5_Knowledge/rules.md                     → Confirmed patterns (never contradict)
3. 5_Knowledge/hypotheses.md                → Patterns being watched
4. 2_Skills/SKILL-REGISTRY.md               → Current skill versions
5. 3_Research/weekly-digests/               → List recent digest files (last 3-4)
```

If running Dimension 3 (Claude & Anthropic Intel), also read:
```
6. 1_Projects/interview-prep/CONTEXT.md     → Current interview state
```

If running any course-heavy dimension (1, 2, 4-10), also read:
```
7. 1_Projects/ai-fluent-course/CONTEXT.md   → Current course state
```

---

## How a Single Synthesis Run Works

### Step 1: Identify the Dimension

When Ravi triggers synthesis, determine which dimension to process:
- If Ravi specifies: "synthesise context engineering" → Dimension 2
- If Ravi says "run synthesis" without specifying → ask which dimension, or suggest the one with the most unprocessed data
- If Ravi says "full synthesis" → run all 10 in sequence across multiple invocations

### Step 2: Fetch from Notion

For the selected dimension, fetch the relevant Notion pages using page IDs from the registry above. Each page contains run outputs as content — look for dated entries.

**Time window:** Process all data that exists since the last synthesis run for this dimension. If first run ever, process everything available. The rolling window is approximately 1 month — after that, data will be archived to Google Drive.

**What to extract from each page:**
- All dated run outputs (H3 headings or dated sections)
- URLs cited in the outputs (these become the URL library)
- Key findings, frameworks, data points
- Signals tagged as high-engagement or production-evidence

### Step 3: Cross-Reference Grok × Perplexity

For dimensions that have BOTH a Grok and Perplexity source:

```
Finding in BOTH Grok + Perplexity    → HIGH CONFIDENCE (verified signal)
Finding in Grok only                  → PRACTITIONER SIGNAL (real-time, unverified)
Finding in Perplexity only            → RESEARCH EVIDENCE (verified, may lack recency)
Finding contradicted between sources  → INVESTIGATE (valuable nuance)
Finding in 3+ separate run outputs    → PATTERN (candidate for rules.md)
```

### Step 4: Cross-Temporal Pattern Recognition

**This is the critical differentiator.** For every significant finding:

1. **Check against `5_Knowledge/rules.md`** — Does this confirm or challenge an existing rule?
2. **Check against `5_Knowledge/hypotheses.md`** — Does this provide the 2nd or 3rd confirmation needed to promote a hypothesis to a rule?
3. **Check against previous weekly digests** in `3_Research/weekly-digests/` — Is this a continuation, acceleration, or reversal of a trend identified last week?
4. **Check across dimensions** — Does this finding in Dimension X connect to something surfaced in Dimension Y during a previous run? These cross-dimensional connections are the novel insights that build thought leadership.

**Pattern connection format:**
```
🔗 CONNECTION: [This week's finding] connects to [previous finding/rule/hypothesis]
   Source A: [This week — dimension, date, source]
   Source B: [Previous — dimension, date, source]
   Implication: [What this connection means that neither finding means alone]
   Thought leadership angle: [How Ravi can frame this as a unique insight]
```

### Step 5: Produce the Dimension Digest

Output structure for each dimension run:

---

## Dimension Digest Template

```markdown
# [Dimension Name] Digest — [Date]
## Synthesis Period: [Start Date] to [End Date]
## Sources: [Which Grok + Perplexity pages were read]

---

## Executive Signal
[3-5 sentences. The single most important thing from this dimension
this period. Written for a busy Senior PM who has 60 seconds.]

---

## Top Findings

### Finding 1: [Title]
**Confidence:** [HIGH / PRACTITIONER SIGNAL / RESEARCH EVIDENCE]
**Source:** [Grok schedule / Perplexity Space — date]
**AIPM Module:** [which module(s) this maps to]

[2-3 paragraph description. What was found, why it matters,
what changed from before.]

**Ravi's Frameworks Applied:**
[Map to relevant proprietary frameworks — CONTEXT letters, SHARP,
Explore/Expand/Extract, Moat types, Strategy half-lives,
Inner/Outer World, PM Cultures, Thinking Algorithms — whichever
are relevant to THIS finding]

**Cross-Temporal Connection:**
[Does this connect to any previous finding? If yes, describe the
connection and what it means. If first occurrence, mark as NEW SIGNAL.]

**Action:**
- [ ] Course update needed: [specific module and what to change]
- [ ] Skill update needed: [specific skill and what to change]
- [ ] Interview prep: [how to use this in an answer]
- [ ] Thought leadership: [angle for original content]

### Finding 2: [Title]
[Same structure]

### Finding 3-N: [Continue as needed]

---

## URL Library — [Dimension Category]

### Must-Read (Top 3)
1. [Title](URL) — [1-line why it matters]
2. [Title](URL) — [1-line why it matters]
3. [Title](URL) — [1-line why it matters]

### Reference (Worth Bookmarking)
- [Title](URL) — [category tag]
- [Title](URL) — [category tag]

---

## Pattern Recognition

### Confirmed This Period (promote to rules.md)
[Patterns that now have 3+ independent confirmations]

### Strengthened (update hypotheses.md)
[Hypotheses that got additional evidence but not yet 3 confirmations]

### New Hypotheses (add to hypotheses.md)
[First-time observations worth watching]

### Contradictions (flag for Ravi)
[Findings that challenge existing rules or widely-held assumptions]

---

## Cross-Dimensional Connections
[Connections between THIS dimension's findings and findings from
OTHER dimensions in previous synthesis runs. These are the novel
insights that build thought leadership.]

🔗 CONNECTION 1: [description]
🔗 CONNECTION 2: [description]

---

## Thought Leadership Seeds
[1-2 original angles that emerge from this dimension's synthesis.
These are ideas Ravi could develop into posts, course content,
or interview narratives that nobody else is articulating because
they aren't cross-referencing these sources systematically.]

### Seed 1: [Working Title]
**The insight:** [What Ravi uniquely sees]
**Why it's novel:** [What conventional wisdom misses]
**Best medium:** [X thread / blog post / course module / interview answer]

---

## Skill & Course Impact

### Course Module Updates
| Module | What to Update | Priority | Type |
|--------|---------------|----------|------|
| [##] | [specific change] | [HIGH/MED/LOW] | [ADD/UPDATE/CONTRADICT] |

### Skill Update Proposals
| Skill | Proposed Change | Evidence Strength | Recommendation |
|-------|----------------|-------------------|----------------|
| [name] | [change] | [CONFIRMED/OBSERVED] | [APPLY/HOLD/HYPOTHESISE] |

### Knowledge System Updates
| Destination | Entry | Action |
|-------------|-------|--------|
| rules.md | [pattern] | PROMOTE from hypotheses |
| hypotheses.md | [pattern] | ADD NEW / UPDATE evidence count |

---

*Dimension [X] of 10 complete.*
*Processed: [N] Grok run outputs + [M] Perplexity outputs*
*Next suggested dimension: [Y — reason]*
```

---

## Weekly Summary Report

After all 10 dimensions are processed (typically Sunday), produce a summary:

**File:** `3_Research/weekly-digests/YYYY-Wxx-SYNTHESIS.md`

This rolls up all 10 dimension digests into:
1. **Week's Top 5 Signals** (across all dimensions)
2. **Cross-Dimensional Connections** (the novel insights)
3. **Thought Leadership Seeds** (best 3 original angles)
4. **URL Library Summary** (top links by category)
5. **Interview Readiness Update** (if Dimension 3 was run)
6. **Module Currency Heat Map** (17 modules × current/aging/stale)
7. **Skills Updated / Proposed**
8. **Knowledge System Changes** (rules promoted, hypotheses added)
9. **Prompt Refinement Suggestions** (if any schedule underperformed)

---

## Knowledge Routing Map

Every synthesis run produces outputs. This table tells you exactly where each type of output belongs.

| Output Type | Destination | When to Write | Format |
|-------------|------------|---------------|--------|
| Dimension digest | `3_Research/weekly-digests/YYYY-Wxx-DIM-[N]-[name].md` | After every dimension run | Full template |
| Weekly summary | `3_Research/weekly-digests/YYYY-Wxx-SYNTHESIS.md` | After all 10 dims complete | Roll-up format |
| Confirmed pattern (3+ confirmations) | `5_Knowledge/rules.md` | Whenever a pattern qualifies | Same format as existing rules |
| New hypothesis (1st/2nd sighting) | `5_Knowledge/hypotheses.md` | Whenever a new pattern is observed | Same format as existing hypotheses |
| Hypothesis with new evidence | `5_Knowledge/hypotheses.md` | Update existing entry, increment evidence count | Add "Second observed:" line |
| Course module update | `1_Projects/ai-fluent-course/CONTEXT.md` | If finding changes module direction | Note: what changed and why |
| Skill update proposal | `2_Skills/SKILL-REGISTRY.md` + the skill's CHANGELOG | If skill needs version bump | Follow versioning protocol |
| Interview prep signal | `1_Projects/interview-prep/CONTEXT.md` | If Dimension 3 surfaces interview-relevant intel | Note: new angle or data point |
| Thought leadership seed | `3_Research/weekly-digests/YYYY-Wxx-DIM-[N]-[name].md` | Inside the dimension digest | Seed format in template |
| Run log update | `3_Research/weekly-digests/SYNTHESIS-RUN-LOG.md` | At END of each successful run | See run log format below |

### Run Log Format

`3_Research/weekly-digests/SYNTHESIS-RUN-LOG.md` tracks every synthesis run to enable the deduplication check.

```markdown
## Run Log

| Date | Dimension | Notion Pages Read | New Content Found | Output File | Key Findings Summary |
|------|-----------|------------------|-------------------|-------------|---------------------|
| YYYY-MM-DD | [N] [Name] | [page IDs/names] | YES/NO | [filename] | [1-2 sentences] |
```

**This file is the memory of the synthesis system.** Without it, every run starts blind.

---

## Data Lifecycle

```
Week 1-4:  Data lives in Notion. Available for synthesis at any time.
Month-end: Ravi archives processed data to Google Drive.
           Weekly digest files in 3_Research/weekly-digests/ persist locally.
           5_Knowledge/ updates persist permanently.
           Skill and course updates persist permanently.
           Only the raw Notion page content gets archived.
```

---

## Invocation Examples

**"Synthesise context engineering"**
→ Run Dimension 2. Fetch Grok Context Engineering Pulse + Perplexity Context-Engineering-Deep from Notion. Process, cross-reference, output digest.

**"Run full synthesis"**
→ Run all 10 dimensions sequentially. Start with Dimension 3 (Claude/Anthropic — interview-critical), then 2 (Context Eng — centrepiece), then remaining in order.

**"What patterns are emerging?"**
→ Read `5_Knowledge/hypotheses.md` and the last 2-3 weekly digests. Identify hypotheses gaining evidence. Report without running a full dimension synthesis.

**"Connect the dots on [topic]"**
→ Search across all available Notion pages and previous digests for findings related to [topic]. Produce a cross-dimensional connection report.

---

## Rules

1. **Notion is the single source of truth.** All raw inputs come from Notion pages via MCP.

2. **One dimension per invocation.** Don't try to cover everything in one run. Depth over breadth.

3. **Never fabricate.** If a dimension had a quiet week, say so. Thin intelligence honestly reported is more valuable than padded noise.

4. **Cross-temporal connections are mandatory.** Every synthesis run must check current findings against previous rules, hypotheses, and digest files. This is what makes the system compound.

5. **URLs are currency.** Every dimension digest must include a categorised URL library. These are the primary source links that feed Ravi's learning.

6. **Apply Ravi's proprietary frameworks.** CONTEXT letters, SHARP, Explore/Expand/Extract, Moat types with half-lives, Strategy half-life decay, Inner/Outer World, 3 PM Cultures, 10 Thinking Algorithms. Use whichever are relevant — don't force-fit all of them.

7. **Thought leadership seeds are non-optional.** Every dimension digest must surface at least 1 original angle. The whole point of this system is that Ravi sees connections others miss.

8. **Respect the evidence hierarchy.** HIGH CONFIDENCE (both sources confirm) > PRACTITIONER SIGNAL (Grok only) > RESEARCH EVIDENCE (Perplexity only) > SPECULATIVE (single mention).

9. **Skill updates follow versioning.** Copy-old → update → increment → log. Non-negotiable.

10. **Contradictions are treasures.** When sources disagree, that's where the nuance lives. Flag prominently, never silently resolve.

11. **Never run without the dedup check.** Always read SYNTHESIS-RUN-LOG.md first. Always verify Notion has new content before processing. A synthesis run on unchanged content is wasted context and wasted time.

12. **Always write outputs to their designated destinations.** Use the Knowledge Routing Map. Don't leave insights only in the digest — route patterns to 5_Knowledge/, course signals to CONTEXT.md, skill updates to the registry. The digest is the source; the routing is what makes knowledge compound.

---

## File Locations

| What | Where |
|------|-------|
| This skill | `2_Skills/research-synthesiser/SKILL.md` |
| Previous versions | `2_Skills/research-synthesiser/versions/` |
| Dimension digests | `3_Research/weekly-digests/YYYY-Wxx-DIM-[N]-[name].md` |
| Weekly summary | `3_Research/weekly-digests/YYYY-Wxx-SYNTHESIS.md` |
| **Run log (dedup memory)** | `3_Research/weekly-digests/SYNTHESIS-RUN-LOG.md` |
| SuperGrok prompts | `3_Research/x-research/prompts/` |
| Perplexity prompts | `3_Research/perplexity-research/prompts/` |
| Confirmed patterns | `5_Knowledge/rules.md` |
| Watched patterns | `5_Knowledge/hypotheses.md` |
| Course signals | `1_Projects/ai-fluent-course/CONTEXT.md` |
| Interview signals | `1_Projects/interview-prep/CONTEXT.md` |

---

*Version 2.1.0 — 5 APR 2026*
*Author: Ravi Teja Palanki*
*Skill Type: On-demand orchestration (reads Notion via MCP, writes curated digests)*
*Scheduled: Sunday 9 PM IST (automated trigger — manual override always available)*
*Previous versions: v1.0, v1.1, v2.0 archived in `versions/`*

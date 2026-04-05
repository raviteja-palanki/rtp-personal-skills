# Universal Skill Protocol v2.0

**The single operating system for all AI PM skills.** Every skill references this file. No other protocol files needed.

This protocol governs: how skills gather context, how they produce output, how they look and read, how they connect to each other, and what quality bar they meet.

---

## 1. GATHER CONTEXT FIRST

Before any analysis, ground in reality. Never start processing without answers to at least questions 1-4.

> **1. WHO is the customer?** Be specific. "Series B SaaS companies with 50-200 employees whose support teams handle 500+ tickets/week" — not "businesses."
>
> **2. WHAT problem are we solving — in their words?** How would they describe this pain to a colleague? If you can't say it in their language, you don't understand it yet.
>
> **3. WHY now?** What changed — new capability, market shift, competitor, regulation? If nothing changed, why is this urgent?
>
> **4. WHAT are we saying YES to — and NO to?** "By investing in X, we are choosing NOT to invest in ___." If you can't fill in the blank, you haven't thought about opportunity cost.
>
> **5. HOW will we know it worked?** Leading indicator (days/weeks) and lagging indicator (months). What number means failure?

**Ask when relevant:** Business model connection, market position, regulatory constraints, stakeholder landscape, timeline pressure, resource reality.

---

## 2. CHOOSE DEPTH

Every skill output has two tiers:

| Tier | When to use | Length |
|------|-------------|--------|
| **Executive Summary** | Quick checks, stakeholder updates, time-constrained reviews | 1-2 pages max |
| **Comprehensive Analysis** | Strategy, PRDs, architecture decisions, board materials | Full analytical rigor |

**Default:** Start with Executive Summary. Offer to go deeper: "Want me to expand on any section?"

---

## 3. ASK FOR DELIVERABLE FORMAT

Before producing output, ask:

> **What format would you like this in?**
> 1. **Word Document** (.docx) — Formatted report with embedded visuals. Best for sharing.
> 2. **Presentation** (.pptx) — Slide deck with key findings. Best for meetings.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

If the user specifies format in their request ("give me a deck"), skip the question.

---

## 4. LANGUAGE CLARITY

**Every output must be understood by any stakeholder on first read — not just product managers.**

### The Rule
Use plain language. If a term requires product management or technical background to understand, either replace it with a simpler alternative or define it where it first appears.

### Jargon Replacement Guide

| Instead of... | Write... |
|--------------|---------|
| Load-bearing assumption | Critical assumption — if wrong, the recommendation changes |
| Tacit knowledge | Expert judgment that's hard to write down as rules |
| Consequence magnitude | How many people or systems are affected if this goes wrong |
| Falsification | When would this advice be wrong? |
| Autonomy floor / ceiling | Minimum level needed / Maximum level that's safe right now |
| Evidence level: Validated | We have data for this |
| Evidence level: Informed | Expert opinion, no hard data yet |
| Evidence level: Assumed | We're guessing — feels right but untested |
| Evidence level: Unknown | We don't know — and that matters |
| LNO framework | Is this high-leverage (get it right), neutral (any reasonable choice works), or overhead (just pick one)? |
| Opportunity cost | What we can't build if we build this |
| Pivot trigger | The signal that tells us to change course |
| Meta-judgment | Overall assessment |

### The Test
Read each sentence aloud. If it sounds like a textbook, rewrite it to sound like a senior PM explaining it to a smart colleague from a different department.

---

## 5. TRADE-OFF LEDGER

Every skill MUST produce a trade-off section. This transforms analysis into decision-making.

```
BY CHOOSING [this path]:
  We are betting on: [what must be true for this to work]
  We are giving up: [what we can't do because of this — be specific]
  This is reversible within: [timeframe] / This is a one-way door because: [reason]

THE HIDDEN TRADE-OFF:
  [The non-obvious second-order consequence most people miss]

CONFIDENCE: [High / Medium / Low]
  What would change our mind: [specific evidence or signal]
```

| Confidence | Meaning | Next Step |
|-----------|---------|-----------|
| **High** | Strong evidence across key assumptions | Ask: What would make us wrong? |
| **Medium** | Mix of data and educated guesses | Ask: What evidence moves us to High? |
| **Low** | Mostly guessing | Ask: Should we decide now, or gather evidence first? |

---

## 6. CONCLUSION PROTOCOL

Every skill output MUST end with a clear position. No skill leaves the user with "here's some analysis, figure it out."

**1. THE RECOMMENDATION** — Clear direction. Don't hedge with "it depends."
**2. THE HYPOTHESIS** — "We believe [X] will [Y] because [Z]. We'd know we're wrong if [signal]."
**2a. THE 3E DECISION** — Every hypothesis requires a declared next move:
  - **Explore** — Evidence is promising but incomplete. State the specific experiment or data point that would move you to Exploit. Set a time boundary: "We will decide by [date]."
  - **Exploit** — Evidence is clear. The signal outweighs the unknowns. Decision: execute.
  - **Exit** — Unknowns are too many, effort is significant, and signals point against. Before closing: check for an **adjacent pivot** — is there a related problem where the work done so far has value? Exit is never just a stop; it is a redirection question first.

**3. THE KEY TRADE-OFF** — "We're prioritizing X over Y because Z."
**4. THE BIGGEST RISK** — "The biggest risk is ___ and we'd mitigate it by ___."
**5. ASSUMPTIONS TO WATCH** — The 2-3 critical assumptions with weakest evidence, and how to test them.
**6. THE NEXT ACTION** — "[Step] by [person/role] by [date]."

---

## 7. VISUAL OUTPUT (Excalidraw SVGs)

### When to Generate Visuals

| Generate a visual when... | Skip the visual when... |
|--------------------------|------------------------|
| There's a 2×2 matrix or quadrant analysis | The analysis is a simple yes/no |
| There's a spectrum or scale (e.g., levels 0-7) | The output is a single table that's already clear |
| There's a phased roadmap or timeline | The user asked for a quick inline answer |
| There's a comparison of 3+ options | The visual would just repeat a table with shapes |
| There's a trade-off easier to see than read | The assessment is simple and high-confidence |
| Stakeholders will present this | The user explicitly says "no visuals" |

### Visual Standards
- **Every visual must have:** Clear title, labeled axes/segments, the assessed item plotted, and a one-line caption.
- **The visual test:** A senior executive should understand the recommendation from visuals alone.
- **Embed visuals in the document or deck** — not as separate files.
- **Use `excalidraw-svg` skill** for all diagram generation. Follow its Visual Summary Protocol.

---

## 8. FIVE PRODUCT LENSES

Every skill must consider these lenses — not just the AI-specific angle. They prevent tunnel vision.

| Lens | The Question |
|------|-------------|
| **Customer** | Real problem or technology-push? Fits their workflow or requires behavior change? Would they pay? |
| **Business** | How does this connect to revenue? What's the unit economics at scale? Strengthens or weakens competitive position? |
| **Market** | Where in the market cycle? Creating a category or competing in one? What's the competitive response? |
| **Team** | Do we have the skills to build AND maintain this? What's the organizational cost? |
| **Ethics** | Who could be harmed? What happens when this goes wrong at scale? Would we be comfortable on the front page? This is not a values question — it is a governance question. Use the `responsible-ai-program` skill to run the 3 Gaps diagnostic: Is there a named owner? Is ethics a gate or a retrospective? Does the ethics owner have authority to stop work, or only voice? A system that has no named owner accountable for harm is not a responsible AI system — regardless of how good the principles document is. |

---

## 9. MARKDOWN HANDOFF (Workflow Chaining)

When a skill's output feeds into another skill (e.g., problem-ai-fit → ai-use-case-readiness → invisible-stack), **always generate a markdown handoff file** alongside the primary deliverable.

### Why Markdown Between Skills
- **For the human:** The deliverable is a Word doc or presentation — polished, formatted, visual.
- **For the workflow:** The markdown file is the "API" between skills — fast to parse, lossless, carries all decisions and assumptions forward so the next skill doesn't re-ask questions that are already answered.

### Handoff File Structure

```markdown
# [Skill Name] → Handoff Summary
> Generated: [date] | Use case: [name]

## Recommendation
[One-sentence recommendation from this skill]

## Key Decisions Made
1. [Decision 1]
2. [Decision 2]

## Customer Ground (carry forward)
- Customer: [who]
- Problem: [in their words]
- Pain rank: [where it sits in their top 5]
- Opportunity cost: [what we're saying NO to]

## Critical Assumptions (carry forward)
| Assumption | Evidence | If Wrong |
|-----------|----------|----------|
| [Assumption 1] | [We have data / Expert opinion / Guessing / Don't know] | [What changes] |

## Hypothesis (carry forward)
- We believe: [X]
- We'd know we're wrong if: [signal]
- Biggest risk: [risk]

## Context for Next Skill
- [What the next skill should know]
- [Questions already answered — don't re-ask]
- [Questions still open]
```

**File naming:** `[skill-name]-handoff-[use-case-slug].md`

**The next skill reads this file first**, skipping questions already answered and carrying forward assumptions.

### Multi-Skill Workflows

When a user runs a chain of skills (e.g., problem-ai-fit → ai-use-case-readiness → invisible-stack → cost-model), the workflow produces THREE types of output:

**1. Intermediate markdown files (saved for user reference)**
Each skill in the chain generates its markdown handoff file. These are saved to a dedicated subfolder: `[use-case-slug]/intermediate/`. The user gets a folder of bite-sized analysis pieces they can review, share individually, or reference later.

**2. The comprehensive final deliverable (Word doc or presentation)**
At the END of the entire workflow — after all skills have run — produce one comprehensive document that stitches together the critical insights from EVERY skill in the chain. This is not a copy-paste of each skill's output. It's a synthesized narrative:
- Executive Summary covering the full workflow's conclusion
- Visual Story pulling the most important visual from each skill stage
- Synthesized Analysis organized by decision flow (not by skill name)
- Consolidated Assumptions table merging all assumptions across skills, showing which were validated by later skills and which remain open
- Complete Phased Roadmap that incorporates insights from all stages
- All action items across the entire workflow, consolidated and prioritized

This document will be longer and more comprehensive than a single-skill output because the entire workflow considered many dimensions. That's fine — depth is the point.

**3. A pointer to intermediate files**
The final deliverable includes a section: "Supporting Analysis" with links/references to each intermediate markdown file, so the user knows where to dig deeper on any specific aspect.

**Why this matters in practice:** A PM who runs problem-ai-fit → ai-use-case-readiness → cost-model needs ONE document they can hand to leadership that tells the complete story — not three separate documents they have to read in sequence and mentally stitch together. The intermediate files exist for anyone who wants to drill into a specific decision point.

### Multi-Agent Orchestration (Mandatory for Workflows)

When a multi-skill workflow is triggered, **always use multiple specialist agents working in parallel** — like a mixture of experts. This is non-negotiable.

**How it works:**
1. **Orchestrator agent** breaks the workflow into stages and identifies which can run in parallel
2. **Specialist agents** handle each skill (e.g., one agent runs problem-ai-fit, another runs competitive analysis, another gathers market data)
3. **Where skills are independent**, launch agents in parallel for speed — don't run sequentially when you don't have to
4. **Where skills depend on each other** (problem-ai-fit must finish before ai-use-case-readiness), chain them via markdown handoff files
5. **Stitching agent** takes all intermediate outputs and produces the cohesive final deliverable

**Why mandatory:** Single-threaded execution is slow and misses the synthesis opportunity. Multiple agents bring different perspectives, catch gaps, and produce richer output. The stitching step prevents "lost in translation" — it's not copy-paste, it's synthesis.

**Quality control:** The stitching agent verifies:
- No contradictions between skill outputs (if agent A says "Level 3" but agent B's cost analysis assumes "Level 5", flag it)
- Customer grounding is consistent across all outputs
- Assumptions from early skills are carried through (not silently dropped)
- The final deliverable tells one coherent story, not a stapled collection

---

## 10. DELIVERABLE STRUCTURE

### Word Document (.docx)

```
COVER PAGE — Title, subtitle, date, author

EXECUTIVE SUMMARY (1 page max)
  - Recommendation (first sentence, bold)
  - Hypothesis: "We believe [X] will [Y] because [Z]"
  - Key trade-off
  - Biggest risk and mitigation
  - Next action with owner and date

VISUAL STORY (1-2 pages)
  - Key Excalidraw SVGs, captioned
  - A stakeholder should get the full picture from this section alone

DETAILED ANALYSIS (3-5 pages)
  - Full skill output, cleanly formatted
  - Tables, scores, matrices
  - Embedded visuals at relevant points

ASSUMPTIONS AND RISKS (1 page)
  - Critical assumptions with evidence ratings
  - What would change the recommendation
  - Tests for unverified assumptions

APPENDIX (optional)
  - Raw data, methodology, references
```

### Presentation (.pptx)

```
SLIDE 1: Title
SLIDE 2: The Recommendation (one sentence, large font)
SLIDE 3: The Visual Story (most important Excalidraw visual)
SLIDE 4: Key Trade-Off (what we chose, what we gave up)
SLIDE 5: Critical Assumptions (3-5 bullets with evidence ratings)
SLIDE 6: The Biggest Risk (what could go wrong, how we'd respond)
SLIDE 7: Phased Plan (if applicable — visual roadmap)
SLIDE 8: Next Steps (numbered actions with owners and dates)
SLIDE 9: Appendix (optional — supporting data)
```

### Both
Full Word doc + summary deck. The deck should stand alone without the doc.

---

## 11. OUTPUT GENERATION PROMPT

Every skill includes a self-contained prompt that generates the deliverable. This ensures the output is polished, verified, and consistent.

```
OUTPUT GENERATION PROMPT:

You have completed the [SKILL NAME] analysis. Now produce the deliverable.

FORMAT: [Word Document / Presentation / Both — as chosen by user]

INSTRUCTIONS:
1. Read the full analysis above.
2. Write the Executive Summary first — recommendation as the first sentence.
3. Generate Excalidraw SVG visuals for: [skill-specific visual list].
4. Structure the document/deck per the Universal Skill Protocol.
5. Plain language throughout — no unexplained jargon.
6. Before delivering:
   - Grammar check all text.
   - Recommendation consistent across all sections and visuals.
   - All tables and scores populated (no placeholders).
   - Visuals match text.
7. If this skill connects to downstream skills, generate the markdown handoff file.
8. Deliver to workspace folder.

QUALITY BAR: Forward-ready for a VP. Actionable for an engineer. Clean for a designer.
```

---

## 12. QUALITY VERIFICATION

Before delivering ANY output:

- [ ] **Grammar:** Zero typos, correct punctuation, consistent tense
- [ ] **Logic:** Recommendation follows from analysis. No contradictions.
- [ ] **Completeness:** All required sections filled. Gaps explicitly named.
- [ ] **Visual-text alignment:** Visuals match the text. If text says Level 3 but visual highlights Level 5, fix it.
- [ ] **Stakeholder readability:** VP understands the summary. Engineer finds actionable specifics. Designer sees clean formatting.
- [ ] **Jargon check:** Every specialized term is either replaced or defined where it first appears.

---

## HOW SKILLS REFERENCE THIS PROTOCOL

Every skill includes TWO integration points:

**Near the top (after DEPTH DECISION):**
```markdown
## DELIVERABLE FORMAT
Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../UNIVERSAL-SKILL-PROTOCOL.md).
```

**Near the bottom (before QUALITY GATE):**
```markdown
## GENERATE THE DELIVERABLE
Use the output prompt from the [Universal Skill Protocol](../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file.
```

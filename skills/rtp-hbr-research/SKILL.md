---
name: rtp-hbr-research
version: 1.0.0
description: >
  Monthly research synthesis engine for Harvard Business Review, MIT Sloan, and other
  tier-1 management research. Auto-classifies PDFs into thematic batches, launches parallel
  extraction agents (each reading through the lens of a top 0.1% AI Product Manager),
  orchestrates cross-batch pattern synthesis, maps findings to the existing AI PM skill system,
  identifies new skills to create, and produces Excalidraw visualizations for retention.
  Use this skill whenever Ravi drops new research PDFs into the hbr-ai-2026 folder, mentions
  "HBR research", "research synthesis", "process the articles", "extract from PDFs",
  "what did the research say", or wants to run the monthly research cycle. Also use when
  Ravi asks about frameworks, data points, or insights from prior research cycles — this skill
  knows where the dossiers live and can retrieve specific findings.
triggers:
  - hbr research
  - research synthesis
  - process the articles
  - monthly research
  - extract from PDFs
  - what did the research say
  - run the research cycle
  - new articles to process
---

# HBR Research Synthesis Engine v1.0

## Purpose

Transform tier-1 management research (HBR, MIT Sloan, McKinsey Quarterly, etc.) into operational intelligence that compounds across Ravi's three work streams: AI PM Skills, Thought Leadership, and Interview Prep. This is not a summarizer — it's an extraction engine that reads through the lens of a world-class AI Product Manager and produces actionable frameworks, data points, and skill enhancements.

The engine runs monthly. Each cycle adds to a growing library of dossiers that cross-reference prior findings, strengthening pattern recognition over time.

---

## When to Use This Skill

**Primary trigger:** Ravi drops new PDF articles into `3_Research/hbr-ai-2026/` and wants them processed.

**Secondary triggers:**
- "What did the research say about [topic]?" → Search existing dossiers
- "Which articles support [framework]?" → Cross-reference the Framework Inventory
- "What new skills came out of the last cycle?" → Read NEW-SKILL-CANDIDATES.md
- "Run the monthly research cycle" → Full pipeline execution

---

## Architecture: 3-Stage Agent Pipeline

```
┌─────────────────────────────────────────────────┐
│  STAGE 0: CLASSIFY                              │
│  Read titles + first pages of new PDFs          │
│  Auto-bucket into themes (8 established +       │
│  detect new themes if needed)                   │
│  Enforce batch size: 8-12 articles per agent    │
│  Split larger themes into sub-batches           │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  STAGE 1: EXTRACT (Parallel Agents)             │
│  Each agent receives:                           │
│  - The AI PM architecture context               │
│  - The Universal Skill Protocol quality bar      │
│  - Ravi's 10 Thinking Algorithms                │
│  - The batch of PDFs to read                    │
│  Each agent produces a Research Dossier         │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  STAGE 2: SYNTHESIZE (Orchestrator Agent)       │
│  Reads ALL batch dossiers                       │
│  Pattern recognition across articles            │
│  Maps to existing skills + identifies new ones  │
│  Proposes architecture updates                  │
│  Produces 8 synthesis documents                 │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  STAGE 3: BUILD (Execution)                     │
│  Draft skill enhancements                       │
│  Draft new SKILL.md files                       │
│  Create Excalidraw visualizations               │
│  Write Executive Summary                        │
└─────────────────────────────────────────────────┘
```

---

## Stage 0: Smart Theme Classification

Before launching agents, classify every new PDF into a theme. This is the intelligence layer that makes the pipeline efficient.

### Established Theme Taxonomy (from April 2026 baseline)

| Theme ID | Theme Name | Description | Typical Keywords in Title |
|----------|-----------|-------------|--------------------------|
| T1 | AI Strategy & Portfolio | Investment, ROI, portfolio allocation, startup landscape | "strategy", "invest", "portfolio", "returns", "startup" |
| T2 | Agentic AI & Agent Design | Agent architecture, deployment, management | "agent", "agentic", "autonomous", "bot" |
| T3 | AI Quality, Eval & Trust | Output quality, evaluation, customer trust, explainability | "quality", "trust", "eval", "bias", "validate", "explainability" |
| T4 | AI Workforce & Adoption | How AI changes work, skill development, adoption curves | "workforce", "adoption", "employees", "skills", "learn", "coding" |
| T5 | AI Product Design & UX | What AI products should feel/sound like, when NOT to use AI | "product", "UX", "design", "customer", "sound", "voice" |
| T6 | Responsible AI & Governance | Ethics, accountability, security, regulation | "responsible", "governance", "security", "accountability", "disclosure" |
| T7 | Transformation & Change | Organizational change, case studies, scaling | "transformation", "change", "scale", "innovation", "digital" |
| T8 | Strategic Leadership | Decision-making, strategic thinking, executive presence | "leader", "decision", "strategy", "uncertainty", "alignment" |

### Classification Algorithm

1. Read the filename of each new PDF
2. For ambiguous titles, read pages 1-2 of the PDF to determine the core topic
3. Assign to the best-fit theme. If a PDF spans two themes, assign to the primary one.
4. If an article doesn't fit ANY theme well, create a new theme (T9+) — but only if 3+ articles cluster around the same novel topic. Otherwise, assign to the closest existing theme.
5. After classification, check batch sizes:
   - **Target:** 8-12 articles per agent batch
   - **If a theme has >12 articles:** Split into sub-batches (e.g., T4a, T4b) of 8-10 each
   - **If a theme has <4 articles:** Consider merging with an adjacent theme for that cycle
   - **Minimum viable batch:** 3 articles (below this, defer to next cycle or merge)

### Classification Output

Produce a classification manifest before launching agents:
```
## Classification Manifest — [Month Year]
New articles: [count]
Theme distribution:
- T1 (AI Strategy): 5 articles → 1 batch
- T4 (Workforce): 14 articles → 2 sub-batches (T4a: 7, T4b: 7)
- T8 (Leadership): 3 articles → merged with T7 this cycle
- T9 (NEW: AI in Healthcare): 4 articles → new theme created
```

Wait for Ravi's confirmation before launching agents.

---

## Stage 1: Extract — Agent Prompt Template

Each extraction agent receives this briefing. Customize only the batch assignment and theme context.

### Agent Briefing

```
You are a research analyst operating at the level of a top 0.1% world-class
AI Product Manager. You read HBR and MIT Sloan not for awareness but to
extract operational frameworks that change how products get built and shipped.

EXISTING AI PM SKILL ARCHITECTURE:
[Insert current architecture summary — layers, plugins, skill names]

COMPOSABILITY PRINCIPLE:
Skills must be lean and chainable. Each produces a tangible standalone output
but chains with others for depth. If enhancing an existing skill would bloat
it, propose a companion skill instead.

THREE-LENS EXTRACTION:
For every article, take structured notes through THREE lenses:
1. AI PM Skills — Where does this embed? Which skill strengthened? New skill signal?
2. Thought Leadership — Contrarian angles, "here's what most get wrong" insights
3. Interview Prep — CPO-level talking points, frameworks to cite, case studies

ARTICLES TO READ:
[Insert batch file list]
```

### Extraction Template (per article)

Every article in the dossier must include all of these sections:

- **Article metadata:** Title, authors, publication, date
- **Core thesis:** 2-3 sentences — what is this article actually saying?
- **Key frameworks:** Named frameworks with exact attribution (Author, Year, Publication)
- **Critical data points:** Statistics, survey findings, benchmarks with source
- **Important quotes:** Verbatim quotes that capture the insight (max 15 words for copyright)
- **Lens 1 — AI PM Skills:** Which existing skill this strengthens (name the skill, the section, what it adds). Any new skill signals.
- **Lens 2 — Thought Leadership:** Essay-worthy contrarian angles, data points for articles
- **Lens 3 — Interview Prep:** CPO-level talking points, frameworks to cite, case study narratives
- **Cross-article connections:** How this relates to other articles in the batch
- **WHEN WRONG:** Under what conditions would this article's advice fail?

### Dossier Output

Each agent writes to: `3_Research/hbr-ai-2026/synthesis/batch-dossiers/batch-[N]-[theme-name].md`

Dossiers are **persistent reference material**. They accumulate across monthly cycles. The orchestrator cross-references current dossiers against prior ones to detect strengthening or fading patterns.

---

## Stage 2: Synthesize — Orchestrator Protocol

The orchestrator reads ALL batch dossiers from the current cycle (and optionally prior cycles) and produces 8 documents:

| Document | Purpose | Output Path |
|----------|---------|-------------|
| PATTERN-MAP.md | Cross-batch patterns (3+ article confirmation = Strong) | synthesis/ |
| FRAMEWORK-INVENTORY.md | All named frameworks with attribution, organized by domain | synthesis/ |
| SKILL-ENHANCEMENT-MAP.md | Specific additions per existing skill, with source and priority | synthesis/ |
| NEW-SKILL-CANDIDATES.md | Proposed new skills with layer, plugin, scope, import chain, 3E decision | synthesis/ |
| ARCHITECTURE-UPDATE.md | How the plugin structure evolves (new plugins, updated counts, new chains) | synthesis/ |
| KNOWLEDGE-UPDATES.md | Proposed additions to rules.md and hypotheses.md | synthesis/ |
| COURSE-SIGNALS.md | Insights feeding into ai-fluent-course module development | synthesis/ |
| EXECUTIVE-SUMMARY.md | 5-minute CPO read: mega-patterns, what changed, what's actionable | synthesis/ |

### Orchestrator Quality Gates

- Every framework traced to Author + Article + Publication
- Every pattern backed by 3+ articles (Strong) or flagged as Emerging (2 articles)
- Plain language — any VP can understand on first read
- WHEN WRONG sections on all new skill candidates
- 3E Decision (Explore/Exploit/Exit) on every new skill candidate
- Responsible AI checkpoint on skills touching deployment, agents, or user-facing AI

---

## Stage 3: Build — Post-Synthesis Execution

After the orchestrator completes and Ravi reviews, proceed to:

### 3A: Skill Enhancements
For each existing skill marked High priority in SKILL-ENHANCEMENT-MAP.md:
- Read the current SKILL.md
- Draft the specific additions (new diagnostic questions, answer nudges, data points)
- Follow versioning protocol (copy current to versions/, update registry)

### 3B: New Skill Creation
For each Tier 1 new skill candidate:
- Draft SKILL.md following Universal Skill Protocol v2.0
- Include: Depth Decision, The Trap, Diagnostic Questions with Answer Nudges, Reality Check, Output Format, Quality Gate, WHEN WRONG
- Place in the correct plugin directory per ARCHITECTURE-UPDATE.md

### 3C: Excalidraw Visualizations
Create SVGs for:
- Updated architecture overview (showing new skills and plugins)
- Research-to-skills provenance map (which articles fed which skills)
- Per-skill visual reference (for new skills created this cycle)
- Any high-signal pattern that benefits from visual retention

### 3D: Executive Summary
A single document a busy CPO reads in 5 minutes:
- 3-5 mega-patterns from this cycle
- What changed in the skill system
- What's most actionable right now
- What to watch (emerging patterns)
- The single most important insight

---

## Folder Structure

```
3_Research/hbr-ai-2026/
├── [PDF files — the raw articles]
├── HBR-RESEARCH-EXECUTION-PLAN.md    ← This cycle's plan
└── synthesis/
    ├── EXECUTIVE-SUMMARY.md
    ├── PATTERN-MAP.md
    ├── FRAMEWORK-INVENTORY.md
    ├── SKILL-ENHANCEMENT-MAP.md
    ├── NEW-SKILL-CANDIDATES.md
    ├── ARCHITECTURE-UPDATE.md
    ├── KNOWLEDGE-UPDATES.md
    ├── COURSE-SIGNALS.md
    ├── batch-dossiers/
    │   ├── batch-1-ai-strategy.md     ← Persistent — accumulates across cycles
    │   ├── batch-2-agentic-ai.md
    │   └── ...
    └── visualizations/
        ├── research-to-skills-map.svg
        └── updated-architecture.svg
```

For future monthly cycles, date the synthesis output:
```
synthesis/
├── 2026-04/    ← April 2026 cycle (current)
├── 2026-05/    ← May 2026 cycle (future)
└── ...
```

---

## Cross-Cycle Intelligence

Each monthly cycle should reference prior dossiers to detect:
- **Strengthening patterns:** A theme from last month now has 5 more articles confirming it
- **Fading patterns:** Something that seemed important last month has no new evidence
- **Emerging contradictions:** New research challenges a prior finding
- **Compounding frameworks:** Two frameworks from different months combine into something more powerful

The orchestrator should note these cross-cycle connections in PATTERN-MAP.md with a "Cross-Cycle" tag.

---

## Quality Bar (Non-Negotiable)

1. **Attribution:** Every framework → Author + Article + Publication + Year
2. **Plain language:** Any VP or engineer understands on first read
3. **WHEN WRONG:** Every framework has failure conditions
4. **Actionability:** No framework enters as decoration — it must change a decision
5. **3E Decision:** Every new skill → Explore / Exploit / Exit
6. **Responsible AI:** Skills touching deployment include RAI checkpoints
7. **Composability:** New skills are lean and chainable, not bloated

---

## Updating This Skill

After each monthly cycle, review and refine:
- Theme taxonomy (add new themes if 3+ articles cluster around a novel topic)
- Batch size targets (adjust if agents consistently hit quality issues)
- Extraction template (add new sections if Ravi identifies gaps)
- Synthesis documents (add new outputs if needed)

Version this skill following standard protocol: copy to versions/, increment version, update SKILL-REGISTRY.md.

<p align="center">
  <img src="diagrams/hero-badge.svg" alt="rtp-personal-skills" width="900"/>
</p>

---

Most people use AI like a calculator. Type a question, get an answer, move on. Nothing connects. Nothing compounds. Every conversation starts from zero.

This is the opposite. A second brain that researches before it answers, pushes back when the direction is wrong, remembers what worked last time, and gets meaningfully sharper every session — across any domain, not just product management.

---

## The idea, in one sentence

**A second brain that thinks before it acts, deploys specialized agents to do the work, reviews their output, commands the entire installed plugin ecosystem (not just its own skills), and gets sharper every time it runs.**

It's a senior PM at a Fortune 100 industrial company spending three years externalizing how he thinks. Not a productivity hack. Not a prompt library. Not a content-generation gimmick. An operating system for judgment, packaged as a plugin you install in two commands.

AI product management is where the depth runs deepest — frontier-model strategy, evals, agent design, safety, harness engineering. But the same thinking discipline applies to anything: code review, finance, history, life decisions, "what should I think about X." The orchestrator never disclaims with "I'm specialized in AI PM, this is outside my expertise." It researches, applies the same algorithms, reaches for the right plugin for the domain, and answers at the same quality bar.

Four parts make it work.

---

## Install (any machine)

**Step 1 — Install this plugin:**

```
/plugin marketplace add github:raviteja-palanki/rtp-personal-skills
/plugin install rtp-personal-skills@rtp-personal-skills
```

Restart Claude Code. Every skill becomes addressable as `rtp-personal-skills:rtp-{name}` (e.g., `rtp-personal-skills:rtp-design-ai-feature`). Slash commands like `/design-ai-feature`, `/stakeholder-update`, `/brief-me`, and `/rtp-setup` work directly.

**Step 2 — Bootstrap the companion ecosystem:**

```
/rtp-setup
```

Prints the install sequence for companion plugins (`superpowers`, `compound-engineering`, `pm-skills`, `anthropic-skills`, `github/linear/supabase`) so the orchestrator can command the entire Claude Code plugin ecosystem — not just RTP's own skills. Full tier map in [COMPANION-PLUGINS.md](COMPANION-PLUGINS.md). Machine-readable manifest in [companion-plugins.json](companion-plugins.json).

Without companion plugins the orchestrator still works — it falls back to RTP-only mode covering AI PM strategy, content, design, governance, and any non-PM question that fits in its training-grounded knowledge. With companion plugins, it commands the wider ecosystem (TDD discipline, textbook PM frameworks, real `.pptx` / `.docx` / `.pdf` file generation, dev tools, web research, episodic memory).

---

## Part 1: The Orchestrator — A Brain, Not a Router

<p align="center">
  <img src="diagrams/00-orchestrator.svg" alt="The Orchestrator" width="900"/>
</p>

Most AI systems route. You say "write a PRD," it loads a PRD template. There's no judgment, no context, no memory of who you are or what you're trying to accomplish.

The orchestrator is different. It's the persistent brain at the center of everything — and it runs on every input, silently, before you see any output. There is no activation question. Loading the plugin activates it.

**On every input it does five things — silently, before any output:**

1. **Listens deeply.** Not just what you asked, but what you meant. It reads the hidden signals — your role, your constraints, the phase of work you're in, the structural problem you haven't mentioned yet.
2. **Classifies the ask.** Quick answer, deep thinking, or direct action? A factual question gets answered in two sentences, not a five-step analysis. Respect for your time is a design principle.
3. **Activates the right thinking patterns.** Ten cognitive algorithms — first principles, falsification, dual lens, production reality, graceful degradation, cross-domain import — run on every input. Not all ten every time. The ones that matter for *this* problem.
4. **Deploys worker agents.** Independent tasks run in parallel. Dependent tasks run in sequence. The orchestrator manages the handoffs.
5. **Reviews and synthesizes.** Workers produce drafts. The orchestrator reviews for quality, consistency, and blind spots. The user sees one synthesized output — executive-level on the surface, PhD-level underneath.

**The honesty layer is non-negotiable.** Every recommendation is decisive (*"Do X"* — not *"consider X"*). Every recommendation has conditions (*"This works IF [condition]. If [condition] changes, pivot to [alternative]."*). Every output ends with what to do Monday morning. When a fact may be stale, the orchestrator says so before recommending — and reaches for `WebFetch` or `context7` rather than guess. False confidence is the failure mode, not admitting limits.

**Scope is determined by the question, not by an AI-PM ceiling.** *"Should I refactor this Python script"* gets the same depth as *"should we ship this AI feature."* *"Explain the Roman Empire's collapse to me"* gets deep research first, then the same thinking algorithms, then a grounded answer with cited sources.

---

## Part 2: 80 Skills + 11 Slash Commands + 6 Sprint Templates

<p align="center">
  <img src="diagrams/01-architecture-overview.svg" alt="Architecture Overview" width="900"/>
</p>

**80 skills total:** 62 AI PM skills across 7 specialist layers + 1 orchestrator + 17 general-purpose skills (writing, presentations, branding, visualization, design systems, research, admin, resume, README storytelling).

The 62 AI PM skills are organized by what they do, not by what role uses them:

| Layer | Count | What it produces | Example skills |
|---|---|---|---|
| **Thinking Core** | 9 | Checks, not documents | `first-principles`, `falsification`, `bias-spotter`, `dual-lens`, `stress-test` |
| **Product Sense** | 14 | Problem framing | `problem-ai-fit`, `jtbd-analysis`, `feedback-flywheel`, `attitudinal-segmentation` |
| **AI Strategy** | 11 | Durable bets | `strategy-canvas`, `moat-finder`, `vision-setting`, `token-economics` |
| **Safety & Trust** | 7 | Earned right to ship | `safety-by-design`, `trust-ladder`, `responsible-ai-program`, `breach-ready` |
| **Agent Design** | 5 | Autonomy decisions | `autonomy-spectrum`, `agent-harness`, `tool-architecture` |
| **Eval & Quality** | 6 | Measurable proof | `eval-framework`, `eval-driven-development`, `confidence-tuner` |
| **Craft** | 10 | Ship-ready artifacts | `ai-prd`, `agent-spec`, `cost-model`, `stakeholder-communications` |

Plus 17 general-purpose skills covering everything else Ravi does: `ravi-thinking-skills`, `ravi-personal-branding`, `email-mastery`, `frontend-slides`, `excalidraw-svg`, `learn-site-design`, `product-thinking`, `hbr-research`, `research-synthesiser`, `claude-admin`, `deep-dive-writer`, `ux-design-systems`, `ravis-resume-builder`, `cinematic-presentations`, `ai-fluent-brand`, `design-spec`, `readme-storytelling`.

### 11 Slash Commands

Each chains multiple skills into one decisive output. Run when the work is single-prompt, not a multi-step sprint.

| Command | What it does | When |
|---|---|---|
| `/rtp-setup` | Bootstraps the full RTP plugin ecosystem on a fresh Claude account | First day on a new machine |
| `/brief-me` | Memory + recent activity → 60-second briefing | Every morning |
| `/stakeholder-update` | Audience-tailored AI comms with confidence framing | Before exec/eng/customer comms |
| `/weekly-digest` | Week's CHANGE_LOG + git activity + ACTION-PLAN deltas | Friday afternoons |
| `/design-ai-feature` | **10-gate gauntlet** — `problem-ai-fit` → `first-principles` → `autonomy-spectrum` → `determinism-compass` → `prompt-craft` → `eval-framework` → `cost-model` → `ai-ux-patterns` → `safety-by-design` → `ai-prd` | Before a single line of code |
| `/ai-prd-flow` | `problem-ai-fit` + `use-case-readiness` + `jtbd-analysis` + `ai-prd` + `ship-decision` | When PRD context is established |
| `/discover` | `problem-ai-fit` + `jtbd-analysis` + `opportunity-solution-tree` + `uncertainty-research` | Single-prompt discovery cycle |
| `/triage-feedback` | `feedback-triage` (4-axis score) + `failure-modes` | When inboxes pile up |
| `/strategy-review` | `strategy-canvas` + `moat-finder` + `competitive-map` + `cost-model` + `signal-scanner` | Quarterly check |
| `/plan-launch` | `adoption-launch` + `ship-decision` + `cost-model` + `breach-ready` + `production-observability` | L4+ AI feature launch |
| `/retro` | Original AI-PRD lookup + `ai-product-metrics` + `stress-test` + `feedback-flywheel` | Post-ship reflection |

The crown jewel is `/design-ai-feature` — every gate prevents a specific AI launch failure mode. *problem-ai-fit* prevents building ML for a problem rules would solve at 1/100th the cost. *autonomy-spectrum* prevents giving AI L4 when L2 was sufficient. *cost-model* prevents the 1000x volume blow-up between pilot and GA. *safety-by-design* prevents bolted-on guardrails that break the UX before fixing the failure mode.

### 6 Sprint Templates (Multi-Step Orchestration)

Slash commands chain skills into one decisive output. Sprint templates orchestrate when the work doesn't fit in one prompt — multiple iterations, multiple skill blocks, multiple outputs that compose into a finished deliverable. Time is the user's variable; the template defines the orchestration depth.

| Template | Scope | Triggers when |
|---|---|---|
| `new-ai-feature.md` | Full feature lifecycle, all 80 skills, concept → ship | Greenfield AI feature with no prior framing |
| `ai-discovery-sprint.md` | Compressed discovery — interviews, JTBD, opportunity tree, AI-fit, decision | You need a bet, not a build |
| `quarterly-strategy-review.md` | Portfolio review, capability scan, moat audit, signal scan, roadmap rewrite | Leadership wants the next bet |
| `ai-incident-response.md` | Active incident — triage, containment, comms, postmortem | A hallucination hit production |
| `eval-ops-setup.md` | Eval pipelines, regression suites, production observability dashboards | Shipping AI without measurement infrastructure |
| `agent-launch-checklist.md` | Autonomy review, harness audit, breach drills, trust-ladder check | An agent is about to act for users |

Slash commands and sprint templates are not competing — slash commands are the single-prompt layer; sprint templates are the multi-prompt orchestration layer for work the orchestrator decomposes across iterations. The orchestrator picks based on how the user describes the situation.

---

## Part 3: Full Ecosystem Awareness — What Makes This 0.1%

<p align="center">
  <img src="diagrams/05-workflow-paths.svg" alt="Workflow Paths" width="900"/>
</p>

The orchestrator commands the entire installed Claude Code plugin ecosystem, not just the skills in this repo. RTP skills are first preference when a purpose-built equivalent exists. But the orchestrator never refuses a task because RTP doesn't ship a skill for it. When a non-RTP plugin solves the problem better, it reaches for it.

Five tiers, each with a clear use:

**Tier 1 — RTP skills (Ravi's voice + thinking).** AI PM strategy, content or visual output that must sound like Ravi, governance, design system work, README storytelling. The 80 skills in this repo.

**Tier 2 — Process and engineering rigor.** `superpowers:*` and `compound-engineering:*` for TDD discipline, systematic debugging, code review (giving and receiving), brainstorming, plan execution, frontend design, agent-native architecture, dhh-rails-style. When the work is actual engineering — code, tests, debug — these own the discipline layer.

**Tier 3 — PM execution (`pm-skills` marketplace, 8 plugins).** Lean Canvas, OKRs, RICE, JTBD canonical, Porter's Five Forces, GTM motions, cohort analysis, A/B test stats. Textbook PM frameworks for when an AI-specific RTP version doesn't apply.

**Tier 4 — File formats and Anthropic skills.** `anthropic-skills:pdf`, `anthropic-skills:pptx`, `anthropic-skills:xlsx`, `anthropic-skills:docx`, `anthropic-skills:web-artifacts-builder`, `anthropic-skills:brand-guidelines`. Whenever the task touches that file format. Layered with Tier 1 design DNA when the output is visual.

**Tier 5 — Development tools.** `github`, `linear`, `supabase`, `commit-commands`, `episodic-memory:search-conversations`, `elements-of-style`. The orchestrator picks the right tool for the actual need — never reinvents what's wrapped.

The result: **the orchestrator is never narrow.** It picks the right plugin every time, RTP-first when a purpose-built skill exists, falling back where it doesn't.

---

## Part 4: The Worker Agents

<p align="center">
  <img src="diagrams/06-import-chain.svg" alt="Import Chain" width="900"/>
</p>

The 80 skills aren't a flat list. They're organized into **specialist agent teams** the orchestrator deploys — sometimes solo, often in parallel.

### The 6 AI PM Expert Teams

**Sense-Maker** — Understands the real problem before anyone solves it. Skills: `first-principles`, `problem-ai-fit`, `use-case-ready`, `problem-type`, `needs-guard`, `jtbd-analysis`, `interview-synthesis`, `feedback-triage`, `attitudinal-segmentation`.

**Strategist** — Where to invest, what to kill. Skills: `strategy-canvas`, `moat-finder`, `build-or-buy`, `cost-reality`, `portfolio-manager`, `signal-scanner`, `trendslop-check`, `adoption-launch`, `purpose-dialogue`, `vision-setting`.

**System Architect** — How much autonomy, what architecture, what controls. Skills: `autonomy-spectrum`, `agent-ecosystem`, `tool-architecture`, `agent-harness`, `determinism-compass`, `multi-modal-product-design`.

**Safety Expert** — Make it safe AND get people to use it. Skills: `safety-by-design`, `rai-ops`, `trust-ladder`, `judgment-guard`, `alignment-check`, `breach-ready`, `agent-risk`, `trust-under-fog`.

**Evals Expert** — Prove it works with evidence, not hope. Skills: `eval-framework`, `eval-first`, `ai-metrics`, `prod-watch`, `experiment-rig`, `confidence-tuner`.

**Crafter** — Produce pre-tested documents. Skills: `ai-prd`, `context-spec`, `agent-spec`, `cost-model`, `ship-decision`, `prompt-as-product`, `prompt-craft`, `competitive-map`, `fit-signal`, `stakeholder-communications`.

### The 17 General-Purpose Workers

For everything else Ravi does. `ravi-voice` (the DNA in every output), `email-mastery`, `frontend-slides`, `excalidraw-svg`, `ravi-personal-branding`, `learn-site-design`, `product-thinking`, `research-synthesiser`, `hbr-research`, `claude-admin`, `deep-dive-writer`, `ux-design-systems`, `ravis-resume-builder`, `cinematic-presentations`, `ai-fluent-brand`, `design-spec`, `readme-storytelling`.

---

## Watch It Work — Two Real Requests

Architecture diagrams show structure. This shows what the structure *does.*

### Request 1 — An Enterprise AI Feature

A VP sends a message: *"We need AI-powered insights on the manufacturing dashboard. Q3 deadline."*

Most PM tools open a PRD template. This system does something different.

<p align="center">
  <img src="diagrams/worked-example.svg" alt="The System in Action — Enterprise AI Request" width="900"/>
</p>

The VP asked for *AI insights.* What shipped was a reframed problem (alert fatigue, not insights), a staged capability roadmap (anomaly detection now, predictive at Month 3), an autonomy decision (Level 2 — AI suggests, human approves), a stress-tested cost model ($42K/mo at 50 plants, ROI-positive if it saves $180K/mo), and a kill switch (< 15% false-alert reduction at day 45 → pivot).

Every section was shaped by a different team. The Sense-Maker reframed the problem. The Strategist built the roadmap with an expiration date. The System Architect and Safety Expert locked the autonomy level and designed the degradation path. The Evals Expert defined success before a line of code was written. The Crafter assembled it all — but the document arrived pre-tested because the thinking happened in the right order.

### Request 2 — A Non-PM Question

*"Help me think about what to look for in a 30-year mortgage right now."*

There is no `mortgage-evaluator` skill. There is no AI PM angle. The orchestrator does NOT disclaim.

It runs the same loop: classify (deep thinking, not quick answer), activate first-principles (what's the real decision — rate, term, optionality, or total interest paid?), reach for `WebFetch` to get current rates from primary sources, apply red-team (state when its advice would be wrong — short residency, expected income drop, rate-cut probability), end with what to do this week.

The output cites sources. Names assumptions. Surfaces the conditions that would change the recommendation. Reads like a smart financial-curious human did the work — because that's the brain it's externalizing, not an AI-PM-only specialist disclaiming outside its lane.

That's the difference between a template and a second brain.

---

## The Frameworks Embedded

Not referenced. Folded into specific skills with attribution and AI-PM extensions.

| Practitioner | Framework | Skill |
|---|---|---|
| **April Dunford** | 5-component positioning + battlecard | `competitive-map` |
| **Hamilton Helmer** | 7 Powers (with real-vs-vanity diagnostics) | `moat-finder` |
| **Shreyas Doshi** | LNO, pre-mortem, altitude-horizon, product work levels | `product-thinking`, `stress-test` |
| **Hamel Husain + Shreya Shankar** | Open coding → axial coding → selective coding | `eval-framework`, `interview-synthesis` |
| **Aparna Chennapragada** | NLX as new UX (5 inversions + 4 patterns) | `ai-ux-patterns` |
| **Bob Moesta** | JTBD demand-side + Switch Interview | `jtbd-analysis`, `uncertainty-research` |
| **Teresa Torres** | OST + AI-feasibility filter | `opportunity-solution-tree` |
| **Lenny Rachitsky** | North Star + AARRR for AI (5-stage funnel) | `ai-product-metrics` |
| **Colin Matthews** | Vibe-coding (PRD → prototype in 10 min) | `prompt-craft` |
| **Hilary Gridley** | AI Embracer / Neutral / Skeptic | `attitudinal-segmentation` |
| **Palle Broe** | AI monetization decision tree (59% bundle / 23% add-on / 18% standalone) | `token-economics` |
| **Marty Cagan / Jackie Bavaro** | Vision durability across model generations | `vision-setting` |
| **Google Labs** | DESIGN.md format spec (W3C / Tailwind / DTCG export) | `design-spec` |
| **Morgan Housel** | Narrative-first technical writing | `readme-storytelling` |

---

## DESIGN.md — Agent-Portable Design System

The `ravi-personal-branding` skill exports as a [Google Labs DESIGN.md](https://github.com/google-labs-code/design.md) file — a single Markdown document with YAML token frontmatter that any coding agent (Claude Code, Cursor, v0, Bolt) can consume to produce consistent UI. Tokens are W3C Design Token Format compatible. Export to Tailwind theme config or DTCG `tokens.json` with a CLI command. A coding agent given this DESIGN.md ships UI in 30 seconds. Given a 50-page Figma file, it gets it wrong half the time.

---

## The Compounding Engine

This part took the most iteration — and it's the part that makes everything else work.

**Every skill follows a shared protocol:** gather context → choose depth → build a trade-off ledger → pass a quality gate → generate the deliverable. Skills compose. The output of one becomes the input of the next without translation loss.

**Every diagnostic question includes calibrated answer nudges** — thinking dimensions, spectrum anchors, red flag patterns, sharpening probes — so the system adjusts depth to match how well-defined the problem is. Vague input doesn't get glossed over. It gets flagged.

**Every skill has a WHEN WRONG section** — the conditions under which its own advice fails. A framework that doesn't know its limits is more dangerous than no framework at all.

**Every session feeds back.** Patterns get watched. After three confirmations, they become rules. Rules shape future sessions. Anti-patterns get captured when they cause real waste. The orchestrator reads them and avoids repeating them. Over months, the system gets meaningfully sharper.

This isn't a library of tools. It's a second brain that learns.

---

## About me

I'm **Ravi Teja Palanki** — Senior Technical PM at Honeywell, Perplexity AI Fellow 2025.

12+ years shipping enterprise B2B products at Fortune 100 scale. From 0-to-1 builds through global adoption across industrial, life sciences, and energy verticals. Led cross-functional teams of 30+ and taken products from first alpha to $100M+ revenue opportunity. More recently: shipping Gen AI into production — RAG pipelines, LLM-powered assistants for plant managers and field supervisors, context-engineered architectures designed for safety-critical industrial environments where a hallucination isn't an inconvenience, it's a compliance incident.

I'm what the research calls a *bridger.* When engineering says *we need a validation layer*, design says *users need to feel in control*, and the business asks *what's the ROI at 10x scale* — I make each feel understood and challenged, then synthesize the path that serves all three. That instinct — translating across contexts, integrating across incentives — is the design principle behind every skill in this system.

---

## Repo state at a glance

- **80 skills** = 62 AI PM layer skills + 1 orchestrator + 17 general-purpose. All lint-clean, frontmatter audited, voice-consistent.
- **11 slash commands** + **6 multi-step sprint templates**.
- **1 plugin marketplace** registration (installable from any machine via `/plugin marketplace add`).
- **1 orchestrator** (v1.4.0) — Ravi's full second brain. Always on, every session. AI PM is the deepest expertise; same rigor applies to any domain.
- **DESIGN.md export** for the brand system (agent-portable across Claude Code, Cursor, v0, Bolt).
- **5-tier companion plugin manifest** — orchestrator commands superpowers, compound-engineering, pm-skills, anthropic-skills, dev tools.
- All skills cross-reference each other; no orphans.

License: All Rights Reserved. Use, study, learn from. Don't ship as your own.

---

<sub>Built with Claude · 4 May 2026 · Compound Engineering · Orchestrator v1.4.0</sub>

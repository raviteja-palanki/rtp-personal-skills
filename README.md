<p align="center">
  <img src="diagrams/hero-badge.svg" alt="rtp-personal-skills" width="900"/>
</p>

---

I didn't build 67 skills. I built a brain.

The skills are its expertise. The orchestrator is its judgment. And the whole thing learns — every session, every correction, every hard question — it compounds.

This is what happens when a product manager treats their own AI tooling with the same rigor they'd bring to any production system they're responsible for.

---

## The idea, in one sentence

**An AI operating system that thinks before it acts, deploys specialized agents to do the work, reviews their output, and gets sharper every time it runs.**

Think of it like this. Most people use AI the way you'd use a calculator — type a question, get an answer, move on. Nothing connects. Nothing compounds. Every conversation starts from zero.

What I built is different. It's more like having a chief of staff who knows your projects, understands your thinking style, remembers what worked last time, and — when you say "write me a PRD" — doesn't just fill in a template. It checks your reasoning first. It asks whether you've considered the failure modes. It models the cost at 10x scale. It flags the assumption that would kill the plan. Then it writes the PRD — and the PRD arrives pre-tested, because the thinking happened in the right order.

The system has three parts.

---

## Part 1: The Orchestrator — A Brain, Not a Router

<p align="center">
  <img src="diagrams/00-orchestrator.svg" alt="The Orchestrator" width="900"/>
</p>

Most AI systems route. You say "write a PRD," it loads a PRD template. You say "do a competitive analysis," it loads an analysis framework. There's no judgment. No context. No memory of who you are or what you're actually trying to accomplish.

The orchestrator is different. It's the persistent brain that sits at the center of everything.

**When any input arrives, the orchestrator does five things — silently, before you see any output:**

1. **Listens deeply.** Not just what you asked, but what you meant. It reads the hidden signals — your role, your constraints, the phase of work you're in, the structural problem you haven't mentioned yet.

2. **Classifies the ask.** Is this a quick answer? Deep thinking? Direct action? The classification determines the response — a factual question gets answered in two sentences, not wrapped in a five-step analysis. Respect for your time is a design principle.

3. **Activates the right thinking patterns.** Ten cognitive algorithms — first principles decomposition, falsification (when would this advice be wrong?), bias detection, production reality checks, graceful degradation design — run on every input. Not all ten every time. The orchestrator activates the ones that matter for *this* problem.

4. **Deploys worker agents.** The orchestrator doesn't do the specialized work itself. It identifies which agents to deploy, what skills they need, and in what order. Independent tasks run in parallel. Dependent tasks run in sequence. The orchestrator manages the handoffs.

5. **Reviews and synthesizes.** Workers produce drafts. The orchestrator reviews for quality, consistency, and blind spots. Then it synthesizes everything into a single output — executive-level on the surface, PhD-level underneath.

**The orchestrator's communication rules are non-negotiable:**
- Every recommendation is decisive. "Do X" — not "consider X."
- Every recommendation has conditions. "This works IF [condition]. If [condition] changes, pivot to [alternative]."
- Every output ends with what to do Monday morning. Not what to think about — what to DO.

---

## Part 2: Worker Agents — An Army of Specialists

<p align="center">
  <img src="diagrams/01-architecture-overview.svg" alt="Architecture Overview" width="900"/>
</p>

Worker agents are not scripts. They're intelligent sub-agents that combine specialized skills with contextual understanding.

Every worker has three components: **domain expertise** (one or two specialized skills), **persona context** (they understand the user's voice, thinking style, and quality bar), and **memory** (they carry feedback from prior executions, so the tenth time a worker runs, it's structurally sharper than the first).

Here's the map:

### The AI PM Expert Teams (55 skills)

Six specialized teams that the orchestrator deploys for AI product work:

**The Sense-Maker** sees the real problem — not the one you described, but the one underneath it. It runs first-principles decomposition, scores AI fit, maps where uncertainty lives, and catches adaptive challenges disguised as technical problems.

**The Strategist** decides where to invest and what to kill. It builds capability-conditional roadmaps with expiration dates, finds the moat (data flywheel, workflow lock-in, context depth, or earned trust), catches when AI-generated strategy is just trendy advice, and models cost reality at production scale.

**The Architect** designs the right level of autonomy. Not "how autonomous CAN we make this" but "what level of autonomy does each interaction DESERVE?" It maps the spectrum from autocomplete to fully autonomous agents, designs tool access with consequence-aware permissions, and builds the harness architecture (planner → generator → evaluator) that keeps agents productive and safe.

**The Trust Builder** makes it safe AND gets people to use it. Safety-by-design principles baked into architecture. Adoption curves modeled by persona. Proportionality analysis for every agent (is the value worth the worst-case harm?). Breach readiness — designing systems that survive being hacked, not just systems that resist it.

**The Prover** replaces hope with evidence. Evaluation frameworks that evolve as the product matures. Experiments designed for causal evidence, not correlation. Confidence calibration that prevents both over-reliance and dismissal. The rule: if you can't measure it, you can't ship it.

**The Crafter** produces the documents that ship the product — PRDs, agent specs, cost models, ship/no-ship decisions. But because the Crafter runs *after* the other five teams, every document arrives pre-tested. The PRD has eval criteria as acceptance criteria. The cost model has been stress-tested at 10x. The ship decision has named the three assumptions that would invalidate it.

### The General-Purpose Agents (12 skills)

Beyond AI PM, the system has specialists for the rest of the workday:

- **Email Writer** — professional communication calibrated to context and audience
- **Article Writer** — thought leadership grounded in research synthesis, not opinion
- **Research Analyst** — signal collection and pattern synthesis from curated sources
- **Presentation Builder** — zero-dependency HTML presentations with Apple-level design polish
- **Diagram Builder** — hand-drawn SVG diagrams with pastel palette and storytelling structure
- **Interview Strategist** — AI PM interview preparation grounded in real frameworks and experience
- **Curriculum Architect** — course development using the CONTEXT framework

Every worker inherits from **Ravi Voice** — the master thinking system that carries 10 cognitive algorithms, 24 AI writing anti-patterns to avoid, and the Bridger communication style. A resume without the persona embedded isn't a Ravi resume. An article without the thinking algorithms isn't Ravi's thought leadership. Voice is the DNA in every worker.

---

## Part 3: The Three-Layer Skill Architecture

<p align="center">
  <img src="diagrams/02-thinking-layer.svg" alt="Thinking Layer" width="900"/>
</p>

The 55 AI PM skills are organized into three layers. Each layer earns the right to exist by making the next layer's output trustworthy.

### Layer 1: Thinking — "Before you decide anything" (10 skills)

These don't produce documents. They produce *checks.*

Before any decision gets made, they ask: Are you decomposing from first principles, or pattern-matching from your last project? Are you anchored on what a competitor built instead of what your users need? If your AI system fails, does it degrade gracefully or does it fail silently? What would make your strongest recommendation completely invalid?

Skills: `first-principles` · `bias-spotter` · `falsification` · `dual-lens` · `determinism-compass` · `stress-test` · `failure-design` · `alignment-check` · `judgment-guard` · `problem-type`

<p align="center">
  <img src="diagrams/03-judgment-layer.svg" alt="Judgment Layer" width="900"/>
</p>

### Layer 2: Judgment — "The hard calls" (37 skills across 5 domains)

The decisions that separate a PM who's been in the room from one who's read about the room.

**Product Sense** (9 skills, incl. needs-guard) — Is AI the right solution, or are you building because the technology is exciting? Scores AI fit 0-16. Maps the invisible stack. Designs the feedback flywheel that turns user corrections into model improvements.

**AI Strategy** (10 skills) — Durable bets when capabilities shift every quarter. Capability-conditional roadmaps. Moat analysis. Portfolio management with stage gates. And a trendslop detector that catches when AI-generated strategy is just telling you what's popular.

**Safety & Trust** (7 skills) — Not compliance theater. Safety as the thing that earns you the right to ship fast. Proportionality analysis for agents. Breach readiness. Trust signals calibrated so users neither over-rely nor ignore.

**Agent Design** (5 skills) — When AI should act, not just answer. The autonomy spectrum from Level 0 to Level 4. Multi-agent orchestration. Tool access with consequence-magnitude-aware permissions.

**Eval & Quality** (6 skills) — If you can't measure it, you don't know if it works. Evaluation before code. Experiments designed for causal evidence. Confidence tuning that reduced errors by 49% in research.

<p align="center">
  <img src="diagrams/04-craft-layer.svg" alt="Craft Layer" width="900"/>
</p>

### Layer 3: Craft — "Ship-ready artifacts" (8 skills)

PRDs, agent specs, cost models, ship decisions, competitive maps, product-market fit signals, prompt specifications.

None of them start by asking requirements. They start by importing the thinking and judgment layers. The output arrives pre-tested — not because a review step was bolted on, but because the architecture won't let you skip one.

---

## The Compounding Engine

<p align="center">
  <img src="diagrams/06-import-chain.svg" alt="Import Chain" width="900"/>
</p>

This is the part that took the most iteration — and it's the part that makes everything else work.

**Every skill follows a shared protocol:** gather context → choose depth → build a trade-off ledger → pass a quality gate → generate the deliverable. Skills compose. The output of one becomes the input of the next without translation loss.

**Every diagnostic question includes calibrated answer nudges** — thinking dimensions, spectrum anchors, red flag patterns, sharpening probes — so the system adjusts its depth to match how well-defined the problem is. Vague input doesn't get glossed over. It gets flagged.

**Every skill has a WHEN WRONG section** — the conditions under which its own advice fails. A framework that doesn't know its limits is more dangerous than having no framework at all.

**Every session feeds back.** Patterns get watched. After three confirmations, they become rules. Rules shape future sessions. Anti-patterns get captured when they cause real waste. The orchestrator reads them and avoids repeating them. Over months, the system gets meaningfully sharper.

This isn't a library of tools. It's an operating system that learns.

---

## How I'd explain this in an interview

*"I built a personal AI operating system — 67 composable skills with an orchestrator that works like a brain, not a routing table.*

*The insight was that most AI tools give you templates. You fill in a PRD template, check the boxes, ship. But the template doesn't know you're anchored on a competitor's approach. It doesn't catch that your cost model collapses at 10x scale. It doesn't ask who pays the cost if you're wrong.*

*So I built a system where the thinking happens in the right order. Ten reasoning skills run as checks before any decision gets made. Thirty-six judgment skills make the hard calls — not 'what is RAG' but 'when is RAG the wrong architecture for your constraints.' Eight craft skills produce documents that arrive pre-tested because the reasoning layers already ran.*

*At the center is an orchestrator — a persistent brain that understands my goals, deploys specialized worker agents in parallel, reviews their output, and compounds its judgment over time. It's like having a chief of staff built from first principles.*

*The system has been my actual daily operating system for months. It's not theoretical — it's how I ship, think, and prepare. And the architecture itself demonstrates the AI PM thinking it teaches: composable skills, import chains that enforce quality, graceful degradation when context is limited, and a compounding feedback loop that makes every session smarter than the last."*

---

## About me

I'm **Ravi Teja Palanki** — Senior Technical PM at Honeywell, Perplexity AI Fellow 2025.

12+ years shipping enterprise B2B products at Fortune 100 scale. From 0-to-1 builds through global adoption across industrial, life sciences, and energy verticals. Led cross-functional teams of 30+ and taken products from first alpha to $100M+ revenue opportunity. More recently: shipping Gen AI into production — RAG pipelines, LLM-powered assistants for plant managers and field supervisors, context-engineered architectures designed for safety-critical industrial environments where a hallucination isn't an inconvenience, it's a compliance incident.

I'm what the research calls a *bridger.* When engineering says "we need a validation layer," design says "users need to feel in control," and the business asks "what's the ROI at 10x scale" — I make each feel understood and challenged, then synthesize the path that serves all three. That instinct — translating across contexts, integrating across incentives — is the design principle behind every skill in this system.

---

## Installation

```bash
# As a Claude plugin:
claude plugin install raviteja-palanki/rtp-personal-skills

# Or clone directly:
git clone https://github.com/raviteja-palanki/rtp-personal-skills.git
```

---

<sub>Built with Claude · April 2026 · All rights reserved</sub>

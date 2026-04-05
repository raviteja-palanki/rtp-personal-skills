# Architecture

How 54 skills compose into a thinking system — not just a collection of files.

<p align="center">
  <img src="diagrams/01-architecture-overview.svg" alt="Three-layer architecture — 54 skills, 3 layers, 5 judgment domains" width="900"/>
</p>

> See also: [Workflow Orchestration](workflow-orchestration.svg) for the 6 curated paths through the skill graph.

---

## Why Three Layers?

The insight that drives the entire architecture: **decisions need to be checked before they're made, and documents need to be checked before they're written.**

Most AI product tools give you templates. Fill in the PRD. Check the boxes. Ship.

The problem: the template doesn't know that you're anchored on what a competitor built instead of what your users need. It doesn't know that the feature you're specifying needs to be predictable every time (rules) in some places and can tolerate variability (AI) in others. It doesn't know that your cost model collapses at 10x scale.

The three-layer architecture solves this by making checking automatic across 54 skills:

- **Layer 1 (Thinking)** catches mistakes before any decision gets made
- **Layer 2 (Judgment)** makes the hard AI-specific decisions that templates can't encode
- **Layer 3 (Craft)** produces documents that have already been pressure-tested by Layers 1 and 2

That's the import chain. It's why a PRD from this system isn't a template — it's a document that arrives pre-tested.

---

## Layer 1: Thinking — "Before you decide anything" (10 skills)

These are checks, not outputs. They don't produce documents. They catch errors in reasoning before those errors become products.

Every Layer 2 and Layer 3 skill imports from this layer first. It's the immune system.

| Skill | What it catches | Why it matters |
|-------|----------------|----------------|
| `first-principles` | Assumptions you didn't know you were making | Strips a problem to the one irreducible operation before you start solving the wrong thing |
| `bias-spotter` | The cognitive bias about to derail the decision | Names the specific bias (anchoring, sunk cost, survivorship) — not "be careful" but "you're anchored on the competitor's approach" |
| `falsification` | Overconfidence in untested hypotheses | Forces the question "under what conditions would this be wrong?" before you build |
| `dual-lens` | Communication that only one side of the table can use | Tests whether both business leaders AND technical leaders can act on this. If only one can, the communication failed |
| `determinism-compass` | The most common AI architecture mistake | Classifies which parts must be predictable every time (rules) vs. where AI variability is acceptable. Miss this and you build the wrong thing |
| `stress-test` | Plans that look great until they meet production | Pressure-tests across 6 dimensions: scale, adversarial input, model degradation, bad data, cascade failure, cost blowup |
| `failure-design` | The assumption that AI won't fail | Designs graceful degradation: AI → simpler model → rules → human fallback. The user experience of failure matters as much as the feature |
| `alignment-check` | Organizational readiness gaps that sink AI projects | Maps the 5-link chain (Purpose → Strategy → Capability → Architecture → Systems) and finds which link is broken. 93% of AI failures are organizational, not technical |
| `judgment-guard` | Silent expertise erosion from AI over-reliance | Designs checkpoints that keep humans sharp. Without designed friction, people accept AI outputs without engaging judgment. Over 6-18 months, expertise atrophies silently |
| `problem-type` | Treating adaptive challenges as technical problems | Distinguishes technical problems (clear solution, known path) from adaptive challenges (requires people to change). Most AI failures happen because teams keep "solving" something that needs organizational change, not a better algorithm |

**Key property:** Domain-agnostic. These work for AI products, traditional products, business strategy. The domain specificity comes from Layers 2 and 3.

---

## Layer 2: Judgment — "The hard calls" (36 skills across 5 plugins)

These are the decisions that separate strong AI PMs from everyone else. Not "what is RAG" but "when is RAG the wrong choice for your context." Not "what is an agent" but "how much autonomy should this agent have on day one."

### Product Sense (9 skills)
Whether AI is the right solution to the right problem.

- `problem-ai-fit` — Scores AI fit 0-16. Runs the "lookup table test" — would rules solve 80%?
- `failure-modes` — Maps exactly how the feature will fail. 6 hallucination types × severity matrix
- `invisible-stack` — Surfaces the 60-80% of engineering users never see (retrieval, validation, monitoring)
- `feedback-flywheel` — How user corrections become data that improves the model over time
- `uncertainty-research` — How to research products with non-deterministic output
- `ai-ux-patterns` — Interaction patterns that build human-AI trust
- `ai-product-taste` — The quality bar separating "remarkable" from "AI for the sake of AI"
- `ai-use-case-readiness` — Maps right-sized autonomy: solution spectrum (0-7), dual matrices, 25 diagnostic questions with answer nudges. Bridges product sense, agent design, and strategy
- `needs-guard` — Ensures AI deployment doesn't threaten worker psychological needs (autonomy, competence, belonging). 31% actively resist; 54% use unauthorized tools. AWARE framework diagnoses which need is broken

### AI Strategy (10 skills)
Strategy when the capabilities you're building on change every quarter.

- `strategy-canvas` — Capability-conditional roadmaps with expiration dates
- `moat-finder` — Where durable advantage comes from: data flywheels, workflow lock-in, context depth, earned trust
- `build-or-buy` — The AI trilemma: prompt it, RAG it, fine-tune it, or buy an API
- `token-economics` — Cost modeling when marginal cost is per-token. Cached prompt economics
- `capability-tracking` — Strategy half-life: how long until this capability is commoditized
- `adoption-launch` — Treats AI adoption as a product launch with phases (Surge → Dip → Rebound), personas, and phase-specific support. 50% churn at month 3 without intervention
- `trendslop-check` — Catches when AI defaults to trendy advice instead of context-specific strategy. Across 15,000+ trials, LLMs systematically favor differentiation over cost-leadership
- `signal-scanner` — Detects weak signals early via dual-speed sensing (real-time operational + long-term strategic). 5% financial lift for companies with systematic scanning
- `purpose-dialogue` — Connects AI initiatives to organizational purpose through dialogue, not posters. 10% commitment lift per point. Best Buy turnaround case
- `ai-portfolio-management` — Manages AI investments like a financial portfolio. Dual Lens, OPEN framework, 3E hypothesis gate, Buy/Sell/Hold, Stage Gates

### Safety & Trust (7 skills)
Safety as competitive advantage, not compliance cost.

- `safety-as-moat` — Quantifies the "alignment tax" and shows where safety builds trust competitors can't match
- `trust-ladder` — When AI should act, ask, or refuse. Calibrated confidence with trust repair
- `safety-by-design` — Constitutional principles built into architecture: 5-10 rules the system must never violate
- `responsible-ai-program` — Makes responsible AI operational. SHARP framework. Named owners, fairness gates, aligned incentives
- `breach-ready` — Designs systems that SURVIVE being hacked. 48-hour manual operations test. FedEx/NotPetya resilience case
- `agent-risk` — Proportionality analysis (value vs worst-case harm) + kill-switch design. If you can't kill it faster than harm cascades, don't deploy
- `trust-under-fog` — Communicates confidently when outcomes are genuinely uncertain. Bounded promises, transparent ranges, uncertainty budgets

### Agent Design (5 skills)
For AI that acts, not just answers.

- `autonomy-spectrum` — Maps each capability from Level 0 (suggest) to Level 4 (autonomous). Progressive trust
- `agent-ecosystem` — Multi-agent orchestration: sequential, parallel, hierarchical. Error boundaries
- `tool-architecture` — MCP/A2A tool access with consequence magnitude-aware permissions. Kill switches
- `multi-modal-product-design` — Cross-modal AI features. Modality-specific failure modes
- `agent-harness` — Planner → Generator → Evaluator architecture. Sprint contracts. Context management

### Eval & Quality (6 skills)
If you can't measure it, you can't ship it.

- `eval-framework` — pass@k (one good result in k tries) vs pass^k (every result must be good). LLM-as-judge
- `eval-driven-development` — Evals before code. Handles criteria drift as quality bar evolves
- `ai-product-metrics` — Acceptance rate, correction rate, time-to-value. Eval saturation detection
- `production-observability` — Silent degradation, context anxiety, distribution drift. What traditional APM misses
- `gen-ai-experimentation` — Designs rigorous experiments with causal evidence. Segmented analysis: 14% overall lift but 34% for juniors, near-zero for seniors
- `confidence-tuner` — Designs trust signals so users neither over-rely on AI nor ignore it. 49% error reduction through calibrated confidence alerts. Endorse/Caution/Warn system

**Key property:** Layer 2 skills import from Layer 1 but never from each other across plugins. No circular dependencies. Each plugin is independently installable.

---

## Layer 3: Craft — "Production-ready output" (8 skills)

Artifact generators. But because each one imports Layers 1 and 2 first, the output arrives pre-tested.

| Skill | What it produces | What it imports first |
|-------|-----------------|----------------------|
| `ai-prd` | PRD with eval gates, failure budgets, probabilistic specs | determinism-compass → bias-spotter → stress-test |
| `context-spec` | Context architecture blueprint | invisible-stack → determinism-compass → stress-test |
| `agent-spec` | Agent boundary matrix with autonomy levels per step | autonomy-spectrum → agent-ecosystem → agent-harness → failure-design |
| `cost-model` | Token cost at scale with path to profitability | stress-test → token-economics → agent-harness |
| `ship-decision` | Eval-gated go/no-go decision | stress-test → safety-as-moat → failure-design → bias-spotter → eval-framework |
| `competitive-map` | AI-specific competitive analysis | moat-finder → first-principles |
| `fit-signal` | PMF diagnosis for non-deterministic products | feedback-flywheel → falsification → stress-test |
| `prompt-as-product` | Prompt versioning with regression testing | eval-framework → determinism-compass |

**Key property:** Craft skills are the only ones that produce files. Layer 1 produces reasoning. Layer 2 produces decisions. Layer 3 produces artifacts that encode both.

---

## The Import Chain

This is the core mechanism. Here's what happens when you ask for a PRD:

```
You: "Write a PRD for our AI coding assistant"

  ┌─ Layer 1 runs first ──────────────────────────────────────┐
  │                                                             │
  │  determinism-compass                                        │
  │  → "Autocomplete: must be right every time (rules).         │
  │     Code explanation: can vary (AI).                        │
  │     Refactoring: needs human approval (hybrid)."            │
  │                                                             │
  │  bias-spotter                                               │
  │  → "You're anchored on what Copilot does. Your users are   │
  │     enterprise — they need auditability, not speed."        │
  │                                                             │
  │  stress-test                                                │
  │  → "At 10x usage, context costs hit $0.12/query.           │
  │     P95 latency spikes to 8s on large files."              │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
                            ↓
  ┌─ Layer 3 generates ────────────────────────────────────────┐
  │                                                             │
  │  ai-prd                                                     │
  │  → PRD with: eval criteria as acceptance criteria,          │
  │    failure budgets per feature, cost model built in,        │
  │    determinism classification per capability,               │
  │    prompt specifications versioned like code                │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

**Without the import chain:** A PRD that says "leverage AI to enhance developer productivity."
**With the import chain:** A PRD that engineering can build from, finance can model, and QA can test against.

---

## Dependency Graph

Full import chain for every skill that has dependencies:

```
craft/ai-prd ──────────► thinking-core/determinism-compass
                 ├─────► thinking-core/bias-spotter
                 └─────► thinking-core/stress-test

craft/context-spec ────► product-sense/invisible-stack
                 ├─────► thinking-core/determinism-compass
                 └─────► thinking-core/stress-test

craft/agent-spec ──────► agent-design/autonomy-spectrum
                 ├─────► agent-design/agent-ecosystem
                 ├─────► agent-design/agent-harness
                 └─────► thinking-core/failure-design

craft/cost-model ──────► thinking-core/stress-test
                 ├─────► ai-strategy/token-economics
                 └─────► agent-design/agent-harness

craft/ship-decision ───► thinking-core/stress-test
                 ├─────► safety-and-trust/safety-as-moat
                 ├─────► thinking-core/failure-design
                 ├─────► thinking-core/bias-spotter
                 └─────► eval-and-quality/eval-framework

craft/competitive-map ─► ai-strategy/moat-finder
                 └─────► thinking-core/first-principles

craft/fit-signal ──────► product-sense/feedback-flywheel
                 ├─────► thinking-core/falsification
                 └─────► thinking-core/stress-test

craft/prompt-as-product ► eval-and-quality/eval-framework
                 └─────► thinking-core/determinism-compass

eval-and-quality/eval-framework ► product-sense/feedback-flywheel
                 ├─────► thinking-core/first-principles
                 └─────► thinking-core/stress-test

eval-and-quality/eval-driven-development ► eval-and-quality/eval-framework
                 └─────► product-sense/feedback-flywheel

eval-and-quality/ai-product-metrics ► eval-and-quality/eval-framework
                 └─────► product-sense/feedback-flywheel

eval-and-quality/production-observability ► thinking-core/stress-test
                 └─────► eval-and-quality/eval-framework

agent-design/agent-harness ─► agent-design/agent-ecosystem
                 ├─────► eval-and-quality/eval-framework
                 └─────► thinking-core/stress-test

agent-design/tool-architecture ► thinking-core/determinism-compass
                 └─────► agent-design/autonomy-spectrum

product-sense/ai-use-case-readiness ─► thinking-core/first-principles
                 ├─────► thinking-core/determinism-compass
                 └─────► agent-design/autonomy-spectrum
```

---

## 6 Workflows

Workflows are curated paths through the skill graph. Different situations need different subsets:

| Workflow | When to use it | Skills | Timeline |
|----------|---------------|--------|----------|
| **New AI Feature** | Full cycle: discover → strategize → spec → ship | 40/40 | 12 days |
| **Discovery Sprint** | Validate an AI idea before committing engineering | 30/40 | 5 days |
| **Quarterly Strategy Review** | Check if strategy still holds as capabilities shift | 35/40 | 5 days |
| **Eval Ops Setup** | Build evaluation infrastructure from zero | 22/40 | 5 days |
| **Agent Launch Checklist** | Ship an autonomous AI feature safely | 24/40 | 3-5 days |
| **AI Incident Response** | AI feature broke in production | 25/40 | Hours |

---

## File Structure

Every skill has two files. One for the AI, one for you:

```
skill-name/
├── SKILL.md     # For the LLM — lean, directive, every token earns its place
└── CONCEPT.md   # For humans — deep context, intellectual lineage, examples
```

**SKILL.md** has 8 sections: depth decision (when to go deep vs skim), the trap (the mistake you're about to make), the process (diagnostic questions, not recipes), key diagnostic questions, reality check, output format, quality gate, and when this skill gives bad advice.

**CONCEPT.md** has 6 sections: first principles, dual definition (business + technical), the trap expanded, intellectual lineage, real-world examples, and further reading.

---

## Plugin Structure

Each plugin is self-contained and independently installable:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json       # Metadata, version, skill list
├── skills/
│   ├── skill-a/
│   │   ├── SKILL.md
│   │   └── CONCEPT.md
│   └── skill-b/
│       ├── SKILL.md
│       └── CONCEPT.md
└── commands/
    └── command-name.md   # Optional CLI commands
```

**Install rules:**
- `thinking-core` is the foundation — install with anything else
- Any Layer 2 plugin works independently (with `thinking-core`)
- `craft` requires `thinking-core` + at least one Layer 2 plugin
- `eval-and-quality` is strongly recommended for any production deployment
- `ai-use-case-readiness` lives in `product-sense` but imports from `agent-design` (autonomy-spectrum) — making it a cross-plugin bridge skill
- Installing everything gives the full composable system

---

## Design Decisions

**Why separate SKILL.md and CONCEPT.md?**
SKILL.md is optimized for LLM context windows — every token counts. CONCEPT.md is for humans reading on GitHub — depth, nuance, lineage. Mixing them wastes tokens or shortchanges understanding.

**Why the import chain instead of monolithic skills?**
Composability. A monolithic `ai-prd` with bias-checking, stress-testing, and determinism classification would be 800+ lines. Importing atomic skills keeps each focused and independently improvable.

**Why five Layer 2 plugins instead of four?**
`eval-and-quality` was extracted from `craft` because evaluation is a judgment discipline, not an artifact. You need eval thinking in discovery, strategy, and safety — not just when writing specs. Making it Layer 2 means every craft skill can import eval judgment.

**Why diagnostic questions instead of step-by-step processes?**
World-class PMs know what questions to ask, not what steps to follow. A rigid process breaks when context changes. Diagnostic questions adapt: a chatbot PM and an agent PM read the same `eval-framework` but ask different questions and reach different eval strategies.

**Why DEPTH DECISION at the top of every skill?**
Practitioners are busy. A PM mid-PRD doesn't need all 250 lines of `eval-framework` — they need to know if they should go deep, skim, or skip. Progressive disclosure respects time while making depth available when needed.

**Why 6 workflows instead of 1?**
Different contexts need different skill subsets. You don't run all 40 skills for an incident. Workflows are curated paths: `new-ai-feature` uses all 40; `ai-incident-response` uses 25 focused on diagnosis and recovery.

---

## The Answer Nudges Architecture

Every diagnostic question in every skill includes answer nudges. This isn't a formatting choice — it's an architectural decision that encodes senior PM judgment into the skill files themselves.

### Structure of Answer Nudges

Each nudge contains:

- **Thinking dimensions** — The conceptual axes that actually matter (financial cost vs. reputational damage vs. regulatory exposure)
- **Spectrum anchors** — Concrete examples at each end of the spectrum so practitioners calibrate to concrete situations, not abstract scales
- **Red flag patterns** — Signals that you're about to make a mistake (confusing solution spectrum with autonomy spectrum, anchoring on competitor precedent)
- **Sharpening probes** — Follow-up questions that deepen the diagnostic (if cost is the constraint, is it marginal cost per token or infrastructure cost?)

### Why Answer Nudges Instead of Just Better Questions?

Questions identify what to think about. Answer nudges teach *how* to think about it. A question like "What's the cost of error?" has infinite valid answers. The nudge constrains the thinking space to the dimensions that actually matter — financial, reputational, regulatory, safety, cascading — and provides calibration anchors so a PM in healthcare and a PM in e-commerce can both use the same question productively. This is the difference between a diagnostic instrument and a diagnostic textbook.

### Why Spectrum Anchors Instead of Scoring Rubrics?

Rubrics create false precision ("cost of error = 3 out of 5"). Spectrum anchors create genuine understanding ("cost of error is between 'wrong product recommendation' and 'unauthorized financial transaction' — closer to the recommendation end"). Practitioners calibrate better with examples than with numbers.

### The Import Chain + Answer Nudges = Skills That Teach

The import chain makes skills that check your work. Answer nudges make skills that teach you how to check. Together:

- When you use `ai-use-case-readiness`, you don't just score autonomy — the nudges teach you what distinguishes a Level 2 ("suggest with approval") from a Level 3 ("act with audit trail")
- When you import `determinism-compass` into a craft skill, you're not just classifying features — the nudges teach you why a chatbot's completion needs determinism but a code explainer's variability is a feature
- When an `eval-framework` question asks about sample efficiency, the nudges show you the difference between "we need 10k examples" (rubric thinking) and "we need enough examples to catch edge cases in the long tail" (spectrum thinking)

This is why answer nudges are structural, not decorative. They turn a diagnostic skill into a teaching instrument.

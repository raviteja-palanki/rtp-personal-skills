# AI Discovery Sprint: 5-Day Intensive
**Structured discovery adapted for AI products**

A compressed, high-intensity discovery sprint for teams that need to understand a new AI product idea, validate core assumptions, or map the failure landscape before committing to build. Orchestrates skills from all 7 plugins with discovery-focused depth.

**Timeline:** 5 days (1 day per theme)
**Audience:** Product managers, design leads, technical leads, research leads
**Cadence:** Run quarterly, when a new AI idea emerges, or when core assumptions feel shaky
**Output:** Validated problem-solution fit; mapped failure landscape; architecture clarity; research roadmap; falsified and validated key assumptions
**Skill Coverage:** 30 of 39 skills (discovery-focused subset; remaining 9 are spec/launch skills used in new-ai-feature workflow)

---

## Day 1: Problem Space & AI Fit

**Goal:** Deeply understand the problem and test whether AI is actually the right solution.

### Morning: First Principles & Bias Check

**Layer 1 — Thinking Core:**
1. **first-principles** — Break the problem down to core principles.
   - What is the user's core need stripped of jargon?
   - What constraints are fundamental vs. temporary?
   - What would an ideal solution look like with unlimited resources?
   - Classify the atomic operation: LOOKUP, TRANSFORM, CLASSIFY, or GENERATE?

2. **bias-spotter** — Run a bias audit on the initial framing.
   - Are we anchored on "AI" as the solution before understanding the problem?
   - Is there survivorship bias from competitor success stories?
   - Are we confusing "technically possible" with "product-valuable"?
   - Check for Maslow's Hammer, sunk-cost, and availability bias.

### Afternoon: AI-Solution Fit & Taste

**Layer 2 — Product Sense:**
3. **problem-ai-fit** — Score AI fit (0-16 across four dimensions: input variability, output judgment, data availability, error tolerance).
   - Run the lookup table test: could rules/heuristics solve 80%?
   - Where does AI add irreplaceable value?
   - What would a non-AI solution cost in time and accuracy?
   - Is the user willing to interact with an AI-driven solution?

4. **ai-product-taste** — Apply taste calibration to the concept.
   - Does this feel like a "museum quality" AI feature or just "AI for the sake of AI"?
   - Run domain-specific taste criteria for the relevant vertical.
   - What would a world-class AI PM critique about this idea?

### Close of Day
- **Output:** Problem statement refined; AI fit scored (0-16); bias audit clean; atomic operation classified; taste assessment documented

---

## Day 2: Failure Mapping & Safety

**Goal:** Understand how this feature will fail, what that means for users, and how to design safety in from the start.

### Morning: Failure Surface

**Layer 2 — Product Sense:**
5. **failure-modes** — Map the failure surface comprehensively.
   - What are the top 10 ways the AI will get this wrong?
   - Classify by type: fabrication, drift, attribution, omission, confidence, cascade
   - What are the consequences of each? (user frustration, data loss, safety issue, trust erosion)
   - Which failure modes are unavoidable vs. designable?

**Layer 1 — Thinking Core:**
6. **failure-design** — Design for failure, not around it.
   - How will the feature degrade gracefully when the AI is wrong?
   - Where do humans need to verify or override?
   - Build fallback cascades: AI → simpler model → rules → human
   - What patterns from other AI products can we learn from?

### Afternoon: Safety & Trust Foundations

**Layer 2 — Safety & Trust:**
7. **safety-as-moat** — Frame safety as competitive advantage early.
   - What could go wrong that would erode user trust permanently?
   - Where does safety become a feature (not just compliance)?
   - Quantify the alignment tax: what does safety cost in latency, accuracy, or complexity?

8. **safety-by-design** — Sketch constitutional AI principles.
   - What 5-10 behavioral rules must this feature NEVER violate?
   - Design defense-in-depth layers for the most critical failure modes.
   - How will adversarial inputs be handled?

**Layer 1 — Thinking Core:**
9. **stress-test** — Run 6-dimension stress testing on the concept.
   - Scale stress: what happens at 10x, 100x current assumptions?
   - Adversarial stress: how do malicious users exploit this?
   - Model degradation: what if model quality drops 10-20%?
   - Context poisoning: what if retrieval returns bad data?

### Close of Day
- **Output:** Failure landscape mapped (10+ modes classified); degradation paths designed; safety principles drafted; stress test results documented

---

## Day 3: Architecture & Agent Design

**Goal:** Understand the technical and product architecture required to make this feature work.

### Morning: Determinism & Architecture

**Layer 1 — Thinking Core:**
10. **determinism-compass** — Map determinism requirements.
    - What parts must be deterministic? (critical decisions, compliance, repeatability)
    - What parts can be probabilistic? (creative suggestions, drafts)
    - Classify: pass@k (at least one good result) vs. pass^k (every result must be good)
    - How does non-determinism affect debugging, testing, and user trust?

**Layer 2 — Product Sense:**
11. **invisible-stack** — Map the hidden architecture.
    - What context retrieval is needed? (RAG, API calls, user history)
    - What post-processing, formatting, or validation happens after AI responds?
    - What monitoring and logging will you need?
    - What's the infrastructure cost of making this fast enough?

### Afternoon: Agent & Tool Architecture

**Layer 2 — Agent Design:**
12. **autonomy-spectrum** — Map where on the autonomy spectrum this feature sits.
    - Level 0 (suggest) through Level 4 (autonomous): where does each capability land?
    - What context anxiety thresholds apply?
    - Design progressive autonomy path based on trust signals.

13. **agent-ecosystem** *(if multi-agent)* — Sketch orchestration patterns.
    - Sequential, parallel, or hierarchical agent coordination?
    - What are the error boundaries between agents?
    - Where do harness patterns (Planner→Generator→Evaluator) apply?

14. **tool-architecture** *(if tool-using)* — Map tool access requirements.
    - Classify tools by mutation type: read-only, write-reversible, write-audited, delete, cascade
    - How many tools? (each consumes ~500 tokens of context)
    - What MCP/A2A patterns apply?

15. **agent-harness** *(if complex agent)* — Sketch harness architecture.
    - Does this need a Planner→Generator→Evaluator pattern?
    - What are the sprint contract criteria?
    - Where is the Pre-Rot Threshold for context management?

16. **multi-modal-product-design** *(if multi-modal)* — Map modality interactions.
    - What input/output modality combinations are needed?
    - What are modality-specific failure modes?
    - How do modalities reinforce or conflict with each other?

### Close of Day
- **Output:** Technical architecture sketched; determinism requirements mapped; autonomy levels assigned; agent patterns identified; tool access scoped

---

## Day 4: Research, Learning & Evaluation

**Goal:** Design the research program and evaluation framework that will reduce your biggest uncertainties.

### Morning: Uncertainty & Research

**Layer 2 — Product Sense:**
17. **uncertainty-research** — Map unknowns and design rapid tests.
    - What are your 5 biggest assumptions? Rank by impact × confidence.
    - What's the minimum test to validate or invalidate each?
    - Who are your learning partners? (users, domain experts, existing data)
    - What can you learn in a week vs. needing months?

18. **feedback-flywheel** — Design the learning loop.
    - How will you collect signals about whether the AI is working?
    - How will signals feed back into model improvement or feature iteration?
    - What's the latency between observing a problem and fixing it?
    - How will you avoid local optima?

### Afternoon: Evaluation & Metrics

**Layer 2 — Eval & Quality:**
19. **eval-framework** — Sketch the evaluation approach.
    - What metrics will measure quality? (accuracy, relevance, safety, latency)
    - What test sets will you need? How will you build them?
    - What acceptance thresholds make sense for discovery vs. production?
    - Is this a pass@k or pass^k problem?

20. **eval-driven-development** — Plan the EDD cycle.
    - How will evals drive iteration during build?
    - Plan for criteria drift: how will eval criteria evolve as you observe outputs?
    - What's the eval dataset refresh cadence?

21. **ai-product-metrics** — Define the metrics dashboard.
    - Map key metrics: pass@k, acceptance rate, correction rate, time-to-value
    - Set up eval saturation detection thresholds
    - Design the monitoring stack for post-launch

22. **production-observability** — Plan the observability stack.
    - What silent degradation signals will you monitor?
    - How will you detect context anxiety in agents?
    - What drift detection alerts are needed?

### Close of Day
- **Output:** Research roadmap (30/60/90 days); eval framework sketched; metrics dashboard defined; observability plan documented

---

## Day 5: Synthesis & Red Team

**Goal:** Integrate all learning and test your core assumptions against reality.

### Morning: Synthesis

**Layer 1 — Thinking Core:**
23. **dual-lens** — Synthesize product and technical perspectives.
    - What did discovery teach you that invalidates or strengthens your hypothesis?
    - Are there user needs that don't require AI?
    - What's the gap between "technically feasible" and "commercially viable"?
    - What's the top risk that could derail this feature?

**Layer 2 — AI Strategy:**
24. **strategy-canvas** — Quick strategic positioning.
    - Where does this feature sit in the competitive landscape?
    - What capability-conditional bets are we making?
    - What trade-offs are we accepting?

25. **moat-finder** — Initial moat assessment.
    - Where would defensibility come from? (data, model, UX, integration, trust)
    - How quickly could a competitor replicate this?
    - Is the moat strengthening or eroding over time?

26. **capability-tracking** — Assess capability dependencies.
    - Which model capabilities are we betting on?
    - What's the strategy half-life? When will this be commoditized?

### Afternoon: Red Team & Economics

**Layer 1 — Thinking Core:**
27. **red-team** — Test core hypotheses against evidence.
    - What would disprove your core hypotheses?
    - Do you have evidence these things are NOT true?
    - Run pre-mortem: "It's 6 months post-launch and this failed — why?"
    - If your core hypothesis is false, what do you do?

**Layer 2 — AI Strategy:**
28. **token-economics** — Quick economics sanity check.
    - What will this cost per query at scale?
    - Are cached prompt economics applicable?
    - Is there a path to sustainable unit economics?

**Layer 2 — Safety & Trust:**
29. **trust-ladder** — Sketch the trust journey.
    - How will users experience the feature's confidence?
    - What's the trust repair path when AI fails?
    - Where are the human-AI handoff points?

**Layer 2 — Product Sense:**
30. **ai-ux-patterns** — Validate interaction patterns.
    - Are confidence displays appropriate for the use case?
    - Are human-AI handoffs smooth?
    - Does the interaction feel natural or forced?

### Close of Day
- **Output:** Validated and falsified assumptions documented; next phase decision (go/pivot/kill); strategic positioning sketched; economics sanity-checked; clear input to strategy phase

---

## Skill Coverage Matrix

| Plugin | Skills Used | Day |
|--------|------------|-----|
| **thinking-core** (7/7) | first-principles, bias-spotter, red-team, dual-lens, determinism-compass, stress-test, failure-design | 1,2,3,5 |
| **product-sense** (7/7) | problem-ai-fit, failure-modes, invisible-stack, feedback-flywheel, uncertainty-research, ai-ux-patterns, ai-product-taste | 1,2,3,4,5 |
| **ai-strategy** (4/5) | strategy-canvas, moat-finder, token-economics, capability-tracking | 5 |
| **safety-and-trust** (3/3) | safety-as-moat, trust-ladder, safety-by-design | 2,5 |
| **agent-design** (5/5) | autonomy-spectrum, agent-ecosystem, tool-architecture, multi-modal-product-design, agent-harness | 3 |
| **eval-and-quality** (4/4) | eval-framework, eval-driven-development, ai-product-metrics, production-observability | 4 |
| **craft** (0/8) | *(craft skills are spec/launch artifacts — used in new-ai-feature workflow, not discovery)* | — |

**Total: 30/39 skills referenced** (remaining 9 are craft/artifact generators used during specification, not discovery)

**Skills NOT used in discovery** (intentionally — these produce artifacts, not insights):
- ai-prd, context-spec, agent-spec, cost-model, ship-decision, competitive-map, fit-signal, prompt-as-product, build-or-buy

---

## Deliverables

By end of sprint, you'll have:

1. **Problem Definition** — Refined with first-principles grounding and bias audit
2. **AI Fit Statement** — Scored 0-16; specific value AI adds; non-AI alternatives understood
3. **Failure Map** — 10+ failure modes classified by type; degradation patterns designed
4. **Safety Principles** — Constitutional rules drafted; stress test results documented
5. **Architecture Sketch** — Determinism map; autonomy levels; agent patterns; tool access scoped
6. **Eval Framework** — Metrics defined; test approach sketched; observability planned
7. **Research Roadmap** — 30/60/90-day learning plan with red-team tests
8. **Go/No-Go Assessment** — Clear recommendation to continue, pivot, or kill

---

## Daily Rhythm

Each day follows this pattern:
- **9am-12pm:** Deep work on primary skills (2-3 skills)
- **12pm-1pm:** Lunch / integration time
- **1pm-4pm:** Secondary skills or validation (2-3 skills)
- **4pm-5pm:** Daily synthesis (what did we learn? what changes tomorrow?)
- **Optional 5-6pm:** Cross-functional debrief (share outputs, challenge assumptions)

---

## Facilitation Tips

1. **Bring the right people:** At least one person per functional area (product, design, engineering, data/research)
2. **Debate is good, consensus isn't required:** Different perspectives surface risks
3. **Write everything down:** Assumptions live in documents; debate in real-time, document the outcome
4. **Use evidence, not intuition:** Questions should point to user research, competitive analysis, or existing data
5. **One clear owner per day:** That person synthesizes and drives to outputs
6. **Default to skepticism:** If something sounds too easy, it probably is
7. **Score, don't just discuss:** Use the scoring frameworks (Problem-AI Fit 0-16, autonomy levels 0-4) to force precision

---

## When to Run This Sprint

- **New AI product idea:** Before you commit engineering effort
- **Quarterly check-in:** To validate assumptions haven't decayed
- **Significant pivot:** When market signals suggest your core hypothesis might be wrong
- **User complaints at scale:** Before you redesign in response to noise
- **Competitive threat:** To reassess if your moat still exists
- **Model capability jump:** When a new model release changes what's possible

---

## Follow-Up

After the sprint, the next phase depends on your findings:
- **Strong product-market signals:** Move to **new-ai-feature** workflow (strategy → spec → launch) — uses all 39 skills including craft artifacts
- **Mixed signals:** Run a 2-week MVP to test core assumptions with users
- **Falsified assumptions:** Kill or pivot the idea; restart discovery with new hypothesis
- **Technical blockers:** Spike on infrastructure, model capabilities, or feasibility
- **Safety concerns:** Deep dive into safety-by-design and trust-ladder before proceeding

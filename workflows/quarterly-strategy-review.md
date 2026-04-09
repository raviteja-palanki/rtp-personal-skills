# Quarterly Strategy Review: Capability & Moat Check
**Refresh strategy with evolving AI landscape**

A structured quarterly workflow for product strategy review, especially critical in AI where model capabilities, competitive landscape, and token economics shift rapidly. Orchestrates skills from all 7 plugins to ensure no strategic blind spots.

**Timeline:** 5 days (one step per day)
**Frequency:** Every quarter (or when major model releases happen)
**Audience:** Product leaders, strategy leads, engineering heads, AI specialists
**Output:** Updated strategy document; identified moat erosion; build-or-buy reassessment; eval health check; adjusted roadmap for next quarter
**Skill Coverage:** 35 of 39 skills (strategy-focused subset; 4 agent-design skills used only when agent features are in scope)

---

## Context & Why This Matters

AI moves fast. A moat built on proprietary data erodes if a new model makes your data less valuable. Cost structure assumptions break if token pricing drops 40%. Build-or-buy decisions flip if new APIs become available. Eval frameworks degrade if criteria drift isn't detected. This quarterly review keeps your strategy synchronized with reality.

---

## Step 1: Volatile Assumptions Check (Day 1)

**Goal:** Identify assumptions that have aged poorly and need re-evaluation.

### Morning: Strategy Canvas Reassessment

**Layer 2 — AI Strategy:**
1. **strategy-canvas** — Run a quarterly check on your strategy canvas.
   - What was your competitive hypothesis at the start of the quarter?
   - Is the landscape still accurate? Have competitors moved?
   - Have new models/APIs changed what's feasible?
   - What capability-conditional roadmap items have triggered or expired?
   - What trade-offs are you making? Do they still make sense?

2. **capability-tracking** — Assess strategy half-life.
   - Which capabilities have been commoditized since last quarter?
   - Which new capabilities have emerged?
   - Track benchmark trajectories: MMLU, HumanEval, SWE-bench, GPQA
   - Has your strategy half-life shortened or lengthened?

### Afternoon: Assumption Volatility Audit

**Layer 1 — Thinking Core:**
3. **red-team** — Test each assumption against current evidence.
   - List all strategic assumptions from last quarter
   - For each: what would disprove it? Has that evidence appeared?
   - Run pre-mortem: "It's end of next quarter and our strategy failed — why?"

4. **bias-spotter** — Check for decision biases in the team.
   - Are we anchored on last quarter's strategy?
   - Are we suffering from sunk-cost fallacy on current bets?
   - Is there survivorship bias in our competitive analysis?

### Close of Day
- **Output:** Volatility audit completed; assumptions rated Green/Yellow/Red; capability half-life updated

---

## Step 2: Moat & Competitive Health Check (Day 2)

**Goal:** Assess whether your competitive advantage still exists and is defensible.

### Morning: Moat Analysis

**Layer 2 — AI Strategy:**
5. **moat-finder** — Run moat analysis focused on erosion.
   - What was your original moat? (data flywheel, workflow lock-in, context depth, earned trust)
   - Has it eroded? How? How quickly?
   - Are competitors closing the gap?
   - Can you strengthen the moat? Or should you shift defensibility?

**Layer 3 — Craft:**
6. **competitive-map** — Update your competitive landscape.
   - Who are your direct competitors today? Has the list changed?
   - New entrants or incumbents moving into your space?
   - For each competitor: moat, positioning, go-to-market
   - Where do you win? Where do they win?

### Afternoon: Product Sense Check

**Layer 2 — Product Sense:**
7. **ai-product-taste** — Run taste calibration on your current product.
   - Does your product still feel "museum quality" or has it stagnated?
   - Apply domain-specific taste criteria: has the bar moved?
   - What would a world-class AI PM critique today?

8. **ai-ux-patterns** — Review UX against evolving best practices.
   - Are your confidence displays still calibrated correctly?
   - Have user expectations evolved? (users now expect more from AI)
   - Are there new AI UX patterns competitors are using that you aren't?

### Close of Day
- **Output:** Moat health assessment; competitive map updated; taste and UX gaps identified

---

## Step 3: Build-or-Buy & Architecture Reassessment (Day 2-3)

**Goal:** Re-evaluate whether you should still build this capability in-house.

### Morning: Build-or-Buy Update

**Layer 2 — AI Strategy:**
9. **build-or-buy** — Re-run build-or-buy with current model capabilities.
   - Has the Build-or-Buy Trilemma shifted? (prompt vs RAG vs fine-tune vs API)
   - Are there new APIs, partnerships, or vendors to consider?
   - Has the model-agnostic abstraction layer strategy held?
   - What's the cost-benefit today vs. 3 months ago?

**Layer 2 — Product Sense:**
10. **invisible-stack** — Reassess the hidden architecture.
    - Has retrieval performance degraded or improved?
    - Are post-processing and validation costs where you expected?
    - Has infrastructure cost changed with new model pricing?

### Afternoon: Agent & Tool Architecture Review

**Layer 2 — Agent Design (if applicable):**
11. **agent-ecosystem** — Review agent orchestration health.
    - Are agent patterns (sequential, parallel, hierarchical) still optimal?
    - Has harness architecture (Planner→Generator→Evaluator) performed as designed?
    - Any new agent failure patterns emerged?

12. **tool-architecture** — Review tool access and MCP ecosystem.
    - Are tool permissions still appropriate? Permission inflation check.
    - Any new MCP connectors that could improve capabilities?
    - Are rate limits and escape hatches still calibrated?

13. **agent-harness** *(if harness in production)* — Review harness performance.
    - Are sprint contracts still effective? Criteria drift?
    - Context management: has Pre-Rot Threshold shifted?
    - Generator quality: is pass rate improving or stagnating?

14. **autonomy-spectrum** — Review autonomy levels.
    - Should any features move up or down the autonomy spectrum?
    - Are context anxiety thresholds still appropriate?
    - Has user trust earned higher autonomy for any features?

15. **multi-modal-product-design** *(if multi-modal)* — Review modality performance.
    - Are cross-modal interactions working as designed?
    - New modalities available that should be integrated?

### Close of Day
- **Output:** Updated build-or-buy decision; architecture health assessed; agent patterns reviewed

---

## Step 4: Economics & Evaluation Review (Day 3-4)

**Goal:** Validate unit economics and evaluation framework health.

### Morning: Economics Update

**Layer 2 — AI Strategy:**
16. **token-economics** — Re-run token cost model with current pricing.
    - Have model prices changed? (usually downward)
    - Have usage patterns changed? (context window growth, query complexity)
    - Are cached prompt economics being fully leveraged? (90% discount)
    - Is model routing ROI where expected?

**Layer 3 — Craft:**
17. **cost-model** — Update unit economics.
    - Baseline cost per unit: expected vs. actual
    - Harness economics: are harness costs ($200/task range) justified by quality?
    - New cost levers discovered? (smarter prompting, batching, routing)
    - Path to profitability at current scale

### Afternoon: Evaluation Health Check

**Layer 2 — Eval & Quality:**
18. **eval-framework** — Review eval framework health.
    - Are eval metrics still aligned with user value?
    - Has eval saturation occurred? (high pass rates with stale test sets)
    - Agent-type-specific evals: still appropriate?
    - Do acceptance thresholds need adjustment?

19. **eval-driven-development** — Check EDD discipline.
    - Is the team running evals before shipping?
    - Has criteria drift been detected and addressed?
    - Is eval dataset refresh happening on cadence?

20. **ai-product-metrics** — Review metrics dashboard.
    - pass@k and pass^k trends: improving, flat, or declining?
    - Acceptance rate and correction rate trajectories
    - Eval saturation detection: any alerts triggered?

21. **production-observability** — Review monitoring health.
    - Are silent degradation signals being caught?
    - Context anxiety detection: working as designed?
    - Sprint contract compliance: tracked and trending?
    - Drift detection: any unexpected distribution shifts?

### Close of Day
- **Output:** Updated cost model; eval framework health assessed; metrics trends documented; observability gaps identified

---

## Step 5: PMF & Safety Posture (Day 4)

**Goal:** Confirm product-market fit is holding and safety practices have evolved.

### Morning: PMF Health Check

**Layer 3 — Craft:**
22. **fit-signal** — Re-evaluate product-market fit signals.
    - What signals said you had PMF last quarter? Do they still hold?
    - New signals emerged? (churn, feature stagnation, complaints)
    - Segment-by-segment: where is PMF strong vs. weak?
    - If PMF is degrading, is it competitive, product, or market shift?

**Layer 2 — Product Sense:**
23. **feedback-flywheel** — Review the learning loop.
    - Is the flywheel spinning? (signals → improvements → better signals)
    - What's the latency between observing a problem and fixing it?
    - Is the team avoiding local optima?

24. **uncertainty-research** — Reassess current unknowns.
    - What new uncertainties have emerged since last quarter?
    - Which previous uncertainties have been resolved?
    - What research is needed for next quarter?

### Afternoon: Safety Posture

**Layer 2 — Safety & Trust:**
25. **safety-as-moat** — Review safety position.
    - Have regulatory expectations changed?
    - New failure modes discovered in production?
    - Is safety building competitive advantage or just avoiding damage?
    - Are there new safety risks from new model capabilities?

26. **safety-by-design** — Review constitutional principles.
    - Are the 5-10 behavioral rules still comprehensive?
    - Any new adversarial patterns that need defense?
    - Multi-agent safety boundaries: still holding?

27. **trust-ladder** — Review trust health.
    - Has user trust improved, held, or eroded?
    - Are trust repair mechanisms working when AI fails?
    - Should calibrated confidence displays be adjusted?
    - Any trust-autonomy calibration changes needed?

### Close of Day
- **Output:** PMF assessment by segment; safety posture reviewed; trust health documented

---

## Step 6: Synthesis & Roadmap Adjustment (Day 5)

**Goal:** Synthesize all findings into updated quarterly priorities.

### Morning: Pattern Recognition & Synthesis

**Layer 1 — Thinking Core:**
28. **dual-lens** — Synthesize product and technical findings.
    - What themes emerge? (moat erosion, cost opportunities, PMF risk, eval gaps, safety needs)
    - Where is the biggest leverage?
    - What's the gap between product ambition and technical reality?

29. **first-principles** — Re-derive priorities from first principles.
    - Strip away inertia. If starting fresh, what would you prioritize?
    - What constraints have changed?
    - What's the atomic operation that matters most next quarter?

30. **stress-test** — Stress test the proposed roadmap.
    - What breaks at 10x scale?
    - What breaks if a competitor launches X?
    - What breaks if model capabilities jump (or stagnate)?

**Layer 2 — Product Sense:**
31. **problem-ai-fit** — Re-score any new features proposed for next quarter.
    - Run the 0-16 fit score on each proposal
    - Are we AI-washing any proposed features?
    - What would rules/heuristics handle just as well?

32. **failure-modes** — Map failure risks for next quarter's roadmap.
    - What are the top failure modes for proposed work?
    - Which carry the highest consequence magnitude?

### Afternoon: Roadmap Reset

**Layer 1 — Thinking Core:**
33. **determinism-compass** — Classify next quarter's features.
    - Which outputs need deterministic guarantees (pass^k)?
    - Which can be probabilistic (pass@k)?
    - How does this affect architecture and testing strategy?

**Layer 3 — Craft:**
34. **prompt-as-product** — Review prompt architecture health.
    - Are prompts versioned and regression-tested?
    - Any prompt degradation detected?
    - Prompt-eval-deploy pipeline running smoothly?

35. **ship-decision** — Apply ship criteria to any features in flight.
    - Are eval gates met for features approaching launch?
    - Any features that should be killed or delayed?
    - Apply eval-gated deployment criteria.

### Close of Day
- **Output:** Updated quarterly roadmap; strategic decisions documented; skill coverage verified

---

## Skill Coverage Matrix

| Plugin | Skills Used | Step |
|--------|------------|------|
| **thinking-core** (7/7) | first-principles, bias-spotter, red-team, dual-lens, determinism-compass, stress-test, failure-design* | 1,6 |
| **product-sense** (7/7) | problem-ai-fit, failure-modes, invisible-stack, feedback-flywheel, uncertainty-research, ai-ux-patterns, ai-product-taste | 2,3,5,6 |
| **ai-strategy** (5/5) | strategy-canvas, moat-finder, build-or-buy, token-economics, capability-tracking | 1,2,3,4 |
| **safety-and-trust** (3/3) | safety-as-moat, trust-ladder, safety-by-design | 5 |
| **agent-design** (5/5) | autonomy-spectrum, agent-ecosystem, tool-architecture, multi-modal-product-design, agent-harness | 3 |
| **eval-and-quality** (4/4) | eval-framework, eval-driven-development, ai-product-metrics, production-observability | 4 |
| **craft** (8/8) | ai-prd*, context-spec*, agent-spec*, cost-model, ship-decision, competitive-map, fit-signal, prompt-as-product | 2,4,5,6 |

*failure-design used implicitly in stress-test; ai-prd/context-spec/agent-spec reviewed if existing specs need updating

**Total: 35-39/39 skills referenced** (agent-design skills conditional on having agent features; all others always used)

---

## Deliverables

By end of review, you'll have:

1. **Volatility Audit** — Assumptions rated Green/Yellow/Red; capability half-life updated
2. **Moat Assessment** — Health check with erosion analysis and strengthening options
3. **Competitive Map** — Updated landscape with threat/opportunity assessment
4. **Build-or-Buy Update** — Confirmed or revised; architecture health assessed
5. **Economics Review** — Updated unit economics with cost levers; harness economics validated
6. **Eval Health Check** — Framework health; criteria drift addressed; metrics trends documented
7. **PMF Status** — Segment-by-segment analysis with feedback flywheel review
8. **Safety Posture** — Constitutional principles reviewed; trust health documented
9. **Updated Roadmap** — Next quarter priorities with skill coverage, success metrics, and strategic decisions

---

## Red Flags That Require Immediate Action

- **Moat erosion detected:** New competitor or model eliminates your advantage
- **Unit economics broken:** Cost has shifted such that profitability path is unclear
- **PMF degrading:** Key retention or growth signals weakening across segments
- **Eval saturation:** High pass rates masking real quality issues; criteria drift undetected
- **Safety incident:** Production failure that signals design gap or constitutional violation
- **Regulatory shift:** New guidelines requiring capability or transparency changes
- **Capability jump:** Major model release that changes build-or-buy economics
- **Trust collapse:** User trust metrics dropping; correction rates spiking

If any red flag is identified, schedule an emergency strategy session before relying on quarterly cadence.

---

## Facilitation Notes

1. **Data over intuition:** Use actual metrics, customer feedback, and competitive intelligence
2. **Invite skepticism:** Assign someone to argue against each assumption (use red-team skill)
3. **Document dissent:** Capture both views and reasoning when team disagrees
4. **Get technical depth:** Include engineers in build-or-buy, cost model, and eval discussions
5. **User voice:** Include customer insights and trust metrics, not just internal opinions
6. **Score, don't just discuss:** Use scoring frameworks (fit score, autonomy levels, capability half-life)
7. **One clear decision owner:** Decisions are made by end of review, not debated indefinitely

---

## Connecting to Product Cycles

- **Q1 Review + New Feature Decisions** → Enter **new-ai-feature** workflow (all 39 skills) for major projects
- **Q2 Review + Competitive Threat** → May trigger **ai-discovery-sprint** on adjacent problems
- **Q3 Review + PMF Concerns** → User research sprint; deep feedback-flywheel and fit-signal analysis
- **Q4 Review + Planning** → Input to annual strategy refresh; capability-tracking drives next year roadmap
- **Emergency Review (any quarter)** → Triggered by red flags; compressed to 2-3 days with focused skill subset

This quarterly review keeps your strategy synchronized with rapid changes in AI capabilities, markets, competition, and evaluation standards.

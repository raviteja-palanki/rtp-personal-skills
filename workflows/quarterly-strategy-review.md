# Quarterly strategy review
**Refresh strategy with evolving AI landscape**

A structured quarterly workflow for product strategy review, especially critical in AI where model capabilities, competitive landscape, and token economics shift rapidly. Orchestrates skills from all 7 plugins to ensure no strategic blind spots.

**Timeline:** 5 days (one step per day)
**Frequency:** Every quarter (or when major model releases happen)
**Audience:** Product leaders, strategy leads, engineering heads, AI specialists
**Output:** Updated strategy document; identified moat erosion; rtp-build-or-buy reassessment; eval health check; adjusted roadmap for next quarter
**Skills used:** the strategy subset, named in the sequence below. The agent-design skills come in only when agent features are in scope.

---

## Context and why this matters

AI moves fast. A moat built on proprietary data erodes if a new model makes your data less valuable. Cost structure assumptions break if token pricing drops 40%. Build-or-buy decisions flip if new APIs become available. Eval frameworks degrade if criteria drift isn't detected. This quarterly review keeps your strategy synchronized with reality.

---

## Step 1: volatile assumptions check (Day 1)

**Goal:** Identify assumptions that have aged poorly and need re-evaluation.

### Morning: strategy canvas reassessment

**Layer 2 — AI Strategy:**
1. **rtp-strategy-canvas** — Run a quarterly check on your strategy canvas.
   - What was your competitive hypothesis at the start of the quarter?
   - Is the landscape still accurate? Have competitors moved?
   - Have new models/APIs changed what's feasible?
   - What capability-conditional roadmap items have triggered or expired?
   - What trade-offs are you making? Do they still make sense?

2. **rtp-capability-tracking** — Assess strategy half-life.
   - Which capabilities have been commoditized since last quarter?
   - Which new capabilities have emerged?
   - Track benchmark trajectories: MMLU, HumanEval, SWE-bench, GPQA
   - Has your strategy half-life shortened or lengthened?

### Afternoon: assumption volatility audit

**Layer 1 — Thinking Core:**
3. **rtp-stress-test** — Test each assumption against current evidence.
   - List all strategic assumptions from last quarter
   - For each: what would disprove it? Has that evidence appeared?
   - Run pre-mortem: "It's end of next quarter and our strategy failed — why?"

4. **rtp-bias-spotter** — Check for decision biases in the team.
   - Are we anchored on last quarter's strategy?
   - Are we suffering from sunk-cost fallacy on current bets?
   - Is there survivorship bias in our competitive analysis?

### Close of Day
- **Output:** Volatility audit completed; assumptions rated Green/Yellow/Red; capability half-life updated

---

## Step 2: moat and competitive health check (Day 2)

**Goal:** Assess whether your competitive advantage still exists and is defensible.

### Morning: moat analysis

**Layer 2 — AI Strategy:**
5. **rtp-moat-finder** — Run moat analysis focused on erosion.
   - What was your original moat? (data flywheel, workflow lock-in, context depth, earned trust)
   - Has it eroded? How? How quickly?
   - Are competitors closing the gap?
   - Can you strengthen the moat? Or should you shift defensibility?

**Layer 3 — Craft:**
6. **rtp-competitive-map** — Update your competitive landscape.
   - Who are your direct competitors today? Has the list changed?
   - New entrants or incumbents moving into your space?
   - For each competitor: moat, positioning, go-to-market
   - Where do you win? Where do they win?

### Afternoon: product sense check

**Layer 2 — Product Sense:**
7. **rtp-ai-product-taste** — Run taste calibration on your current product.
   - Does your product still feel "museum quality" or has it stagnated?
   - Apply domain-specific taste criteria: has the bar moved?
   - What would a world-class AI PM critique today?

8. **rtp-ai-ux-patterns** — Review UX against evolving best practices.
   - Are your confidence displays still calibrated correctly?
   - Have user expectations evolved? (users now expect more from AI)
   - Are there new AI UX patterns competitors are using that you aren't?

### Close of Day
- **Output:** Moat health assessment; competitive map updated; taste and UX gaps identified

---

## Step 3: rtp-build-or-buy and architecture reassessment (Day 2-3)

**Goal:** Re-evaluate whether you should still build this capability in-house.

### Morning: rtp-build-or-buy update

**Layer 2 — AI Strategy:**
9. **rtp-build-or-buy** — Re-run rtp-build-or-buy with current model capabilities.
   - Has the Build-or-Buy Trilemma shifted? (prompt vs RAG vs fine-tune vs API)
   - Are there new APIs, partnerships, or vendors to consider?
   - Has the model-agnostic abstraction layer strategy held?
   - What's the cost-benefit today vs. 3 months ago?

**Layer 2 — Product Sense:**
10. **rtp-invisible-stack** — Reassess the hidden architecture.
    - Has retrieval performance degraded or improved?
    - Are post-processing and validation costs where you expected?
    - Has infrastructure cost changed with new model pricing?

### Afternoon: agent and tool architecture review

**Layer 2 — Agent Design (if applicable):**
11. **rtp-agent-ecosystem** — Review agent orchestration health.
    - Are agent patterns (sequential, parallel, hierarchical) still optimal?
    - Has harness architecture (Planner→Generator→Evaluator) performed as designed?
    - Any new agent failure patterns emerged?

12. **rtp-tool-architecture** — Review tool access and MCP ecosystem.
    - Are tool permissions still appropriate? Permission inflation check.
    - Any new MCP connectors that could improve capabilities?
    - Are rate limits and escape hatches still calibrated?

13. **rtp-agent-harness** *(if harness in production)* — Review harness performance.
    - Are sprint contracts still effective? Criteria drift?
    - Context management: has Pre-Rot Threshold shifted?
    - Generator quality: is pass rate improving or stagnating?

14. **rtp-autonomy-spectrum** — Review autonomy levels.
    - Should any features move up or down the autonomy spectrum?
    - Are context anxiety thresholds still appropriate?
    - Has user trust earned higher autonomy for any features?

15. **rtp-multi-modal-product-design** *(if multi-modal)* — Review modality performance.
    - Are cross-modal interactions working as designed?
    - New modalities available that should be integrated?

### Close of Day
- **Output:** Updated rtp-build-or-buy decision; architecture health assessed; agent patterns reviewed

---

## Step 4: economics and evaluation review (Day 3-4)

**Goal:** Validate unit economics and evaluation framework health.

### Morning: economics update

**Layer 2 — AI Strategy:**
16. **rtp-token-economics** — Re-run token cost model with current pricing.
    - Have model prices changed? (usually downward)
    - Have usage patterns changed? (context window growth, query complexity)
    - Are cached prompt economics being fully leveraged? (90% discount)
    - Is model routing ROI where expected?

**Layer 3 — Craft:**
17. **rtp-cost-model** — Update unit economics.
    - Baseline cost per unit: expected vs. actual
    - Harness economics: are harness costs ($200/task range) justified by quality?
    - New cost levers discovered? (smarter prompting, batching, routing)
    - Path to profitability at current scale

### Afternoon: evaluation health check

**Layer 2 — Eval & Quality:**
18. **rtp-eval-framework** — Review eval framework health.
    - Are eval metrics still aligned with user value?
    - Has eval saturation occurred? (high pass rates with stale test sets)
    - Agent-type-specific evals: still appropriate?
    - Do acceptance thresholds need adjustment?

19. **rtp-eval-driven-development** — Check EDD discipline.
    - Is the team running evals before shipping?
    - Has criteria drift been detected and addressed?
    - Is eval dataset refresh happening on cadence?

20. **rtp-ai-product-metrics** — Review metrics dashboard.
    - pass@k and pass^k trends: improving, flat, or declining?
    - Acceptance rate and correction rate trajectories
    - Eval saturation detection: any alerts triggered?

21. **rtp-production-observability** — Review monitoring health.
    - Are silent degradation signals being caught?
    - Context anxiety detection: working as designed?
    - Sprint contract compliance: tracked and trending?
    - Drift detection: any unexpected distribution shifts?

### Close of Day
- **Output:** Updated cost model; eval framework health assessed; metrics trends documented; observability gaps identified

---

## Step 5: PMF and safety posture (Day 4)

**Goal:** Confirm product-market fit is holding and safety practices have evolved.

### Morning: PMF health check

**Layer 3 — Craft:**
22. **rtp-fit-signal** — Re-evaluate product-market fit signals.
    - What signals said you had PMF last quarter? Do they still hold?
    - New signals emerged? (churn, feature stagnation, complaints)
    - Segment-by-segment: where is PMF strong vs. weak?
    - If PMF is degrading, is it competitive, product, or market shift?

**Layer 2 — Product Sense:**
23. **rtp-feedback-flywheel** — Review the learning loop.
    - Is the flywheel spinning? (signals → improvements → better signals)
    - What's the latency between observing a problem and fixing it?
    - Is the team avoiding local optima?

24. **rtp-uncertainty-research** — Reassess current unknowns.
    - What new uncertainties have emerged since last quarter?
    - Which previous uncertainties have been resolved?
    - What research is needed for next quarter?

### Afternoon: safety posture

**Layer 2 — Safety & Trust:**
25. **rtp-safety-as-moat** — Review safety position.
    - Have regulatory expectations changed?
    - New failure modes discovered in production?
    - Is safety building competitive advantage or just avoiding damage?
    - Are there new safety risks from new model capabilities?

26. **rtp-safety-by-design** — Review constitutional principles.
    - Are the 5-10 behavioral rules still comprehensive?
    - Any new adversarial patterns that need defense?
    - Multi-agent safety boundaries: still holding?

27. **rtp-trust-ladder** — Review trust health.
    - Has user trust improved, held, or eroded?
    - Are trust repair mechanisms working when AI fails?
    - Should calibrated confidence displays be adjusted?
    - Any trust-autonomy calibration changes needed?

### Close of Day
- **Output:** PMF assessment by segment; safety posture reviewed; trust health documented

---

## Step 6: synthesis and roadmap adjustment (Day 5)

**Goal:** Synthesize all findings into updated quarterly priorities.

### Morning: pattern recognition and synthesis

**Layer 1 — Thinking Core:**
28. **rtp-dual-lens** — Synthesize product and technical findings.
    - What themes emerge? (moat erosion, cost opportunities, PMF risk, eval gaps, safety needs)
    - Where is the biggest leverage?
    - What's the gap between product ambition and technical reality?

29. **rtp-first-principles** — Re-derive priorities from first principles.
    - Strip away inertia. If starting fresh, what would you prioritize?
    - What constraints have changed?
    - What's the atomic operation that matters most next quarter?

30. **rtp-stress-test** — Stress test the proposed roadmap.
    - What breaks at 10x scale?
    - What breaks if a competitor launches X?
    - What breaks if model capabilities jump (or stagnate)?

**Layer 2 — Product Sense:**
31. **rtp-problem-ai-fit** — Re-score any new features proposed for next quarter.
    - Run the 0-16 fit score on each proposal
    - Are we AI-washing any proposed features?
    - What would rules/heuristics handle just as well?

32. **rtp-failure-modes** — Map failure risks for next quarter's roadmap.
    - What are the top failure modes for proposed work?
    - Which carry the highest consequence magnitude?

### Afternoon: roadmap reset

**Layer 1 — Thinking Core:**
33. **rtp-determinism-compass** — Classify next quarter's features.
    - Which outputs need deterministic guarantees (pass^k)?
    - Which can be probabilistic (pass@k)?
    - How does this affect architecture and testing strategy?

**Layer 3 — Craft:**
34. **rtp-prompt-as-product** — Review prompt architecture health.
    - Are prompts versioned and regression-tested?
    - Any prompt degradation detected?
    - Prompt-eval-deploy pipeline running smoothly?

35. **rtp-ship-decision** — Apply ship criteria to any features in flight.
    - Are eval gates met for features approaching launch?
    - Any features that should be killed or delayed?
    - Apply eval-gated deployment criteria.

### Close of Day
- **Output:** Updated quarterly roadmap; strategic decisions documented; skill coverage verified

---

## Skill coverage matrix

| Plugin | Skills Used | Step |
|--------|------------|------|
| **thinking-core** | rtp-first-principles, rtp-bias-spotter, rtp-stress-test, rtp-dual-lens, rtp-determinism-compass, rtp-failure-modes* | 1,6 |
| **product-sense** | rtp-problem-ai-fit, rtp-failure-modes, rtp-invisible-stack, rtp-feedback-flywheel, rtp-uncertainty-research, rtp-ai-ux-patterns, rtp-ai-product-taste | 2,3,5,6 |
| **ai-strategy** | rtp-strategy-canvas, rtp-moat-finder, rtp-build-or-buy, rtp-token-economics, rtp-capability-tracking | 1,2,3,4 |
| **safety-and-trust** | rtp-safety-as-moat, rtp-trust-ladder, rtp-safety-by-design | 5 |
| **agent-design** | rtp-autonomy-spectrum, rtp-agent-ecosystem, rtp-tool-architecture, rtp-multi-modal-product-design, rtp-agent-harness | 3 |
| **eval-and-quality** | rtp-eval-framework, rtp-eval-driven-development, rtp-ai-product-metrics, rtp-production-observability | 4 |
| **craft** | rtp-ai-prd*, rtp-context-spec*, rtp-agent-spec*, rtp-cost-model, rtp-ship-decision, rtp-competitive-map, rtp-fit-signal, rtp-prompt-as-product | 2,4,5,6 |

*rtp-failure-modes used implicitly in rtp-stress-test; rtp-ai-prd/context-spec/agent-spec reviewed if existing specs need updating

**The skills this sequence uses are named above.** The agent-design ones are conditional on having agent features; the rest apply every quarter.

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

## Red flags that require immediate action

- **Moat erosion detected:** New competitor or model eliminates your advantage
- **Unit economics broken:** Cost has shifted such that profitability path is unclear
- **PMF degrading:** Key retention or growth signals weakening across segments
- **Eval saturation:** High pass rates masking real quality issues; criteria drift undetected
- **Safety incident:** Production failure that signals design gap or constitutional violation
- **Regulatory shift:** New guidelines requiring capability or transparency changes
- **Capability jump:** Major model release that changes rtp-build-or-buy economics
- **Trust collapse:** User trust metrics dropping; correction rates spiking

If any red flag is identified, schedule an emergency strategy session before relying on quarterly cadence.

---

## Facilitation notes

1. **Data over intuition:** Use actual metrics, customer feedback, and competitive intelligence
2. **Invite skepticism:** Assign someone to argue against each assumption (use rtp-stress-test skill)
3. **Document dissent:** Capture both views and reasoning when team disagrees
4. **Get technical depth:** Include engineers in rtp-build-or-buy, cost model, and eval discussions
5. **User voice:** Include customer insights and trust metrics, not just internal opinions
6. **Score, don't just discuss:** Use scoring frameworks (fit score, autonomy levels, capability half-life)
7. **One clear decision owner:** Decisions are made by end of review, not debated indefinitely

---

## Where the review leads next

A review is worth running only if something follows from it. What follows usually depends on what the quarter surfaced.

| What the review found | What to run next |
|---|---|
| New features worth committing to | The `new-ai-feature` workflow, for each project large enough to justify the full cycle |
| A competitive threat | An `ai-discovery-sprint` on the adjacent problem |
| Doubt about product and market fit | A user research sprint, going deep on `rtp-feedback-flywheel` and `rtp-fit-signal` |
| Planning season | Input to the annual refresh, with `rtp-capability-tracking` shaping next year's roadmap |
| Red flags mid-quarter | A compressed review, two or three days on the subset of skills the flags point at |

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.

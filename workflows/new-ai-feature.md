# New AI Feature: Full Cycle Workflow
**Discovery → Strategy → Spec → Launch**

A complete workflow for taking a new AI feature from initial concept through production launch. Orchestrates all 39 skills across the 7-plugin system to ensure no blind spots.

**Timeline:** 12 days (can compress to 6 or expand to 4 weeks based on complexity)
**Audience:** Product managers, design leads, engineering leads, AI specialists
**Output:** Fully specified, risk-vetted, economically defensible AI feature ready for launch
**Skill Coverage:** All 39 skills across thinking-core, product-sense, ai-strategy, safety-and-trust, agent-design, eval-and-quality, craft

---

## Phase 1: Discovery (Days 1-2)

**Objective:** Understand the problem space deeply, test AI-solution fit, and surface key uncertainties.

### Day 1: Problem Space

**Layer 1 — Thinking Core:**
1. **first-principles** — Deconstruct the problem to first principles. What is the core user need? What constraints are immovable? Classify the atomic operation (LOOKUP, TRANSFORM, CLASSIFY, GENERATE).
2. **bias-spotter** — Run a bias audit on the initial framing. Are we anchored on a solution? Are we conflating "AI can do this" with "AI should do this"? Check for Maslow's Hammer, survivorship bias, and sunk-cost reasoning.

**Layer 2 — Product Sense:**
3. **problem-ai-fit** — Score AI fit (0-16 on four dimensions). Run the lookup table test. Would rules, heuristics, or search solve 80%? Where does AI add irreplaceable value?
4. **ai-product-taste** — Apply domain-specific taste criteria. Is this feature "museum quality" or just functional? What would a world-class AI PM critique about this concept?

### Day 2: Uncertainty & Fit

**Layer 2 — Product Sense:**
5. **uncertainty-research** — Map the 5 largest sources of uncertainty. Rank by impact × confidence. Design rapid tests for the highest-impact unknowns.
6. **failure-modes** — Map the failure surface. What are the top 10 ways this AI feature will fail? Classify by hallucination type (fabrication, drift, attribution, omission, confidence, cascade).

**Layer 3 — Craft:**
7. **fit-signal** — Assess early product-market fit signals. Run the "40% very disappointed" test. Is there customer demand? What would make them choose the AI version?

**Gate:** Do we have clarity on the core problem, proof that AI is the right approach, and a mapped failure landscape? Do we understand customer willingness to adopt an AI solution?

---

## Phase 2: Strategy (Days 3-4)

**Objective:** Position the feature strategically, identify competitive advantages, and decide build vs. partner vs. buy.

### Day 3: Strategic Canvas & Competitive Position

**Layer 2 — AI Strategy:**
8. **strategy-canvas** — Map the feature against customer needs, competitive landscape, and business objectives. Build capability-conditional roadmaps. What trade-offs are we making?
9. **capability-tracking** — Assess model capability half-life. Which capabilities are we betting on? How long until commoditization? Track benchmark trajectories (MMLU, HumanEval, SWE-bench).

**Layer 3 — Craft:**
10. **competitive-map** — Map the competitive landscape. Who are direct competitors? Where do we win? Where do they win? What's the switching cost?

### Day 4: Moat & Build-or-Buy

**Layer 2 — AI Strategy:**
11. **moat-finder** — Identify where defensibility lives. Is it in data flywheel, workflow lock-in, context depth, or earned trust? What moat can we build with this feature?
12. **build-or-buy** — Run the Build-or-Buy Trilemma (prompt vs RAG vs fine-tune vs API). Model build cost, time, and risk against off-the-shelf. Include model-agnostic abstraction layer considerations.

**Gate:** Do we have strategic clarity on why this feature matters and how we'll defend it? Have we made an informed build-or-buy decision with capability half-life factored in?

---

## Phase 3: Specification (Days 5-8)

**Objective:** Fully specify the feature — requirements, context, evaluation, agent architecture, cost structure, and technical design.

### Day 5: Product Requirements & Context

**Layer 3 — Craft:**
13. **ai-prd** — Write a complete AI PRD with probabilistic specs, eval criteria as acceptance criteria, dual success metrics (deterministic + probabilistic), and prompt specifications. Include failure budgets, not just success criteria.
14. **context-spec** — Define the context architecture. What information must be available? Map retrieval patterns, context window budgets, and the CONTEXT stack (Collection, Organization, Navigation, Transformation, Evaluation, eXecution, Tracking).

**Layer 2 — Product Sense:**
15. **invisible-stack** — Map the hidden architecture: retrieval layer, post-processing, validation, monitoring. Surface the 60-80% of engineering work that users never see.

### Day 6: Evaluation Framework

**Layer 2 — Eval & Quality:**
16. **eval-framework** — Build the evaluation framework. Define metrics, test sets, acceptance thresholds. Include agent-type-specific evals (pass@k for assistive, pass^k for autonomous). Address eval saturation.
17. **eval-driven-development** — Establish the EDD cycle: define evals → build feature → measure → iterate. Design for criteria drift (Shankar). Plan eval dataset refresh cadence.
18. **ai-product-metrics** — Define the metrics dashboard. Map pass@k, pass^k, acceptance rate, correction rate, time-to-value. Set up eval saturation detection.

### Day 7: Agent & Architecture Design

**Layer 2 — Agent Design:**
19. **agent-spec** *(if agent/multi-step)* — Specify the agent architecture using the boundary matrix: autonomy levels (0-4) per step, trust thresholds, handoff protocols, failure recovery, state snapshots. Include sprint contracts and file-based communication patterns.
20. **autonomy-spectrum** — Map where on the autonomy spectrum this feature sits. Define context anxiety thresholds. Design progressive autonomy based on trust signals.
21. **agent-ecosystem** *(if multi-agent)* — Design orchestration patterns (sequential, parallel, hierarchical). Define inter-agent communication, error boundaries, and harness architecture.
22. **tool-architecture** *(if tool-using)* — Design tool access with MCP/A2A patterns. Classify tools by mutation type. Define permission scopes, rate limits, approval gates, and escape hatches.
23. **agent-harness** *(if complex agent)* — Design the Planner→Generator→Evaluator harness. Define sprint contracts, context management (Pre-Rot Threshold at 50-60%), and the four quality dimensions.
24. **multi-modal-product-design** *(if multi-modal)* — Design cross-modal interactions. Map input/output modality combinations. Define modality-specific failure modes.

### Day 8: Cost & Economics

**Layer 2 — AI Strategy:**
25. **token-economics** — Model the token flow. Map input/output patterns, cached prompt economics (90% discount), model routing ROI. Where are the cost surprises?

**Layer 3 — Craft:**
26. **cost-model** — Build a defensible cost model. Include harness economics ($9 solo vs $200 harness), overhead multipliers (1.2-5x), eval cost at scale. Map the path to profitability.

**Layer 3 — Craft:**
27. **prompt-as-product** — Design the prompt architecture. Version prompts like code. Build regression testing framework. Define prompt-eval-deploy pipeline.

**Gate:** Do we have a complete, testable specification? Can engineering build from this? Do we understand cost structure, evaluation criteria, and agent architecture?

---

## Phase 4: Safety & Trust (Days 9-10)

**Objective:** Design safety into the feature, build trust scaffolding, and validate against adversarial scenarios.

### Day 9: Safety Architecture

**Layer 2 — Safety & Trust:**
28. **safety-as-moat** — Position safety as competitive advantage. Quantify the alignment tax. Where does safety build trust with users? Where does safety become a feature?
29. **safety-by-design** — Implement constitutional AI principles (5-10 core behavioral rules). Design defense-in-depth layers. Integrate adversarial eval. Plan multi-agent safety boundaries.

**Layer 1 — Thinking Core:**
30. **failure-design** — Design graceful degradation. What happens when the model is wrong? When context is incomplete? When users provide adversarial input? Build fallback cascades.
31. **stress-test** — Run 6-dimension stress testing: scale, adversarial input, model degradation, context poisoning, cascade failure, economic stress. Test boundary conditions.

### Day 10: Trust & Observability

**Layer 2 — Safety & Trust:**
32. **trust-ladder** — Map the trust journey. Design calibrated confidence displays. Build trust repair mechanisms. Define the trust-autonomy calibration table.

**Layer 2 — Eval & Quality:**
33. **production-observability** — Design the observability stack. Monitor for silent degradation, context anxiety, harness-level metrics, sprint contract compliance. Set up drift detection alerts.

**Layer 1 — Thinking Core:**
34. **determinism-compass** — Final classification: which outputs MUST be deterministic (pass^k) vs. which can be probabilistic (pass@k)? Map determinism requirements to architecture decisions.

**Gate:** Have we designed safety in from the ground up? Do users understand when to trust the feature? Can we detect and respond to failures in production?

---

## Phase 5: Synthesis & Launch (Days 11-12)

**Objective:** Synthesize all inputs, validate assumptions, and make the ship decision.

### Day 11: Synthesis & Validation

**Layer 1 — Thinking Core:**
35. **dual-lens** — Synthesize product and technical perspectives. What did spec and safety phases reveal that changes strategy? What's the gap between "technically feasible" and "commercially viable"?
36. **falsification** — Test your core hypotheses against evidence. What would disprove them? Run pre-mortem: "It's 6 months post-launch and this feature failed — why?"

**Layer 2 — Product Sense:**
37. **feedback-flywheel** — Design the post-launch learning loop. How will signals feed back into model improvement? What's the latency between observing a problem and fixing it?
38. **ai-ux-patterns** — Validate UX patterns against best practices. Are confidence displays calibrated? Are human-AI handoffs smooth? Does the interaction feel natural?

### Day 12: Ship Decision

**Layer 3 — Craft:**
39. **ship-decision** — Synthesize all inputs: strategy, spec, cost, safety, evals, and user testing. Apply eval-gated deployment criteria. Make the final go/no-go decision. Define launch criteria, rollout plan, monitoring triggers, and success metrics.

**Gate:** Is this feature ready to ship? Have all risks been surfaced and mitigated? Do we have a clear rollout and measurement plan with eval gates?

---

## Skill Coverage Matrix

| Plugin | Skills Used | Phase |
|--------|------------|-------|
| **thinking-core** (7/7) | first-principles, bias-spotter, falsification, dual-lens, determinism-compass, stress-test, failure-design | 1,4,5 |
| **product-sense** (7/7) | problem-ai-fit, failure-modes, invisible-stack, feedback-flywheel, uncertainty-research, ai-ux-patterns, ai-product-taste | 1,3,5 |
| **ai-strategy** (5/5) | strategy-canvas, moat-finder, build-or-buy, token-economics, capability-tracking | 2,3 |
| **safety-and-trust** (3/3) | safety-as-moat, trust-ladder, safety-by-design | 4 |
| **agent-design** (5/5) | autonomy-spectrum, agent-ecosystem, tool-architecture, multi-modal-product-design, agent-harness | 3 |
| **eval-and-quality** (4/4) | eval-framework, eval-driven-development, ai-product-metrics, production-observability | 3,4 |
| **craft** (8/8) | ai-prd, context-spec, agent-spec, cost-model, ship-decision, competitive-map, fit-signal, prompt-as-product | 1,2,3,5 |

**Total: 39/39 skills referenced**

---

## Success Criteria

- **Discovery:** Problem-AI fit scored; failure landscape mapped; key uncertainties ranked; bias audit clean
- **Strategy:** Competitive positioning and moat identified; build-or-buy decision with capability half-life; strategy canvas complete
- **Spec:** Complete AI PRD with eval criteria; cost model with harness economics; agent architecture with boundary matrix; prompt versioning established
- **Safety:** Constitutional AI principles defined; trust ladder calibrated; observability stack designed; stress test passed
- **Launch:** Eval-gated deployment criteria met; rollout plan and monitoring triggers documented; feedback flywheel active

---

## Common Pitfalls

1. **Skipping discovery** — Rushing to spec without scoring problem-AI fit or running the lookup table test
2. **Ignoring cost until too late** — Discovering harness economics ($200/task) make the feature unprofitable after launch
3. **Treating safety as afterthought** — Adding safeguards in Phase 5 instead of designing constitutional principles from Day 1
4. **No eval framework** — Building without knowing how you'll measure quality; shipping without pass@k/pass^k targets
5. **No human-AI design** — Forgetting that AI features live in human workflows; failure modes are user experiences
6. **Autonomy creep** — Designing agents at Level 3-4 autonomy without earning trust at Level 1-2 first
7. **Eval drift** — Setting eval criteria once and never updating as criteria drift emerges from production data
8. **Context anxiety ignored** — Not monitoring when agents degrade due to context window saturation

---

## Customization

- **Fast track (6 days):** Compress discovery+strategy (existing product, clear signal); merge safety into spec phase
- **Deep dive (4+ weeks):** Add user research sprints, multiple eval rounds, competitive deep dives, adversarial red-teaming
- **Regulated domains:** Expand safety phase to 4 days; add compliance, audit trails, and constitutional AI documentation
- **Agent-heavy features:** Expand Days 7-8 to full week; deep dive on autonomy-spectrum, agent-ecosystem, tool-architecture, agent-harness
- **Multi-modal features:** Add dedicated day for multi-modal-product-design with cross-modal failure testing
- **Cost-sensitive features:** Add token-economics deep dive with cached prompt optimization and model routing analysis

# New AI feature, full cycle
**Discovery → Strategy → Spec → Launch**

Takes a new AI feature from first concept to production launch. It draws on skills from every layer of the library, which is the point: the failure it is built to prevent is a decision made well in one dimension and never examined in the others.

**Timeline:** 12 days (can compress to 6 or expand to 4 weeks based on complexity)
**Audience:** Product managers, design leads, engineering leads, AI specialists
**Output:** Fully specified, risk-vetted, economically defensible AI feature ready for launch
**Skills used:** every layer. Thinking core, product sense, AI strategy, safety and trust, agent design, eval and quality, and craft.

---

## Phase 1: discovery (days 1-2)

**Objective:** Understand the problem space deeply, test AI-solution fit, and surface key uncertainties.

### Day 1: problem space

**Layer 1 — Thinking Core:**
1. **rtp-first-principles** — Deconstruct the problem to first principles. What is the core user need? What constraints are immovable? Classify the atomic operation (LOOKUP, TRANSFORM, CLASSIFY, GENERATE).
2. **rtp-bias-spotter** — Run a bias audit on the initial framing. Are we anchored on a solution? Are we conflating "AI can do this" with "AI should do this"? Check for Maslow's Hammer, survivorship bias, and sunk-cost reasoning.

**Layer 2 — Product Sense:**
3. **rtp-problem-ai-fit** — Score AI fit (0-16 on four dimensions). Run the lookup table test. Would rules, heuristics, or search solve 80%? Where does AI add irreplaceable value?
4. **rtp-ai-product-taste** — Apply domain-specific taste criteria. Is the feature good, or merely working? What would a demanding senior product leader push back on?

### Day 2: uncertainty and fit

**Layer 2 — Product Sense:**
5. **rtp-uncertainty-research** — Map the 5 largest sources of uncertainty. Rank by impact × confidence. Design rapid tests for the highest-impact unknowns.
6. **rtp-failure-modes** — Map the failure surface. What are the top 10 ways this AI feature will fail? Classify by hallucination type (fabrication, drift, attribution, omission, confidence, cascade).

**Layer 3 — Craft:**
7. **rtp-fit-signal** — Assess early product-market fit signals. Run the "40% very disappointed" test. Is there customer demand? What would make them choose the AI version?

**Gate:** Do we have clarity on the core problem, proof that AI is the right approach, and a mapped failure landscape? Do we understand customer willingness to adopt an AI solution?

---

## Phase 2: strategy (days 3-4)

**Objective:** Position the feature strategically, identify competitive advantages, and decide build vs. partner vs. buy.

### Day 3: strategic canvas and competitive position

**Layer 2 — AI Strategy:**
8. **rtp-strategy-canvas** — Map the feature against customer needs, competitive landscape, and business objectives. Build capability-conditional roadmaps. What trade-offs are we making?
9. **rtp-capability-tracking** — Assess model capability half-life. Which capabilities are we betting on? How long until commoditization? Track benchmark trajectories (MMLU, HumanEval, SWE-bench).

**Layer 3 — Craft:**
10. **rtp-competitive-map** — Map the competitive landscape. Who are direct competitors? Where do we win? Where do they win? What's the switching cost?

### Day 4: moat and rtp-build-or-buy

**Layer 2 — AI Strategy:**
11. **rtp-moat-finder** — Identify where defensibility lives. Is it in data flywheel, workflow lock-in, context depth, or earned trust? What moat can we build with this feature?
12. **rtp-build-or-buy** — Run the Build-or-Buy Trilemma (prompt vs RAG vs fine-tune vs API). Model build cost, time, and risk against off-the-shelf. Include model-agnostic abstraction layer considerations.

**Gate:** Do we have strategic clarity on why this feature matters and how we'll defend it? Have we made an informed rtp-build-or-buy decision with capability half-life factored in?

---

## Phase 3: specification (days 5-8)

**Objective:** Fully specify the feature — requirements, context, evaluation, agent architecture, cost structure, and technical design.

### Day 5: product requirements and context

**Layer 3 — Craft:**
13. **rtp-ai-prd** — Write a complete AI PRD with probabilistic specs, eval criteria as acceptance criteria, dual success metrics (deterministic + probabilistic), and prompt specifications. Include failure budgets, not just success criteria.
14. **rtp-context-spec** — Define the context architecture. What information must be available? Map retrieval patterns, context window budgets, and the CONTEXT stack (Collection, Organization, Navigation, Transformation, Evaluation, eXecution, Tracking).

**Layer 2 — Product Sense:**
15. **rtp-invisible-stack** — Map the hidden architecture: retrieval layer, post-processing, validation, monitoring. Surface the 60-80% of engineering work that users never see.

### Day 6: evaluation framework

**Layer 2 — Eval & Quality:**
16. **rtp-eval-framework** — Build the evaluation framework. Define metrics, test sets, acceptance thresholds. Include agent-type-specific evals (pass@k for assistive, pass^k for autonomous). Address eval saturation.
17. **rtp-eval-driven-development** — Establish the EDD cycle: define evals → build feature → measure → iterate. Design for criteria drift (Shankar). Plan eval dataset refresh cadence.
18. **rtp-ai-product-metrics** — Define the metrics dashboard. Map pass@k, pass^k, acceptance rate, correction rate, time-to-value. Set up eval saturation detection.

### Day 7: agent and architecture design

**Layer 2 — Agent Design:**
19. **rtp-agent-spec** *(if agent/multi-step)* — Specify the agent architecture using the boundary matrix: autonomy levels (0-4) per step, trust thresholds, handoff protocols, failure recovery, state snapshots. Include sprint contracts and file-based communication patterns.
20. **rtp-autonomy-spectrum** — Map where on the autonomy spectrum this feature sits. Define context anxiety thresholds. Design progressive autonomy based on trust signals.
21. **rtp-agent-ecosystem** *(if multi-agent)* — Design orchestration patterns (sequential, parallel, hierarchical). Define inter-agent communication, error boundaries, and harness architecture.
22. **rtp-tool-architecture** *(if tool-using)* — Design tool access with MCP/A2A patterns. Classify tools by mutation type. Define permission scopes, rate limits, approval gates, and escape hatches.
23. **rtp-agent-harness** *(if complex agent)* — Design the Planner→Generator→Evaluator harness. Define sprint contracts, context management (Pre-Rot Threshold at 50-60%), and the four quality dimensions.
24. **rtp-multi-modal-product-design** *(if multi-modal)* — Design cross-modal interactions. Map input/output modality combinations. Define modality-specific failure modes.

### Day 8: cost and economics

**Layer 2 — AI Strategy:**
25. **rtp-token-economics** — Model the token flow. Map input/output patterns, cached prompt economics (90% discount), model routing ROI. Where are the cost surprises?

**Layer 3 — Craft:**
26. **rtp-cost-model** — Build a defensible cost model. Include harness economics ($9 solo vs $200 harness), overhead multipliers (1.2-5x), eval cost at scale. Map the path to profitability.

**Layer 3 — Craft:**
27. **rtp-prompt-as-product** — Design the prompt architecture. Version prompts like code. Build regression testing framework. Define prompt-eval-deploy pipeline.

**Gate:** Do we have a complete, testable specification? Can engineering build from this? Do we understand cost structure, evaluation criteria, and agent architecture?

---

## Phase 4: safety and trust (days 9-10)

**Objective:** Design safety into the feature, build trust scaffolding, and validate against adversarial scenarios.

### Day 9: safety architecture

**Layer 2 — Safety & Trust:**
28. **rtp-safety-as-moat** — Position safety as competitive advantage. Quantify the alignment tax. Where does safety build trust with users? Where does safety become a feature?
29. **rtp-safety-by-design** — Implement constitutional AI principles (5-10 core behavioral rules). Design defense-in-depth layers. Integrate adversarial eval. Plan multi-agent safety boundaries.

**Layer 1 — Thinking Core:**
30. **rtp-failure-modes** — Design graceful degradation. What happens when the model is wrong? When context is incomplete? When users provide adversarial input? Build fallback cascades.
31. **rtp-stress-test** — Run 6-dimension stress testing: scale, adversarial input, model degradation, context poisoning, cascade failure, economic stress. Test boundary conditions.

### Day 10: trust and observability

**Layer 2 — Safety & Trust:**
32. **rtp-trust-ladder** — Map the trust journey. Design calibrated confidence displays. Build trust repair mechanisms. Define the trust-autonomy calibration table.

**Layer 2 — Eval & Quality:**
33. **rtp-production-observability** — Design the observability stack. Monitor for silent degradation, context anxiety, harness-level metrics, sprint contract compliance. Set up drift detection alerts.

**Layer 1 — Thinking Core:**
34. **rtp-determinism-compass** — Final classification: which outputs have to be deterministic, measured with pass^k, and which can be probabilistic, measured with pass@k? Map determinism requirements to architecture decisions.

**Gate:** Have we designed safety in from the ground up? Do users understand when to trust the feature? Can we detect and respond to failures in production?

---

## Phase 5: synthesis and launch (days 11-12)

**Objective:** Synthesize all inputs, validate assumptions, and make the ship decision.

### Day 11: synthesis and validation

**Layer 1 — Thinking Core:**
35. **rtp-dual-lens** — Synthesize product and technical perspectives. What did spec and safety phases reveal that changes strategy? What's the gap between "technically feasible" and "commercially viable"?
36. **rtp-stress-test** — Test your core hypotheses against evidence. What would disprove them? Run pre-mortem: "It's 6 months post-launch and this feature failed — why?"

**Layer 2 — Product Sense:**
37. **rtp-feedback-flywheel** — Design the post-launch learning loop. How will signals feed back into model improvement? What's the latency between observing a problem and fixing it?
38. **rtp-ai-ux-patterns** — Validate UX patterns against best practices. Are confidence displays calibrated? Are human-AI handoffs smooth? Does the interaction feel natural?

### Day 12: ship decision

**Layer 3 — Craft:**
39. **rtp-ship-decision** — Synthesize all inputs: strategy, spec, cost, safety, evals, and user testing. Apply eval-gated deployment criteria. Make the final go/no-go decision. Define launch criteria, rollout plan, monitoring triggers, and success metrics.

**Gate:** Is this feature ready to ship? Have all risks been surfaced and mitigated? Do we have a clear rollout and measurement plan with eval gates?

---

## Skill coverage matrix

| Plugin | Skills Used | Phase |
|--------|------------|-------|
| **thinking-core** | rtp-first-principles, rtp-bias-spotter, rtp-stress-test, rtp-dual-lens, rtp-determinism-compass, rtp-failure-modes | 1,4,5 |
| **product-sense** | rtp-problem-ai-fit, rtp-failure-modes, rtp-invisible-stack, rtp-feedback-flywheel, rtp-uncertainty-research, rtp-ai-ux-patterns, rtp-ai-product-taste | 1,3,5 |
| **ai-strategy** | rtp-strategy-canvas, rtp-moat-finder, rtp-build-or-buy, rtp-token-economics, rtp-capability-tracking | 2,3 |
| **safety-and-trust** | rtp-safety-as-moat, rtp-trust-ladder, rtp-safety-by-design | 4 |
| **agent-design** | rtp-autonomy-spectrum, rtp-agent-ecosystem, rtp-tool-architecture, rtp-multi-modal-product-design, rtp-agent-harness | 3 |
| **eval-and-quality** | rtp-eval-framework, rtp-eval-driven-development, rtp-ai-product-metrics, rtp-production-observability | 3,4 |
| **craft** | rtp-ai-prd, rtp-context-spec, rtp-agent-spec, rtp-cost-model, rtp-ship-decision, rtp-competitive-map, rtp-fit-signal, rtp-prompt-as-product | 1,2,3,5 |

**The skills this sequence uses are named above**, across all seven layers.

---

## Success criteria

- **Discovery:** Problem-AI fit scored; failure landscape mapped; key uncertainties ranked; bias audit clean
- **Strategy:** Competitive positioning and moat identified; rtp-build-or-buy decision with capability half-life; strategy canvas complete
- **Spec:** Complete AI PRD with eval criteria; cost model with harness economics; agent architecture with boundary matrix; prompt versioning established
- **Safety:** Constitutional AI principles defined; trust ladder calibrated; observability stack designed; stress test passed
- **Launch:** Eval-gated deployment criteria met; rollout plan and monitoring triggers documented; feedback flywheel active

---

## Common pitfalls

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
- **Agent-heavy features:** Expand Days 7-8 to full week; deep dive on rtp-autonomy-spectrum, rtp-agent-ecosystem, rtp-tool-architecture, rtp-agent-harness
- **Multi-modal features:** Add dedicated day for rtp-multi-modal-product-design with cross-modal failure testing
- **Cost-sensitive features:** Add rtp-token-economics deep dive with cached prompt optimization and model routing analysis

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.

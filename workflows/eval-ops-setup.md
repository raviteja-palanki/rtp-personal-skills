# Eval Ops Setup: Building Your Evaluation Infrastructure
**From zero evals to production-grade quality gates**

A structured workflow for teams building AI evaluation infrastructure from scratch — or upgrading ad-hoc testing to systematic eval-driven development. The most common gap in AI product teams: they ship without knowing how to measure quality.

**Timeline:** 5 days (can compress to 3 for experienced teams)
**Audience:** Product managers, ML engineers, QA leads, data scientists
**Trigger:** New AI feature approaching first release; existing feature with no eval infrastructure; team wants to adopt eval-driven development
**Output:** Complete eval framework, metrics dashboard, observability stack, and EDD process ready for production

---

## Day 1: Eval Foundations

**Goal:** Understand what you're measuring and why. Define the eval strategy before building infrastructure.

### Morning: First Principles of Evaluation

**Layer 1 — Thinking Core:**
1. **first-principles** — Decompose the quality problem.
   - What does "good" mean for this feature? (accuracy, relevance, safety, speed, cost)
   - What's the atomic unit of quality? (single response, full conversation, task completion)
   - Who judges quality? (user, domain expert, LLM-as-judge, automated test)

2. **determinism-compass** — Classify outputs by determinism requirement.
   - Which outputs MUST be correct every time? → pass^k (all k attempts succeed)
   - Which outputs need at least one good result? → pass@k (at least 1 of k is good)
   - Which outputs are subjective? → Human or LLM-as-judge evaluation
   - How does this classification drive your eval architecture?

### Afternoon: Eval Framework Design

**Layer 2 — Eval & Quality:**
3. **eval-framework** — Design the complete evaluation framework.
   - Define metrics for each quality dimension
   - Design test sets: golden datasets, adversarial sets, edge case collections
   - Set acceptance thresholds (start conservative, loosen with data)
   - Choose eval methods: exact match, semantic similarity, LLM-as-judge, human review
   - Address the eval saturation problem: when do you refresh test sets?

4. **eval-driven-development** — Establish the EDD cycle.
   - Define: write evals BEFORE building features
   - Build: implement against eval targets
   - Measure: run evals on every change
   - Iterate: fix failures, add new test cases
   - Plan for criteria drift (Shankar): eval criteria will evolve as you observe outputs
   - Set eval dataset refresh cadence (monthly recommended)

### Close of Day
- **Output:** Eval strategy document; quality dimensions defined; test set plan; EDD process documented

---

## Day 2: Metrics & Observability

**Goal:** Define what you'll measure in production and how you'll detect quality degradation.

### Morning: Metrics Dashboard

**Layer 2 — Eval & Quality:**
5. **ai-product-metrics** — Define the complete metrics stack.
   - Core metrics: pass@k, pass^k, acceptance rate, correction rate, time-to-value
   - Safety metrics: refusal rate, harmful output rate, boundary violations
   - Cost metrics: cost per query, cost per successful outcome, harness overhead
   - Set up eval saturation detection: alert when pass rates plateau
   - Design the metrics dashboard layout

**Layer 2 — Product Sense:**
6. **feedback-flywheel** — Design the signal collection loop.
   - How will user corrections become eval data?
   - Explicit feedback (thumbs up/down, ratings) vs. implicit (edits, retries, abandonment)
   - How fast does feedback reach the eval pipeline?
   - How do you avoid local optima in your eval set?

### Afternoon: Production Observability

**Layer 2 — Eval & Quality:**
7. **production-observability** — Design the monitoring stack.
   - Silent degradation detection: quality drops without errors
   - Context anxiety monitoring: when agents degrade due to context saturation
   - Drift detection: input distribution shifts that break model assumptions
   - Harness-level monitoring: sprint contract compliance, generator pass rates
   - Alert thresholds: warning vs. critical vs. auto-rollback

**Layer 1 — Thinking Core:**
8. **stress-test** — Stress test the eval infrastructure itself.
   - What happens when eval volume scales 10x?
   - What if LLM-as-judge disagrees with human judges?
   - What if eval data gets contaminated?
   - What's the cost of running evals at production scale?

### Close of Day
- **Output:** Metrics dashboard spec; observability stack designed; alert thresholds set; feedback flywheel documented

---

## Day 3: Test Set Construction

**Goal:** Build the actual test sets and evaluation datasets.

### Morning: Golden Dataset

**Layer 2 — Product Sense:**
9. **problem-ai-fit** — Revisit the problem to scope test sets correctly.
   - What input patterns represent 80% of real usage?
   - What edge cases carry the highest consequence magnitude?
   - What failure modes from the failure taxonomy need dedicated test cases?

10. **failure-modes** — Map failures to test cases.
    - For each hallucination type (fabrication, drift, attribution, omission, confidence, cascade): create 5-10 test cases
    - For each failure severity (minor, moderate, critical): set detection thresholds
    - Build adversarial test sets: inputs designed to trigger failures

### Afternoon: Evaluation Pipeline

**Layer 2 — Eval & Quality:**
11. **eval-framework** *(implementation)* — Build the eval pipeline.
    - Automated eval: run on every commit/deploy
    - LLM-as-judge: configure judge prompts, calibrate against human judgments
    - Human eval: define review workflow, sampling strategy, inter-rater reliability
    - Regression tests: capture every production failure as a new test case

**Layer 1 — Thinking Core:**
12. **bias-spotter** — Audit the eval set for bias.
    - Is the golden dataset representative of real usage?
    - Are edge cases over- or under-represented?
    - Does the eval set encode assumptions that might not hold?
    - Are there demographic or domain biases in the test data?

### Close of Day
- **Output:** Golden dataset built; adversarial test set built; eval pipeline configured; bias audit on test data completed

---

## Day 4: Integration & Agent Evals

**Goal:** Integrate evals into the development workflow and handle agent-specific evaluation.

### Morning: Dev Workflow Integration

**Layer 3 — Craft:**
13. **prompt-as-product** — Integrate prompt versioning with evals.
    - Every prompt change triggers eval regression suite
    - Version prompts alongside their eval results
    - Build the prompt-eval-deploy pipeline
    - Decision tables: when to accept prompt changes based on eval delta

14. **ship-decision** — Define eval-gated deployment.
    - What eval scores are required to deploy?
    - What's the rollback trigger? (eval score drops X% in production)
    - How do you handle features that pass evals but fail in production?

### Afternoon: Agent & Multi-Step Evals

**Layer 2 — Agent Design:**
15. **agent-harness** *(if applicable)* — Design harness evaluation.
    - Evaluate Planner quality: are plans feasible and complete?
    - Evaluate Generator quality: pass rate against sprint contracts
    - Evaluate Evaluator quality: does it catch real failures?
    - End-to-end: does the harness produce correct final output?

16. **autonomy-spectrum** — Eval by autonomy level.
    - Level 0-1 (suggest): measure relevance and helpfulness
    - Level 2 (act + report): measure action correctness and undo rate
    - Level 3-4 (autonomous): measure outcome quality and error detection

**Layer 2 — Safety & Trust:**
17. **trust-ladder** — Eval trust calibration.
    - Is confidence display calibrated? (stated confidence vs. actual accuracy)
    - Are trust repair mechanisms triggered at the right thresholds?
    - Are human-AI handoffs happening when they should?

18. **safety-by-design** — Eval safety boundaries.
    - Do constitutional principles hold under adversarial input?
    - Are defense-in-depth layers catching what they should?
    - Safety eval: red-team the feature with adversarial prompts

### Close of Day
- **Output:** Eval-gated deploy pipeline configured; agent evals designed; safety and trust evals operational

---

## Day 5: Launch Readiness & Process

**Goal:** Verify everything works end-to-end and document the ongoing process.

### Morning: End-to-End Validation

**Layer 1 — Thinking Core:**
19. **red-team** — Try to break the eval system.
    - What inputs would pass evals but fail in production?
    - What production scenarios aren't covered by test sets?
    - What would a skeptic say about your eval methodology?

20. **dual-lens** — Validate from both product and technical perspectives.
    - Product: do these metrics actually correlate with user satisfaction?
    - Technical: is the eval pipeline reliable, fast, and cost-effective?
    - Gap analysis: what's missing?

### Afternoon: Documentation & Handoff

**Layer 2 — Product Sense:**
21. **ai-product-taste** — Taste-check the eval setup.
    - Does this feel like a "museum quality" eval system or a checkbox exercise?
    - Would a world-class AI PM be satisfied with this coverage?
    - What would Anthropic's or OpenAI's eval team critique?

**Layer 3 — Craft:**
22. **cost-model** — Model eval costs at scale.
    - What does running evals cost per deploy? Per day? Per month?
    - LLM-as-judge token costs at production eval volume
    - Human eval cost at sampling rate
    - Is the eval budget sustainable?

### Close of Day
- **Output:** Eval system validated end-to-end; process documentation complete; cost model for eval ops established; team trained on EDD

---

## Skill Coverage

| Plugin | Skills Used | Day |
|--------|------------|-----|
| **thinking-core** (5/7) | first-principles, determinism-compass, stress-test, bias-spotter, red-team, dual-lens | 1,2,3,5 |
| **product-sense** (4/7) | problem-ai-fit, failure-modes, feedback-flywheel, ai-product-taste | 2,3,5 |
| **eval-and-quality** (4/4) | eval-framework, eval-driven-development, ai-product-metrics, production-observability | 1,2,3 |
| **agent-design** (2/5) | agent-harness, autonomy-spectrum | 4 |
| **safety-and-trust** (2/3) | trust-ladder, safety-by-design | 4 |
| **craft** (3/8) | prompt-as-product, ship-decision, cost-model | 4,5 |

**Total: 22/39 skills** (eval-focused subset)

---

## Deliverables

1. **Eval Strategy Document** — Quality dimensions, metrics, acceptance thresholds
2. **Golden Dataset** — Representative test set with adversarial and edge cases
3. **Eval Pipeline** — Automated + LLM-as-judge + human review workflow
4. **Metrics Dashboard** — pass@k, acceptance rate, correction rate, cost tracking
5. **Observability Stack** — Silent degradation detection, drift alerts, context anxiety monitoring
6. **EDD Process** — Documented eval-driven development cycle for the team
7. **Eval Cost Model** — Sustainable budget for ongoing eval operations

---

## When to Run This Workflow

- **First AI feature approaching launch** — Before you ship without evals
- **Post-incident** — After a quality failure that should have been caught
- **Team scaling** — When new engineers need to understand the eval process
- **Model migration** — When switching models and need to re-validate quality
- **Eval debt** — When you've been shipping without systematic evaluation

# Agent launch checklist
**From prototype agent to production-grade autonomous system**

A structured pre-launch workflow specifically for agent and autonomous AI features — where the consequence magnitude of failure is higher, the architecture is more complex, and traditional QA doesn't cover the failure surface. Use this when your AI feature makes autonomous decisions, uses tools, or operates in multi-step workflows.

**Timeline:** 3-5 days (parallel with final engineering work)
**Audience:** Product managers, ML engineers, safety leads, QA leads
**Trigger:** Agent feature approaching launch; agent moving up the autonomy spectrum; multi-agent system going to production
**Output:** Fully vetted agent with boundary matrix, safety boundaries, tool governance, eval gates, and rollout plan

---

## Day 1: agent architecture audit

**Goal:** Verify the agent architecture is sound, permissions are scoped, and failure boundaries are defined.

### Morning: architecture review

**Layer 2 — Agent Design:**
1. **rtp-agent-spec** — Audit the agent specification.
   - Is the step graph complete? (every discrete operation mapped)
   - Autonomy level assigned per step with explicit reasoning?
   - Trust thresholds defined? (confidence score boundaries, not vague)
   - Handoff protocol documented? (state passed forward, state dropped, reason)
   - Failure recovery specified per step? (rollback, notification, user experience)
   - Boundary matrix complete?

2. **rtp-agent-harness** *(if harness pattern)* — Verify harness architecture.
   - Planner→Generator→Evaluator roles clear?
   - Sprint contracts defined with testable pass/fail criteria?
   - Max iterations set with kill conditions?
   - Context management: Pre-Rot Threshold configured?
   - File-based communication vs. context window state?

3. **rtp-agent-ecosystem** *(if multi-agent)* — Verify orchestration.
   - Agent-to-agent communication protocols defined?
   - Error propagation boundaries explicit?
   - What happens when one agent in the chain fails?
   - Capability advertisement and task negotiation patterns?

### Afternoon: tool and permission audit

**Layer 2 — Agent Design:**
4. **rtp-tool-architecture** — Audit tool access governance.
   - Every tool classified by mutation type? (read, write-reversible, write-audited, delete, cascade)
   - Permission scopes defined? (agent, tool, resource, rate, approval gate)
   - Audit logs capture action + decision metadata?
   - Escape hatches exist? (circuit breaker, kill switch, rollback window)
   - MCP connectors tested in production-like environment?

5. **rtp-autonomy-spectrum** — Verify autonomy calibration.
   - Is the feature at the right autonomy level for launch?
   - Context anxiety thresholds set?
   - Progressive autonomy path defined? (start low, earn higher)
   - User override mechanism clear and accessible?

### Close of Day
- **Output:** Architecture audit complete; boundary matrix verified; tool permissions locked; autonomy levels confirmed

---

## Day 2: safety and trust validation

**Goal:** Validate that safety is designed in and trust mechanisms work correctly.

### Pre-Flight: responsible AI governance check

**Run this before any safety testing begins.** Safety testing without governance ownership is procedure without accountability.

**Invoke `rtp-responsible-ai-program`** — Run the 3 Gaps diagnostic and SHARP self-assessment.

| Gap | Closed? | What "Closed" Means |
|-----|---------|---------------------|
| **Accountability Gap** | YES / NO | A named individual — not a committee — is personally accountable if this AI causes harm |
| **Strategy Gap** | YES / NO | This Day 2 review is a mandatory gate, not a retrospective tick-box after launch |
| **Resource Gap** | YES / NO | The responsible AI owner has authority to pause launch, not merely advisory voice |

**SHARP minimum bar for launch:**
- **S** — Project-level owner named and accepted accountability
- **H** — Ethics review is hardwired into this checklist, not optional
- **A** — Top 3 ethical risks have been translated into business risk language (financial or reputational impact)
- **R** — Responsible behavior is rewarded in post-launch retrospectives, not just penalized when missing
- **P** — Team has reviewed at least one analogous failure case — judgment rehearsed, not just policy read

> **Gate:** If Accountability or Strategy gaps remain open, resolve before proceeding. Proceeding without a named owner means no one stops the agent when it needs to be stopped.

---

### Morning: safety boundaries

**Layer 2 — Safety & Trust:**
6. **rtp-safety-by-design** — Verify constitutional principles.
   - 5-10 behavioral rules defined and testable?
   - Defense-in-depth layers active? (input validation → model constraints → output filtering → human review)
   - Adversarial eval completed? (rtp-stress-test the agent with adversarial inputs)
   - Multi-agent safety: can one agent override another's safety constraints?

7. **rtp-safety-as-moat** — Position safety for launch narrative.
   - What's the alignment tax? (latency, accuracy, complexity cost of safety)
   - Where does safety become the feature story? (not just compliance)
   - What safety guarantees can we make to users?

**Layer 1 — Thinking Core:**
8. **rtp-failure-modes** — Verify degradation paths.
   - For each failure mode: what does the user experience?
   - Fallback cascade: AI → simpler model → rules → human — tested?
   - Recovery paths: how far back does rollback go?
   - User communication: how does the agent explain when it fails?

9. **rtp-stress-test** — Run 6-dimension stress test.
   - Scale: what happens at 10x concurrent agents?
   - Adversarial: malicious user inputs and prompt injection
   - Model degradation: agent with 10-20% worse model quality
   - Context poisoning: bad retrieval data fed to agent
   - Cascade: one step fails — does the whole agent collapse?
   - Economic: cost per task at 10x volume

### Afternoon: trust calibration

**Layer 2 — Safety & Trust:**
10. **rtp-trust-ladder** — Verify trust mechanisms.
    - Confidence displays calibrated? (stated confidence matches actual accuracy)
    - Trust repair works? (when agent fails, recovery restores user confidence)
    - Human override accessible at every autonomy level?
    - Trust-autonomy calibration table verified with real usage data?

**Layer 1 — Thinking Core:**
11. **rtp-bias-spotter** — Audit for decision biases in agent behavior.
    - Does the agent exhibit systematic biases?
    - Are there input patterns where bias is amplified?
    - Does multi-step reasoning compound biases?

### Close of Day
- **Output:** Safety boundaries verified; stress test passed; trust calibration confirmed; bias audit clean

---

## Day 3: evaluation and observability

**Goal:** Verify eval infrastructure is ready and monitoring will catch production issues.

### Morning: eval readiness

**Layer 2 — Eval & Quality:**
12. **rtp-eval-framework** — Verify agent-specific evals.
    - Per-step eval: each step tested independently
    - End-to-end eval: full agent workflow tested
    - Cascading error eval: 90% × 90% × 90% = 72.9% — is this acceptable?
    - pass@k vs pass^k: are the right metrics applied per step?
    - Eval saturation check: are test sets fresh?

13. **rtp-eval-driven-development** — Verify EDD discipline.
    - Every agent behavior has a corresponding eval?
    - Criteria drift addressed? (eval criteria updated from production observation)
    - Regression suite covers known failure modes?

14. **rtp-ai-product-metrics** — Verify metrics dashboard.
    - Agent-specific metrics: step completion rate, rollback rate, human intervention rate
    - pass@k and pass^k per step and end-to-end
    - Cost per successful task completion (including retries)
    - Time-to-completion distribution

### Afternoon: observability

**Layer 2 — Eval & Quality:**
15. **rtp-production-observability** — Verify monitoring stack.
    - Silent degradation detection active?
    - Context anxiety monitoring (context window utilization approaching limits)?
    - Sprint contract compliance tracking?
    - Drift detection on input distributions?
    - Alert routing: who gets paged for what severity?

**Layer 1 — Thinking Core:**
16. **rtp-determinism-compass** — Final determinism classification.
    - Which agent outputs must be deterministic? Are they?
    - Which can be probabilistic? Within acceptable variance?
    - Are determinism requirements reflected in eval thresholds?

### Close of Day
- **Output:** Eval gates verified; monitoring active; metrics dashboard operational; determinism requirements confirmed

---

## Day 4: economics and launch decision

**Goal:** Validate cost structure and make the ship decision.

### Morning: economics validation

**Layer 3 — Craft:**
17. **rtp-cost-model** — Validate agent economics.
    - Cost per successful task (including harness overhead, retries, eval cost)
    - Harness economics: justified? ($9 solo vs $200 harness — is quality worth it?)
    - Token flow: cached prompt optimization applied?
    - Cost at 10x, 100x scale: sustainable?

**Layer 2 — AI Strategy:**
18. **rtp-token-economics** — Verify token flow.
    - Input/output token patterns per step
    - Cached prompt economics leveraged?
    - Model routing: right model per step?
    - Cost surprises in production load testing?

**Layer 2 — Product Sense:**
19. **rtp-invisible-stack** — Verify hidden infrastructure.
    - Retrieval latency under load?
    - Post-processing pipeline stable?
    - Monitoring coverage complete?
    - Infrastructure cost within budget?

### Afternoon: ship decision

**Layer 3 — Craft:**
20. **rtp-ship-decision** — Make the go/no-go decision.
    - All eval gates passed?
    - Safety boundaries verified?
    - Tool permissions locked?
    - Cost structure sustainable?
    - Rollout plan defined? (% rollout, canary, monitoring triggers)
    - Rollback plan tested? (can you revert to non-agent or lower-autonomy version?)
    - Success metrics defined for first 30 days?

**Layer 1 — Thinking Core:**
21. **rtp-stress-test** — Final pre-mortem.
    - "It's 30 days post-launch and this agent feature failed — why?"
    - What production scenarios aren't covered by evals?
    - What would make you pull the kill switch?

### Close of Day
- **Output:** Economics validated; ship decision made; rollout plan documented; kill conditions defined

---

## Day 5: launch and monitor (launch Day)

**Goal:** Execute launch and verify production behavior.

### Morning: staged rollout

22. **rtp-production-observability** — Monitor launch metrics in real-time.
    - Canary metrics: error rate, latency, cost, user satisfaction
    - Compare canary vs. control (if A/B testing)
    - Watch for silent degradation signals
    - Monitor context anxiety levels

### Afternoon: first 4 hours

23. **rtp-feedback-flywheel** — Activate signal collection.
    - User corrections flowing to eval pipeline?
    - Implicit signals tracked? (retries, abandonment, escalation)
    - Feedback latency: how fast are signals arriving?

24. **rtp-ai-ux-patterns** — Monitor user interaction.
    - Are confidence displays working as designed?
    - Are human-AI handoffs happening at right moments?
    - Any unexpected user behavior patterns?

### Close of Day
- **Output:** Launch executed; first 4 hours monitored; no critical issues (or rollback executed); 30-day monitoring plan active

---

## Skill coverage

| Plugin | Skills Used |
|--------|------------|
| **thinking-core** | rtp-first-principles*, rtp-determinism-compass, rtp-bias-spotter, rtp-stress-test, rtp-failure-modes |
| **product-sense** | rtp-invisible-stack, rtp-feedback-flywheel, rtp-ai-ux-patterns |
| **agent-design** | rtp-agent-spec, rtp-agent-harness, rtp-agent-ecosystem, rtp-tool-architecture, rtp-autonomy-spectrum |
| **safety-and-trust** | rtp-safety-by-design, rtp-safety-as-moat, rtp-trust-ladder |
| **eval-and-quality** | rtp-eval-framework, rtp-eval-driven-development, rtp-ai-product-metrics, rtp-production-observability |
| **craft** | rtp-cost-model, rtp-ship-decision |
| **ai-strategy** | rtp-token-economics |

**The skills this sequence uses are named above.** It is the agent-launch subset, not the whole library.

---

## Pre-Launch checklist (summary)

- [ ] Boundary matrix complete (autonomy level, trust threshold, failure mode, recovery cost per step)
- [ ] Tool permissions scoped and audited (read/write/delete/cascade classified)
- [ ] **Responsible AI governance confirmed** — named owner, mandatory gate, authority to pause launch (3 Gaps + SHARP — Day 2 Pre-Flight)
- [ ] Constitutional principles defined and tested (5-10 behavioral rules)
- [ ] 6-dimension stress test passed (scale, adversarial, degradation, poison, cascade, economic)
- [ ] Trust calibration verified (confidence display accuracy, repair mechanisms, override access)
- [ ] Eval gates met (per-step and end-to-end, pass@k and pass^k)
- [ ] Observability active (silent degradation, context anxiety, drift detection, alerts routed)
- [ ] Cost model validated (per-task cost sustainable at 10x scale)
- [ ] Rollout plan defined (canary %, monitoring triggers, rollback criteria)
- [ ] Kill conditions documented (what triggers immediate shutdown)
- [ ] Pre-mortem completed (rtp-stress-test of core assumptions)
- [ ] 30-day monitoring plan active (metrics, alerts, review cadence)

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.

# AI incident response
**Diagnose, contain, fix, learn.**

What to do when an AI feature fails in production, whether it is hallucinating, degrading quietly, crossing a safety boundary, or costing more than it should.

An AI incident behaves differently from a conventional software incident. It is usually probabilistic, so it is hard to reproduce. It often degrades gradually rather than crashing, which means the first person to notice may be a customer rather than an alert.

**Timeline:** Hours to days (depends on severity)
**Audience:** Product managers, ML engineers, on-call engineers, safety leads
**Trigger:** Quality metric drops; user complaints spike; safety boundary violated; cost anomaly detected; observability alert fires
**Output:** Incident contained; root cause identified; fix deployed; post-mortem with prevention measures

---

## Severity classification

Before starting: classify the incident.

| Severity | Description | Response Time | Example |
|----------|-------------|---------------|---------|
| **SEV-1** | Safety violation or data exposure | Immediate (minutes) | Agent executes unauthorized action; PII leaked; harmful output to users |
| **SEV-2** | Major quality degradation | Within 1 hour | Accuracy drops >20%; hallucination rate spikes; user complaints surge |
| **SEV-3** | Moderate degradation | Within 4 hours | Gradual quality decline; cost overrun; partial feature failure |
| **SEV-4** | Minor issue | Within 24 hours | Edge case failures; cosmetic quality issues; minor cost drift |

---

## Phase 1: detect and classify (first 30 minutes)

**Goal:** Understand what's happening, how bad it is, and who's affected.

### Observability check

**Layer 2 — Eval & Quality:**
1. **rtp-production-observability** — Pull monitoring data.
   - What metrics triggered the alert? (quality, safety, cost, latency)
   - When did degradation start? (gradual drift vs. sudden drop)
   - What's the consequence magnitude? (all users, segment, geography, use case)
   - Is this a silent degradation or a visible failure?
   - Context anxiety levels: is the agent running out of context?

2. **rtp-ai-product-metrics** — Check the metrics dashboard.
   - pass@k / pass^k trends: where's the drop?
   - Acceptance rate and correction rate: user-facing impact?
   - Cost per query: unexpected spike?
   - Eval saturation: were evals catching this before it hit production?

### Root cause hypotheses

**Layer 2 — Product Sense:**
3. **rtp-failure-modes** — Map the failure to known taxonomy.
   - Which hallucination type? (fabrication, drift, attribution, omission, confidence, cascade)
   - Is this a known failure mode or a new one?
   - Is the failure mode in the model, the context, the tools, or the orchestration?

**Layer 1 — Thinking Core:**
4. **rtp-first-principles** — Decompose the failure.
   - What changed? (model update, prompt change, data drift, traffic pattern, external API)
   - What's the atomic cause? (not symptoms, the root)
   - Is this a regression or a novel failure?

### Output: incident classification
```
Severity: [SEV-1/2/3/4]
Started: [timestamp]
Consequence magnitude: [users/queries affected]
Root cause hypothesis: [best guess]
Containment needed: [yes/no]
```

---

## Phase 2: contain (30 minutes - 2 hours)

**Goal:** Stop the bleeding. Limit consequence magnitude while you diagnose.

### Containment options

**Layer 2 — Agent Design:**
5. **rtp-tool-architecture** — Activate escape hatches.
   - Circuit breaker: disable the failing tool/agent if error rate > threshold
   - Kill switch: shut down the feature entirely if SEV-1
   - Gradual rollback: reduce traffic to the AI path (route to fallback)
   - Rate limit: reduce query volume to manageable level

6. **rtp-autonomy-spectrum** — Downgrade autonomy.
   - Move from Level 3-4 (autonomous) to Level 1-2 (suggest/confirm)
   - Enable human-in-the-loop for all decisions until root cause is found
   - This is the "safe mode" for agent features

### Fallback activation

**Layer 1 — Thinking Core:**
7. **rtp-failure-modes** — Activate designed degradation paths.
   - AI → simpler model → rules → human: which fallback level?
   - Is the fallback tested and ready? (or is this the first time you're using it?)
   - User communication: how do you tell users the feature is degraded?

**Layer 2 — Safety & Trust:**
8. **rtp-safety-as-moat** — If safety boundary violated:
   - Immediate: disable the feature for affected users
   - Assess: is there legal/compliance exposure?
   - Communicate: notify affected users and internal stakeholders
   - Document: capture exact inputs/outputs for investigation

### Output: containment status
```
Containment action: [what you did]
Current state: [feature disabled / degraded / rate-limited / human-in-loop]
User impact: [what users see now]
Estimated time to root cause: [hours]
```

---

## Phase 3: diagnose (2-8 hours)

**Goal:** Find the root cause and understand why existing safeguards didn't catch it.

### Deep investigation

**Layer 2 — Eval & Quality:**
9. **rtp-eval-framework** — Run diagnostic evals.
   - Run the full eval suite against the current system
   - Compare results to last known good state
   - Which specific test cases are failing that weren't before?
   - Are evals catching the production failure? (if not, eval gap identified)

10. **rtp-eval-driven-development** — Check for criteria drift.
    - Have production patterns drifted from eval dataset?
    - Are there new input patterns not covered by test sets?
    - Has the model's behavior changed in ways evals don't measure?

**Layer 2 — Product Sense:**
11. **rtp-invisible-stack** — Investigate the hidden layers.
    - Retrieval: is context being retrieved correctly?
    - Post-processing: are validation steps working?
    - External dependencies: is an API or data source degraded?
    - Infrastructure: latency, memory, compute — within normal bounds?

12. **rtp-feedback-flywheel** — Check user signal data.
    - What are users telling you? (corrections, complaints, abandonment)
    - Do user signals correlate with the metric drop?
    - Any user-reported edge cases that explain the failure?

### Agent-Specific investigation

**Layer 2 — Agent Design (if agent feature):**
13. **rtp-agent-harness** — Investigate harness failures.
    - Is the Planner generating bad plans?
    - Is the Generator failing against sprint contracts?
    - Is the Evaluator missing failures?
    - Context management: has Pre-Rot Threshold been exceeded?

14. **rtp-agent-spec** — Check boundary matrix.
    - Which step is failing?
    - Is the failure contained by error boundaries?
    - Is state being passed correctly between steps?
    - Are handoff protocols working?

### Root cause categories

**Layer 1 — Thinking Core:**
15. **rtp-bias-spotter** — Check for investigation bias.
    - Are you anchored on the first hypothesis?
    - Have you considered causes outside your mental model?
    - Is there confirmation bias in your diagnostic data?

### Output: root cause analysis
```
Root cause: [precise description]
Category: [model / context / tools / orchestration / data / infrastructure / external]
Why safeguards missed it: [eval gap / monitoring gap / novel failure / criteria drift]
Fix approach: [hotfix / prompt change / model switch / data fix / architecture change]
```

---

## Phase 4: fix and verify (hours to days)

**Goal:** Implement the fix and verify it resolves the issue without creating new problems.

### Fix implementation

**Layer 3 — Craft:**
16. **rtp-prompt-as-product** — If prompt-related fix:
    - Version the fix as a new prompt version
    - Run regression suite on new prompt
    - A/B test fix vs. current (if not SEV-1)
    - Document what changed and why

17. **rtp-cost-model** — If cost-related incident:
    - Identify cost driver (token explosion, retry loops, harness overhead)
    - Implement cost controls (token limits, retry caps, model routing)
    - Validate fix at production scale

### Verification

**Layer 2 — Eval & Quality:**
18. **rtp-eval-framework** — Verify the fix.
    - Run full eval suite: does fix resolve the failing cases?
    - Run regression suite: does fix create new failures?
    - Run production shadow test: does fix work with real traffic?
    - Add the incident's failure pattern as a permanent test case

**Layer 2 — Safety & Trust:**
19. **rtp-trust-ladder** — Verify trust restoration.
    - If trust was damaged: what's the trust repair path?
    - Should calibrated confidence displays be adjusted?
    - Do users need communication about the fix?

**Layer 1 — Thinking Core:**
20. **rtp-stress-test** — Stress test the fix.
    - Does the fix hold under the conditions that caused the original failure?
    - Does it hold at 10x scale?
    - Does it introduce new stress points?

### Output: fix verification
```
Fix deployed: [timestamp]
Eval results: [pass/fail with specifics]
Regression: [clean / new issues found]
Production verification: [metrics returning to normal / still degraded]
```

---

## Phase 5: Post-Mortem and prevention (within 48 hours)

**Goal:** Learn from the incident and prevent recurrence.

### Post-Mortem

**Layer 1 — Thinking Core:**
21. **rtp-stress-test** — Challenge the fix.
    - Under what conditions would this fix fail?
    - What similar failure modes haven't been addressed?
    - What assumptions are we making about the fix that might not hold?

22. **rtp-dual-lens** — Synthesize product and technical learnings.
    - Product: what did this incident teach us about user expectations?
    - Technical: what does this reveal about our architecture gaps?
    - Process: what does this tell us about our eval and monitoring coverage?

### Prevention measures

**Layer 2 — Eval & Quality:**
23. **rtp-production-observability** — Update monitoring.
    - Add alerts that would have caught this incident earlier
    - Tighten thresholds on affected metrics
    - Add the incident pattern to drift detection

24. **rtp-eval-driven-development** — Update eval infrastructure.
    - Add incident's failure pattern to golden dataset
    - Update eval criteria to catch this class of failure
    - Schedule eval dataset refresh if criteria drift was the cause

**Layer 2 — Product Sense:**
25. **rtp-ai-product-taste** — Assess overall quality impact.
    - Has this incident degraded the "museum quality" standard?
    - Do we need a broader quality initiative?
    - Are there other features at similar risk?

### Output: Post-Mortem document
```
# AI incident post-mortem: [title]
Date: [date]
Severity: [SEV-X]
Duration: [hours]
Users affected: [count]

## Timeline
- [detection] → [classification] → [containment] → [root cause] → [fix] → [verification]

## Root cause
[Precise technical description]

## Why we Didn't catch it
[Eval gap / monitoring gap / novel failure / criteria drift]

## Fix
[What was deployed]

## Prevention
- [ ] New eval test cases added
- [ ] Monitoring alerts updated
- [ ] Process change documented
- [ ] Affected users communicated with

## Learnings
[What this incident teaches the team]
```

---

## Skill coverage

| Plugin | Skills Used |
|--------|------------|
| **thinking-core** | rtp-first-principles, rtp-bias-spotter, rtp-stress-test, rtp-dual-lens, rtp-failure-modes |
| **product-sense** | rtp-failure-modes, rtp-invisible-stack, rtp-feedback-flywheel, rtp-ai-product-taste |
| **eval-and-quality** | rtp-eval-framework, rtp-eval-driven-development, rtp-ai-product-metrics, rtp-production-observability |
| **agent-design** | rtp-tool-architecture, rtp-autonomy-spectrum, rtp-agent-harness, rtp-agent-spec |
| **safety-and-trust** | rtp-safety-as-moat, rtp-trust-ladder |
| **craft** | rtp-prompt-as-product, rtp-cost-model |

**The skills this sequence uses are named above.** It is the incident-response subset, not the whole library.

---

## When to use this playbook

- **Alert fires:** Observability alert triggers on quality, safety, or cost metric
- **User complaints surge:** Multiple users reporting the same failure pattern
- **Safety violation detected:** Constitutional principle breached in production
- **Cost spike:** Token costs or infrastructure costs exceed budget unexpectedly
- **Model update regression:** Quality degrades after a model provider updates their model
- **Eval failure in production:** Features passing evals in staging but failing in prod

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.

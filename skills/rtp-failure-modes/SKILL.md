---
name: rtp-failure-modes
description: "Complete AI failure engineering: identify failure types (hallucination, injection, cascade, drift), quantify risk (cost × detectability), then design the response (confidence UX, correction paths, refusal boundaries, graceful degradation). Use to spec features, design telemetry, write failure acceptance criteria. Merges former failure-design skill."
imports: [stress-test]
version: "2.0"
---

# Failure Modes: Diagnostic & Design Framework

## DEPTH DECISION

**Go deep if:** Speccing a new AI feature, designing telemetry for production AI, performing a failure mode audit, or designing failure UX for a customer-facing feature. **Skim to diagnostic questions if:** Quick review of failure coverage in a feature spec. **Skip if:** Purely deterministic system or research prototype with no production users.

**If you're asking "Should we use AI at all?", use problem-ai-fit instead.** This skill assumes you've decided to use AI — it maps what will go wrong when you do AND how to handle it when it does.

## GROUNDING (Before Starting)

Before doing any failure analysis, answer these three questions. If you can't answer them, you're not ready to use this skill.

1. **Who is the user and what stakes do they face?** (A doctor acting on AI output has different stakes than a knowledge worker drafting an email — this changes which failures matter AND how much UX investment they deserve.)
2. **What does the AI output feed into next?** (Is it a final recommendation, an input to another system, or raw material the user will edit? Each has a different cascade risk profile and different recovery cost.)
3. **Do we have existing telemetry?** (If yes, look at error rates before theorizing. If no, the monitoring design is your most urgent deliverable from this session.)

**DELIVERABLE FORMAT**

Do you want:
- **(A) Quick audit** — Top 5 failure modes with annual risk budget + failure UX recommendations. 1 page. (Use when reviewing a spec or doing a 30-minute design review.)
- **(B) Full registry** — Complete failure taxonomy, detection latency map, cascade risk paths, mitigation budget, monitoring design, failure UX spec, graceful degradation hierarchy, and acceptance criteria. (Use when architecting a production system or doing a pre-launch audit.)

If the user hasn't specified, ask. The quick audit takes 20 minutes. The full registry takes 2-4 hours.

## THE TRAP

**The Accuracy Mono-focus.** Teams obsess over model accuracy while ignoring latency, cost, and drift. A model that's 95% accurate but takes 4 seconds to respond loses users faster than a model that's 88% accurate at 500ms. Accuracy is one of six failure dimensions, not the only one.

**The Happy Path Monopoly.** Product demos show success. Design reviews focus on ideal flow. User stories describe winning scenarios. The PM writes one line about failures — "show error message" — and moves on. This is designing a car with no seatbelts because you plan to only drive in good weather.

**The Confident Wrong.** The most dangerous failure mode isn't errors — it's **confident errors**. When the model is wrong and says "I'm not sure," the user can verify. When the model is wrong and says it with full confidence, the user acts on it. In multi-agent systems, a confidently wrong upstream agent poisons every downstream agent.

**The Blame-Shift Pattern.** "Try rephrasing your question" shifts the burden to the user — they asked wrong. Trust erodes not because the AI was wrong, but because it avoided responsibility. Compare: "I'm not confident in this answer. Here's what I found, but verify before acting on it." Same failure, opposite trust impact.

**The Confidence Theater.** Displaying confidence percentages without actionable meaning. "87% confidence" is noise. Confidence must translate to action: "I'm confident — no verification needed" vs "I found something — you should review it" vs "I'm too uncertain — ask a human." Actionable trust language beats false precision.

## THE PROCESS

### Phase 1: Identify — Map Your Failure Taxonomy

| **Failure Type** | **Manifestation** | **Detectability** | **Cost Asymmetry** |
|---|---|---|---|
| **Hallucination: Fabrication** | Pure invention (facts never existed) | Medium (requires external verification) | High (user trusts false info) |
| **Hallucination: Conflation** | Correct facts, wrong attribution/context | Hard (requires domain knowledge) | Critical (undetectable errors) |
| **Hallucination: Extrapolation** | Extends a true pattern beyond data | Hard (sounds plausible) | High (creates false confidence) |
| **Hallucination: Temporal confusion** | Mixes timeframes (reports 2023 data as current) | Medium (requires temporal verification) | High in fast-moving domains |
| **Hallucination: Over-generalization** | Applies a specific fact broadly | Medium (requires scope awareness) | Medium-High (misleading conclusions) |
| **Hallucination: Misattribution** | Real quote/fact attributed to wrong source | Hard (requires citation check) | Critical in legal/academic contexts |
| **Confident Wrong** | High certainty + factually false | Critical (no uncertainty signal) | Extreme (highest user-harm mode) |
| **Prompt Injection** | External input tricks model behavior | Hard (zero-day potential) | Extreme (jailbreak, data theft) |
| **Retrieval Failure** | Wrong document returned; bad synthesis | Medium (verify against source) | High if confidential/legal context |
| **Refusal** | Legitimate request declined | Immediate (user sees it) | Low per instance, High if systematic |
| **Latency** | Response exceeds user expectation | Immediate | Low (retry/abandon) |
| **Cost Explosion** | Token budget exceeded | Delayed (discovered in billing) | High (feature disabled) |
| **Cascade: Sub-agent Failure** | One agent's bad output → downstream propagation | Hard (error buried in chain) | Extreme (compounding errors) |
| **Silent Degradation** | Quality drops gradually without error signals | Critical (invisible) | Extreme (months of bad output before detection) |
| **Partial Failure** | Truncated or incomplete output | Medium (detect via length/structure) | Medium (user may not notice missing info) |

### Phase 2: Quantify — Detection Latency & Cost

**Detection Latency Framework**

Ask: **How long until a silent failure is noticed?**

- **Immediate**: User sees the failure (latency, refusal, obviously wrong output) → Detected in seconds
- **Delayed**: User notices degradation over time (drift, cost creep, bias in cohort) → Days/weeks
- **Silent**: Nobody notices unless audited (confidential data conflation, outdated facts in archival use) → Months or never
- **Discovered externally**: Customer complaint, legal challenge, news article → Reputational/legal risk

**Critical insight**: A rare catastrophic failure (confident hallucination affecting 0.1% of users) matters more than frequent harmless ones (benign refusal, 50% of requests). Prioritize by **failure cost × detection latency**, not by frequency alone.

**Failure Cost Asymmetry Table**

Not all failures are equal. Use this to allocate mitigation budget:

| Failure | Frequency | Cost per Incident | Annual Risk | Mitigation Budget |
|---------|-----------|------------------|------------|------------------|
| Hallucination (fabrication) | 3% of responses | $500 (user acts on false info) | $150K at 10K daily responses | $50K/year (citation verification) |
| Confident wrong | 0.5% of responses | $5,000 (legal/financial action) | $250K | $100K/year (confidence calibration) |
| Prompt injection | 0.01% of requests | $50,000 (data breach) | $50K | $30K/year (input filtering) |
| Silent degradation | 2x/year events | $200,000 (months of bad output) | $400K | $80K/year (continuous eval pipeline) |

**Prioritize by annual risk, not frequency.** Rare-but-catastrophic outweighs common-but-cheap.

### Phase 3: Design — Failure UX & Response Modes

**For each AI output, answer: "What happens when this is wrong?"**

- Wrong and user notices immediately → Design correction path
- Wrong and user notices later → Design recovery path + trust repair
- Wrong and user never notices → Design verification mechanism
- Wrong and causes downstream action → Design undo/reversal mechanism

**Failure Response Modes (choose one per failure type):**

- **Graceful degradation**: Return partial/low-confidence result with explicit uncertainty signal ("I'm not certain, but..."). Cost: UX friction. Best for: non-critical features, early-stage products.
- **Explicit failure**: Refuse the request, explain why, offer alternatives. Cost: User blocked. Best for: high-stakes contexts (financial, medical, legal), where silence is worse than refusal.
- **Silent failure**: Return output with confidence signal but no mechanism for verification. Cost: Trust erosion. Only acceptable for: low-stakes, user-facing experimentation where users know they're testing.

**Never ship confident wrong.** If you can't detect/prevent it, you've chosen silent failure — own that choice.

**Failure UX Patterns:**

- **Progressive confidence:** Show confidence inline, not as a separate warning. "I'm fairly confident this is the answer, but verify the date" vs generic "AI-generated content may be inaccurate." Calibrated transparency matched to risk.
- **Inline correction:** Let users edit AI output in place without starting over. Changes apply instantly. Trains the model on the correction if approved.
- **Explanation on failure:** "I couldn't find recent pricing because our knowledge base was last updated in January" beats "No results found." Users understand the constraint and decide what to do next.
- **Undo/revert:** Every AI action should have a single-click undo for at least 30 seconds.
- **Feedback on failure:** Make it dead easy to report bad output. Thumbs down, flag for review, short comment. Route high-volume bad outputs to model improvement queue.
- **Degraded mode indicator:** Show users explicitly when they're getting a fallback experience. Transparency builds trust even in failure.

**Refusal Boundary Design:**

When should the AI say "I don't know" instead of guessing?
- What confidence threshold triggers refusal?
- What does the refusal look like to the user?
- Is refusal better than a low-confidence answer? (Usually yes for high-stakes domains.)
- **The refusal paradox:** Too many refusals = useless system. Too few = dangerous. The threshold is a product decision, not a technical one. Measure and tune empirically.

### Phase 4: Design — Graceful Degradation Hierarchy

When AI fails, what's the fallback chain? Each step trades speed for reliability.

- **Cache:** Return last known good result (fast, stale)
- **Simpler model:** Swap to cheaper, more reliable model (slower, less capable)
- **Rules:** Switch to deterministic fallback (no surprise failures)
- **Human escalation:** Hand off to customer support (slow, high trust)
- **Error state:** Show degraded experience or "try later" (worst case, last resort)

**Worked Example: AI Customer Support Agent**

| Level | Trigger | Latency | Quality | Coverage | User Experience |
|-------|---------|---------|---------|----------|-----------------|
| Cache | Exact phrase match on 50+ historical | 50ms | High (proven) | 85% | Instant, "from our knowledge base" |
| Simpler Model | Low complexity score | 200ms | 78% | 10% | Normal latency, "quick lookup" |
| Rules | Confidence < 60% | 10ms | 85% (deterministic) | 4% | Human-like, includes escalation link |
| Human | All above below threshold | Async | 99% | 1% | "Creating a support ticket for you" |
| Error | Service unavailable/cascade | Instant | Honest failure | Outages | Direct contact info |

### Phase 5: Cascade Failures in Multi-Agent Systems

When agents chain together, failures compound in ways single-agent systems never experience:

**Error Propagation Math:**
- Agent A outputs with 95% accuracy → Agent B receives 5% garbage input
- Agent B can't detect garbage input (it looks like valid text) → treats it as ground truth
- Agent B's accuracy on clean input: 95%. On garbage input: ~20%
- End-to-end: 95% × 95% = 90.25% on clean paths. But: 5% × 20% = 1% catastrophic (wrong + confident)
- That 1% cascading confident-wrong is your worst failure mode

**Multi-Agent Failure Patterns:**

| Pattern | Cause | Detection | Mitigation |
|---------|-------|-----------|-----------|
| Upstream hallucination propagation | Agent 1 fabricates, Agent 2 amplifies | Compare output against known facts | Verification gate between agents |
| Coordination drift | Agents' context diverges | Monitor inter-agent state consistency | Shared state file (Anthropic pattern) |
| Tool call cascade | Agent calls wrong tool | Log all tool calls; alert on unexpected sequences | Circuit breaker per tool |
| Context window saturation | Upstream context exhausts downstream | Monitor token count at each handoff | Compaction between agent steps |
| Evaluator hallucination | GAN-style evaluator false positive | Cross-validate with deterministic checks | Hybrid eval: LLM + code-based graders |

**Multi-Agent Failure Design:**
- **Circuit breaker:** If agent fails 3 times in 10 minutes, route to fallback. Reset when agent succeeds 5 times.
- **Isolation:** Each agent's failure shouldn't cascade. Design handoff contracts with fallback input types.
- **Checkpoint/rollback:** Save state before each hand-off. If Agent B fails, revert and try Agent C.
- **Timeout per step:** Agent A: 2s, Agent B: 3s, Agent C: 1s. Any timeout → escalate to fallback.
- **Error attribution:** Log Agent → Operation → Latency → Failure Type → Recovery Path.

### Phase 6: Recovery Cost Spectrum

Not all failures cost the same to recover from:

| Tier | Examples | Cost | Design Implication |
|------|----------|------|--------------------|
| **Seconds (Undo)** | Wrong autocomplete, declined suggestion | 2-5 seconds | Simple dismiss/undo |
| **Minutes-Hours (Repair)** | Email with wrong content, bad code committed | Trust + time | Correction + apology path |
| **Days-Weeks (Remediation)** | Bulk records updated wrong, bad financial advice | Legal risk + weeks | Audit trail + escalation |
| **Permanent (Irrecoverable)** | PII leaked, safety-critical error, trust destroyed | Cannot undo | Prevention-only; no recovery exists |

**Design by user type:**
- **Power user:** Tolerates higher error rate, recovers quickly. Design for speed.
- **Casual user:** Doesn't know when AI is wrong. Errors compound. Design for safety — prefer "I'm not sure."
- **Enterprise admin:** Wrong action affects thousands. Design for confirmation + audit logs + reversibility.

## DIAGNOSTIC QUESTIONS (Use These in Design Review)

**Q1: "What's the worst-case failure and what does it cost?"**
Not most likely — worst plausible. What would make the front page of a trade publication? State it as: "A user takes [action] based on [failure type] and suffers [harm]. This happens [frequency] and costs [dollar estimate] per incident."

**Q2: "How long until we notice a silent failure?"**
For each failure type, assign a detection latency band: Immediate (< 1 hour) / Delayed (1-7 days) / Silent (> 7 days). Every Silent failure needs an owned monitoring mechanism before launch.

**Q3: "Which failures are recoverable vs permanent?"**
For your top 3 failure modes: "If this failure occurs, what is the fastest path to making the user whole again? What's the time and cost?" If there's no answer, that's a permanent failure — invest in prevention, not recovery.

**Q4: "What's our false-confidence vector?"**
Run a confusion matrix against confidence scores. If accuracy < 60% in the high-confidence bucket — that's your confident-wrong zone and it needs immediate attention before launch.

**Q5: "Do users have any way to verify the output?"**
Map every output type: Ground truth / Expert spot-check / Proxy only. For any "Proxy only" output that feeds a consequential decision, name the explainability or review mechanism you'll build.

**Q6: "What happens if this fails in a cascade?"**
Draw your agent chain. Mark every handoff. For each: "Could garbage input from the prior step pass through undetected?" If yes — add a verification gate.

**Q7: "What's our detection asymmetry?"**
For your top 5 failure modes: Easy / Requires monitoring / Impossible without audit. For every "Impossible without audit" — name the sampling + review cadence.

**Q8: "What's the failure cost ratio?"**
Annual failure cost = frequency × cost per incident × annual volume. Compare to prevention cost. If prevention < 10% of annual risk → invest. If > 50% → reassess.

## PRODUCTION CASE: THE CASCADE NO ONE SAW COMING

*Anonymized from a real B2B SaaS product, 2024.*

A 3-agent pipeline: Analyst (pulled data, ran SQL) → Summarizer (synthesized findings) → Reporter (formatted executive brief). The Analyst connected to a data warehouse partition that stopped refreshing — but returned data without an error signal. The Summarizer received stale data and summarized it with full confidence. The Reporter formatted a polished brief.

Failure went undetected for 19 days. 34 enterprise customers received briefs. Three made budget decisions on stale metrics.

**Post-mortem fixes:**
1. Freshness check (hard stop if data > 6 hours old)
2. Cross-check: if data deviates > 20% from prior period, flag for human review
3. Reporter adds data-freshness timestamp to every output
4. End-to-end acceptance rate as a pipeline metric, checked daily

**Key lesson:** In a multi-agent pipeline, structurally valid output with no error code is invisible to agent-level monitoring. You need pipeline-level quality metrics and freshness checks at every handoff.

## FAILURE COST MATRIX (Stakes Calibration)

| Failure Scenario | Low Stakes (autocomplete) | Medium Stakes (search) | High Stakes (medical/financial) |
|---------|--------------------------|----------------------|-------------------------------|
| **Design investment** | Dismiss button, undo | Correction + alternatives | Full verification + human review |
| **Detection speed** | Batch eval (daily) | Near real-time (per session) | Real-time (per response, before display) |
| **Recovery path** | Auto-dismiss, undo | 3-5 alternatives, escalation | Block action, require human approval |
| **Cost of building** | 1-2 days | 1-2 weeks | 1-2 months (including safety review) |
| **Acceptance criteria** | "Wrong 15% is fine" | "Wrong ≤ 5%, alternatives shown" | "Wrong < 0.1%, human verification" |

## OUTPUT FORMAT

```
## Failure Engineering Spec: [Feature Name]

### AI Outputs
- [Output 1]: [Description and user context]
- [Output 2]: [Description and user context]

### Failure Mode Registry
| Failure Mode | Frequency | Severity | Detection | Detection Latency | Response | Owner | Escape Hatch |
|-------------|-----------|----------|-----------|-------------------|----------|-------|-------------|

### Per Output Failure Design: [Output Name]
**When wrong:** [Specific scenario]
**Detection:** [How wrong-ness is detected]
**User recovery:** [Inline edit, regenerate, escalate]
**Degradation level:** [Which fallback applies]

### Refusal Boundary
**Confidence threshold:** [e.g., "< 50% confidence OR can't find source"]
**Behavior:** [What the AI says]
**Rationale:** [Why this threshold]

### Cascade Risk: [if multi-agent]
[Agent chain with verification gates at each handoff]

### Annual Risk Budget
| Failure | Frequency × Cost | Mitigation Investment | Net Risk |
|---------|-----------------|----------------------|----------|

### Acceptance Criteria
- "When the AI is wrong, the user can [action]"
- "When the AI is uncertain, the system [behavior]"
- "When the AI fails completely, the user sees [experience]"

### Top 3 Unmitigated Risks: [what you've accepted and why]
```

## REALITY CHECK

- Not every failure mode needs mitigation. Accept low-cost failures. **But document that choice.**
- The worst failures are those you don't know you have. Invest in detection, not just prevention.
- Mitigations compound (prompt guardrails + retrieval + post-hoc checks = latency tax). Measure total cost.
- "Bad taste" failures are invisible in A/B tests. Monitor NPS proxy metrics.
- Cascade failures are exponential: 95% × 95% = 90.25% end-to-end. Map your cascade.
- Over-warning trap: If every output has a disclaimer, users develop warning fatigue. Calibrate transparency to risk.
- Correction cost vs consequence magnitude: Prioritize rich UX for high-stakes outputs, simple dismiss for low-stakes.
- **The Hamel Husain insight:** Spend 60-80% of your time on error analysis and evaluation.
- **Eval saturation problem (Anthropic):** When your eval catches 99%, the remaining 1% is where catastrophic ones hide. Refresh eval datasets quarterly.

## QUALITY GATE

- [ ] Top 5 failure modes identified and ranked by (cost × 1/detectability)
- [ ] 6 hallucination types explicitly mapped (fabrication, conflation, extrapolation, temporal, over-generalization, misattribution)
- [ ] Detection latency mapped for each (immediate/delayed/silent)
- [ ] Response mode chosen for each with explicit justification
- [ ] Failure UX pattern designed for each high-stakes output (confidence, correction, escalation)
- [ ] Refusal boundary defined with specific threshold and reasoning
- [ ] Failure acceptance criteria written for every user story
- [ ] Graceful degradation hierarchy mapped with trigger conditions
- [ ] Cascade failure paths documented with verification gates (for multi-agent systems)
- [ ] Monitoring/alerting designed for failures with detection latency > 1 hour
- [ ] Annual risk budget calculated for top failures
- [ ] Escape hatch documented (how to disable feature if it fails)
- [ ] Recovery cost classified per tier (seconds/minutes/days/permanent)

## WHEN WRONG

- When the feature is truly sandboxed and never touches external-facing output
- When the AI component is a research prototype with explicit "beta" messaging
- When shipping to learn is the priority AND detection/rollback is fast (< 1 hour)
- When failure analysis becomes a delay tactic instead of a path to safer shipping
- Internal tools where failure is cheap and users are trained to verify all outputs
- For deterministic components (rules-based error handling is different)
- **When you need to decide whether to use AI at all** — use problem-ai-fit instead. This skill assumes the AI decision is made.

---

## TRADE-OFF LEDGER

| Decision | Option A | Option B | How to choose |
|---|---|---|---|
| Monitoring depth | Instrument every failure type | Instrument top 5 by annual risk | If budget constrained, top 5 covers 80%+ |
| Response mode | Graceful degradation (always show something) | Explicit failure (refuse if uncertain) | Graceful for consumer; Explicit for high-stakes/regulated |
| Prevention vs detection | Prevent all failures upfront | Fast detection + rollback | Prevention for permanent failures; Detection for recoverable |
| Human-in-the-loop | Review all AI outputs | Review only flagged outputs | Full review for high-stakes; Sampling for high-volume |
| Transparency level | Confidence on every output | Confidence only when uncertain | Over-warning creates fatigue; calibrate to risk |
| Refusal threshold | High (refuse often, fewer errors) | Low (refuse rarely, more output) | Too high = useless; Too low = dangerous. Tune empirically |

## CONCLUSION

After completing the failure engineering spec, state:

1. **The recommendation:** "The top unmitigated risk is [failure type]. The annual risk is [$X]. The prevention cost is [$Y]. We recommend [invest / accept / monitor]."
2. **The key trade-off:** "We're choosing [option A] over [option B], accepting [cost of A] to avoid [cost of B]."
3. **The biggest risk:** "The failure mode we know least about is [type]. We'll establish a baseline by [method] within [timeframe]."
4. **The next action:** "Before launch: [specific action, owner, deadline]."

**Hypothesis frame:** "We believe [monitoring approach] will catch [failure type] because [mechanism]. We'd know this is wrong if [signal] within [timeframe]."

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

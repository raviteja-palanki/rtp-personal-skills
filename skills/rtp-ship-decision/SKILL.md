---
name: rtp-ship-decision
description: 'Go/no-go gate: safety tested, error rates acceptable, cost defensible at 10x, observability live, user education clear, failures mapped, fallback defined, formal go-no-go. Use when: 1 week before launch, production-ready. Triggers: ''ship gate'', ''launch checklist'''
---
# Ship Decision

## DEPTH DECISION

**Go deep if:** Shipping a user-facing AI feature in production, where failure has meaningful consequence magnitude (customer-visible, safety-critical, or revenue-impacting).

**Skim to Phase 3 if:** You've already passed safety review and just need to validate economics and observability setup.

**Skip if:** Internal experimental feature with automatic rollback, <30-day A/B test, or pre-PMF research features.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## Eval-Gated Shipping (Mandatory Gate)

Never ship without eval pass. This is the gate that prevents "it worked in staging" from shipping broken.

**Process:**
1. **Define ship-gate eval set:** 150+ real-world test cases representing the distribution of production use (not cherry-picked)
2. **Set threshold per severity:** Catastrophic <0.1%, High <1%, Medium <5%, Low <10%
3. **Run eval 48 hours before launch:** Not 2 weeks before. Output quality can degrade.
4. **If any severity fails:** Fix or delay ship. "We'll monitor it post-launch" means you didn't pass the gate.
5. **Document eval results:** Which test cases failed, why, what changed. This is your launch justification.

**"Good enough" for probabilistic systems:** A 98% accurate feature shipping to 10,000 users means 200 hallucinations per day. That's acceptable if: (1) hallucinations are reversible (user can undo), (2) confidence scores make obvious which outputs to trust, (3) monitoring catches patterns before churn spike. Without those three, 98% is not good enough.

---

## Eval-Gated Deployment (Automated Gate)

No AI change ships without the eval regression suite passing. This is automation, not approval.

**Pattern: CI/CD pipeline includes eval run as gating step.**
- Every prompt change: runs eval before merge to main
- Every model version bump: runs eval before production deploy
- Every context engineering change (system message, RAG retrieval, tool definitions): runs eval
- Every agent role change in harness systems: runs eval for that agent + full pipeline eval

**If ANY eval metric degrades beyond threshold: deploy is blocked automatically.** No human override (except explicit board decision for loss-leader features). The gate is:

- **Catastrophic errors:** If catastrophic error rate increases or stays above threshold, block.
- **High-severity errors:** If high-severity error rate increases beyond 0.5%, block.
- **Quality regression:** If any primary metric (accuracy, hallucination rate, latency) regresses >5%, block.

**For harness systems specifically:**
- Eval each agent's output independently (does Planner generate valid specs? Does Generator follow spec? Does Evaluator's judgment correlate with ground truth?)
- Run full pipeline eval (can the system complete a full sprint end-to-end without getting stuck?)
- If agent-level evals pass but pipeline evals fail, there's a handoff problem — dig in before shipping.

**Harness Deployment Considerations:** When shipping harness-based systems, deploy agents independently. Roll out planner changes before generator changes. Never change planner + generator + evaluator simultaneously (too many variables, can't debug regressions). Use canary deployments per agent role: planner to 5% → 25% → 100%, validate, then advance generator, then evaluator.

---

## Canary Deployment for AI Features

Don't flip a switch. Ship to 1% → 5% → 25% → 100% while monitoring for quality degradation, cost spikes, or unexpected failure modes.

**Canary thresholds (go/no-go):**
- **Quality:** If error rate at 5% > 10% above baseline, pause and investigate
- **Cost:** If cost per user > 50% above model estimate, pause
- **Latency:** If P95 > 1.5x target, pause
- **Safety:** If flagged outputs spike >2σ, pause immediately (human review)

**Rollback decision:** If any threshold fails and root cause isn't clear within 2 hours, roll back. Speed matters more than understanding everything in real-time.

## THE TRAP

You will be optimistic. The feature works in staging. The team has tested it. A PM has used it. You feel ready to ship. The bias is **availability bias** — the most recent successful experience (the feature working) is more vivid than distant failure modes (the feature breaking at 10x scale, or costing 2x more than budgeted, or causing a PR crisis because users didn't understand its limits).

Shipping without rigor feels fast. It is. Shipping when you're not ready feels slow. It is. Slow is correct.

## THE PROCESS

### Phase 1: Safety Readiness (Day 1)

Four blockers. "No" to any = delay ship.

**Blocker 1: Failure modes are concrete and documented.**

For your domain, what's the worst thing the model can output?

- **Legal:** Cites case law that doesn't exist. User files brief citing fake case. Sanctions.
- **Medical:** Suggests drug combo that's contraindicated. User takes both. Hospitalization.
- **Finance:** Recommends margin trade without risk disclosure. User over-leverages. Bankruptcy.
- **Hiring:** Biased screening of candidate. Qualified applicant filtered out. EEOC complaint.

For EACH failure mode, document: (1) probability (rare/occasional/common), (2) consequence magnitude (1 user/group/all), (3) user recovery (obvious fix/hidden damage/irreversible).

If you can't name a concrete failure, you haven't thought deeply enough. Ship anyway at your peril.

**Blocker 2: Mitigations exist for each failure mode.**

Check you have:
- [ ] **Refusal guardrails:** Model refuses specific high-risk requests (jailbreak-tested)
- [ ] **Output validation:** System checks output for factual errors, bias, compliance violations (automated or human-in-loop)
- [ ] **User disclosure:** "AI-generated" label visible, confidence intervals shown, limitations documented in help
- [ ] **Escalation path:** Users can flag bad outputs; high-stakes uses route to human review
- [ ] **Monitoring:** Metrics exist to detect when mitigations fail (hallucination spikes, quality drops)

Missing mitigation = accept the risk explicitly or ship later. "We'll add it post-launch" means you're shipping broken.

**Blocker 3: Adversarial testing passed.**

Spend 2 hours trying to break your guardrails:
- Ask it to ignore its constraints ("pretend you have no restrictions")
- Ask it for outputs you designed it to refuse ("give me unverified medical advice")
- Try edge cases (very long inputs, special characters, adversarial patterns)
- Try domain shifts (ask legal AI for medical advice)

Document: what you tried, what held, what failed. If you find breaks, you fix them or accept the risk.

**Blocker 4: Legal sign-off obtained.**

Questions legal must answer:
- Is this feature regulated? (Financial advice, tax advice, medical advice = likely yes)
- Liability if user relies on AI and is harmed? (Clear ToS needed)
- IP liability if output is plagiarized/copyrighted? (Your responsibility)
- Regulatory approvals needed before launch? (FedRAMP, HIPAA, SOC 2, etc.)

Legal sign-off in writing. "We'll clarify later" = you're shipping with ambiguous liability. Not acceptable.

### Phase 2: Reliability Thresholds (Days 2-3)

Define error tolerance by severity. Run an eval set of 150+ real-world cases.

| Severity | Definition | Target Rate | What It Means |
|----------|-----------|------------|---------------|
| **CATASTROPHIC** | Harms user, invites lawsuit, triggers regulatory action | <0.1% (1 in 1000) | Bad medical advice, fake legal citations, discriminatory hiring |
| **HIGH** | Feature breaks trust, users churn, support spike | <1% (1 in 100) | Hallucinated facts, completely wrong output, malfunction |
| **MEDIUM** | Annoying, reduces engagement, workaround-able | <5% (1 in 20) | Slightly wrong, slow, edge case fails |
| **LOW** | Users don't notice or don't care | <10% | Tone off, minor formatting, style inconsistency |

**Eval set results (example):**
```
Catastrophic: 0/150 = 0.0% ✓ PASS
High: 2/150 = 1.3% ✗ FAIL (target <1%)
Medium: 8/150 = 5.3% ✓ PASS
Low: 12/150 = 8% ✓ PASS
```

If HIGH or CATASTROPHIC fail: fix via better model, better prompt, or guardrails. Don't ship with these failing.

**Latency threshold:**

Define P50 and P95 latency targets:

```
Target P50: 1000ms
Target P95: 3000ms
Measured P50: 950ms ✓
Measured P95: 4200ms ✗
```

P95 above target? Users will bounce. Load-test with concurrent users and check latency under load.

**Uptime requirement:**

What % of the time must the feature work?

- Consumer product: 99.0% (6 9s of availability = ~44 minutes/month downtime)
- Enterprise product: 99.9% (3 9s = ~45 seconds/month downtime)
- Mission-critical (healthcare, financial): 99.99% (4 9s = ~4 seconds/month downtime)

Your infrastructure should be sized to hit this. If you don't know your current uptime, measure it in staging with realistic load.

### Phase 3: Economics at Scale (Day 3)

Return to your cost model (from cost-model skill). Verify three things:

**1. Unit economics are defensible at 10x scale.**

Current: Cost per user/day = $0.03. Revenue per user/month = $30.
At 10x scale (stress-tested): Cost per user/day = $0.08. Revenue per user/month = $30.

Margin at 10x: -26%. **This is a blocker.** Either improve cost structure, raise prices, or accept the loss as a strategic investment (with board buy-in).

**2. You have cost monitoring in place.**

Set up alerts:
- [ ] Weekly cost tracking (cost per user, total spend)
- [ ] Month-over-month cost growth (flag if cost grew >20% MoM)
- [ ] Cost per unit (identify if cost per call is trending up)
- [ ] Token volume trending (is usage growing faster than expected?)

If you hit a cost alert, there's a runbook. Don't ship without the monitoring infrastructure.

**3. You have a cost kill switch.**

If costs exceed budget by 30%, who decides to disable the feature? Define this in writing before launch. Don't discover it after your $100k monthly overage.

### Phase 4: Observability (Days 3-4)

You cannot manage what you cannot measure. Set up:

**1. Quality metrics:**
- [ ] Output quality (eval set scored daily)
- [ ] Error rate by severity category
- [ ] User satisfaction (upvote/downvote counts on outputs)
- [ ] Hallucination rate (if applicable)

**2. Performance metrics:**
- [ ] P50, P95, P99 latency
- [ ] Availability (uptime %)
- [ ] Error rate (model inference failures, timeouts)

**3. Cost metrics:**
- [ ] Tokens per call (trending up = potential issue)
- [ ] Cost per user
- [ ] Total cost (for budget tracking)

**4. Behavioral metrics:**
- [ ] Usage (DAU, MAU, queries/user)
- [ ] Engagement (how often is the feature used per session?)
- [ ] Retention (users who used it once and never again)

Set up dashboards. Set up alerts. Define who gets paged if metrics degrade. Write a runbook for each alert (what do you do if quality degrades? If latency spikes? If cost explodes?).

Ship without observability infrastructure and you're flying blind.

### Phase 5: User Education (Days 4-5)

Users will misuse your feature. Design for this.

**1. Disclosure:**
- [ ] UI makes clear: [AI Assistant] or [AI-Generated] label visible
- [ ] First-time users see a tooltip: "This is an AI model. Always verify important facts."
- [ ] Help docs explain what the feature does and what it cannot do
- [ ] In-product limitations are shown (e.g., "knowledge cutoff: April 2025")

**2. Expectation setting:**
- [ ] If the feature is not always reliable, say so: "This feature is experimental and may produce incorrect results. Use with caution."
- [ ] If confidence varies, show confidence: "I'm 90% confident in this answer, 40% confident in this answer."
- [ ] If the feature has a narrow domain, say so: "Works best for X. Not designed for Y."

**3. Escalation path:**
- [ ] Users can flag bad outputs (downvote, report)
- [ ] For high-stakes uses, users can request human review
- [ ] Support team has a runbook for handling complaints about AI outputs

Users who understand the limits use the feature better. Users surprised by a failure churn and leave bad reviews.

### Phase 6: Graceful Degradation (Days 5-6)

Plan for failure. What happens when:

**If the AI model breaks:**
- [ ] Feature goes dark (disables itself with "temporarily unavailable" message), or
- [ ] Falls back to deterministic approach (search results instead of summarization), or
- [ ] Human review takes over (slower but reliable)

Pick one. Implement it. Test it. If the model is unavailable, users should see a polite message, not an error.

**If latency exceeds threshold:**
- [ ] Show a loading indicator (users accept delay if they see progress), or
- [ ] Dequeue non-critical requests (premium users get priority), or
- [ ] Show a cached result from a previous session

**If cost exceeds budget:**
- [ ] Throttle feature for lower-tier users, or
- [ ] Add usage limits (e.g., 10 queries/day), or
- [ ] Disable the feature for new users until next billing cycle

**If quality degrades:**
- [ ] Reduce confidence on low-quality outputs, or
- [ ] Route high-stakes uses to human review, or
- [ ] Disable the feature until root cause is fixed

Document each scenario. Assign someone to implement it.

### Phase 7: Launch Checklist (Day 6)

- [ ] Safety review: all failure modes documented, mitigations in place, legal signed off
- [ ] Reliability: error rates measured and acceptable, latency meets target, uptime verified
- [ ] Economics: cost at 10x scale is defensible or accepted, cost monitoring in place, kill switch defined
- [ ] Observability: dashboards live, alerts configured, runbooks written for each
- [ ] Education: users can understand what the feature does, help docs exist, escalation path clear
- [ ] Degradation: failure modes have mitigation plans, fallback behavior is defined, tested
- [ ] Go/no-go meeting: product, engineering, legal, finance agree "yes, ship this"

If all seven are checked, you ship. If any is incomplete, you delay. There is no "ship and fix later" for the top three.

## DAY-1 REVIEW PROTOCOL

The ship decision doesn't end at launch. The first 24 hours reveal whether your pre-launch assumptions hold. This protocol defines what to check, when to escalate, and when to roll back.

**Who runs Day-1 Review:** The PM who owned the ship decision + the on-call engineer. Both must be available for the full 24-hour window.

### The 10 Metrics (Check at +1hr, +6hr, +24hr)

| # | Metric | Where to Find It | Green | Yellow (Investigate) | Red (Escalate Immediately) |
|---|---|---|---|---|---|
| 1 | **Error rate by severity** | Error tracking (Sentry, Datadog) | Critical: 0. High: <0.1% of requests. | Critical: 0. High: 0.1–0.5% | Any critical error. High: >0.5% |
| 2 | **Latency P95** | APM dashboard | Within 20% of pre-launch baseline | 20–50% above baseline | >50% above baseline or >8s absolute |
| 3 | **Cost per user (hourly extrapolation)** | Token/API cost dashboard | Within 30% of modeled cost | 30–80% above model | >80% above model (margin at risk) |
| 4 | **Feature activation rate** | Product analytics | >5% of eligible users tried it (1hr); >15% (24hr) | 2–5% (1hr); 5–15% (24hr) | <2% (1hr); <5% (24hr) — discovery problem |
| 5 | **Acceptance rate** | Output interaction events | >70% of outputs accepted or used | 50–70% accepted | <50% — quality problem |
| 6 | **Hallucination/error rate** | Flagged outputs + spot-check | <3% of outputs flagged | 3–8% flagged | >8% flagged — quality crisis |
| 7 | **Confidence calibration** | User behavior (accept rate at different confidence levels) | High-confidence outputs accepted >85% | Acceptance doesn't correlate with confidence | Users reject high-confidence outputs — calibration is broken |
| 8 | **Support volume** | Support tickets tagged to feature | <0.5% of users file tickets | 0.5–2% file tickets | >2% file tickets in first 24hr |
| 9 | **Rollback health** | Feature flag system | Rollback tested and working | Rollback exists but untested | No rollback mechanism — this should have been caught pre-launch |
| 10 | **Safety incidents** | Safety monitoring, user reports | Zero safety-critical incidents | Flagged outputs caught by guardrails (guardrails working) | Any safety-critical output that reached users |

### Escalation Rules

- **1 Red metric:** Investigate immediately. PM + on-call engineer diagnose within 30 minutes. If root cause is unclear within 1 hour, roll back.
- **2+ Red metrics:** Roll back immediately. Investigate post-rollback. Re-launch only after root cause is fixed and validated.
- **3+ Yellow metrics:** Treat as equivalent to 1 Red. Investigate immediately — multiple yellow signals compound.
- **All Green at +24hr:** Feature is stable. Move to weekly monitoring cadence.

### Day-1 Dashboard Template

```
┌─────────────────────────────────────────────────────────────────┐
│  DAY-1 REVIEW: [Feature Name]           Launch: [timestamp]     │
│  Owner: [PM name]    On-call: [Eng name]  Status: [🟢/🟡/🔴]   │
├─────────────────────────────────────────────────────────────────┤
│  +1hr    │  +6hr    │  +24hr   │  Trend   │  Status            │
│  ───────────────────────────────────────────────────────────────│
│  Errors:     0.02%  │  0.03%  │  0.02%  │  stable  │  🟢     │
│  Latency:    2.1s   │  2.3s   │  2.2s   │  stable  │  🟢     │
│  Cost/user:  $0.04  │  $0.05  │  $0.04  │  stable  │  🟢     │
│  Activation: 8%     │  14%    │  22%    │  ↑       │  🟢     │
│  Acceptance: 74%    │  71%    │  73%    │  stable  │  🟢     │
│  Halluc.:    1.2%   │  1.8%   │  1.5%   │  stable  │  🟢     │
│  Confidence: corr.  │  corr.  │  corr.  │  stable  │  🟢     │
│  Support:    0.1%   │  0.2%   │  0.3%   │  ↑ slow  │  🟢     │
│  Rollback:   tested │  tested │  tested │  ready   │  🟢     │
│  Safety:     0      │  0      │  0      │  clear   │  🟢     │
└─────────────────────────────────────────────────────────────────┘
```

## REALITY CHECK

- **Over-engineering:** Not every feature needs 99.99% uptime on day one. Match rigor to consequence magnitude. A customer-facing feature requires rigor. An internal tool does not.
- **Calendar pressure:** "Launch window closes Friday" is not a reason to ship incomplete safety review. Delay to the next launch window.
- **Team fatigue:** "The team is tired" is not a reason to skip observability setup. Tired teams ship broken features. Invest in setup.
- **Competitive pressure:** "Competitors shipped already" is not a reason to cut corners. You're optimizing for 3 years, they're optimizing for 3 weeks.

## QUALITY GATE

Before launch meeting:

- [ ] **Phase 1:** Failure modes documented + legal sign-off obtained
- [ ] **Phase 2:** Error rates measured + high/catastrophic <target
- [ ] **Phase 3:** Cost model defensible at 10x scale OR board-approved loss-leader
- [ ] **Phase 4:** Dashboards live, alerts configured, runbooks written
- [ ] **Phase 5:** Users understand AI label, limitations, escalation path
- [ ] **Phase 6:** Failure modes have mitigation plans (dark / fallback / degrade)
- [ ] **Go/No-Go:** Product + engineering + legal + finance agree "ship"
- [ ] **Rollback:** Plan exists to disable feature in <30 minutes
- [ ] **Day-1 Review:** Scheduled; someone owns monitoring

## WHEN WRONG

This skill gives bad advice if:

- You're shipping an internal experimental feature with explicit opt-in and automatic rollback. (Lighter process is fine; this process is for user-facing launches.)
- The feature is a short-lived A/B test (30 days max), explicitly marked as experimental, with clear opt-out. (Simpler process is appropriate.)
- You're operating in a startup pre-PMF mode where speed to learn is more important than safety. (Speed wins. But document that you're accepting the risk.)
- Regulatory bodies have explicitly preempted your safety review with their own standards. (Follow regulatory standard, not this one.)

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## GENERATE THE DELIVERABLE

Follow the Deliverable Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11:

1. **Output format matching:** If the grounding questions called for an executive summary, a slide deck, or a specific document type, structure your deliverable accordingly.
2. **Checklist completion:** Ensure all checkboxes from the QUALITY GATE section are addressed in the output. Make it scannable — use the checklist format directly if presenting to a go/no-go committee.
3. **Day-1 Review assignment:** The deliverable should name who owns Day-1 Review monitoring and confirm the dashboard template is deployed.
4. **Rollback clarity:** If shipping with any Yellow flags, the deliverable must make explicit: what will trigger a rollback and who decides.
5. **Sign-off:** The deliverable should have explicit written approval from product, engineering, legal, and finance before it's considered final.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---
name: rtp-agent-risk
description: >
  For every agent: is the value worth the potential harm? And can you pull the plug fast enough? Proportionality analysis (value vs worst-case) + kill-switch design (manual, anomaly-triggered, time-elapsed). If you can't kill it faster than harm cascades, don't deploy it. Use for any agentic system (AI agents, automated workflows, autonomous processes), pre-launch risk reviews, or when debating autonomy levels. Skip for static systems (no autonomous actions) or systems with trivial harm potential.
imports: [stress-test, failure-design, autonomy-spectrum]
---

# Agent Risk

## DEPTH DECISION

**Go deep if:** Designing or evaluating agentic systems, pre-launch risk assessment, or deciding whether to increase autonomy. **Skim to questions if:** Quick screening of whether an agent meets safety criteria. **Skip if:** The system is static (no autonomous actions) or harm potential is truly trivial.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What actions does the agent take autonomously? What's the worst-case outcome? What's the business value?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will approve agents based on "average case" harm, not worst case. The bias is **optimism bias in autonomy** — the assumption that if a system works 95% of the time, it's safe. It's not. The 5% failure case is where catastrophe hides.

The mechanism is insidious: **Harm cascade speed**. Some failures cascade instantly (agent makes one bad decision, millions of dollars move). Others cascade slowly (degraded performance over time, customers gradually leave). Most agent risks are of the fast-cascade variety. You can't contain them once they start.

The trap is most seductive when:
- The system is well-tested in your lab (where it won't fail in interesting ways)
- You have a human override in theory (but not in practice — humans miss the alert or are too slow)
- The worst-case seems unlikely ("what's the probability this goes wrong?")
- Autonomy delivers clear business value (efficiency, speed, cost savings)

### The Amazon Marketplace Scraper (2016-2017)

Amazon's recommendation system uses autonomous agents to scrape competitor prices, adjust product pricing in real-time, and optimize keywords dynamically. Autonomy delivers value: Amazon can optimize thousands of products per hour. Humans can't do this manually.

In late 2016, one category (batteries) had a pricing anomaly. Third-party sellers were flooding Amazon with counterfeit listings. The autonomous agent detected "high-volume listing" as a legitimate tactic (used by authorized resellers) and started cascading price reductions to compete. Within 6 hours, the same product was being listed at $0.01 (the auction was trying to win by volume). Seller margins collapsed. Customers could buy batteries for a cent.

Amazon's revenue in that category dropped 40% that day. A human analyst spotted it, but the agent had already taken thousands of actions. Recovery took weeks of manual corrections.

Worst case: This was a pricing agent. If it had been a delivery agent (autonomously contracting with couriers), a healthcare agent (autonomously approving treatments), or a hiring agent (autonomously extending job offers), the cascade would be worse.

What stopped the damage? Amazon had a **24-hour audit layer** — human analysts who reviewed agent actions daily. The audit caught it within a day. Imagine if they didn't have the audit.

## THE PROCESS

### 1. PROPORTIONALITY TEST

Ask: **"Is the value of this agent worth the worst-case harm?"**

This is a deliberate, numerical comparison.

**Build a proportionality matrix:**

| Dimension | Value | Worst-Case Harm | Proportional? |
|-----------|-------|-----------------|---------------|
| **Revenue at stake** | $10M annual opportunity | $5M loss in catastrophic failure | No. 50% upside, 50% downside if failures aren't caught. |
| **Customer impact** | 5% efficiency gain = faster service | 0.1% false-positive rate = harmful action to 500 customers | Yes. Harm is bounded. |
| **Brand damage** | Not quantified | Headline "AI system harms customers" | No. Reputational harm > financial harm |
| **Regulatory exposure** | Compliant if operating as designed | Non-compliant if agent hallucinates or deviates | No. Risk > reward. |

**Decision logic:**
- If Best Case > Worst Case by 10x+ → proportional, consider it
- If Best Case : Worst Case < 3x → not proportional, don't deploy
- If Worst Case is existential or regulatory → not proportional, period

**Example (AI hiring agent):**
- Value: Hire 500 candidates/year instead of 50 (10x throughput)
- Worst case: Agent discriminates based on protected attributes (gender, race, age), harms 50 candidates, exposes company to lawsuits, regulatory investigation
- Proportionality: No. Regulatory and legal risk > operational upside. Reject autonomy.

### 2. HARM CASCADE ANALYSIS

Ask: **"How fast does damage spread if the agent goes rogue? Where does it stop?"**

Map the blast radius and cascade speed.

**Cascade dimensions:**

**Speed of cascade:**
- **Instant cascade** (seconds to minutes): Agent makes one decision, millions move. Price agents, portfolio trading agents, resource allocation agents.
- **Fast cascade** (hours): Agent's decisions have ripple effects. Delivery agents create cascading service failures. Keyword agents damage SEO over hours.
- **Slow cascade** (days to weeks): Degraded performance, customer dissatisfaction, compounding failures. Content recommendation agents drift toward low-quality content.

**Blast radius:**
- **Single user**: Agent makes bad decision affecting one customer (low blast, high count)
- **Segment**: Agent affects a category or cohort (medium blast)
- **System-wide**: Agent's decision affects the whole platform (high blast)
- **Ecosystem**: Agent's decision affects customers AND partners AND competitors (catastrophic blast)

**Example (supply chain optimization agent):**
- Speed: Fast cascade. Agent routes all shipments through a single carrier for cost savings. Carrier fails. All shipments stuck. 48 hours to realize and redirect.
- Blast radius: System-wide. All customers affected. Not just one segment.
- Propagation: Customers see delayed deliveries, competitors steal market share, recovery takes weeks.

### 3. KILL-SWITCH DESIGN

Ask: **"Can I stop this agent faster than harm cascades?"**

Design multiple, independent kill switches. One human-controlled override is not enough.

**Kill-switch taxonomy:**

**1. Manual kill-switch:**
- Human sees alert, clicks "pause"
- Problem: Humans miss alerts, or alerts are too frequent (cry wolf → ignored)
- Backup: One human seeing the alert isn't enough. You need two people, in separate locations, to activate kill-switch (reduces false-positives from triggering cascade stops)

**2. Anomaly-triggered kill-switch:**
- Agent's outputs deviate from expected range → automatically pause
- Example: Pricing agent sets price below cost → auto-pause
- Problem: You have to predict "expected range" in advance. Unknown unknowns bypass this.
- Backup: Combine with manual review. Auto-pause alerts a human; human reviews in 15 minutes; human decides "resume" or "investigate"

**3. Time-elapsed kill-switch:**
- Agent has maximum runtime (e.g., 4 hours) before it must be manually re-approved
- Example: Hiring agent reviews candidates for 4 hours, then stops and waits for human review
- Problem: If the harm cascades within 4 hours, kill-switch is too slow
- Backup: Use for lower-impact agents. Combine with other switches for high-impact agents.

**4. Scope-bounded kill-switch:**
- Agent can only take actions in a limited scope (e.g., pricing can only change by ±5%)
- Example: Recommendation agent can only choose from pre-approved content pool
- Problem: Scope boundaries are a constraint on value. Agent can't optimize beyond the boundary.
- Backup: Use for high-impact agents. Accept the value trade-off.

**5. Simulation kill-switch:**
- Agent runs in simulation first. Actions are previewed, not executed. Human approves before execution.
- Example: Workflow automation shows "I will send 1000 emails" before actually sending. Human reviews, then approves.
- Problem: Adds latency. Not viable for real-time agents.
- Backup: Use for batch-process agents or low-frequency high-impact decisions.

**Effective kill-switch design combines multiple:**
- Manual (human can stop anytime) + Anomaly-triggered (automatic pause on deviation) + Simulation (preview before execute)
- This triple layer catches failures at different stages

### 4. KILL-SWITCH TESTING

Ask: **"Have I tested the kill-switch? Can I actually stop the agent?"**

Most teams have kill-switches on paper that don't work in practice.

**Testing checklist:**
- [ ] Manual kill-switch: Activates within 5 minutes. Person trained, response time measured.
- [ ] Anomaly kill-switch: Alerts trigger on test anomaly within 1 minute. Alert escalation path tested.
- [ ] Time-elapsed: Agent actually pauses after max runtime. Doesn't keep running past the boundary.
- [ ] Scope boundary: Agent attempts to exceed scope, is blocked, error is caught and logged.
- [ ] Simulation kill-switch: Execution is blocked until approval. No "sneaking around" the simulation step.

**Failure mode:** You test kill-switches in lab. In production, under load, with real data, something breaks. The alert system is slow. The human is asleep. The API call to pause the agent times out.

**Solution:** Chaos test your kill-switches quarterly. Simulate failures, measure response time, measure time from "harm detected" to "agent stopped."

### 5. HARM DETECTION

Ask: **"How do I know the agent is causing harm? What's the alert?"**

Without detection, kill-switches never trigger.

**Detection mechanisms:**
- **Output audit**: Agent outputs reviewed by humans (Pricing agent outputs reviewed daily. Any price < cost is caught.)
- **Anomaly detection**: Agent's output distribution compared to baseline (Agent suddenly starts recommending a different category → alert)
- **Threshold monitoring**: Agent's metrics compared to bounds (Conversion rate on recommendations drops below X% → alert)
- **External signal**: Customer complaints, competitor analysis, partner feedback (Customers report receiving harmful recommendations → alert)
- **Regression test**: Agent tested against known-good scenarios daily (Agent fails 5% of test cases it used to pass → alert)

**Problem:** All detection has false positives (alert triggers on harmless anomaly) and false negatives (harm happens but isn't detected). You need multiple detection mechanisms. No single signal is sufficient.

## DIAGNOSTIC QUESTIONS

Answer these honestly to assess agent risk:

1. **"If this agent went completely rogue for 1 hour, what's the maximum harm?"** Quantify it. Money, customers, brand damage, regulatory exposure.
   - **Red flag:** "We don't know." "It's unlikely to go rogue." (Don't conflate probability with impact. Maximize on impact.)
   - **Sharpening probe:** "Has any agent ever done something unexpected? What was the impact?"

2. **"Can I describe the worst-case failure mode in one sentence?"** If you can't, you haven't thought about it.
   - **Red flag:** "It would just stop working." (That's base case. What about failure modes where it keeps working but wrongly?)
   - **Sharpening probe:** "What would a malicious actor do if they had access to this agent's parameters?"

3. **"How fast would that harm cascade if it starts?"** Minutes? Hours? Days?
   - **Red flag:** "It would spread immediately." "We'd need weeks to contain it." (If it's spreading immediately and takes weeks to contain, autonomy level is too high.)
   - **Sharpening probe:** "At what point in the cascade can a human still intervene?"

4. **"Have I tested the kill-switch? Can I actually stop this right now?"** Test it. Don't assume.
   - **Red flag:** "We have a kill-switch but haven't tested it under load." "It works in staging." (Not the same as production.)
   - **Sharpening probe:** "What's the last time we tested stopping this agent? What happened?"

5. **"If this agent made one catastrophic decision, how would I know?"** What alert would fire?
   - **Red flag:** "We'd see it in the metrics eventually." (Eventually isn't fast enough for fast-cascade harms.)
   - **Sharpening probe:** "If an alert fired right now, who would see it? In what timeline would they act?"

6. **"Is the business value of this agent's autonomy worth the worst-case harm?"** Honest answer only.
   - **Red flag:** "Yes, definitely." (If you're certain, you haven't imagined the worst case hard enough.)
   - **Sharpening probe:** "What would have to be true for you to say no?"

## REALITY CHECK

**Failure modes:**
- **False confidence from testing**: Agent works in test environment. In production, with real data and edge cases, it fails in new ways.
- **Cascading failures**: You designed for single-point failures. Multiple failures happen simultaneously. Cascade is faster than you predicted.
- **Alert fatigue**: Kill-switch alerts fire so frequently that humans ignore them. Automation bias ("the system will handle it") kicks in.

**Cost traps:**
- Manual audit for a high-velocity agent is expensive (10+ FTEs to review millions of decisions daily)
- Scope boundaries limit agent value (can't optimize beyond them)
- Kill-switch testing is recurring cost (quarterly, minimum)

**Monitoring:**
- Track "cascade speed for detected harms" (hours to detection + hours to kill-switch + assessment time)
- Track "false positive rate on kill-switch alerts" (too high = humans will ignore)
- Track "time from alert to action" (should be <30 min for fast-cascade harms)
- Track "% of agent decisions audited" (for high-value agents, should be 100% initially, then sample as confidence builds)

## THE AGENT RISK MATRIX

| Autonomy Level | Consequence Magnitude | Risk Level | Required Controls |
|---|---|---|---|
| **Tier 1 (Advisory)** Agent suggests, human approves | Low (1-10 customers affected) | Low | None beyond normal testing |
| **Tier 1 (Advisory)** Agent suggests, human approves | Medium (100-1000 customers) | Medium | Human review before action, audit trail |
| **Tier 2 (Conditional)** Agent acts, human reviews after | Low | Low | Post-action audit, weekly review |
| **Tier 2 (Conditional)** Agent acts, human reviews after | Medium | High | Anomaly kill-switch, manual kill-switch, daily audit |
| **Tier 3 (Autonomous)** Agent acts, humans don't review | Low | Medium | Scope boundaries, anomaly kill-switch, automatic rollback |
| **Tier 3 (Autonomous)** Agent acts, humans don't review | Medium | **Red zone** | Reconsider. Requires simulation kill-switch + multi-layer detection + fast response protocol. |
| **Tier 3 (Autonomous)** Agent acts, humans don't review | High | **Do not deploy** | No kill-switch can be fast enough. Reduce autonomy. |

## QUALITY GATE

- [ ] Proportionality test completed (value vs worst-case quantified)
- [ ] Harm cascade speed estimated (blast radius and timeline mapped)
- [ ] Multiple kill-switches designed (manual + anomaly + scope bounds, minimum)
- [ ] Kill-switches tested in production-like conditions (not just in lab)
- [ ] Harm detection mechanism specified (how do we know something is wrong?)
- [ ] Response time target for "harm detected" → "agent stopped" defined and measured
- [ ] Autonomy level is proportional to consequence (Tier 3 autonomous only for low-consequence actions)

## WHEN WRONG

This skill gives bad advice when:
- **The system is not autonomous** (human-in-the-loop always, no independent action) — agent-risk analysis is not needed
- **Consequence magnitude is truly trivial** (internal tool affecting <10 people, low financial impact)
- **You have confidence you can bound the agent's behavior completely** (rare, requires formal verification or extremely constrained action space)

## TRADE-OFF LEDGER

BY CHOOSING **proportional autonomy with kill-switches**:
  We are betting on: Harm can be contained if we detect it fast enough.
  We are giving up: Efficiency. Agents with strong kill-switches are slower (reviews, audits, scope boundaries).
  This is reversible within: Autonomy level can increase after months of safe operation. It's not a one-way door.

THE HIDDEN TRADE-OFF:
  Designing real kill-switches forces you to admit you don't fully understand the agent's failure modes. This is uncomfortable. It's also honest. The moment you try to design a kill-switch, unknown unknowns become visible. Some unknowns are worth accepting. Some trigger "don't deploy."

CONFIDENCE: **High**
  What would change our mind: If we saw an agent with no kill-switches that operated safely for years. We've never seen this at scale.

## CONCLUSION

**The recommendation:** Do not deploy autonomous agents in proportion to consequence magnitude without kill-switches. If you can't kill it faster than harm cascades, lower the autonomy level.

**The hypothesis:** We believe that **agents with well-designed, tested kill-switches will catch 95% of harm before cascade completes**, because multiple independent detection and stop mechanisms create redundancy.

**The 3E decision:**
- **Explore:** Run harm cascade analysis + proportionality test (1 week). If worst-case is acceptable, proceed.
- **Exploit:** Design kill-switches (manual + anomaly + scope bounds), test them (1 week), deploy with monitoring.
- **Exit:** If proportionality test fails (worst-case outweighs upside) or kill-switches can't keep pace with cascade, reduce autonomy level or don't deploy.

**The key trade-off:** We're choosing safety redundancy over efficiency. Multi-layer kill-switches are slower than pure autonomy. This is intentional.

**The biggest risk:** That kill-switches look good on paper but fail in production. Test them quarterly under load.

**Assumptions to watch:**
1. Harm cascade can be detected in real-time (test with synthetic faults)
2. Kill-switch can execute faster than harm cascades (measure response time)
3. Proportionality test is based on realistic worst-case (challenge the "it's unlikely" assumption)

**The next action:** Identify worst-case harm scenario for this agent (1 day). Design kill-switch architecture (2 days). Build and test kill-switches (1 week). Measure baseline response time. Deploy.

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).
If this skill connects to downstream skills, also generate the markdown handoff file (if relevant to broader autonomy governance or safety-by-design).

## VISUAL SUMMARY

After completing the primary output, invoke the excalidraw-svg skill to create a single Excalidraw SVG visual summary showing:
- The Agent Risk Matrix (autonomy level × consequence magnitude → required controls)
- Harm cascade timeline (detection lag + kill-switch activation lag + stop lag = total response time)
- Kill-switch architecture (multiple independent kill-switches with overlap)
- Proportionality test visualization (value curve vs worst-case harm curve)

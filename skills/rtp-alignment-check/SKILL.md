---
name: rtp-alignment-check
description: Check if your organization is actually ready for AI — structure, roles, accountability — before spending on technology. 93% of AI failures are organizational, not technical. This skill maps the 5-link chain (Purpose → Strategy → Capability → Architecture → Systems) and finds which one is broken. Use when kicking off an AI initiative, inheriting a stalled project, evaluating why pilots fail to scale, assessing readiness before a major investment, or diagnosing production failures. Do NOT use to delay decisions or as a perfectionist checklist — it's diagnostic, not a maturity model.
---
# Alignment Check

## DEPTH DECISION

**Go deep if:** Planning a major AI investment, joining a team with struggling AI initiatives, or diagnosing why pilots fail at scale. **Skim to questions if:** Quick readiness assessment before greenlight. **Skip if:** Organization has proven AI execution track record and this is incremental capability building.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What problem is this AI initiative solving? Who owns it cross-functionally? What happens if it fails?
2. Route depth: Are you diagnosing an existing failure (Comprehensive) or assessing readiness (Executive Summary)?
3. Identify output format: Word Document, Presentation, or Both?

Then proceed with the skill-specific analysis below.

## DELIVERABLE FORMAT

Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE TRAP

You will assume technology is the constraint. The bias is **availability heuristic** — you can see the technology problem (models, training data, infrastructure), so you assume it's the real problem. But 93% of AI failures are organizational misalignment. Teams with brilliant ML engineers and infinite compute still fail if Purpose isn't clear or Strategy isn't bought by operations.

The trap is most seductive because:
- Technology problems are visible and feel solvable
- Organizational problems are messy and interpersonal
- The business wants to feel like "we just need better engineers"
- Admitting organizational misalignment requires difficult conversations

But here's the mechanism: A technology problem creates one failure mode (the model doesn't work). An organizational misalignment creates cascading failures: the model works but nobody adopts it, or it works but the business model breaks, or it works for one division but alienates another, or it works but compliance rejects it mid-rollout.

## THE 5-LINK CHAIN

Every successful AI deployment requires five links to hold. If any link breaks, the deployment fails, even if the other four are perfect.

### Link 1: PURPOSE
**The question:** Do all stakeholders understand what problem this AI solves, in their own terms?

A aligned Purpose means:
- Executive leadership can state the problem in one sentence without saying "AI"
- Each operating division understands how this AI affects their role
- Finance can articulate the ROI thesis
- The customer feels the urgency
- If asked "why AI specifically, not a simpler solution?", the team has a crisp answer

Signs of broken Purpose:
- "We need AI because our competitors are using it"
- "AI will solve our [vague problem]"
- People in different departments describe the problem differently
- The stated problem doesn't match the actual implementation (e.g., "We're solving customer support efficiency" but the AI is doing churn prediction)
- Purpose was decided by one person and broadcast, not discovered collaboratively

### Link 2: STRATEGY
**The question:** Does the organization have a clear playbook for how AI fits into competitive positioning, customer value, and business model?

A aligned Strategy means:
- Product leadership has defined where AI creates differentiation vs commodity
- Go-to-market team understands which customer segments benefit most
- Sales can explain why this AI matters to a prospect
- Operations has a roadmap for how AI changes workflows (or it has decided not to change workflows)
- Finance has a unit economics model (cost per inference or per user, volume assumptions, cannibalization risk)

Signs of broken Strategy:
- "AI is a strategic priority" but nobody can define what that means operationally
- The AI roadmap exists in a silo, separate from product roadmap
- Sales and support haven't been consulted on adoption risks
- Nobody has thought through what happens if the AI works "too well" (cannibalization of premium services, workforce displacement anxiety)
- The business case assumes adoption will be voluntary and frictionless

### Link 3: CAPABILITY
**The question:** Does the organization have the right mix of skills — both technical and organizational?

Technical capability:
- ML engineers who understand your domain, not just the state-of-the-art
- Data engineers who can build reliable pipelines (garbage in = garbage out)
- Infra engineers who can deploy and monitor models (a laptop model ≠ production model)
- Product managers who understand AI's constraints (probabilistic, not deterministic; latency vs accuracy trade-offs)

Organizational capability:
- Someone explicitly accountable for AI outcomes (not "everyone's responsibility")
- Decision-making authority to override bad AI outputs when needed (not hostage to "the model said so")
- Change management capacity to help teams adjust to AI-augmented workflows
- Governance ability to say "no" to bad AI uses even if technically possible

Signs of broken Capability:
- "We hired an ML engineer and expect them to do ML, infrastructure, and product"
- Nobody is explicitly accountable for outcomes — it's "the team's responsibility"
- Technical people are making strategy decisions and business people don't understand implications
- No one has been authorized to kill a project if the AI isn't working
- The organization has never done large-scale process change before

### Link 4: ARCHITECTURE
**The question:** Is the technical architecture designed for the actual business problem, not the shiniest technology?

Aligned Architecture means:
- The system is designed to fail gracefully (what happens when the AI is wrong? → human escalation, fallback rules, confidence thresholds)
- Monitoring is built in, not added later (you track accuracy, latency, and business outcomes in parallel)
- The architecture assumes the model will drift over time (not stale forever)
- Data flows are tested — you're not discovering "we don't have access to real-time features" at launch
- Privacy and compliance constraints are embedded in the design, not patched on (GDPR, regulations, data residency)

Signs of broken Architecture:
- "We'll worry about monitoring after launch"
- The system has no fallback (if the model fails, everything fails)
- Data isn't flowing from production back into retraining (model degradation is inevitable and undetected)
- Privacy/compliance is a last-minute review, not a design constraint
- The architecture was designed by technical people in isolation from ops/compliance/legal

### Link 5: SYSTEMS
**The question:** Does the organization have the operational processes to keep the AI working over time?

Systems include:
- **Monitoring:** You're tracking model accuracy, latency, fairness, and business metrics in real time
- **Incident response:** When the AI breaks (it will), who investigates? What's the decision tree for rollback vs quick fix?
- **Continuous improvement:** Is there a process to retrain the model, incorporate feedback, test changes before deploying?
- **Feedback loops:** Are you capturing user corrections (when the AI is wrong), and are those corrections flowing back into retraining?
- **Documentation:** Can a new team member understand why this AI exists, what it does, what it doesn't do, and what could go wrong?

Signs of broken Systems:
- "The model is in production and we're not monitoring it actively"
- No one owns incident response — when it breaks, it's chaos
- Retraining happens on a calendar (every 3 months) instead of when the model degrades
- User corrections are logged but not used to improve the model
- Documentation lives in someone's head

## THE PROCESS

1. **Map the five links.** For each link, assess: aligned, partially aligned, or broken?

2. **Identify the weakest link.** Usually it's not technical. Often it's Purpose (unclear problem) or Capability (no one accountable for outcomes) or Systems (no monitoring).

3. **Trace the failure mode.** If [weakest link] breaks, what happens?
   - Purpose broken → team builds the wrong thing
   - Strategy broken → team builds right thing nobody wants
   - Capability broken → team builds something and doesn't know if it works
   - Architecture broken → team ships and then it breaks in production
   - Systems broken → team ships and it slowly degradates without anyone noticing

4. **Prioritize the fix.** The weakest link is the constraint. Technology improvements upstream won't help if the constraint is downstream.

5. **Reorder if needed.** Usually: Purpose → Strategy → Capability → Architecture → Systems. But if Strategy is broken and Capability is strong, sometimes you build Capability while you're fixing Strategy.

## DIAGNOSTIC QUESTIONS

### On PURPOSE

1. **Can the CEO state the problem this AI solves in one sentence, WITHOUT saying "AI"?**
   - Red flag: "We're implementing AI for customer support efficiency"
   - Green flag: "Support staff spend 30% of time on repeat questions. These consume resources and create frustration. The AI should handle the 80% of questions our FAQ already answers."
   - Spectrum anchor: "Poster on the wall" (mentioned but not internalized) → "Every team can articulate how their AI work serves it"

2. **Does every division that will use this AI understand how it affects their role?**
   - Red flag: Sales found out about the product release from the customer, not from the team
   - Green flag: Sales participated in beta, understands limitations, knows how to position it
   - Spectrum anchor: "We didn't tell them until launch" → "They co-designed the rollout"

3. **If you asked the team "why AI specifically, not a simpler solution?", do they have a crisp answer?**
   - Red flag: "Because the competitors are using it" or "We have the compute" or "ML engineers wanted to try"
   - Green flag: "A rule-based system would handle 80% of cases. AI handles the remaining 20% where customer intent is ambiguous and requires judgment."
   - Spectrum anchor: "Aspirational" (sounds good, no real backing) → "Defensible" (we could explain it to a competitor)

### On STRATEGY

4. **Can the product lead draw a 2x2 showing where AI is differentiating vs commodity in your market?**
   - Red flag: They haven't thought about it. Or they have one column (all differentiation)
   - Green flag: "Recommendation accuracy is table stakes now. Our differentiation is in explanation quality and user trust."
   - Spectrum anchor: "Aspirational roadmap" (what we want) → "Grounded in competitive reality" (updated monthly as competition moves)

5. **Has go-to-market thought through which customer segments are actually ready for AI?**
   - Red flag: "All segments. Everyone needs AI."
   - Green flag: "Enterprise customers with in-house data teams will adopt immediately. Mid-market needs more guardrails and documentation. SMB needs human escalation because they can't sustain a data operation."
   - Spectrum anchor: "One-size-fits-all messaging" → "Segment-specific value props and adoption strategies"

6. **Is there a financial model showing how this AI changes unit economics?**
   - Red flag: "We don't have one yet. We'll figure it out after launch."
   - Green flag: "Cost per inference is $0.02. Our current support cost per ticket is $1.50. We can handle 70% of volume at AI, 30% at human. Blended cost drops from $1.50 to $0.95 per ticket."
   - Spectrum anchor: "Aspirational story" (imagine we get it right) → "Stress-tested model" (with pessimistic, base, and optimistic cases)

### On CAPABILITY

7. **Is there one person with unambiguous accountability for AI outcomes?**
   - Red flag: "It's the team's responsibility" or "It's owned by engineering"
   - Green flag: "Sarah owns end-to-end outcomes. She has authority to change the model, the process, or recommend kill decisions."
   - Spectrum anchor: "Diffused responsibility" → "Clear single point of accountability"

8. **If the AI is not delivering value after 3 months, is there someone with authority to kill it?**
   - Red flag: "We already decided to do it, so we have to"
   - Green flag: "Yes, Sarah has executive cover to recommend a pivot or kill if signal shows it's not working."
   - Spectrum anchor: "Committed to the decision regardless of outcomes" → "Willing to change course based on evidence"

9. **Has the organization successfully managed large-scale process change before?**
   - Red flag: "This is our first time. We're hoping the AI sells itself."
   - Green flag: "We've done CRM rollouts and data migrations. We have change management playbooks."
   - Spectrum anchor: "No organizational change experience" → "Seasoned change management team"

### On ARCHITECTURE

10. **If the AI gives a wrong answer, what happens?**
    - Red flag: "It doesn't" or "We're not sure" or "Everything stops"
    - Green flag: "It's escalated to a human who reviews it in 2 minutes. The human's correction retrains the model. We have fallback rules if latency is too high."
    - Spectrum anchor: "Cascading failure" → "Graceful degradation"

11. **How will you know when the model has degraded?**
    - Red flag: "We'll run monthly accuracy checks"
    - Green flag: "We're tracking accuracy, latency, fairness, and business metrics (cost per ticket, resolution rate, customer satisfaction) in real time. Alerts fire if any metric drifts 1 standard deviation."
    - Spectrum anchor: "Calendar-based checks (after degradation happens)" → "Real-time monitoring with alerts"

12. **What data are you NOT going to have access to?**
    - Red flag: "We haven't thought about this"
    - Green flag: "Real-time customer sentiment, because our sentiment API has 2-day latency. Historical competitor data, because we don't have access. So our model is trained on our own data, which creates [known limitation]."
    - Spectrum anchor: "Wishful thinking" → "Realistic constraint mapping"

### On SYSTEMS

13. **When the AI breaks, who investigates and who decides on action?**
    - Red flag: "Probably engineering" or "We'll figure it out"
    - Green flag: "Sarah gets alerted, pulls the accuracy dashboard, determines if it's a data issue or model issue, decides on immediate mitigation (rollback, rules override) vs longer-term fix (retrain). Escalates to exec if we need to pause revenue-impacting features."
    - Spectrum anchor: "Ad hoc chaos" → "Defined incident response"

14. **How will user corrections flow back into model improvement?**
    - Red flag: "We'll log them and retrain once a quarter"
    - Green flag: "Every correction gets tagged, aggregated daily, and if we see 50+ corrections on the same edge case, we trigger a retrain cycle. We A/B test the new model on shadow traffic before deploying."
    - Spectrum anchor: "No feedback loop (model stagnates)" → "Tight feedback loop (model learns from corrections)"

15. **Can a new engineer understand this AI from documentation?**
    - Red flag: "It's in someone's head"
    - Green flag: "Architecture doc with design decisions, failure modes, monitoring setup, and runbook. Model card with training data, performance, known limitations, and improvement priorities."
    - Spectrum anchor: "Tribal knowledge" → "Documented system"

## REALITY CHECK

- **Failure mode of this skill:** Using it to justify delay. "We need perfect alignment before we can even try." No — you need good-enough alignment to start, and you learn by doing. Use this as a diagnostic, not a maturity model.
- **Most common weak link:** Purpose or Capability. Technical teams often skip the "why this AI" conversation and jump to building.
- **Hidden cost:** Organizations often discover broken links mid-implementation, requiring rework. Better to diagnose early.
- **The time-value tradeoff:** 1 week to diagnose the 5 links can save 3 months of building the wrong thing.
- **When to revisit:** Every time the problem statement changes, or after a major operational failure. For normal operations, quarterly check-in.

## QUALITY GATE

- [ ] All 5 links assessed (Purpose, Strategy, Capability, Architecture, Systems)
- [ ] Weakest link identified with specific evidence
- [ ] Failure mode traced (if this link breaks, then X happens)
- [ ] At least one diagnostic question answered for each link
- [ ] Spectrum anchor used (not just yes/no)
- [ ] Recommendation prioritized by constraint (fix the weakest link first)

## WHEN WRONG

- Organization has no interest in organizational work and only wants technical fixes
- Timing is already committed (launch is in 4 weeks) and diagnosis would only add stress
- Organization is in crisis mode and needs quick action, not careful diagnosis
- Team is already fatigued from planning and needs to build something to regain momentum

---

## TRADE-OFF LEDGER

BY CHOOSING to diagnose alignment before building:
  We are betting on: that organizational alignment is the constraint, not technology
  We are giving up: 1-2 weeks of immediate building momentum
  This is reversible within: 2 weeks (you can always start building after diagnosis)

THE HIDDEN TRADE-OFF:
  Diagnosis can surface uncomfortable truths (e.g., "our CEO and CMO disagree on what this AI is for"). Those conversations are hard but necessary. Skipping diagnosis doesn't eliminate the misalignment — it just moves it to launch.

CONFIDENCE: High
  What would change our mind: An organization that has proven track record of AI execution AND is building incrementally on existing capabilities (not a new domain)

---

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. State the recommendation (which link to fix first, what evidence is strongest)
2. Name the key trade-off (building delay vs alignment gain)
3. Acknowledge the biggest risk (organizational discomfort with hard conversations)
4. Define the next action (owner, date, decision point)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram should show the 5-link chain with current status (aligned, partial, broken) for each link, the weakest link highlighted, and the failure mode labeled. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

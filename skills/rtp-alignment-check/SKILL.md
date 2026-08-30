---
name: alignment-check
version: v1.7_latest
description: 'Check if your organization is actually ready for AI (structure, roles, accountability) before spending on technology. 93% of AI failures are organizational, not technical. This skill maps the 5-link chain (Purpose → Strategy → Capability → Architecture → Systems) and finds which one is broken. Use when kicking off an AI initiative, inheriting a stalled project, evaluating why pilots fail to scale, assessing readiness before a major investment, or diagnosing production failures. Do NOT use to delay decisions or as a perfectionist checklist. It is diagnostic, not a maturity model. Pairs with: problem-type (technical fix vs. organizational change), responsible-ai-program (the governance layer), adoption-launch (the people side of readiness).'
imports: []
---

# Alignment Check

## DEPTH DECISION

**Go deep if:** Planning a major AI investment, joining a team with struggling AI initiatives, or diagnosing why pilots fail at scale. **Skim to questions if:** Quick readiness assessment before greenlight. **Skip if:** Organization has proven AI execution track record and this is incremental capability building.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: What problem is this AI initiative solving? Who owns it cross-functionally? What happens if it fails?
2. Route depth: Are you diagnosing an existing failure (Comprehensive) or assessing readiness (Executive Summary)?
3. Identify output format: Word Document, Presentation, or Both?

Then proceed with the skill-specific analysis below.

## DELIVERABLE FORMAT

Before starting, ask for format: Word Document, Presentation, or Both.
Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE TRAP

You will assume technology is the constraint. The bias is **availability heuristic** — you can see the technology problem (models, training data, infrastructure), so you assume it's the real problem. But 93% of AI failures are organizational misalignment. Teams with brilliant ML engineers and infinite compute still fail if Purpose isn't clear or Strategy isn't bought by operations.

The trap is most seductive because:
- Technology problems are visible and feel solvable
- Organizational problems are messy and interpersonal
- The business wants to feel like "we just need better engineers"
- Admitting organizational misalignment requires difficult conversations

But here's the mechanism: A technology problem creates one failure mode (the model doesn't work). An organizational misalignment creates cascading failures: the model works but nobody adopts it, or it works but the business model breaks, or it works for one division but alienates another, or it works but compliance rejects it mid-rollout.

## KEY TERMS (plain language)

- **The 5-link chain** — Purpose → Strategy → Capability → Architecture → Systems; every link must hold, or the AI deployment fails even if the other four are perfect.
- **Re-attachment** — re-creating named ownership one level up (with peer-visible reporting) *before* the old system-by-system ownership is cut, so accountability transfers instead of draining into the platform.
- **Reusable data / context component** — a validated data building block or context bundle built once and consumed by many agents or products.
- **Named owner** — a specific accountable person for a component, not "the team" or "the platform."

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

**Diagnostic — the urgency trap (a Purpose-to-Strategy break in practice).** Ask: is this initiative scoped against organizational purpose, or against whatever is easiest to measure, a dashboard metric, a cost line, an output count? When leaders default to the visible and measurable, every AI initiative gets capped at a faster version of the status quo instead of a real strategic bet. **Why it matters:** Upwork and Workplace Intelligence data, reported in an HBR piece on the urgency trap, found AI-assisted output up as much as 77%, self-reported burnout up 88% in the same population, and regular AI users twice as likely to say they would consider quitting when they cannot connect their AI-assisted work to organizational strategy. **When wrong:** a narrow, genuinely urgent fix, a compliance deadline or a security patch, does not need a strategy chain first. The trap is initiatives that get managed as operational triage while being described as strategic.
*(Source: HBR, on the "urgency trap" in AI strategy, Jul 2026; underlying figures from Upwork/Workplace Intelligence survey data — ◆ company-disclosed, population is the surveyed knowledge-worker sample, read as directional rather than a rate that transfers to any one org.)*

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

**Diagnostic — the shared-component ownership test (AI-platform era).** As enterprises move to a shared data/context platform, ask at this link: *does every reusable data or context component have a named business-side owner with a monthly quality report?* When a platform absorbs the old system-by-system ownership, accountability drains into the platform unless it's re-created one level up *before* the old bindings are cut. Caterpillar re-attached it as 14 named data domains with ~a dozen VP owners and monthly quality reports; peer visibility ("no executive would fund a rival customer database when a peer clearly owned customer data") is what actually killed the sprawl, not a policy document. **Why it matters:** this is the concrete Architecture-link test for the re-attachment move — the shared context component that fifty agents consume needs a single named owner. **When wrong:** it's a diagnostic, not a maturity gate — don't block a launch on it; a small team can legitimately have one owner across many components. The test is "is ownership named and visible," not "is there a VP per object."
*(Source: "Data Transformation Is the CEO's Business," MIT Sloan Management Review, 21 May 2026 — Caterpillar; ◆ 14 domains / ~a dozen VP owners.)*

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

## GATE: THE WRITE-FIRST TEST (run before the diagnostic conversation, not during it)

**The diagnostic below is a conversation, and a conversation is the instrument this failure defeats.** Run this gate first or the five links will all read green.

**The failure has a name and it is not disagreement.** Alignment means people are not in each other's way, which a single meeting and a nod will produce. **Agreement means detailed, explicit compacts that hold under pressure.** Teams routinely have the first and believe they have the second, and the belief survives every verbal check you can run on it.

**The case that shows the size of the gap.** At a North American energy distributor being prepared for sale, executives were asked how the company would change. **10 of 13 said they were clear. 8 of 13 said the team felt aligned.** Then the same 13 were asked to write down, independently, the specific ways the company would be different. Their answers diverged completely: one described a larger but operationally similar company, another framed it as standing alone, a third listed new assets, markets, cost structure, people and leaders. **The instrument that found it was independent written elicitation. No better-facilitated meeting would have.**

**The gate, and it costs one email:**

1. Before any group discussion, each stakeholder **writes down independently**, in their own words, their answer to the Purpose and Strategy diagnostic questions below. Specifics, not principles.
2. Compare the written answers for divergence **before** convening.
3. Run the group session on the divergence you found, not on the questions.

See `rtp-adoption-launch` for the false-alignment test, a pre-flight instrument for exactly this kind of performed-versus-real agreement.

**Why verbal checks cannot substitute.** Two biases compound. The **false consensus effect** makes people overestimate how widely their own view is shared, so nobody thinks to test it. **Affective forecasting error** makes people overestimate how unpleasant a disagreement will feel, so they avoid triggering one. Leaders therefore assume agreement exists and avoid the check that would reveal otherwise. A third cause is pure schedule pressure: differences get deferred on the belief that clarity arrives once execution starts, and it compounds instead.

**What this changes elsewhere in the skill.** The Trade-off Ledger prompt about a CEO and CMO disagreeing on what the AI is for stops being something the facilitator watches for in the room. **Watching for it in real time is the failure mode.** It becomes the specific thing the write-first gate is built to surface before anyone gets in the room.

**The general rule underneath, and it is worth carrying past this skill.** Any claim of shared state between independent reasoning parties, human executives or AI systems, **is false by default until tested against an out-of-band, individually-elicited comparison.** Verbal consensus is not evidence of shared state. It is the artifact that consensus-testing exists to interrogate. The machine version of the same failure is a group of agents converging on identical answers because they read the same public signals, each one appearing independent (see `rtp-moat-finder`, the anti-moat loop, and `rtp-bias-spotter`, ideation bubbles). Humans produce false convergence-blindness; machines produce false difference-blindness. Neither is visible without an independent baseline.

**One addition to the Systems link: declare who decides, before the discussion starts.** Naming the decision-maker stops two failures at once. Conversations drift toward decisions nobody in the room has authority to make. Or they end with no decision at all.

The sharpest form is one question: **does anyone here have the authority to block or override this?** Declaring a block right at the start is the difference between a decision and an ambush. An undeclared one is a Systems break that surfaces months later as rework.

**One more site for the write-first gate: the three sites of disagreement.** Cross-functional IT-and-AI conflict rarely runs on a disagreement about facts. In three anonymized advisory cases, the standoff resolved the moment both sides agreed on a classification scheme, not before, and the action that followed needed no further negotiation. Disagreement clustered in three specific places:

- **Definitions of data.** What counts as data at all, and where it starts and stops.
- **Definitions of competence.** Which taxonomy an object belongs to, and therefore which team's judgment governs it.
- **Definitions of the foundation.** Which dependency tier a use case sits on, and what breaks if that tier changes.

The mechanism: each function already has a competent process tied to its own category system. Reclassifying a contested object into a category the other side already trusts moves competence across without anyone having to learn a new skill, which is cheaper than training and cheaper than filing an access request. Add these three as write-first questions alongside the Purpose and Strategy ones above. **Falsifier:** a case where both sides agree on classification using shared terms and still cannot agree whether to proceed. That would show the dispute was substantive, not definitional, and this diagnostic would not apply.

**A blind spot this skill's own check can miss: the common-parent settlement.** Two functions in conflict can both escalate privately to the manager they share, who resolves each side in a separate conversation. No memo exists, no shared decision record, nothing an org chart or a formal escalation log would show. An alignment check that reads reporting lines will call this resolved, because on paper it is: there is a decision-maker and a decision got made. What is missing is an accountability artifact either side, or anyone else, can point to later. This is invisible to any check that only looks at reporting-line structure, not because the structure is hidden, but because the structure alone cannot show whether the decision was ever made visible to both sides at once. The fix is the same write-first habit: put the decision and its reasoning in writing to both sides at once, not in two separate rooms.

**One addition to the Capability link: the Readiness Triad.** An external instrument worth borrowing, naming three conditions execution needs:

- **Appetite.** People are committed and experience the outcome as theirs to shape.
- **Capacity.** The organization has the bandwidth, focus and resilience to sustain the work.
- **Skillset.** Current capabilities match the work as it actually is, not the role on paper.

Two things about it are useful beyond the mnemonic:

- **It is not three parallel checks.** All three must hold, and the framework gives no partial-credit case, no ordering and no weighting. Treat a missing leg as a stop, not as a score.
- **Capacity is created by removing work, not by adding people.** Of the four standard moves for creating it (postpone a competing initiative, clarify who owns decisions, shift resources to what matters most, protect uninterrupted thinking time), three take work away. A readiness plan that adds headcount and postpones nothing has not created capacity.

**One more addition to the Capability link: the accountable-vs-able 2x2.** Cross who is accountable for a decision against who is actually able to alter its outcome. Four cells result, but only one is dangerous: accountable but not able, where someone answers for a result they cannot actually change. Check this cell whenever AI has moved decision power upstream or downstream from where accountability still sits, for example a team lead accountable for a queue's resolution time but unable to adjust the model-routing rule that sets it. Treat the 2x2 as a prompt for the write-first conversation, not as a scored assessment.

**One more addition to the Capability link: the trust-readiness check.** Before any AI tool rollout, ask whether organizational trust is high enough for logging to read as support rather than surveillance. A survey of 604 daily AI-using US employees found organizational trust was the strongest predictor of employees intentionally withholding AI-related knowledge from coworkers or their employer, independent of job insecurity or whether a formal AI policy existed. The counterintuitive part: where trust is already low, giving employees access to sanctioned, approved AI tools increases hiding instead of reducing it, because the logging reads as evidence-gathering against the employee, not as support. Add trust readiness as a check before any rollout, alongside training, budget, and technical fit: a rollout planned without it risks growing shadow AI use rather than shrinking it, and no checklist that only asks about training, budget, or technical fit will catch this gap. **Falsifier:** an organization that rolled out heavily logged AI tooling into a documented low-trust environment and saw shadow use decrease rather than increase.

**One more addition to the Capability link: readiness preconditions before a transformation or shock (capability-before-crisis).** Two sources point at the same underlying pattern from opposite directions: capability has to exist before the test arrives, not get improvised during it.

The first is infrastructure-level. UNHCR spent eight years decentralizing decision rights and building an innovation office before an 18-month funding shock hit in 2025-2026; over the decade its budget grew roughly 40% while the population it served roughly doubled. "Do more with less" only holds while the efficiency infrastructure built during the calm years still has a lever left to pull. Once the shock arrived with no lever left, it became "do less with less," which is what eventually happened even at an organization that had done the prep work. Add a time-boundary test as a diagnostic: was this capability operating and load-bearing before the disruption, or would it have to be improvised during it? **Falsifier:** an organization that built genuinely new capability fast enough, mid-shock, to matter. If that turns out to be common rather than rare, this test needs revising.

The second is organizational-readiness level, and applies the identical pattern to individuals. An HBR piece on AI transformation and mindset cites GDPval, an OpenAI benchmark tracking agentic-model parity with human experts on professional tasks, at roughly 80%, up from 50% six months earlier; that figure could not be independently confirmed against the primary source in this pass, so treat it as reported, tier ⚠, not verified. Before telling someone to stop defending their old skillset and rebuild around judgment, three organizational preconditions have to exist first: radical, not incremental, transformation targets; evaluation infrastructure built before scaling a deployment; and unified data as a gate before rollout. Skip these and the individual mindset shift exposes the person asked to make it, rather than protecting them, because the organization has not actually changed what it rewards or how it catches mistakes. **When wrong:** a small, non-critical pocket of the organization with low downside from an early individual shift does not need all three preconditions locked in first; the checklist matters most where the individual is being asked to bet their standing on a judgment call the organization has not yet backed with infrastructure.

**One more addition to the Capability link: senior hiring and promotion criteria, one level up.** As AI commoditizes demonstrable hard expertise, senior hiring and promotion criteria shift from technical expertise toward judgment, learning speed, and orchestration capability. This is the same logic this skill already applies at the individual level, moved up to who gets hired and promoted into leadership. Add one diagnostic question: does senior hiring or promotion in this organization still weight demonstrated technical expertise over judgment, learning speed, and orchestration capability?

The source is an executive-search firm's analysis of more than 5,000 job descriptions, presented by the firm's own chief science officer; tier ⚠, a single firm with a commercial interest in the answer, not an independent study. A five-stage board-maturity model from the same analysis is included here as context: Luddite, hygiene-factor use, AI-ready processes, agents as board participants, and full delegation, with an "unknown unknowns" stage as the apex beyond all five. It has no existing home elsewhere in the skill library, so it stays compact here rather than fully developed. **When wrong:** for execution-heavy technical roles below the senior tier, weighting demonstrated technical expertise is often still correct; this diagnostic targets senior hiring and promotion specifically, not hiring in general.

*(Sources: the write-first gate and the 10-of-13 case, HBR, Dhar, Ellmer & Jameson, "The False Alignment Trap," Aug 2026 — ◆ author-disclosed single case at an unnamed North American energy distributor, the article's own field observation rather than a published study. **This is the single most load-bearing number in that piece and the whole construct rests on it; treat it as illustrative case evidence, not a rate.** The underlying biases are named third-party research (Ross on false consensus, Minson on affective forecasting). The decision-maker declaration, HBR, "How the Best Leaders Shape Conversations," Aug 2026 — ◆. The Readiness Triad, HBR, Morris, Aug 2026 — ⚠ weakest evidence rung, a consultant selling his own named framework, three of five illustrations unnamed composite clients; the distinctions hold up, the framework carries no outcome data. The three sites of disagreement and the common-parent blind spot, HBR piece on AI-and-IT-team conflict, Jul 2026 — three anonymized advisory cases with no outcome measures; cite the mechanism, not a result. The accountable-vs-able 2x2, HBR, "3 Questions to Pressure-Test Your Priorities," Jul 2026 — ⚠ weakest evidence rung, n=10 from a single workshop; a useful lens, not a validated instrument. The trust-readiness check, HBR, Anicich & Brouwers, "Why Employees Aren't Transparent About Their AI Usage," 10 Jun 2026 — ◆ survey of 604 daily AI-using US employees, self-selected into daily AI use, US-only, self-reported; the trust-quartile gap (47% hiding at lowest trust vs. 14% at highest) is the study's own finding, and the tool-amplification moderation is correlational within a cross-sectional survey, read as directional rather than a rate that transfers to any one org. The readiness-preconditions pair: the UNHCR time-boundary case, an interview with a UNHCR executive (Clements), 2025-2026 — ◆ company-disclosed figures, unaudited, a single organization's own account. The three organizational preconditions and the GDPval figure, an HBR piece on AI transformation and mindset, 2026, exact publication date not given in the source note — the GDPval "roughly 80%, up from 50%" figure is reported, not independently verified in this pass, tier ⚠. The senior hiring and promotion shift and the board-maturity model, an executive-search firm's analysis of 5,000+ job descriptions, 2026, exact publication date not given in the source note — ⚠, single firm, self-interested, presented by the firm's own chief science officer. The false-alignment test pointer above cites a separate HBR piece on transformation-leadership skills; its full citation lives in `rtp-adoption-launch`, not here.)*

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

## RESILIENCE IS THE RESIDUE OF WORK DONE BEFORE THE SHOCK

**You cannot build resilience during the crisis. What you have when the shock lands is whatever the efficiency work of previous years left behind.**

The case that makes it concrete: a large humanitarian organization ran an eight-year transformation before a sustained eighteen-month funding contraction hit. Decentralized decision rights. Shared services with a partner agency. Cash-based assistance replacing in-kind aid. A formal innovation office with an accelerator. **None of it was done for the contraction. All of it was what made the contraction survivable.**

**The argument is made by sequencing rather than stated as a thesis**, and it is worth stating: organizations that wait for the crisis to start reforming arrive with weaker tools, and their slogan degrades from "do more with less" into "do less with less."

**What this changes about an alignment check.** The chain diagnoses whether purpose, strategy, capability, architecture and systems currently line up. **Add one question about time: which links were built recently enough that they have not yet been tested, and which were built years ago and have already survived something?**

- **Decision rights that have never been exercised under pressure are not decision rights.** They are a document.
- **A capability funded this year is an intention. A capability that survived a budget cut is a capability.**

**The practical version, and it is uncomfortable:** the reforms most worth doing now are the ones with no current forcing function, because a forcing function means you are already late. **A reform proposed during good conditions has no urgency behind it and is exactly the one that will matter.** That is a hard case to make, and knowing it is the case is most of what makes it makeable.

*(Source: an HBR IdeaCast interview with a UNHCR leader on organizational transformation, Jun 2026 — ⚠ single-organization practitioner narrative. **The article names no framework and states no thesis**; the sequencing argument above is this corpus's reading of the account, and there is no counterfactual for what would have happened without the eight years of prior work. Falsifier: an organization that built comparable resilience during a contraction rather than before it.)*

## WHERE YOUR BOARD SITS DECIDES WHICH ALIGNMENT IS EVEN AVAILABLE

An alignment chain has to terminate somewhere, and for anything strategic it terminates at the board. **Five stages describe where a board can be, and each one supports a different ceiling on what you can align to.**

1. **AI is peripheral.** Traditional governance rituals, static reporting, human-only deliberation. **Framed as stability and functioning as slow obsolescence.**
2. **Generative AI as hygiene.** Directors use it to summarize materials, stress-test assumptions, prepare for meetings. The comparison the author draws is email or spreadsheets: table stakes, not differentiation.
3. **AI-ready governance.** It is inside the core processes, scenario planning, risk modelling, CEO evaluation, capital allocation. Directors use it to augment judgment rather than only to save time.
4. **Agents as participants.** The system moves from tool to actor, generating alternative strategies and acting as an independent voice, without formal voting rights.
5. **Governance handed over.** The stated dystopian endpoint, named by the author as a warning rather than a forecast.

**How to use it, which is not as a maturity score to chase.** Stages 1 and 2 are the common ones and the practical read is this: **at stage 1 or 2, a strategy that depends on the board understanding AI-specific risk is not alignable, and you should design the chain so it does not depend on that.** Put the AI-specific judgment in a body that has it and bring the board a business decision.

**The parallel shift one level down, which is more actionable.** Job-description analysis across 2019 to 2025 shows what senior roles are being asked for. **CFO descriptions trend up on data analytics, AI and machine learning, cloud and security. CHRO descriptions trend up on workforce analytics, human-AI collaboration design, and the ethical governance of AI in talent decisions**, while HR operations, compliance and traditional performance cycles trend down toward table stakes.

**The alignment consequence: the person across from you is being evaluated on different things than they were three years ago.** A CHRO now measured on human-AI collaboration design is a different counterpart from one measured on program delivery, and an argument pitched at the old scorecard will land as irrelevant even when it is right.

**The claim underneath all of it, worth stating plainly because it is the article's thesis:** AI commoditizes hard expertise, so the traits that differentiate a leader move to learning speed and judgment quality. **The best leaders of this era will not be the ones who know the most.**

*(Source: an HBR piece on how C-suite and board roles are being reshaped around AI, Jun 2026 — ⚠ argument-tier for the pyramid, which is the author's own model with no measured population and a stated forecast date rather than evidence. **The CFO and CHRO skills-shift tables are the stronger part**: ◆, from a Russell Reynolds analysis of job descriptions, 2019 against 2025. Falsifier: boards observed moving through these stages out of order, or skipping straight from stage 1 to stage 3.)*

## WHO IS ACTUALLY IN THE ROOM, AND HOW LONG THEY WILL BE THERE

Alignment work assumes the people you align with will still be there to hold the line. Three findings say to check that assumption before you spend the political capital.

**A new CEO resets the room inside four years, and the reset is not evenly distributed.** In S&P 500 companies, CEO tenure averages 7.8 years, the longest of any C-suite role, and most CEOs replace most of their team within four years of arriving. At least one in five CFOs, CHROs and CMOs turn over in the first year alone. Within four years, more than a third of chief legal officers, 42% of CTOs and 39% of chief supply chain officers have also gone.

**What that changes about a multi-year alignment.** A strategy chain anchored to a specific executive's sponsorship has a half-life you can estimate. **If a CEO transition is underway or likely, an alignment built on personal sponsorship is a depreciating asset and an alignment built into a controlled document, a budget line or a committee charter is not.** That is not cynicism about relationships. It is knowing which artifact survives the person.

**Where those people come from, which tells you what they will respond to.** Roughly 59% of S&P 500 functional leaders are internal promotions, rising to 80% for COO, with long tenure behind them. Of the external hires, 57% held the identical title somewhere else, rising to about 75% for CFO. Industry match matters much less than role match. **The read: your internal audience is arguing from institutional memory, and your external hires are arguing from how the same job worked at their last company.** Those two need different evidence. The internal hire wants to know what has changed since the last time this was tried here. The external hire wants to know why this company is different from the one they came from.

**The composition of the room is not the same as the composition of the argument.** Field research on team performance finds that a mix of personality types beats a room of similar people, but only when the differences are surfaced rather than smoothed over. The default failure is a team that resolves difference by deferring to the loudest consistent voice, which is a room that produces alignment on paper and no examination underneath it. **The check: in your last three alignment sessions, did anyone change position? If nobody moved, you did not run an alignment, you ran a briefing.**

*(Sources: HBR, "How People Actually Get to the C-Suite in S&P 500 Companies," May 2026, analyzing Spencer Stuart's S&P 500 C-Suite Snapshot 2025 — ✅ audited against the primary snapshot for the internal-promotion and role-match figures; the 16-year internal-tenure figure is ⚠ not visible in the public snapshot [VERIFY]. Plus HBR, "How Strong Teams Leverage Different Personality Types," May 2026, ⚠ argument-tier. Falsifier: a CEO transition after which the predecessor's strategy chain held without being written into a controlled document.)*

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

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. State the recommendation (which link to fix first, what evidence is strongest)
2. Name the key trade-off (building delay vs alignment gain)
3. Acknowledge the biggest risk (organizational discomfort with hard conversations)
4. Define the next action (owner, date, decision point)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram should show the 5-link chain with current status (aligned, partial, broken) for each link, the weakest link highlighted, and the failure mode labeled. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

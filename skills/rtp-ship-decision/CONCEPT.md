# Ship Decision — Concept Guide

## FIRST PRINCIPLES

Software ships when it's "done enough." Done enough is defined by engineering excellence, not business readiness. A deployed system is running; it doesn't crash; it returns results. Ship.

AI features require a different gate. AI features can deploy and run without crashing, but still cause harm. The system can return results that are plausible, confidently stated, and entirely false. It can work beautifully for 99% of cases and catastrophically fail for the 1% that matters most.

The atomic insight: **AI features require a post-engineering gate — a business and safety gate — before they touch users. Deploying an AI feature is not the same as shipping a feature.**

## DUAL DEFINITION

**Business definition:** The ship decision is a go/no-go governance process that verifies an AI feature is safe for production users, reliable within acceptable error thresholds, economically sustainable, observable if it breaks, understandable to users, and gracefully degradable if it fails. It's the final handoff from engineering to product operations.

**Technical definition:** A seven-phase review covering safety (mitigation completeness, adversarial testing, legal), reliability (error rates by severity, latency thresholds, uptime targets), economics (unit cost at scale, cost monitoring, budget constraints), observability (quality/performance/cost metrics and alerting), user education (limitations disclosure, confidence calibration), graceful degradation (failure modes and fallback behavior), and a formal go/no-go meeting before deploy-to-production.

## THE TRAP (Expanded)

**The "Works in Staging" Assumption.** You test the feature with intended use cases, friendly inputs, and expected query patterns. It works beautifully. You imagine: "Users will use it this way." They won't. Users will:

- Ask questions the model was never trained to handle
- Try to break the guardrails ("pretend you have no restrictions")
- Use the output in ways you never intended (relying on it for decisions you explicitly said not to)
- Test edge cases (very long inputs, special characters, adversarial patterns)
- Expect reliability you never promised

Staging is biased toward success because you control the test cases. Production is biased toward failure because you don't.

**The Confidence Trap.** The team has used the feature extensively. It feels reliable. But you've tested with benign, expected inputs from users who understand the limitations. In production, you'll have:

- Users who don't read the disclosure
- Users asking the feature to do things it was explicitly designed not to do
- Users making high-stakes decisions based on the output
- Users from different cultures, domains, and backgrounds (distribution shift)
- Adversarial users trying to break it

A 99% accuracy rate sounds reliable. But if a million users call it a million times, that's 10,000 failures. If even one of those causes user harm, you have a PR crisis and potential liability.

**The Observability Blindness.** You ship the feature. It's live. Users are using it. You have no dashboards, no alerts, no way to know if output quality is degrading. Three weeks later, someone notices users are complaining in support. You have no logs to understand what happened. You release a fix. You still don't know how many users were affected or how long the problem lasted.

Without observability, you're operating in the dark. Problems compound before you detect them.

**The Liability Assumption.** You assume: "If the AI makes a mistake, the user should know better than to rely on it." Law doesn't work this way. If you've labeled it [AI], but the output is confident and specific, courts may hold you liable for misrepresentation if a user relies on it and is harmed.

The bar for "user should have known better" is high. The bar for "you should have disclosed limitations more clearly" is low. Clear disclosure, confidence calibration, and escalation paths are not niceties — they're liability reduction.

## INTELLECTUAL LINEAGE

- **SRE Playbook (Google)** — Error budgets, SLOs, and the principle that reliability is engineered, not hoped for.
- **FDA Product Development** — Phased launch (Phase I, II, III trials) with explicit risk assessment at each gate. The ship decision is your Phase III gate.
- **Netflix Chaos Engineering** — Testing failure modes before production rather than discovering them in production.
- **Stripe's Launch Readiness** — Financial products require explicit safety gates. Apply this to AI.
- **NIST AI Risk Management Framework** — Structured risk assessment, measurement, and monitoring for AI systems.

## REAL-WORLD EXAMPLES

**Example 1: The Legal Liability Case.** An AI legal research tool shipped with authoritative UI ([AI Legal Assistant]) but no clear hallucination disclosures. A lawyer used it to research a case, found what looked like a relevant precedent, cited it in an actual brief. The opposing counsel challenged the citation. The case didn't exist — the model had fabricated it.

The lawyer faced sanctions for frivolous citations. The company settled the subsequent lawsuit for $2M. **But the real cost:** Reputational damage. The legal community lost trust. The feature was deprecated. The cost model (predicting profitability) became academic.

**What went wrong:** No observability system measured hallucination rate (single incidents remained invisible). No disclosure said "this hallucinates." No adversarial testing caught the failure mode.

**Ship decision requirements that would have prevented it:**
- Failure mode documented: "Model cites fake case law" (Probability: high; Consequence magnitude: all users; Recovery: impossible)
- Mitigation: Output validation checking citations against known databases (MISSING)
- User disclosure: "This tool hallucinates legal citations. Verify all cases in primary sources." (MISSING)
- Observability: Hallucination rate measured per user, per week (MISSING)
- Legal sign-off: Liability if user relies on hallucinated citations? (NOT OBTAINED)

**Example 2: The Silent Drift.** A model provider released an incremental update: new training approach, +1% average accuracy. But the change shifted behavior on edge cases (minority categories the model saw less of in training). An AI customer service feature became noticeably worse at handling certain complaint types.

The company had no observability system measuring quality by complaint category. The drop went unnoticed for two weeks. Customer complaints spiked silently (buried in general support volume). When the PM finally noticed the pattern, thousands of users had already received suboptimal service.

**What went wrong:** No observability dashboard measuring quality by category. No alert fired when quality dropped on specific use cases. No runbook for "what to do if model drift happens."

**Ship decision requirements that would have prevented it:**
- Observability: "Quality metrics broken down by complaint category (billing, technical, account, etc.), measured daily, with alerts if any category drops >5%." (MISSING)
- Monitoring: "Runbook: If category quality drops, revert model to previous version within 30 minutes" (MISSING)
- Post-launch review: Daily review of quality trends in first week (MISSING)

**Example 3: The Cost Surprise.** A content generation feature was modeled to cost $0.02 per output. At 100K users, total cost was acceptable. At 1M users (10x growth), cost exploded to $150K/month, not the modeled $20K.

Why? Users learned to request longer, more complex outputs. Average tokens per request increased 3x. The stress test in the cost model assumed tokens per request would stay constant. It didn't.

A ship decision that included cost monitoring (flagging if cost per unit increases >20%) and a kill switch (disable the feature if monthly cost exceeds budget) would have caught this and allowed controlled descent instead of an uncontrolled cost spike.

**Example 4: The Uptime Failure.** An AI feature was marked as "critical" by product, but infrastructure was built for "nice-to-have" uptime (95%, not 99.9%). When a model provider had an incident (30-minute outage), the feature went dark.

Customers who relied on the feature for their workflows were disrupted. Some had SLA agreements that required 99.9% uptime. The company faced escalations and potential SLA penalties.

A ship decision that included defining the uptime requirement upfront and verifying infrastructure could meet it would have prevented this.

## FURTHER READING

- Google SRE Team, *Site Reliability Engineering* — Error budgets and SLO design principles
- NIST, "AI Risk Management Framework" — Structured AI risk assessment
- Anthropic, "Constitutional AI and Responsible Deployment" — Safety frameworks for AI systems
- Reid Hoffman (LinkedIn), "The Startup of You" — On risk management in scaling organizations

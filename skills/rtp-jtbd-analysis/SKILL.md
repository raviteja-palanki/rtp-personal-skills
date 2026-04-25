---
name: rtp-jtbd-analysis
description: >
  Demand-side Jobs-to-be-Done analysis for AI features — the structural reframe
  most PMs miss. Use when teams jump from "build X" to "ship X" without naming
  what users are actually hiring the AI to do. Runs the four-forces diagram,
  the switch interview script, and the surface-job vs hidden-job map. Output
  is a job statement plus a design implication, not a 40-page customer empathy
  deck.
imports:
  - problem-ai-fit
  - first-principles
  - uncertainty-research
---

# JTBD Analysis

Decipher what users are actually hiring an AI feature to do — and design for the hidden job, not the surface one.

> "People don't want a quarter-inch drill. They want a quarter-inch hole." — Theodore Levitt, often misquoted but still right.
>
> The 0.1% AI PM correction: people don't want the hole either. They want the picture on the wall. They want the partner to feel proud. They want the room to feel done.

---

## DEPTH DECISION

**Go deep if:** A new AI feature is being scoped, an existing AI feature has flat adoption despite working as designed, or the team is debating "what should this AI do?" before they've named what users are hiring it for.

**Skim to the four forces if:** You already have a job statement and just need to test whether switching forces are strong enough to drive adoption.

**Skip if:** The feature is a commodity (procurement-driven B2B buys, regulated must-haves, contract renewals — see RED TEAM), or the user has no choice in the matter (mandated tools, captive workflows).

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like?**
> 1. **Word Document** — Job statement, four-forces diagram, surface vs hidden job map, design implication. Best for spec reviews and PRD appendices.
> 2. **Presentation** — Visual deck for stakeholder alignment. Best for kickoffs.
> 3. **Inline** — Text output ready to paste into a PRD. Best for fast iteration.
>
> *Default if no preference: Inline.*

---

## THE STRUCTURAL INSIGHT

Bob Moesta's demand-side reframe says: people don't buy products, they hire them to do a job. Most PMs stop there. They write a "job statement," call it customer-centric, and move on.

**The 0.1% AI PM angle: AI changes the job being hired.**

Users don't hire AI for the surface task. They hire it for cognitive offloading, decision deferral, social proof, or anxiety reduction. The functional job is the cover story. The hidden job is the actual demand.

| Feature | Surface Job (what user says) | Hidden Job (what AI is hired for) |
|---|---|---|
| GitHub Copilot | "Complete my code" | "Feel less alone while coding. Stay in flow. Avoid the shame of asking a stupid question on Stack Overflow." |
| ChatGPT for writing | "Draft this email" | "Defer the decision about tone. Get permission to use these words. Lower the activation energy." |
| Notion AI summarize | "Summarize this doc" | "Avoid reading 40 pages. Have a defensible answer if my boss asks 'what's in there?'" |
| Predictive maintenance dashboard | "Predict when the asset fails" | "Have a defensible audit trail. Avoid being the operator who 'should have caught it.'" |
| AI-powered legal review | "Find risky clauses" | "Outsource the blame if I miss something. Reduce the cognitive load of reading dense contracts." |

The product manager who designs for the surface job ships a feature that works on the demo and dies in production. The one who designs for the hidden job builds something users defend even when it's wrong.

**Why this matters specifically for AI:** every other product category competes on capability. AI competes on whether the user trusts you with their cognitive load. The hidden job is almost always about emotional regulation, social positioning, or anxiety reduction — and AI is the first technology that reaches those layers directly. Miss the hidden job and you're competing on benchmarks. Hit the hidden job and you're competing on relationship.

---

## THE FOUR FORCES

Bob Moesta's force diagram. Switching is rational only when push + pull outweigh anxiety + habit. For AI features, anxiety is usually the dominant force — and most PMs ignore it.

```
                    THE SWITCH
                        │
        ┌───────────────┼───────────────┐
        │                               │
    PUSH FORCES                    PULL FORCES
    (away from current)            (toward new)
        │                               │
        │  • Current solution is        │  • New solution promises
        │    failing in a specific way  │    a specific better outcome
        │  • A new event made it        │  • Someone they trust uses it
        │    intolerable (cost spike,   │  • The story of the new
        │    new boss, audit, etc.)     │    solution feels true
        │                               │
        └───────────────┬───────────────┘
                        │
                    [SWITCH HAPPENS]
                        │
        ┌───────────────┼───────────────┐
        │                               │
    ANXIETY                          HABIT
    (about new)                      (of current)
        │                               │
        │  • What if AI hallucinates?   │  • Muscle memory of old tool
        │  • What if my boss audits     │  • Sunk cost in current setup
        │    the AI's recommendation?   │  • Fear of looking stupid
        │  • What if I lose the skill?  │    while learning new
        │  • What if I'm liable?        │  • Team isn't ready
        │                               │
        └───────────────────────────────┘

           Rule: PUSH + PULL > ANXIETY + HABIT
           For AI features: ANXIETY is usually 2-3x larger than PMs assume.
```

**The trap most PMs fall into:** they spend 90% of design energy on PULL (how good the AI is) and 10% on ANXIETY (what could go wrong, who is liable, what happens if it's confidently wrong). For enterprise AI, the ratio should be inverted. The pull is real but anxiety is what blocks adoption.

**A working rule for enterprise AI:** if you can't name the top three anxieties in one sentence each, you haven't done the job analysis. Reread the four forces and try again.

---

## SWITCH INTERVIEW METHODOLOGY

The classic JTBD switch interview reconstructs the timeline from "thought of switching" to "first use." For AI features, you're hunting for the moment the user decided to trust an AI with a task they previously did themselves.

### The 6-Question Script

Run this with 5-8 users who recently switched to your AI feature (or a competitor's). Don't run it with users who never adopted — they can't tell you what triggered the switch.

**1. When did you first realize you needed something different?**
> *Listening for:* the trigger event. Not "when did you hear about us" — when did the old way become intolerable. There's almost always a specific moment. "My boss asked me to summarize this 200-page report by Monday." "We had a near-miss audit and I realized I had no defensible record."

**2. What had you tried before?**
> *Listening for:* the consideration set. Most users tried 2-3 things before yours. What did they reject and why? This reveals the competitive frame they actually used (often nothing like the one in your strategy doc).

**3. What were you anxious about when you considered the new approach?**
> *Listening for:* anxiety forces. For AI: hallucination, liability, skill atrophy, team backlash, audit trail. Users rarely volunteer these — you have to ask directly. Follow up: "What would have made you walk away?"

**4. What pushed you to actually try it — what made the anxiety smaller than the push?**
> *Listening for:* the activating force. Often a peer, a deadline, a permission ("my manager said it was OK"), or a low-stakes test ("I'll just try it on this one task").

**5. When you used it the first time, what surprised you?**
> *Listening for:* the gap between expected and actual experience. For AI features: did it feel magical, or did it feel like the user was managing the AI? This is the diagnostic for whether the hidden job got served.

**6. What would have to be true for you to stop using it?**
> *Listening for:* the fragility of the switch. AI adoption is not durable until 30 days of consistent use. Switching costs are low. What pulls them back to the old way?

### What to Listen For (the meta-skill)

**The struggle moment, not the feature evaluation.** Users will try to give you a product review ("the UI was clean"). Redirect them to the timeline. "Walk me through the day you decided to try it."

**Emotional language is data, not noise.** "I was embarrassed I didn't know that." "I felt relieved when I saw the answer." These are hidden-job signals. Write them down verbatim.

**The thing they didn't say.** If a user describes adopting an AI tool and never mentions trust, accuracy, or risk — they have a job that doesn't depend on those. (This is rare in enterprise. When it happens, it's usually a casual-stakes use case like brainstorming or first drafts.)

**The moment of social proof.** Almost every enterprise AI switch traces back to a person, not a product. "My colleague at our Bangalore site used it." "My manager mentioned it in a 1:1." The hidden job often includes "looking competent in front of someone specific."

---

## AI-SPECIFIC JOB MAPPING

For each AI feature in scope, fill out this map. The structural move: surface job goes in the PRD, hidden job goes in the design.

```
FEATURE: [name]

SURFACE JOB
  When [situation],
  I want to [functional task],
  so I can [stated outcome].

HIDDEN JOB
  When [situation],
  I want to [emotional / social / cognitive shift],
  so I can [actual outcome — feel, be perceived as, defer].

DESIGN IMPLICATION
  If we design only for surface job: [what we'd build]
  If we design for hidden job: [what we'd build]
  The difference: [the structural change in the product]
```

### Worked example: GitHub Copilot

```
SURFACE JOB
  When I'm writing a function I've written before,
  I want to autocomplete the boilerplate,
  so I can save typing time.

HIDDEN JOB
  When I'm stuck on a function and don't want to admit it,
  I want a non-judgmental partner who will offer a starting point,
  so I can stay in flow without breaking my focus to ask a colleague
  or search Stack Overflow.

DESIGN IMPLICATION
  Surface-job design: faster autocomplete, better keyword matching.
  Hidden-job design: never make the user feel stupid for accepting a
  suggestion. Don't show suggestions that highlight gaps. Make rejection
  zero-friction. Never punish the user for accepting a wrong suggestion.

  The actual GitHub Copilot UI does the second. That's why it works.
```

### Worked example: AI-powered customer support draft response

```
SURFACE JOB
  When a customer ticket comes in,
  I want a draft response,
  so I can save time.

HIDDEN JOB
  When I have 40 tickets in my queue and a manager who tracks resolution time,
  I want plausible deniability that I considered every ticket carefully,
  so I can move fast without feeling like I'm being a bad agent.

DESIGN IMPLICATION
  Surface-job design: high-quality draft, good tone matching.
  Hidden-job design: the draft should preserve the agent's authorship — let
  them edit easily, show what was AI vs what they added, give them an audit
  log they can show their manager. The agent is hiring AI to be a faster
  version of themselves, not a replacement.

  Get this wrong and agents reject every draft because they don't trust
  having "an AI response" attached to their name. Get this right and they
  send 3x more tickets per hour and feel better about their work.
```

---

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

Predictive maintenance recommendation system for industrial assets — turbines, compressors, HVAC fleets across plants. Real a Fortune 100 enterprise territory. The kind of feature where the surface job is obvious and the hidden job is where the design lives or dies.

### Surface job (the demo job)

```
When a turbine's vibration profile starts to drift,
I want the system to predict failure 7 days out,
so I can schedule maintenance before unplanned downtime.
```

This is the job in the marketing deck. It's the job in the RFP. It's also the job that makes the system fail in production.

### Hidden job for the plant operator

```
When the system flags a possible failure,
I want a defensible record that I acted on it (or didn't, with reason),
so I can avoid being the operator who "should have caught it" if something
goes wrong — and also avoid being the operator who shut down a $2M asset
on a false alarm and got blamed for that too.
```

The operator's hidden job is **anxiety asymmetry management**. Both action and inaction can hurt them. They're not hiring the AI to predict failure — they're hiring it to share the blame. This changes the design completely.

### Hidden job for plant management

```
When an asset fails (or is taken down for maintenance),
I want a defensible audit trail showing the decision was data-driven,
so I can answer to corporate / insurers / regulators with evidence
instead of judgment calls.
```

Management's hidden job is **audit-defensibility**. They don't care if the AI is right 92% of the time — they care that the system produces a paper trail that survives a deposition.

### The design implication

Surface-job design (what most vendors build):
- High-accuracy prediction models
- Clean dashboards
- Maintenance scheduling integration

Hidden-job design (what actually wins the renewal):
- Every recommendation is timestamped, version-locked, and exportable
- Operators can record their disposition (acted / declined / deferred) with a one-line reason — this becomes the audit log
- The system shows confidence level in plain language ("high confidence" not "0.87"), and explicitly flags low-confidence cases as "review with engineer" instead of "predicted failure"
- Refusal is allowed: the system says "I don't have enough data to predict this asset" instead of guessing
- Disagreement is captured: when an operator declines a recommendation that turns out to be right, the system doesn't surface that to management — it surfaces it to the model team for retraining

a Fortune 100 enterprise's competitive moat in industrial AI is not better models. It's that we understand the operator's hidden job — share the blame, preserve the audit trail, never make them look stupid in front of management. Vendors who ship better accuracy without that insight lose the renewal.

---

## DELIVERABLE FORMAT

Every JTBD analysis produces four artifacts. If you can't produce all four, the analysis isn't done.

### 1. Job Statement (one paragraph)

> When [situation], I want to [job], so I can [outcome]. The hidden job underneath: [emotional / social / cognitive shift].

Two layers, surface and hidden, in five sentences total.

### 2. Four-Forces Diagram

Push, pull, anxiety, habit — each with 2-4 specific forces. For enterprise AI, anxiety must be at least as developed as pull. If anxiety has fewer entries than pull, the analysis is incomplete.

### 3. Surface vs Hidden Job Map

The table format from this skill, filled out for the specific feature. Includes the design implication: what would change if we designed for the hidden job.

### 4. Design Implication (one paragraph)

> If we design only for the surface job, we'd build X. If we design for the hidden job, we'd build Y. The difference is Z, and Z is what determines whether this feature gets adopted past the pilot.

This last artifact is what makes the JTBD work load-bearing. Without it, the analysis is decoration.

---

## CROSS-LINK WITH ADJACENT SKILLS

This skill doesn't run alone. It connects to:

- **`problem-ai-fit`** — JTBD identifies what job is being hired. Problem-AI-fit checks whether AI is the right hire for that job. Run JTBD first when the problem is unclear; run problem-ai-fit when the AI assumption needs testing.
- **`uncertainty-research`** — once you have a job statement, the switch interview methodology in this skill becomes one of the research methods. The research designs in uncertainty-research are how you scale validation.
- **`failure-modes`** — the hidden job tells you which failures hurt most. If the hidden job is "preserve audit trail," then silent degradation is catastrophic and confident-wrong is acceptable (because the audit log catches it). If the hidden job is "save me from feeling stupid," then refusals hurt more than errors.
- **`opportunity-solution-tree`** — a job statement becomes the desired outcome at the top of the tree. The hidden job filters which opportunities are worth pursuing.

The chain: JTBD names the job → problem-ai-fit confirms AI is the right hire → opportunity-solution-tree picks where to bet → failure-modes designs for what hurts most.

---

## RED TEAM

This skill gives bad advice when:

**The product is a commodity with no real switch decision.** Procurement-driven B2B buys (corporate Office 365 licenses, enterprise CRM mandated by IT, regulatory compliance tools) don't have a "moment of switch" — the buyer is forced. JTBD's force model assumes voluntary adoption. For mandated tools, use stakeholder-mapping instead and figure out who has political incentive to make it succeed.

**The user is captive.** Internal tools where employees have no choice (HR systems, expense reporting, mandatory safety platforms) don't generate the kind of struggle moments JTBD is designed to capture. The feature ships because it has to. JTBD will produce hollow job statements that read well but don't change the design.

**The feature is competing on price, not job.** When buyers pick the cheapest option that meets a checklist, JTBD adds noise. The job is "satisfy procurement at lowest cost." Run cost-modeling and competitive-position instead.

**The user can't articulate their own job.** Sometimes the user is too close to the problem to see it. They'll describe the surface job over and over and resist the hidden-job framing. In these cases, behavior beats words: instrument the workflow, watch what they actually do, and infer the job from their actions. Switch interviews still work, but you have to mine the silence as much as the words.

**The "AI" framing is a distraction.** If the feature is genuinely deterministic (lookup, rule-based routing, simple classification), forcing it through an AI-job lens generates artificial complexity. Use straight JTBD without the AI overlay. The hidden job still matters; the AI-specific anxieties might not.

---

## WHEN WRONG

This skill produces overconfident output when:

- **You only interviewed users who switched to your product.** You're getting survivorship bias. Add interviews with users who switched away from competitors to nothing — they reveal the anxiety and habit forces most clearly.
- **The hidden job feels obvious to the team.** If everyone in the room agrees on the hidden job in the first 10 minutes, it's probably the surface job in disguise. Real hidden jobs feel slightly uncomfortable to name out loud — they often involve users hiring the AI to manage how they're perceived, defer responsibility, or avoid effort. Push past the polite framing.
- **You skipped the four-forces analysis.** A job statement without the force diagram is a poem, not a tool. The force diagram is what makes the job statement actionable.

---

## QUALITY GATE

Before shipping the JTBD analysis, verify:

- [ ] Job statement is two layers (surface + hidden), not one
- [ ] Four forces diagram has at least 2 entries per quadrant
- [ ] Anxiety quadrant is at least as developed as pull
- [ ] Surface vs hidden job map includes a design implication that would change the product
- [ ] At least 5 switch interviews informed the analysis (not "we think users want X")
- [ ] The hidden job names emotional, social, or cognitive demand — not just functional
- [ ] The analysis ends with a Monday-morning design change, not a customer empathy slide

If any box is unchecked, the JTBD work isn't done.

---

## CONCLUSION

A complete JTBD analysis ends with one sentence:

> "We're going to redesign [feature] to serve the hidden job of [job], because right now we're designing for the surface job of [task] and it's why adoption is [observed pattern]."

That sentence is the deliverable. Everything else is the working.

If the team can't write that sentence at the end, restart at the switch interviews — the job analysis isn't done yet.

---
name: jtbd-analysis
description: "Demand-side Jobs-to-be-Done for AI features — the reframe most PMs miss: users don't hire the AI for the surface task they name, they hire it for the hidden job (offloading cognition, sharing blame, reducing anxiety, looking competent). Design for the surface job and the feature dies in production; design for the hidden job and users defend it even when it's wrong. Runs the four-forces diagram, the switch-interview script, and the surface-vs-hidden map — output is a job statement plus a design implication, not a 40-page empathy deck. Use when scoping a new AI feature, or when a working feature has flat adoption. Do NOT use for commodity, mandated, or captive tools with no real switch decision. Pairs with: problem-ai-fit (is AI the right hire), uncertainty-research (scaling the switch interviews), failure-modes (which failures the hidden job makes catastrophic), opportunity-solution-tree (the job as top-of-tree outcome). Triggers: 'what should this AI do', flat adoption despite working as designed."
imports:
  - problem-ai-fit
  - first-principles
  - uncertainty-research
---

# JTBD Analysis

**The objective:** decipher what users are actually hiring an AI feature to do — and design for that, not for the task they name — for the PM scoping a new AI feature or staring at a working one nobody adopts.

## The one idea

> "People don't want a quarter-inch drill. They want a quarter-inch hole." — Theodore Levitt.

The 0.1% AI-PM correction: people don't want the hole either. They want the picture on the wall, the partner to feel proud, the room to feel *done.*

Here is the whole idea in one example. A developer using GitHub Copilot will tell you the job is "complete my code." That's the cover story. The real job is *feel less alone while coding; stay in flow; avoid the shame of asking a stupid question on Stack Overflow.* The functional task is what they say. The **hidden job** — emotional, social, cognitive — is the actual demand.

This matters more for AI than for any product category before it, and here's the mechanism: every other category competes on *capability*. AI competes on whether the user trusts you with their **cognitive load** — and that load is almost always about emotional regulation, social positioning, or anxiety reduction. AI is the first technology that reaches those layers directly. So the PM who designs for the surface job ships a feature that works on the demo and dies in production. The one who designs for the hidden job builds something users *defend even when it's wrong* — because it's still doing the real job (sharing the blame, preserving the audit trail, keeping them in flow) even on a turn where the output was bad.

Miss the hidden job and you're competing on benchmarks. Hit it and you're competing on relationship. That's the reframe.

## How to use this skill

1. **Map surface vs. hidden job** — for the feature in scope, name the task the user says and the emotional/social/cognitive job underneath. (THE SURFACE/HIDDEN MAP.)
2. **Run the four forces** — switching happens only when push + pull beat anxiety + habit; for AI, anxiety is 2–3× what PMs assume, so develop it hardest. (THE FOUR FORCES.)
3. **Validate with switch interviews** — reconstruct the timeline from "thought of switching" to "first use" with 5–8 users who actually switched. (THE SWITCH INTERVIEW.)
4. **End on a design implication** — the one Monday-morning change that comes from designing for the hidden job instead of the surface one. Without it, the analysis is decoration.

## KEY TERMS (plain language)

- **Surface job** — the functional task the user names ("summarize this doc"). Goes in the PRD.
- **Hidden job** — the emotional, social, or cognitive shift they're actually hiring the AI for ("have a defensible answer if my boss asks what's in there"). Goes in the design.
- **The four forces** — Bob Moesta's switch model: push (away from the old way) + pull (toward the new) must beat anxiety (about the new) + habit (of the old) for a switch to happen.
- **Switch interview** — a JTBD interview that reconstructs the timeline of a real switch, hunting the struggle moment, not a feature review.
- **The struggle moment** — the specific event that made the old way intolerable ("my boss asked me to summarize 200 pages by Monday"); the trigger a switch traces back to.
- **Anxiety asymmetry** — when both acting and not-acting can hurt the user (shut down a $2M asset on a false alarm, or miss the real failure); the AI is often hired to share that blame.
- **Audit-defensibility** — the hidden job of producing a paper trail that survives a deposition, independent of whether the AI was right.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum: name the feature and who's hiring it, and what "adoption" would look like. Then route depth and output format:

- **Go deep** when a new AI feature is being scoped, an existing one has flat adoption despite working as designed, or the team is debating "what should this AI do?" before naming what it's hired for.
- **Skim to the four forces** when you already have a job statement and just need to test whether the switching forces are strong enough.
- **Skip** for commodity, mandated, or captive tools where the user has no real switch decision (see RED TEAM).

Output format: **Inline** (paste into a PRD, the default), **Word** (spec-review appendix), or **Presentation** (stakeholder kickoff).

## THE SURFACE/HIDDEN MAP

The structural move: the surface job goes in the PRD, the hidden job goes in the design.

| Feature | Surface job (what the user says) | Hidden job (what the AI is hired for) |
|---|---|---|
| GitHub Copilot | "Complete my code" | Feel less alone; stay in flow; avoid the shame of a "stupid" Stack Overflow question |
| ChatGPT for writing | "Draft this email" | Defer the decision about tone; get permission to use these words; lower activation energy |
| Notion AI summarize | "Summarize this doc" | Avoid reading 40 pages; have a defensible answer when the boss asks "what's in there?" |
| Predictive maintenance | "Predict when the asset fails" | Have a defensible record; avoid being the operator who "should have caught it" |
| AI legal review | "Find risky clauses" | Share the blame if something's missed; reduce the load of reading dense contracts |

**The template to fill for your feature:**

```
FEATURE: [name]
SURFACE JOB   When [situation], I want to [functional task], so I can [stated outcome].
HIDDEN JOB    When [situation], I want to [emotional/social/cognitive shift], so I can [actual outcome — feel, be perceived as, defer].
DESIGN IMPLICATION
  Design only for surface → [what we'd build]
  Design for hidden       → [what we'd build]
  The difference          → [the structural change that decides adoption]
```

**Worked example — GitHub Copilot.** *Surface:* autocomplete boilerplate to save typing. *Hidden:* when I'm stuck and don't want to admit it, give me a non-judgmental partner who offers a starting point so I stay in flow without asking a colleague. *Design implication:* the hidden-job design never makes the user feel stupid for accepting a suggestion — zero-friction rejection, no suggestions that highlight gaps, no punishment for accepting a wrong one. The real Copilot UI does the second. That's why it works.

**Worked example — AI support-draft response.** *Surface:* draft a reply to save time. *Hidden:* with 40 tickets queued and a manager tracking resolution time, I want plausible assurance I considered each ticket, so I can move fast without feeling like a bad agent. *Design implication:* preserve the agent's authorship — easy edits, show AI-vs-human contribution, give them an audit log to show their manager. Get it wrong and agents reject every draft because they won't attach "an AI response" to their name; get it right and they send 3× more tickets per hour and feel better about it.

## THE FOUR FORCES

A switch is rational only when **push + pull > anxiety + habit.** For AI, anxiety is usually the dominant force — and the one PMs underweight.

- **Push** (away from the current way) — the old solution is failing in a specific way; a new event made it intolerable (a cost spike, a new boss, an audit).
- **Pull** (toward the new) — a specific better outcome; someone they trust already uses it; the story of the new way feels true.
- **Anxiety** (about the new) — *what if the AI hallucinates? what if my boss audits its recommendation? what if I lose the skill? what if I'm liable?*
- **Habit** (of the current) — muscle memory, sunk cost, fear of looking stupid while learning, a team that isn't ready.

**The trap:** PMs spend 90% of design energy on pull (how good the AI is) and 10% on anxiety (what goes wrong, who's liable, what happens when it's confidently wrong). For enterprise AI, invert it — the pull is real, but anxiety is what blocks adoption. **The working rule:** if you can't name the top three anxieties in one sentence each, you haven't done the job analysis yet.

## THE SWITCH INTERVIEW

Reconstruct the timeline from "thought of switching" to "first use." You're hunting the moment a user decided to trust an AI with a task they used to do themselves. Run it with 5–8 users who *recently switched* (to you or a competitor) — not users who never adopted; they can't tell you what triggered a switch.

1. **When did you first realize you needed something different?** → the trigger event (the struggle moment), not "when did you hear about us."
2. **What had you tried before?** → the real consideration set (usually nothing like your strategy doc's competitive frame).
3. **What were you anxious about?** → the anxiety forces (hallucination, liability, skill atrophy, audit trail); they rarely volunteer these — ask directly, then "what would have made you walk away?"
4. **What pushed you to actually try it?** → the activating force (a peer, a deadline, a manager's permission, a low-stakes test).
5. **When you first used it, what surprised you?** → the gap between expected and actual; did it feel magical, or like managing the AI? The diagnostic for whether the hidden job got served.
6. **What would have to be true for you to stop?** → the fragility of the switch (AI adoption isn't durable until ~30 days of consistent use).

**What to listen for:** the *struggle moment*, not a feature review ("walk me through the day you decided to try it"). Emotional language is data, not noise — "I was embarrassed I didn't know that" is a hidden-job signal; write it verbatim. The *thing they didn't say* — if trust, accuracy, and risk never come up, they have a low-stakes job. And the *moment of social proof* — almost every enterprise switch traces to a person, not a product ("my manager mentioned it in a 1:1"); the hidden job often includes "looking competent in front of someone specific."

## REAL-WORLD ENTERPRISE EXAMPLE — industrial predictive maintenance

A predictive-maintenance recommendation system for industrial assets — turbines, compressors, HVAC fleets across plants. Real Fortune-100 territory, and the kind of feature where the surface job is obvious and the hidden job is where the design lives or dies.

**Surface job (the demo job):** *when a turbine's vibration drifts, predict failure 7 days out so I can schedule maintenance before unplanned downtime.* This is the job in the RFP — and the one that makes the system fail in production.

**Hidden job — the plant operator: anxiety asymmetry.** *When the system flags a possible failure, give me a defensible record that I acted on it (or didn't, with reason), so I'm not the operator who "should have caught it" — and also not the one who shut down a $2M asset on a false alarm and got blamed for that too.* Both action and inaction can hurt them. They aren't hiring the AI to predict failure; they're hiring it to **share the blame.**

**Hidden job — plant management: audit-defensibility.** *When an asset fails or is taken down, give me a data-driven audit trail, so I can answer corporate, insurers, and regulators with evidence instead of judgment.* They don't care that the AI is right 92% of the time; they care that it produces a paper trail that survives a deposition.

**The design implication.** Most vendors build the surface job: high-accuracy models, clean dashboards, scheduling integration. The hidden-job design is what wins the renewal — five moves, each serving blame-sharing or audit-defensibility over raw accuracy:

- **Timestamp everything** — every recommendation version-locked and exportable, so it survives a deposition.
- **Record the operator's disposition** — acted / declined / deferred, each with a one-line reason. That record *is* the audit log.
- **Show confidence in plain language** — "high confidence," not "0.87"; flag low-confidence cases "review with engineer," not "predicted failure."
- **Allow refusal** — "not enough data to predict this asset" beats a confident guess that blows up the operator's credibility.
- **Route a wrong decline to the model team, not to management** — when an operator overrides a recommendation that turns out right, that's retraining data, not a performance flag.

The moat in industrial AI is not better models — it's the operator's hidden job: share the blame, preserve the audit trail, never make them look stupid in front of management. Vendors who ship better accuracy without that insight lose the renewal.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

JTBD produces one thing — a job statement (surface + hidden + design implication). Trace where it travels, not just what sits beside it.

**The forward chain — who acts on the job statement first:**
- **`rtp-problem-ai-fit`** *(import)* — takes the named job and checks whether AI is even the right hire for it. Run JTBD first when the problem is unclear; run problem-ai-fit when the AI assumption needs testing. Writing two beautiful job layers for a feature AI shouldn't own is a wasted analysis, not a solved one.
- **`rtp-opportunity-solution-tree`** — the job statement becomes the desired outcome at the top of the tree; the hidden job is the filter that decides which opportunities are worth pursuing.
- **`rtp-uncertainty-research`** *(import)* — the switch interview is one method; this scales it into a real research design when 5–8 interviews aren't enough to trust the finding.

**The second-order path — where the hidden job resurfaces once you've built:**
- **`rtp-failure-modes`** — the hidden job decides which failures are catastrophic: "preserve the audit trail" makes silent degradation fatal and confident-wrong survivable (the log catches it); "save me from feeling stupid" makes a refusal hurt more than an error. The hidden job is the input that turns a generic failure taxonomy into a prioritized one.
- **`rtp-fit-signal`** — the non-obvious two-hop most teams miss. Weeks after launch, fit-signal measures whether users *depend* on the feature — and what they depend on is the hidden job being served reliably. A feature that passed JTBD but fails fit-signal's trust curve is evidence the hidden job was mis-named or stopped being served, not that the surface feature broke. Feed the hidden job into fit-signal's magic-moment definition so it measures dependence on the real job, not the cover story.

**The upstream informal feeder (reciprocal with gossip-mode):**
- **`rtp-gossip-mode`** — a hidden job isn't found once and frozen. An operator saying "I'd rather it refuse than guess" in a standup is live anxiety-and-tolerance data (gossip-mode's signal 8) that refreshes this map between formal switch-interview rounds. Gossip-mode catches the sideways signal and routes it here; this skill is where it lands as a revised gain criterion.

## RED TEAM — when this skill gives bad advice

- **A commodity with no real switch.** Procurement-driven B2B buys (mandated CRM, compliance tools) have no "moment of switch" — the buyer is forced. Use stakeholder-mapping to find who has the political incentive to make it succeed.
- **A captive user.** Internal tools employees can't opt out of (HR, expense, mandatory safety platforms) don't generate struggle moments; JTBD produces hollow job statements that read well and change nothing.
- **Competing on price, not job.** When buyers pick the cheapest option that clears a checklist, the job is "satisfy procurement at lowest cost" — run cost-model and competitive-map instead.
- **The user can't articulate their own job.** Too close to see it, they repeat the surface job. Behavior beats words: instrument the workflow, watch what they do, infer the job from actions; mine the silence as much as the words.
- **The "AI" framing is a distraction.** If the feature is genuinely deterministic (lookup, rule-based routing), the hidden job still matters but the AI-specific anxieties may not — use straight JTBD without the AI overlay.

## WHEN WRONG

- **You only interviewed users who switched *to* you** — survivorship bias. Add users who switched away from a competitor to nothing; they reveal anxiety and habit most clearly.
- **The hidden job feels obvious to the whole room in 10 minutes** — it's probably the surface job in disguise. Real hidden jobs feel slightly uncomfortable to say out loud (users hiring the AI to manage perception, defer responsibility, avoid effort). Push past the polite framing.
- **You skipped the four forces** — a job statement without the force diagram is a poem, not a tool.

## QUALITY GATE

- [ ] Job statement is two layers (surface + hidden), not one
- [ ] Four-forces diagram has ≥2 entries per quadrant, and anxiety is at least as developed as pull
- [ ] Surface-vs-hidden map includes a design implication that would change the product
- [ ] At least 5 switch interviews informed it (not "we think users want X")
- [ ] The hidden job names an emotional, social, or cognitive demand — not just a functional one
- [ ] It ends with a Monday-morning design change, not an empathy slide

## TRADE-OFF LEDGER

By designing for the hidden job, you bet that adoption is won on trust and emotional fit, not on benchmark capability. You give up the clean, defensible "we shipped the requested feature" story and take on the harder, softer work of naming what users won't say out loud. **Reversible?** Yes — it reshapes design priorities, not architecture. **The hidden trade:** the failure mode is *projection* — the team inventing a flattering hidden job instead of mining a real one, which is why the switch interviews (not the whiteboard) are load-bearing. **Confidence: High** for voluntary-adoption AI; **Low** for commodity/mandated/captive tools (see RED TEAM), where the switch model doesn't apply. What would change it: no real switch decision exists.

## CONCLUSION

A complete JTBD analysis ends with one sentence:

> "We're going to redesign [feature] to serve the hidden job of [job], because right now we're designing for the surface job of [task], and that's why adoption is [observed pattern]."

That sentence is the deliverable; everything else is the working. If the team can't write it, restart at the switch interviews — the job analysis isn't done. Then follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): recommendation, key trade-off, biggest risk, next action.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the surface job and the hidden job stacked (what they say / what they're hiring it for), with the four forces drawn as the switch scale beneath — push + pull on one side, anxiety + habit (anxiety enlarged) on the other — so a viewer sees that adoption turns on serving the hidden job and shrinking the anxiety, not on adding capability. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

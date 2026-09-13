---
name: rtp-stakeholder-communications
version: v1.9.1_latest
description: 'Write stakeholder messages that help people understand the evidence, the decision, and their part in the next step. Use for executive summaries, engineering briefs, launch announcements, risk escalations, weekly digests, or work that is not landing with its audience. Adapt the same underlying facts to executives, engineers, partners, customers, and boards without changing their meaning. For AI performance claims, make scope, measurement, uncertainty, known limits, monitoring, and recovery traceable at the depth the audience needs. Includes five communication formats, four worked cases, six audience needs, relationship mapping, a four-level trust framework, channel choice, constructive challenge, issue selling, candor, and influence without formal authority. Keep advice proportionate: a short update can stay short, and missing evidence should be stated rather than invented. Pairs with trust-under-fog, confidence-tuner, eval-framework, ai-product-metrics, and problem-ai-fit.'
imports:
  - ai-product-metrics
  - eval-framework
  - problem-ai-fit
  - trust-under-fog
  - confidence-tuner
---

# Stakeholder Communications

Help the reader understand **what matters, what supports it, and what happens next**. Adapt the language and detail to the audience while keeping the facts, uncertainty, and commitments consistent.

Good communication depends on evidence, understandable wording, useful framing, relationships, and timing. None substitutes for the others. An executive, engineer, and customer can need different views of the same evidence; they should not receive contradictory promises.

## Choose a useful path

- **A short update or urgent unblock:** write the few lines needed, verify their claims, and stop.
- **A decision, launch, or material risk:** use the process below and the appropriate [communication format](references/formats-and-examples.md).
- **A draft with questionable AI claims:** go directly to **Keep the evidence intact**.
- **Good work is not landing, or a meeting is difficult:** use the [relationship and influence guide](references/relationships-and-influence.md).

The basic communication practices also apply to deterministic features. Add AI-specific measurement only where it is relevant. A stakeholder unfamiliar with AI needs a plain explanation, not exclusion from the conversation. When evidence does not yet exist, communicate the gap, its consequence, and the plan to resolve it.

## Prepare the message

### 1. Identify the reader, purpose, and live concern

Clarify who will use the message, what they need to understand or decide, the current relationship, and any deadline. Use context already available. One main purpose helps focus, but a decision note can also provide awareness and address several affected readers. Separate messages when interests, permissions, or decisions differ enough to warrant it.

Use the **six needs** as prompts for listening, not labels assigned from a person's title:

| Need | What the person may be asking |
|---|---|
| Protection | What risk am I taking, and what support exists? |
| Fairness | Are the criteria and consequences applied consistently? |
| Vision | Where is this going, and why does it matter? |
| Expertise | What do I need to understand to judge or do the work? |
| Affiliation | Am I included, respected, and connected to the group? |
| Status | Will my contribution be recognized and my standing treated fairly? |

Several needs can be active at once. Check your interpretation through questions and observed concerns, and notice whether you keep supplying your preferred answer instead. In a fearful room, clarify protections and fairness while allowing private or anonymous input when appropriate; these are not needs that can always be “over-supplied” without cost.

### 2. Assemble a shared evidence record

Separate observed facts, interpretations, estimates, hypotheses, and commitments. For material quantitative claims, record the metric definition, population, denominator, time window, method, source, and uncertainty that affect interpretation. For qualitative claims, identify the observation or source and its limits.

For AI capability claims, link the effective model/prompt/configuration and evaluation date in the working record. Include tools, context, or routing when they materially affect the result. Readers do not need every identifier repeated in a customer announcement, but the claim should remain reconstructable.

Use one consistent **evidence set**, not one forced number. An overall result of 92% and a difficult-segment result of 87% can both be correct and necessary. Do not collapse them into 94% for a more attractive executive message.

### 3. Choose the format and channel

| Audience | Usually foreground | Add when needed |
|---|---|---|
| Executive | Recommendation, benefit, boundary, risk, resources, and ask | Measurement detail that changes the decision |
| Engineering | User problem, contracts, effective configuration, evals, failures, and open implementation decisions | Business priorities and customer context |
| Design, legal, sales, support, and other partners | What changes in their work, affected cases, responsibilities, and approved representations | Relevant technical evidence or commercial detail |
| Customer or buyer | Useful experience, availability, applicable limits, controls, and assistance | Performance evidence, versions, or technical details relevant to their purchase or use |
| Board | Strategic options, capability, material exposure, capital use, accountability, and decisions | Detail needed to assess a material assumption or incident |

These are starting points, not restrictions on what each audience may understand or ask for.

Use writing when a durable record, careful review, accessibility, or asynchronous participation matters. Use a conversation when rapid clarification, emotion, conflict, or ambiguity makes interaction useful. Often the best sequence is a concise pre-read, a conversation, then an agreed written record. Sensitive content does not automatically require a live channel; a clear, scoped written message can preserve nuance better than an undocumented call. Assume either can be repeated or forwarded, and protect confidential information appropriately.

### 4. Draft around the decision or useful outcome

Lead with the recommendation, material change, impact, or relevant user moment. Then provide the evidence and context needed to understand it. Put consequential uncertainty beside the claim it qualifies. End with the actual next step, owner, or update time when one exists; an awareness note need not invent an ask.

Choose among the five formats in [Formats and examples](references/formats-and-examples.md): executive summary, engineering brief, launch announcement, risk escalation, or weekly digest. Its length suggestions are editing aids, not hard limits. Do not bury an urgent fact while trying to complete a template or invent three options when only one responsible containment action exists.

AI can help with an outline, draft, critique, or revision. Choose the method that helps you retain the intended position. An outline-first workflow can reduce anchoring for some writers; a generated draft can also be useful. Check the opening, argument, evidence, and ask, rather than assuming edited words mean the framing is yours. A read-aloud pass can help when practical; a silent readability check is also valid. Never claim a review that was not performed.

### 5. Review meaning across audiences

Compare versions against the evidence record. Check metric names, denominators, dates, scope, uncertainty, availability, fallback, and commitments. Shortening should not turn “observed in a pilot” into “works everywhere,” “use” into “trust,” or “may help” into “will solve.”

Make the final draft ready to use. Put optional review notes outside the copy, clearly marked, when the user benefits from them. For multiple audiences, supply complete labeled variants and a brief reconciliation note if useful. This skill prepares communication; sending or publishing requires the user's authorization and the applicable task permissions.

## Keep the evidence intact

### Claim, change risk, and response

For a consequential AI-performance statement, make three things available at the right level of detail:

1. **What supports the claim:** the measured result, relevant population and method, uncertainty, and evaluation conditions. A percentage is not automatically a confidence interval, and not every meaningful claim needs a number.
2. **What could change the result:** known boundaries, plausible shifts in data or use, relevant dependency changes, monitoring owner, and action trigger. Unknown change risks can remain unknown; do not claim you know exactly when drift will occur.
3. **What happens when the feature falls short:** detection limits, fallback, user control, escalation, and recovery that actually exist.

Use a separate “What could be wrong” section when it improves a substantial decision note. A two-line update or customer announcement may integrate the same essential limit beside the claim instead. Do not reproduce a full risk register in every turn.

### One illustrative evidence set, three accurate framings

Assume a fictional evaluation records **364 acceptable answers out of 400 labeled queries (91%)**, collected March 1–15 under a defined rubric. A separately defined difficult bucket achieved 78%; its size and overlap must be reported in the full record. The normal-binomial assumptions may not hold for clustered queries. If independent binary trials are a reasonable approximation, a 95% Wilson interval for 364/400 is approximately **87.8–93.4%**.

- **Engineering:** “The March 1–15 evaluation achieved 364/400 acceptable answers under the linked rubric. Difficult queries scored 78%; see their sample and definition. Review coverage, subgroup results, and the tested fallback before expanding.”
- **Executive:** “The system met the evaluation standard on about nine in ten sampled queries. Performance was lower on the difficult cases we tested. We recommend the bounded rollout described below, with monitoring and a tested alternative.”
- **Customer:** “The assistant provides a draft answer for supported questions. You can inspect its sources and use the available correction or assistance options. Complex or unclear questions may need additional review.”

The customer wording assumes those controls exist. The executive version does **not** say we can identify every wrong answer in advance. An expected calibration error of 0.04 would not establish “no overconfidence on errors”; its method, bins, population, and important failure slices need interpretation. A user's correction does not automatically retrain the model or improve future output.

### Use the right claim for the measure

| Loose statement | More useful, scoped wording |
|---|---|
| “Highly accurate” | “[Defined success] on [count/total] held-out cases, [population/date], with [material limits]” |
| “Performance improved” | “First-pass acceptance rose eight percentage points in this segment over this window; verified quality and possible causes are assessed separately” |
| “Hallucination is rare” | “196 of 200 sampled outputs passed the stated source-consistency check; this does not cover every type of factual error” |
| “Latency is good” | “P50/P95/P99 were [values] for [end-to-end measure, population, load, window]” |
| “Users love it” | “First-pass use, regeneration, and CSAT were [values and denominators]; these describe behavior and reported satisfaction” |

An unchanged prompt version does not rule out a prompt/context interaction, and stable latency does not rule out all infrastructure problems. Association with a data refresh is a lead, not a proven cause. Use a numeric probability only when it has a defensible basis; a plain statement such as “retrieval is our leading hypothesis” is often more honest than an invented 70%.

### Describe monitoring without promising inevitable drift

Report what has been observed and what is being watched: “Acceptance stayed within three percentage points over 47 days. A new segment could change task mix; we will evaluate its cases, review results after onboarding, and act at the agreed threshold.” Label any expected 15–20% mix shift as an estimate with a basis.

Drift may occur; it is not necessarily happening now. Re-baselining should record a justified change in population or objective, not erase a regression. Specify whether a threshold is a relative percent or percentage-point change, and use a meaningful window and denominator.

## Communicate risk and governance in decision terms

Connect the request to a concrete exposure, obligation, operational dependency, customer outcome, or financial consequence. Quantify where the evidence supports it and distinguish exposure from expected loss. A $420,000 renewal pipeline touching a feature is not $420,000 of proven lost revenue.

Boards can act on legal duties, severe plausible harms, stakeholder commitments, or strategic dependencies without a precise dollar estimate or a prior incident. If uncertainty matters, explain what is unknown and request the needed mitigation, investigation, or decision. Do not delay a required control merely to make the risk look financially measurable. `trust-under-fog` helps with disclosure under uncertainty; `confidence-tuner` helps match claims and confidence to evidence.

For voluntary initiatives, report participation and its denominator alongside outcomes and use. Falling attendance, questions, or contributions can indicate withdrawal, competing demands, task completion, or another cause. Investigate rather than labeling quiet as health or inevitable failure. “No objections raised” describes reporting; it does not establish consent or success. Participation is a useful early indicator in some settings, not the only one.

## Run conversations with clear roles and follow-through

Before a decision meeting, establish the goal and expected output. Clarify four participation questions:

1. Who is expected to contribute ideas, experience, or evidence?
2. Who decides, and by what process?
3. Who primarily needs context to implement or carry the decision forward?
4. Who can block or override the decision, within what scope?

Confirm an existing arrangement briefly rather than repeating a ritual. Close with the decision or unresolved question, owner, next step, and timing. A junior person can facilitate; a senior expert can contribute or listen. Roles are responsibilities, not a ranking of personal worth.

When relationships or disagreement are the main obstacle, use the [relationship guide](references/relationships-and-influence.md). It preserves the network map, four trust practices, five relationship principles, four challenge patterns, three-faction issue map, seven leadership shifts, candor practices, review-bottleneck moves, moderation roles, and five informal influence paths. Treat them as tools for understanding and cooperation, not scripts for manipulating a room.

## Final review

- [ ] The main reader, purpose, and relevant concern are clear.
- [ ] The opening makes the useful point without burying material impact.
- [ ] Claims have appropriate support; facts, estimates, and hypotheses are distinguishable.
- [ ] Boundaries that affect the reader's action are understandable.
- [ ] Monitoring and uncertainty are described accurately where relevant.
- [ ] Failure response and user controls match the real product.
- [ ] The evidence can be traced to the relevant date and configuration.
- [ ] Any ask, commitment, owner, and deadline are real and clear.
- [ ] The language sounds natural and precise; remove empty hype and unnecessary jargon.
- [ ] Versions for different audiences reconcile without exposing inappropriate detail.

Prefer ordinary words to “leverage,” “seamless,” “transformative,” or “game-changing” when those phrases add no meaning. A legitimate technical term need not be banned when it is the clearest description. Check substance as well as tone: polished writing can still hide a weak inference, and rough wording can still contain important evidence.

Deliver the finished communication in the user's requested form. Include a short rationale or evidence-gap note only when useful. For source boundaries, see [Communication evidence notes](references/communication-evidence.md). Apply the shared Universal Skill Protocol proportionately to handoffs, not as a mandatory visible wrapper around every message.

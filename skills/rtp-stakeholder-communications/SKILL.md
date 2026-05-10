---
name: rtp-stakeholder-communications
description: 'Audience-tailored communication for AI features — exec summaries, engineering briefs, launch announcements, risk escalations, weekly digests. The differentiator is AI-native confidence framing: every claim about a model''s behavior carries an eval-backed band, a named drift surface, and a mandatory "what could be wrong" section. Use when a single piece of information needs to land in three rooms — exec, engineering, customer — and each room is going to ask a different "but what''s the failure rate?" question. Do NOT use for internal team chat, casual PR updates, or comms about deterministic features where probabilistic framing is theater. Triggers: "stakeholder update," "exec briefing," "escalate to leadership," "launch announcement," "weekly digest," "send a note to."'
---
# Stakeholder Communications: AI-Native Edition

## DEPTH DECISION

**Go deep** — read the whole skill — when: writing the launch announcement for an AI feature, escalating a model failure to an SVP, drafting a board-facing AI capability briefing, or putting your name on a quarterly update where someone will ask "but what's the failure rate?"

**Skim to AI-NATIVE CONFIDENCE FRAMING** when: you already have a draft, you just need to pressure-test the probabilistic claims before sending.

**Skip** when: you're sending a deterministic-feature update (rules engine, integration ship, CRUD launch) — the AI scaffolding here will read as theater. Use `pm-execution:write-stories` or a normal PRD update instead.

## THE STRUCTURAL INSIGHT

Most PMs treat stakeholder communication as a tone problem. It is not. **It's an evidence problem.** The reason an exec, an engineer, and a customer can read the same AI launch update and reach different conclusions is not that the message was tonally wrong — it's that the message did not anchor any of them to the same eval evidence, the same drift surface, the same boundary condition. They each filled the gap with their own assumption. By the time the model misfires in production, the exec thinks you over-promised, the engineer thinks you under-specced, the customer thinks the product is broken. None of them are wrong. The PM gave them three different mental models of the same feature.

The 0.1% move: **one set of eval evidence, three audience-shaped framings.** Engineers see the eval matrix and prompt diff. Execs see the boundary condition in plain English ("works for use case X, degrades when Y exceeds Z, fallback is W"). Customers see the experience and the human-in-the-loop. All three are anchored to the same number, the same regression test, the same drift watch. You cannot be caught with a different story in different rooms.

This is the Bridger move applied to comms. Not "translate jargon." Translate the *underlying evidence* into each audience's decision language without losing the evidence.

## AUDIENCE TIER MAP

| Audience | What they need | What they don't | Decision they're making |
|---|---|---|---|
| **Executive (VP/SVP/CPO/CEO)** | Boundary condition. Cost trajectory. Trust trajectory. One ask. | Eval methodology. Prompt internals. Sprint-level status. | Should I keep funding this? Defend it externally? Kill it? |
| **Engineering (EM/Tech Lead/IC)** | Eval matrix. Prompt diff. Failure surface. Open architecture questions. | Customer narrative. ROI framing. | What do I build, ship, instrument, or push back on this sprint? |
| **Cross-functional (Design/Legal/Sales/Support)** | What changes for *their* workflow. Edge cases that hit *their* surface. | The full eval matrix. The prompt history. | How do I represent this to my own audience? What do I need to update on my side? |
| **Customer (External user/buyer)** | What it does. What it doesn't do. What happens when it's wrong. The human escape hatch. | Confidence numbers, model versions, internal benchmarks. | Should I trust this with my workflow? When do I override it? |
| **Board (Quarterly/Strategic)** | Capability trajectory. Risk register. Competitive position. Capital efficiency. | Roadmap detail. Prompt-level debate. | Is the company investing the right amount in the right capability? |

**The mandatory translation rule:** the exec view and the engineering view of the same feature must reconcile to the same eval number. If the exec hears "94% accuracy" and engineering hears "92% on heldout, 87% on out-of-distribution," you have a credibility bomb on a fuse. Pick one number, define it once, frame it in each audience's language.

## THE 5 COMMUNICATION TYPES

### 1. Executive Summary

**When to use:** A decision is needed from leadership, or leadership awareness is required for an event they will be asked about externally. Never both in the same note — pick one.

**Structure (Pyramid Principle / Minto SCR):**
- **Bottom line (one sentence):** "We are on track / at risk / off track on [initiative], because [boundary condition]. Decision needed: [yes/no on specific ask]."
- **Situation:** Where things stand in two sentences.
- **Complication:** What changed or what's in the way. Specific, not "execution challenges."
- **Resolution / Recommendation:** What you're doing about it, and what you need from leadership.
- **AI evidence anchor:** One line. "Eval as of [date]: 91% accuracy on labeled set N=400, degrades to 78% on long-tail queries. Drift watch: weekly. Fallback: rules engine + human review."

**Length:** 150 words. If it's longer than the executive's screen without scrolling, cut it.

**Anti-patterns:**
- "We've made significant progress" with no number behind it
- Five risks listed equally without a recommended priority
- Decision needed and awareness mixed in the same note (the exec will only act on one)
- AI claim with no eval anchor ("model is performing well")

### 2. Engineering Brief

**When to use:** A decision affects what engineering builds, instruments, or reviews this sprint. Or engineering needs context to make better implementation choices on something already in flight.

**Structure (Context-first):**
- **Why this matters (2 sentences):** The user problem and the structural reason this is the right approach.
- **Current state:** What's shipped, what's in flight, what's blocked. Owners and ETAs.
- **The eval matrix:** The actual table. Accuracy by class, latency P50/P95/P99, hallucination rate, cost per inference. Linked to the dashboard.
- **The prompt diff:** What changed since last shipped version. Why. What regressed in evals, what improved.
- **Open architecture questions:** What you need engineering input on *before* the next decision point.
- **What's not changing:** Important. Engineers anchor on stability — explicitly call out the contract that's stable.

**Length:** 400-700 words. Engineers expect more density and less polish than execs.

**Anti-patterns:**
- Marketing language ("game-changing model upgrade")
- Eval claims without methodology or sample size
- "We need to discuss" without a specific question
- Hiding regressions ("v2.1 ships Friday" with no mention that confidence calibration got worse)

### 3. Launch Announcement

**When to use:** Feature is shipping to customers, or a new capability is going GA. Required: an internal version (sales, support, success) and an external version (customer-facing).

**Structure (Narrative):**
- **The user moment:** Open with the situation the user is in when this matters. Not "We are excited to announce." A specific user, a specific Tuesday afternoon.
- **What it does:** Plain language, benefit-first. "You can now..." not "The system supports..."
- **What it doesn't do (mandatory for AI features):** The boundary condition. "It works well for X. It's not designed for Y. If you're trying to do Z, here's the workaround."
- **What happens when it's wrong:** The fallback. The human-in-the-loop. The override. AI features that don't show their failure path lose customer trust the first time the model misfires.
- **How to give feedback:** A real channel. Not "let us know." A link, a name, a Slack channel.

**Internal version adds:**
- Eval results customers don't need to see (the actual confidence band, the regression test status)
- Sales talking points and objection handling
- Support escalation path for the failure mode that *will* happen in week two

**Anti-patterns:**
- AI feature launch with no boundary condition stated
- Confidence claim ("highly accurate," "industry-leading") with no number, no segment, no methodology
- Hiding the human-in-the-loop because "it sounds less impressive"
- Same copy for internal and external (sales needs different evidence than customers)

### 4. Risk Escalation

**When to use:** A model regressed, an eval gate failed, a drift threshold tripped, or a launch is at risk because of an AI-specific issue. Bias toward escalating early — surfacing a 60% probability problem at week two beats surfacing a 100% certain problem at week six.

**Structure (Calm, factual, options-first):**
- **What happened (one paragraph):** Specific incident or trend. Date, scope, magnitude. "Acceptance rate dropped from 78% to 64% over the last 14 days on the enterprise segment, isolated to queries with >2 entities."
- **What we know vs. what we're still figuring out:** Be honest about the uncertainty. "We've ruled out token cost spike and prompt regression. We're testing whether it correlates with the data refresh on March 12."
- **Impact assessment:** Who is affected. What's the revenue / trust / regulatory exposure. Quantify wherever the data exists.
- **Options table:** Three options minimum. For each: action, cost (time, money, opportunity), upside, downside, confidence.
- **Recommendation:** Which option, why, and what would change your mind.
- **Decision needed by:** A real date, with the cost of waiting longer.

**Length:** 300-500 words. Resist the urge to overpad.

**Anti-patterns:**
- Escalating a problem with no recommended action (managers stop reading after the third "we need to discuss")
- Burying the impact in the third paragraph
- Vague magnitude ("significant impact") instead of "$420K of pipeline at risk"
- Claiming certainty you don't have ("model is broken") instead of "we're 70% confident the regression is in the retrieval layer, not the model"

### 5. Weekly Digest

**When to use:** Recurring cadence (Friday EOD or Monday AM) for a stable audience. The point is not novelty — the point is signal continuity. People should be able to skip three weeks and re-enter at week four without confusion.

**Structure:**
- **TL;DR (3 sentences):** What shipped. What's at risk. What you need from them.
- **Shipped this week:** Specifics with impact. Not "Released v2.4." Instead: "Released v2.4 — confidence calibration improved (overconfidence rate 12% → 6%). No regressions on top-100 queries."
- **In flight:** What's progressing, what's blocked, what changed direction. Owners, ETAs.
- **Eval state (for AI features):** One-line per active model. "Recommendation engine v3.1 — 91% acceptance on heldout, drift watch green, no incidents."
- **Risks (top 3 only):** Age, owner, action. If a risk has been on the list for 3+ weeks with no movement, escalate it inside the digest.
- **Asks (specific):** What you need from each named stakeholder this week.
- **Next week's focus:** What's the one thing that matters.

**Length:** 400 words target. The discipline of keeping it short forces prioritization.

**Anti-patterns:**
- Activity log instead of decision log ("we had three meetings on X")
- Risks aging quietly week after week with no escalation
- "All green" status that's lying — execs lose trust the first time the digest said green and the launch slipped
- AI features without an eval state line (signals the PM isn't watching)

## AI-NATIVE CONFIDENCE FRAMING

This is the section that separates a PM who can ship AI features in a large industrial enterprise scale from a PM who once wrote a Medium post about LLMs.

### The non-negotiable trio

Every claim about an AI feature in any stakeholder communication carries three things. If any one is missing, the comm is incomplete:

**1. The eval-backed confidence band.** Not "highly accurate." Not even "94% accurate." The right form is: *"91% accuracy on N=400 labeled queries from production sample, March 1-15. Degrades to 78% on long-tail queries (>2 entities, ambiguous intent). Confidence calibration verified — model is not overconfident on errors."*

The shape: number + sample size + segment + methodology + calibration check. Without those five, "94% accuracy" is a marketing slogan, not evidence.

**2. The named drift surface.** Where will this number degrade? When? How fast? What's watching for it? *"Drift watch: daily eval on production sample, alert if accuracy drops >3% week-over-week. Most likely drift cause: shift in query distribution as we onboard the manufacturing segment in Q2."*

If you can't name where the model will degrade, you don't understand the model. If you don't know who's watching, you're not running a production AI feature — you're running a demo.

**3. The "what could be wrong" section.** Mandatory in every AI-feature comm to executives, board, customers above a certain trust threshold, or anywhere the model's claim could be quoted back at you. Format:
- *What is the model wrong about today, that we know?* (Known boundaries.)
- *What might it become wrong about, that we don't yet know?* (Unknown boundaries — open evals, watch list.)
- *What happens when it's wrong?* (Fallback path, human-in-the-loop, escalation rule.)

A PM who omits this section is gambling that the model never fails publicly. The model will fail publicly. When it does, the question is whether you said so before or after.

### Audience-specific framing of the same evidence

Same eval result. Three audiences. Three legitimate framings:

**Engineer hears:** "Production sample N=400, March 1-15, accuracy 91% (CI 88-93%). Long-tail bucket (>2 entities) drops to 78%. Calibration: ECE 0.04, no overconfidence on errors. Drift watch: daily eval, alert at -3pp WoW. Last regression: v2.4 on 2026-03-08, retrieval ranking change, contained in 36 hours."

**Exec hears:** "The model is right 9 out of 10 times on the use cases we shipped for, and we know which 1 of 10 it gets wrong. We watch for degradation daily and we have a rules-based fallback if it ever drops below the threshold. The boundary is queries with more than two entities — for those, we hand off to a human reviewer. Cost trajectory and trust trajectory both holding."

**Customer hears:** "When you ask a question with one or two clear entities, the assistant gives you an answer right away. When the question is more complex or ambiguous, you'll see a 'review with a specialist' option instead of a guess. You can override any answer with one click — your override teaches the system."

Three framings. One eval matrix underneath. The PM who can do this without losing fidelity is a PM you trust to ship.

### Drift watch language — what it actually sounds like

PMs lose credibility when they describe drift as if it's hypothetical. It is not. It is happening to your model right now. The language that signals you know this:

- "The model has been live for 47 days. Acceptance rate has held within a 3pp band. We expect drift when [specific event] — the manufacturing segment onboards in Q2, which will shift query distribution by an estimated 15-20%. We've pre-built a regression test for that distribution and we'll re-baseline after week one of onboarding."
- Not: "We monitor for drift."

### Model-version specificity

Every AI claim names the model version, the prompt version, and the eval date. Without those three, future-you cannot reconstruct what was true when you wrote the claim. *"Recommendation engine v3.1.2, prompt v2.4-prod, evals as of 2026-03-15"* — that's the form. Saying "the model" is how PRDs become unfalsifiable later.

### Eval-backed claims vs hand-waving

| Hand-waving | Eval-backed |
|---|---|
| "The model is highly accurate" | "91% on the heldout set N=400, methodology in [link]" |
| "We've improved performance" | "Acceptance rate up 8pp WoW on the enterprise segment, no regression on consumer" |
| "Hallucination is rare" | "Factual consistency 98.2% on RAG outputs, measured against source docs, N=200" |
| "Latency is good" | "P50 180ms, P95 480ms, P99 1.1s on production traffic, last 7 days" |
| "Users love it" | "Acceptance rate 78% on first-pass output, regeneration rate 7%, feature CSAT 4.4 (n=312)" |

The discipline: never let a hand-waving claim into a stakeholder comm. The first time someone calls you on it, your credibility on every other claim drops.

## REAL-WORLD ENTERPRISE-SCALE EXAMPLES

### Example 1: Shipping an AI feature to skeptical execs

**Context:** A predictive maintenance assistant launching to plant managers. The CFO has historically been skeptical — last AI initiative two years ago overpromised and the model degraded inside six months.

**Wrong move:** Lead with the 92% accuracy number and the demo video.

**Right move (exec summary, 140 words):**

> Predictive maintenance assistant goes GA on April 8. Decision needed: confirmation that the rollout sequence (3 plants → 12 plants → all 47) is acceptable.
>
> The boundary condition: the model achieves 91% precision on the 312 fault patterns we trained on, and falls back to the existing rules engine on patterns it has not seen. Eval matrix and drift dashboard linked below. Watch is daily.
>
> What could be wrong: the manufacturing query distribution differs from the training set; we have a pre-built regression test for that, and the rollout sequence is paced to catch drift inside week one of each new plant.
>
> Cost: $0.12 per assisted decision at current scale, holding under $0.20 at 10x. Trust trajectory: plant managers in pilot accepted 78% of recommendations without modification.
>
> Recommendation: proceed with the staged rollout. Default to rules engine if any plant's acceptance drops below 60% in week one.

Why this works: the CFO's prior bad experience is acknowledged structurally (the model has a known boundary, the watch is real, the fallback is concrete). No "highly accurate." No demo video. A boundary, a fallback, a number with a methodology.

### Example 2: Escalating a model failure to leadership

**Context:** Acceptance rate on the enterprise segment dropped 14 percentage points over two weeks. The cause is unclear. Board update is in nine days.

**Wrong move:** Wait three more days hoping the team finds the root cause.

**Right move (risk escalation, 380 words):**

> **What happened:** Acceptance rate on the recommendation engine dropped from 78% to 64% on the enterprise segment over the last 14 days. Consumer segment unaffected. Confidence calibration unchanged.
>
> **What we know:** The drop correlates with the March 12 data refresh — the catalog grew by 23% with new SKUs that have sparse engagement data. We have ruled out prompt regression (v2.4 unchanged), token cost spike (within 4% of baseline), and infrastructure (latency P95 stable at 480ms).
>
> **What we're still figuring out:** Whether the issue is in the retrieval layer (sparse data → low-quality candidates) or the ranking layer (the model overweights popularity). 70% confident it's retrieval. Test running through Friday.
>
> **Impact:** $420K of enterprise renewal pipeline touches the recommendation surface in Q2. Two enterprise champions have flagged the regression. Board update is on April 4.
>
> **Options:**
>
> | Option | Action | Cost | Upside | Downside | Confidence |
> |---|---|---|---|---|---|
> | A | Roll back catalog refresh until retrieval is fixed | 1 day eng + sales explanation to 40 enterprise accounts | Immediate restore of acceptance rate | Lose 23% of new SKU coverage; sales hates it | High |
> | B | Patch retrieval with a popularity-floor heuristic, ship by Wednesday | 2 days eng | Likely 80% restore by board update | Won't fully recover; partial fix carries forward | Medium-high |
> | C | Wait for full root cause before any fix | 0 immediate cost | Permanent fix the first time | Board update lands during the regression; trust hit larger | Low |
>
> **Recommendation:** Option B. The 80% restore by board update preserves trust while the team finishes root cause for a permanent fix in the next sprint. Would change my mind if Friday's test shows it's actually in the ranking layer — then Option A.
>
> **Decision needed by:** EOD Tuesday. Cost of waiting until Wednesday: ship moves to Friday, board update lands red.

Why this works: a 70% confidence claim is honest, three options force a real decision, the recommendation is named, the kill condition is named. A leader can act on this in five minutes.

### Example 3: Weekly digest when the AI feature regressed

**Context:** The week the recommendation engine started drifting. Same digest cadence as always, but the news is bad.

**Wrong move:** Bury it under the good news. Use vague language. Frame it as "monitoring continues."

**Right move (weekly digest, 350 words):**

> **TL;DR:** Recommendation engine acceptance dropped 14pp on enterprise (Option B patch ships Wednesday). Predictive maintenance pilot expanded to plant 4. Need exec sign-off on the staged rollout sequence by Friday.
>
> **Shipped this week:**
> - Predictive maintenance pilot: plant 4 onboarded, 78% acceptance week 1, no incidents.
> - Vendor risk dashboard: alerting integrated with PagerDuty, deployed to ops.
>
> **In flight:**
> - Recommendation engine — patch v2.4.1 in eng, ship Wednesday, target 80% acceptance restore.
> - Onboarding flow refactor — design review Tuesday, no AI dependencies.
>
> **Eval state:**
> - Recommendation engine v2.4 — 64% acceptance enterprise (down from 78%, 14d trend), drift watch RED, root cause 70% retrieval / 30% ranking, full root cause Friday.
> - Predictive maintenance v1.0 — 78% acceptance plant 4, drift watch GREEN, eval baseline holding.
> - Vendor risk classifier v3.2 — 94% precision holding, drift watch GREEN.
>
> **Risks (top 3):**
> 1. **Recommendation engine regression** — 14d old, owner: me, action: Option B patch ships Wednesday, board update preserved.
> 2. **Plant 4 onboarding window** — 7d to plant 5 cutover, owner: ops lead, action: confirm rollout sequence with VP Ops by Friday.
> 3. **Vendor risk model drift watch instrumentation gap** — 21d old, owner: eng lead, action: escalating into next sprint, drift would surface in eval but not in dashboard.
>
> **Asks:**
> - **CFO:** approve the staged rollout sequence for predictive maintenance (3 → 12 → 47) by Friday.
> - **VP Eng:** review the recommendation engine root cause doc Tuesday before Wednesday ship.
> - **VP Sales:** align on customer comms for the recommendation patch — we have two enterprise champions flagging it.
>
> **Next week's focus:** Recommendation engine restore + predictive maintenance plant 5.

Why this works: the bad news leads. The eval state is specific. The risks are aged and owned. The asks are named. No "monitoring continues." A reader who skipped the last two weeks can re-enter cleanly.

### Example 4: Launch comm when AI confidence is below target

**Context:** A summarization feature is shipping to customers. Eval shows 87% acceptance on the labeled set against an 88% target. The CMO wants to ship for an event next Tuesday. The PM has to decide what to say in the launch announcement.

**Wrong move:** Pretend the gap doesn't exist. Or hold the launch over 1 percentage point.

**Right move (customer-facing launch comm, 220 words):**

> **Tuesday morning. You open a 40-page contract. The summary is at the top.**
>
> Starting today, the assistant generates a draft summary for any document in your workspace. Headlines, parties, dates, obligations, risk flags — surfaced at the top so you can decide where to read closely.
>
> **What it's good at:** Standard contract structures, vendor agreements, NDAs, SOWs. The assistant has been evaluated on 312 documents across these categories with 87% accuracy. We will continue to improve this on the categories you use most.
>
> **What it's not designed for yet:** Multi-party agreements with nested obligations, contracts in languages other than English, and contracts longer than 80 pages. For these, the assistant will offer a "review with a specialist" option instead of a guess.
>
> **What happens when it's wrong:** Every summary line is one-click overridable. Your override is logged and used to improve future summaries. If you see a wrong summary on a high-stakes contract, flag it with the "report" button — these go directly to the team.
>
> **Available now in the document workspace.** Beta label stays until we hit 92% accuracy on the labeled set. We'll let you know when we get there.

Why this works: the 87% number is named. The boundary is named. The fallback is named. The override is named. The "we'll tell you when we hit 92%" line earns trust by setting a transparent quality bar customers can hold the team to. The CMO got a launch on Tuesday. The PM kept the credibility for the next launch.

## QUALITY GATE

Before sending any AI-feature stakeholder communication, the following ten items must all be true. Any "no" sends the comm back for a rewrite.

- [ ] **One audience, one purpose.** This comm is targeted at one audience tier with one decision or awareness purpose, not a hybrid.
- [ ] **The bottom-line fits in the first sentence.** A reader who stops after sentence one knows what's happening and what's being asked.
- [ ] **Every AI claim has a number.** No "highly accurate," no "performing well." Every claim is anchored to an eval number with sample size, segment, methodology.
- [ ] **The boundary condition is stated.** What the model is good at AND what it's not good at, in language the audience can act on.
- [ ] **The drift surface is named.** Where will this number degrade? Who's watching? What triggers escalation?
- [ ] **The "what could be wrong" section exists.** Known boundaries + unknown boundaries + fallback path. Mandatory for exec, board, and external customer comms.
- [ ] **Model and prompt versions are named.** Future-you can reconstruct what was true when this was written.
- [ ] **A specific ask is in the comm.** Either a decision the reader needs to make, or an action they need to take, with a real date.
- [ ] **No banned language.** No "leverage," "robust," "seamless," "transformative," "game-changing," "comprehensive ecosystem." No "in today's fast-paced world." No "it is important to note that."
- [ ] **Reconciliation check.** If the same evidence is being framed for a different audience, the underlying number reconciles. The exec view and the engineering view must point to the same eval matrix.

## DELIVERABLE FORMAT

The skill produces output in the following structure. Always.

```
## [Communication Type]: [Topic]
**Audience:** [Executive / Engineering / Cross-functional / Customer / Board]
**Purpose:** [Decision needed / Awareness / Action required]
**Model and prompt version:** [if AI feature — name them]
**Evidence date:** [date of the eval / metric snapshot underneath the comm]

[Body — formatted per communication type]

---

## Communication Notes
- **Tone:** [chosen tone, why]
- **Boundary condition stated:** [yes/no — if AI feature, must be yes]
- **Drift surface named:** [yes/no — if AI feature with eval claim, must be yes]
- **What-could-be-wrong section:** [included / not applicable, with reason]
- **Sensitivities flagged:** [anything stakeholder-specific to be careful about]
- **Suggested follow-up:** [next comm or action this triggers]
- **Reconciliation:** [if multi-audience, the underlying eval anchor that all versions trace back to]
```

When producing multi-audience comms in the same session, output each variant fully, separated by clear audience labels, and end with the reconciliation note showing the single eval anchor underneath all three.

## RED TEAM

This skill is wrong, or should be bypassed, when:

- **The feature is deterministic.** Rules engine, integration, CRUD launch. Forcing AI-native confidence framing onto a deterministic feature is theater that erodes credibility.
- **You're communicating internal team activity, not stakeholder decisions.** Standup notes, sprint planning, design crit. Use lighter-weight formats — this skill's overhead is wasted.
- **The audience is technically junior in AI but the comm is being treated as introductory training.** A new exec who has never seen a confidence band needs onboarding before this skill helps. Run the explanation conversation first; come back to this skill when they're ready to act on the evidence.
- **The eval evidence does not exist yet.** This skill assumes you have an eval matrix to anchor to. If you don't, you're not ready to communicate — you're ready to build the eval. Use `eval-framework` first.
- **The audience explicitly asked for a casual update.** A peer DM, a "just FYI" Slack note. Forcing the structure into casual comms makes the PM look like they only have one mode.
- **Speed-to-decision dominates polish.** A 2-line slack to unblock something in the next 30 minutes shouldn't go through this skill's structure. Send the 2 lines.

The signal you've over-applied this skill: people start saying "the AI launch comms feel formulaic." That's a real cost. Use the skill where it earns its weight; bypass it where it doesn't.

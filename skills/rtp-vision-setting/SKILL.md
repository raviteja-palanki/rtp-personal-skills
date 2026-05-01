---
name: rtp-vision-setting
description: >
  Articulate the aspirational picture of what the world looks like when an AI product wins. Vision is not strategy (how) and not roadmap (what) — it's the destination that makes strategy and roadmap choices obvious. Use when starting a new initiative, refining an existing vision, preparing a board / all-hands deck, or when the team can't agree on priorities (the symptom of a missing vision). Triggers on "product vision," "long-term vision," "where are we going," "3-year vision," "vision statement," "north star vision," "the destination."
imports:
  - purpose-dialogue
  - strategy-canvas
  - first-principles
  - signal-scanner
---

# Vision Setting

Vision is not strategy. Vision is not roadmap. Vision is the destination — the picture of the user's transformed work or life when the product wins. Strategy is how you get there. Roadmap is what you build next. Mix them up and you get a roadmap pretending to be a vision (a feature list with aspirational verbs in front of it) or a vision pretending to be a strategy (a poster on the wall that nobody can act on).

This skill exists because most AI product visions written today won't survive 18 months. They're capability-anchored ("we use the best model to..."), feature-listed ("we have summarization, search, and Q&A"), or competitor-mirrored ("the OpenAI for X"). They die the moment the next model ships. The 0.1% angle is durability across model generations — vision built on what HUMANS DO with AI, not what AI does.

---

## DEPTH DECISION

**Go deep (full exercise, 2-3 weeks):**
- Starting a new product or business unit from zero
- Major pivot — the previous bet didn't work and the team needs a new destination
- Post-fundraise — the capital changes ambition, and the vision needs to scale to the new altitude
- Pre-board cycle for a product crossing $10M ARR or 100k DAU — the vision is now a stakeholder artifact, not just an internal compass
- The team can't agree on priorities. This is almost always the symptom of a missing or stale vision, not a prioritization problem.

**Lighter touch (refresh, 1 week):**
- Annual vision cycle on an existing product where direction is stable
- New CPO / VP Product joining and inheriting the existing vision — they need to test whether to keep, sharpen, or replace
- The current vision is 18+ months old and AI capability has shifted underneath it (almost certain)

**Skip:**
- Pre-PMF startups still hunting the problem. Vision before problem validation is decoration. Use first-principles and run problem-hypothesis tests instead.
- Mature consumer products in commodity categories where execution is the bottleneck. A new vision won't fix a slow checkout flow.
- Teams in survival mode (runway under 6 months, recent layoff). Vision becomes distraction from execution. Stabilize first.

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who specifically benefits? What changes in their work or life? What timeframe?
2. Route depth: Full exercise or refresh?
3. Identify output format: Document, presentation, or both?

Then proceed with the skill-specific analysis below.

---

## THE STRUCTURAL INSIGHT — WHY MOST AI PRODUCT VISIONS DON'T SURVIVE 18 MONTHS

Most vision statements describe a future state that's already obsolete by the time it ships. AI capability is moving in 6-month cycles. Vision must be **durable across model generations** — and most aren't.

The 0.1% angle: a good AI product vision is durable when both conditions hold.

**Condition 1 — It's about what HUMANS DO with AI, not what AI does.**

A vision like "We use AI to summarize documents" is a feature description with a verb tense problem. The moment summarization becomes a default capability of every model (it already has), the vision is meaningless. Compare to "Knowledge workers think clearly under pressure." That sentence doesn't break when GPT-6 ships. It doesn't break when summarization becomes free. The human transformation — clearer thinking under pressure — survives any model generation because it's anchored to a human need, not a model capability.

**Condition 2 — It survives a 10x improvement in capability without becoming trivial AND a 10x cost increase without becoming impossible.**

The 10x-better test: if models become 10x more capable, does your vision still mean something? If the answer is "no, because everyone can do this now" — the vision was a feature, not a destination.

The 10x-cost test: if inference costs spike 10x (regulatory, supply, energy), does your vision still motivate? If the answer is "no, because we couldn't afford to deliver it" — the vision was a price-point bet, not a transformation.

A durable vision passes both. It says: even when AI is much better, the human transformation we're after is meaningful. Even when AI is much more expensive, the value of that transformation is worth paying for.

**The retroactive test:** read your vision out loud. Does it sound like "GPT-3 era" five years from now? "We use AI to..." sentences age badly. "People do X..." sentences age well.

**Worked example:**
- Bad: "We use AI to summarize documents." → Obsolete the moment context windows hit 1M tokens. Already happened.
- Good: "We help knowledge workers think clearly under pressure." → Still true if AI becomes 10x better (the help just gets sharper) AND if AI becomes 10x more expensive (the pressure-thinking job is more valuable than the cost). Survives Claude 6, GPT-7, whatever comes next.

This is the structural insight. Most PM books miss it because they were written before AI capability moved at this speed. The principle generalizes: anchor on the durable human transformation, treat capability as the changing means.

---

## THE 5-TEST VISION FRAME (Cagan / Doshi / Bavaro composite)

A vision that fails any of these tests is a draft, not a vision. Run all five before locking.

### 1. Aspirational

**Definition:** Describes a future state, not a current state or a plan. The future state is meaningfully different from today.

**AI-product example:** "Plant operators ship a shift with confidence, not anxiety — every machine that's about to fail tells them why." (Future state, different from today's reactive maintenance.)

**Common failure:** Disguised current state. "We provide AI-powered insights to operators" — that's what we do today. Where's the destination? If a stranger reads it and says "okay, sounds like a normal product," the aspirational test failed.

### 2. Specific

**Definition:** Names who benefits and how. "Everyone" is not a valid answer. The user segment is concrete enough that you could find a real person who fits.

**AI-product example:** "Solo legal practitioners handle the workload of a 4-person firm without burning out." (Specific user: solo practitioners. Specific transformation: 4-person workload, no burnout.)

**Common failure:** "We help businesses be more productive." Who? Which businesses? Productive at what? If three different people reading the vision picture three different users, the specific test failed.

### 3. Durable

**Definition:** Directionally right 3-5 years from now, even when tactics change. Survives model generation shifts.

**AI-product example:** "Hospital pharmacists catch every drug interaction risk before it reaches the patient." (Still true in 5 years regardless of which AI model is doing the catching.)

**Common failure:** "We use Claude to..." or "Our GPT-4-powered platform..." The capability anchor dates the vision the day it's written. When the model changes — and it will — the vision feels stale even if the underlying ambition is intact.

### 4. Differentiating

**Definition:** Distinct from what competitors would say. Someone reading the vision should be able to identify the company without seeing the logo.

**AI-product example:** "Field engineers at industrial sites diagnose any machine they've never seen before, in 5 minutes, using only what they can see and hear." (a Fortune 100 enterprise-shaped. Doesn't fit Microsoft or OpenAI or a generic SaaS company.)

**Common failure:** "We're building the leading AI platform for [industry]." This is the same sentence every competitor would write with their industry swapped in. If you can copy a competitor's vision, change two words, and it describes you — the differentiating test failed.

### 5. Motivating

**Definition:** Makes smart people want to work here AND choose this product. The vision creates pull, not push.

**AI-product example:** "We're the reason a 60-year-old plant operator decides to keep working past retirement — because the job finally feels like it respects their judgment instead of replacing it." (Engineers want to build this. Operators want to use it. There's an emotional center.)

**Common failure:** "We deliver value to enterprise customers through AI-powered productivity gains." Nobody quits a stable job to work on this sentence. If reading the vision out loud feels like reading a corporate boilerplate, the motivating test failed.

---

## VISION INPUTS — THE THREE CLARIFICATIONS BEFORE WRITING

Don't write a vision until you can answer these three. If any are blurry, the vision will be too. Ask one targeted question at a time — don't blast all three.

### The user — who specifically benefits?

"Everyone" is not valid. "Knowledge workers" is closer but still vague. "Senior associates at mid-tier law firms who bill 60+ hours and lose nights to discovery review" is specific enough to picture a person.

The test: name three real customers (real or composite) who fit the segment. If you can't, the user is too abstract.

### The transformation — what changes in their work or life when the product wins?

Not what the product does — what changes for the user. Before/after framing helps:
- Before: associate spends 3 nights a week on document review, misses kid's bedtime, considers leaving the firm
- After: review takes 90 minutes, associate is home for dinner, retention up across the cohort

The transformation must be felt, not measured. Metrics come later. The vision is the human change.

### The timeframe — calibrate ambition to scope

| Horizon | Use when | Ambition calibration |
|---|---|---|
| **1-year tactical vision** | The team needs an alignment artifact for the next planning cycle | Must be achievable with current capability + 1-2 model generation improvements. Sober. |
| **3-year strategic vision** | Default for most product visions | Assumes 3-4 model generations, 5-10x cost reduction, regulatory framework still recognizable. The right altitude for board decks and roadmap anchoring. |
| **10-year aspirational vision** | Founder-level, industry-level. Used when defining the company's reason to exist. | Assumes capability will be unrecognizable. Anchor purely on the human transformation. |

Wrong horizon is the most common silent failure. A 3-year vision written at 1-year ambition reads timid. A 1-year vision written at 10-year ambition reads detached. Match the horizon to the audience and the moment.

---

## THE THREE-DRAFT METHOD

Write three versions of every vision. Each serves a different audience and stress-tests the underlying idea from a different angle. If the three drafts feel inconsistent with each other, the vision isn't sharp yet.

### Draft 1 — Narrative version (3-5 sentences)

Tells the story of the user's transformed work or life. Reads like a paragraph from a future case study.

**Example:** "It's Tuesday morning at the plant. Rajesh, the shift lead, walks the floor with a tablet that already knows what's about to fail. The compressor on Line 3 has been drifting for 11 days — vibration signature, oil temperature, current draw — and the system tells him *why* before it tells him *what*. He schedules the repair for the planned maintenance window two days out, instead of after the shutdown. He goes home on time."

This draft is the emotional spine. It's what you read before the all-hands.

### Draft 2 — Headline version (15 words or less)

The billboard. The thing that fits on a t-shirt or above a slide.

**Example:** "Plant operators ship a shift with confidence, not anxiety — every failure tells them why."

This draft is the compression test. If the vision can't compress to 15 words without losing its soul, it's not sharp yet. The narrative version supplies the depth; the headline supplies the recall.

### Draft 3 — Team version (internal use)

For the people building it. Three sections, each tight.

- **Why this matters:** The structural problem you're solving and why now is the moment.
- **Who it serves:** The specific user, not the market category.
- **What winning looks like:** Three concrete signals you'd see when the vision is realized — not metrics, signals.

**Example:**
> **Why this matters.** Industrial unplanned downtime costs $50B/year in the US alone. The reason isn't sensor data — every plant has it. The reason is interpretation. Operators get a wall of red lights and no narrative. We close that gap.
>
> **Who it serves.** Plant operators with 10-30 years of experience whose intuition is being underused because the tools don't speak their language. Not the data scientist. Not the executive dashboard. The operator on the floor.
>
> **What winning looks like.** (1) An operator says "I trust this more than the gut feeling I had 20 years ago, and that's saying something." (2) Plants reduce unplanned downtime by half within 18 months of deployment. (3) a Fortune 100 enterprise's name comes up in industry conversations as the company that respected operator judgment instead of replacing it.

This draft is what survives the 47th Slack reorg.

### For each draft — the cuts test

After writing each draft, name two things explicitly:

1. **What this makes obviously prioritized.** Specific roadmap items that should accelerate.
2. **What this makes obviously out-of-scope.** Specific roadmap items that should die.

If the cuts aren't obvious — if you read the vision and the current roadmap and can't tell which 30% of items should go — the vision isn't sharp enough. Vague visions don't make decisions easier; they preserve the status quo with extra words.

**The 30% rule:** A sharp vision makes at least 30% of the current roadmap look obviously wrong. If your vision validates 100% of the current roadmap, it's a description, not a decision.

---

## THE STRATEGY COHERENCE CHECK

Vision without coherence is decoration. After locking the vision, audit:

### Does the current roadmap point toward this vision?

Pull the Now / Next / Later list. For each item, ask: does this move toward the vision, or sideways? Items that move sideways fall into two buckets:
- **Cover fire:** Justified non-strategic work (tech debt, regulatory must-do, key customer save). Tag it, time-box it.
- **Misaligned:** Doing the item well does not get closer to the vision. These are the conversations to have.

### Are at least 60% of next-quarter bets directly serving the vision?

If under 60% — the vision is decorative. The team is committed to other things. Either the vision is wrong (it doesn't reflect what people actually believe matters), or the prioritization is wrong (the team is busy on the urgent at the cost of the important).

The 60% threshold is calibrated for AI product teams. Pure execution teams (mature SaaS) can run higher (75%+). Discovery-stage teams can run lower (40-50%) because exploration bets often look "off-vision" but are actually testing the vision.

### Is there an active bet that contradicts the vision?

Not "doesn't help" — actively contradicts. A vision that says "operators trust the system because it explains itself" while the team is shipping a black-box recommendation engine has an internal contradiction. Either kill the bet, or update the vision. Coexisting contradictions corrode trust faster than any other strategic flaw — the team senses the inconsistency even when nobody names it.

The output of this check is one of three:
- **Coherent:** Roadmap and vision agree. Move on.
- **Drifting:** Roadmap is mostly aligned but with 1-2 contradicting bets. Make the call.
- **Disconnected:** Vision and roadmap are different conversations. The team has been operating without a real vision and the new one needs to be earned, not announced.

---

## VISION FOR AI PRODUCTS — THE FOUR FAILURE MODES

These are the four ways AI product visions die. Each has a tell, a fix, and a durable shape.

### Failure mode 1 — Capability-anchored vision

**Example:** "We use GPT-4 to deliver enterprise-grade summarization."

**How to detect:** The vision names a specific model, capability ("summarization"), or technique ("RAG", "fine-tuning"). The vision document mentions vendor names. Reading it, you can tell what year it was written.

**Why it dies:** The model gets replaced (Claude 5 ships, GPT-6 ships). The capability commoditizes (every model can summarize now). The vision feels stale within 6 months and embarrassing within 18.

**How to fix:** Translate the capability into the human transformation it enables. "GPT-4 summarization" → "Lawyers walk into Monday morning already knowing what mattered in 200 hours of weekend depositions." The vision now survives the GPT-4 → Claude 5 transition because the transformation is what matters, not the engine.

**Durable shape:** Anchored on what the user can now DO that they couldn't do before. The model is the means; the doing is the destination.

### Failure mode 2 — Feature-list vision

**Example:** "Our platform offers summarization, search, Q&A, document generation, and translation."

**How to detect:** The vision contains the word "and" three or more times. It reads like the product page. There's no transformation, just a catalog.

**Why it dies:** A roadmap pretending to be a vision. It tells the team what to build (the list), not where they're going (the destination). When the list grows, the vision dilutes. When the list changes, the vision changes. There's no anchor.

**How to fix:** Ask "if we had all five features and they all worked perfectly, what would the user be able to do?" That answer is the vision. The list of features is the means.

**Durable shape:** A single transformation statement. The features are the implementation. They live on the roadmap, not in the vision.

### Failure mode 3 — Industry-jargon vision

**Example:** "AI-powered enterprise productivity for digital transformation."

**How to detect:** Strip every word that's industry-buzzword. What's left? If the answer is "almost nothing," the vision was 80% noise. The sentence could describe Microsoft, Salesforce, ServiceNow, or a generic startup with no changes.

**Why it dies:** It says nothing. The team can't make a decision from it. The customer doesn't know what's different about you. The board nods politely and moves on.

**How to fix:** Run the "explain it to your grandmother" test. State the vision using only words a non-technical family member would understand. If you can't, you don't have a vision — you have a press release.

**Durable shape:** Plain language. Concrete user. Concrete change. No words that require context to understand.

### Failure mode 4 — Competitor-mirror vision

**Example:** "We're the OpenAI for healthcare." Or: "The Bloomberg Terminal for legal."

**How to detect:** The vision borrows the shape of a successful competitor and substitutes the domain. The construction "the X for Y" is the giveaway.

**Why it dies:** It tells nobody what you do *differently*. It tells investors you're a copy with a vertical bet. It tells the team to imitate, not innovate. And when the original (OpenAI, Bloomberg) enters your vertical, you have nothing distinct to defend.

**How to fix:** State the vision in your own terms. What's the human transformation in your domain that the analog doesn't capture? "OpenAI for healthcare" might really mean "every primary care physician sees one fewer hour of charting per day, and uses that hour with the patient." That sentence is yours. "OpenAI for healthcare" is borrowed.

**Durable shape:** The vision describes your wedge in a way that doesn't depend on someone else's brand for legitimacy.

---

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

Setting: industrial predictive maintenance AI product, mid-2024. Existing vision on the wall: **"AI-powered predictive maintenance for industrial customers."**

### The diagnosis

Run the 5-test frame on the existing vision.

| Test | Pass / Fail | Reason |
|---|---|---|
| Aspirational | Fail | Describes current state. a Fortune 100 enterprise already does predictive maintenance. The "AI-powered" prefix doesn't change the destination. |
| Specific | Fail | "Industrial customers" — which? Refineries, chemical plants, food processing, aerospace? Each has a different operator, different failure mode, different value prop. The vision serves none of them. |
| Durable | Fail | "AI-powered" dates the vision to the 2023-2024 capability era. In 2027 every product is AI-powered; the modifier becomes meaningless. |
| Differentiating | Fail | GE, Siemens, Schneider, ABB, Rockwell could all use this exact sentence. The vision doesn't identify the company. |
| Motivating | Fail | Reads like a corporate boilerplate. No engineer chooses to work on this sentence. No operator chooses to buy from it. |

**Diagnosis:** Capability-anchored ("AI-powered") + industry-jargon ("predictive maintenance for industrial customers"). Two of the four failure modes in one statement. Score: 0/5 on the test frame.

This is the realistic Fortune-100-grade enterprise condition. The vision exists. It's on a poster. Nobody believes it. The team can't use it to prioritize. The starting condition isn't "no vision" — it's "vision so flat it's invisible."

### The rewrite

Run the three vision inputs.

- **The user:** Plant operators with 10-30 years of experience working rotating shifts at refineries, chemical plants, and aerospace assembly lines. Specifically the shift lead — the person responsible for the floor, not the data scientist or the executive.
- **The transformation:** Today, they walk into shift not knowing what's about to break. They react. They burn weekends on emergency calls. They lose intuition to alert fatigue. After the vision: they walk in already knowing what's drifting, why, and when to schedule the fix. Confidence replaces anxiety. Their judgment is amplified, not replaced.
- **The timeframe:** 3-year strategic vision. Long enough to assume 3-4 model generation improvements; short enough to be a planning artifact.

Three drafts.

**Narrative version:**
> "It's the start of shift at a a Fortune 100 enterprise-equipped plant. The shift lead walks the floor with the system that already knows what's about to fail. The compressor on Line 3 has been drifting for 11 days — vibration signature, oil temperature, current draw — and the system tells them *why* before it tells them *what*. They schedule the repair into a planned window. They go home on time. Their 25 years of judgment is sharper than ever, because the system speaks their language and respects their call."

**Headline version (rewritten vision):**
> **"Plant operators ship a shift with confidence, not anxiety — every machine that's about to fail tells them why."**

**Team version:**
- *Why this matters.* Industrial unplanned downtime is a $50B/year problem. Sensor data isn't the gap; interpretation is. Operators are drowning in red lights and starved of narrative. a Fortune 100 enterprise's installed base is the largest in the industry — we're the only company that can close this gap end-to-end.
- *Who it serves.* Shift leads at refineries, chemical plants, aerospace assembly. Not data scientists. Not executive dashboards. The person walking the floor.
- *What winning looks like.* (1) An operator says "I trust this more than my gut, and my gut is good." (2) Plants on industrial predictive maintenance see unplanned downtime drop 50% within 18 months. (3) When an industry person says "operator-respecting AI," our name comes up first.

### Re-running the 5-test frame

| Test | Pass / Fail | Reason |
|---|---|---|
| Aspirational | Pass | "Confidence, not anxiety" is a future state. Today's reality is anxiety. The destination is meaningfully different. |
| Specific | Pass | Plant operators. Shift-level. The user is concrete enough to picture. |
| Durable | Pass | Doesn't name a model, capability, or year. Survives Claude 6, GPT-7. Survives a 10x improvement (the system gets sharper) and a 10x cost increase (downtime costs more than inference). |
| Differentiating | Pass | a Fortune 100 enterprise-shaped. The phrase "respects operator judgment" doesn't fit GE's executive-dashboard pitch or Siemens's industrial-IoT pitch. Identifies the company. |
| Motivating | Pass | Engineers want to build a system that respects 25 years of judgment. Operators want a product that doesn't try to replace them. There's an emotional center. |

Score: 5/5. Same domain. Same product category. Different vision shape — anchored on the human transformation, not the capability.

### The cuts test

What this vision makes obviously prioritized:
- Explainability investment — the system has to tell operators *why*, not just *what*. This stops being a nice-to-have and becomes a vision-critical feature.
- Operator UX work — the language has to match the floor, not the data scientist. Tablet-first, jargon-free, fast.
- Failure narrative generation — the human-readable story behind a flagged anomaly is the product.

What this vision makes obviously out-of-scope:
- Executive dashboards as a primary surface. They're not the user.
- Generic anomaly-detection products that ship without explanation. They contradict the vision.
- Black-box recommendation engines. Ditto.

That's at least 30% of the prior roadmap, killed cleanly.

---

## CROSS-LINKS

- **`purpose-dialogue`** — Vision is downstream of purpose. Don't set vision until purpose is named. Purpose answers "why does this organization care about AI in the first place?" Vision answers "what does the world look like when this specific product wins?" Confusing the two produces vision statements that are really purpose statements (too high-altitude to drive product decisions) or purpose statements that are really vision statements (too product-specific to align the org). Run purpose-dialogue first if cultural commitment is shaky. Run vision-setting once the team agrees on why this work matters.

- **`strategy-canvas`** — Vision sits at the top of the strategy canvas. Without it, every other element drifts. The capability-conditional bets need a destination to point at; the moat needs a transformation to defend; the reset triggers need a vision to test against. Once vision is locked, run strategy-canvas to translate it into 6-month bets with measurable triggers.

- **`signal-scanner`** — Environmental scanning informs how durable the vision is. If signal-scanner detects a major model capability shift, regulatory move, or cost structure change in the next 6-12 months, vision must account for that. A vision written without environmental scanning is a guess. A vision written after scanning is a calibrated bet.

- **`first-principles`** — Use first-principles to test whether the vision rests on assumptions that survive scrutiny. The 5-test frame catches surface failures; first-principles catches deeper ones. Run when the vision passes the 5-test but the team still can't agree.

- **`stakeholder-communications`** — Vision is the highest-altitude stakeholder communication. Calibrate per audience: **board** hears the why (the structural problem and the bet), **engineering** hears the durable invariant (the part that doesn't change across model generations), **customer** hears the experience (the transformation in their own work). Same vision, three calibrations. Bridger work — making each audience feel the vision in their own language without diluting the core.

---

## DELIVERABLE FORMAT

```
## Vision: [Product Name]

**HORIZON:** [1-year tactical | 3-year strategic | 10-year aspirational]

**INPUTS LOCKED:**
- The user: [specific segment, not "everyone"]
- The transformation: [before / after]
- The timeframe: [horizon + reasoning]

**THREE DRAFTS:**

**Narrative (3-5 sentences):**
[The story of the user's transformed work or life]

**Headline (≤15 words):**
[The billboard]

**Team version:**
- Why this matters: [structural problem + why now]
- Who it serves: [specific user]
- What winning looks like: [three concrete signals]

**5-TEST SCORECARD:**
| Test | Pass/Fail | Note |
|---|---|---|
| Aspirational | | |
| Specific | | |
| Durable | | |
| Differentiating | | |
| Motivating | | |

**CUTS TEST:**
- Obviously prioritized: [3 roadmap items this accelerates]
- Obviously out-of-scope: [3 roadmap items this kills]
- 30% rule: [does this vision invalidate at least 30% of current roadmap? Yes/No]

**STRATEGY COHERENCE AUDIT:**
- Bets serving vision (% of next-quarter): [%]
- Cover-fire bets (justified non-vision): [count + tag]
- Contradicting bets: [list — kill the bet or update the vision]
- Coherence verdict: [coherent | drifting | disconnected]

**FAILURE MODE CHECK:**
- [ ] Not capability-anchored (no model names, no specific techniques)
- [ ] Not a feature list (single transformation, not a catalog)
- [ ] Not industry jargon (passes grandmother test)
- [ ] Not competitor-mirrored (states the wedge in own terms)

**MONDAY MORNING:**
[One sentence: what changes in this week's roadmap as a result of this vision]
```

---

## RED TEAM — WHEN THIS SKILL IS WRONG

This skill gives bad advice when:

- **Pre-PMF startups still hunting the problem.** The team should be testing problem hypotheses, not painting visions. Vision before problem-validation is decoration that locks in the wrong destination. Use first-principles and run problem tests first; come back to vision-setting after the third successful customer.

- **Mature consumer products in commodity categories.** When product fundamentals (checkout speed, error rate, onboarding completion) are the bottleneck, a new vision is decoration. The team needs execution support, not aspiration. Fix the funnel first.

- **Teams in survival mode.** Companies under 6 months of runway, post-layoff, or in crisis mode shouldn't run vision exercises. Vision becomes a distraction from execution. Stabilize, then return to vision when capacity for long-term thinking is restored.

- **Vision-setter and execution lead don't speak.** When the person writing the vision and the person running the roadmap aren't in regular conversation, vision becomes corporate fiction. The artifact ships, the roadmap continues unchanged, the vision dies. Fix the org chart problem first; vision follows.

- **The poster-on-the-wall syndrome.** When the team has been told "we have a vision" so many times that the word itself triggers eye-rolls, a new vision exercise can backfire. The fix isn't another exercise — it's earning the right to set vision again. Ship a hard product call that aligns with the new direction *before* announcing the new vision. Behavior precedes language.

- **Pure infrastructure / platform plays where the user is another developer.** The 5-test frame still applies, but the "transformation" is technical, not emotional. The skill works, but the worked examples here (operators, lawyers, knowledge workers) need to be substituted with developer-shaped ones (the developer ships in 30 minutes what used to take 3 days).

---

## QUALITY GATE

- [ ] Three drafts written (narrative, headline, team)
- [ ] 5-test scorecard run on each — all five pass on the chosen draft
- [ ] Four AI failure modes checked (no capability anchor, no feature list, no jargon, no competitor mirror)
- [ ] 10x-better and 10x-cost durability tests passed
- [ ] Cuts test names at least 3 obvious priorities and 3 obvious out-of-scope items
- [ ] 30% rule satisfied (vision invalidates at least 30% of current roadmap)
- [ ] Strategy coherence audit completed — verdict named
- [ ] Three audience calibrations drafted (board / engineering / customer)
- [ ] Monday morning action specified

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. **The recommendation** — which of the three drafts is the working vision and why
2. **The hypothesis** — "We believe this vision will hold for [horizon] because it's anchored on [durable transformation], not [volatile capability]. We'd know we're wrong if [signal] within [timeframe]."
3. **The key trade-off** — what this vision is choosing and what it's giving up
4. **The biggest risk** — and the specific mitigation
5. **The next action** — Monday morning roadmap change

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (strategy-canvas, moat-finder, signal-scanner), also generate the markdown handoff file per Section 9.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The diagram should show:
- The 5-test frame as a pentagon, with each draft scored against all five tests
- The four AI failure modes as four corners of a quadrant, with the chosen vision plotted in the durable center
- The strategy coherence audit as a horizontal flow: vision → roadmap items → coherent / drifting / disconnected verdict
- The Monday-morning action highlighted as the output

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

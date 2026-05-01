---
name: rtp-uncertainty-research
description: >
  Research for non-deterministic AI where output varies per query. Use when
  planning trust studies, threshold studies, or validating AI features. Runs
  longitudinal designs, stratified sampling, Wizard-of-Oz calibration.
  Prevents applying fixed-artifact methods to probabilistic products.
imports: [falsification, first-principles]
---

# Uncertainty Research

## DEPTH DECISION

**Go deep if:** Planning trust studies, validating a new AI feature, or measuring whether users' expectations match AI capability.

**Skim to Step 4 if:** You have a fast-moving experiment and just need directional signal — not rigorous research.

**Skip if:** Deterministic software, batch/offline AI, or fewer than 50 weekly active users (signals are too noisy to be meaningful).

## DELIVERABLE FORMAT

Before starting, ask: Word Document, Presentation, or Both?
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Before designing any research, answer at minimum:
1. What specific behavior are we measuring? (Not "trust" — "acceptance rate over 4 weeks")
2. Who is the user? What's their baseline tolerance for AI error?
3. What do we do differently if research says threshold is 70% vs 90%? (If the answer is "nothing," don't run the study)
4. When does this research finding expire? What model change or product change would make it stale?

---

## THE TRAP

You will apply traditional user research methods unmodified. The bias is **methodological anchoring** — using familiar techniques (A/B tests, usability studies, surveys) on AI products without accounting for non-determinism.

In traditional software: two users clicking the same button get the same result. In AI products: two users asking the same question may get different answers. This breaks most standard research assumptions in ways that aren't visible until you're defending your findings to a skeptical stakeholder.

**The three places this breaks:**
- **A/B tests:** Standard tests measure one metric against one output. AI products need multi-metric tests (quality + time-to-value + error rate) segmented by output quality quartile — because the same feature can have great average quality but terrible tail quality.
- **Usability sessions:** A one-session study captures week-1 trust (cautious, realistic). Real trust stabilizes at week 4. Ship based on week-1 data and you'll be surprised when users over-trust at month 3.
- **Surveys:** "Is this helpful?" averages across good and bad outputs. You need to know if users even *noticed* the output was bad — because most don't, and that's a different problem.

---

## Expectation Calibration Interviews (The Prerequisite)

Before running research, interview 10-15 active users. This is not optional — it determines which research method you need.

**Questions:**
1. "What do you think this AI can and can't do?"
2. "If it makes a mistake, what would you expect?"
3. "How confident are you in its answers?" (Have them rate 1-10)
4. "What would make you stop using it?"

**Interpret:**
- If users expect 95% accuracy and the AI delivers 75%: the expectation gap will destroy trust regardless of feature quality. Fix the UX framing before researching trust.
- If users understand it's probabilistic and might be wrong: realistic expectations, trust is more durable when errors occur.
- If users answer "I don't know what it does": your UX isn't clear. Fix before research.

**Post-launch:** Re-run calibration interviews at week 2 and week 8. Users' expectations shift as they gain experience. Track whether expectations become more realistic or more inflated. Inflated expectations are more dangerous — they precede sharp trust collapses.

---

## Research Methods for Probabilistic Products

| What You're Testing | Wrong Method | Right Method | Sample Size | Duration |
|-------------------|-------------|-------------|-----------|----------|
| Does the AI help users? | Single 1-hour usability session | Longitudinal diary study (7-14 days, user logs interactions) | 15-25 users | 2-4 weeks |
| Is output quality good? | Expert review of 5 examples | Stratified random sample of 150+ outputs, scored by domain experts and users separately | 50+ outputs per use case | 1 week |
| Do users trust it? | "Would you use this?" survey | Behavioral: measure acceptance rate, edit rate, rejection rate over time | 100+ active users | 4-8 weeks |
| Is it better than baseline? | A/B test on single engagement metric | Multi-metric A/B test: quality + time-to-value + error rate, segmented by output quality quartile | 500+ per arm | 2-4 weeks |
| Does it calibrate trust? | Post-session NPS | Track user confidence curves over 4 weeks: does confidence grow as accuracy becomes familiar? | 30+ users, 5+ interactions each | 4 weeks |

---

## THE PROCESS

**Step 1: Identify what varies.** Before designing research, map the sources of variation:
- Model output varies per query (non-determinism)
- Model output varies over time (drift, updates)
- User expectations vary based on mental model of AI
- "Quality" is subjective for generative tasks

**Step 2: Choose the right method for the uncertainty type:**

| What You're Testing | Wrong Method | Right Method |
|-------------------|-------------|-------------|
| Does the AI help users? | Single usability session | Longitudinal study (trust develops over time) |
| Is output quality good? | Expert review of 5 examples | Statistical sample with stratified query types |
| Does the user trust it? | Post-session survey | Behavioral observation (do they verify, edit, or accept?) |
| Is it better than baseline? | A/B test on single metric | Multi-metric A/B with per-query-type segmentation |

**Step 3: Design for variability:**
- Use larger sample sizes than traditional research (model variation adds noise)
- Stratify by query complexity, user expertise, and domain
- Measure trust behaviors, not just satisfaction ratings
- Record the actual AI output each participant saw (it will vary — this matters)

**Step 4: Interpret with non-determinism in mind:**
- Average satisfaction across varied outputs is misleading
- Segment results by output quality (good responses vs bad responses)
- Trust is a leading indicator; satisfaction is a lagging indicator
- "The AI was helpful" and "I would rely on this AI" are different questions — ask both

**Step 5: Advanced — Wizard-of-Oz methodology (demand validation, not quality validation):**
- Humans generate responses; users believe it's AI
- Utility: validates demand and informs UX design before the model is ready
- Critical limitation: humans produce near-perfect responses (no latency, high quality)
- Users calibrate expectations to human-quality baseline
- When real AI launches at 70-80% quality, the expectation gap destroys trust
- Mitigation: never use WoZ results to forecast user satisfaction for real AI
- Instead: use WoZ for feature discovery, then plan quality calibration messaging
- If you must estimate real-AI satisfaction: discount WoZ results by 30-40% (empirical from multiple products)

---

## "Good Enough" Threshold Research

The most important research question for AI products: **"What quality level do users actually accept?"** Not perfect — acceptable.

**Why this matters:**
- Teams often assume 90%+ quality is required. Reality: users may accept 60-70% if the alternative is no assistance.
- Under-investing in this research leads to over-engineering (spending months on quality improvements that don't change user behavior).
- Over-investing leads to launching too early (shipping a 40% quality feature that users reject).

### Threshold Study Protocol

**Step 1 — Prepare stratified outputs**
Generate AI outputs at 4-5 quality levels: approximately 50%, 65%, 75%, 85%, and 95% accuracy. Do not label them by quality score — show users outputs in realistic context, as they would appear in the product.

**Step 2 — Recruit the right users**
Minimum N=30. Segment by user type from the start:
- **Expert users** (domain knowledge > 5 years): tend to accept lower quality because they catch errors
- **Novice users** (limited domain knowledge): need higher quality because they trust the AI without verification
If your product serves both, run separate analyses — a single combined threshold number will mislead you.

**Step 3 — Measure behavior, not opinion**
For each quality level, measure:
- **Acceptance rate:** % of outputs they use without editing
- **Edit rate:** % they edit before using
- **Rejection rate:** % they discard entirely
- **Confidence:** Do they share the output externally, or keep it internal? External use = real trust.

Do NOT ask "How helpful was this on a scale of 1-5?" That question captures opinion. Acceptance rate captures behavior. Behavior is what you need.

**Step 4 — Find the behavioral knee**
Plot acceptance rate vs. quality level. The "good enough threshold" is where acceptance rate stops increasing meaningfully as quality improves. Above this threshold, additional quality investment has diminishing returns on user behavior.

**Step 5 — Set validity conditions**
Document: "This threshold is valid for [user segment] under [use case] with [alternatives available]. Re-run if: user segment changes, the alternative changes, or the stakes of error change."

### Why Thresholds Differ So Much Across Domains

Teams are often surprised by how far thresholds vary. The spread is driven by three factors — not by arbitrary user preference:

| Factor | Low threshold (e.g., 50-60%) | High threshold (e.g., 90-95%) |
|---|---|---|
| **Alternative** | Blank page, nothing | Existing trained expert, established process |
| **Error cost** | Embarrassing, fixable | Dangerous, irreversible, regulated |
| **User expertise** | Expert who catches errors | Novice who trusts the output |

**Real examples across domains:**

- **Coding assistant (threshold: ~60%):** The alternative is a blank page. Developers review and debug the code before shipping. A hallucinated function name is annoying, not dangerous — they catch it. Users accept lower quality because they own the final check.

- **Healthcare decision support (threshold: ~90-95%):** The alternative is an experienced clinician's judgment. Errors have patient safety implications. In regulated contexts, even a 5% error rate can mean liability. Users demand near-certainty before trusting the recommendation.

- **Creative writing tool (threshold: ~40-50%):** The alternative is also a blank page, but the output will always be heavily edited. Users never ship AI output as-is — they use it for ideation only. Quality at this stage means "good enough to spark an idea," not "good enough to publish."

- **Customer support draft generation (threshold: ~70%):** The alternative is manual drafting. Agents review every draft before sending. A wrong sentence gets caught before it reaches the customer. The time savings (even on imperfect drafts) justify the threshold.

**The pattern:** The threshold is set by the cost of being wrong × how often users catch the error × what the alternative looks like. Research this — don't assume it.

---

## Research Decay

AI research findings expire. Model improvements can invalidate research within months. Build expiry conditions into every finding from the start.

**Why decay happens:**
- You measure "users trust an AI with 75% accuracy"
- Three months later, the model improves to 82% accuracy
- The original finding is now stale — users may trust 82% more than expected
- You re-run the study and get different results
- But you've already built the product against the old finding

**The 5% guideline — and why it's a starting point, not a rule:**

The common heuristic is "re-validate if accuracy changes >5%." This is a reasonable starting point for mid-stakes products (customer support, productivity tools). But the right threshold is domain-dependent:

| Domain stakes | Re-validate when accuracy changes by... | Why |
|---|---|---|
| Low stakes (creative, ideation) | >10-15% | Users tolerate quality variance; threshold shift is small |
| Mid stakes (productivity, support) | >5% | The balance between speed and accuracy is sensitive |
| High stakes (healthcare, finance, legal) | >2-3% | Near-threshold products; small accuracy changes cross into trust collapse |

**The better practice:** For every research finding, define the *condition*, not just a number.

**Examples:**
- "This trust study is valid while model accuracy is 75-85%. Re-validate if accuracy changes >5% because we're mid-stakes and users are near the acceptance threshold."
- "This usage study is valid with context window <8K tokens. Re-validate if context window expands significantly, because retrieval behavior changes."
- "This user preference study is valid with response latency <500ms. Re-validate if latency changes >100ms — users have shown latency sensitivity in this product."

**Action:** Create a research findings database with expiry *conditions* (not just expiry dates). Schedule re-validation studies quarterly or when major model updates land. The trigger for re-validation should be a change in the product — not just the passage of time.

---

## Measuring Trust Over Time (Longitudinal Design)

Trust doesn't stabilize in one session. It develops (or collapses) over weeks.

**Timeline of trust calibration:**
- **Week 1:** Users are cautious. They verify everything. Low trust, but realistic expectations.
- **Week 2-3:** Users start trusting. They reduce verification. Trust rising.
- **Week 4:** Trust begins to stabilize at a realistic level (novelty effect wearing off).
- **Week 5-8:** Trust stabilizes or collapses. If the AI has made errors, trust may plummet sharply.

**The short-study trap:** A 1-2 session usability study captures week-1 trust (cautious, realistic). You think you have the real trust number. Three months after launch, real users over-trust or sharply distrust. You shipped based on misleading data.

**Longitudinal design requirements:**
- Minimum **4 weeks** duration
- **5+ interactions per user per week** (to build realistic history of errors and successes)
- Measure actual behavior (acceptance rate, edit rate, rejection rate) — not just surveys
- Track when users stop verifying outputs (sign of over-trust worth flagging)
- Track when users start rejecting outputs (sign of under-trust or broken trust)

**Sample size:** 30+ users minimum. More if segmenting by user type (expert vs. novice, power user vs. casual).

**What to measure:**

| Metric | What it tells you |
|---|---|
| Acceptance rate | % of outputs user ships without editing — pure behavioral trust signal |
| Edit rate | % of outputs user edits before using — they trust the direction, not the execution |
| Rejection rate | % of outputs user discards — either wrong or they've lost trust |
| Verification time | How long before users stop checking the AI's work? Declining = growing trust |
| Return usage | Do users come back? Churn in week 3-4 = trust collapse, not novelty fatigue |

**Never ship a feature based on short-form research (1-2 sessions).** Treat short studies as directional signal only. Plan longitudinal studies before launch as a quality gate.

---

## SWITCH INTERVIEW — THE MOMENT-OF-CHANGE METHOD (Bob Moesta)

The methods above (longitudinal diary, threshold studies, expectation calibration) measure *current* user behavior. The Switch Interview measures the *moment a user changed* — the inflection point when they switched from one product to another, or from one behavior to another.

The methodology comes from Bob Moesta's Jobs-to-be-Done research. It anchors the entire interview on a specific event: the moment of change. Around that anchor, you reconstruct the timeline that led to it.

For AI products, the Switch Interview probes one specific question that no other method captures: **the moment users started TRUSTING the AI** (or the moment they stopped trusting it). That moment is more revealing than any usability test, threshold study, or NPS survey.

### When to Run a Switch Interview

Use this method when:
- A user just adopted your AI feature after using a competitor or manual workflow → understand what triggered the switch
- A user just churned from your AI product → understand what broke their trust
- A power user tells you "I now trust this for X use case" → understand what made the trust click
- You're entering a new market and need to understand what makes those users adopt or reject AI tools
- You're seeing high acquisition but low retention → the data tells you they leave; the Switch Interview tells you why

### The Six Timeline Questions

The interview has six questions. They're asked in this order, anchored on the moment of change. The discipline: don't deviate from the timeline. The answers in order matter — the user's narrative builds chronologically and probing out of order destroys the recall.

#### Question 1: When did you first think about this?

**The probe:** Take me back to the very first time you remember thinking "I need a better way to do [task]." Or "the current way isn't working." Or "I wonder if there's an AI for this."

**What you're listening for:**
- The first signal in their environment — a frustration, a peer's recommendation, a moment of failure with the old system
- The time horizon — was this last week, last quarter, or two years ago? Long incubation time signals high stakes; short signals impulse adoption
- The emotional charge — frustrated, curious, desperate, opportunistic. Different starting emotions predict different trust trajectories.

**Why this matters for AI:** Users who started thinking about AI from a place of desperation (current system completely broken) have higher trust thresholds for the new tool — they need it to *demonstrably* work or they fall back to their old broken system. Users who started from curiosity have lower trust thresholds and are more forgiving of early errors.

#### Question 2: What triggered it?

**The probe:** What specifically pushed you from "thinking about it" to "actively looking for a solution"? Was it a moment, a person, an event?

**What you're listening for:**
- The triggering event — usually a specific incident, not a gradual realization
- Whether the trigger was external (someone showed them a demo) or internal (they hit a wall with the existing approach)
- The urgency — did they start looking that day, or did the trigger marinate for weeks?

**Why this matters for AI:** AI adoption usually triggers from one of three patterns: someone they trust used it and shared an output ("look what this AI did"), they hit an unsolvable wall in their existing process, or they were given mandate from above. Each pattern produces different post-adoption behavior. Mandate-driven adopters are the highest-risk for trust collapse — they didn't choose; they comply.

#### Question 3: What did you try?

**The probe:** Walk me through what you considered. What other options did you look at? What did you almost pick instead of [your product]?

**What you're listening for:**
- The full consideration set — usually 3-5 options, not just yours
- Which alternatives they took seriously vs. which they dismissed quickly and why
- The deal-breakers that eliminated alternatives (price, trust, reputation, safety concerns, integration gaps)

**Why this matters for AI:** The competitive set in the user's mind is usually different from what your competitive analysis suggests. They might have compared you to a manual process, a non-AI tool, and a different category entirely — not to the AI competitors you think you're losing to. This question reveals the real competitive frame.

#### Question 4: What made you decide?

**The probe:** What was the moment you decided "I'm going with [your product]"? What tipped it for you?

**What you're listening for:**
- The decision moment — usually a specific signal, demo, conversation, or trial output
- The decision criteria — explicit (cost, features) and implicit (gut feel, social proof, recovery story)
- Whether the decision was rational, emotional, or social

**Why this matters for AI:** AI adoption decisions are rarely purely rational. They're trust calibration events. The user picked your product because something specific gave them confidence the AI would work. That "something" — often a demo output, a customer reference, a safety statement, or a moment of unexpected accuracy — is the marketing message that actually converts. Most teams don't know what their actual conversion driver is until they run Switch Interviews.

#### Question 5: What almost stopped you?

**The probe:** Was there a moment where you almost didn't do this? What was the hesitation? Who or what almost talked you out of it?

**What you're listening for:**
- The objections that didn't fully kill the deal but slowed it
- Internal blockers (skeptical colleagues, procurement, safety review) and external (price, capability gaps, integration concerns)
- The reassurances that resolved the hesitation

**Why this matters for AI:** Every AI buyer has a moment of "is this hype or real?" hesitation. The Switch Interview surfaces what almost killed the deal. The patterns across 10-15 interviews tell you the systematic objections your sales motion needs to dismantle, not the one-offs.

#### Question 6: How did the new thing feel after the switch?

**The probe:** Take me through your first few interactions with [your product]. When did it click? When did you trust it? Was there a moment when you stopped feeling cautious?

**What you're listening for:**
- The first "wow" moment — the specific interaction where trust clicked
- The setbacks — moments of "wait, did the AI just hallucinate?" and how the user recovered (or didn't)
- The trust trajectory — did trust grow steadily, plateau, or spike-and-recover?

**Why this matters for AI:** This question is the entire reason to run Switch Interviews on AI products. Other research methods can tell you trust *levels*. Only the Switch Interview tells you trust *moments* — the specific interactions that built or broke trust.

The 0.1% angle: **for AI features, the trust moment is more revealing than any usability metric.** A user who tells you "I started trusting it on day 3 when it caught a contract risk our last review missed" has just told you exactly what marketing asset, demo, or onboarding moment converts skeptical buyers into believers. A user who tells you "I stopped trusting it on day 8 when it confidently cited a regulation that didn't exist" has told you exactly which failure mode causes irrecoverable trust damage.

### Switch Interview Logistics

- **Sample size:** 10-15 users per switch direction (to-you, to-competitor, to-manual). Patterns emerge around interview 8-10. Beyond 15, you're confirming patterns, not finding new ones.
- **Recruitment:** Recently-switched users (within 30-60 days). The memory is fresh enough to recall specifics; far enough that initial novelty has settled.
- **Duration:** 45-60 minutes. Less than 45 and you can't get through six questions with depth. More than 60 and the user starts to confabulate.
- **Format:** 1-on-1, video call, recorded with permission. The interviewer doesn't lead — they ask the question and let silence force the user to fill it. Long pauses are productive; rushing them produces shallow answers.
- **The interviewer's job:** Listen. Probe specifically when the user says something abstract ("it just felt right" → "what specifically felt right? what were you doing in that moment?"). Resist the urge to validate the product or argue with negative feedback.

### Synthesizing Switch Interviews

After 10-15 interviews, you have ~10 hours of recordings. The synthesis pattern is the same open coding → axial coding → selective coding methodology used in eval frameworks:

1. **Open code** every transcript. Tag specific moments, quotes, decisions, frustrations, trust events.
2. **Axial code** the labels. Cluster into themes — common triggers, common decision criteria, common trust moments, common failure modes.
3. **Selective code** the themes. Pick the 3-5 highest-leverage findings — the ones that should change product, marketing, or onboarding decisions.

The output is not a deck. It's a memo with three sections:
- **The triggers** — what made users start looking for an AI tool
- **The decision criteria** — what made them choose us (or our competitor)
- **The trust events** — the specific moments that built or broke trust after the switch

Each section has 3-5 patterns backed by 3+ user quotes each. Patterns with fewer than 3 corroborating quotes are noted but not acted on yet.

### When NOT to Use Switch Interviews

- When users haven't switched recently — the method requires a real moment of change
- When the AI feature is too new — there's no switching pattern yet
- When you need quantitative data — Switch Interviews are qualitative; pair with threshold studies for the numbers
- When you can't conduct 1-on-1 interviews (regulated industries, anonymous users) — adapt to async written formats but expect lower depth

---

## OUTPUT FORMAT

Use this template when planning uncertainty research:

```
## Uncertainty Research Plan: [Feature Name]

**Research question:** [Specific, testable — not "does the AI work?" but
  "what accuracy threshold do healthcare providers require to accept
  AI-generated diagnosis summaries without verification?"]

**Method:** [From the methods table]
  Example: Behavioral acceptance study with stratified outputs

**Sample:**
  - Total size: [N= — minimum 30 for threshold studies, 100+ for trust studies]
  - Segments: [User types and why they're different]
  - Recruitment source: [Where do these users come from?]

**Duration:** [Weeks — minimum 4 for trust studies]
  Example: 4 weeks, 3 interactions per provider per week

**Metrics (behavioral, not survey):**
  - Primary: [Acceptance rate / Edit rate / Rejection rate]
  - Secondary: [Verification time, return usage]

**Validity conditions:**
  This finding is valid while: [model accuracy stays within X%, latency stays below Y ms,
  user segment stays the same, alternative option stays the same]
  Re-validate if: [specific trigger conditions]
```

---

## REALITY CHECK

- Longitudinal AI research is expensive. Budget for it explicitly or accept that you'll have incomplete trust data at launch.
- Wizard-of-Oz testing establishes upper-bound expectations that real AI may not meet. Always discount WoZ findings by 30-40% when estimating real-AI satisfaction.
- AI research findings decay — model improvements can invalidate research within months. Every finding needs an expiry condition, not just a date.
- The right quality threshold for your product comes from users, not from your eval benchmarks. Benchmarks measure capability. Users define acceptability.

## QUALITY GATE

- [ ] Sources of variation mapped before study design
- [ ] Research method matched to uncertainty type (from the methods table)
- [ ] Sample size accounts for model output variation — minimum 30 for threshold studies
- [ ] Segmented by user expertise (expert vs. novice) before analyzing threshold
- [ ] Actual AI outputs recorded for each participant (outputs will vary — this matters)
- [ ] Results segmented by output quality, not just averaged
- [ ] "Good enough" threshold identified from behavioral data (acceptance rate), not opinion surveys
- [ ] Validity conditions set for all major findings (condition + trigger for re-validation)
- [ ] Longitudinal study planned (minimum 4 weeks) before launch decision
- [ ] Wizard-of-Oz results discounted 30-40% if used to estimate real-AI satisfaction

## WHEN WRONG

- Testing deterministic features within the AI product (use standard research methods)
- When you need directional signal fast and methodological rigor can follow later (short study is OK — just flag it as directional)
- When the AI component is so early that the model itself will change before research concludes
- When you have fewer than 50 weekly active users — signals are too noisy for any quantitative study

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. **The recommendation** — specific research plan with method, sample, duration
2. **The hypothesis** — "We believe users will accept X quality level because Y. We'd know we're wrong if acceptance rate at that level is below Z."
3. **The key trade-off** — rigor vs. speed; longitudinal vs. directional
4. **The biggest risk** — and the mitigation (usually: findings expire before the team acts on them)
5. **The next action** — [step] by [role] by [date]

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill feeds into feature decisions (problem-ai-fit → uncertainty-research → ai-use-case-readiness), generate the markdown handoff file per Section 9.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The diagram should show:
- The methods matrix (what you're testing × right method) as a visual table
- The quality threshold curve (acceptance rate plotted against output quality, showing the "good enough" knee)
- The trust timeline (week 1-8 trust calibration arc)

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

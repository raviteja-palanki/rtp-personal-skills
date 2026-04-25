---
name: rtp-feedback-triage
description: >
  Score user feedback by frequency × severity × strategic fit + an AI-failure
  axis. Use when triaging support tickets, NPS comments, in-product feedback,
  or social-channel complaints. Most triage frameworks treat AI feedback like
  any other UX issue. They shouldn't — AI failures are bimodal and route to
  different fix teams. This skill separates them and ranks accordingly.
imports:
  - failure-modes
  - ai-product-metrics
  - eval-framework
---

# Feedback Triage

Take an unstructured pile of user feedback and produce a ranked, routed report — with the AI-failure axis that frequency-only triage misses.

> Most feedback triage is frequency-based: "we get this complaint most." That works fine for non-AI features. For AI features, frequency hides the structural problem — bimodal feedback gets averaged into "mostly positive" while a small slice of users are watching the AI hallucinate at them.

---

## DEPTH DECISION

**Go deep if:** Triaging 50+ pieces of feedback, the team has both AI and non-AI features in the same product, or routing decisions will set the next sprint's priorities. Run the full 4-axis score when output drives the roadmap.

**Skim to AI-failure breakdown if:** You already have a triage report and just need to separate AI failures from UX issues.

**Skip if:** Frequency-only triage is fine — non-AI features with simple bugs (login broken, button doesn't render). See RED TEAM.

---

## DELIVERABLE FORMAT

Before starting, ask:

> **Format?**
> 1. **Ranked themes report** — Themes table with scores, routing recommendations, AI-failure breakdown. Best for sprint planning.
> 2. **Live triage doc** — A working document that updates weekly as new feedback arrives. Best for ongoing operations.
> 3. **Inline summary** — Top 5 themes, top 3 AI failures, top 3 routes. Best for fast iteration.
>
> *Default: Ranked themes report.*

---

## THE STRUCTURAL INSIGHT

Standard PM feedback triage uses a 3-axis score: frequency × severity × strategic fit. It's clean, it works for traditional features, and it's been the default for a decade.

For AI features, this 3-axis score misroutes the work.

**The 0.1% angle: AI-feature feedback is bimodal.**

Users either love the AI ("magic, saves me hours") or they hate it ("hallucinated, gave me wrong answer in front of my client"). The middle is small. When you average across the bimodal distribution, you get "mostly positive with some complaints" — which masks the structural problem. The complaints aren't UX issues. They're signals that the AI is failing in a way that requires a different fix team.

A user complaint about button placement routes to design. A user complaint about confused interaction routes to UX research. A user complaint about hallucinated output routes to the AI eval team — and possibly to model retraining, prompt engineering, or grounding pipeline updates. Same UI surface, three completely different fix paths.

**Triage that doesn't separate "AI failure" from "generic UX issue" misroutes the fix to the wrong team.** The design team can't fix hallucinations. The eval team can't fix button placement. The roadmap waits while the wrong team owns the problem.

The AI-failure axis is the structural addition. Add it as a fourth axis (yes/no flag) and the routing becomes obvious. Skip it and you'll spend a quarter wondering why the design team's UX research isn't moving the AI complaint count.

---

## THE 4-AXIS SCORE

Each piece of feedback (or each theme after clustering) gets four scores. Total = 11-point scale.

### Axis 1 — Frequency (0-5)

How often does this theme appear in the feedback corpus?

| Score | Frequency |
|---|---|
| 5 | Mentioned by >20% of all feedback in the period |
| 4 | 10-20% |
| 3 | 5-10% |
| 2 | 2-5% |
| 1 | <2% but recurring (3+ instances) |
| 0 | One-off (single instance, no signal) |

For volume <50 pieces of feedback, use absolute counts: 5 = 10+ mentions, 4 = 5-9, 3 = 3-4, 2 = 2, 1 = 1.

### Axis 2 — Severity (0-3)

What happens to the user when this issue occurs?

| Score | Severity | Examples |
|---|---|---|
| 3 | Blocking — user cannot complete their core task | Login fails, AI refuses entire workflow, data corruption |
| 2 | Major friction — user completes task but with significant pain | AI gives wrong answer that user has to manually correct, error message doesn't explain how to recover |
| 1 | Minor annoyance — user notices but adapts | UI confusion that they figure out, AI suggestion that doesn't apply |
| 0 | Cosmetic — user mentions but it doesn't affect outcome | Color preference, copy nit |

### Axis 3 — Strategic Fit (0-2)

Does fixing this serve the current product strategy?

| Score | Fit |
|---|---|
| 2 | Directly serves a current OKR, roadmap commitment, or strategic bet |
| 1 | Adjacent — improves a feature in the strategic area but isn't the focus |
| 0 | Misaligned — about a feature being deprioritized, sunset, or out of scope |

### Axis 4 — AI-Failure Flag (0-1)

Is this an AI failure, or a generic UX/product issue?

| Score | Flag |
|---|---|
| 1 | AI failure (see breakdown below) |
| 0 | Not AI-failure — UX, perf, scope, content, etc. |

The AI-failure flag is a yes/no, but it carries disproportionate weight in routing. A "1" routes to a different team and gets a different fix protocol. A "0" routes through standard product/design/eng tracks.

### Total score (0-11)

Sum the four axes. Sort descending. Use the score to set sprint priority. The AI-failure flag isn't just a tiebreaker — it changes the routing path entirely.

**Threshold guidance:**
- 8-11: Critical — must address this sprint
- 5-7: High — next sprint or experiment first
- 3-4: Medium — backlog, watch for trend
- 0-2: Low — monitor or close

---

## CLASSIFICATION RULES

Before scoring, classify every piece of feedback into one of six categories. The classification determines which scoring axes apply and which fix team owns the issue.

### 1. UX Issue (non-AI)

The feature works as designed but the design is confusing, awkward, or misaligned with user mental models.

**Signals:** "I couldn't find...", "the button was hidden", "I expected X but got Y", "the flow was confusing"
**Routes to:** Design + UX research
**AI-failure flag:** 0

### 2. Performance Issue

The feature is slow, unreliable, or fails to load.

**Signals:** "it took 30 seconds", "it timed out", "the page froze", "every third click fails"
**Routes to:** Engineering (infra/perf team)
**AI-failure flag:** 0 (unless the latency is an AI inference latency — see breakdown)

### 3. AI Failure (the bimodal axis)

The AI itself produced a wrong, confidently-wrong, refused, or otherwise failed output. See the breakdown below for sub-types.

**Signals:** "the AI said X but X is wrong", "it made up a fact", "it refused for no reason", "it confidently told me the wrong number", "the recommendation was nonsense"
**Routes to:** AI eval team + ML/AI engineering
**AI-failure flag:** 1

### 4. Edge Case

The feature works for the common path but fails for a specific user context, locale, or unusual input.

**Signals:** "it works for English but not French", "fails for usernames with special characters", "doesn't handle negative numbers"
**Routes to:** Engineering (likely a fast fix once scoped)
**AI-failure flag:** 0 (unless the edge case is the AI failing on a specific input class — then it's a 1)

### 5. Out-of-Scope Request

The user is asking for a feature or behavior that isn't part of the product, isn't on the roadmap, and isn't strategic.

**Signals:** "could you add X?", "I wish it did Y", "would be nice if..."
**Routes to:** Product (acknowledge, decline or defer)
**AI-failure flag:** 0

### 6. Future Capability Signal

The user is describing a problem the product doesn't solve yet, but might in the future. This is the most strategically valuable category — and the easiest to miss.

**Signals:** Repeated mentions across users of an unmet need, often phrased as "I work around it by..." or "I use a different tool for that"
**Routes to:** Discovery / strategy
**AI-failure flag:** 0

The classification is the first cut. Apply scores within each category. Don't try to compare an AI failure score to a UX issue score directly — they're different axes of fix.

---

## THE AI-FAILURE BREAKDOWN

When a piece of feedback is flagged as AI failure (axis 4 = 1), classify the failure type. Each type routes to a different sub-team and triggers a different fix protocol.

### 1. Hallucination

The AI generated content that was factually wrong (fabricated a fact, misattributed a quote, invented a citation).

**Routes to:** AI eval team (failure-modes mapping) + grounding pipeline owner (if RAG)
**Fix protocols:**
- Add the failure to the eval set (regression prevention)
- Audit retrieval pipeline if RAG-based
- Tighten prompt grounding constraints
- Lower confidence thresholds for high-stakes outputs

### 2. Over-Confidence

The AI produced a wrong output but expressed certainty (no hedging, no "I'm not sure").

**Routes to:** AI eval team + UX (confidence-display owner)
**Fix protocols:**
- Calibrate confidence scoring
- Update UX to surface uncertainty when confidence is below threshold
- Add explicit "I'm not certain" outputs for borderline cases

### 3. Under-Confidence

The AI hedged or refused when it shouldn't have ("I cannot determine..."). Users got frustrated by unnecessary caution.

**Routes to:** AI eval team + prompt engineering
**Fix protocols:**
- Audit refusal triggers (often over-tuned safety)
- Adjust prompt to allow confident answers in well-supported cases
- Test against eval set for refusal rate by query type

### 4. Wrong Refusal

The AI declined a legitimate request, often for compliance reasons that don't apply to the actual query.

**Routes to:** Safety team + prompt engineering
**Fix protocols:**
- Audit refusal taxonomy
- Distinguish "must refuse" from "should answer carefully"
- Add eval cases for legitimate-but-borderline queries

### 5. Wrong Tool / Wrong Routing

In multi-agent or tool-using systems, the AI picked the wrong tool, agent, or knowledge source for the query.

**Routes to:** Agent design / orchestration team
**Fix protocols:**
- Update routing logic
- Add eval cases for ambiguous queries
- Improve tool descriptions and selection prompts

### 6. Latency Failure

The AI took so long to respond that the user gave up. Distinct from a generic perf issue because the cause is in the AI inference path (model size, retrieval slowness, multi-step reasoning chain).

**Routes to:** AI infrastructure + model selection
**Fix protocols:**
- Profile inference latency
- Consider smaller model or distillation
- Add streaming or progressive disclosure UX

The breakdown matters because each sub-type has a different fix team and a different cycle time. Hallucinations might take 4 weeks (retraining or pipeline updates). Over-confidence might take 1 week (UX tweak). Lumping them all as "AI complaints" delays everything.

---

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

Triaging 200 pieces of feedback on the predictive maintenance feature, collected over 6 weeks across in-app feedback, support tickets, and customer success notes.

### Step 1: Classify

| Category | Count | % of total |
|---|---|---|
| UX Issue | 64 | 32% |
| Performance | 18 | 9% |
| AI Failure | 71 | 36% |
| Edge Case | 22 | 11% |
| Out-of-Scope | 14 | 7% |
| Future Capability Signal | 11 | 6% |

The AI failure rate (36%) is the diagnostic. If it's >25% in a mature feature, the feature has structural issues that won't be solved by UX iteration.

### Step 2: Score the AI Failure bucket (the 71 items)

Apply the 4-axis scoring, with all entries having axis 4 = 1.

Top themes after clustering:

| Theme | Freq | Sev | Fit | AI-Fail | Total | Sub-type |
|---|---|---|---|---|---|---|
| System ranks alerts in confusing order vs operator judgment | 5 | 2 | 2 | 1 | 10 | Hallucination + Over-confidence (false ranking presented confidently) |
| System flagged failure 4 hours after operator noticed it on shop floor | 4 | 3 | 2 | 1 | 10 | Latency (or under-detection — needs investigation) |
| System said "high confidence: failure imminent" on an asset that was fine | 4 | 3 | 2 | 1 | 10 | Over-confidence |
| System refused to predict a Tier-2 asset (said "insufficient data") | 3 | 2 | 2 | 1 | 8 | Wrong Refusal |
| System recommended replacing a part that was just replaced 2 weeks ago | 3 | 2 | 2 | 1 | 8 | Hallucination (context-blind) |
| System took 12+ seconds to load asset detail page | 4 | 1 | 1 | 1 | 7 | Latency |

### Step 3: Route to fix teams

| Theme | Route to | Fix cycle |
|---|---|---|
| Confusing alert ranking | AI eval team + UX | Add to regression suite, tune confidence + ranking model |
| Late failure detection | AI eval + reliability eng | Audit detection latency, possibly retrain |
| Confident-wrong predictions | AI eval team | Calibration audit, lower confidence thresholds for Tier-1 |
| Wrong refusal | Prompt + safety | Audit refusal triggers for asset tiers |
| Context-blind recommendation | Grounding pipeline + AI eval | Add maintenance history to retrieval context |
| Latency on detail page | AI infrastructure | Profile and optimize, consider caching |

### Step 4: Score the UX bucket separately (the 64 items)

Top themes:

| Theme | Freq | Sev | Fit | AI-Fail | Total | Route |
|---|---|---|---|---|---|---|
| Operators can't filter alerts by plant | 5 | 2 | 2 | 0 | 9 | Design + Eng |
| Mobile view truncates alert text | 4 | 2 | 1 | 0 | 7 | Design + Eng |
| No "snooze" option for known issues | 4 | 1 | 1 | 0 | 6 | Design + PM (scope decision) |

### Step 5: Future capability signals (the 11 items)

| Theme | Mentions | Strategic value |
|---|---|---|
| Operators want to share alerts with reliability engineers | 7 | High — adjacent collaboration product |
| Operators want a "what would I do?" suggestion alongside the prediction | 4 | High — taps into JTBD hidden job (audit-defensibility) |

These don't get routed to a fix team — they go to discovery. They're inputs to the next OST cycle.

### What the synthesis says about strategy

- 36% AI failure rate is a structural signal. The feature works in demo but is fragile in production. Fix the AI failure modes before adding new AI capabilities — adoption will collapse if the failure rate stays high.
- Over-confidence is the most dangerous failure type because it leads to operator action on wrong data. Calibrate first.
- Two future-capability signals (sharing with reliability engineers, "what would I do?" suggestions) point at adjacent products in the maintenance space. Consider for the next quarterly OST.

The triage isn't just about this sprint. It's about whether the AI feature stays in market or gets walked back to a "draft mode" until the failure modes are addressed.

---

## DELIVERABLE FORMAT

Every triage produces five artifacts:

### 1. Classification breakdown

Counts and percentages for the six categories. The AI-failure rate is the diagnostic — track it over time.

### 2. Ranked themes table (by category)

Within each category, themes ranked by total score with frequency, severity, and strategic fit.

### 3. AI-failure sub-type breakdown

The 6-type breakdown applied to all AI-failure items. Routes are explicit.

### 4. Routing recommendations

Each high-priority theme gets a fix team, a fix protocol, and a cycle-time estimate. The routing should be unambiguous — anyone reading the report should know who owns the fix.

### 5. Future capability signals

Items that aren't bugs or fixes — they're inputs to the next discovery cycle. Tag for downstream work.

---

## CROSS-LINK WITH ADJACENT SKILLS

- **`failure-modes`** — Each AI-failure sub-type maps to a failure mode in failure-modes. Use that taxonomy to design fixes.
- **`eval-framework`** — Every recurring AI failure should become a regression test in the eval suite. The triage report is the input to eval expansion.
- **`ai-product-metrics`** — The AI-failure rate is itself a metric. Track over time. Set thresholds.
- **`interview-synthesis`** — When triage surfaces a theme that needs deeper exploration, run interview synthesis on a sample of users who reported it.
- **`opportunity-solution-tree`** — Future capability signals from triage become opportunities in the next OST cycle.

---

## RED TEAM

This skill produces overhead instead of insight when:

**The product has no AI features.** Frequency × severity × strategic fit is sufficient for traditional UX triage. The AI-failure axis adds nothing. Use a simpler 3-axis framework.

**The feedback volume is below 20.** With 5-15 pieces of feedback, the noise dominates the signal. Don't run formal triage — read each one carefully and respond individually.

**The product is a clear, unambiguous bug.** "Login broken" doesn't need a 4-axis score. Fix it.

**The "feedback" is internal complaints, not user feedback.** Internal stakeholder feedback (executives, sales) follows a different routing protocol. Use stakeholder-mapping instead. This skill assumes feedback comes from users using the product.

**You're triaging into a backlog that nobody reads.** If the routing recommendations don't actually trigger work, the triage is theater. Either fix the upstream (PM doesn't have authority to assign work) or stop spending time on triage.

---

## WHEN WRONG

This skill misfires when:

- **The AI-failure flag is applied too loosely.** Not every complaint that mentions AI is an AI failure. "I don't like that the AI replaces my workflow" is an out-of-scope or future-capability signal, not a failure. The flag is for outputs the AI got wrong, not for design choices users dislike.
- **Severity is conflated with stakeholder volume.** A loud customer doesn't make a low-severity issue high-severity. Score severity by what happens to the user, not by who's complaining. (You can also note "vocal customer" separately for political routing.)
- **Strategic fit is judged by what's exciting, not what's planned.** If "strategic fit = 2" requires it to serve the current OKR, then a fascinating but off-strategy theme gets a 0. That's correct. The triage isn't deciding strategy — it's routing to it.
- **The roadmap doesn't update based on triage.** The whole point is the routing. If the report gets filed and ignored, the triage produced a document, not a decision.

---

## QUALITY GATE

Before shipping the triage:

- [ ] Every piece of feedback is classified into one of six categories
- [ ] AI-failure items have a sub-type assigned
- [ ] Each high-priority theme has a fix team and fix protocol
- [ ] Future capability signals are tagged for downstream discovery
- [ ] The AI-failure rate is calculated and reported
- [ ] Routing recommendations are unambiguous (no "team X or team Y")
- [ ] Themes are sourced — quotes are verbatim, not paraphrased
- [ ] The "what to ignore" list is explicit (low-frequency, anti-persona, etc.)

---

## CONCLUSION

A complete triage report ends with one paragraph:

> "Of the [N] pieces of feedback this period, [%] were AI failures, [%] were UX issues, and [%] were future capability signals. The top three themes drive [Y%] of all complaints. We're routing [theme A] to AI eval, [theme B] to design, and [theme C] to discovery. The AI failure rate is [trending up / stable / trending down] vs last period — [implication for the AI roadmap]."

If the report ends there, the team can act on Monday morning. If it ends with "lots of feedback, mixed sentiment, will continue monitoring" — the triage isn't done.

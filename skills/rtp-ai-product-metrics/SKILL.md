---
name: rtp-ai-product-metrics
id: ai-product-metrics
title: AI Product Metrics
category: craft
description: AI products require different metrics. Traditional DAU/retention are lagging indicators. Leading indicators are acceptance rate, correction rate, regeneration rate, and cost-per-successful-outcome.
difficulty: intermediate
imports:
  - eval-framework
  - feedback-flywheel
author: ai-pm
last_updated: 2026-03-28
---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## DEPTH DECISION

Are you measuring what users actually care about, or what's easy to track?

**Red flag**: "Our DAU is up, retention is up." But users are regenerating outputs constantly, correcting AI mistakes, or doing manual work despite having AI.

**Green flag**: You track acceptance rate, correction patterns, cost-per-successful-task, and hallucination drift. You catch product degradation before DAU drops.

Most PMs measure like it's 2010. AI products hide degradation in plain sight.

---

## THE TRAP

**The "Vanity Metrics" Trap**

DAU goes up. Retention looks good. But your AI is producing garbage that users fix manually. You don't notice because:

- DAU measures usage, not value
- Retention measures habit, not satisfaction
- Time spent could mean "struggling" not "succeeding"
- Revenue could be from frustration (users buying more credits to re-run failed outputs)

Traditional metrics lag. By the time DAU drops, you've already lost users' trust.

**The "Accuracy Theater" Trap**

You measure eval accuracy at 94%. Users say the product is broken. Why?
- Accuracy is unweighted (wrong answer to important question == wrong answer to trivial question)
- Doesn't measure "trust calibration" (does the model know when it's wrong?)
- Ignores the distribution of errors (10 errors on 1000 simple questions, or 1 error on 10 hard questions?)

---

## THE PROCESS

**1. Define Your Leading Indicators**

These predict product health before revenue metrics move:

- **Acceptance Rate**: What % of AI outputs do users accept as-is? (Target: 70%+)
- **Regeneration Rate**: How often do users re-run the same prompt? (Target: < 10%)
- **Correction Rate**: What % of outputs do users edit before using? (Target varies by domain)
- **Abandonment Rate**: Tasks users start but never complete with the AI
- **Cost-per-Successful-Outcome**: Actual money spent per task the user marks "done"

**2. Measure Hallucination + Trust Calibration**

- Track: False positive rate (AI says X with high confidence, but X is wrong)
- Track: Confidence gap (does AI confidence correlate with accuracy?)
- Monitor: User corrections to AI claims (high correction rate = low trust)

**3. Layer in Efficiency Metrics**

- Latency (p50, p95, p99 — tail matters)
- Token efficiency (are prompts getting bloated?)
- Cost per output (includes model cost + infrastructure)
- Cost per successful outcome (adjusted for acceptance rate)

**4. Build Cohort Dashboards**

Slice by:
- User segment (power users vs. casual)
- Task complexity (simple vs. reasoning-heavy)
- Model version
- Prompt version

Catch degradation in specific segments before it hits company metrics.

**5. Set Regression Thresholds**

- Acceptance rate drops > 3%? Investigate.
- Regeneration rate jumps > 20%? Alert.
- Cost per output increases > 10%? Check prompt version.
- Hallucination rate spikes > 2%? Pause releases.

**6. Track pass@k and pass^k Metrics (Anthropic Framework)**

These consistency metrics measure whether your system is capability-limited or consistency-limited:

- **pass@k**: Probability of at least one correct solution in k attempts. Answers: "Can the system succeed if given multiple tries?" Use for: development, capability benchmarking, research, understanding raw capability.
- **pass^k**: Probability that ALL k trials succeed consistently. Answers: "Will every interaction work reliably?" Use for: production readiness, SLA commitments, customer-facing agents where every interaction must work.

**Decision table:**
| Scenario | pass@k | pass^k | Diagnosis | Action |
|----------|--------|--------|-----------|--------|
| High pass@k, low pass^k | 0.80+ | 0.33- | Capable but inconsistent | Improve determinism: few-shot examples, temperature tuning, structured outputs |
| Both low | 0.50- | 0.20- | Capability problem | Retrain, change model, redesign prompts |
| Both high | 0.90+ | 0.85+ | Production ready | Scale confidently, monitor drift |

**Real example**: A coding agent with pass@1 = 0.8 (80% success rate) has pass^5 = 0.33 (33% chance all 5 solutions work). That's a 67% failure rate for multi-step tasks. Customers see failure, even though the system is 80% capable.

For customer-facing agents, track pass^k not pass@k. A single failure in a sequence damages trust more than raw capability metrics suggest.

**7. Define Anti-Metrics (What Going UP Would Be Bad)**

Most metric frameworks define what success looks like. Anti-metrics define what a dangerous signal looks like — a metric that's increasing but shouldn't be.

**The pattern:** For every primary metric, ask: "What metric going UP would actually signal a problem?"

| Primary Metric | Anti-Metric | Why It's Dangerous |
|----------------|-------------|-------------------|
| DAU (Daily Active Users) | Session count with no task completion | Users are coming back because the AI keeps failing — they're retrying, not succeeding |
| Acceptance rate | Acceptance rate + zero edits on complex tasks | Users may be blindly accepting AI output without reviewing. Over-trust is a failure mode, not a success signal |
| Feature adoption | Adoption + increased support tickets | Users are adopting but can't figure it out — adoption without competence |
| Time in product | Time in product + low task completion | User is stuck, not engaged. High time-on-task in a productivity tool means friction, not value |
| Cost reduction | Cost reduction + declining quality scores | You cut cost by degrading quality. The savings are temporary — churn follows |

**Process:**
1. For each primary metric and guardrail metric, define its anti-metric
2. Monitor anti-metrics alongside primaries on the same dashboard — never in isolation
3. If a primary metric is trending up AND its anti-metric is also trending up, investigate before celebrating. The growth may be masking a deeper problem.

**The check that catches perverse incentives:** Anti-metrics are the systematic defense against Goodhart's Law — "when a measure becomes a target, it ceases to be a good measure." By defining what going UP would mean going WRONG, you force the team to think about gaming, over-optimization, and unintended consequences.

**8. Detect Eval Saturation**

When your eval suite stops moving despite meaningful improvements in production, your metrics have plateaued. Signs include:

- All metrics are green, but users still complain or support tickets spike
- Scores haven't moved in 3+ months despite launches and iterations
- New model versions show no improvement on evals, but users perceive them as better (or vice versa)

**Root cause**: Your eval set is stale. It measures what you've already solved, not what breaks in production.

**Fix**: Refresh eval sets monthly. Replace 20-30% of eval dataset with real production traces — actual user inputs that failed, edge cases you didn't anticipate, novel task types. Track eval "difficulty score" — if average difficulty drops over time, your suite is getting too easy.

**Process:**
1. Monthly: Pull top 20-30 errors from production logs
2. Add to eval set, removing lowest-signal existing examples
3. Measure: Does this new eval version show measurable gaps in your system?
4. Iterate: If new evals don't expose problems, you're not testing hard enough

---

## NORTH STAR + AARRR FOR AI PRODUCTS

The metrics above (acceptance rate, regeneration rate, hallucination rate, pass^k) are AI-specific leading indicators. They tell you whether the model is doing its job. They do not tell you whether the *product* is doing its job.

For that, you need the foundational metric framework — North Star + AARRR — adapted for AI features. Lenny Rachitsky's North Star guide is the canonical reference. AARRR (Acquisition / Activation / Retention / Revenue / Referral) is the canonical funnel. Both are PM table stakes. The AI twist is what they look like when the product is non-deterministic.

### The North Star for AI Products

**The Lenny criteria for a North Star metric:**
1. Represents value delivered to users (not value extracted from them)
2. Predicts long-term revenue
3. Measurable
4. Actionable (the team can move it)
5. Understandable (everyone in the company can explain it)

**The AI-specific failure mode:** Most AI products pick a North Star that ignores AI quality. "Daily active users." "Queries per day." "Sessions per week." These are activity metrics — they go up when users come back, regardless of whether the AI did its job.

**The 0.1% angle: AI features need a "successful AI interaction rate" North Star that pure DAU/retention misses.**

The pattern: pick the North Star metric AT the moment of AI-driven value delivery. Not "users who logged in" — "users who completed a successful AI-assisted task." Not "queries per session" — "queries that produced a user-accepted output."

**The canonical AI-feature funnel (the five-stage model):**

| Stage | Definition | What "Good" Looks Like |
|---|---|---|
| **Surfaced** | The AI feature was visible to the user (in their UI, in their workflow) | High — the feature is discoverable |
| **Invoked** | The user actually used the feature (typed a prompt, clicked the button) | Conversion from surface depends on UX clarity |
| **Completed** | The AI finished generating an output (no timeout, no refusal, no error) | High — model and infra reliability |
| **Accepted** | The user kept the output (used it, copied it, sent it, saved it) | The acceptance rate metric — the truth about quality |
| **Retained** | The user came back and used the feature again within 7 days | The trust metric — did the experience earn repeat use? |

Each stage has a drop-off. Each drop-off has a different optimization. **The North Star sits at "Accepted" or "Retained" — never at "Invoked."** Invocation is activity. Acceptance is value.

**Worked example:**

For an AI contract review tool, candidate North Stars:

- **Bad:** "Daily active users" — measures coming back, not value
- **Bad:** "Queries per day" — measures activity, not success
- **Bad:** "Reviews completed" — measures throughput, not whether the review was useful
- **Better:** "Reviews accepted by user without edit" — measures whether the AI's output was good enough as-is
- **Best:** "Weekly active users who accept at least 3 reviews per week" — combines retention, activity, and quality into one metric

The "best" version satisfies all five Lenny criteria. It moves only when the product is genuinely working. It can't be gamed by adding more users or running more queries.

### AARRR Adapted for AI Features

The AARRR funnel applies to AI products, but each stage gets an AI-specific layer.

#### Acquisition

The user discovers the feature exists. Same as any product — marketing, search, word of mouth, in-product placement.

**The AI-specific twist:** Unlike traditional features, AI features benefit from social proof signals that signal "this AI doesn't suck." Demo videos showing real outputs. Customer logos. Eval transparency. Hallucination rates published openly. Trust signals at acquisition time reduce the "is this just AI hype?" friction.

**Metric:** Trial conversion rate from acquisition channel. Watch for big variation by channel — power-user channels (developer communities, expert forums) often convert at 3-5x the rate of generic channels because the audience already trusts AI and knows how to use it.

#### Activation

The user experiences first value. For AI features, this is the first successful interaction.

**The AI-specific twist:** Activation is about whether the user's *first prompt produces a useful output*. If the first prompt fails or feels wrong, churn risk in the first week is 3-5x higher than for users whose first prompt succeeded. The first impression is load-bearing.

**Metric:** First-prompt acceptance rate. Measures: of users who tried the feature once, what % accepted the AI's output without editing or regenerating?

**Optimization:** First-time user experience matters more in AI products than traditional ones. Show example prompts. Suggest queries. Pre-populate the input with a high-confidence template. Get the user to a "yes, this worked" moment in their first 60 seconds.

#### Retention

The user comes back and uses the feature again.

**The AI-specific twist:** Trust takes 4 weeks to stabilize (per the `uncertainty-research` skill). A user who uses the feature 3 times in week 1 and never returns has been quietly disappointed. A user who uses it 1 time per week for 8 weeks has built durable trust. Track retention curves by week, not just by month.

**Metric:** Weekly active acceptance rate — % of weekly actives who accepted at least one AI output that week. Catches users who keep coming back but stop accepting outputs (a sign of declining trust before churn).

**Optimization:** The biggest retention lever in AI products is fixing the failure modes that surface in week 2-3. Users tolerate week-1 errors as "I'm still learning." They don't tolerate week-3 errors. The eval-and-quality work compounds at retention.

#### Revenue

The user pays. For AI products, this often shows up as: free tier users converting to paid, paid users upgrading to higher tiers, expanding seat count.

**The AI-specific twist:** AI features have unit cost. Revenue without unit economics modeling produces "we have $1M ARR and burn $1.2M on inference" surprises. Track revenue PER unit of AI capacity consumed. Track revenue versus cost-per-successful-outcome (the metric from the Process section above).

**Metric:** Net revenue per user, after AI cost. Not gross. The AI cost is the real margin compression.

**Optimization:** The pricing model should align with the cost structure. Per-seat pricing (flat fee per user) is a margin trap if power users consume 10x the AI capacity of casual users. Usage-based pricing aligns better but requires the user to understand and accept variable bills. The right answer depends on segment — enterprise often prefers flat, prosumer often prefers usage-based.

#### Referral

The user invites others.

**The AI-specific twist:** AI products have a unique referral mechanism — *output sharing*. When a user copies an AI output and pastes it into Slack, email, or a doc, the recipient sees the output AND the implicit endorsement. Track output-shared rate as a leading indicator of organic growth.

**Metric:** % of accepted outputs that were shared externally. Higher = organic referral surface area.

**Optimization:** Make sharing easy. Watermark outputs subtly with the product name (without compromising the user's intent). Offer "share this answer" affordances. Track which outputs get shared most — they reveal which use cases produce shareable artifacts and which produce private ones.

### Mapping the AI Funnel to AARRR

The five-stage AI funnel (Surfaced → Invoked → Completed → Accepted → Retained) maps onto AARRR but isn't identical. Use both:

| AARRR | Maps to AI Funnel | Why Both Matter |
|---|---|---|
| Acquisition | Pre-Surfaced | User has to find the product before the AI funnel begins |
| Activation | Surfaced + Invoked + Completed (first time) | Activation in AI = first successful interaction |
| Retention | Repeated Acceptance + Retention | Coming back AND accepting outputs |
| Revenue | (Conversion event, separate) | Often gated by retention |
| Referral | Output Sharing | Distinct from formal referral programs |

**The discipline:** Build dashboards that show both. AARRR for the business view (where executives think). The five-stage AI funnel for the product view (where PMs and engineers diagnose). They tell the same story at different altitudes.

### The Combined Dashboard Structure

Add this to the dashboard template in the section above. The North Star + AARRR sit *above* the AI-specific metrics — they're the company-level view that the AI quality metrics support.

```
NORTH STAR METRIC: [e.g., Weekly active users who accept ≥3 AI outputs per week]
Current: [Value]    Target: [Value]    Trend (4w): [↑/↓]

AARRR FUNNEL
| Stage | Metric | Current | Target | Trend |
|---|---|---|---|---|
| Acquisition | Trial conversion rate | — | — | — |
| Activation | First-prompt acceptance rate | — | — | — |
| Retention | WAU with ≥1 acceptance | — | — | — |
| Revenue | Net revenue per user (post-AI cost) | — | — | — |
| Referral | % outputs shared externally | — | — | — |

AI FUNNEL (per primary feature)
| Stage | Conversion | Drop-off Reason | Action |
|---|---|---|---|
| Surfaced → Invoked | — | — | — |
| Invoked → Completed | — | — | — |
| Completed → Accepted | — | — | — |
| Accepted → Retained (7d) | — | — | — |
```

The discipline: every drop-off in the AI funnel ladders up to a drop-off in AARRR. If first-prompt acceptance is low, AARRR Activation is low. If accepted-to-retained conversion is low, AARRR Retention is low. The funnels aren't separate diagnoses — they're the same diagnosis at different altitudes.

---

## KEY DIAGNOSTIC QUESTIONS

**On Leading Indicators:**
- Can you tell me the acceptance rate for your product right now? (Be honest: can you?)
- How do you know if a prompt change made things better or worse?
- What's your cost per successful user outcome, not per API call?

**On Hallucination Awareness:**
- Do you track false positives separately from false negatives?
- Can you measure how often users correct AI outputs after using them?
- Do you know which domains/tasks have highest hallucination risk?

**On Segment Visibility:**
- Are your metrics the same for all users, or split by segment?
- Do power users have different acceptance rates than casual users?
- Where is degradation happening first? (Usually in the edge cases.)

**On Causality:**
- If acceptance rate drops, can you trace it to a specific change? (Prompt, model, feature)
- Do you monitor metrics BEFORE and AFTER every release?
- Can you explain why a metric changed, or are you just reacting?

---

## REALITY CHECK

**What mature AI product telemetry looks like:**
- Real-time dashboard: acceptance rate, regeneration rate, cost per output, latency
- Per-cohort breakdowns: power users vs. casual, by task type
- Automated alerts: acceptance rate down > 3%, cost per output up > 10%
- Regression testing: new prompt version must not degrade any metric
- User feedback loop: corrections flagged, investigated, fed back to evals

**What it doesn't look like:**
- "Our DAU is up" (but users are frustrated)
- Accuracy metrics only (ignoring cost, latency, hallucination rate)
- No visibility into cost per successful outcome
- Monthly reviews of metrics (by then, damage is done)
- Metrics that only go up (if you never see degradation alerts, you're not measuring hard things)

---

## QUALITY GATE

**Metrics infrastructure must include:**
1. ✓ Acceptance rate tracking (per user, per task type, per model version)
2. ✓ Correction/edit distance tracking (how much do users change AI output?)
3. ✓ Cost-per-successful-outcome (not just API cost)
4. ✓ Hallucination/false positive monitoring (calibrated by domain)
5. ✓ Latency tracking (p50, p95, p99)
6. ✓ Cohort analysis (power users vs. casual, task type, geography)
7. ✓ Automated regression testing (new releases checked against baseline)
8. ✓ Regression thresholds (with automated alerts)

**Blocks shipping if:**
- No acceptance rate baseline to compare against
- Cost-per-outcome increases without explanation
- Hallucination rate increases > 2%
- Latency degradation > 20% (p95)

---

## WHEN WRONG

**You'll see:**
- DAU up, but support tickets spike (users struggling silently at first, then complaining)
- Acceptance rate drops without explanation (didn't correlate with any release)
- Cost per output climbs (prompts got verbose, model overthinking)
- Certain segments have degraded acceptance (you missed it because you only looked at aggregate)
- Users switch to competitors but you don't know why (you never asked about correction rate)

**Recovery:**
- Pull the metrics for the past 30 days, split by segment
- Correlate drops with releases/changes
- Investigate: was it a prompt change, model change, or user behavior shift?
- Measure the actual impact: how many users affected, what's the revenue impact?
- Fix the root cause, then re-verify with your metrics
- Adjust your alert thresholds based on what you learned

---

## AI PRODUCT METRICS DASHBOARD TEMPLATE

Use this structure to build your product metrics dashboard. Adapt the metric names to your domain, but keep the structure: leading indicators first, then consistency, then cost, then cohort breakdowns.

### Dashboard: [Product Name]

**Last Updated:** [Date]
**Report Period:** [Week/Month]

#### Leading Indicators

| Metric | Current | Target | Trend (7d) | Alert Threshold |
|--------|---------|--------|------------|-----------------|
| Acceptance Rate | — | 70%+ | — | Drop > 3% |
| Regeneration Rate | — | < 10% | — | Rise > 20% |
| Correction Rate | — | [Domain-specific] | — | TBD |
| Abandonment Rate | — | < 5% | — | Rise > 2% |
| Cost per Output | — | [Budget] | — | Rise > 10% |
| Cost per Successful Outcome | — | [Budget] | — | Rise > 15% |

#### Consistency Metrics

| Metric | pass@1 | pass@3 | pass@5 | pass^5 | Target (pass^5) |
|--------|--------|--------|--------|--------|-----------------|
| Overall | — | — | — | — | 0.85+ |
| Simple Tasks | — | — | — | — | 0.90+ |
| Complex Tasks | — | — | — | — | 0.75+ |
| [Segment] | — | — | — | — | TBD |

**Interpretation**: If pass^5 is low while pass@5 is high, your system is capable but inconsistent. Focus on determinism improvements.

#### Cost Metrics

| Metric | Per-Query | Per-Success | Monthly Spend | vs Budget | vs Prior Month |
|--------|-----------|-------------|---------------|-----------|----------------|
| Compute Cost | $— | $— | $— | — | — |
| Token Efficiency | — tokens | — | — | — | — |
| Model Cost | $— | $— | $— | — | — |
| Infrastructure | $— | $— | $— | — | — |
| Total Cost | $— | $— | $— | — | — |

**Cost-per-Success calculation**: Total monthly spend ÷ (successful outcomes / month)

#### Quality Metrics

| Metric | Current | Target | Status | Notes |
|--------|---------|--------|--------|-------|
| Hallucination Rate | —% | < 2% | — | False positive rate |
| False Negative Rate | —% | < 3% | — | Missed cases |
| Confidence Calibration | — | High | — | Does AI know when it's wrong? |
| User Correction Rate | —% | TBD | — | % outputs edited before use |

#### Latency Metrics

| Percentile | Current | Target | vs Prior Week | Status |
|------------|---------|--------|----------------|--------|
| p50 | — ms | — ms | — | Median |
| p95 | — ms | — ms | — | Tail matters for UX |
| p99 | — ms | — ms | — | Outliers |

#### Cohort Breakdowns

| Segment | Acceptance Rate | Correction Rate | Cost/Success | pass^5 | Trend |
|---------|-----------------|-----------------|--------------|--------|-------|
| Power Users | —% | —% | $— | — | — |
| Casual Users | —% | —% | $— | — | — |
| [Task Type A] | —% | —% | $— | — | — |
| [Task Type B] | —% | —% | $— | — | — |
| [Geography/Region] | —% | —% | $— | — | — |
| [Model Version A] | —% | —% | $— | — | — |
| [Model Version B] | —% | —% | $— | — | — |

**Why slice by segment**: Degradation usually hits edge cases first. Aggregate metrics hide problems.

#### Health Status Summary

| Category | Status | Notes |
|----------|--------|-------|
| Leading Indicators | 🟢 | Acceptance rate stable, regen rate low |
| Consistency | 🟢 | pass^5 = 0.82, above target |
| Cost Efficiency | 🟡 | Cost/success up 8%, investigate |
| Quality | 🟢 | Hallucination rate within bounds |
| Latency | 🟢 | p95 within SLA |

**Alerts Triggered:**
- [List any metrics that crossed thresholds]

**Actions for Next Period:**
- [List decisions: prompt changes, model updates, eval refreshes, etc.]

---

## BUILDING YOUR DASHBOARD

**Start here (Month 1):**
- Acceptance rate + regeneration rate (easiest to instrument)
- Cost per output (from your inference platform logs)
- Basic cohort: power users vs. casual

**Expand (Month 2-3):**
- Correction rate (track edit distance on outputs)
- Hallucination monitoring (user feedback loop)
- Latency tracking (p50, p95, p99)

**Mature (Month 4+):**
- pass@k and pass^k metrics
- Eval saturation detection
- Automated regression testing
- Real-time alerts on all thresholds
- Monthly eval refresh with production traces

**Common pitfall**: Building a dashboard is not enough. You need to *act* on it. Set specific owners for each alert threshold. Weekly metric reviews. Monthly asks: "What changed this week? Why? What do we do about it?"

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

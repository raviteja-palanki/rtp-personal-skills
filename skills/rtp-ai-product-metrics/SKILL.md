---
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

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
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

**7. Detect Eval Saturation**

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

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

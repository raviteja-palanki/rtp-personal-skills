---
name: rtp-production-observability
description: Catch silent AI degradation in production before users leave. Monitor latency, cost, quality drift, usage patterns, and error categorization with real-time alerts — not weekly dashboards. AI systems degrade silently in ways traditional logging misses (model drift, prompt regressions, distribution shift). Use when shipping an AI feature to production, debugging "it worked yesterday" reports, designing alerts for AI systems, or auditing whether you'd catch a degradation before users complain. Triggers on "AI in production", "monitoring AI", "model drift", "quality regression", "production observability", "alerts for AI", "silent failure".
---
## DEPTH DECISION

Can you detect when your AI product degraded in the past hour? Or do you find out when users complain?

**Red flag**: "We check dashboards weekly." By then, you've served bad outputs to thousands of users.

**Green flag**: Real-time alerts on latency spikes, cost anomalies, quality drift, and usage patterns. You detect degradation and roll back before it becomes a user problem.

Silent failure is the AI product killer.

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

**The "Silent Degradation" Problem**

Your AI product slowly gets worse. But you don't notice because:

- Traditional metrics (DAU, retention) lag by weeks
- Users tolerate degradation until it's intolerable
- Quality drift is statistical (slightly more hallucinations, slightly worse reasoning)
- Failures are often soft (wrong answer, not crashed system)

You ship a prompt change. Hallucination rate ticks up 2%. Users don't complain immediately. Two weeks later, your support volume spikes. You don't connect it to the change.

**The "Observability Debt" Problem**

Building observability feels like "non-product work." So you skip it. Then:
- You can't correlate user problems to system changes
- Cost surprises you (infrastructure bills spike)
- Performance degrades and you don't know why
- You can't prove that a fix actually worked
- Rollbacks are painful because you don't have baseline metrics

The cost of not observing is higher than the cost of observing.

---

## THE PROCESS

**1. Define What to Log**

Log strategically (logs are expensive and noisy):

**Per request:**
- Request timestamp, ID, user segment
- Input tokens, output tokens, total cost
- Latency (time to first token, total)
- Model version, prompt version
- Output quality signals (confidence, uncertainty markers)

**Per batch/hourly:**
- Latency distribution (p50, p95, p99)
- Cost per output, cost per successful outcome
- Quality metrics (acceptance rate, regeneration rate, correction rate)
- Error categories (timeout, rate limit, model error, validation error)
- Usage patterns (peak traffic, geographic distribution)

**On degradation:**
- Hallucination spike (false positive rate increases)
- Latency regression (p95 crosses threshold)
- Cost anomaly (cost per output increases > 15%)
- Availability drop (error rate increases > 2%)

**2. Build Observability Dashboards**

Real-time dashboards for:
- **System Health**: Latency, error rate, cost, availability
- **Quality Metrics**: Acceptance rate, regeneration rate, correction rate, hallucination rate
- **Usage Patterns**: Peak times, user segments, task types, geographic distribution
- **Cost Tracking**: Cost per output, cost per successful outcome, cost by segment

Split every metric by:
- Model version (to detect model regression)
- Prompt version (to catch prompt-induced degradation)
- User segment (degradation often hits edge cases first)
- Time of day (some issues are traffic-dependent)

**3. Set Regression Thresholds with Alerts**

**Latency Alerts:**
- p95 latency > 5 sec (or your domain threshold)
- p99 latency > 10 sec
- Time to first token > 2 sec (affects user experience significantly)

**Cost Alerts:**
- Cost per output increases > 15% (usually bad prompting or model change)
- Cost per successful outcome increases > 20%
- Sudden spike in token usage (runaway generation, bad prompt, or abuse)

**Quality Alerts:**
- Acceptance rate drops > 3%
- Hallucination rate increases > 1%
- Regeneration rate increases > 20%
- Error rate increases > 2%

**Usage Alerts:**
- Spike in specific error category (rate limits? model errors? validation failures?)
- Unusual geographic pattern (potential abuse or regional outage)
- Sustained drop in traffic (users abandoning due to degradation?)

**4. Harness-Level Monitoring**

When running multi-agent harnesses (Planner/Generator/Evaluator), monitor each agent individually AND the pipeline as a whole.

**Key signals per agent:**
- **Planner spec quality:** Does the evaluator pass the spec on first try? Declining pass rate = planner regression.
- **Generator iteration count per sprint:** Trending up = degradation (model worse, prompt worse, or context confusion).
- **Evaluator false pass rate:** Cross-validate with deterministic checks. If evaluator marks bad outputs as good, its judgment is breaking.
- **Inter-agent latency:** How long do handoffs take? Planner → Generator → Evaluator delays compound. Alert on > 2x baseline.
- **Context utilization per agent:** Track tokens used by each agent per sprint. Approaching Pre-Rot Threshold (see below).

**Context Anxiety Detection:** Anthropic finding — agents wrap up work prematurely as context fills. Monitor output quality vs. context utilization. If quality drops at 50-60% of max context, you've hit the Pre-Rot Threshold. Alert on this pattern: quality dropping while context is abundant is a signal to pause and investigate.

**Sprint Contract Compliance:** For harness systems, monitor whether agents are adhering to sprint contracts — are they completing all criteria before declaring done? Track: criteria pass rate per sprint (did agents complete 100% of required work?), iteration count per sprint (are they overshooting?), kill condition triggers (are they exiting at the right moment?).

Set alerts on:
- Planner spec fail rate increasing (regenerate spec, don't proceed)
- Generator iteration count trending up (model or context degradation)
- Evaluator false positive rate (re-eval the evaluator)
- Inter-agent latency spike (investigate handoff bottleneck)
- Context anxiety pattern (quality drops while tokens available)
- Sprint contract violations (agents not meeting criteria before exit)

**5. Categorize Errors Ruthlessly**

Not all errors are equal. Categorize by:

**Transient** (can retry):
- Timeout
- Rate limit
- Temporary model unavailability
- Network blip

**User Error** (they sent bad input):
- Validation failure
- Malformed request
- Out-of-bounds parameters

**System Failure** (we broke something):
- Model error (hallucination, reasoning failure)
- Prompt error (output format broken)
- Infrastructure failure
- Cost overrun (token limit exceeded)

Alert differently for each. Transient errors retry. User errors log and ignore. System failures escalate.

**6. Cost-of-Observability Accounting**

Observability isn't free. Track:
- Log storage costs (might exceed product revenue at scale)
- Query costs (dashboards hitting log systems constantly)
- Alert fatigue (too many false positives kills alerting value)

Optimize:
- Log only high-signal data (not every request)
- Aggregate before storing (hourly rollups vs. per-request logs)
- Prune old logs (30-day retention? 90-day?)
- Sample traffic (if you have 1M requests/day, sample 10K for detailed logging)

---

## KEY DIAGNOSTIC QUESTIONS

**On Logging Completeness:**
- Can you tell me the cost per output for requests in the last hour? (Real answer, not estimate.)
- Do you log which prompt version produced each output?
- Can you correlate a quality drop to a specific change? (What metrics would you check first?)

**On Dashboard Visibility:**
- Show me your real-time latency dashboard. (Do you have one?)
- Can you see cost anomalies in < 1 hour? (Or do you discover them in the weekly report?)
- Do you track acceptance rate by user segment? (Where is degradation hitting first?)

**On Alert Responsiveness:**
- What happens when latency p95 spikes? (Do you get paged? Does someone check it?)
- If quality drops 5%, how long until you know? (Should be < 5 minutes.)
- Can you rollback a prompt change in response to an alert? (Or does it require a deploy?)

**On Error Understanding:**
- How many requests failed today? (For each category: transient, user error, system failure.)
- Which error category is growing? (Indicator of a real problem.)
- Can you distinguish between "user sent garbage" and "your system broke"?

---

## REALITY CHECK

**What mature AI product observability looks like:**
- Real-time dashboards: latency, cost, quality, errors
- Automated alerts: paging on degradation, not on normal variance
- < 5 minute detection time (from degradation to alert)
- < 30 minute recovery time (from alert to rollback or fix)
- Error categorization (you know which errors matter)
- Correlation analysis (you can connect drops to changes)
- Cost tracking (you know which features are expensive)

**What it doesn't look like:**
- Weekly reviews of metrics (too late, damage is done)
- No latency/cost dashboards (flying blind)
- Alerts on everything (alert fatigue kills responsiveness)
- Can't connect quality drop to the prompt/model change
- No error categorization (all errors treated equally)
- Log volume consuming majority of infrastructure budget

---

## QUALITY GATE

**Observability infrastructure must include:**
1. ✓ Per-request logging (timestamps, tokens, cost, latency, versions)
2. ✓ Real-time dashboards (latency, cost, quality, errors, by segment)
3. ✓ Regression thresholds (with automated alerts)
4. ✓ Cost tracking (cost per output, cost per successful outcome)
5. ✓ Error categorization (transient vs. user error vs. system failure)
6. ✓ Correlation analysis (what changed when metrics moved?)
7. ✓ Rollback automation (< 5 min to respond to alert)
8. ✓ Log retention policy (cost-effective, not forever)

**Blocks shipping if:**
- No baseline cost-per-output to compare against
- Can't measure latency impact of change
- Alerts would generate false positives > 10% (will be ignored)
- Rollback procedure untested

---

## WHEN WRONG

**You'll see:**
- Quality complaints spike but you can't find the cause
- Infrastructure costs balloon unexpectedly (runaway token usage)
- Latency degradation but only users report it
- Specific user segments suffering (you didn't see it in aggregate metrics)
- Recovery takes hours (you don't know what to roll back first)

**Recovery:**
- Implement emergency logging (detailed per-request logs to understand the failure)
- Correlate timing (when did the problem start? What changed that day?)
- Segment analysis (which users affected? Which queries? Which model versions?)
- Build the observability you should have had (cost-of-learning)
- Set stricter thresholds (you want to catch this earlier next time)
- Automate rollback for future alerts (so recovery is < 5 min)

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

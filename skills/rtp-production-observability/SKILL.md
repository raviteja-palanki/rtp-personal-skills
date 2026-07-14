---
name: rtp-production-observability
description: >
  Catch silent AI degradation in production before users leave. Monitor latency, cost,
  quality drift, usage patterns, and error categorization with real-time alerts — not
  weekly dashboards. AI systems degrade silently in ways traditional logging misses
  (model drift, prompt regressions, distribution shift). Use when shipping an AI feature
  to production, debugging "it worked yesterday" reports, designing alerts for AI
  systems, or auditing whether you'd catch a degradation before users complain.
  Triggers on "AI in production", "monitoring AI", "model drift", "quality regression",
  "production observability", "alerts for AI", "silent failure", "traces", "spans",
  "failure genealogy", "why did the agent fail".
  Also carries what ops-grade monitoring skips: the trace (not the request) as the unit of
  AI observability, quality-aware alerting on eval-score drift (the PM's signal, not just
  p99 latency), separating "the model failed" from "the harness failed the model", and
  failure-mode genealogy (thousands of traces → the ~3 root causes behind ~80% of failures).
  Pairs with: eval-framework (the scores you attach to spans and alert on), confidence-tuner
  (the judge that produces those scores must be calibrated), invisible-stack / context-spec
  (where most "model" failures actually route), feedback-flywheel (production traces are the
  raw material that closes the loop), eval-driven-development (traces feed the challenge tier).
imports:
  - stress-test
  - eval-framework
  - feedback-flywheel
---

## DEPTH DECISION

Can you detect when your AI product degraded in the past hour? Or do you find out when users complain?

**Red flag**: "We check dashboards weekly." By then, you've served bad outputs to thousands of users.

**Green flag**: Real-time alerts on latency spikes, cost anomalies, quality drift, and usage patterns. You detect degradation and roll back before it becomes a user problem.

Silent failure is the AI product killer.

---

## THE ONE IDEA

**In a deterministic system you monitor whether it's *up*. In an AI system you monitor whether it's *right* — and "right" degrades silently, continuously, and statistically. That single difference forces three shifts most teams never make:**

1. **The unit of observation is the trace, not the request.** A request log tells you *what happened*; a trace tells you *why* — the full reasoning path, every tool call, retrieval, and model invocation as nested spans. You cannot debug a wrong answer from a status code. (This is now the industry standard: OpenTelemetry graduated CNCF with **GenAI semantic conventions**, and the canonical 2026 pattern is *eval-score-as-span-attribute* — quality lives inside the trace.)
2. **The signal that matters is eval-score drift, not p99 latency.** Latency and cost are the SRE's job and they move loudly. Quality drift moves silently — "context recall −4% this week" — and it's *the PM's job to alert on it*. A green latency dashboard over a rotting quality score is exactly the silent failure that kills AI products.
3. **Most "model failures" are context failures — attribute correctly or you'll fix the wrong thing.** With frontier models, degradation usually traces to the *harness* (context overflow, retrieval stuffing, a prompt regression), not the model's raw capability. "The harness failed the model" is a different bug than "the model failed," and it routes to a different team.

And the integrative point that reframes the whole skill: **observability is not a downstream ops chore — it's the *top* of the feedback flywheel.** Production traces are the raw material that feeds the eval challenge tier (`eval-driven-development`), the correction clusters that reveal unmet needs (`ai-product-metrics`), and the recalibration set for the judge (`confidence-tuner`). Read defensively, the trace catches a regression. Read offensively, the trace *is* the discovery pipeline.

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
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

## TRACES & SPANS: THE UNIT OF AI OBSERVABILITY

The per-request logging above tells you *what* happened. To debug *why*, you need the trace — and this is the shift ops-grade monitoring misses.

- **A trace is the full path of one request through your system.** A **span** is one step inside it — an LLM call, a retrieval, a tool invocation, a guardrail check. Nested spans reconstruct the reasoning path. Analogy: the **trace is a patient's full medical chart; each span is one test result**. You don't diagnose from the discharge code; you read the chart.
- **This is now standardized — instrument against it.** OpenTelemetry graduated the CNCF with **GenAI semantic conventions**; each tool call, model invocation, and retrieval step becomes a child span with standard attributes (model name, token counts). Instrument against the open convention, not a vendor SDK, so you keep the migration door open.
- **Attach eval scores to spans (eval-as-span-attribute).** The canonical 2026 pattern: quality metrics live *inside* the trace, not in a separate dashboard. That's what makes "correlate a quality regression to the exact config/prompt change that caused it" a query instead of an archaeology project — and it's the join that turns the two skills together: `eval-framework` produces the score, observability records it on the span.

*(Sources: [OpenTelemetry GenAI semantic conventions, Greptime 2026](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions); [OTel graduation + GenAI observability, 2026](https://www.webhani.com/blog/opentelemetry-graduation-genai-observability-2026).)*

## TRACE DEBUGGING: LOGIC BUG vs MEMORY BUG (and "the harness failed the model")

When a trace shows a wrong output, resist the reflex to blame the model. Classify the failure first:

- **Logic bug** — the agent followed a *wrong procedure* (bad plan, wrong tool, flawed reasoning step). The fix is in the instructions/architecture.
- **Memory bug** — the agent followed the *right procedure but lost the context* it needed (dropped an earlier fact, forgot a constraint). The fix is in state/memory management.
- **The harness failed the model** — the classic false accusation. Example: retrieval stuffed 12 documents / 47K tokens into a 64K window; the relevant fact was there but *drowned*. The model didn't fail — the context pipeline did. With frontier models this is the *majority* case. It routes to `invisible-stack` / `context-spec`, not to a model swap.

**Slice with high-cardinality queries.** Aggregate metrics hide the failure; the trace store lets you slice by user, tenant, error type, model/prompt version, and time. Degradation almost always concentrates in a slice (one tenant, one task type, one prompt version) before it shows in the average. Find the slice, read its traces, classify the bug.

## QUALITY-AWARE ALERTING: alert on eval-score drift, not just p99

The SRE team already alerts on latency and cost — those move loudly. The PM's unique contribution is **alerting on quality drift**, which moves silently. Alert on the eval score itself: "context recall −4% this week," "hallucination-rate +1.5% on tenant X," "acceptance −3% since prompt v7." Run a lightweight eval continuously on a sample of production traffic and treat its drift as a first-class signal.

**Tier the alerts, or fatigue kills them:**

| Tier | Trigger | Route |
|---|---|---|
| **Critical** | Safety / policy breach, availability drop | Page someone now |
| **Warning** | Quality drift (eval-score regression, guardrail FP-rate rising) | Daily digest, investigate same-day |
| **Informational** | Usage-pattern shifts, cost trend toward the cliff | Weekly review |

Two AI-specific monitors ops teams forget: the **guardrail false-positive rate** (a guardrail that over-blocks trains users to route around it — a Layer-1 alert-fatigue problem manifesting in production), and **agent gaslighting** — the agent *claims* it did the thing ("I've booked the meeting"), but the trace shows the API was never called. Detect it by comparing the agent's stated actions against the actual tool/API-call spans in the trace. Fabricated execution evidence passes every text-only quality check; only the trace catches it.

## FAILURE-MODE GENEALOGY: from thousands of traces to ~3 root causes

Defensive observability catches one regression. Offensive observability does something no single trace can: **aggregate thousands of failing traces and cluster them by root cause.** The pattern that repeats across mature teams — roughly **80% of failures trace back to ~3 architectural root causes** (⚠ practitioner heuristic, not a law — measure your own distribution). Those root causes are *invisible in any single trace*; they only emerge in aggregate. One overflowing retrieval step, one ambiguous instruction, one missing state handoff — each generating hundreds of surface-different failures.

This is the observability payoff that feeds the rest of the stack: the genealogy is your architectural fix-list (ranked by volume), your challenge-tier seed (`eval-driven-development`), and your demand-signal map (`ai-product-metrics`'s "evals as discovery"). The review queue and the failure clusters are the same raw material seen from two skills. *(B6 "production-grade trace scoring" framing: score traces to protect **users**, not to decorate dashboards — the genealogy is what turns scoring into action.)*

## KEY DIAGNOSTIC QUESTIONS

**On Tracing & Attribution:**
- When an output is wrong, can you pull its full trace (every span) — or only its request log?
- Are eval scores attached to spans, so you can correlate a quality drop to the exact change?
- For your last "the model got worse" incident, was it the model or the harness (context overflow, retrieval, prompt regression)? How did you tell them apart?

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
9. ✓ Trace capture with nested spans (OpenTelemetry GenAI conventions), eval scores attached to spans
10. ✓ Quality-drift alerting on eval score (not just latency/cost), tiered critical/warning/informational
11. ✓ Failure attribution discipline (logic bug vs memory bug vs harness-failed-the-model)
12. ✓ Agent-gaslighting check (stated actions reconciled against actual API-call spans)

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

## WHERE THIS MEETS YOUR STACK

Observability is the top of the feedback flywheel — it hands the rest of the domain its raw material:

- **The quality scores you alert on come from → `eval-framework`, and are only trustworthy if the judge is calibrated → `confidence-tuner`.** Alerting on a drifting eval score is worthless if the judge producing it is itself drifting. Calibrate the judge; then trust the alert.
- **Most "model degraded" incidents route to → `invisible-stack` / `context-spec`.** The "harness failed the model" attribution is the same context-failure bridge that runs through the whole eval domain: before proposing a model swap, read the trace and check the context pipeline (retrieval, window, prompt).
- **Failure-mode genealogy feeds → `eval-driven-development` (challenge tier) and `ai-product-metrics` (evals as discovery).** The clustered root causes are your next-sprint fix-list, your new hard eval cases, and your unmet-need map — one artifact, three consumers.
- **Production traces feed → `feedback-flywheel`.** This is the loop closing: traces → labeled failures → eval dataset → next model/prompt → new traces. Observability is where the flywheel gets its fuel.
- **What the agent is allowed to do (and the kill-switch you trip on a critical alert) → `agent-risk` / `tool-architecture` / `safety-by-design`.** A critical-tier alert is only useful if you can *act* on it fast; the rollback/kill-switch design lives in those skills.

The spine: **observability turns silent, statistical degradation into a signal you can attribute, alert on, and feed back — it is the sensor layer the entire eval loop runs on.**

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

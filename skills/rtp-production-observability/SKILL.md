---
name: rtp-production-observability
version: v1.2.1_latest
description: 'Detect, investigate, and respond to AI degradation in production. Connect system health, task quality, user outcomes, and cost to traces, versioned configurations, and an accountable response. Design alerts without mistaking a proxy, a noisy score, or a missing span for proof of failure. Distinguish model, prompt, retrieval, memory, tool, and infrastructure problems; reconcile claimed actions with verified effects; and turn recurring failures into evaluation cases and discovery evidence. Examine human review and gaps between organizational reports and lived experience, with limits on proposed instruments. Use when shipping, debugging "it worked yesterday", designing alerts, or checking whether monitoring would detect an important failure. Pairs with eval-framework, confidence-tuner, invisible-stack, feedback-flywheel, and observability-stack. Triggers include "monitoring AI", "model drift", "quality regression", "traces", and "why did the agent fail".'
imports:
  - stress-test
  - eval-framework
  - feedback-flywheel
---

# Production Observability

Make important failures visible early enough for someone to act. Observe system health, task quality, and user outcomes together, then connect each alert to an owner and a recovery path. A responsive service can still produce wrong answers; a high quality score can still hide slow, expensive, or unauthorized behavior.

## Start with the harm and response window

Identify the customer, task, deployment, consequential failure, and decision monitoring should support. Use known context rather than repeating questions. Choose an inline audit or fuller monitoring design to fit the request; the shared Universal Skill Protocol lives at the AI-PM library root, or the plugin root in the packaged library.

A quick pass follows one recent failure from detection to diagnosis and recovery. A full pass covers the six process steps, relevant human/organizational checks, and readiness review. Choose detection and recovery targets from exposure, severity, traffic, label availability, and operating capacity. Weekly review can suit a slow business outcome; it is insufficient for an active, serious incident. Real-time telemetry is useful only if the signal and response work.

Before expanding collection, establish allowed data, access, destinations, retention, and authorization. Use `observability-stack` for platform and instrumentation choices. Detailed traces can contain customer data, secrets, or sensitive business context; emergency debugging still needs bounded, appropriate collection.

## What observability adds

Use three complementary views:

1. **Events, traces, and outcomes.** Request records show an interaction; traces connect instrumented operations; external outcomes show whether the intended task succeeded. A trace supports diagnosis but is not a complete account of internal reasoning or proof of causality.
2. **Quality alongside reliability and cost.** Monitor task correctness, relevant safety constraints, latency, availability, and cost together. PM, engineering, evaluation, and operations share ownership; quality is not useful if nobody can respond, and latency is also a product concern.
3. **Attribution before repair.** A model, context pipeline, instruction, tool, evaluator, or changed workload can explain degradation. Test plausible causes rather than assuming that most failures belong to one component.

Production evidence feeds the learning loop: traces and user reports → investigated failures → evaluation cases → changes → production checks. It also reveals unmet needs and reviewer workload. Logging alone does not close that loop.

An illustrative failure: after a prompt change, unsupported answers increase slightly, while latency stays flat. Support complaints rise later. Without versioned quality evidence the team cannot easily connect the events. The example's original “2%” was not a measured case and did not specify percentage points versus relative change. Define both the metric and comparison before acting on such a number.

## The six-step process

### 1. Define the events and evidence to retain

Log strategically. Determine which fields support the actual monitoring or audit need and which can be omitted, aggregated, pseudonymized, or retained briefly.

| Level | Useful evidence |
|---|---|
| Request/task | Timestamp, correlation ID, permitted segment/task labels, input/output tokens and units, estimated or billed cost, time to first useful output and completion, model/prompt/configuration version, outcome status. |
| Trace/span | Model request, retrieval, tool invocation, guardrail decision, retry, handoff, error, and external result. Preserve parent/link relationships and distinguish attempts from completed effects. |
| Batch/window | Latency distribution, availability/errors, cost per output and successful outcome, task-quality estimates, acceptance/regeneration/correction behavior, traffic by relevant segment, region, and task. |
| Change/incident | Deployment and routing changes, evaluator/rubric version, affected window and cohort, detection time, evidence, response, and recovery result. |

For model routing, record the actual served provider/model/version when exposed, including fallback and retries. Distinguish it from the requested alias and record unknowns honestly. A successful failover may change capabilities, price, or the authorized data path.

Separate measured correctness from proxies. Acceptance, correction, regeneration, confidence language, and user satisfaction are informative but are not interchangeable with accuracy. A “hallucination rate” needs a defined unit, adjudication rule, denominator, and treatment of missing labels; it is not automatically a false-positive rate. Label model-estimated costs as estimates until reconciled with billing.

### 2. Build views that support a decision

Provide four views: system health, task quality, usage, and cost. Enable useful splits by model/prompt/configuration version, task or customer segment, tenant where permitted, and time/region when relevant. Control cardinality and access rather than indiscriminately indexing personal identifiers.

Display sample size, sampling method, time window, data freshness, missingness, and evaluator version beside quality metrics. Show both overall results and important slices; average performance can hide a rare severe failure, while small slices can fluctuate sharply. Guard against traffic-mix shifts masquerading as model changes.

Connect evaluations to their trace/span or response ID. Scores may be span attributes, linked evaluation events, annotations, or records in an evaluation store. Asynchronous scores often arrive after a span closes. The essential property is a reliable join with the score definition and version, not a mandate to put every score inside a span.

OpenTelemetry graduated within CNCF in May 2026. That project milestone does not make every GenAI convention stable: the GenAI event documentation checked for this revision still marks its conventions as in development. Verify the supported schema and language implementation. See [monitoring examples and sources](references/monitoring-examples-and-evidence.md).

### 3. Define alerts and the response they trigger

For each alert, specify the metric and denominator, baseline, important effect size, evaluation window, data/label delay, relevant slice, severity, owner, and action. Distinguish an absolute threshold, a relative change, and a percentage-point change. Use uncertainty and minimum evidence where appropriate; one confirmed critical violation may justify action without waiting for a large sample.

Possible alerts include latency or token spikes, rising cost per successful outcome, availability loss, validated quality drift, excessive blocking, repeated tool failures, and sustained traffic changes. Treat traffic declines and unusual geography as questions to investigate, not proof of abandonment or abuse. Cost can rise because of price, task mix, more valuable work, retries, or bad configuration.

| Tier | Meaning | Response |
|---|---|---|
| Critical | A serious active safety, permission, availability, quality, or spending incident. | Notify the accountable responder promptly; contain exposure using the agreed mechanism. |
| Warning | A meaningful deterioration that permits investigation before immediate containment. | Assign a bounded response window, such as same-day investigation when suitable. |
| Informational | A trend, small change, or planning signal without urgent impact. | Review on a suitable cadence and promote if evidence or consequences change. |

Quality incidents can be critical; cost incidents can also be critical. The category alone does not set urgency. Tune precision, recall, detection time, and reset behavior together. Evaluate the burden of false alarms and the cost of missed incidents. “Fewer than 10% false positives” is not a universal release threshold, and false alarms among alerts are not the same denominator as a classifier's false-positive rate.

Version alerts and test routing. Use SLO/error-budget methods where the metric supports them. The historical numerical examples are retained in the reference as illustrative starting points, not product-independent targets.

### 4. Monitor agents and the whole workflow

In a planner/generator/evaluator harness, inspect component performance and end-to-end results:

- **Planner:** specification completeness and first-review outcomes. A falling pass rate may reflect the planner, the evaluator, harder tasks, or changed criteria.
- **Generator:** attempts, useful progress, completed requirements, cost, and outcome. More iterations can signal degradation or more thorough work; compare similar tasks.
- **Evaluator:** missed defects and incorrect rejections against trustworthy checks or adjudicated samples. Deterministic checks cover only their defined properties. Use `confidence-tuner` for calibration and threshold interpretation.
- **Handoffs:** delay, missing state, lost constraints, duplicate work, and unresolved tool results. A delay relative to baseline should be interpreted with workload and service commitments.
- **Context:** tokens, retained constraints, retrieval relevance, compaction/reset events, and quality over task duration. Token occupancy alone cannot locate a universal “pre-rot” threshold.
- **Work contract:** required criteria satisfied, justified exceptions, iteration/cost bounds, stop conditions, and evidence supporting completion. A status statement is not a completed task.

Anthropic describes context anxiety in some tested models: premature wrapping up near a perceived context limit. Its account also describes model-dependent improvements. Test the behavior in the actual model/harness; the original 50–60% window threshold is not a general finding. Compare context selection, retrieval, state persistence, model capability, and task difficulty before prescribing a reset or model swap.

Use verified critical failures to stop or contain a workflow when necessary. A noisy planner-score decline does not automatically require regenerating the entire specification. Preserve completed work and the evidence needed for recovery.

### 5. Categorize failures to choose a useful response

| Category | Examples | Response |
|---|---|---|
| Potentially transient | Rate limit, temporary provider outage, network interruption, timeout. | Use bounded backoff/retries when safe. A timeout after a write may leave its outcome unknown; reconcile before repeating the action. |
| Input or interaction problem | Malformed input, unsupported parameter, failed validation, unclear request. | Give actionable feedback and investigate recurrence. These may reveal product, accessibility, integration, or documentation defects; do not simply blame the user and ignore them. |
| System or policy failure | Wrong answer, invalid format, retrieval miss, lost state, tool error, authorization breach, infrastructure failure, spending overrun. | Contain according to severity, attribute the cause, and route to an owner. Several categories can contribute to the same incident. |

For trace debugging, retain the **logic versus memory** distinction. A logic failure follows an unsuitable procedure, tool choice, or inference; a memory/state failure omits or loses required information. Both can involve model and harness interactions, and neither is proven solely by a surface symptom.

The original example of twelve retrieved documents occupying 47,000 tokens in a 64,000-token window is illustrative. It raises a retrieval/context hypothesis; it does not prove that the relevant fact was “drowned” or absolve the model. Compare controlled variants and actual retrieval usefulness. Read permitted slices and trace details to identify candidate causes, then test them. A correlation with a deployment is a lead, not a complete causal explanation.

**Reconcile claimed actions with effects.** If an agent says it booked a meeting, verify the operation and resulting booking through an authoritative receipt or state check. A recorded API call may fail; provider acceptance may precede completion; an absent span may reflect sampling, broken instrumentation, or an asynchronous path. Use states such as requested, attempted, pending, confirmed, failed, and unknown. The historical label “agent gaslighting” describes a misleading completion claim here, not an inference about intent. Text review, state checks, receipts, and traces can all expose the mismatch.

### 6. Account for the cost of observing

Track storage, ingestion, queries, evaluator calls, instrumentation overhead, investigation time, and alert burden. Choose sampling, aggregation, retention, and indexing to preserve useful diagnosis without collecting everything by default.

Sampling 10,000 of one million requests is a 1% example, not a sufficient design for every service. Rare failures may need targeted capture; unbiased overall estimates need known inclusion rules and suitable weighting. Error-enriched samples should not be presented as production incidence. Protect required audit records from inappropriate sampling or deletion, and check both data minimization and retention duties.

Monitor the monitoring: exporter errors, dropped spans, missing labels, broken joins, late ingestion, evaluator failures, and stale dashboards. “No failures observed” is ambiguous when the sensor is not working.

## Human review and organizational reporting

### Check whether review is contributing

Gu, Li, and Zhu's theoretical working paper models how reviewers adjust effort as AI becomes more reliable, and how small capability changes can alter the preferred coordination structure. It is not a measured law that every reviewer disengages once a score crosses a bar. Workload, incentives, consequences, and review effectiveness matter.

A useful local hypothesis is that good aggregate output can coexist with weak oversight of exceptions. Output scores alone may not identify the human contribution, particularly near a ceiling. They can still reveal meaningful differences on other outcomes, harder cases, or more discriminating criteria. Do not assume there are only two valid measurement methods.

Possible checks include adjudicated audits, review interaction evidence, representative exception drills, and a **seeded-error catch-rate test**. The last is a proposed instrument in this library: in a controlled, separately managed exercise, present known flawed cases and measure which defects are caught, with matched difficulty and a clear denominator. Include acceptable cases to measure unwarranted rejection where useful.

Do not inject known bad material into live clinical, legal, or safety-critical work, or divert attention/capacity needed for real cases. Prevent any test action from reaching real users or systems; agree on the exercise and data handling. Pilot the instrument before treating it as a release gate or employee-performance measure.

A lower catch rate indicates worse performance on those test cases, not uniquely lower effort. Case difficulty, interface changes, fatigue, incentives, and training can also explain it. Review logs can help, but time spent and click counts alone do not establish sound judgment.

### Compare reports with work at the source

The **reporting-to-reality gap**, also called the polish paradox in the original, is a practitioner hypothesis: polished reports can diverge from employees' experience. Three candidate mechanisms are information compression across levels, incentives shaping what is reported, and selective retention of voices over time.

AI can amplify or reduce these distortions. Better writing and accurate reporting are compatible. Neither a polished report nor a long management chain proves distortion, and a small organization can also misreport.

For a consequential recurring report, trace selected claims to source records, compare omitted concerns, and gather candid observations from people doing the work. Protect appropriate confidentiality and avoid turning this into surveillance of individuals. System traces may corroborate some claims but cannot describe all lived experience. Link this work to `alignment-check`, `judgment-guard`, and relevant discovery skills rather than claiming that no skill can address it.

## Turn recurring failures into a useful fix list

**Failure-mode genealogy** means linking different symptoms to shared contributing causes. Group failing traces by a provisional mechanism, retain counterexamples, and validate the cluster. A single trace may already expose a cause; aggregation shows its reach and recurrence.

The historical “80% of failures from about three causes” is a practitioner heuristic, not an expected distribution. Measure the actual concentration. Prioritize by severity, frequency, affected users, recovery cost, confidence in the cause, and feasibility—not volume alone. One rare permission breach can outrank a common minor formatting issue.

Each validated cluster can produce an architectural repair, a challenge or regression case for `eval-driven-development`, and a needs hypothesis for `ai-product-metrics` or `feedback-flywheel`. Preserve successes and population denominators separately. A cluster of errors is evidence to investigate an unmet need, not proof of market demand.

## Readiness and diagnostic review

Check the relevant parts rather than forcing every system into the same fourteen-item checklist:

1. Required request/task evidence and version identifiers exist, with appropriate data controls.
2. System, quality, usage, and cost views expose material failures and relevant slices.
3. Alert thresholds, owners, channels, and response windows are defined and exercised.
4. Cost per output and successful outcome have clear units, scope, and estimate/billing status.
5. Failure categories lead to useful responses, including safe retries and input feedback.
6. Changes can be linked to affected evidence, with causal claims kept distinct from correlation.
7. Containment and recovery have been tested at the required level; automation is used where justified.
8. Retention, sampling, access, and deletion fit the purpose and applicable obligations.
9. Traces and evaluation records can be joined reliably, with known coverage and freshness.
10. Quality and guardrail performance are monitored alongside reliability and cost.
11. Investigations consider model, logic, state, retrieval, tools, and infrastructure.
12. Claimed external actions can be reconciled with authoritative outcomes.
13. Where human review is relied on, its effectiveness is assessed. Seeded testing is optional and proposed, not a universal prerequisite.
14. Important AI-assisted organizational reports have an appropriate source check; the polish-paradox account remains a hypothesis.

Useful desk questions: Can we reconstruct the last wrong output? Which model and prompt served it? What is known versus estimated about its cost? Could a severe failure remain invisible because of sampling or missing labels? Who responds to a quality or latency alert? What indicates that human review contributed? Which report claims have been checked against source work?

Set release gates for the product's actual risk. A consequential system may need a demonstrated baseline, quality visibility, enforceable limits, and tested containment before exposure. Do not impose universal five-minute detection, thirty-minute recovery, automatic rollback, or a fixed false-alarm percentage on every deployment.

## Respond when monitoring misses a failure

Contain the active harm, preserve the necessary evidence, establish the affected time and cohort, and inspect recent changes and alternative causes. Use bounded additional logging if justified. Repair the detector, sampling, labels, routing, or response that failed, then exercise the repair.

Stricter thresholds are one option; better signals or less noisy thresholds may work better. Rollback can restore a prior configuration but does not undo sent messages, payments, data exposure, or other external effects. Reconcile and remediate those separately. Recovery is complete when the relevant service and user outcomes recover, not merely when a deployment command succeeds.

## Output and connections

```markdown
# Production Observability: [Product]
Decision and important failure: [customer, task, consequences]
Monitoring scope: [events, versions, quality evidence, data boundary]
Baseline and slices: [metric definitions, counts, windows, uncertainty]
Alerts: [condition → severity → owner → response window → action]
Trace/outcome coverage: [joins, sampling, freshness, unknowns]
Attribution: [candidate cause, supporting evidence, alternative, next test]
Containment/recovery: [tested mechanism, limits, external remediation]
Human review/reporting checks: [relevant method and evidence limits]
Learning loop: [failure cluster → repair/eval/needs hypothesis → owner]
Operating cost and trade-off: [accepted collection/response cost]
Open gaps and next action: [owner, scope, success condition]
```

Use `eval-framework` for valid quality measures and `confidence-tuner` for judge calibration; neither turns a score into unquestionable truth. Route context/state hypotheses to `invisible-stack` and `context-spec`, and test model changes when evidence supports them. `agent-risk`, `tool-architecture`, and `safety-by-design` define action limits and containment. `feedback-flywheel`, `eval-driven-development`, and `ai-product-metrics` turn investigated evidence into improvements.

Close with the recommendation, material trade-off, main uncertainty, and next action. A diagram is optional when it clarifies the signal-to-response path or the learning loop.

---
name: ai-product-metrics
version: v1.10.2_latest
description: 'Choose and define metrics that show whether an AI product delivers useful work, at what cost, and with which risks. Use for dashboards, North Star and AARRR design, the Surfaced/Invoked/Completed/Accepted/Retained funnel, release monitoring, or executive reporting. Covers acceptance, corrections, regeneration, conversational burden, task success, calibration, pass@k/pass^k, cost per successful outcome, cohorts, and companion measures for misleading improvements. Distinguish usage, quality, oversight, and realized value; acceptance and fewer escalations are signals, not proof. Connect each important measure to a decision, owner, denominator, time window, evidence limits, and response. Use correction clusters for discovery after checking their causes, and translate findings into business implications without inventing causal effects. Pairs with eval-framework, feedback-flywheel, confidence-tuner, cost-model, token-economics, stakeholder-communications, and fit-signal.'
imports:
  - eval-framework
  - feedback-flywheel
  - confidence-tuner
---

# AI Product Metrics

Build a measurement system that helps the team understand user outcomes, quality, effort, risk, and economics—and make a useful decision when they change. Start with the customer, problem, workflow, and decision owner. Use context already available; ask only for missing information that materially affects the work.

The central distinction is **activity versus outcome**. A generated answer is not necessarily useful; an accepted answer is not necessarily correct; a correctly completed task is not necessarily valuable enough to sustain the product. Keep all three visible where they matter.

Produce a proportionate metric dictionary and dashboard, with baselines, relevant segments, thresholds or review conditions, owners, and the next decisions. Use the [dashboard template](references/dashboard-template.md) and [evidence and interpretation notes](references/evidence-and-interpretation-notes.md) for detail.

## 1. Start from the decisions and the value chain

Name what the measurement informs: improve a workflow, assess a release, allocate review capacity, understand adoption, investigate unmet demand, or evaluate an investment. Business and product owners define the intended outcome with users; analytics and domain experts help establish a credible measurement. These responsibilities can overlap.

Self-service questions can support exploration. Decision-oriented analytics clarifies which comparison and evidence matter. Neither access nor a new dashboard alone guarantees a better decision.

Use three reporting lenses when helpful:

- **Enablement:** data freshness, relevant coverage, usable integrations, and evaluated capability.
- **Value creation:** useful work completed and the user experience of doing it. Usage is supporting evidence, not the whole outcome.
- **Value realization:** benefits the organization or customer actually obtains—revenue, realized savings, reduced loss, improved service, or another justified outcome.

This ordering suggests hypotheses about how value is produced. It does not prove a causal chain from a higher eval score to revenue. Keep unknown links explicit, especially for long investments. An improving asset-quality measure can explain progress while the outcome remains uncertain; it is not a permanent exemption from assessing value.

Benchmark, product, and trajectory metrics answer different questions. Benchmarks inform capability on the tested tasks; product measures reflect the deployed experience; trajectory measures inspect how the result was reached. Use the relevant layers together. They are not rigid maturity eras, and not every simple feature needs extensive trajectory instrumentation.

## 2. Define the metric before interpreting it

For each important measure, record:

1. **Decision and owner:** what could change, and who acts.
2. **Unit and population:** user, session, task, output, claim, action, or account; who is eligible.
3. **Definition:** numerator, denominator, event rules, observation window, exclusions, and treatment of partial or unknown outcomes.
4. **Evidence:** logs, user actions, surveys, adjudicated samples, or a validated judge; source and version.
5. **Comparison:** baseline, cohort, task mix, deployment configuration, and uncertainty.
6. **Companions and response:** alternative explanations, relevant guardrails, threshold meaning, and next investigation.

Label **percentage points** and **relative change** correctly. A rate moving from 20% to 23% rises 3 percentage points and 15% relative. An alert saying “up 3%” is incomplete until it specifies which.

Distinguish missing data, unavailable measurement, zero events, and an undefined ratio. Protect sensitive content and avoid collecting employee or customer behavior beyond a justified purpose. A dashboard for product improvement should not silently become an unvalidated individual-performance score.

## 3. Select useful indicators and their companions

Leading and lagging describe a relationship over a chosen timeframe. Acceptance may lead retention in one product and fail to predict it in another. DAU, retention, revenue, accuracy, and satisfaction remain useful when their limits and purpose are understood.

| Measure | Operational definition to specify | What it cannot establish alone |
|---|---|---|
| **Acceptance rate** | Accepted outputs divided by eligible outputs shown; distinguish as-is, edited, and inferred acceptance. | Correctness, useful review, or durable user value. Copying or saving may be provisional. |
| **Correction rate and edit burden** | Eligible outputs changed before or after use; classify factual repair, preference, formatting, and collaboration. | All edits are errors or all unedited work is correct. Edit distance misses meaning. |
| **Regeneration rate** | Outputs/tasks rerun under a defined rule and window; separate retries from intentional variants. | All regeneration is dissatisfaction or all repeated calls are waste. |
| **Conversational burden** | User effort to reach a useful outcome: turns, time, rephrases, corrections, and avoidable clarification. | More turns are always worse. Exploration, learning, and complex work may benefit from dialogue. |
| **Abandonment** | Eligible started tasks not completed through the product within the defined window. | The user failed; work may continue elsewhere, finish asynchronously, or no longer be needed. |
| **Task success** | Completion against explicit user-relevant criteria, with partial, pending, failed, and unknown states. | Every successful task has the same value or consequence. |
| **Cost per successful outcome** | Total in-scope cost over the period divided by successful outcomes in the matched population and period. | Profitability without revenue, fixed costs, risk, and accounting context. |
| **Escalation and intervention** | Cases routed to a person, cases with intervention, or total interventions—each separately defined. | Fewer escalations mean better handling or effective oversight. |
| **Latency** | Response onset, time to useful result, and completion; relevant p50/p95/p99 under realistic conditions. | User effort or complete workflow speed. |

No universal 70% acceptance, <10% regeneration, <5% abandonment, or fifteen-turn failure threshold applies. Choose measures the workflow can meaningfully observe; a non-interactive agent may need outcome and incident evidence rather than user acceptance events.

### Measure errors and uncertainty precisely

Define unsupported claims, factual errors, omitted information, policy violations, and unsafe actions separately where they have different implications. A **false-positive rate** is `FP / (FP + TN)` for a defined binary classification task. It is not a synonym for hallucination rate or “confidently wrong.” Define the positive class before reporting precision, recall, sensitivity, or specificity.

Calibration asks whether probability estimates match observed frequencies under the evaluation conditions. Correlation between confidence and accuracy is insufficient. Evaluate the score or judge on representative and important difficult cases, including subgroup performance and severe errors. Overall agreement can hide failure on a rare class. Route this work to `confidence-tuner` and `eval-framework`.

For acceptance quality, preserve three separate criteria: **minimally sufficient**, **comparable to typical human work**, and **better than typical human work**. State whether editing is allowed and how the reference standard was established. None alone proves that an entire job can be replaced; integration, input preparation, supervision, coverage, and consequences remain relevant.

## 4. Use North Star, AARRR, and the AI funnel together when useful

Choose a North Star that represents a meaningful user outcome, can be measured and influenced, and is understandable. Test its relationship to the organization's longer-term goal; not every organization optimizes revenue, and not every product benefits from one composite metric.

For a contract-review product, “useful reviews completed with the required error checks” may be more informative than raw queries. “Weekly users accepting three reviews without edits” is one possible proxy, not a best or ungameable metric. It can reward unnecessary reviews, weak checking, or simple tasks.

### The five-stage AI funnel

| Stage | Definition | Interpretation to check |
|---|---|---|
| **Surfaced** | An eligible user encountered the feature or entry point. | A provisioned seat does not prove exposure; exposure does not prove relevance. |
| **Invoked** | The feature received an eligible request or started an authorized run. | Invocation can be exploratory, required, accidental, or useful. |
| **Completed** | Processing reached a defined terminal state. Report successful delivery, appropriate refusal, error, and cancellation separately. | Finishing generation is not completing the user's job; an appropriate refusal can be correct behavior. |
| **Accepted** | The user used or kept the result under a stated event rule. | Acceptance is an observed behavior, not a truth label. |
| **Retained** | The relevant user or account returns to useful use within a task-appropriate interval. | Repeat use can reflect value, habit, obligation, or unresolved work. |

A seven-day retention window is an example. Infrequent tasks may need a longer or opportunity-based window; recurring autonomous jobs may need a different event model. Use per-stage conversion with matching eligible populations and observation periods. Do not force every interaction into a linear path when users skip, repeat, or branch stages.

Track **provisioned but unused** separately when licenses matter: eligible provisioned users, time to first use, and the share not yet invoking by a defined horizon. Handle censoring, revocation, departure, and access changes. Removing a license need not erase historical measurement. Investigate workload, incentives, benefit destination, access, understanding, and UX rather than assuming one cause.

### AARRR adaptations

- **Acquisition:** qualified discovery and trial by channel. Demonstrations, transparency, and credible references can help; no general 3–5× channel conversion multiplier applies.
- **Activation:** the first meaningful value event, which may require more than one prompt and may include edits. Help users get there without manipulating the metric.
- **Retention:** useful repeat engagement at the product's natural cadence. Four weeks is not a universal trust-stabilization period, and week-2/3 failures are not always the main cause of churn.
- **Revenue:** recognized or recurring revenue, pricing, expansion, and the associated cost/margin view. Revenue minus AI cost is not automatically “net revenue”; name it as a contribution measure with the included costs.
- **Referral:** intentional referrals or sharing with appropriate consent and data handling. Sharing a result is not necessarily endorsement or acquisition. Do not add branding or observe external sharing contrary to user expectations.

AARRR and the AI funnel overlap but are not identical: activation requires useful experience beyond mere generation, revenue is a separate event, and referral can occur at different stages. Use both only where they clarify the decision.

## 5. Calculate reliability and economics without overstating them

### pass@k and pass^k

**pass@k** asks whether at least one of `k` attempts succeeds. **pass^k** asks whether all `k` trials succeed. Report the task set, attempt policy, configuration, number of trials, uncertainty, and costs. At `k=1`, both represent the single-trial success rate.

For a homogeneous, independent repeated-trial example with success probability `p`:

```text
pass@k = 1 − (1 − p)^k
pass^k = p^k
p = 0.8, k = 5:
pass@5 = 0.99968
pass^5 = 0.32768
```

These are assumptions, not formulas to apply blindly to a heterogeneous task set or dependent retries. Repeated trials of a task are not automatically the steps in one workflow. The example does **not** establish a 67% multi-step-task failure rate. Measure the actual trajectory, recovery, and joint outcome.

A high pass@k with a lower pass^k can reveal inconsistency under the tested policy; it does not identify the cause. Low scores may reflect model limits, task design, context, tools, environment, or the grader. High scores alone do not establish production readiness or an SLA. Use pass@1, repeated reliability, useful retry behavior, and operational outcomes as the task requires.

### Cost per outcome and human review

Include costs of failed attempts, retries, partial work, and relevant overhead in the numerator. Match the denominator to the same workload; account for delayed outcomes. Zero successful outcomes makes cost per success undefined or unbounded for interpretation—report the cost and zero count explicitly rather than displaying zero cost.

Human review cost needs time:

```text
review cost per period
= Σ(reviewed cases × average review minutes per case / 60 × loaded hourly rate)
+ other in-scope review costs
```

Use actual summed time when available and separate reviewer groups. Multiplying an hourly rate by traces and frequency without a time-per-trace term has incorrect units. Flat or rising total review cost during growth does not prove an untrustworthy judge; compare workload, complexity, coverage, cost per outcome, and errors. Automated evaluation can add value through broader or faster checks even if it does not cut total human hours.

Outcome-based billing is a commercial definition; billed resolution is not independently verified correctness. Seats, usage, hybrids, and outcome pricing can each work. Use `token-economics` for contract definitions, contribution margins, paired customer revenue/cost, and deliberate subsidy. Do not label cost per outcome a universal minimum selling price.

### ARR per FTE and other ratios

ARR per FTE can inform a scoped efficiency comparison. State ARR definition, period, average or point-in-time staffing, contractor treatment, vendor costs, inherited assets, investment phase, and business model. If adding contractor equivalents, label the adjusted measure so it remains comparable.

Revenue already contains a price term: broadly, `revenue = price × volume`. ARR per FTE is not literally price-blind, though it cannot by itself explain price, volume, staffing, outsourcing, or margin changes. Tokens per task has a different denominator and does not necessarily rise with reduced headcount. Pair ratios with their components and realized value; do not treat high ARR/FTE as proof of AI maturity or low ARR/FTE as a cause of failure.

Means and medians answer different questions. A gap can signal skew or heterogeneity, but does not prove a few outliers explain everything. Use the distribution and the actual prediction/result population. A forecast is not realized productivity.

## 6. Check apparent improvements for alternative causes

Use companion measures, sometimes called **anti-metrics**, to catch gaming and misleading movement. Goodhart-style effects are a risk to manage, not a claim that every targeted metric becomes useless.

| Apparent improvement | Plausible alternative | Useful companion evidence |
|---|---|---|
| More sessions or longer engagement. | Repeated failure, unnecessary work, or changing task complexity. | Completed useful tasks, burden, repeat intent, and user explanation. |
| More acceptance with few edits. | Better work **or** weak review. | Sampled correctness, error detection, evidence inspected, and review authority. |
| More adoption with more support. | Confusion, growth in exposure, a broader audience, or normal onboarding. | Tickets per relevant workload, severity, cohort, and root cause. |
| Lower costs. | Efficiency improvement or loss of quality/coverage. | Matched outcomes, severe errors, workload mix, and user impact. |
| Fewer escalations or faster approvals. | Better handling, missed exceptions, staffing changes, or weaker checks. | Review of automatically resolved cases and consequential decisions, including false negatives. |
| Stable satisfaction. | Good experience or an instrument insensitive to a specific problem. | Direct user inquiry and task-relevant behavioral evidence. |

An escalation rate is cases escalated divided by eligible cases; **handoff count** is the number of transfers and may include several per case. Keep them separate. Lower approval time with a higher approval rate does not by itself prove that a gate dissolved.

Satisfaction distributions may have nonlinear relationships with retention or advocacy. Inspect the full distribution, top-box share, response bias, and predictive relationship where relevant. Top-box reporting is not always superior to an average, and NPS is **percentage promoters minus percentage detractors**, not an “average of averages.”

Behavioral proxies such as rephrases, time spent, or after-hours activity can help but do not automatically outrank self-report or establish burnout, harm, or poor judgment. Consider context, privacy, and measurement validity. Do not infer an individual's condition from telemetry alone.

## 7. Detect measurement limits and improve the instrument

An unchanged score may mean stability, insufficient power, the wrong task mix, a weak grader, a ceiling, or stale coverage. Complaints may indicate a missing outcome or a distinct segment. Diagnose before replacing the dataset.

Keep a stable regression set for comparability and add versioned capability or production-derived cases where needed. Preserve held-out checks, rights and privacy, historical comparability, and representative task coverage. Do not replace 20–30% monthly by rule or make a test harder solely to force a red score. A reliable regression suite should often stay green.

### When human contribution becomes hard to distinguish

If a system already clears a coarse quality bar, final-output scores may not distinguish human contributions. That can be task-specific and is not proof that expertise disappeared. Also inspect scale limits, task mix, scorer resolution, and selection.

Possible responses include:

- Examine relevant interaction and process evidence, while recognizing missing or incentive-shaped logs.
- Use clearly controlled known-error cases or independent audits to assess detection. Seeded cases are not the only instrument and must not expose real users to harm or covertly determine employment decisions.
- Assess a different task, retention, or transfer outcome that matches the capability of interest.
- Examine whether the tool or retrieval configuration masks or changes the capability being assessed, then validate any revised assessment against an independent outcome.

There are more than three possible exits. Changing the rubric or tool can also change what “good” means; do not use success on the new instrument as its own validation. Recognize evidence that a task should remain manual or that a deployment creates rework. A no-blame discussion may reveal hidden costs, but needs usable incentives and follow-through.

Formal models of reduced review effort under strong AI performance identify a possible mechanism under assumptions. They do not prove every reviewer rationally disengages, nor make unknown oversight quality measurable from stop rate alone.

## 8. Use cohorts, alerts, and release checks proportionately

Slice by relevant user segment, task type/complexity, model, prompt, harness, retrieval, locale, and release version. Check sample sizes, selection, and privacy before interpreting small groups. Preserve a standard workload view alongside current-mix results so composition changes do not masquerade as improvements.

Define alerts using consequence, baseline variation, exposure, change size, and response capacity. Record whether the threshold is absolute, relative, or in percentage points, and whether it signals investigation, restricted rollout, or a release block. The original 3% acceptance, 20% regeneration, 10% cost, 2% hallucination, and 20% latency thresholds are examples only.

No release must preserve every metric without trade-off. Protect non-negotiable requirements and evaluate deliberate changes with evidence. A cost increase may buy worthwhile quality or coverage; an appropriate refusal may reduce raw completion while improving the product.

Start with the smallest credible measurement for the action's consequences. Do not wait until month four for essential regression tests or alerts. Real-time monitoring is useful where response time matters; periodic review may be sufficient elsewhere.

When a signal changes, verify the measurement, scope the affected work, inspect traces, compare changes, test plausible causes, act, and check recovery. A temporal association with a release is a lead, not causal proof. Route by evidence rather than assuming most problems are context or model failures.

## 9. Use failure clusters for discovery

Group corrections, regeneration, abandonment, and review cases by intent, task, and relevant user segment. Consider severity, frequency, affected population, confidence, and the cost of doing nothing.

A cluster is a **candidate problem**, not automatically a feature or merely a defect. Read representative traces and speak to users where needed. Edits can express taste, collaboration, or an error; a review queue can reflect a deliberate policy rather than missing capability. A 15% share of failures is not a roadmap promotion rule.

Once the cause is clearer, route bug repair to the relevant owner or unmet needs to `feedback-flywheel`, `jtbd-analysis`, and `opportunity-solution-tree`. Preserve the path from signal to interpretation to decision so the discovery can be revisited.

Track **new task scope** separately from success: more cross-domain or previously unattempted work signals demand, not demonstrated value. Evaluate the quality and consequence of the new tasks too. For agent-mediated buying, **share of algorithmic choice** can be useful if the eligible decision set and observation method are credible. API latency, feed completeness, awareness, and brand preference are inputs or related measures, not the selection outcome itself.

## 10. Translate findings into decisions without inventing causal links

Pair a technical metric with its plain-language implication, including the strength of evidence. An executive may act on a serious capability or risk gap without a fabricated dollar translation. Separate a measured relationship, a forecast, and a plausible mechanism.

| Audience | Decision-relevant translation |
|---|---|
| **CFO / budget owner** | Matched cost, revenue, margin or savings scenarios, investment needs, and uncertainty. |
| **GC / control owner** | Relevant requirement coverage, failures, evidence limits, and unresolved obligations. A 99.2% eval score is not 99.2% legal compliance. |
| **COO / operational owner** | Case volume, cycle time, review workload, quality, backlog, and response capacity. |
| **CHRO / people leader** | Task and role changes, workload, learning, support, and evidence about human capability. Automation share does not prove a staffing reduction. |

For example, a 4-point context-recall drop may warrant investigating support effects; it does not establish a 12% ticket increase without a measured or explicitly modeled mapping. A decline from 18% to 9% intervention is half the **rate**; case counts and hours depend on volume, review duration, and case mix.

Translate questions back into work too: margin concerns may require a cost study; control concerns may require different evaluation coverage. Build a customer-facing value view with the customer's champion where that improves a B2B buyer's decision. Co-creation can help relevance and credibility, but does not substitute for evidence.

## Deliver and check the dashboard

Use the [template](references/dashboard-template.md) as a menu, not a requirement to instrument every cell. Make the following legible:

- The intended value and decision, with the relevant outcome and business view.
- Defined events, populations, denominators, windows, and current measurement limits.
- Quality, effort, risk, cost, and useful behavioral companions.
- Cohort and release comparisons that remain meaningful across changes.
- Owners and response rules, open questions, and the next action.

Conclude with the recommendation, main trade-off, largest uncertainty or risk, and next step. Use the shared `UNIVERSAL-SKILL-PROTOCOL.md` proportionately: it lives at the AI PM collection root in the source library and the plugin root in distribution. A funnel, trend, or comparison can help; use `excalidraw-svg` when useful, without promising a visual makes the deliverable ten times better.

`eval-framework` defines and validates evaluations; `confidence-tuner` assesses scores and judges; `production-observability` supports trace diagnosis; `ai-ux-patterns` supports burden and interaction design; `invisible-stack` / `context-spec` address evidenced context failures; `cost-model` / `token-economics` support economics; and `stakeholder-communications` supports the final narrative.

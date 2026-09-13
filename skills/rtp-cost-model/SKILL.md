---
name: rtp-cost-model
version: v1.5.1_latest
description: 'Calculate the full cost of delivering a useful AI outcome, including model calls, retrieval, tools, storage, retries, human work, evaluation, and operations. Use for launch decisions, pricing inputs, vendor renewals, scaling plans, or affordability reviews. Define success and the accounting period; distinguish aggregate cost per success from task and account cost percentiles. Model current volume, growth, and downside scenarios, including usage, vendor units, prices, quality, and review capacity. Compare routing, caching, batch processing, and harness designs on cost at acceptable quality. Deliver a traceable cost model, sensitivities, spending controls, and pricing handoff. Prototypes and intentional loss leaders still need a proportionate budget. Pairs with token-economics for pricing, stress-test for scale, moat-finder for advantage, and ship-decision for release decisions. Triggers: unit economics, AI cost model, cost per outcome, can we afford this.'
imports: [stress-test, token-economics]
---

# Cost Model

Calculate what the complete workflow costs to deliver the outcome the user needs. Include unsuccessful attempts and the human work required to make outputs useful. Then determine which assumptions could change the decision at growth, renewal, or launch.

**Start with the outcome, cost boundary, and period.** “Cost per call,” “cost per successful outcome,” and “monthly cost per account” answer different questions. Keep all three where useful; do not substitute one for another or turn a percentile into an average bill.

## Choose the depth and gather the inputs

Use the full process for a pricing input, launch commitment, significant renewal, or unclear economics at scale. To review an existing model, start with the diagnostic questions. For a prototype, use ranges, a spending limit, and a learning objective. An intentional subsidy, compliance requirement, or strategic loss leader changes the decision criterion; it does not make cost irrelevant.

Reuse available context under the Universal Skill Protocol. Establish the user task, alternatives, action permissions, expected volume, quality requirements, and business objective before asking further questions. Use relevant `3_Research` material and Novel Insights to find assumptions worth checking; verify changing prices and product terms against current primary sources and the applicable contract. Distinguish first-hand evidence, estimates, and unverified claims.

Gather:

- **Usage:** tasks, calls, tokens, retries, tools, outcomes, and account-level usage over a stated period.
- **Architecture:** the actual execution branches, background jobs, evaluations, and human gates from `agent-harness` or `harness-operating-model`.
- **Rates:** model and platform, region/currency, input/output/cache/batch rates, included units, commitments, overages, effective dates, and contractual exceptions.
- **Quality and operations:** failure taxonomy, escalation outcomes, review time, support burden, service targets, and staffing capacity.

A seat purchased is not an active user. Separate plan types, enterprise versus smaller customers, included completions versus metered agent/chat work, and internal deployments versus customer use. For a pricing-history question, date the changes and identify the affected product and population. A vendor announcement, one complaint, and an invoice are different kinds of evidence.

## 1. Define the economics before building the spreadsheet

### Outcome and accounting definitions

Write the success criterion, who verifies it, when it becomes observable, and how pending, failed, reversed, or disputed outcomes are treated. A completed tool call, an accepted draft, and a resolved customer issue are distinct events. A billable event may also differ from a useful outcome.

For one matched cohort or period:

```text
Aggregate cost per successful outcome
  = all costs in the stated scope attributable to that cohort
    / verified successful outcomes from that cohort
```

Include failed and abandoned attempts in the numerator. Align delayed outcomes with their originating work or disclose the lag. With no observed successes, report “no successes observed; ratio undefined” and the spend; do not substitute zero. Report machine-only resolution separately from resolution achieved through human escalation when that distinction matters.

**Percentiles need an entity and a method.** P90 task cost is the 90th percentile of task costs, including unsuccessful tasks. P90 account-month cost is a different distribution. A distribution of account-month cost-per-success ratios requires explicit treatment of accounts with no successes and a stated allocation of shared costs. Report these alongside the aggregate ratio and mean. Do not sum component P90s or multiply one task’s P90 by every task to forecast the ordinary total bill. A high-cost stress scenario may use that assumption if clearly labeled.

### Benefit and alternative

Name the pathway: the same output with fewer inputs, more output with similar inputs, or a new offer/workflow. Compare it with a credible manual, deterministic, simpler AI, or existing-vendor alternative. Separate cash savings, released capacity, added revenue, and reduced error exposure. Time saved is not automatically payroll removed, and more output is not automatically demand or revenue.

Assess how competitors and suppliers could share or capture the gain. Widely available models may accelerate imitation, while differentiated data, execution, distribution, contracts, or switching costs can affect the result. Rented capability does not guarantee immediate margin erosion; ownership does not guarantee protection. Model the plausible erosion path rather than assume permanent margin or a fixed expiry date.

For a substantial investment, use four finance checks: explicit alternatives; attributable assets and capital needs; an appropriate, current finance-approved discount rate; and comparable scenarios. Match the rate to the cash flows being valued—for example, do not use an equity rate indiscriminately for all project cash flows. Do not copy a published market-average cost of equity as the company’s rate.

## 2. Map the full cost stack

| Cost area | Include | Driver to record |
|---|---|---|
| Model inference | Every billable generation, input, output, reasoning category, and cache operation | Per-call usage and actual rate |
| Retrieval | Document/query embedding, indexing, search, re-ranking, refresh | Corpus updates, storage, and query workload |
| Storage | Documents, vectors, caches, logs, backups, retention | Bytes or the vendor’s defined unit over time |
| Compute and orchestration | Hosting, state, queues, retries, fallback, tools, fan-out, network/egress | Complete execution path and concurrency |
| Human work | Preparation, context repair, review, correction, escalation, annotation, support | Time, role cost, frequency, and capacity |
| Evaluation and monitoring | Test generation, scored runs, human calibration, audits, drift detection | Coverage, repetitions, changes, and sampling |
| Setup and ongoing operations | Design, integration, rollout, maintenance, migration, commitments | One-time, recurring fixed, variable, and step costs |

Avoid double counting: a retry’s tokens belong in model usage; orchestration adds its own compute, not another copy of those tokens. Separate provider cost, customer effort, and broader social or risk costs. Customer review time belongs in the buyer-value case even when it is not seller cost of goods sold.

**Call multiplier:** measure calls per task and its distribution, including validators, branches, retries, and background work. A single agent can make many calls; a simple chatbot can also retry. There is no universal 10–20-call multiplier, 3–5× retrieval expansion, or 20–30% inference share.

**Fixed versus marginal:** show setup separately from each additional run and recurring maintenance. Allocating setup over a small actual volume is a real average cost, not a mathematical overstatement. Forecast amortization only over a defensible usage horizon. Compare alternative total costs:

```text
AI total = AI fixed cost + volume × AI variable cost
Alternative total = alternative fixed cost + volume × alternative variable cost
Break-even volume = (AI fixed − alternative fixed)
                    / (alternative variable − AI variable)
```

Use that break-even formula only when its denominator is positive and the linear assumptions hold over the relevant range. Include capacity steps, rework, and maintenance where they change it. A one-off task can still be worthwhile; it must justify its actual total cost.

### Count the work of managing AI

Measure prompt attempts, missing-context preparation, verification, correction, handoffs, and downstream rework against the same workflow baseline. Distinguish necessary oversight from avoidable friction. Do not remove valuable checks merely to improve a productivity metric.

The botsitting survey in the research library reports 11 hours automated and 6.4 hours spent managing AI. Their ratio is about 58%, but it is not a validated deduction from net savings or a statistical ceiling. Shared respondents do not guarantee canceling biases; the underlying definitions and overlap matter. Similarly, Vanguard’s task-versus-workflow comparison and vendor-versus-customer anecdotes do not establish universal half-or-third adjustments. Use them to ask for the correct scope and a defensible baseline. [Research limits](references/cost-evidence.md)

Price the actual review design: inspection after seeing an AI answer, an independent assessment followed by comparison, specialist review, or sampling. Compare error detection, effort, delay, and consequences. Independence can help in some settings; it is not the only effective review method. Review cheaper than a manual baseline is not itself evidence of unsafe design.

### Include physical capacity where it changes the decision

For self-hosting, colocation, or material infrastructure commitments, include hardware utilization, idle capacity, depreciation or rental, electricity, cooling, staffing, maintenance, and regional constraints. Managed API prices normally already include the supplier’s power costs; do not add them again as a direct expense.

Managed-service buyers can still examine available regions, workload timing, procurement terms, and efficiency where supported. They need not negotiate a power-purchase agreement to have a useful lever. Respect latency, residency, and quality constraints.

If energy is decision-relevant, record measured or estimated energy per completed workflow, its coverage, and uncertainty. Tokens per kWh are comparable only with consistent tokenization, model, workload, and quality assumptions. The IEA’s 2026 outlook projects data-centre electricity use rising from 485 TWh in 2025 to about 950 TWh in 2030; this is a forecast for all data centres, not an audited future outcome or a price forecast for this feature. [IEA outlook](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)

## 3. Calculate from traceable units

For every row, show quantity, unit, rate, period, source/date, formula, and estimate range. Reconcile the total against billing and operational records when available. Until then, label assumptions and set a review trigger based on the decision and volume—not a mandatory wait until 30 days after launch.

**Illustrative monthly document-search model.** These assumed rates are not vendor quotes. The 100,000 calls are the complete inference-call count for this example; additional calls would require an additional row or revised quantity.

| Component | Quantity and assumed rate | Monthly cost |
|---|---|---:|
| Query inference | 100,000 calls × $0.0218 | $2,180 |
| Query embedding | 100,000 × 100 tokens × $0.00001/token | $100 |
| Re-ranking | 100,000 calls × $0.001 | $100 |
| Vector storage | 1 million vectors × $300/million vector-months | $300 |
| Vector database hosting | Fixed monthly | $800 |
| Evaluation | 30 days × $150/day | $4,500 |
| Human QA | 500 reviews × $15 | $7,500 |
| Other operations | Defined monthly allocation | $6,000 |
| **Total** | Sum of the eight cost rows | **$21,480** |

Inference is about 10.1% and QA about 34.9% **in this example**. If this cohort produces 80,000 verified successes, the aggregate scoped cost is **$0.2685 per success**. Storage assumes one vector per document; chunking or replicas would change the quantity. Identify omitted costs before calling this an all-in estimate.

### Model retries and escalation as branches

Suppose each inference attempt costs $0.0218 and 15% of initial attempts fail:

- With immediate $5 human escalation after each failure, expected processing cost per initial task is `$0.0218 + 0.15 × $5 = $0.7718`. If every task is eventually resolved, that is also the processing cost per resolution under these assumptions.
- With one retry, and a **conditional** 15% failure rate on that retry, expected calls are `1 + 0.15 = 1.15`; 2.25% of tasks then need the $5 escalation. Expected processing cost is `$0.0218 × 1.15 + 0.0225 × $5 = $0.13757`.

Measure the conditional retry outcome; repeated errors may be correlated. Add other costs and divide by actual final successes if human escalation also fails. Never multiply dollar-denominated inference cost by a dollar-denominated escalation charge. The shorthand `cost / success rate` is useful only when its cost and cohort definitions match the workflow.

## 4. Model growth, price changes, and the usage tail

Use current volume, a plausible growth case—often 10×—and a downside case. Separate demand volume, task mix, corpus size, concurrency, vendor rates, and outcome quality. More users do not automatically produce longer prompts, lower cache hits, or more expensive routing. Scale can also improve utilization, discounts, and reuse.

| Variable | Current evidence | Growth/downside assumption to test |
|---|---|---|
| Active users and tasks | Usage by segment, including power users | Adoption, frequency, background work, and concentration |
| Calls and tokens per task | Trace distributions by task type | More complex work, bounded retries, changed context |
| Corpus and retrieval | Index size, updates, latency, query cost | Growth in data separately from growth in requests |
| Cache | Read/write token counts or response-cache hit rate | Reuse, personalization, traffic timing, invalidation |
| Routing | Model mix and outcome quality | Different task mix, model changes, fallback demand |
| Human work | Review minutes and escalation outcomes | Staffing, queues, missed errors, capacity steps |
| Evaluation and operations | Fixed and usage-sensitive costs | Coverage needs, releases, retention, regional capacity |
| Revenue and vendor terms | Actual unit definitions and commitments | Price erosion, overages, subsidy expiry, meter changes |

Recalculate the component model for each scenario. Do not multiply several broad “overhead” factors that already include the same retry, retrieval, or review work. Vary the largest uncertain drivers and show the breakpoints that would change the decision.

The **Jevons risk** is that lower unit cost enables enough additional use to increase total spend. It is a possibility to measure, not a law that every optimization increases the bill. Track both cost per useful outcome and total usage. A model swap can be a valid saving if it preserves the required behavior; it is not automatically inferior to routing.

### Vendor units and renewal exposure

For a simple metered contract:

```text
Billable units = max(0, billable activity × units per activity − included units)
Charge = billable units × rate + fixed charges and applicable adjustments
```

Replace this with the actual contract when commitments, tiers, multiple meters, minimums, or credit conversion change the arithmetic. Trace interactions per workflow, units per interaction, price per unit, and usage. Influence over these terms varies; customers can negotiate more than the headline price, and vendors do not control every architecture choice.

Define a reference workload and negotiate unit definitions, measurement rights, change notice, caps, grace periods, rollover, and exit/data-portability terms where worthwhile. An affordability breakpoint is not demand elasticity: elasticity concerns how demand responds to price. Both may inform a renewal.

Garr’s **hypothetical** 10,000-employee example uses five units per interaction, 20,000 included monthly units, and $0.01 per excess unit. At 10% participation and ten interactions each per month, the cost is $300 monthly/$3,600 yearly. At 50% participation it is $2,300 monthly/$27,600 yearly. These small totals do not establish that AI pricing is always immaterial to payroll; workload frequency, products, rates, and internal effort can differ greatly.

Track renewal and pricing dates separately from capability forecasts. Both prices and capabilities can change gradually or abruptly. Assess migration effort, operational fallback, and access to human expertise before retiring a viable substitute. Wages are not an owned balance-sheet asset, and retaining every capability indefinitely is not free; price the option that protects a consequential dependency.

## 5. Compare cost levers at acceptable quality

### Architecture and routing

Compare a simple deterministic or single-model flow, generation plus verification, an iterative harness, and any required human review. A single agent is not necessarily a single call. More agents or a human gate do not guarantee correctness. Choose the smallest design that meets the task’s requirements, and honor the user’s execution constraints.

Anthropic’s March 2026 application-building example compared a $9, 20-minute solo run with a $200, six-hour harness run. That is about 22.2× the reported spend **for that example**, not the universal price of complexity or a prescribed design for high-stakes decisions. [Primary harness report](https://www.anthropic.com/engineering/harness-design-long-running-apps)

Compare incremental cost with measured quality, delay, and the reduction in relevant error exposure. Avoid arbitrary “failure cost is 100× task cost, so upgrade” rules. Required controls remain constraints even when an expected-value estimate favors removing them. Falling escalation alone is not a reliability moat; confirm that correct resolutions increase and harmful misses do not.

Routing can use rules, a lightweight classifier, or a learned policy. This is a menu, not a mandatory sequence. Test actual differences in quality, price, latency, availability, and restrictions. A cheaper model can be useful even when answers are similar; specialization is not the only purpose of routing. Check paraphrases, drift, and misroute-to-rework costs. There is no universal 70–80% easy-query share or 75% routing-accuracy gate. [Routing research](https://arxiv.org/abs/2607.09197)

**Illustrative routing calculation:** 70% of requests at $0.004 + 20% at $0.015 + 10% at $0.05 gives **$0.0108 per request**. Add $0.0005 for routing to get **$0.0113**, a 77.4% reduction from a $0.05 baseline before additional rework and fixed implementation costs. With $200 of fixed cost over the modeled period and no other differences, break-even is 5,168 requests in that period. Validate quality and assumptions before claiming the saving.

| Lever | What to compare | Main check |
|---|---|---|
| Model selection or routing | Full outcome cost across eligible models | Quality, restrictions, fallback, and maintenance |
| Retrieval/embedding changes | Corpus, chunking, search, re-ranking, and context cost | Missing evidence and downstream errors |
| Prompt caching | Prefix writes, reads, expiry, and dynamic input | Actual reuse and provider-specific billing |
| Response caching | Saved computation versus lookup/storage | Identity, freshness, permissions, answer validity |
| Batch processing/review | Throughput and unit cost | Delay, queue behavior, and review quality |
| Bounded loops and early exit | Calls avoided versus unresolved work | Stopping criteria and complete outcomes |
| Hosting/utilization changes | Total ownership versus managed-service cost | Capacity, operations, security, and workload fit |

Rank measured savings against implementation effort and risk. Do not add overlapping percentage savings or assume that users’ inability to see the chosen model makes a downgrade low risk.

### Prompt caching and batch economics

Prompt caching reuses computation for a matching prefix; response caching reuses an answer. They have different correctness and cost implications. Personalization can still leave a reusable prefix, and repeated private sessions may have within-session reuse.

Verify the provider’s read/write rates, minimum prefix, expiry, refresh, isolation, and batch compatibility for the selected model/platform. Do not assume caching is free to populate, lasts only five minutes, is isolated per API key, or eliminates output charges. Anthropic currently documents five-minute and one-hour options and best-effort cache hits in asynchronous batches; model/platform details vary. [Prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

An **illustrative** $3/million ordinary-input rate, $3.75/million cache-write rate, and $0.30/million read rate gives these input costs for 14,000 reusable + 1,000 dynamic tokens:

- No caching: `$0.045` each request.
- Initial write: `$0.0525 + $0.003 = $0.0555`.
- Successful later read: `$0.0042 + $0.003 = $0.0072`.
- One write plus one hit: `$0.0627`, versus `$0.09` without caching—a 30.3% reduction across those two requests. The 84% reduction applies to the hit request’s input cost alone.

Include output and other charges in the final comparison. Measure cache reads and writes over representative traffic. A 70% token hit share is not a universal target; avoid padding prompts merely to make a dashboard look better. Keep version, identity, and invalidation rules correct when data changes.

## 6. Budget evaluation, calculate margin, and decide

Budget evaluation explicitly: examples × repetitions × model/tool cost, plus human calibration, setup, storage, and monitoring. Choose coverage and cadence from consequence, change frequency, detection delay, and evidence needs. Evaluation above 20% of inference cost is not automatically waste. An inexpensive inference path may still need substantial verification.

For illustration, 100,000 production queries/day at $0.015 cost $1,500/day. Evaluating 1% at $0.20 per example costs $200/day, or $6,000 over 30 days—13.3% of $45,000 production inference spend. This example does **not** show evaluation exceeding inference. At one million daily queries with unchanged assumptions, those lines become $450,000 and $60,000 per 30 days.

Use stratified samples, cheaper validated graders, cached unchanged test results, and batch runs where they preserve the required detection. Weight sampled results appropriately for population estimates. Evaluation frequency alone does not guarantee detection within that interval. Preserve necessary coverage; reduce scope or redesign if the required verification cannot be funded.

Calculate matched revenue and costs by segment and in total. Distinguish contribution margin, gross margin under the organization’s cost-of-goods policy, and operating profit after broader expenses. Zero revenue makes percentage margin undefined; show the loss in dollars. P90 cost alone is not a portfolio profitability test.

**Separate margin illustration:** at an assumed all-in service cost of $0.094 per success, ten successes per user-month cost $0.94. For 10,000 users, monthly service cost is **$9,400**, not $94,000. At $20 per user, revenue is $200,000 and the margin on this defined service-cost scope is **95.3%**. A 30% price cut gives $140,000 revenue and **93.3%** on the same scope. Other costs and changed demand must be added before judging overall sustainability.

Use a justified price-downside scenario; 30% is an optional sensitivity, not a forecast. Send `ship-decision` the economics and uncertainty. Negative economics can support a bounded, explicitly funded experiment or subsidy with an owner, loss limit, review date, and exit condition. Do not silently claim profitability or impose a new board approval on every routine decision.

Pricing belongs with `token-economics`: provide the outcome definition, cost distribution, aggregate ratio, volume assumptions, and relevant limits. Expert work can support value beyond a software-seat comparison, but salary budgets are neither uncapped nor universally ten times larger. Value, procurement, alternatives, accountability, and adoption determine the price. For outsourcing or renewal, compare cost, quality, speed, risk, and control, including rights to data, prompts, code, and derived knowledge. Growth and savings are both valid investment paths; do not copy an industry-specific valuation multiple as a universal priority rule.

## Review, dashboard, and handoff

Ask: What counts as success? Which cost is largest and avoidable? Which assumption changes the decision? How are failures and human work counted? What is the complete call multiplier? Does routing improve the actual outcome? How does cache reuse change? What verification is necessary? How concentrated are costs and revenue? What changes at renewal or the next capacity step?

```text
Feature / cohort / period / currency / cost scope:
Total cost and revenue; defined margin or funded loss:
Verified outcomes; failed, pending, reversed, and human-resolved shares:
Aggregate cost per success; mean task cost:
Task-cost P50/P90/P99; account-month distribution and zero-success handling:
Calls/task; input/output/cache usage; background spend:
Model mix; outcome quality; misroute-to-rework cost:
Cache read/write spend; hit definition and observed rate:
Human review time, queue capacity, and escalation outcomes:
Eval/monitoring spend and coverage:
Growth/downside result; largest sensitivity; renewal dates:
Spending limits, owner, next measurement, and decision date:
```

Mark unavailable telemetry as a gap with a measurement plan, not a reason to halt all useful analysis. Spending limits need enforcement, including concurrent work and reporting lag; an alert alone is not a hard cap.

- [ ] Success, cost scope, period, units, and baseline are explicit.
- [ ] All material cost areas, failures, and human work are included without double counting.
- [ ] Fixed, marginal, and capacity-step costs are separated.
- [ ] Totals, branching probabilities, and unit conversions reconcile.
- [ ] Growth and downside assumptions are tested rather than asserted.
- [ ] Routing, caching, and architecture comparisons preserve required quality and controls.
- [ ] Evaluation has a justified budget and coverage plan.
- [ ] Aggregate economics and relevant tail distributions are both visible.
- [ ] Vendor definitions, change dates, and spending controls are understood.
- [ ] `token-economics` and `ship-decision` receive the appropriate evidence and unresolved assumptions.
- [ ] Any intentional loss has the authority, funding, and review conditions required by the decision.

Deliver the recommendation, traceable cost model, leading sensitivity, trade-off, and next action with an owner. Choose a spreadsheet, document, or concise inline table to suit the task. Add a diagram only if it clarifies the cost flow. See the [concept guide](CONCEPT.md) and [evidence notes](references/cost-evidence.md) for examples and corrections.

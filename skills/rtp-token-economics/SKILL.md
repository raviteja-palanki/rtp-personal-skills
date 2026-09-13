---
name: rtp-token-economics
version: v1.4.2_latest
description: "Choose how to charge for an AI product and package its value while keeping customer spending understandable and the business sustainable. Use for launch pricing, a plan change, an enterprise offer, bill shock, or a claim that per-seat pricing no longer works. Compare six model families against willingness to pay, usage and cost distributions, outcome measurability, procurement, and competition. Cover software and labor budgets, bundle/add-on/standalone packaging, discounts, renewal defaults, pricing transitions, and spending controls. Consume full delivery costs from cost-model; assess portfolio contribution, customer-level tail exposure, and growth scenarios without treating a percentile as a universal launch gate. Produce a pricing decision, evidence gaps, a margin analysis, and an implementation plan. Connect to moat-finder, harness-operating-model, adoption-launch, and stakeholder-communications."
imports: [stress-test, falsification]
---

# Token Economics

Choose a price, billing unit, and package that customers understand and that the business can support. AI delivery costs can vary substantially by workload, so assess the joint distribution of customer revenue, usage, quality, and cost. A heavy user is not necessarily the most valuable customer, and a useful pricing model need not follow a universal progression away from seats.

## Start with the commercial decision

Identify the product line, target segment, buyer, payer, use case, alternatives, contract context, and decision owner. Establish whether this is a new offer, a pilot, a negotiated deal, or a change to an existing commitment. Record the currency, geography, tax treatment where relevant, billing period, and effective date of comparisons.

Use available cost and customer evidence. Before launch, create explicit usage and willingness-to-pay hypotheses and test them with a bounded offer; do not release an unpriced product merely to collect thirty days of data. After launch, use enough representative history to capture relevant cycles and tail workloads. Thirty days or six months may help in some businesses but are not universal minimums.

Keep a proposed price separate from authorization to change customer contracts, send announcements, or charge anyone. For existing customers, check obligations and plan migration before recommending implementation.

### Six principles to reason from

1. **Costs are real and may be uneven.** Include the full delivery process, including failed attempts, human work, and support. Examine totals and averages alongside customer and workload tails. A power-law distribution is a hypothesis to test, not a law of AI economics.
2. **The billing unit should fit value and incentives.** Seats, work units, credits, and outcomes each distribute risk differently. Charging for an outcome can reward useful work but can also encourage easy-case selection or gaming. Price need not reproduce every underlying cost.
3. **Find the actual budget and value case.** Software, labor, services, revenue growth, risk reduction, or a combination may fund the purchase. The payer's authority and realized benefit matter more than a presumed tenfold salary-budget ceiling.
4. **Test where pricing power comes from.** Routing, domain context, verification, and workflow integration can improve economics. Models and infrastructure can also differentiate. Open weights do not establish a permanent inference-price floor or make every pass-through service worthless.
5. **Make spend and terms understandable.** Explain inclusions, limits, rates, expiry, and changes in familiar work units. Predictability matters, but some buyers prefer flexible consumption over a fixed commitment.
6. **Make subsidies explicit and bounded.** Measure sustainable contribution and the fixed costs it must eventually cover. A funded pilot, acquisition offer, research service, or cross-subsidized feature can rationally lose money within an approved budget. Do not disguise losses or assume growth will cure them.

## Inputs and shared definitions

Get the cost model from `cost-model`, including model calls, tool and retrieval costs, retries, verification, human review, support, and infrastructure. Distinguish variable delivery costs, fixed costs, and accounting cost-of-revenue treatment. Use the same periods and units on the revenue and cost sides.

Collect or estimate:

- Customer and workload distributions: count, volume, total cost, revenue, P10/P50/P90/P99 where sample size supports them, and known extreme cases.
- Cost per attempted task and per successful outcome, with the success definition and all failed-task costs included in the relevant total.
- Usage mix, routing policy, limits, billing delays, seasonality, and adoption assumptions.
- Willingness to pay, customer value, alternatives, competitive terms, procurement authority, and available budget.
- Actual human/AI responsibilities from `strategy-canvas` and the operating design. Labels such as copilot or agent do not determine pricing by themselves.

**Value metric** is the customer-facing unit being priced. **Meter** is how consumption is counted. **Packaging** is which capabilities and entitlements are sold together. A token, credit, request, agent run, and completed outcome are different units; define their conversion or explain why it varies.

**P90 cost** needs an entity and period: for example, monthly total delivery cost per active account. It is not interchangeable with P90 task cost or a percentile of cost-per-success ratios. Small samples may not estimate P99 usefully. Inspect exceptional workloads directly where necessary.

**Contribution** is revenue less the variable costs defined for the decision. **Gross margin** follows the organization's cost-of-revenue accounting and can differ. Specify both when needed; do not label contribution as gross margin.

## 1. Find the budget and the value being purchased

Identify what the buyer can actually redirect and when. Quantify the value of faster work, greater capacity, improved quality, avoided losses, or new revenue. Include the buyer's remaining human work, implementation effort, and switching costs. Time saved is not automatically cash released or headcount removed.

The earlier software-versus-salary distinction remains useful as a procurement question. The approximate tenfold ratio and requirement to replace a person or create tenfold productivity are not universal facts. A valuable lookup tool can justify a substantial price; an expert-like output may have little realizable value. Labor benefits may still be purchased through the software budget.

Use the work pattern to generate candidates:

| Work pattern | Pricing options to investigate | Main question |
|---|---|---|
| Assistance or copilot, with people acting | Seat, add-on, tier, usage, or hybrid | Does the entitlement fit value and delivery cost across users? |
| Agent performs multi-step work with oversight | Run, credit pool, outcome, subscription, or hybrid | What bounds a run, and who pays for retries and review? |
| Service performs an agreed business function | Work unit, outcome, service fee, commitment, or hybrid | Which result is controllable, observable, valuable, and contractible? |

Services-as-software describes selling completed work rather than only access to a tool. It is an option, not the inevitable destination of every AI business. A better agent may reduce needed seats or create more useful activity; estimate the actual effect.

## 2. Compare the six pricing families

These families overlap. Select a combination for the product line, and explain why it fits better than the next-best alternative.

| Family | Mechanism and useful fit | Risk to resolve |
|---|---|---|
| Hybrid tiered subscription | Predictable recurring price with differentiated entitlements, access, or usage allowances | Hidden limits, confusing upgrades, and expensive included usage |
| Usage-based pricing | Charge per disclosed token, request, work unit, or compute measure; often useful for APIs and variable workloads | Uncertain bills, incentives to consume unnecessarily, and weak linkage to value |
| Credit pools | A purchase or subscription provides credits across capabilities or agent work | Opaque conversion, expiry, changing work per credit, and pooling surprises |
| Outcome-based pricing | Charge for an agreed qualifying result, potentially with a base commitment | Attribution, delayed evidence, disputes, outcome gaming, and delivery-cost risk |
| Seat-based pricing with or without an AI add-on | Price access per user, team role, or licensed entitlement | Value may move away from seats; unlimited promises can expose cost tails |
| Freemium or reverse trial | Free ongoing access or temporary premium access supports acquisition and learning | Acquisition cost, abuse, conversion, cannibalization, and ongoing service cost |

There is no universal ranking of these models. A reverse trial can help users experience value; a permanent free tier can also serve a sound acquisition, public-benefit, or network strategy. A conversion rate below 2–3% does not alone establish failure. Evaluate acquisition economics and the value of the free population.

Compare candidates using three connected inputs:

1. **Cost structure:** variable cost per billable unit, account-period cost, total cost of revenue, and the contribution available at plausible prices. Express cost as a share of revenue or delivery cost with a named denominator. Avoid using token spend divided by gross-margin percentage or a near-zero profit amount as a gate.
2. **Usage distribution:** revenue and cost together, including their correlation. P90/P10, median-to-P99, and Gini can describe inequality; they cannot by themselves decide whether flat pricing works. P10 may be zero. Broad usage can remain affordable when absolute costs are small.
3. **Alternatives and willingness to pay:** compare the full offer, switching costs, quality, risk, and buyer preferences. An absence of direct competitors does not imply unlimited pricing power; manual work, doing less, and doing nothing may be alternatives.

The old 20%/50% cost bands, 2×/5× usage ratios, and Gini thresholds of 0.4 or 0.6 are exploratory prompts, not mandatory pricing rules. Test candidate economics directly.

## 3. Define outcome billing before promising it

The library's **Default-FAIL** principle means an unverified billing claim should not silently become a confirmed billable success. Use explicit states such as pending, qualified, failed, reversed, and disputed. Pending is not necessarily a technical failure.

Agree the observable event, unit boundaries, relevant population, exclusions, attribution, evidence, timing, audit access, and dispute/refund process. Specify duplicates, retries, customer inactivity, reopened cases, human involvement, and outcomes that depend on customer actions. If using a proxy or assumed outcome, state that clearly and evaluate its validity.

An outcome does not have to be a final business result under the vendor's sole control. A useful intermediate result may be billable if both parties agree. Conversely, a discrete output or expensive task is not automatically a clean outcome: diagnosis and legal judgment may be harder to verify than a routine classification. High task volume does not prevent automated outcome metering.

When the agreed result cannot yet be measured reliably enough, mark `OPEN: outcome measurement — [evidence needed]`. Use a defined work-unit, subscription, pilot fee, or another suitable interim model. Do not describe vendor billing definitions as proof of correctness or customer benefit. Current Fin and Agentforce distinctions are in the [case notes](references/cases-and-evidence.md).

## 4. Choose the package separately from the meter

Compare **bundle**, **add-on**, and **standalone** against incremental cost, customer value, separable demand, purchase process, and distribution.

- Bundle when shared access and distribution improve the offer and its economics. Significant variable cost requires an explicit funding or limit design, not necessarily a separate SKU.
- Use an add-on when a distinct entitlement, buyer need, or usage pattern benefits from separate choice and pricing. An improvement to an existing job can justify an add-on.
- Consider standalone when an independent product and purchase experience are useful. It can serve the same buyer as another product; a different buyer is not mandatory.

Questions such as “is this included?” and “what does that cost?” are clues, not willingness-to-pay measurements. Test actual trade-offs and purchasing behavior. The former 5% and 20% cost cutoffs and 59%/23%/18% incumbent-study split do not choose the package for you.

Duolingo's move from a separate math app into its broader app illustrates discovery, sign-in friction, and reuse of product mechanics. It also exposes the whole brand to a weak first experience in a new subject. Shared engineering cost is not the same measure as P90 inference cost. Treat this as an analogy to investigate, not a universal bundling result.

## 5. Design spending controls and service behavior together

Show the buyer the plan price and included credits or requests separately. State what remains unlimited and which usage incurs additional charges. For a Copilot-class plan, distinguish paid subscribers, licensed seats, active users, credits, and completions. Date comparisons and transitions.

Provide controls proportionate to exposure:

- Usage and spend by account, team, feature, or run, with estimated versus invoiced cost and known reporting lag.
- Notifications before an allowance is exhausted, authorized overage options, and clear soft and hard limits.
- A response to limits: pause before starting more work, use an agreed fallback, request additional budget, or finish an already-reserved operation. Consider safe stopping and avoid abandoning consequential work mid-action.
- Bounded agent loops, concurrency and run budgets, retry limits, and approval rules for expensive actions.
- Transparent changes in seat tiers, included capacity, rate cards, and credit conversion. Explain any step change rather than hiding it in an upgrade.

A dashboard alone cannot enforce a cap. Delayed billing and concurrent operations can overshoot it; reserve budgets or define the permitted exposure. Exact real-time billing may be unavailable. Give the buyer an honest estimate and reconciliation process.

Track the whole work equation: **requests × work per request × metered units per work unit × price per unit**, plus fixed and other charges. A model or routing change can increase the bill without changing the nominal unit price. Define representative workloads and re-benchmark rights or change notices where suitable; do not promise a fixed token count for every possible request.

Customer dependence may grow as workflows change and internal substitutes disappear. Include migration, retained competence, alternative suppliers, and exit costs when assessing the customer's value and renewal risk. No single loss of internal expertise establishes a predictable price increase.

## 6. Check contribution, tail exposure, and trade-offs

Reuse `cost-model` calculations rather than creating an inconsistent second model. The minimum decision check is:

```text
Account contribution = account revenue - attributable variable delivery cost
Portfolio contribution = total revenue - total variable delivery cost
Contribution margin % = portfolio contribution / total revenue × 100
Operating result for this model = portfolio contribution - relevant fixed costs
```

Use actual revenue paired with cost for each account or workload. A P90-cost customer is not necessarily a P10-margin customer. Calculate the distribution of contribution directly when possible; never subtract unrelated percentiles and call the result observed margin. With zero revenue, report contribution in money and label the percentage undefined.

Inspect P90/P99 costs, the worst plausible run, portfolio exposure, and 10×/100× scenarios where useful. Specify what scales: customers, usage per customer, complexity, or all three. Include plausible revenue, price, and cost changes. Do not assume revenue stays fixed when customer count grows, or grows when existing users consume more included work.

A negative tail account is not an automatic launch prohibition. Determine whether the loss is bounded, budgeted, understood, and offset in a durable way. An unfunded or unbounded loss requires redesign, a limit, or deferral. Positive contribution also does not prove overall profitability.

Assess quality, cost, and latency together. Quality includes task correctness and relevant harm, not only acceptance without edits. Measure both time to first useful response and time to completed work, using suitable percentiles. These can trade off, but improvements may move all three favorably; no pricing model mechanically “buys two.” One extra attempt adds its actual cost. It doubles a one-attempt cost only when the extra attempt costs the same and other conditions are unchanged.

Routing, caching, batching, context management, and verification may improve economics. Measure their end-to-end effects, including quality and delay. The old 8× routing example, 10–22× harness multiplier, 90% cache saving, and 50% batch saving are workload- or provider-specific, not constants to paste into a price.

## 7. Plan renewal, discounts, and transitions

### Renewal defaults

Assess the full acquisition-to-renewal funnel: trial take-up, paid conversion, genuine repurchase preference, usage value, contribution, cancellation, complaints, and customer understanding. A high observed auto-renewal rate can contain inertia; low usage can still deliver valued availability. Neither is a complete measure of retention.

Miller and Zhang's newspaper research motivates testing the trade-off between easy trial entry and continued subscription. Its former 70–80% repurchase and 50% market-share bands are not universal optima for AI. Do not copy a market leader's default without testing fit, but do not assume the leader is always wrong for a challenger. Clearly disclose recurring charges and cancellation, and check applicable requirements for the actual market before implementation.

### Discounts

Discounts can segment willingness to pay, support access, reward commitment, or reflect lower cost to serve. Four mechanisms to compare are self-selected eligibility or effort; purchase quantity; acquisition channel or moment; and time or market conditions. These categories are the library's synthesis of Rafi Mohammed's discussion.

If a hurdle is the intended mechanism, ask whether it reaches the price-sensitive group without unnecessary friction or exclusion. A discount does not have to be inconvenient to be useful. Volume metering and a volume discount are not automatically duplicate segmentation: assess marginal cost, commitment, elasticity, and contribution. Use clear eligibility and genuine deadlines; avoid manufacturing urgency.

### Pricing transitions

At an early stage, use a bounded pilot, trial, subscription, or hybrid to learn value and demand. During growth, refine entitlements, controls, segmentation, and support. At scale, consider commitments, service fees, or outcome pricing where they improve the offer. These are options, not mandatory stages in a seat-to-outcome progression.

For a change, model affected cohorts, explain old and new bills on representative workloads, provide notice and migration choices, and monitor unexpected charges. Price increases can be justified and reductions can be revised; existing commitments and customer expectations determine the path. Avoid claiming the first price must be permanently correct.

Treat vendor subsidy withdrawals and future dates as scoped contract facts to verify. Caps, rollover, grace periods, and rate concessions have different value for different buyers; quantify them rather than ranking them universally.

## Deliver the pricing decision

```text
PRICING DECISION — [product line, segment, owner, date]
Buyer / payer / budget: [authority, realized value, alternatives]
Value metric / meter / package: [definition, inclusions, chosen family]
Offer: [currency, rate, base fee, allowance, term, overage, expiry]
Selection rationale: [cost distribution, WTP evidence, competitive comparison]
Outcome rules: [qualification, pending states, exclusions, disputes; or N/A]
Economics: [portfolio contribution, fixed costs, account tails, subsidies]
Stress scenarios: [what changes at 10×/100×; exposure and controls]
Spend controls: [visibility, reporting lag, limits, safe stop, authorization]
Renewal / discounts: [rationale, disclosure, eligibility, economics]
Migration / next decision: [affected cohorts, communication, owner, date]
Open questions: OPEN: [decision] — [evidence that would settle it]
```

Return margin assumptions to `cost-model`, launch and migration requirements to `adoption-launch`, and the strategic rationale to `stakeholder-communications`. `harness-operating-model` owns deeper delivery-economics choices; `moat-finder` tests durable pricing power. Use `stress-test` for costly workload scenarios and `falsification` for the assumptions that could overturn the offer.

Close with the recommendation, hypothesis and falsifier, main trade-off, largest risk and mitigation, and next action. Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) for a proportionate trade-off ledger and handoff in the requested format. An optional `excalidraw-svg` matrix or transition diagram can help compare choices; show alternatives rather than an inevitable maturity ladder.

Use relevant local research before broad searching; verify current commercial claims with dated primary sources. Read specific book or article sections when they help resolve the decision. Social posts may supply leads but do not replace evidence or justify invented quotes. Reusable learning can be proposed for the library; a one-off pricing task does not itself require modifying this skill.

See [CONCEPT.md](CONCEPT.md) for corrected worked calculations and [cases and evidence](references/cases-and-evidence.md) for historical claims and source limits.

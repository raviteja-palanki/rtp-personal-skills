# Cost Model — Concept Guide

An AI cost model connects work performed, resources consumed, and useful outcomes delivered. It is a decision model, not just a token calculator. Its value comes from making assumptions visible enough to change before the organization commits to them.

## What can change with scale

Traditional software and AI systems can both have fixed costs, capacity steps, economies of scale, and congestion. Neither must scale linearly. An AI workflow adds important sources of variation: input/output length, model selection, tool loops, retries, verification, and the cost of unresolved tasks.

More users do not necessarily mean a larger context per request. A larger corpus may require a different index without increasing the number of retrieved tokens. More traffic can improve prompt-cache reuse, while a more diverse task mix can reduce response-cache hits. Forecast these drivers separately and check them against actual traffic.

A scenario in which a $2,000 pilot grows from 500 to 15,000 users gives $60,000 by simple proportional scaling. A $150,000 downside case is 2.5 times that estimate, but it needs explicit changes in usage, rates, quality, and operations. Calling it “what AI does at scale” would turn a scenario into an unsupported law.

## Three common blind spots

**The pilot omits recurring work.** A few hand-selected requests may hide preparation, failed attempts, support, and review. Include those costs, but do not apply an automatic 3–5× overhead multiplier. Some products are dominated by inference; others by people, storage, or distribution.

**Average usage hides important segments.** A minority may generate much of the cost, but the distribution need not follow a power law. Examine task and account distributions, usage commitments, and revenue together. A heavy user can be profitable; a low-usage account can still be expensive to acquire and support.

**The team confuses contribution with profit.** A product sold for $10 with $5 of variable serving cost earns $5 contribution per unit before other expenses. Ten times the volume does not turn that arithmetic into a loss. Fixed costs, discounts, acquisition costs, and capacity constraints may change the total result; model them. Compare lifetime value with acquisition cost in consistent monetary units, and track payback as a time measure.

## Example 1: Transcription and summarization

This is a fictional planning example, not a reported company outcome.

At **$0.08 per audio minute**, ten minutes each day costs **$0.80 per day**, or **$24 over 30 days**. A $10 monthly subscription would already fail to cover that serving cost at the assumed usage. The original example’s $0.80 monthly cost mixed daily and monthly units.

If full cost rises to **$0.15 per minute**, ten daily minutes cost **$45 over 30 days**. A customer using 60–120 minutes every day would cost **$270–$540** over the same period. Actual plans may impose usage limits or have different economics; these figures only follow the stated assumptions.

Model the distribution of audio minutes, task retries, inference and storage cost, included usage, and the price paid. Test provider-price changes independently from usage growth. Then compare pricing, limits, routing, product scope, and subsidized access. Do not invent a churn rate or claim that the upper 10% of users drive half the bill without data.

## Example 2: Review capacity constrains an analysis service

A fictional service estimates these costs per analysis:

| Item | Cost |
|---|---:|
| Model processing | $0.12 |
| Human review | $5.00 |
| Logging and audit support | $0.08 |
| Evaluation allocation | $0.15 |
| Test-suite allocation | $0.10 |
| **Total on this scope** | **$5.45** |

At a $10 price, contribution before costs outside this scope is $4.55. The review is part of this product’s chosen or applicable control design; the example does not assert a universal regulation requiring a lawyer to review every AI output.

If five reviewers can each complete 200 reviews monthly, capacity is **1,000 analyses per month**. Buying inference capacity for 10,000 analyses does not remove that constraint. Check arrival variability, review complexity, staffing cost, and queues before treating the nominal capacity as a service guarantee.

Consider improvements in context quality, case routing, preparation, tooling, and review design. Verify that any reduced review effort preserves the required detection and decision quality. A lower escalation rate by itself cannot tell whether the system improved or stopped detecting its mistakes.

## Example 3: A response-cache assumption

Suppose an uncached request costs $0.003 and, for a simplified illustration, a valid response-cache hit has negligible variable compute cost. At a 60% hit rate, expected compute cost is:

`$0.003 × (1 − 0.60) = $0.0012 per request`.

At an 8% hit rate it becomes:

`$0.003 × (1 − 0.08) = $0.00276 per request`.

That is **2.3×**, not 7×. Add cache lookup, storage, invalidation, and maintenance costs to both cases. The old calculation discounted an already discounted baseline a second time.

Response caching also requires a validity rule: identity and permissions, source freshness, policy version, and whether the answer applies to the request. Semantic similarity is not enough when an account, date, or amount changes the answer.

Prompt caching is different: it reuses computation for a matching prefix but still generates an output. It can work even when each user asks a different question. See the main skill’s write-versus-read example before applying a headline cache discount to the entire bill.

## Relate cost to benefit without double counting

For a workflow, compare the complete baseline with the complete AI-assisted process. If a baseline takes 60 minutes and the revised process takes 40 minutes including preparation and review, the measured saving is 20 minutes. Do not subtract those same review minutes again as a separate productivity adjustment.

Released time is capacity. It becomes cash savings only through an actual change in paid resources or spending, and it becomes added output only when work, demand, and downstream capacity permit. Keep customer benefits separate from seller margin.

A modeled counterfactual can be useful when direct observation is impractical. State how it was constructed, test its assumptions, and distinguish it from a measured control. Several estimates from the same data are not independent experiments. A survey ratio is not a universal correction factor.

## Use the model to make a decision

Show costs and outcomes over the intended horizon; report current evidence, a growth case, and downside sensitivities. Revisit the model when usage, architecture, quality, vendor terms, or capacity changes—not because a fixed calendar interval is inherently correct.

An intentionally subsidized feature should have a purpose, funding, loss boundary, and review conditions. A one-off task should justify its full cost. A mandatory control can constrain the options even when its cost is high. A cheaper model, routing policy, or hosting arrangement earns its place by meeting the requirements at a better total cost.

Use the [main skill](SKILL.md) for the process and the [evidence notes](references/cost-evidence.md) for source boundaries and corrected calculations. The underlying disciplines are unit economics, reliability engineering, activity-based costing, and explicit decision-making under uncertainty; do not rely on unverified titles or attribution to establish them.
